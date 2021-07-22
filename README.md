# Raspberry Pi Thermal Printer Scripts

This repository contains various scripts to print information to a Hoin HOP H58 Thermal Printer Via USB.

# Setup

Clone the repository and run installer.sh:

```
git clone https://github.com/LukePrior/Raspberry-Pi-Thermal-Printer
cd Raspberry-Pi-Thermal-Printer
sudo chmod +x ./installer.sh
sudo ./installer.sh
```

You can run the programs from the code folder:

```
python3 /home/pi/Raspberry-Pi-Thermal-Printer/code/weather.py --api API_KEY
```

You can find the complete installation and setup guide in the Diyode Magazine article.


# Scripts

- Weather Forecast
- News Headlines
- Tweets

# DIYODE Magazine Article

[Printing with Pi](https://diyodemag.com/projects/printing_with_pi_raspberry_pi_thermal_printer_fun)

# License

This project is licensed under the MIT License. This project contains code from the [HOP-H58 58mm Thermal Printer CUPS Driver for RaspberryPi](https://github.com/OkkarMin/HOP-H58-RaspberryPi-Driver) guide.
