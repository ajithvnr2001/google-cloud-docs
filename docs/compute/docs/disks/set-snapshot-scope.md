---
url: https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope/
title: Set creation and restore locations for regionally scoped snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:32.325875+00:00
---

# Set creation and restore locations for regionally scoped snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/set-snapshot-scope/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Set creation and restore locations for regionally scoped snapshots Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, snapshots are created with a global scope. Globally scoped snapshots are stored in a specific [storage location](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) and can be restored (used to create a new disk) in _any_ region or zone. For additional location-based isolation control, you can create regionally scoped snapshots. Regionally scoped snapshots store all snapshot data and metadata together in the scoped region. With regionally scoped snapshots, you can also restrict the regions where you can create and restore snapshots.

This document explains how to set allowed locations for regional snapshot creation and restoration.

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




## Limitations

  * Setting a regional scope overrides all [default storage location settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) for the project.
  * Setting a regional scope applies only to new regional snapshots.
  * You can't convert a globally scoped snapshot to a regionally scoped snapshot. You must create a new snapshot with the appropriate scope.



## Required roles and permissions

To get the permissions that you need to set storage and restore locations for regionally scoped snapshots, ask your administrator to grant you the following IAM roles on the project:

  * [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

These predefined roles contain the permissions required to set snapshot creation and restore locations. To see the exact permissions that are required, expand the **Required permissions** section:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * To set allowed snapshot creation locations to regions other than the source disk region:
    * `compute.diskSettings.get` on the disk
    * `compute.diskSettings.update` on the disk
    * `compute.regionDiskSettings.get` on the disk
    * `compute.regionDiskSettings.update` on the disk
  * To set allowed snapshot restore locations to regions other than the source disk region:
    * `compute.regionSnapshotSettings.get` on the project
    * `compute.regionSnapshotSettings.update` on the project



## Set allowed snapshot creation locations

By default, you can create snapshots in all regions. To restrict where you can create regionally scoped snapshots, set allowed access locations at the project level. Once you set access locations, you can create regionally scoped snapshots for the project only in these locations.

###  gcloud 

To let zonal disks in Zone A create snapshots in any region, use the [`gcloud beta compute disk-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disk-settings):
    
    
      gcloud beta compute disk-settings update \
          --zone=ZONE_A \
          --access-location-policy=all-regions \
    

To let regional disks in Region A create snapshots in any region, use the [`gcloud beta compute disk-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disk-settings):
    
    
      gcloud beta compute disk-settings update \
          --region=REGION_A \
          --access-location-policy=all-regions
    

To let disks in Region A create snapshots only in Region B, use the [`gcloud beta compute disk-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/disk-settings):
    
    
      gcloud beta compute disk-settings update \
          --access-location-policy=specific-regions \
          --region=REGION_A \
          --add-access-locations=REGION_B
    

Replace the following:

  * `ZONE_A`: The zone of the disks that can create snapshots in any region.
  * `REGION_A`: The region of all disks (in a project) that require regionally scoped snapshot creation restrictions.
  * `REGION_B`: An allowed region for regionally scoped snapshot creation. You can set multiple regions as allowed access locations. You must include the region that the source disk is stored in as one of the allowed regions.



###  REST 

To let zonal disks in Zone A create snapshots in any region, make a `PATCH` request to the `diskSettings.patch` method:
    
    
      PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE_A/diskSettings?updateMask=accessLocation
    
      {
        "accessLocation":
        {
          "policy":"ALL_REGIONS"
        }
      }
    

To let regional disks in Region A create snapshots only in Region B, make a `PATCH` request to the `regionDiskSettings.patch` method:
    
    
      PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION_A/diskSettings?updateMask=accessLocation
    
      {
        "accessLocation":
        {
          "policy":"SPECIFIC_REGIONS",
          "locations":
          {
            "REGION_B":{"region":"REGION_B"}
          }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `ZONE_A`: The zone of the disk.
  * `REGION_A`: The region of the disk.
  * `REGION_B`: An allowed region for snapshot creation. You can set multiple regions as allowed access locations. You must include the region that the source disk is stored in as one of the allowed regions.



## Set allowed snapshot restore locations

By default, you can restore regionally and globally scoped snapshots to any region. To configure restore locations for your regionally scoped snapshots, set allowed access locations at the project level. You must set allowed access locations for each project individually. Once you set access locations, you can restore regionally scoped snapshots for the project only in these locations.

###  gcloud 

To let snapshots for a project in Region A be restored in _all_ regions, use the [`gcloud beta compute snapshot-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update):
    
    
      gcloud beta compute snapshot-settings update \
          --project=PROJECT_ID \
          --region=REGION_A \
          --access-location-policy=all-regions
    

To let snapshots for a project in Region A be restored only in Region B, use the [`gcloud beta compute snapshot-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update):
    
    
      gcloud beta compute snapshot-settings update \
          --project=PROJECT_ID \
          --access-location-policy=specific-regions \
          --region=REGION_A \
          --add-access-locations=REGION_B
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `REGION_A`: The region where the regionally scoped snapshots are stored.
  * `REGION_B`: An allowed region where regionally scoped snapshots can be restored. You can set multiple regions as allowed restore locations.



###  REST 

To let snapshots for a project in Region A be restored in _all_ regions, make a `PATCH` request to the [`regionSnapshotSettings.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/patch):
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/snapshotSettings?updateMask=accessLocation
    
      {
        "accessLocation":
        {
          "policy":"ALL_REGIONS"
        }
      }
    

To let snapshots for a project in Region A be restored only in Region B, make a `PATCH` request to the [`regionSnapshotSettings.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/patch):
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/snapshotSettings?updateMask=accessLocation
    
      {
        "accessLocation":
        {
          "policy":"SPECIFIC_REGIONS",
          "locations":
            {"REGION_B":
              {"region":"REGION_B"}
            }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `REGION_A`: The region where the regionally scoped snapshots are stored.
  * `REGION_B`: An allowed region where regionally scoped snapshots can be restored. You can set multiple regions as allowed restore locations.



## Edit allowed snapshot restore locations

###  gcloud 

To view the allowed restore locations for snapshots for a project stored in Region A, use the [`gcloud beta compute snapshot-settings describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/describe):
    
    
      gcloud beta compute snapshot-settings describe \
          --project=PROJECT_ID \
          --region=REGION_A
    

To remove Region B from the list of allowed restore locations for snapshots for a project stored in Region A, use the [`gcloud beta compute snapshot-settings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshot-settings/update):
    
    
      gcloud beta compute snapshot-settings update \
          --project=PROJECT_ID \
          --access-location-policy=specific-regions \
          --remove-access-locations=REGION_B \
          --region=REGION_A
    
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `REGION_A`: The region where the regionally scoped snapshots are stored.
  * `REGION_B`: The region where you want to remove restore access for regionally scoped snapshots.



###  REST 

To view the allowed restore locations for snapshots for a project stored in Region A, make a `GET` request to the [`regionSnapshotSettings.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/get):
    
    
      GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/snapshotSettings
    

To remove Region B from the list of allowed restore locations for snapshots for a project stored in Region A, make a `PATCH` request to the [`regionSnapshotSettings.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshotSettings/patch):
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION_A/snapshotSettings?updateMask=accessLocation
    
      {
        "accessLocation":
        {
          "policy":"SPECIFIC_REGIONS",
          "locations":
            {"REGION_B":{}}
        }
      }
    

Replace the following:

  * `PROJECT_ID`: The ID of the project.
  * `REGION_A`: The region where the regionally scoped snapshots are stored.
  * `REGION_B`: The region where you want to remove restore access for regionally scoped snapshots.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
