---
layout: post
title: New feature
author: Migue
tags: [Technology]
---

I was thinking about one of my scripts running in my Raspberry Pi 3. Every hour I receive two e-mails. The first of them is to know how many devices are connected on my local network (more info in the [repo](https://github.com/MAInformatico/Tools)).
     
The second e-mail show me the current temperature of the server, and this is the subject. How can I get more info about the temperature specially now that it is summer time?
Well, I am currently working with Python. So I have think that this language could help me and that's right. Just importing some packages, reading and writing a file and voilà an script that help us to know is the temperature of our device has increase or decrease.
     
##How it's works?
Temperature.py reads a file called temperature.txt that contains the last info about the temperature of our device.
After that, we execute the command: vcgencmd measure_temp to get the current temperature.
Now just we need to compare the two values to know has changed the temperature and write it on the file to attach it and send by e-mail.
     
This is an initial idea, if you have any suggestion it's will be welcome  



#### A day without smile it's a day wasted (Charlie Chaplin)