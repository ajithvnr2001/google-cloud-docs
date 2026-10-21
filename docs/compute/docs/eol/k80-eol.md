---
url: https://docs.cloud.google.com/compute/docs/eol/k80-eol/
title: NVIDIA K80 end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:44:23.908320+00:00
---

# NVIDIA K80 end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/k80-eol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  NVIDIA K80 end of support Stay organized with collections  Save and categorize content based on your preferences. 

In June 2022, NVIDIA announced the upcoming end of support (EOS) of the NVIDIA K80 GPU model. For Google Cloud, NVIDIA K80 GPUs will reach EOS on May 1, 2024.

## What do I need to know

As of May 1, 2024, you won't be able to create or access any VMs that run NVIDIA K80 GPUs.

## How will this EOS impact my existing virtual machine (VM) instances

Until May 1, 2024, your VMs that are running NVIDIA K80 GPUs are not affected.

However, your projects might be at risk because you are running a GPU model that is approaching its EOS. EOS products or features are not supported by Google Cloud.

## What do I need to do

  1. For VMs that have attached NVIDIA K80 GPUs, select another [GPU model](https://docs.cloud.google.com/compute/docs/gpus). **We recommend the NVIDIA L4 GPUs**.
  2. Make a note of the machine type that is supported for the selected GPU model.
  3. Review the available [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) for that GPU model.
  4. Complete _one_ of the following procedures:

     * Move to a new VM.
     * Modify the existing VM: This method is only supported if the new GPU model is available in the same zone, and uses the N1 general- purpose machine type.



### Move to a new VM

You must move to a new VM if the new GPU model is not supported in the zone of the existing VM, or if you are switching to a GPU that runs on an [accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).

To move to a new VM, complete the following steps:

  1. If your existing VM uses Local SSD disks that contain data you want to keep, move the contents of those disks to a Persistent Disk.

  2. [Create a new VM](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) and specify your new GPU model.

**Note:** To reuse most of your configurations from your existing VMs, you can use the [create similar](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance) option. However, remember to update the GPU type.
  3. Move Persistent Disk volumes from the old VM to the new VM. You can do this by detaching the Persistent Disk from the old VM and adding it to the new VM. You can alternatively [transfer files](https://docs.cloud.google.com/compute/docs/instances/transfer-files) from one VM to the other.

  4. Optional: Move the saved data from Persistent Disk volumes back to a Local SSD disk.

  5. [Reassign any static IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) associated with the original VM to the new VM.

  6. [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) on the VM.

  7. Install your applications on the new VM.

  8. Delete the old VM.




### Modify your existing VM

If the new GPU model that you choose is supported in the same zone, and uses the N1 general-purpose machine type, you can modify your existing VM to switch from an NVIDIA K80 to the new GPU model.

  1. [Verify that you have enough quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#check-quota) for the new GPU type.
  2. Verify that all of your critical applications are stopped on the VM.

  3. In the Google Cloud console, go to the **VM instances** page to see your list of VMs.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Click the name of the VM that is running the NVIDIA K80 GPU. The **VM instance details** page opens.

  5. Complete the following steps from the **VM instance details** page.

     1. Click stop **Stop**. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**. Check the notification panel to see when the VM is stopped.

     2. Click edit **Edit** and then complete the following steps:

        1. In the **Machine configuration** section, select the **GPU** machine family.
        2. From the **GPU type** list, change the GPU model from NVIDIA K80 to your new GPU model.
  6. To apply your changes, click **Save**.

  7. To restart the VM, click **Start/Resume**.




## What's next

  * Learn more [about GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).
  * Review [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
