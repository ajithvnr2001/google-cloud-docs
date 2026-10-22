---
url: https://docs.cloud.google.com/compute/docs/connect/windows-ssh/
title: Connect to Windows VMs using SSH \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:55.272567+00:00
---

# Connect to Windows VMs using SSH  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/windows-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Windows VMs using SSH Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to connect to Windows virtual machine (VM) instances using SSH. For other ways to connect to Windows VMs, see [Connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) and [Connect to Windows VMs using PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell). To learn about how SSH works in Compute Engine, see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

**Note:** When a user connects to a VM, that user can use all of the IAM permissions granted to the service account attached to the VM. 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




## Supported images

SSH for Windows is supported on [Windows Server images](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) running the guest agent (`GCEGuestAgent`) version `20220527.00` or later and OpenSSH version `8.6` or later.

## Enable SSH for Windows VMs

To enable SSH connections to Windows VMs, install the `google-compute-engine-ssh` package and set the `enable-windows-ssh` key to `TRUE` in project or instance metadata. Enabling SSH for Windows in project metadata enables SSH for all Windows VMs in your project. Enabling SSH for Windows in instance metadata enables SSH for a single VM and overrides the value set in project metadata.

**Note:** If you enable SSH for Windows on a VM running as an Active Directory (AD) controller or in a project that contains an AD controller, the AD controller VM's Guest agent provisions AD users based on SSH keys added to project and instance metadata. You can prevent unintended AD user provisioning by [disabling the account manager](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances#disable_the_account_manager) on the AD controller VM.

### Enable SSH for Windows while creating a VM

Enable SSH for Windows while creating a VM using the Google Cloud console or the Google Cloud CLI.

###  Console 

[Create a VM from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage) that installs the `google-compute-engine-ssh` package and enables SSH on startup:

  1. Specify the following **Boot disk** properties:

     * **Operating system:** Windows Server
     * **Version:** Any version
  2. In the **Advanced options** section, expand the **Management** section.

  3. In the **Metadata** section, click **Add item**. Add a startup script that installs the `google-compute-engine-ssh` package by entering the following metadata key-value pair:

     * **Key:** `sysprep-specialize-script-cmd`
     * **Value:** `googet -noconfirm=true install google-compute-engine-ssh`
  4. In the **Metadata** section, click **Add item**. Set `enable-windows-ssh` to `TRUE` by entering the following metadata key-value pair:

     * **Key:** `enable-windows-ssh`
     * **Value:** `TRUE`
  5. Click **Create** to create and start the VM.




###  gcloud 

Run the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create a Windows Server VM that installs the `google-compute-engine-ssh` package and enables SSH on startup:
    
    
    gcloud compute instances create VM_NAME \
        --image-family=IMAGE_FAMILY \
        --image-project=windows-cloud \
        --metadata sysprep-specialize-script-cmd="googet -noconfirm=true install google-compute-engine-ssh",enable-windows-ssh=TRUE
    

Replace the following:

  * `VM_NAME`: the name of the new VM.
  * `IMAGE_FAMILY`: a [Windows Server image family](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server). This creates the VM from the most recent non-deprecated Windows Server image.



### Enable SSH for Windows on a running VM

To enable SSH on a running Windows VM, do one of the following, depending on whether you can use RDP to access your VM or if your workload can tolerate a reboot:

  * **RDP access required** : Connect to the VM using RDP and install the SSH package
  * **Reboot required** : Use a startup script to install the SSH package




###  RDP 

If you can access your VM using RDP, enable SSH by doing the following:

  1. [Connect to the VM using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows#connecting_to_windows_vms_by_using_rdp).

  2. Open an administrator Command Prompt session by doing the following:

     1. Open the **Start** menu.

     2. Navigate to **Command Prompt**.

     3. Right-click **Command Prompt** and select **Run as administrator**.

If you are prompted to allow Command Prompt to make changes to your device, select **Yes**.

  3. Download and install the `google-compute-engine-ssh` package by running the following command:
         
         googet -noconfirm=true install google-compute-engine-windows && googet -noconfirm=true install google-compute-engine-ssh
         

  4. Close the RDP session.

  5. Enable Windows SSH in metadata by setting the `enable-windows-ssh` key to `TRUE`. For more information about setting metadata, see [Set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).




###  Startup script 

If you can't access your VM using RDP, enable SSH by doing the following:

  1. [Stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

  2. Set the following metadata key-value pairs on the VM to enable SSH. For more information about setting metadata, see [Set custom metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata).

     * SSH package installation metadata:

       * **Key** : `windows-startup-script-cmd`
       * **Value** : `googet -noconfirm=true update && googet -noconfirm=true install google-compute-engine-ssh`
     * SSH enablement metadata:

       * **Key** : `enable-windows-ssh`
       * **Value** : `TRUE`
  3. [Start the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance). The VM might take a few minutes to reboot.




## Connect to VMs using SSH

Connect to VMs using the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):
    
    
    gcloud compute ssh VM_NAME
    

Replace `VM_NAME` with the name of the Windows VM that you want to connect to.

### Connect to VMs that use AD

If the VM you're connecting to uses Active Directory (AD), connect using the following command:
    
    
    gcloud compute ssh DOMAIN\USERNAME@VM_NAME
    

Replace the following:

  * `DOMAIN`: your AD domain. For example the domain of the `ad.example.com` AD, is `example`.
  * `USERNAME`: your AD username. For example, `cloudysanfrancisco`.
  * `VM_NAME`: the name of the Windows VM that you want to connect to.



## What's next?

  * Learn how to [troubleshoot SSH connections](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh#windows-errors).
  * Learn how to [Add SSH keys to VMs](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys)
  * Learn how to [Restrict SSH keys from VMs](https://docs.cloud.google.com/compute/docs/connect/restrict-ssh-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
