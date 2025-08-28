# Weather CLI 🌦️

A simple Python command-line tool to fetch real-time weather updates for any city using wttr.in

# Features

1. Get instant weather conditions by entering a city name
2. Lightweight and easy to use
3. Uses the free wttr.in API (no API key required)

Installation
1. Clone this repository:
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli

# Install dependencies:
pip install requests

# Usage
Run the script with Python:
python weather.py
Enter the city name when prompted:
Enter city name: London
Partly cloudy +18°C

# Example Output
Enter city name: New York
Sunny +25°C

Notes
1. This script relies on wttr.in, so an active internet connection is required.
2. The output format is %C (condition) and %t (temperature). You can customize this by editing the format parameter in the URL.

# License

This project is licensed under the MIT License.
