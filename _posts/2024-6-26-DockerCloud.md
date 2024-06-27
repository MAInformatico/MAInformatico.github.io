---
layout: post
title: Local cloud using Docker
author: Migue
---

Updating my backup policies. I have included a new one: a local cloud.

We get another clouds like Google Drive, Microsoft Onedrive etc. But I prefer to create my own cloud for fun and get control of my data. So after my girlfriend was accepted in her PhD program and remembering some comments about "A PhD student lose its thesis after a computer disaster" and similar situations, I decide to create another backup and prevent it kind of issues.
  

To do that I have used [Nextcloud](https://nextcloud.com/). It is a free software project that allow you to create your own cloud.
  
In my case I have a Raspberry Pi 4 running Raspberry Pi OS (previously called "Raspbian"). You can use a Raspberry Pi for many purpose: enable an access point, monitoring your local network, CI/CD with Jetkins etc. In order to deploy my own cloud I am using [Docker](https://www.docker.com/products/docker-desktop/).
  
Docker allow us to create, test and deploy our apps faster in containers. So our layers are:
Raspberry Pi OS --> Docker --> Nextcloud
By this way, we have allow our device to run more services (using Docker or other tool) and also use it for other purpose.

  
You can follow [this tutorial](https://www.cherryservers.com/blog/install-nextcloud-docker) if you are interested in create your own cloud.
(My suggestion is buy a Raspberry Pi or a similar device if you will use it for personal purpose)
  



> "If you can think it, you can code it"
