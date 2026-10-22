---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-disk/create-disk/
title: Create a standalone disk \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:35.405587+00:00
---

# Create a standalone disk  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-disk/create-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create a standalone disk Stay organized with collections  Save and categorize content based on your preferences. 

Create a standalone disk in the Google Distributed Cloud (GDC) air-gapped appliance console.

  1. In the navigation menu, click **Virtual Machines > Disks**.

  2. Click **Create disk**.

  3. Enter a disk name unique to the current project across all disks.

  4. In the **Size** field, enter a disk size between 10 and 65536 GB.

  5. Provision a blank disk or an image:

     * To provision a standalone blank disk, click **Blank disk**.

     * To provision a standalone disk from an image:

       1. Click **Image**.

       2. In the **Image name** list, select a source image. When you select an image, the minimum disk size changes to match the image. You might want to increase the size you specified earlier to meet your needs.

  6. In the **Storage profile** section, choose a profile. The default profile is **Standard**.

  7. Click **Create**.




The disk appears in the list of disks. When the disk status is **Pending** or **Ready** , you can add the disk to a VM.

## What's next

  * [Add a disk to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
