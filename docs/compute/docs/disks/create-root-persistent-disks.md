---
url: https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks/
title: Create a customized boot disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:01.313496+00:00
---

# Create a customized boot disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a customized boot disk Stay organized with collections  Save and categorize content based on your preferences. 

When you create a Compute Engine instance, you must also create a boot disk for the instance. You can use a public image, a custom image, or a snapshot that was taken from another boot disk. When you create a boot disk, limit the disk size to 2 TiB to account for the limitations of [MBR](https://wikipedia.org/wiki/Master_boot_record) partitioning.

Compute Engine automatically creates a boot disk when you [create an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). If you require additional data storage space for your instances, add one or more secondary [instance storage disks](https://docs.cloud.google.com/compute/docs/disks) to the instance.

Use the procedures described in this document to create boot disks that you can use later to create Compute Engine instances. To improve the performance of a boot disk or to add space for additional applications or operating system files, you can resize the [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) or [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#modify_hyperdisk) boot disk.

As a best practice, don't use [regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) for boot disks. In a failover situation, they don't force-attach to a compute instance.

## Before you begin

  * When you create Compute Engine instances from images or disks by using the Google Cloud CLI or REST, there's a limit of 20 Compute Engine instances per second. If you need to create a higher number of Compute Engine instances per second, [request a higher quota limit](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota) for the **Images** resource.
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




## Create a boot disk from an image

You can create a standalone boot disk outside of instance creation and attach it to an instance afterwards.

###  Console 

  1. In the Google Cloud console, go to the **Create a disk** page.

[Go to the Create a disk page](https://console.cloud.google.com/compute/disksAdd)

  2. Under **Disk source type** , select **Image**. Choose an image from the list.

  3. Click **Create**.




###  gcloud 

To create a standalone boot disk, use the [`gcloud compute disks create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) command:
    
    
    gcloud compute disks create DISK_NAME --image IMAGE_NAME
    

###  REST 

To create a new boot disk, make a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks?sourceImage=IMAGE
    

Replace `IMAGE` with the URL-encoded, fully qualified URI of the source image to apply to this boot disk.

The request body must contain a name for this new disk:
    
    
    {
        "name": "DISK_NAME"
    }
    

If you created a boot disk that is larger than the image, you might want to [repartition the boot disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#resize_partitions).

## Create a boot disk from a snapshot

After you create a snapshot of a boot disk, you can use the snapshot to create new boot disks.

You can only apply data from a snapshot when you first create a disk. You can't apply a snapshot to an existing disk, or apply a snapshot to disks that belong to a different project than the snapshot.

###  Console 

  1. In the Google Cloud console, go to the **Create a disk** page.

[Go to the Create a disk page](https://console.cloud.google.com/compute/disksAdd)

  2. Under **Disk source type** , select **Snapshot**.

  3. Choose a snapshot from the list.

  4. Finish setting the properties for your disk and click **Create**.




###  gcloud 

To apply data from a disk snapshot, run the following command:
    
    
    gcloud compute disks create DISK_NAME --source-snapshot SNAPSHOT_NAME
    

Replace the following:

  * `DISK_NAME`: the name of the new disk.

  * `SNAPSHOT_NAME`: the name of the source snapshot to use when creating the disk.




###  REST 

To create a boot disk from a snapshot, make a `POST` request to the [`disks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks
    

The request body must contain a name for this new disk and the URL for the snapshot to use when creating the disk:
    
    
    {
        "name": "DISK_NAME",
        "sourceSnapshot": "zones/ZONE/snapshots/SNAPSHOT_NAME"
    }
    

Replace the following:

  * `PROJECT_NAME`: the name of your project.

  * `ZONE`: the zone where you want to create the disk.

  * `DISK_NAME`: the name of the new disk.

  * `SNAPSHOT_NAME`: the name of the source snapshot to use when creating the disk.




## Create a boot disk from a machine image

If you have backed up an instance using a machine image, you can create a copy of the boot disk contained within the machine image. For more information, see [Create a disk from a machine image](https://docs.cloud.google.com/compute/docs/machine-images/create-instance-from-machine-image#create-disk-from-machine-image).

## What's next

  * The process for resizing a boot disk and a non-boot disk are the same. For more information, see the instructions in [Resize a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#resize_partitions) or [Change the size or provisioned performance of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#modify_hyperdisk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
