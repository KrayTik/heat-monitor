# heat-monitor

[![Linux compatible](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=linux)](https://www.linux.org/)
[![Python](https://img.shields.io/badge/Language-Python-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

A simple, lightweight command-line utility written in Python to display your system's temperature readings on Linux.

## ✨ Features

* Get real-time CPU and other sensor temperatures.
* Leverages the standard `lm-sensors` package for reliable hardware interaction.
* Works seamlessly in any Linux shell (Bash, Zsh, Fish, etc.).
* Minimal dependencies and fast execution.

## ⚠️ Prerequisites

This script is **Linux-only** and requires the `lm-sensors` package to be installed and configured on your system. It will not run on Windows or macOS.

Before using `heat-monitor`, ensure you have:

1.  **Linux Operating System:** Running a distribution like Ubuntu, Debian, Fedora, Arch Linux, etc.
2.  **`lm-sensors` installed:** This package provides the `sensors` command that `heat-monitor` uses internally.
3.  **`lm-sensors` configured:** You need to run `sensors-detect` at least once to identify your system's sensors.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/KrayTik/heat-monitor.git](https://github.com/KrayTik/heat-monitor.git)
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd heat-monitor
    ```

3.  **Make the script executable:**
    ```bash
    chmod +x heat-monitor.py
    ```

4.  **Install `lm-sensors` (if you haven't already):**

    * **Debian/Ubuntu:**
        ```bash
        sudo apt update
        sudo apt install lm-sensors
        ```

    * **Arch-based (Arch Linux, Manjaro, etc.):**
        ```bash
        sudo pacman -S lm_sensors
        ```

    * **Fedora:**
        ```bash
        sudo dnf install lm_sensors
        ```

    * *For other distributions, consult your package manager documentation.*

5.  **Configure `lm-sensors`:** Run the sensor detection utility. Follow the on-screen prompts, typically answering "yes" to probe most buses and load modules when asked.
    ```bash
    sudo sensors-detect
    ```
    After running `sensors-detect`, you might need to restart your system or load the kernel modules manually as instructed to make the sensor data available.

## 🚀 Usage

Navigate to the `heat-monitor` directory or add the script's location to your system's PATH.

* **Run once:**
    ```bash
    ./heat-monitor.py
    ```

* **Watch and auto-refresh (e.g., every 5 seconds):**
    ```bash
    watch -n 5 ./heat-monitor.py
    ```
    This command uses the standard `watch` utility to periodically execute the script and display its output, providing a live view of temperatures. Press `Ctrl+C` to stop `watch`.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements, find a bug, or want to add features, please feel free to:

1.  Open an issue to discuss your ideas or report problems.
2.  Fork the repository, make your changes, and open a pull request.

Please follow standard Python coding conventions and include relevant documentation or comments for your changes.

## 📄 License

This project is open-source and licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
