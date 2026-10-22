---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-hsm-network-connection/
title: Configure external HSM network connection \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:19.599867+00:00
---

# Configure external HSM network connection  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/configure-hsm-network-connection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Configure external HSM network connection Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up the network for the external HSM connection.

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

## Before you begin

[Configure the device and install software](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/setup)

## Connect the external HSM

  1. Connect one of the ethernet ports on the HSM device to port number 11 on the TOR switch. This is a 10G port. Use the following optic and fiber cable:

     * Optic type: 10GBASE - SR
     * Fiber type: Multimode fiber



## Configure the HSM specs

  1. Configure the following IP on the port on HSM device:

     * IP address: `198.18.2.20`
     * Subnet mask: `255.255.255.0`
  2. The default gateway for the HSM device should be set at `192.168.2.1`.




## Configure the TOR switch

### SSH in to the TOR switch

  1. Get the password. Run the following command on the root-admin-node (BM03):
         
         release/gdcloud system network troubleshoot list --switch-login-info --kubeconfig /root/release/root-admin/root-admin-kubeconfig
         

  2. Connect a laptop to the uplink management port (port 10) on the switch. As this port is an access port, there is no need to set VLAN tags.

  3. Establish a Secure Shell (SSH) session to the TOR by entering `ssh admin@198.18.0.1`.




### Configure the switch ports

  1. Go to the configuration mode as follows:
         
         switch [standalone: master] > enable
         switch [standalone: master] # configure terminal
         switch [standalone: master] (config) #
         

  2. Enter the following configuration:
         
         switch [standalone: master] (config) # interface ethernet 1/11 switchport access vlan 100
         

  3. Save the configuration:
         
         switch [standalone: master] (config) # write memory
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
