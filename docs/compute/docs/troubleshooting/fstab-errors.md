---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/fstab-errors/
title: Troubleshoot Linux VM boot issues due to fstab errors \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:13.280186+00:00
---

# Troubleshoot Linux VM boot issues due to fstab errors  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/fstab-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot Linux VM boot issues due to fstab errors Stay organized with collections  Save and categorize content based on your preferences. 

Fstab (file system table) is a configuration file that is used to define how disk partition, file system, and file share mounts in your Linux VM persist across system reboots.

This document outlines multiple conditions where an incorrect fstab configuration may result in a boot problem and offers troubleshooting advice to fix the issue.

For other causes of boot failures, and to detect the cause automatically, see [Troubleshoot Linux Compute Engine instance boot issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-linux-boot-issues).

A few of the common issues with fstab misconfiguration are listed below:

  * Syntax error in `fstab` configuration file
  * An incorrect UUID
  * An entry exists for an unattached/unavailable device
  * Deprecated mount options like `nobarrier` for the xfs file system type in [SUSE](https://www.suse.com/c/xfs-nobarrier-option-is-now-more-than-deprecated) or [RHEL](https://access.redhat.com/solutions/5315771) images.



## Before you begin

  * If you want to log serial port output in Cloud Logging, familiarize yourself with [Cloud Logging](https://docs.cloud.google.com/logging).
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Identify fstab issues

For boot issues, Google highly recommendeds that you check the boot logs in the Serial Console of the Linux VM. The VM goes into emergency mode with an error message hinting that the issue is with fstab.
    
    
      [K[[1;31m TIME [0m] Timed out waiting for device dev-incorrect.device.
      [[1;33mDEPEND[0m] Dependency failed for /distribution.
      [[1;33mDEPEND[0m] Dependency failed for Local File Systems.
      ...
      Welcome to emergency mode! After logging in, type "journalctl -xb" to viewsystem logs, "systemctl reboot" to reboot, "systemctl default" to try again to boot into default mode.
      Give root password for maintenance
      (or type Control-D to continue)
      

As per the error message, there is dependency failure for the `/distribution` file system. The dependency failure for a file system mount point will differ based on the file system names used.

## Resolution

Use the following options to solve the `fstab` error in Linux VMs hosted in Google Cloud. You can resolve the issue faster using the serial console than using the manual method.

**Note:** To fix the issue from emergency mode, you must have the root password. By default, a root password is not set on Google provided Linux images. If you didn't set a root password, use Option 2 instead.

To use the following methods to resolve the fstab issue, you must [enable serial port access for your VM](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enable_instance_access).

### Option 1: Use the serial console to log into the VM in emergency mode

  1. Log into the serial console of the VM from Google Cloud console. ![Serial Console](https://docs.cloud.google.com/static/compute/images/fstab1.png)

  2. In the current emergency mode, enter the root password to access your VM.

  3. Use your favorite text editor to open the `fstab` file. Make the necessary changes and save the changes to the `fstab` file. In the following example, the `vi` editor is used.
         
         vi /etc/fstab

![Fstab file](https://docs.cloud.google.com/static/compute/images/fsfile.png)

In the previous example, the device for `/distribution` is detached from the VM. Comment the line that references the file system or remove the fstab entry for `/distribution` mount point.

Use `man fstab` for more details about the fstab configuration and syntax.

  4. Save the file and exit the editor. If you are using the `vi` editor, use `ESC` \+ `:wq!` to save and exit the editor.

  5. Resume the boot process by entering **reboot** at the prompt.

  6. After successfully fixing the issue, the VM boot process should complete and the login prompt appears in the serial console.

  7. Verify you can log in to the VM again using SSH.




### Option 2 - Using Single User mode in Serial Console

This option can be used if the root password is not set.

Prerequisite: The `GRUB_TIMEOUT` parameter in the grub configuration file must be set to a non-zero value. Usually this file is at `/etc/default/grub`, but on some earlier distributions, it might be located in a non-standard directory.

  1. Go to the VM instances page in the Google Cloud console. [Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Log into the serial console of the Virtual Machine from the Google Cloud console. ![Serial Console2](https://docs.cloud.google.com/static/compute/images/fstab2.png)

  3. Click **RESET** for virtual machine from the Google Cloud console.

![Reset file](https://docs.cloud.google.com/static/compute/images/fsreset1.png)

  4. In the serial console window, interrupt the boot process by clicking the arrow key to pause in the grub screen or menu.

  5. In the list of kernels in the grub boot loader screen, choose the kernel and press `e` on the keyboard.

![bootloader file](https://docs.cloud.google.com/static/compute/images/fstabgs.png)

  6. Add the `rd.break` parameter at the end of the kernel line and press `ctrl`+`x`. This helps in booting the VM into single user mode.

![bootloader Menu](https://docs.cloud.google.com/static/compute/images/fsmenu.png)

**Note:** The `rd.break` parameter works for RHEL, CENTOS, Oracle Linux, SUSE Operating Systems. This parameter isn't a persistent entry so no changes are required after boot. For Ubuntu 18.04, 20.04 and 22.04 LTS, you can add `systemd.unit=rescue.target` to boot into rescue mode which is similar to single user mode.
  7. Mount the root file system in read write mode.

  8. Analyze, make necessary change and save `fstab` file. Use `man fstab` for more details about configuration and syntax. Use your favorite text editor to open the `fstab` file. In the below example, the vi editor is used.
         
         vi /etc/fstab

![Fstab file2](https://docs.cloud.google.com/static/compute/images/fsfile2.png)

In this example, the device for `/distribution` is detached from the VM, so comment the line or remove the fstab entry for the `/distribution` mount point.

  9. Save the file and exit from the editor. If you are using the vi editor, then use `ESC` \+ `:wq!` to save and exit from fstab.

  10. Resume the boot process by entering `reboot` at the prompt.

  11. After successfully fixing the issue, the VM boot process should complete and you should see the login prompt in the serial console.

  12. Verify you can log in to the VM using SSH.




### Option 3 - Rescue the VM

This option can be used if the root password is not set or if you can't use single user mode.

For more information, see [Rescue an inaccessible VM](https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
