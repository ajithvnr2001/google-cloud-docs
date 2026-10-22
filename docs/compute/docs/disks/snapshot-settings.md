---
url: https://docs.cloud.google.com/compute/docs/disks/snapshot-settings/
title: Set default storage locations for globally scoped snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:32.442324+00:00
---

# Set default storage locations for globally scoped snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/snapshot-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set default storage locations for globally scoped snapshots Stay organized with collections  Save and categorize content based on your preferences. 

When you create snapshots, they are created as globally scoped snapshots by default. For a given project, you can customize the default location where Google Cloud stores the globally scoped snapshots by configuring your snapshot settings. Using snapshot settings to define your own custom default removes the need for you to manually specify a location every time you create a snapshot.

This document provides information about snapshot settings and how to use them to customize the default storage location for your project's globally scoped snapshots.

To manage location settings for regionally scoped snapshots, see [Set snapshot creation and restore locations for regionally scoped snapshots](https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope) ([Preview](https://cloud.google.com/products/#product-launch-stages)).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

  * You can view and update the snapshot settings only by using the gcloud CLI or REST.
  * You can't customize the default storage location of instant snapshots. You can only do so for standard and archive snapshots.
  * Modifying the location policy in your project's snapshot settings only affects the snapshots that are created after that modification. Updating your project's snapshot settings does not change the location of any existing snapshots.
  * If you manually specify a location during snapshot creation, then Google Cloud overrides the snapshot settings and creates your snapshot in that newly specified location. However, the storage location policy in your snapshot settings remains unchanged.
  * Default storage locations apply only to globally scoped snapshots. To control storage locations for regionally scoped snapshots, you must [Set allowed snapshot creation locations](https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope#set-storage-region).
  * Setting a default storage location controls only where the snapshot is stored. With globally scoped snapshots, you can't set where snapshot data can be restored. To set allowed locations for snapshot restoration, you need to [create a regional snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_snapshots) and [set allowed restore locations](https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope#set-restore-locations).



## How snapshot settings work

The storage location policy of a project's snapshot settings defines where Google Cloud automatically stores that project's snapshots. Google Cloud maintains a predefined value for this storage location policy until you update the snapshot settings and configure a new default. After you update the snapshot settings and set a new default storage location, Google Cloud uses this location to store every new snapshot created in that project.

You can update your snapshot settings to modify the storage location policy any number of times. However, modifying your project's snapshot settings only affects the locations of snapshots that are created after that modification. Updating your project's snapshot settings does not change the location of any existing snapshots.

To ensure that Google Cloud uses the storage location defined by your snapshot settings, don't manually specify a location during snapshot creation. If you manually specify a location during snapshot creation, then Google Cloud overrides the snapshot settings and creates your snapshot in that newly specified location. However, the storage location policy in your snapshot settings remains unchanged.

You can use snapshot settings to customize the default storage location of your standard and archive snapshots. You can't customize the default storage location of [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots).

### Storage location options

When you configure your project's snapshot settings and specify a new default storage location, you can either choose specific regions or use disk-based location settings. More specifically, you can choose one of the following location options for your storage location policy:

  * The nearest multi-region to the source disk
  * The same local region as the source disk
  * Specific regions of your choice



### Google Cloud predefined storage location policy

Until you update your snapshot settings for the first time, Google Cloud maintains a predefined value for the storage location policy. This predefined policy provides the default storage location for snapshots until you configure your own default storage location by updating your project's snapshot settings. The predefined storage location policy is set to the [multi-region](https://docs.cloud.google.com/storage/docs/locations#location-mr) that is geographically closest to the location of your source disk.

  * If your source disk is in a location that is part of a multi-region, then your snapshot settings storage location policy is set to that multi-region. For example, if your disk is in a location like `us-central1`, then the default storage location is the multi-region `us`.
  * For a location that is outside of a multi-region, the default storage location is the geographically closest multi-region outside of that region. For a location like `australia-southeast1`, the default location becomes the `asia` multi-region.



## Pricing implications

You don't have to pay any extra amount to use snapshot settings for your projects. However, the location values that you specify using snapshot settings affect other operations, which may in turn affect those operational costs.

## Set the default storage location for a project using snapshot settings

You can update your project's snapshot settings and set a new default storage location by using REST and the gcloud CLI.

If you don't set a storage location policy in your snapshot settings, then your snapshots are created using the Google Cloud predefined storage location policy.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.snapshotSettings.update` on the project



###  gcloud 

To add the snapshot settings or update the existing snapshot settings for your project, use the [`gcloud compute snapshot-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update):
    
    
      gcloud compute snapshot-settings update \
          --project=PROJECT_ID \
          --storage-location-policy=STORAGE_LOCATION \
          --storage-location-names=REGION_NAME
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `STORAGE_LOCATION`: The snapshot storage location policy for your project. The value can be one of the following:

    * `nearest-multi-region`: Specifies the location policy as the closest [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) to the location of your disk.
    * `local-region`: Specifies the location policy as the same [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where your disk is located.
    * `specific-locations`: Specifies the location policy as a custom [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) location of your choice. If you specify this option, you must also specify the location that you want by using the `--storage-location-names` flag.
  * `REGION_NAME`: Optional: If you include the `--storage-location-policy` flag with a value of `specific-locations`, then you must specify a [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r). You can specify only one region and it can't be a Cloud Storage multi-region. Set this value to the name of the region that you want to specify as your storage location policy.




### Examples to set storage location policy using snapshot settings

Consider an example project `my-project` in `us-central1` region.

  * To configure the storage location policy of your project's snapshot settings as the Cloud Storage multi-region closest to your disk, run the following command:


    
    
      gcloud compute snapshot-settings update \
          --project=my-project \
          --storage-location-policy=nearest-multi-region
    

  * To configure the storage location policy of your project's snapshot settings as the same Cloud Storage region as your disk, run the following command:


    
    
      gcloud compute snapshot-settings update \
          --project=my-project \
          --storage-location-policy=local-region
    

  * To configure as the storage location policy of your project's snapshot settings as a specific location of your choice (like `us-central1`), use the `--storage-location-names` flag and run the following command:


    
    
      gcloud compute snapshot-settings update \
          --project=my-project \
          --storage-location-policy=specific-locations \
          --storage-location-names=us-central1
    

###  REST 

To add the snapshot settings or update existing the snapshot settings for your project, make a `PATCH` request to the [`snapshotSettings.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/patch):
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshotSettings
    
      {
        "storageLocation": {
          "policy": "STORAGE_LOCATION",
          "locations": {
                "REGION_NAME": { "name": "REGION_NAME" }
          }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `STORAGE_LOCATION`: The snapshot storage location policy for your project. The value can be one of the following:

    * `NEAREST_MULTI_REGION`: Specifies the location policy as the closest [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) to the location of your disk.
    * `LOCAL_REGION`: Specifies the location policy as the same [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where your disk is located.
    * `SPECIFIC_LOCATIONS`: Specifies the location policy as a custom [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) location of your choice. If you specify this option, you must also specify the location that you want by using the `locations` parameter in your request.
  * `REGION_NAME`: Optional: If you include the `policy` parameter with a value of `SPECIFIC_LOCATIONS`, then you must specify a [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r). You can specify only one region and it can't be a Cloud Storage multi-region. Set this value to the name of the region that you want to specify as your storage location policy.




### Examples to set storage location policy using snapshot settings

Consider an example project `my-project` in `us-central1` region.

  * To configure the storage location policy of your project's snapshot settings as the Cloud Storage multi-region closest to your disk, make the following `PATCH` request:


    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshotSettings
    
        {
          "storageLocation": {
            "policy": "NEAREST_MULTI_REGION"
          }
        }
    

  * To configure the storage location policy of your project's snapshot settings as the same Cloud Storage region as your disk, make the following `PATCH` request:


    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshotSettings
    
        {
          "storageLocation": {
            "policy": "LOCAL_REGION"
          }
        }
    

  * To configure as the storage location policy of your project's snapshot settings as a specific location (like `us-central1`), make the following `PATCH` request:


    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshotSettings
    
        {
          "storageLocation": {
            "policy": "SPECIFIC_LOCATIONS",
            "locations": {
              "us-central1": { "name": "us-central1"}
            }
          }
        }
    

## View the default storage location defined by a project's snapshot settings

You can view your project's snapshot settings by using the Compute Engine API and the gcloud CLI.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.snapshotSettings.get` on the project



###  gcloud 

To view the snapshot settings for your project, use the [`gcloud compute snapshot-settings describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/describe):
    
    
      gcloud compute snapshot-settings describe \
          --project=PROJECT_ID
    

Replace `PROJECT_ID` with the ID of the project.

###  REST 

To view the snapshot settings for your project, make a `GET` request to the [`snapshotSettings.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/get):
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshotSettings
    

Replace `PROJECT_ID` with the ID of the project.

## What's next

  * Learn how to [view, delete, and share disk snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).
  * Learn how to [create scheduled snapshots for disks](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).
  * Learn how to [create a disk image from your snapshot](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
