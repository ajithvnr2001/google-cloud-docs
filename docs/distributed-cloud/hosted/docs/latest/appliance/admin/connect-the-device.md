---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device/
title: Connect the laptop to the switch \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:31.500950+00:00
---

# Connect the laptop to the switch  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/connect-the-device/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Connect the laptop to the switch Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for administrators setting up the Google Distributed Cloud (GDC) air-gapped appliance. Since this appliance is built for securely isolated environments, it doesn't have external network access by default. To fully provision the appliance and deploy your software stack, you'll first need to establish a direct, local management connection. By connecting a laptop directly to the top-of-rack (TOR) switch, you'll gain the secure administrative access required to authenticate the hardware, configure your initial network settings, and prepare the device for production.

## Before you begin

Before you power on the device and configure your network, ensure you've completed this crucial step:

  * **[Insert the YubiKeys](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup-prerequisites):** You must insert the provided YubiKeys into the designated servers before starting the boot sequence. These hardware security keys serve as a strict cryptographic requirement—they unlock the encrypted storage volumes and authenticate the hardware while the system starts up. If the YubiKeys aren't inserted properly, the servers won't boot securely. Consequently, you'll be unable to establish an SSH connection or proceed with configuring the device.



## Power on the device

Follow these instructions to connect the laptop to the switch using an adapter and log into the terminal:

  1. Use the included power cables to supply power to the device, and power on all three servers and the TOR switch.

  2. Connect a laptop to the uplink management port (port 10) on the switch.

![Switch](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/admin/images/switch-port10.png)

  3. Set the networking configuration of the laptop:

     1. Set the Internet protocol (IP) address of the link on the laptop to `198.18.0.30`.
     2. The subnet mask is `255.255.255.224`.
     3. The default gateway is `198.18.0.1`.
     4. DNS fields can be left blank, as you must connect to `198.18.0.6` by using the IP address and not a hostname.
  4. Verify that you can access the device by establishing a Secure Shell (SSH) connection to the server assigned the IP `198.18.0.6` using the username `applianceusr` and default password `Bosco08!`.
         
         ssh applianceusr@198.18.0.6
         




## What's next

[Create an input configuration file](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/create-input-ciq)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
