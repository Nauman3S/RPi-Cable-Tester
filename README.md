<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="temp/cableTester.png" alt="Project logo"></a>
</p>

<h3 align="center">RPi Cable Tester</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> RPi Cable Tester
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About <a name = "about"></a>](#-about-)
- [Getting Started <a name = "getting_started"></a>](#getting-started-)
  - [AutoStart on Boot<a name = "Installation"></a>](#autostart-on-boot)
- [Circuit <a name = "circuit"></a>](#circuit-)
  - [Raspberry Pi Pinout](#raspberry-pi-pinout)
  - [Pins Used](#pins-used)
- [Logic Details <a name = "logic"></a>](#logic-details-)
- [Usage <a name = "usage"></a>](#usage-)
- [Demo <a name = "demo"></a>](#demo-)
- [⛏️ Built Using <a name = "built_using"></a>](#️-built-using-)
- [✍️ Authors <a name = "authors"></a>](#️-authors-)


## 🧐 About <a name = "about"></a>

This repo contain files and detailed instructions on running the RPi Cable Tester Program.


## Getting Started <a name = "getting_started"></a>

- This program is tested on Raspbery Pi 3B.
- Copy Firmware folder to the Destkop of your Raspberry Pi.


### AutoStart on Boot<a name = "Installation"></a>

Open the terminal on your Raspberry Pi and execute the following command

- ```sudo nano /etc/rc.local```

Then put the following line before `exit 0` 
-  ```(sleep 5; sh /home/pi/Desktop/Firmware/starter.sh)&```
-   Press CTRL+O and CTRL+X to save and exit.

## Circuit <a name = "circuit"></a>

### Raspberry Pi Pinout

[![PinOut](temp/rpi.png)](https://i.stack.imgur.com/VEBEs.png)

### Pins Used

```bash
Green LED
```
| Raspberry Pi Pin | LED Pin | 
| :---  | :--- |
| `GPIO 12` | LED Possitive |
| `GND` | LED Negative|


```bash
Y-Cable (Connector 1)
```
| Raspberry Pi Pin | Connector | 
| :---  | :--- |
| `GPIO 4` | Connector 1 Pin 1 |
| `GPIO 17` | Connector 1 Pin 2  |
| `GPIO 27` | Connector 1 Pin 3  |
| `GPIO 22` | Connector 1 Pin 4  |
| `GPIO 10` | Connector 1 Pin 5  |
| `GPIO 9` |Connector 1 Pin 6  |

```bash
Y-Cable (Connector 2)
```
| Raspberry Pi Pin | Connector | 
| :---  | :--- |
| `GPIO 11` | Connector 2 Pin 1 |
| `GPIO 5` | Connector 2 Pin 2  |
| `GPIO 6` | Connector 2 Pin 3  |
| `GPIO 13` | Connector 2 Pin 4  |
| `GPIO 19` | Connector 2 Pin 5  |
| `GPIO 26` |Connector 2 Pin 6  |



```bash
Y-Cable (Connector 3)
```
| Raspberry Pi Pin | Connector | 
| :---  | :--- |
| `GPIO 18` | Connector 3 Pin 1 |
| `GPIO 23` | Connector 3 Pin 2  |
| `GPIO 24` | Connector 3 Pin 3  |
| `GPIO 25` | Connector 3 Pin 4  |
| `GPIO 8` | Connector 3 Pin 5  |
| `GPIO 7` |Connector 3 Pin 6  |

## Logic Details <a name = "logic"></a>

-   The program logic for testing cable is simple. Connector 1 is connected to the 6 GPIO pins of Raspberry Pi acting as OUTPUT pins. Connector 2 and Connector 3 are connected to other set of GPIO pins of Raspberry Pi acting as INPUT Pins(with RPi internal PULL-UP Resistors). 
-   Connector 1 pins send signal(LOW) to Connector 2 and Connector 3 INPUT GPIOs and if all the GPIOs of Connector 2 and 3 becomes LOW, the GREEN LED lights up.

Raspberry Pi
## Usage <a name = "usage"></a>

- Copy Firmware folder of this Repo to the Destkop of Raspberry Pi and run the program using the following command
        
        python3 /home/pi/Desktop/Firmware.py

- Or follow `AutoStart on Boot` section of this README to make the program run automatically on Raspberry Pi boot.
- In case of auto boot, a log file is created in logs directory inside the Firmware folder.
## Demo <a name = "demo"></a>

A demo video is present in the root of this repository which tires to mimic a Y-Cable connections and on any broken connection the Green LED turns off. If all connections are correct then the Green LED turns on.
## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - For programming the Watchman Service
  

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development
