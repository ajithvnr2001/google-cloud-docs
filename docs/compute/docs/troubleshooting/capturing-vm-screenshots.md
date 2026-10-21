---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots/
title: Capturing VM screenshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:03:09.940572+00:00
---

# Capturing VM screenshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/capturing-vm-screenshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Capturing VM screenshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes how to capture a screenshot from a virtual machine (VM) instance by using the VM screenshot tool.

Capturing a screenshot from a VM can help you troubleshoot a VM that is not otherwise accessible. For example, a VM might not be accessible if it is booting or has a disk image that is corrupted.

## Windows-based operating systems

VM screenshots can help to troubleshoot failed RDP connections to Windows VMs, by identifying if the instance has started successfully. For information about troubleshooting RDP connections, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp#vm-screenshot).

## Privacy considerations with remote desktop clients

The VM screenshot tool uses the display adapter of the VM to capture a screenshot of the local console session through a remote desktop client. Capturing a screenshot through the local console session might capture sensitive information from the user's desktop or browser.

If you are concerned about exposing sensitive information as part of a screenshot, configure your respective remote desktop client in the following way so that it does not use the local console session:

  * [Chrome Remote Desktop](https://remotedesktop.google.com/): If you are using Chrome Remote Desktop, be sure to enable [Curtain mode](https://support.google.com/chrome/a/answer/2799701) so that it does not connect to the local console session.

  * [Microsoft RDP](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients): RDP clients connect by using [Windows Remote Desktop Services (RDS)](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds). Windows RDS lets RDP clients choose whether to start a new console session or connect to the existing one, and because of this, there might be privacy implications. For information about customizing RDS so that it does not connect to the local console session, see [Supported Remote Desktop RDP file settings](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/rdp-files).




Before sharing screenshots with [Google Support](https://cloud.google.com/support-hub), make sure to review them for sensitive information.

## Before you begin

  * [ Enable virtual displays on your VM](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display). 
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




## Limitations

  * The instance must be in the `RUNNING` [life cycle state](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

  * The maximum rate for capturing screenshots is 20 per second, which is the [API rate limit](https://docs.cloud.google.com/compute/docs/api-rate-limits).

  * You can't initiate a screenshot while one is in progress.

  * You can capture one screenshot at a time.




## Capturing a screenshot from a VM

Use the following procedures to capture a screenshot from a VM.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.getScreenshot`



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. From the **VM instances** page, click the name of the VM instance to capture a screenshot from.

  3. On the **VM instance details** page, click the **Screenshot** tab.

  4. Click **Refresh** to generate a screenshot from the VM. If you have not [enabled a virtual display](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display), the Google Cloud console does not show a screenshot.




###  gcloud 

Capture a screenshot from a VM by using the [`gcloud compute instances get-screenshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances):
    
    
    gcloud compute instances get-screenshot VM_NAME \
      --destination=JPEG_FILENAME \
      --zone=ZONE
    

Replace the following:

  * `VM_NAME`: name of the VM to capture a screenshot from.

  * `JPEG_FILENAME`: optional filename of the jpeg for the screenshot output. If you do not specify a filename, the raw jpeg data is sent to standard output (stdout).

  * `ZONE`: zone of the VM to capture a screenshot from.




###  REST 

With the Compute Engine API, capture a screenshot from a VM by using the [`instances.getScreenshot` request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/getScreenshot):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zo
    nes/ZONE/instances/VM_NAME/screenshot
    

Replace the following:

  * `PROJECT`: ID of the project containing the VM to capture a screenshot from.

  * `ZONE`: zone containing the project.

  * `VM_NAME`: name of the VM to capture a screenshot from.




## Example VM screenshots

### The Compute Engine UEFI loading the boot manager

The following screenshot shows a [Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) VM that is unavailable while the boot manager is loading:

![The UEFI loading the boot manager](https://docs.cloud.google.com/static/compute/images/uefi.png)

![](https://docs.cloud.google.com/static/compute/images/uefi.png)

### Windows Server 2016 Datacenter performing updates

The following screenshot shows a [Windows Server 2016](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) VM that is unavailable while completing updates:

![Windows Server 2016 Datacenter performing updates.](https://docs.cloud.google.com/static/compute/images/updating.png)

![](https://docs.cloud.google.com/static/compute/images/updating.png)

### Windows Server 2016 loading system services

The following screenshot shows a [Windows Server 2016](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) VM that is unavailable while loading system services:

![Windows Server 2016 loading system services.](https://docs.cloud.google.com/static/compute/images/services.png)

![](https://docs.cloud.google.com/static/compute/images/services.png)

### Login screen for Windows Server 2016 Datacenter

The following screenshot shows a [Windows Server 2016](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) VM that has completed startup and is ready to login:

![Login screen for Windows Server 2016 Datacenter.](https://docs.cloud.google.com/static/compute/images/login.png)

![](https://docs.cloud.google.com/static/compute/images/login.png)

### Sysprep process of Windows Server 2019 Core

The following screenshot shows the [sysprep process](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image#create_server_image) of a [Windows Server 2019 Core](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) VM instance:

![Sysprep process for Windows Server 2019 Core.](https://docs.cloud.google.com/static/compute/images/windows-ss-1.png)

![](https://docs.cloud.google.com/static/compute/images/windows-ss-1.png)

### Blue screen error from Windows Server 2016 Datacenter

The following screenshot shows a blue screen error from a [Windows Server 2016 Datacenter](https://docs.cloud.google.com/compute/docs/images) VM instance:

![Blue screen from Windows Server 2016 Datacenter.](https://docs.cloud.google.com/static/compute/images/bsod.png)

![](https://docs.cloud.google.com/static/compute/images/bsod.png)

## What's next

  * Learn how to [collect diagnostic information from a VM](https://docs.cloud.google.com/compute/docs/instances/collecting-diagnostic-information).

  * Learn how to [troubleshoot Windows instances](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-windows).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
