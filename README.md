# heat-monitor

A simple command-line tool for checking your system's temperature on Linux.

# FOR LINUX ONLY

This python script can only run on Linux systems because the script is written for POSIX shells, and it relies on lm-sensors.

## Features

- Displays current system temperature
- Uses `lm-sensors` for sensor data
- Works with any shell (Fish, Bash, etc.)
- Minimal and fast

## Installation

Clone the repository:
git clone https://github.com/KrayTik/heat-monitor.git

cd heat-monitor

chmod +x heat-monitor.py

Install lm-sensors if it's not already installed:

# Debian/Ubuntu
sudo apt install lm-sensors

# Arch-based
sudo pacman -S lm_sensors

Run sensor detection:

sudo sensors-detect

Follow the prompts and confirm with "yes" when needed.
# Usage

Run the script:

./heat-monitor.py

To automatically refresh every few seconds:

watch -n 5 ./heat-monitor.py

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Contributing

If you want to improve the script or report an issue, feel free to open a pull request or file an issue.


---

Let me know if you're planning to expand `heat-monitor` with logging, config files, or sensor filtering—happy to add sections for that.
