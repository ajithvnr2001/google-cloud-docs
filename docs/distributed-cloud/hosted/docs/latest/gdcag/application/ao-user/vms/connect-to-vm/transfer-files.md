---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/transfer-files/
title: Transfer files \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:16.499993+00:00
---

# Transfer files  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/transfer-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Transfer files Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to transfer files to and from a virtual machine (VM) instance in Google Distributed Cloud (GDC) air-gapped.

Use secure copy (SCP) from the command line to transfer files to Google Distributed Cloud air-gapped VM instances. Transferring files between VMs in GDC lets you maintain strict data sovereignty and regulatory compliance while still enabling essential operational workflows.

This document is for developers in platform administrator or application operator groups that manage file transfers to and from VMs in a Distributed Cloud environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

**Important:** You _must already have access management enabled_ to proceed. If you don't, follow the steps in [Guest environment](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-the-os/guest-environment). By default, access management is enabled. You need the following to use the SCP command-line tool to transfer files to VMs: 

  * You must manually manage your SSH keys.
  * You must enable ingress on port 22 for your VM. See the [Enable IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses) page for more information.



The SCP tool uses the same key files that you use to connect to your instances using standard SSH.

**Important:** If you haven't yet applied a public key to your VM instance, create an SSH key pair and add the public key to the VM following the instructions in [Linux (SSH)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm#api).

### Request IAM roles

Contact your IAM Project Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.



All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Transfer files to VMs

Locate the external IP address for the VM to which you want to send files using the instructions on the [Enable IP addresses](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/ip-addresses) page.

Use the SCP tool to copy a file from your workstation to the home directory of the target VM in the following example, which uses a private key at `~/.ssh/my-ssh-key`:
    
    
    scp -i ~/.ssh/my-ssh-key LOCAL_FILE_PATH USERNAME@IP_ADDRESS:~
    

Use the following definitions for your variables.

Variable| Definition  
---|---  
`LOCAL_FILE_PATH`| The name of the local file that you want to upload.  
`USERNAME`| Your username.  
`IP_ADDRESS`| The VM's external ingress IP address.  
  
## Transfer files from a VM

To copy files from a VM to your local workstation, reverse the source and destination variables. The following example shows how to copy a file from your VM to a path on your workstation:
    
    
    scp -i ~/.ssh/my-ssh-key USERNAME@IP_ADDRESS:REMOTE_FILE_PATH LOCAL_FILE_PATH
    

Use the following definitions for your variables.

Variable| Definition  
---|---  
`USERNAME`| Your username.  
`IP_ADDRESS`| The VM's external ingress IP address.  
`REMOTE_FILE_PATH`| The name of the remote file that you want to download.  
`LOCAL_FILE_PATH`| The location on your workstation to which you want to download the file.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
