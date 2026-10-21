---
url: https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac/
title: Connect to a Windows VM's SAC \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:18.695203+00:00
---

# Connect to a Windows VM's SAC  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Connect to a Windows VM's SAC Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

This document describes how to connect to the [Windows Special Administration Console](https://technet.microsoft.com/en-us/library/cc787940) (SAC). The SAC uses a serial port connection to a Windows virtual machine (VM) instance and doesn't rely on network connectivity, which can help troubleshoot or recover a Windows VM instance. By connecting to the VM's serial console and using the SAC, you can interrupt the VM's boot process or gain access to a CMD or PowerShell terminal to perform troubleshooting. For a general purpose remote desktop experience other than troubleshooting, [connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

## Before you begin

  * Before you can connect to your VM's SAC by using the interactive serial console, enable interactive access for your VM. For more information, see [Enabling interactive access on the serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-using-serial-console#enabling_interactive_access_on_the_serial_console).
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


**Caution:** The interactive serial console does not support IP-based access restrictions such as IP-based include lists or exclude lists. If you enable the interactive serial console on an instance, anyone from any IP address is able to connect if they know a local username, project ID, zone, and instance name.

## Connect to the Serial Console

To connect to your Windows instance using an interactive serial console, complete the steps in one of the following tabs.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.setMetadata` on the VM if enabling interactive access on a specific VM 
  * `compute.projects.setCommonInstanceMetadata` on the project, if enabling interactive access for all VMs in the project 
  * `iam.serviceAccountUser` role on the instance's service account 



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM you want to connect to.

  3. Click **Connect to serial console** to open the interactive console.




The interactive serial console opens. It's ready to use when you see the following output:
    
    
    Computer is booting, SAC started and initialized.
    
    Use the "ch -?" command for information about using channels.
    Use the "?" command for general help.
    
    SAC>
    

If the interactive serial console is a blank screen with a blinking cursor, it is likely because the [Emergency Management Services](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/boot-parameters-to-enable-ems-redirection) are off. See [troubleshooting interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#troubleshooting-interactive-serial-console) to learn how to resolve this issue.

###  gcloud 

Use the [`gcloud compute connect-to-serial-port` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/connect-to-serial-port) to connect to VM instances that have serial port access enabled:
    
    
    gcloud compute connect-to-serial-port VM_NAME \
        --port=2 \
        --zone=ZONE \
        --project=PROJECT_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VM
  * `ZONE`: the name of the zone in which the VM is located
  * `VM_NAME`: the name of the VM



The interactive serial console opens. It is ready to use when you see the following output:
    
    
    Computer is booting, SAC started and initialized.
    
    Use the "ch -?" command for information about using channels.
    Use the "?" command for general help.
    
    SAC>
    

If the interactive serial console is a blank screen with a blinking cursor, it is likely because the [Emergency Management Services](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/boot-parameters-to-enable-ems-redirection) are off. See [troubleshooting interactive serial console](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#troubleshooting-interactive-serial-console) to learn how to resolve this issue.

For information about using the interactive serial console, see the Microsoft [SAC Commands documentation](https://technet.microsoft.com/en-us/library/cc787940#sac-commands).

## Open Command Prompt in Windows SAC

To open Command Prompt in the SAC, do the following:

  1. Type `cmd`, then press **Enter**. You see the following output:
         
         SAC>cmd
         The Command Prompt session was successfully launched.
         SAC>
         EVENT:   A new channel has been created.  Use "ch -?" for channel help.
         Channel: Cmd0001
         SAC>
         

  2. Use the `ch -sn CHANNEL_NAME` command, then press **Enter**.
         
         ch -sn CHANNEL_NAME
         

Replace `CHANNEL_NAME` with the name of the channel you created in the previous step.

The output is similar to the following:
         
         Name:                  Cmd0001
         Description:           Command
         Type:                  VT-UTF8
         Channel GUID:          28de7392-5413-11ea-bb03-c9656a2ed613
         Application Type GUID: 63d02271-8aa4-11d5-bccf-00b0d014a2d0
         
         Press <esc><tab> for next channel.
         Press <esc><tab>0 to return to the SAC channel.
         Use any other key to view this channel.
         

  3. Press **Space** , then login with the local credentials registered on the system.
         
         Please enter login credentials.
         Username: USERNAME
         Domain: DOMAIN (leave blank if no domain)
         Password: PASSWORD
         

**Note:** If you are unsure of the credentials, you might be able to [create or reset the password](https://docs.cloud.google.com/compute/docs/instances/windows/creating-passwords-for-windows-instances).

Once connected, you have access to a Command Prompt shell.
         
         Microsoft Windows [Version 10.0.14393]
         (c) 2016 Microsoft Corporation. All rights reserved.
         
         C:\Windows\system32>
         

  4. Optional: To enter a Powershell prompt, type `powershell.exe`, then press **Enter**.

**Note:** Pasting into the SAC Powershell terminal might result in repeated characters in the pasted text. You can prevent this on a per-session basis by issuing the `Remove-Module PSReadLine` command in your terminal.



## What's next

  * Learn how to [connect to Windows VMs using RDP](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)
  * Learn how to [troubleshoot Interactive Serial Console ](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows#troubleshooting-interactive-serial-console).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
