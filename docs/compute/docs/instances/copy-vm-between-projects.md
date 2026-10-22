---
url: https://docs.cloud.google.com/compute/docs/instances/copy-vm-between-projects/
title: Copying VMs between projects \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:17.949736+00:00
---

# Copying VMs between projects  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/copy-vm-between-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Copying VMs between projects Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to copy your VM to a different project.

## Before you begin

  * Review [ Best practices for persistent disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#prepare_for_consistency) and prepare your boot disk for snapshots.
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



### Required roles

To get the permissions that you need to copy VM between projects, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to copy VM between projects. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to copy VM between projects:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Copy a VM to another project

  1. In your source project, create a snapshot of the VM's boot disk, using one of the following commands:

###  Zonal boot disk 

If your VM has a zonal boot disk, create a snapshot using the following command:
         
         gcloud compute snapshots create SNAPSHOT_NAME \
             --source-disk SOURCE_DISK \
             --snapshot-type SNAPSHOT_TYPE \
             --source-disk-zone SOURCE_DISK_ZONE
         

Replace the following:

     * SNAPSHOT_NAME: A name for the snapshot.
     * SOURCE_DISK: The name of the zonal Persistent Disk volume from which you want to create a snapshot.
     * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created. Choose Archive for more cost-efficient data retention.
     * SOURCE_DISK_ZONE: The zone of the zonal Persistent Disk volume from which you want to create a snapshot.

###  Regional boot disk 

If your VM has a regional boot disk, create a snapshot using the following command:
    
    gcloud compute snapshots create SNAPSHOT_NAME \
        --source-disk SOURCE_DISK \
        --source-disk-region=SOURCE_DISK_REGION \
        --snapshot-type=SNAPSHOT_TYPE
    

Replace the following:

     * SNAPSHOT_NAME: A name for the snapshot.
     * SOURCE_DISK: The name of the regional Persistent Disk volume from which you want to create a snapshot.
     * SOURCE_DISK_REGION: The region of the regional Persistent Disk volume from which you want to create a snapshot.
     * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a **STANDARD** snapshot is created.

  2. Create a custom image from the snapshot using the following command:
         
         gcloud compute images create IMAGE_NAME \
             --source-snapshot=SOURCE_SNAPSHOT \
             [--storage-location=LOCATION]
         

Replace the following:

     * `IMAGE_NAME`: a name for the new image
     * `SOURCE_SNAPSHOT`: the snapshot from which you want to create the image
     * `LOCATION`: Optional: a flag that lets you designate the region or multi-region where your image is stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.
  3. Optional: Share the custom image with users who create VMs in the destination project. For more information about sharing custom images, see [Sharing custom image within an organization](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#share-images-within-organization).

  4. In your destination project, create a VM from the custom image using the following command:
         
         gcloud compute instances create VM_NAME \
             --image-project IMAGE_PROJECT \
             IMAGE_FLAG \
             --subnet SUBNET \
             --zone ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM
     * `IMAGE_PROJECT`: the ID of the Google Cloud project that contains the image
     * `IMAGE_FLAG`: specify one of the following: 
       * Use the `--image IMAGE_NAME` flag to specify a custom image. 

For example, `--image my-debian-image-v2`.

       * If you created your custom images as part of a [custom image family](https://docs.cloud.google.com/compute/docs/images#custom-families), use the `--image-family IMAGE_FAMILY_NAME` flag to specify that custom image family. 

This creates the VM from the most recent, non-deprecated OS image and OS version in your custom image family. For example, if you specify `--image-family my-debian-family`, Compute Engine creates a VM from the latest OS image in your custom `my-debian-family` image family.

**Note:** Compute Engine uses the default image family and project if you don't specify an image, for example `debian-10` and `debian-cloud`, respectively. 
     * `SUBNET`: if the subnet and instance are in the same project, replace `SUBNET` with the name of a subnet that is in the same region as the instance. 

To specify a subnet in a Shared VPC network, replace `SUBNET` with a string of the form:
           
           projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
                  

Replace the following:

       * `HOST_PROJECT_ID`: the project ID of the Shared VPC host project
       * `REGION`: the region of the subnet
       * `SUBNET_NAME`: the name of the subnet

The region of the subnet for a Shared VPC network must also match the region containing the instance.

     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones) for the VM



## What's next

  * Customize the destination project's [VPC network](https://docs.cloud.google.com/vpc/docs/vpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
