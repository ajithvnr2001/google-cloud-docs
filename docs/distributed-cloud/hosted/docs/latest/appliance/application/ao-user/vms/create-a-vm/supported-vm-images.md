---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/supported-vm-images/
title: GDC-supported VM images \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:34.346512+00:00
---

# GDC-supported VM images  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/supported-vm-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  GDC-supported VM images Stay organized with collections  Save and categorize content based on your preferences. 

You can [create a virtual machine (VM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start) using one of the Google Distributed Cloud (GDC) air-gapped appliance-provided images listed on this page. You can also bring-your-own (BYO) custom VM image to use instead. This document provides information on GDC-provided and GDC-supported VM images, as well as instructions to view this list in your GDC air-gapped appliance deployment.

## Before you begin

To get the permissions you need to list and use Google Distributed Cloud air-gapped appliance VM golden images, ask your Project IAM Admin to grant you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) that you have the required permissions.

## List VM images

This section provides information about GDC-supported operating systems.

### List golden images

Before you create a VM using a GDC-provided image, review the list of available images. Refer to the instructions in [View a list of available GDC-provided images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#view-list-images-available).

### List BYO images

You can also use your own custom images to create VM instances. This is useful when you have specific operating system or software configurations that you must use. To create and list BYO images, refer to the instructions in [Create custom images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images).

## GDC-supported operating systems

This section details the operating systems GDC air-gapped appliance VMs support.

### Linux OS

GDC air-gapped appliance supports the following Linux OS images:

OS | Golden Image | Importable  
---|---|---  
Ubuntu 20.04 | Yes | Yes  
Ubuntu 22.04 | Yes | Yes  
Ubuntu 24.04 | Yes | Yes  
RHEL 8 | No | Yes  
Rocky 8 | Yes | No  
SUSE CHost 15.5 | No | Yes  
  
GDC air-gapped appliance supports importing an image from a bootable virtual disk or an existing VM disk only for Linux operating systems. To boot your Linux virtual disks in GDC air-gapped appliance, the disks must run one of the GDC-supported Linux operating systems. GDC air-gapped appliance doesn't support importing a Windows image from a VM disk; instead, you must import Windows images from ISO installation media that you upload to object storage.

### Windows OS

GDC air-gapped appliance supports the following Windows OS images:

OS | Golden Image | Importable  
---|---|---  
Windows Server 2019 Datacenter edition | No | Yes  
Windows 10 | No | Yes  
Windows Server 2022 Datacenter edition | No | Yes  
  
You can import Windows images from ISO installation media. GDC air-gapped appliance installs Windows and creates a bootable image from the resulting disk.

Image import requires that the ISO doesn't prompt for input when booted with Unified Extensible Firmware Interface (UEFI). To create a no-prompt ISO, start from an existing ISO file. Complete the following steps:

  1. Extract the ISO contents using the 7Zip archive management tool:
         
         7z x windows-installation.iso -oiso-unpack
         

  2. Create a new ISO from your extracted ISO using `mkisofs`, substituting in the EFI noprompt binary:
         
         mkisofs -b boot/etfsboot.com -no-emul-boot -c BOOT.CAT -iso-level 4 -J -l -D -N -joliet-long -relaxed-filenames -v -V "Custom" -udf -boot-info-table -eltorito-alt-boot -eltorito-boot efi/microsoft/boot/efisys_noprompt.bin -no-emul-boot -o ISO_NAME.iso -allow-limited-size iso-unpack
         

Replace ISO_NAME with a name for the no-prompt ISO. For example, `noprompt-install`.


**Note:** Image import is only verified on official Microsoft installation media. Other installation ISO files might work if they contain a GDC-provided Windows OS.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
