---
url: https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell/
title: Connect to Windows VMs using PowerShell \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:19.275832+00:00
---

# Connect to Windows VMs using PowerShell  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to Windows VMs using PowerShell Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes how to connect to a Windows virtual machine (VM) instance by using PowerShell.

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




## Connect using PowerShell

If you have a Windows workstation with PowerShell, you can connect to your Windows Server instances through a remote PowerShell session.

  1. If you have not created a username and password on the remote Windows instance yet, [create or reset your Windows password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances).

  2. [Add a firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls) that opens port `5986` on the [Google Cloud VPC network](https://docs.cloud.google.com/vpc/docs) where your Windows Server instance is located.

  3. On your local workstation, open the PowerShell terminal.

  4. Optional: You can initialize a variable to hold your user credentials so you do not need to enter them each time you connect to the instance. If you skip this step, you receive a prompt for your username and password later.
         
         $credentials = Get-Credential
         

  5. Choose whether you want to establish an interactive Powershell session, or invoke commands on your Windows Server VM remotely.




### Establish an interactive PowerShell session

To establish a PowerShell session, run the following command:
    
    
    Enter-PSSession -ComputerName IP_ADDRESS -UseSSL -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck) -Credential $credentials

Replace `IP_ADDRESS` with the external IP address, DNS name, or Windows computer name for the instance to which you want to connect.

**Note:** You can find the external IP address of your Windows instance either in the Google Cloud console on the [**VM Instances**](https://console.cloud.google.com/compute/instances) page, or in the Google Cloud CLI by running `gcloud compute instances list`.

After you connect, the command prompt changes to include the IP address of the remote Windows instance. You can now use the terminal to run PowerShell commands on the remote Windows Server instance.

### Invoke commands on your Windows Server VM remotely

As an alternative to the `Enter-PSSession` command, you can run [`Invoke-Command`](https://msdn.microsoft.com/en-us/powershell/reference/5.1/microsoft.powershell.core/invoke-command) with the `-ScriptBlock` flag to execute PowerShell commands on the remote instance without establishing an interactive session.
    
    
    Invoke-Command -ComputerName IP_ADDRESS -ScriptBlock { SCRIPT } -UseSSL -SessionOption (New-PSSessionOption -SkipCACheck -SkipCNCheck) -Credential $credentials
    

Replace the following:

  * `IP_ADDRESS`: the IP address, DNS name, or Windows computer name for the instance to which you want to connect.
  * `SCRIPT`: one or more commands to run on the remote instance. For example, specify `Get-EventLog -log "Windows PowerShell"` to get a list of log events.



## What's next

  * Learn how to [manage access to instances](https://docs.cloud.google.com/compute/docs/instances/managing-instance-access) for multiple users across a project or organization.
  * [Securely connect to VM instances](https://cloud.google.com/solutions/connecting-securely).
  * [Transfer files to your Linux instances](https://docs.cloud.google.com/compute/docs/instances/transfer-files).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
