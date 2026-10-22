---
url: https://docs.cloud.google.com/compute/docs/virtual-workstation/
title: About creating virtual workstations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:22.507752+00:00
---

# About creating virtual workstations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/virtual-workstation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About creating virtual workstations Stay organized with collections  Save and categorize content based on your preferences. 

A virtual workstation is a cloud-based workstation that users can access from anywhere by using an internet connection. The concept of remote computing dates back to the 1960s with so-called [dumb terminals](https://wikipedia.org/wiki/Computer_terminal). But a virtual workstation that's built using modern cloud infrastructure is a powerful, economical alternative to an expensive workstation at the user's desk.

With a virtual workstation, there is no capital expense. You can customize the size and power of the virtual workstation to the exact specifications required for a particular task. You only pay for the resources used, when they're used, and you're billed by the second.

You don't pay for electricity to power the workstation or for the [HVAC](https://wikipedia.org/wiki/HVAC) to keep it cool. You also don't have to pay a staff of IT professionals to build physical workstations, upgrade components, add RAM, or swap out disks; all of this is managed by Google Cloud.

## Choose a virtual workstation

When you create a virtual workstation, you can choose from resource configurations such as number and type of CPUs, amount of RAM, type and size of disk, and whether or not to attach GPUs. You can also choose your operating system, like Windows or Linux.

Your intended workload can help you determine how to build your virtual workstation. The following table lists options for creating a virtual workstation.

Task | Tutorials | Use cases  
---|---|---  
Create a virtual workstation |  [Ubuntu 22.04](https://docs.cloud.google.com/compute/docs/virtual-workstation/linux)   
  
[Windows Server 2022](https://docs.cloud.google.com/compute/docs/virtual-workstation/windows) |  Workloads that don't require graphics, or have low graphics requirements. These workstations are useful for migrating legacy business applications to the cloud. The tutorials for this option use HP Anyware Software to stream the desktop to a client for viewing.   
Create a virtual GPU-accelerated workstation  |  [Ubuntu 22.04](https://docs.cloud.google.com/compute/docs/virtual-workstation/linux-gpu)   
  
[Windows Server 2022](https://docs.cloud.google.com/compute/docs/virtual-workstation/windows-gpu) |  Workloads that include graphics-intensive applications that require hardware acceleration, high color accuracy, and support for external peripherals. The tutorials for this option use Teradici Cloud Access Software to stream the desktop to a client for viewing.  
  
These workstations are used in industries such as media and entertainment, architecture, science, and manufacturing.  
Set up Chrome Remote Desktop |  [Debian](https://docs.cloud.google.com/solutions/chrome-desktop-remote-on-compute-engine)   
  
[Windows Server 2022](https://docs.cloud.google.com/solutions/chrome-desktop-remote-windows-compute-engine) |  Workloads for users who need only a low-cost way to access a cloud workstation from a Chrome browser, or workloads where bandwidth or security limitations prevent the installation of third-party software.  
  
## Create a virtual workstation using Google Cloud Marketplace

If you don't want to build your own virtual workstation using one of the tutorials listed earlier, you can use a preconfigured virtual workstation solution on [Cloud Marketplace](https://console.cloud.google.com/marketplace). These solutions offer a quick way to create a virtual workstation that has features like graphics drivers and remote desktop software already installed.

Solution | Available deployments | Details  
---|---|---  
NVIDIA RTX Virtual Workstation |  [RHEL 9](https://console.cloud.google.com/marketplace/product/nvidia/nvidia-rtx-virtual-workstation-rhel-9)  
  
[Ubuntu 22.04](https://console.cloud.google.com/marketplace/product/nvidia/nvidia-rtx-virtual-workstation-ubuntu-22)  
  
[Windows Server 2019](https://console.cloud.google.com/marketplace/product/nvidia/nvidia-quadro-vws-win2019)  
  
[Windows Server 2022](https://console.cloud.google.com/marketplace/product/nvidia/nvidia-rtx-virtual-workstation-windows-server-2022) | Includes NVIDIA RTX Virtual Workstation (vWS) driver software for visualization-capable GPUs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
