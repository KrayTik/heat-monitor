import psutil
import GPUtil
import tkinter as tk
from tkinter import ttk
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

cpu_history = []
gpu_history = []
MAX_POINTS = 60

def get_cpu_temp():
    temps = psutil.sensors_temperatures()
    for name, entries in temps.items():
        for entry in entries:
            if 'cpu' in entry.label.lower() or 'core' in entry.label.lower() or 'package id' in entry.label.lower() or 'tdie' in entry.label.lower():
                return entry.current
    return None

def get_gpu_temp():
    gpus = GPUtil.getGPUs()
    if gpus:
        return gpus[0].temperature
    return None

def get_fan_speeds():
    fans = psutil.sensors_fans()
    all_rpms = []
    for name, entries in fans.items():
        for entry in entries:
            if entry.current:
                all_rpms.append(entry.current)
    return all_rpms if all_rpms else None

def update_temps():
    cpu_temp = get_cpu_temp()
    gpu_temp = get_gpu_temp()
    fan_rpms = get_fan_speeds()

    if cpu_temp:
        cpu_history.append(cpu_temp)
        if len(cpu_history) > MAX_POINTS:
            cpu_history.pop(0)
        cpu_temp_label.config(text=f"{cpu_temp:.1f}°C")
        cpu_bar["value"] = cpu_temp
        cpu_stats_label.config(text=f"Min: {min(cpu_history):.1f}°C  Max: {max(cpu_history):.1f}°C  Avg: {mean(cpu_history):.1f}°C")
    else:
        cpu_temp_label.config(text="N/A")
        cpu_stats_label.config(text="Min: --  Max: --  Avg: --")

    if gpu_temp:
        gpu_history.append(gpu_temp)
        if len(gpu_history) > MAX_POINTS:
            gpu_history.pop(0)
        gpu_temp_label.config(text=f"{gpu_temp:.1f}°C")
        gpu_bar["value"] = gpu_temp
        gpu_stats_label.config(text=f"Min: {min(gpu_history):.1f}°C  Max: {max(gpu_history):.1f}°C  Avg: {mean(gpu_history):.1f}°C")
    else:
        gpu_temp_label.config(text="N/A")
        gpu_stats_label.config(text="Min: --  Max: --  Avg: --")

    if fan_rpms:
        fan_label.config(text=", ".join(f"{rpm} RPM" for rpm in fan_rpms))
    else:
        fan_label.config(text="Not available")

    draw_graph()
    root.after(1000, update_temps)

def draw_graph():
    cpu_line.set_ydata(cpu_history + [None] * (MAX_POINTS - len(cpu_history)))
    gpu_line.set_ydata(gpu_history + [None] * (MAX_POINTS - len(gpu_history)))
    ax.relim()
    ax.autoscale_view()
    canvas.draw()

root = tk.Tk()
root.title("System Temperature Monitor")
root.geometry("740x350")
root.configure(bg="#1e1e1e")
root.resizable(False, False)
root.eval('tk::PlaceWindow . center')

style = ttk.Style()
style.theme_use("clam")

style.configure("TFrame", background="#1e1e1e")
style.configure("TLabel", background="#1e1e1e", foreground="#e1e1e1", font=("Segoe UI", 11))
style.configure("Value.TLabel", foreground="#00ff99", font=("Segoe UI", 14, "bold"))
style.configure("Stat.TLabel", foreground="#aaaaaa", font=("Segoe UI", 10))
style.configure("TProgressbar", thickness=10, troughcolor="#333333", background="#00ff99")

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(side="left", fill="both")

def add_sensor_section(parent, row, label_text):
    label = ttk.Label(parent, text=label_text)
    label.grid(row=row, column=0, sticky="w")
    
    value_label = ttk.Label(parent, text="Loading...", style="Value.TLabel")
    value_label.grid(row=row, column=1, sticky="e")
    
    bar = ttk.Progressbar(parent, length=200, maximum=100)
    bar.grid(row=row+1, column=0, columnspan=2, sticky="ew", pady=2)

    stat_label = ttk.Label(parent, text="Min: --  Max: --  Avg: --", style="Stat.TLabel")
    stat_label.grid(row=row+2, column=0, columnspan=2, sticky="w", pady=(0, 10))
    
    return value_label, bar, stat_label

cpu_temp_label, cpu_bar, cpu_stats_label = add_sensor_section(main_frame, 0, "CPU Temperature:")
gpu_temp_label, gpu_bar, gpu_stats_label = add_sensor_section(main_frame, 3, "GPU Temperature:")

ttk.Label(main_frame, text="Fan Speed(s):").grid(row=6, column=0, sticky="w", pady=(10, 0))
fan_label = ttk.Label(main_frame, text="Loading...", style="Value.TLabel")
fan_label.grid(row=6, column=1, sticky="e", pady=(10, 0))

graph_frame = ttk.Frame(root, padding=(10, 20))
graph_frame.pack(side="right", fill="both", expand=True)

fig, ax = plt.subplots(figsize=(5.5, 2.5), dpi=100)
fig.patch.set_facecolor('#1e1e1e')
ax.set_facecolor('#2a2a2a')
ax.tick_params(colors='white')
ax.set_title('Temperature History (°C)', color='white')
ax.set_ylim(0, 100)
ax.set_xlim(0, MAX_POINTS)
cpu_line, = ax.plot([None]*MAX_POINTS, label="CPU", color="#00ff99")
gpu_line, = ax.plot([None]*MAX_POINTS, label="GPU", color="#3399ff")
ax.legend(loc='upper right', facecolor='#1e1e1e', edgecolor='#1e1e1e', labelcolor='white')

canvas = FigureCanvasTkAgg(fig, master=graph_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

update_temps()
root.mainloop()
