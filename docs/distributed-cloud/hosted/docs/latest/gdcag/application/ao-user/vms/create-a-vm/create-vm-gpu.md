---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-vm-gpu/
title: Create and start a VM instance with NVIDIA GPUs \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:24:58.244570+00:00
---

# Create and start a VM instance with NVIDIA GPUs  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-vm-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create and start a VM instance with NVIDIA GPUs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Linux-based virtual machine (VM) instance with NVIDIA graphics processing units (GPUs). To perform similar steps on a Windows VM instance, see [Install NVIDIA GPU drivers on a Windows VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/install-nvidia-drivers-win).

A Virtual Machine with GPUs lets you run various GPU-accelerated workloads, for example, artificial intelligence and machine learning.

Virtual machines with GPUs are part of the "accelerator-optimized" A-series machine family, for example, A2 and A3. For more information, see [View VM machine type](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/view-vm-machine-type).

This document is for developers in platform administrator or application operator groups that create VMs in a Google Distributed Cloud (GDC) air-gapped environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

### Prepare the environment

To use gdcloud command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the gdcloud CLI. All commands for Distributed Cloud use the gdcloud or kubectl CLI, and require a Linux environment.

### Request IAM roles

Contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespace.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Create a VM

Create a VM by following the steps outlined in [Create a VM from an image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-image) and select an A-series machine type.

## Install NVIDIA drivers

This section provides steps to install NVIDIA drivers on your GDC VM instance.

### Install the package

Starting with version `v20250809` and later, GDC-provided Ubuntu and Rocky Linux images have NVIDIA drivers preinstalled.

For image versions earlier than `v20250809` and user-provided custom images, install the driver from the GDC package repository. Connect to the VM using SSH and run the command that corresponds to your VM operating system (OS):

###  Ubuntu 
    
    
     sudo apt install nvidia-dkms-570-server-open
    

###  Rocky Linux and RHEL 
    
    
     sudo dnf install nvidia-driver-cuda
    

### Run DKMS

Enable the NVIDIA driver on your VM with the `dkms` command. You only need to perform this task once per VM:
    
    
       sudo dkms autoinstall
    

## Install the CUDA toolkit

The NVIDIA CUDA toolkit is available in the GDC package repositories. Connect to the VM using SSH, then run the command that corresponds to your VM OS:

###  Ubuntu 
    
    
     sudo apt install cuda-toolkit-12-8
    

###  Rocky Linux and RHEL 
    
    
     sudo dnf install cuda-toolkit-12-8
    

## Enable Secure boot and sign drivers

If you need to [enable secure boot](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/secure-vms/secure-boot#enable-secure-boot) on your VM with GPUs, you must sign the GPU drivers. Refer to the instructions for your corresponding OS.

###  Ubuntu 

  1. Connect to the VM using SSH.
  2. Switch to superuser:
         
         sudo su
         

  3. Generate a MOK key if one doesn't already exist:
         
         [ -f /var/lib/shim-signed/mok/MOK.der ] || openssl req -new -x509 -newkey rsa:2048 -keyout /var/lib/shim-signed/mok/MOK.priv \
             -outform DER -out /var/lib/shim-signed/mok/MOK.der \
             -nodes -days 36500 -subj "/CN=DKMS Signing Key/"
         

  4. Enroll the key using `mokutil`:
         
         mokutil --import /var/lib/shim-signed/mok/MOK.der
         

  5. When prompted, create and enter a new password of your choice.

  6. Sign the NVIDIA kernel modules using the MOK:
         
         for module in nvidia nvidia_drm nvidia_modeset nvidia_uvm nvidia_peermem; do
             /usr/src/linux-headers-$(uname -r)/scripts/sign-file sha256 /var/lib/shim-signed/mok/MOK.priv /var/lib/shim-signed/mok/MOK.der $(modinfo -n $module)
         done
         




###  Rocky Linux and RHEL

  1. Connect to the VM using SSH.
  2. Switch to superuser:
         
         sudo su
         

  3. Sign the driver with the key using `dkms autoinstall`:
         
         sudo dkms autoinstall
         

  4. Enroll the DKMS key in MOK:
         
         mokutil --import /var/lib/dkms/mok.pub
         




## Finalize MOK enrollment and verification

To access the MOK management screen, make sure to reboot the VM instance and immediately connect to the serial port. The screen is time sensitive and appears only briefly during the boot process. Specifically, follow these steps:

  1. Reboot the VM instance:
         
         reboot
         

  2. Connect to the VM's serial console. For more information, see [Connect to a serial port](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud-compute-connect-to-serial-port).

  3. Enroll the MOK from the console:

![VM serial console MOK management screen](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/mok-mgmt-pre-screen.png)

![VM serial console MOK management screen with 'Enroll MOK' highlighted](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/mok-mgmt-enroll.png)

You can view the key to make sure it matches the one generated in an earlier step:

![VM serial console MOK management screen with 'Continue' selected](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/mok-mgmt-continue.png)

  4. Enter the password that you selected earlier:

![VM serial console MOK management screen prompting for a password](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/mok-mgmt-pw.png)

  5. Select Reboot from the MOK management menu:

![VM serial console MOK management screen with 'Reboot' selected](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/images/mok-mgmt-reboot.png)

  6. Verify that the NVIDIA driver works by running `nvidia-smi`.

The output displays the GPU status and driver information:
         
         $ nvidia-smi
         Wed Aug 13 00:09:17 2025
         +-----------------------------------------------------------------------------------------+
         | NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.8     |
         |-----------------------------------------+------------------------+----------------------+
         | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
         |                                         |                        |               MIG M. |
         |=========================================+========================+======================|
         |   0  NVIDIA H200                    Off |   00000000:08:00.0 Off |                    0 |
         | N/A   42C    P0            128W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   1  NVIDIA H200                    Off |   00000000:09:00.0 Off |                    0 |
         | N/A   36C    P0            127W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   2  NVIDIA H200                    Off |   00000000:0A:00.0 Off |                    0 |
         | N/A   34C    P0            122W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   3  NVIDIA H200                    Off |   00000000:0B:00.0 Off |                    0 |
         | N/A   40C    P0            128W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   4  NVIDIA H200                    Off |   00000000:0C:00.0 Off |                    0 |
         | N/A   39C    P0            125W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   5  NVIDIA H200                    Off |   00000000:0D:00.0 Off |                    0 |
         | N/A   35C    P0            122W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   6  NVIDIA H200                    Off |   00000000:0E:00.0 Off |                    0 |
         | N/A   39C    P0            128W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         |   7  NVIDIA H200                    Off |   00000000:0F:00.0 Off |                    0 |
         | N/A   35C    P0            121W /  700W |       0MiB / 143771MiB |      0%      Default |
         |                                         |                        |             Disabled |
         +-----------------------------------------+------------------------+----------------------+
         
         +-----------------------------------------------------------------------------------------+
         | Processes:                                                                              |
         |  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
         |        ID   ID                                                               Usage      |
         |=========================================================================================|
         |  No running processes found                                                             |
         +-----------------------------------------------------------------------------------------+
         




## What's next

  * [Supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images)
  * [Create custom images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images)
  * [Import virtual disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/import-virtual-disk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
