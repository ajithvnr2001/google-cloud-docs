---
url: https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot/
title: Copy an instant snapshot to a different location \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:40:45.920542+00:00
---

# Copy an instant snapshot to a different location  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Copy an instant snapshot to a different location Stay organized with collections  Save and categorize content based on your preferences. 

In certain scenarios, you might want to copy an [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) to a different zone or region from its source disk. Possible occasions include:

  * Preserving the data on an instant snapshot before you delete the source disk, since deleting the disk deletes its instant snapshots.
  * Protecting the instant snapshot from a zonal or regional outage by storing it in a different location.
  * Moving an instant snapshot with data from an event or project milestone to long-term storage.
  * Using an instant snapshot in one location to create a new disk in another location.



In these scenarios, you must create a [standard or archive snapshot](https://docs.cloud.google.com/compute/docs/disks/snapshots) from the instant snapshot, and use that newly created snapshot. The new standard or archive snapshot is stored as an incremental resource, in the existing [snapshot chain](https://docs.cloud.google.com/compute/docs/disks/snapshots#snapshot_chains) for the disk.

This page explains how to create a standard or archive snapshot from an instant snapshot.

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




### Required roles and permissions

To get the permissions that you need to create a standard snapshot from an instant snapshot, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that has an attached service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a standard snapshot from an instant snapshot. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a standard snapshot from an instant snapshot:

  * `compute.snapshots.create` on the destination project for the new standard snapshot
  * `compute.instantSnapshots.useReadOnly` on the instant snapshot



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restrictions

If an instant snapshot's source disk is encrypted with a [customer-supplied encryption key (CSEK)](https://docs.cloud.google.com/compute/docs/disks/view-disk-details#view-encryption) ([Deprecated](https://docs.cloud.google.com/compute/docs/deprecations)), then the instant snapshot is also encrypted with the same key. Therefore, to create a standard snapshot from a CSEK-encrypted instant snapshot, you must provide the key you used to encrypt the source disk.

You can create a standard snapshot of an individual disk at most 6 times every 60 minutes. This limit also applies to creating a standard snapshot from an instant snapshot of a disk.

## Create a standard or archive snapshot from an instant snapshot

You can create a standard or archive snapshot from an instant snapshot by using the gcloud CLI, Google Cloud console, or REST.

###  Console 

  1. Find the instant snapshot:

     1. In the Google Cloud console, go to the **Snapshots** page.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

     2. Click the **Instant snapshots** tab.

     3. In the **Name** column, note the name of the snapshot you want to restore.

  2. Click **Create snapshot**.

  3. In the **Name** field, enter a unique name to identify the snapshot.

  4. Optional. Add more details about the snapshot in the **Description** field.

  5. Under **Snapshot source type** , choose **Instant snapshot**.

  6. In the **Source instant snapshot** list, select the instant snapshot you want to use.

  7. For **Type** , choose either **Snapshot** or **Archive snapshot**.

  8. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following:

     1. Choose the type of storage location that you want for your snapshot.

        * Choose [**Multi-regional**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) for higher availability at a higher cost.
        * Choose [**Regional snapshots**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) for more control over the physical location of your data at a lower cost.
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**.

  9. If the instant snapshot is CSEK-encrypted, provide the encryption key:

     1. In the **Decryption** section, enter the encryption key in the **Encryption key** field.
     2. If the key is wrapped with the public RSA key, select **Wrapped key**.
  10. Click **Create** to create the snapshot.




###  gcloud 

Create a standard or archive snapshot from a zonal or regional instant snapshot with the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create). You use different flags depending on whether the instant snapshot is of a zonal or regional disk.

###  Zonal instant snapshot 

Create your standard or archive snapshot from a zonal instant snapshot using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

  * To create a standard or archive snapshot in the predefined or customized default location configured in your snapshot settings, use the following command:


    
    
    gcloud compute snapshots create NEW_STANDARD_SNAPSHOT_NAME \
      --source-instant-snapshot=SRC_INSTANT_SNAPSHOT_NAME \
      --source-instant-snapshot-zone=SOURCE_ZONE \
      --snapshot-type=SNAPSHOT_TYPE
    

Replace the following with the corresponding values:

  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new standard snapshot.
  * `SRC_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located.
  * `SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`. If this flag is omitted, a standard snapshot is created.

  * To override the snapshot settings and create a standard or archive snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot:



    
    
    gcloud compute snapshots create NEW_STANDARD_SNAPSHOT_NAME \
      --source-instant-snapshot=SRC_INSTANT_SNAPSHOT_NAME \
      --source-instant-snapshot-zone=SOURCE_ZONE \
      --storage-location=STORAGE_LOCATION \
      --snapshot-type=SNAPSHOT_TYPE
    

Replace the following with the corresponding values:

  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new snapshot.
  * `SRC_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located.
  * `STORAGE_LOCATION`: For custom storage locations, this is the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` flag only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * `SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`. If this flag is omitted, a standard snapshot is created.




###  Regional instant snapshot 

Create your standard or archive snapshot from a regional instant snapshot using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

  * To create a standard or archive snapshot in the predefined or customized default location configured in your snapshot settings, use the following command:


    
    
    gcloud compute snapshots create NEW_STANDARD_SNAPSHOT_NAME \
      --source-instant-snapshot=SRC_INSTANT_SNAPSHOT_NAME \
      --source-instant-snapshot-region=SOURCE_REGION \
      --snapshot-type=SNAPSHOT_TYPE
    

Replace the following with the corresponding values:

  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new standard snapshot.
  * `SRC_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_REGION`: the region where the instant snapshot is located.
  * `SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`. If this flag is omitted, a standard snapshot is created.

  * To override the snapshot settings and create a standard or archive snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot:



    
    
    gcloud compute snapshots create NEW_STANDARD_SNAPSHOT_NAME \
      --source-instant-snapshot=SRC_INSTANT_SNAPSHOT_NAME \
      --source-instant-snapshot-region=SOURCE_REGION \
      --storage-location=STORAGE_LOCATION \
      --snapshot-type=SNAPSHOT_TYPE
    

Replace the following with the corresponding values:

  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new snapshot.
  * `SRC_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_REGION`: the region where the instant snapshot is located.
  * `STORAGE_LOCATION`: For custom storage locations, this is the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` flag only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * `SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`. If this flag is omitted, a standard snapshot is created.




###  REST 

To create a standard snapshot from a zonal or regional instant snapshot, make a `POST` request to the [snapshots.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert) method.

The API request properties depend on whether the instant snapshot is of a zonal or regional disk.

###  Zonal instant snapshot 

Create your standard or archive snapshot from a zonal instant snapshot using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

  * To create a standard or archive snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert).

  * To override the snapshot settings and create the snapshot in a custom storage location, include the `storageLocations` property in your request.



    
    
    POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT/global/snapshots
    {
      "name": "NEW_STANDARD_SNAPSHOT_NAME",
      "snapshotType": "NEW_SNAPSHOT_TYPE",
      "sourceInstantSnapshot": "projects/SOURCE_PROJECT/zones/SOURCE_ZONE/instantSnapshots/SOURCE_INSTANT_SNAPSHOT_NAME",
      "sourceInstantSnapshotEncryptionKey": "SOURCE_ENCRYPTION_KEY"
    }
    

Replace the following with the corresponding values:

  * `DESTINATION_PROJECT`: the project in which to create the new snapshot.
  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new snapshot.
  * `NEW_SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`.
  * `SOURCE_PROJECT`: the project containing the source instant snapshot.
  * `SOURCE_ZONE`: the zone where the instant snapshot is located.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_ENCRYPTION_KEY`: if the instant snapshot is encrypted with a customer-supplied key or customer-managed key, replace this value with the key information. Otherwise, you can omit this property.
  * `STORAGE_LOCATION`: Optional. The [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.



Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

###  Regional instant snapshot 

Create your regional standard or archive snapshot from a regional instant snapshot using the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

To create a standard or archive snapshot volume in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/DESTINATION_PROJECT/global/snapshots
    {
    "name": "NEW_STANDARD_SNAPSHOT_NAME",
    "snapshotType": "NEW_SNAPSHOT_TYPE",
    "sourceInstantSnapshot": "projects/SOURCE_PROJECT/regions/SOURCE_REGION/instantSnapshots/SOURCE_INSTANT_SNAPSHOT_NAME",
    "sourceInstantSnapshotEncryptionKey": "SOURCE_ENCRYPTION_KEY"
    }
    

Replace the following with the corresponding values:

  * `DESTINATION_PROJECT`: the project in which to create the new snapshot.
  * `NEW_STANDARD_SNAPSHOT_NAME`: a unique name for the new snapshot.
  * `NEW_SNAPSHOT_TYPE`: the type of snapshot to create, either `STANDARD` or `ARCHIVE`.
  * `SOURCE_PROJECT`: the project containing the source instant snapshot.
  * `SOURCE_REGION`: the region where the instant snapshot is located.
  * `SOURCE_INSTANT_SNAPSHOT_NAME`: the name of the source instant snapshot.
  * `SOURCE_ENCRYPTION_KEY`: if the instant snapshot is encrypted with a customer-supplied key or customer-managed key, replace this value with the key information. Otherwise you can omit this property.



### API request response

If the `POST` request is successful, the response body will be an object that you can poll to get the status of the snapshot's creation. See [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses) for more information.

## What's next

  * Learn how to [share a standard snapshot across projects](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#sharing_snapshots).
  * Learn how to [create a VM from the standard snapshot](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot).
  * Get help troubleshooting [errors creating standard snapshots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-snapshots) and [errors creating instant snapshots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-instant-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
