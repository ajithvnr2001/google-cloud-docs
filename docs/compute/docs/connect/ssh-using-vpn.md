---
url: https://docs.cloud.google.com/compute/docs/connect/ssh-using-vpn/
title: Connect to Linux VMs using Cloud VPN or Cloud Interconnect \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:41.217861+00:00
---

# Connect to Linux VMs using Cloud VPN or Cloud Interconnect  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/ssh-using-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Linux VMs using Cloud VPN or Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to connect to a virtual machine (VM) instance through its internal IP address, from an on-premises network that uses [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) to connect to the VM's VPC network.

Connecting to a VM using its internal IP address is useful if the VM doesn't have an external IP address. If the VM does have an external IP address, [connect to the VM using its external IP address](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). If your on-premises network isn't connected to your VM's VPC network and you need to connect to your VM's internal IP address, review the other methods listed in [Connection options for internal-only VMs](https://docs.cloud.google.com/compute/docs/connect/ssh-internal-ip).

## Supported operating systems

These connection methods are supported for all [public Linux images](https://docs.cloud.google.com/compute/docs/images/os-details) that are available on Compute Engine. For Fedora CoreOS images, you must [set up SSH access](https://docs.fedoraproject.org/en-US/fedora-coreos/tutorial-containers/) before you can use these methods.

## Connect to VMs

To connect to a VM, complete the steps in one of the following tabs.

###  gcloud 

Connect to a VM using SSH by running the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh) with the [`--internal-ip` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#--internal-ip):

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Connect to the VM by running the following command:
         
         gcloud compute ssh VM-NAME \
             --internal-ip

Replace `VM_NAME` with the name of the VM that you want to connect to.


**Note:** When you connect to VMs using the gcloud CLI, Compute Engine creates a persistent SSH key for you. For more information about SSH keys, see [SSH connections to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/ssh).

###  IAP Desktop 

To connect to a VM using IAP Desktop, do the following:

  1. [Install IAP Desktop](https://github.com/GoogleCloudPlatform/iap-desktop/) on your workstation if you haven't already. 

  2. Open IAP Desktop. The **Add projects** window opens. 

  3. When prompted, sign in using the Google account that has access to the project with the VMs you want to connect to. 

  4. In the **Add projects** window, enter the project ID or name of the project that contains the VMs you want to connect to. 

  5. In the **Project Explorer** window, right-click the name of the VM that you want to connect to and select **Connection settings**. 

  6. In the **Connection settings** window, set **Connect via** to **Vpc**. 

  7. In the **Project Explorer** window, right-click the name of the VM again and select **Connect** to connect to the VM. 




###  OpenSSH clients 

Connect through a VM's internal IP address from an OpenSSH client, by doing the following:

  1. [Add an SSH key to the VM](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) if you haven't already.
  2. In the Google Cloud console, go to the **VM Instances** page and find the internal IP address of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  3. Open a terminal on your workstation.
  4. Connect to the VM by running the following command:
         
         ssh -i PATH_TO_PRIVATE_KEY USERNAME@INTERNAL_IP

Replace the following:

     * `PATH_TO_PRIVATE_KEY`: the path to the private SSH key file that corresponds to the public key you added to the VM.
     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `INTERNAL_IP`: the internal IP address of the VM. 



###  PuTTY app 

Connect through a VM's internal IP address using PuTTY, by doing the following:

  1. [Add an SSH key](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) to the VM if you haven't already.
  2. If your workstation doesn't already have the PuTTY app installed, [download the PuTTY package files](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html).
  3. In the Google Cloud console, go to the **VM Instances** page and find the internal IP address of the VM that you want to connect to.

[Go to VM Instances](https://console.cloud.google.com/compute/instances)

  4. Open the PuTTY app. A connection configuration window opens.
  5. In the `Host Name` field, enter the username associated with the SSH key, and the internal IP address of the VM that you want to connect to. Use the following format:
         
         USERNAME@INTERNAL_IP

Replace the following:

     * `USERNAME`: your username. If you manage your SSH keys in metadata, the username is what you specified when you [created the SSH key](https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys). For OS Login accounts, the username is [defined in your Google profile](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys#os-login). For example, `cloudysanfrancisco_example_com` or `cloudysanfrancisco`.
     * `INTERNAL_IP`: the internal IP address of the VM. 
  6. In the **Category** menu, navigate to **Connection > SSH > Auth**.
  7. In the **Private key file for authentication** field, select the private SSH key file that corresponds to the public key you added to the VM.
  8. Click **Open** to connect to the VM.



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
