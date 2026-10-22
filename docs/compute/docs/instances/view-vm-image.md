---
url: https://docs.cloud.google.com/compute/docs/instances/view-vm-image/
title: View the source image of a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:28.994933+00:00
---

# View the source image of a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/view-vm-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View the source image of a VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You create a virtual machine (VM) instance from either an [OS image](https://docs.cloud.google.com/compute/docs/images/os-details) or a disk image. This document shows you how to determine the source OS image or source disk image of a VM.

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




## View the source OS image or source disk image of a VM

To view the source OS image or source disk image of a VM, use the Google Cloud console, Google Cloud CLI, or Compute Engine API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.get` on the instance



###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the **Name** of the VM.

  3. The name of the source OS image or source disk image is in **Storage** > **Boot disk** > **Image**.




###  gcloud 

  1. View the disks attached to a VM by using the following [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe):
         
         gcloud compute instances describe VM_NAME
         

Replace `VM_NAME` with the name of the VM.

  2. View the source OS image or source disk image of the disk by using the following [`gcloud compute disks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/describe):
         
         gcloud compute disks describe DISK_NAME \
            --zone=ZONE \
            --format="get(SOURCE)"
         

Replace the following:

     * `DISK_NAME`: the name of the disk to view the source of.

     * `ZONE`: the zone that the disk is located in.

     * `SOURCE`: a value that specifies whether to return the source OS image or the source disk image. Set to `sourceDisk` or to `sourceImage`. No value is returned when specifying `sourceDisk` or `sourceImage` unless there is a corresponding source OS image or a source disk image. If no value is returned, specify the other value and run the command again.




###  REST 

  1. View the disks attached to a VM by using the following [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get):
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `ZONE`: the zone containing the VM
     * `VM_NAME`: the name of the VM
  2. View the source OS image or source disk image of the disk by using the [`disks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/get).

For a VM that has a source OS image, this method returns the source image that was used to create the disk in the `sourceImage` field. For a VM that has a source disk image, this method instead returns the source image in the `sourceDisk` field.
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `ZONE`: the zone containing the disk
     * `DISK_NAME`: the name of the disk



## What's next

  * Learn more about [OS images](https://docs.cloud.google.com/compute/docs/images) on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
