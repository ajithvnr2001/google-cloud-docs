---
url: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance/
title: Create a VM similar to an existing VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:40.674881+00:00
---

# Create a VM similar to an existing VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a VM similar to an existing VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to create a virtual machine (VM) instance that has properties similar to an existing VM using the Google Cloud console.

If you have a VM with properties that you want to reuse, then you can create a VM based on it. You can create the VM by using the same properties as the reference VM or by modifying them. This is useful when you need to quickly create a VM, such as in the following scenarios:

  * Rapid deployment

  * Scaling

  * Testing

  * Disaster recovery


**Important:** When creating the VM, the Google Cloud console uses the reference VM's properties. However, the Google Cloud console doesn't copy any data from the reference VM or from any Persistent Disk volumes attached to it.

## Create a VM similar to an existing VM

To create a VM with similar properties to an existing VM, do the following:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the **Name** column, click the name of an existing VM which you want to use to create your VM.

The **VM instance details** page opens.

  3. Click **Create similar**.

![The Create similar button in the Google Cloud console.](https://docs.cloud.google.com/static/compute/images/create-similar.png)

The **Create an instance** page opens. By default, the Google Cloud console specifies the same properties as the reference VM.

  4. Customize the properties of the VM.

**Note:** To view the equivalent Google Cloud CLI, Compute Engine API, or Terraform code to create the VM, click **Equivalent code**.
  5. Click **Create**.




## Troubleshoot

If you encounter issues when creating VMs, then see [Troubleshoot creating, updating and deleting VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-vm-creation).

## What's next

  * [Add persistent disks to the new VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk)
  * [Transfer files to the new VM](https://docs.cloud.google.com/compute/docs/instances/transfer-files)
  * [Create a VM from an image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#startinginstancewithimage)
  * [Create a VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template)
  * [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
