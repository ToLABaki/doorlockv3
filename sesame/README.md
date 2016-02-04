# Sesame: open the door

These scripts are the low level part of Doorlock's software and are used to open the door directly:

- **dlock-gpio-command**: The command that sends the signal on the GPIO pins to open the door. It uses the `gpio` utility provided by [WiringPi](http://wiringpi.com/). Please use it directly only if you know what you're doing (see below).
- **doorlock**: A wrapper for running `dlock-gpio-command`. It uses `nohup` so the script won't be killed before closing the door. Please use this if you want to open the door from the command-line.
