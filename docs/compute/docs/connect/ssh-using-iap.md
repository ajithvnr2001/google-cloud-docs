---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap/
title: Connect to Linux VMs using Identity-Aware Proxy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:56.556463+00:00
---

# Connect to Linux VMs using Identity-Aware Proxy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Linux VMs using Identity-Aware Proxy Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to connect to a virtual machine (VM) instance through its internal IP address, using [Identity-Aware Proxy (IAP) TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding).

IAP TCP forwarding lets you establish an encrypted tunnel over which you can forward SSH connections to VMs. When you connect to a VM that uses IAP, IAP wraps the SSH connection inside HTTPS before forwarding the connection to the VM. Then, IAP checks if you have the [required IAM permissions](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#grant-permission) and if you do, grants access to the VM.

If you need to connect to a VM that doesn't have external IP addresses and you can't use IAP, review the other methods listed in [Connection options for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip).

## Before you begin

  * [Create a firewall rule](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#create-firewall-rule) to enable connections from IAP.
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

These connection methods are supported for all [public Linux images](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine. For Fedora CoreOS images, you must [set up SSH access](https://docs.fedoraproject.org/en-US/fedora-coreos/tutorial-containers/) before you can use these methods.

## Connect to VMs

To connect to a VM, complete the steps in one of the following tabs.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions included in the [IAP roles](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding#grant-permission).



###  Console 

Tunnel SSH connections through a VM's internal IP address using SSH-in-Browser by doing the following:

**Note:** SSH-in-Browser only uses IAP if the VM doesn't have an external IP address.

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. In the list of virtual machine instances, click **SSH** in the row of the instance that you want to connect to. 

**Note:** When you connect to VMs using the Google Cloud console, Compute Engine creates an ephemeral SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  gcloud 

Tunnel SSH connections through a VM's internal IP address using the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) with the [`--tunnel-through-iap` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#--tunnel-through-iap):

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  1. Connect to the VM by running the following command:
         
         gcloud compute ssh VM-NAME \
             --tunnel-through-iap

Replace `VM_NAME` with the name of the VM that you want to connect to.


**Note:** When you connect to VMs using the gcloud CLI, Compute Engine creates a persistent SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  IAP Desktop 

To connect to a VM using IAP Desktop, do the following:

  1. [Install IAP Desktop](https://github.com/GoogleCloudPlatform/iap-desktop/) on your workstation if you haven't already. 

  2. Open IAP Desktop. The **Add projects** window opens. 

  3. When prompted, sign in using the Google account that has access to the project with the VMs you want to connect to. 

  4. In the **Add projects** window, enter the project ID or name of the project that contains the VMs you want to connect to. 

  5. In the **Project Explorer** window, right-click the name of the VM again and select **Connect** to connect to the VM. 




###  OpenSSH clients 

Connect to a VM that doesn't have an external IP address by using SSH through an IAP tunnel. You can write your own SSH configuration file (`~/.ssh/config`) so that tools like VS Code or OpenSSH client can connect seamlessly.

  1. Generate and propagate your SSH keys by connecting to your VM at least once by running the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):
         
         gcloud compute ssh --project=PROJECT_ID --zone=ZONE VM_NAME --tunnel-through-iap

Verify the connection is successful and then exit.

  2. Open or create the SSH configuration file on your local workstation. This file is typically located at `~/.ssh/config` on Linux and macOS, or `%USERPROFILE%\.ssh\config` on Windows.

  3. Append a configuration entry for your VM by adding the following block to your SSH configuration file:
         
         Host VM_NAME
             HostName VM_NAME
             IdentityFile PATH_TO_PRIVATE_KEY
             ProxyCommand gcloud compute start-iap-tunnel %h %p --listen-on-stdin --project=PROJECT_ID --zone=ZONE --verbosity=warning
             User USERNAME

Replace the following:

     * `VM_NAME`: the name of the VM you want to connect to.
     * `PATH_TO_PRIVATE_KEY`: the path to your private key file, typically `~/.ssh/google_compute_engine`.
     * `PROJECT_ID`: the ID of the project that contains the VM.
     * `ZONE`: the zone where your VM is located.
     * `USERNAME`: the username on the VM (for example, your Google Cloud OS Login username or the metadata username).
  4. Connect to the VM from your local terminal or SSH client by running the following command:
         
         ssh VM_NAME




###  PuTTY app 

Tunnel SSH connections through a VM's internal IP address using PuTTY, by doing the following:

  1. [Add an SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) to the VM if you haven't already.
  2. If your workstation doesn't already have the PuTTY app installed, [download the PuTTY package files](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
  3. In the Google Cloud console, go to the **VM Instances** page and find the name of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  4. Open the PuTTY app. A connection configuration window opens.
  5. In the `Host Name` field, enter the username associated with the SSH key, and the name of the VM that you want to connect to. Use the following format:
         
         USERNAME@VM_NAME

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `NAME`: the name of the VM. 
  6. In the **Category** menu, navigate to **Connection > SSH > Auth**.
  7. In the **Private key file for authentication** field, select the private SSH key file that corresponds to the public key you added to the VM.
  8. In the **Category** menu, navigate to **Connection > Proxy**.
  9. In the **Proxy type** section, select **Local**.
  10. In the **Telnet command, or local proxy command** field, enter the following command:
         
         gcloud.cmd compute start-iap-tunnel VM_NAME PORT_NUMBER --listen-on-stdin --project=PROJECT_ID --zone=ZONE

Replace the following:

     * `VM_NAME`: the name of the VM that you want to connect to.
     * `PORT_NUMBER`: the port that the sshd daemon runs on. The default `PORT_NUMBER` is `22`.
     * `PROJECT_ID`: the project that hosts the VM that you want to connect to.
     * `ZONE`: the zone where the VM is located.
  11. Click **Open** to connect to the VM.



## Troubleshooting

To find methods for diagnosing and resolving failed SSH connections, see [Troubleshooting SSH](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh).

## What's next

  * Learn how to [manage access to VMs](https://docs.cloud.google.com/compute/docs/instances/access-overview).
  * Learn how to [transfer files to VMs](https://docs.cloud.google.com/compute/docs/instances/transfer-files).
  * Learn how [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
