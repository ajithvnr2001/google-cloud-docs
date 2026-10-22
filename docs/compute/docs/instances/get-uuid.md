---
url: https://docs.cloud.google.com/compute/docs/instances/get-uuid/
title: Get the UUID of a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:42.072086+00:00
---

# Get the UUID of a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/get-uuid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Get the UUID of a VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document shows you how to get the universally unique identifier (UUID) of a virtual machine (VM) instance by using a tool that is specific to the VM's operating system.

Each VM has a UUID that has the following properties:

  * It is unique among Compute Engine VMs.

  * It is generated from the VM's project ID, zone, and name.

  * It is stable for the lifetime of the VM. If the VM is deleted and recreated in the same project, zone, and with the same name, the VM receives the same UUID.




UUIDs are only available for VMs created on or after October 30, 2014. If you have a VM created before that date, recreate the VM so Compute Engine can assign it a UUID.

## Use operating system tools to get the UUID of a VM

To get the UUID of a VM, run the command that corresponds to the VM's operating system:

###  Linux 

  1. From the Linux VM, run the following [`dmidecode`](http://www.nongnu.org/dmidecode/) command:
         
         sudo dmidecode -t system | grep UUID
         

  2. Verify a response similar to the following:
         
         UUID: 3748eb17-a207-5bc3-aa4f-3113a1b9409d
         




###  Windows (Cmd.exe) 

  1. From the Command Prompt on the Windows VM, run the following [`wmic`](https://docs.microsoft.com/windows/win32/wmisdk/wmic) command:
         
         wmic path win32_computersystemproduct get uuid
         

  2. Verify a response similar to the following:
         
         UUID
         81CBB42C-73A0-9660-6C7D-2FE94627F3A3
         




###  Windows (PowerShell) 

  1. From PowerShell, run the following [Windows Management Instrumentation (WMI)](https://docs.microsoft.com/powershell/scripting/learn/ps101/07-working-with-wmi) command:
         
         (Get-WmiObject -Class Win32_ComputerSystemProduct).UUID
         

  2. Verify a response similar to the following:
         
         81CBB42C-73A0-9660-6C7D-2FE94627F3A3
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
