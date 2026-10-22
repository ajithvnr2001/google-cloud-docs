---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip/
title: Choose a connection option for internal-only VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:19.051328+00:00
---

# Choose a connection option for internal-only VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose a connection option for internal-only VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document provides an overview of the methods that you can use to connect to a Compute Engine virtual machine (VM) instance through its internal IP address. Connecting to a VM using its internal IP address is useful if you isolate VMs from external networks by removing their external IP addresses or restricting inbound traffic to their external IP addresses.

If your VMs have external IP addresses, you can [connect using external IP address](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

## Options

The following table summarizes the SSH options for connecting to VMs through their internal IP addresses.

Method | Best used when  
---|---  
[SSH tunneling with IAP](https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap) | You don't want any external IP address access to any VMs in your project. You can use IAP on all Linux VMs, including bastion host VMs and VMs within projects that use Cloud VPN or Cloud Interconnect.  
[Bastion host VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-using-bastion-host) | You have a specific use case, like session recording, and you can't use IAP.  
[Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/compute/docs/connect/ssh-using-vpn) | Your organization has configured [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect) for their networking needs. Cloud VPN and Cloud Interconnect are separate Google Cloud products that aren't included in Compute Engine pricing.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
