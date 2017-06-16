# RaspIoT
This project is to use a Raspberry Pi to extend my home alarm system to a web of sensors and responses (audio warnings, lights, etc) outside my home, and learn a little git, github, Python, and other stuff along the way.

I have a home alarm and automation system that's easy to set up automations with, but lacks the ability to use relays, and other sensors and technologies outside of its own ecosystem. By integrating it with an RPI, I can take advantage of the flexibility of the GPIO pins, and having a full Linux OS to use. I can remotely control the RPI using an app like Dataplicity or Cayenne, without having to do any port forwarding.

https://mydevices.com/
https://www.dataplicity.com

Status of the alarm system is passed from the alarm system to the RPI via a Zigbee outlet powering on and off when the alarm system changes state, which I use to drive a 3.3V charge to a GPIO input pin.

When the logic I have on the RPI dictates the alarm should be tripped, I can use a GPIO output pin to apply a charge to a zigbee door sensor (reed switch) that reports to the Alarm system. I could in theory have multiple reed switches attached to various GPIO output pins so I can tell exactly what outside my house was tripped, but the Nest cameras will show me that.

The intent is to run a loop that monitors the input pins for the alarm status, and only respond to sensor inputs if/when the alarm is armed, and otherwise lie dormant.
