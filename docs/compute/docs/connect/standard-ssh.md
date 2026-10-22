---
url: https://docs.cloud.google.com/compute/docs/connect/standard-ssh/
title: Connect to Linux VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:55.116750+00:00
---

# Connect to Linux VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/standard-ssh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Linux VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to connect to Linux virtual machine (VM) instances that have external IP addresses by using SSH keys. To learn how to connect to VMs that don't have external IP addresses, see [Connection options for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip). To learn how to connect to Linux VMs using SSH certificates, see [Require SSH certificates for OS Login VMs](https://docs.cloud.google.com/compute/docs/oslogin/certificates).

For information about how SSH connections work in Compute Engine, including SSH key configuration and storage, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

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




## Supported operating systems

These connection methods are supported for all [public Linux images](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine. For Fedora CoreOS images, you must [set up SSH access](https://docs.fedoraproject.org/en-US/fedora-coreos/getting-started/) before you can use these methods.

## Connect to VMs

To connect to a VM, complete the steps in one of the following tabs.

###  Console 

Connect to VMs using [SSH-in-browser](https://docs.cloud.google.com/compute/docs/connect/ssh-in-browser) from the Google Cloud console, by doing the following:

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

![SSH button next to instance name.](https://docs.cloud.google.com/static/docs/images/establish-ssh-connection-1.png)


**Note:** When you connect to VMs using the Google Cloud console, Compute Engine creates an ephemeral SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  gcloud 

Connect to a VM using SSH by running the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Run the following command:
         
         gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VM
     * `ZONE`: the name of the zone that the VM is located in
     * `VM_NAME`: the name of the VM

If you have [set default properties](https://docs.cloud.google.com/compute/docs/gcloud-compute#default-properties) for the Google Cloud CLI, you can omit the `--project` and `--zone` flags from this command. For example:
    
    gcloud compute ssh VM_NAME


**Note:** When you connect to VMs using the gcloud CLI, Compute Engine creates a persistent SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  OpenSSH client 

Connect to a VM using SSH from an OpenSSH client, do the following:

  1. [Add an SSH key to the VM](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) if you haven't already.
  2. In the Google Cloud console, go to the **VM Instances** page and find the external IP address of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  3. Open a terminal on your workstation.
  4. Connect to the VM by running the following command:
         
         ssh -i PATH_TO_PRIVATE_KEY USERNAME@EXTERNAL_IP

Replace the following:

     * `PATH_TO_PRIVATE_KEY`: the path to the private SSH key file that corresponds to the public key you added to the VM.
     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP`: the external IP address of the VM. 



###  PuTTY app 

Connect to a VM using SSH from the Windows PuTTY app, by doing the following:

  1. [Add an SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) to the VM if you haven't already.
  2. If your workstation doesn't already have the PuTTY app installed, [download the PuTTY package files](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
  3. In the Google Cloud console, go to the **VM Instances** page and find the external IP address of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  4. Open the PuTTY app. A connection configuration window opens.
  5. In the `Host Name` field, enter the username associated with the SSH key, and the external IP address of the VM that you want to connect to. Use the following format:
         
         USERNAME@EXTERNAL_IP

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `EXTERNAL_IP`: the external IP address of the VM. 
  6. In the **Category** menu, navigate to **Connection > SSH > Auth**.
  7. In the **Private key file for authentication** field, select the private SSH key file that corresponds to the public key you added to the VM.
  8. Click **Open** to connect to the VM.



###  Secure Shell Chrome app 

To connect to a VM using SSH from the Secure Shell Chrome app, do the following:

  1. [Add an SSH key to the VM](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) if you haven't already.

  2. Install [Secure Shell](https://chrome.google.com/webstore/detail/secure-shell/iodihamcpbpeioajjeobimgagajmlibd) on your Chromebook or Chrome browser if you have not done so already.

  3. In the Google Cloud console, go to the **VM Instances** page and find the external IP address of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  4. Open the Secure Shell in a Chrome browser tab address bar, by doing the following:

     * Type `ssh`.
     * Press `Space`.
     * Press `Enter`.
  5. Click **[New Connection]**.

  6. In the **username** field, enter your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.

  7. In the **hostname** field, enter the external IP address of the VM.

  8. In the **Identity** field, click **Import...** and select the path to the private SSH key file that corresponds to the public key you added to the VM.

  9. Click **[ENTER] Connect** to connect to the VM.




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
