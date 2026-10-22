---
url: https://docs.cloud.google.com/compute/docs/instances/transfer-files-windows/
title: Transfer files to Windows VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:35.268992+00:00
---

# Transfer files to Windows VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/transfer-files-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Transfer files to Windows VMs Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

To transfer files to Compute Engine virtual machine (VM) instances, different options are available depending on your workstation OS and the target instance OS.

Transfer from | To Windows instances  
---|---  
Linux | 

  * Cloud Storage
  * Google Cloud CLI

  
Windows, macOS, or Android | 

  * Cloud Storage
  * Google Cloud CLI
  * RDP Client

  
  
## Transferring files through Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage) buckets can be used as a transfer point between you and your VMs. You can use a web browser, the Google Cloud CLI, or a programming language to transfer files between Cloud Storage and Compute Engine VMs. 

Different credential types can be used for the upload and download step to best suit your needs: 

  * [Accessing data on a user's behalf](https://docs.cloud.google.com/storage/docs/user-accounts) is best for single use operations, or resources that you are primarily responsible for. 
  * Consider [ service account credentials](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using) for scaled deployments and shared resource scenarios. 



To use Cloud Storage to transfer files between a computer and a VM, do the following: 

  1. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) if you don't have an existing bucket to use for file transfers. 
  2. [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to modify the access to the bucket: 
     * Accounts uploading file(s) to the bucket should have the **Storage Object Admin** granted. 
     * Accounts downloading file(s) should have the **Storage Object Viewer** role granted. 
  3. Log in to the source device and [upload the files](https://docs.cloud.google.com/storage/docs/uploading-objects) to the bucket. 
  4. Log in to the destination device and [download the files](https://docs.cloud.google.com/storage/docs/downloading-objects) from the bucket completing the file transfer. 
  5. Optional: [Delete files](https://docs.cloud.google.com/storage/docs/deleting-objects) that you no longer need to prevent any unwanted storage charges. 



If you need to transfer files in the other direction, you can reverse the process. Ensure that the account uploading the file has write access to the bucket. 

## Transfer files using the Google Cloud CLI

**Note:** Transferring files using the Google Cloud CLI is only supported on VMs running Windows Server 2019 and later. 

Google Cloud CLI provides a Secure Copy Protocol (SCP) file transfer utility over an established SSH connection. 

To transfer files using SCP, do the following: 

  1. [Enable SSH](https://docs.cloud.google.com/compute/docs/connect/windows-ssh) on your Windows VM if it's not already enabled. 
  2. [Review your firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#listing-firewall-rules-vpc) and confirm that SSH connections in on port `22` are permitted; if not [create a SSH firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#common-use-cases-allow-ssh). 
  3. Ensure [gcloud CLI is installed](https://docs.cloud.google.com/sdk/docs/install) on the source device containing the files to be transferred. 
  4. Use the `[gcloud compute scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp)` command to transfer the files to the destination machine. 



The following example copies a file from your workstation to the home directory of the VM:
    
    
    gcloud compute scp LOCAL_FILE_PATH VM_NAME:REMOTE_DIR
    

Replace the following:

  * `LOCAL_FILE_PATH`: the path to the file on your machine
  * `VM_NAME`: the name of your VM
  * `REMOTE_DIR`: a directory on the remote machine



You can also copy files and directories in reverse from the remote machine. The following example recursively copies a directory from the source to the destination:
    
    
    gcloud compute scp --recurse VM_NAME:REMOTE_DIR LOCAL_FILE_PATH
    

For more information, see the [ `gcloud compute scp` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/scp).

## Transferring files through the Windows RDP client

Many first party [Microsoft RDP Clients](https://docs.microsoft.com/windows-server/remote/remote-desktop-services/clients/remote-desktop-clients) support connecting local storage to a remote Windows VM; however this is not supported on all clients.

Follow the instructions for the operating system of the device you're transferring files to or from:

###  Windows 

Transfer files through the built-in Remote Desktop Connection app (`%systemroot%/system32/mstsc.exe`) by doing the following:

  1. Open the **Remote Desktop Connection** application.
  2. Expand **Show Options**.
  3. Click the **Local Resources** tab.
  4. Under **Local devices and resources** , click **More**.
  5. Select the **Drives** checkbox, or pick your chosen drive.
  6. Connect and login to the VM as you would normally.
  7. Open **File Explorer** on the remote machine and see your drive mounted.
  8. Use this drive for file transfers while you are connected.



###  macOS 

Transfer files through the [Remote Desktop Microsoft RDP Client for macOS](https://apps.apple.com/app/microsoft-remote-desktop/id1295203466) by doing the following:

  1. Click the **+** icon in the top left.
  2. Select **Add PC**.
  3. Under the **Folders** tab, enable **Redirect folders**.
  4. Press **+** icon in the bottom left.
  5. Choose a folder that you would like redirected.
  6. Connect and login to the VM as you would normally.
  7. Open **File Explorer** on the remote machine and see your folder mounted.
  8. Use this drive for file transfers while you are connected.



###  Android 

Transfer files through the [Remote Desktop](https://play.google.com/store/apps/details?id=com.microsoft.rdc.androidx) app from Microsoft.

  1. Press the **+** icon in the top right.
  2. Select **Add PC**.
  3. Under **Device & Audio Redirection**, enable **Storage**.
  4. Connect and login to the VM as you would normally.
  5. Open **File Explorer** on the remote machine and see your storage mounted.
  6. Use this drive for file transfers while you are connected.



## What's next

  * [Connect to your VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) to use the files that you transferred.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
