---
url: https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows/
title: Format and mount a non-boot disk on a Windows VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:17.755767+00:00
---

# Format and mount a non-boot disk on a Windows VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Format and mount a non-boot disk on a Windows VM Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

If you attached a new, blank disk to your VM, before you can use it you must format and mount the disk. If you attached a disk that already contains data, then you must mount the disk before you can use it.

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




## Connect to the VM

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the **RDP** button next to the VM that has the new blank disk attached. The browser opens an RDP connection to the instance.




## Format and mount a non-boot disk on a Windows VM

Use the [Windows Disk Management utility](https://learn.microsoft.com/windows-server/storage/disk-management/initialize-new-disks) to format and mount the new disk on a Windows VM.

  1. Right-click the Windows Start button and select **Disk Management**.

![Selecting Disk Management by right-clicking the Windows Start button.](https://docs.cloud.google.com/static/compute/images/start_disk_manager_windows.png)

  2. Disk Management prompts you to select a partitioning scheme for the new disk. Select **GPT** and click **OK**.

![Selecting a partition scheme in the disk initialization window.](https://docs.cloud.google.com/static/compute/images/initialize_disk_windows.png)

  3. After the disk initializes, right-click the unallocated disk space and select **New Simple Volume**.

![Creating a New Simple Volume from the attached disk.](https://docs.cloud.google.com/static/compute/images/pd_new_volume_windows.png)

  4. Follow the instructions in the **New Simple Volume Wizard** to configure the new volume. You can use any partition format that you like, but for this example select `NTFS`. Also, check **Perform a quick format** to speed up the formatting process. Optionally, set the cluster size in the **Allocation unit size** field. The cluster size [limits the maximum size of the partition](https://learn.microsoft.com/windows-server/storage/file-server/ntfs-overview). Keep this in mind if you try to resize the zonal persistent disk and this partition later.

![Selecting the partition format type in the New Simple Volume Wizard.](https://docs.cloud.google.com/static/compute/images/configure_new_volume_windows.png)

  5. After you complete the wizard and the volume is formatted, check the `Status` column on the list of attached disks to ensure that the new disk has a `Healthy` status.

![Checking that the disk is online with a healthy status.](https://docs.cloud.google.com/static/compute/images/pd_healthy_windows.png)




You can now write files to the disk.

## What's next

  * Learn how to [resize your persistent disks](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).
  * Learn how to regularly [back up your disks using snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) to prevent unintended data loss.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
