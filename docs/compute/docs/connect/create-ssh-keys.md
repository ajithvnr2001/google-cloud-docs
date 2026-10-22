---
url: https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys/
title: Create SSH keys \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:20.199847+00:00
---

# Create SSH keys  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/connect/create-ssh-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create SSH keys Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to create an SSH key pair for Compute Engine virtual machine (VM) instances to securely connect to your Compute Engine VM instances.

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create an SSH key pair

If you connect to VMs using the Google Cloud console or the Google Cloud CLI, Compute Engine creates SSH keys on your behalf. For more information on how Compute Engine configures and stores keys, see [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh).

If you connect to VMs using third party tools or OpenSSH, you need to add a key to your VM before you can connect. If you don't have an SSH key, you must create one. VMs accept the key formats listed in the `sshd_config` file.

**Note:** Compute Engine, including the metadata service and OS Login, doesn't restrict or validate the cryptographic algorithm of the SSH keys you upload, for example, RSA, ECDSA, or Ed25519. However, whether you can use a key to connect to a VM depends entirely on the guest operating system's specific SSH configuration.

###  Linux and macOS 

On Linux and macOS workstations, use the [`ssh-keygen` utility](https://man.openbsd.org/ssh-keygen) to create a new SSH key pair. The following example creates an RSA key pair.

Open a terminal and use the `ssh-keygen` command with the `-C` flag to create a new SSH key pair.
    
    
    ssh-keygen -t rsa -f ~/.ssh/KEY_FILENAME -C USERNAME
    

Replace the following:

  * `KEY_FILENAME`: the name for your SSH key file.

For example, a filename of `my-ssh-key` generates a private key file named `my-ssh-key` and a public key file named `my-ssh-key.pub`.

  * `USERNAME`: your username on the VM. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`.

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.




`ssh-keygen` saves your private key file to `~/.ssh/KEY_FILENAME` and your public key file to `~/.ssh/KEY_FILENAME.pub`.

A public key for the user `cloudysanfrancisco` looks similar to the following:
    
    
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... cloudysanfrancisco
    

###  Windows 10 or later 

On workstations with Windows version 10 or later, use the [`ssh-keygen` utility](https://man.openbsd.org/ssh-keygen) to create a new SSH key pair. The following example creates an RSA key pair.

Open Command Prompt and use the `ssh-keygen` command with the `-C` flag to create a new SSH key pair.
    
    
    ssh-keygen -t rsa -f C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME -C USERNAME
    

Replace the following:

  * `WINDOWS_USER`: your username on the Windows machine.

  * `KEY_FILENAME`: the name for your SSH key file.

For example, a filename of `my-ssh-key` generates a private key file named `my-ssh-key` and a public key file named `my-ssh-key.pub`.

  * `USERNAME`: your username on the VM. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`.

For Linux VMs, the `USERNAME` can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a `USERNAME` of `example\cloudysanfrancisco`.




`ssh-keygen` saves your private key file to `C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME` and your public key file to `C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME.pub`.

A public key for the user `cloudysanfrancisco` looks similar to the following:
    
    
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... cloudysanfrancisco
    

###  Windows 8 or earlier 

On workstations with Windows version 8 or earlier, use the PuTTYgen tool to create a new SSH key pair. The following example creates an RSA key pair.

  1. [Download `puttygen.exe`](http://www.chiark.greenend.org.uk/%7Esgtatham/putty/download.html) if you haven't already.

  2. Open PuTTYgen.

  3. Under **Parameters** specify the following:

     * **Type of key to generate** : `RSA`
     * **Number of bits in a generated key** : `2048` or more
  4. Click **Generate** and follow the on-screen instructions.

The tool displays the public key value.

  5. In the **Key comment** section, replace the pre-populated text with your username. For example, `cloudysanfrancisco`, or `cloudysanfrancisco_gmail_com`.

For Linux VMs, the **Key comment** can't be `root`, unless you configure your VM to allow root login. For more information, see [Connect to VMs as the root user](https://docs.cloud.google.com/compute/docs/connect/root-ssh).

For Windows VMs that use Active Directory (AD), the **Key comment** must be prepended with the AD domain, in the format of `DOMAIN\`. For example, the user `cloudysanfrancisco` within the `ad.example.com` AD has a **Key comment** of `example\cloudysanfrancisco`.

  6. Optional: enter a **Key passphrase** to password-protect your key.

  7. Click **Save private key** to choose a location to save the private key to.

PuTTYgen writes the private key to a file with a `.ppk` extension.

  8. Click **Save public key** to choose a location to save your public key to. Keep the PuTTYgen window open.

  9. Copy the text from the **Public key for pasting into OpenSSH authorized_keys file** field.

  10. Open the public key file. The public key has a format similar to the following:
         
         ---- BEGIN SSH2 PUBLIC KEY ----
         Comment: "USERNAME"
         KEY_VALUE
         ---- END SSH2 PUBLIC KEY ----
         

  11. Replace the entire contents of the public key file with the value you copied from the **Public key for pasting into OpenSSH authorized_keys file** field, so that your public key file matches the following format:
         
         KEY_VALUE USERNAME
         




A public key for the user `cloudysanfrancisco` looks similar to the following:
    
    
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAu5kKQCPF... cloudysanfrancisco
    

## What's next?

  * Learn how to [Add SSH keys to VMs](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys)
  * Learn [About SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh) work on Compute Engine



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
