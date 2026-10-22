---
url: https://docs.cloud.google.com/compute/docs/connect/root-ssh/
title: Connect to Linux VMs as the root user \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:18.865920+00:00
---

# Connect to Linux VMs as the root user  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/root-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Linux VMs as the root user Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to connect to Linux virtual machine (VM) instances as the root user, which enables superuser privileges on the VM. By default, Compute Engine VMs built from [public images](https://docs.cloud.google.com/compute/docs/images#os-details) and most common operating systems don't allow root login with a password over SSH.

An alternative to connecting to VMs as the root user is to run commands through `sudo`, which we recommend instead of enabling root login.

## Supported operating systems

These connection methods are supported for all [public Linux images](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine. For Fedora CoreOS images, you must [set up SSH access](https://docs.fedoraproject.org/en-US/fedora-coreos/tutorial-containers/) before you can use these methods.

## Enable root login

**Note:** We recommend running commands through `sudo` instead of enabling root login.

By default, Compute Engine VMs, set the `PermitRootLogin` parameter to `prohibit-password` or `no` in the `/etc/ssh/sshd_config` SSH configuration file. Enable root login by following the instructions for your VM:

###  OS Login VMs 

Enable root login by doing the following:

  1. [Create an SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). Copy the public SSH key for later.

  2. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) as you usually do.

  3. Change `PermitRootLogin no` to `PermitRootLogin prohibit-password` in the `/etc/ssh/sshd_config` file, by running the following command:
         
         sudo sed -i 's/PermitRootLogin no/PermitRootLogin prohibit-password/g' /etc/ssh/sshd_config
         

  4. Create the `/root/.ssh` directory using the following command:
         
         sudo mkdir /root/.ssh
         

  5. Set permissions on the `.ssh` directory, by running the following command:
         
         sudo chmod 700 /root/.ssh
         

  6. Create the `authorized_keys` file by running the following command:
         
         sudo touch /root/.ssh/authorized_keys
         

  7. Set permissions on the `authorized_keys` file, by running the following command:
         
         sudo chmod 600 /root/.ssh/authorized_keys
         

  8. Paste the public SSH key into the `/root/.ssh/authorized_keys` file.

  9. Restart the `sshd` daemon by restarting the VM, or running the restart command for your VM's operating system. Wait for the VM to reboot, then connect as the root user.




###  Non-OS Login VMs 

Enable root login by doing the following:

  1. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) as you usually do.

  2. Change `PermitRootLogin no` to `PermitRootLogin prohibit-password` in the `/etc/ssh/sshd_config` file, by running the following command:
         
         sudo sed -i 's/PermitRootLogin no/PermitRootLogin prohibit-password/g' /etc/ssh/sshd_config
         

  3. Restart the `sshd` daemon by restarting the VM, or running the restart command for your VM's operating system. Wait for the VM to reboot, then connect as the root user.




## Connect as the root user

After you enable root login, connect to the VM as the root user. If you're connecting to a VM that has OS Login enabled, you must use third-party tools instead of the gcloud CLI.

###  gcloud 

Note: You must use third-party tools to connect as the root user if the VM you're connecting to has OS Login enabled. 

Connect to VMs as the root user by using the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) with `root@` specified before the VM name:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Connect to the VM by running the following command:
         
         gcloud compute ssh \
             --project=PROJECT_ID \
             --zone=ZONE \
             root@VM_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone in which the VM is located
     * `VM_NAME`: the name of the VM



###  Third-party tools 

Connect to VMs as the root user by following the instructions for your VM:

  * **OS Login VMs**

[Connect using third-party tools](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools) and specify the following:

    * **Private key** : the private key that corresponds with the public key that you added to the `authorized_keys` file
    * **Username** : the username must be `root`
  * **Non-OS Login VMs**

    1. [Create an SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys) for the root user. The username for the key must be `root`.

    2. [Add the key for the root user to metadata](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#metadata).

    3. [Connect using third-party tools](https://docs.cloud.google.com/compute/docs/connect/ssh-using-third-party-tools) and specify the following:

       * **Private key** : the private key for the root user

       * **Username** : the username must be `root`




## Troubleshooting

To find methods for diagnosing and resolving failed SSH connections, see [Troubleshooting SSH](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh).

## What's next

  * Learn how to [manage access to VMs](https://docs.cloud.google.com/compute/docs/instances/access-overview).
  * Learn how to [transfer files to VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files).
  * Learn how [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
