---
url: https://docs.cloud.google.com/lakehouse/docs/use-managed-disaster-recovery/
title: Use cross-region replication and disaster recovery \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:50.403319+00:00
---

# Use cross-region replication and disaster recovery  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/use-managed-disaster-recovery/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Use cross-region replication and disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

_Borderless Lakehouse_ supports cross-region replication and disaster recovery for catalog metadata.

This configuration requires catalogs backed by Cloud Storage [Dual-Region](https://docs.cloud.google.com/storage/docs/locations#location-dr) or [Multi-Region](https://docs.cloud.google.com/storage/docs/locations#location-mr) buckets.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to use the Iceberg REST catalog endpoint in the Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles: 

  * Perform administrative tasks, such as managing catalog user access, storage access, and the catalog's credential vending mode: 
    * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) on the project
    * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the Cloud Storage bucket
  * Read table data in credential vending mode: [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project 
  * Write table data in credential vending mode: [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project 
  * Read catalog resources and table data in non-credential vending mode: 
    * [BigLake Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`) on the project
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Cloud Storage bucket
  * Manage catalog resources and write table data in non-credential vending mode: 
    * [BigLake Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`) on the project
    * [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) on the Cloud Storage bucket



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Replication and disaster recovery workflow

To use cross-region replication and disaster recovery, you follow these general steps:

  1. **View replication status:** Identify your current primary and secondary regions to determine the target region for the failover.
  2. **Check synchronization status:** Verify the current state of your primary and secondary regions to ensure they are ready for a transition.
  3. **Choose a failover mode:** Decide between a [_soft failover_](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery) (best for planned maintenance) or a [_hard failover_](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery) (best for emergency recovery).
  4. **Initiate the failover:** Run the command corresponding to your chosen mode to switch your primary and secondary regions.



## Prepare for failover

Identify your current primary region and verify the synchronization status of your secondary region. Then, initiate the failover.

### View replication status

To determine the regions where your catalog is replicated, run the following [`gcloud biglake iceberg catalogs describe`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/describe) command.
    
    
    gcloud biglake iceberg catalogs describe CATALOG_NAME
    

Replace `CATALOG_NAME` with the name of your catalog.

### Check synchronization status

Before you initiate a failover, check the synchronization status of your secondary replica with the [`gcloud biglake iceberg catalogs failover`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/failover) command:
    
    
    gcloud biglake iceberg catalogs failover CATALOG_NAME \
        --validate_only \
        --primary-replica PRIMARY_REPLICA_REGION
    

Replace the following:

  * `CATALOG_NAME`: the name of your catalog.
  * `PRIMARY_REPLICA_REGION`: the region to designate as the new primary replica.



## Initiate a failover

The disaster recovery feature uses metastore replication to designate primary and secondary regions. All table commit metadata is served from the primary region and replicated to the secondary region. You can switch the primary and secondary regions for the catalog using the failover operation.

###  Soft failover 

To initiate a soft failover, run the following [`gcloud biglake iceberg catalogs failover`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/failover) command:
    
    
    gcloud biglake iceberg catalogs failover CATALOG_NAME \
        --primary-replica PRIMARY_REPLICA_REGION
    

Replace the following:

  * `CATALOG_NAME`: the name of your catalog.
  * `PRIMARY_REPLICA_REGION`: the region to designate as the new primary replica.



###  Hard failover 

To initiate a hard failover, run the following [`gcloud biglake iceberg catalogs failover`](https://docs.cloud.google.com/sdk/gcloud/reference/biglake/iceberg/catalogs/failover) command:
    
    
    gcloud biglake iceberg catalogs failover CATALOG_NAME \
        --primary-replica PRIMARY_REPLICA_REGION \
        --conditional-failover-replication-time=REPLICATION_TIMESTAMP
    

Replace the following:

  * `CATALOG_NAME`: the name of your catalog.
  * `PRIMARY_REPLICA_REGION`: the region to designate as the new primary replica.
  * `REPLICATION_TIMESTAMP`: an RFC 3339 timestamp that acts as a checkpoint for replication. The replication process verifies that the replica contains all data committed up to this time. If the replica does not contain all data committed before this timestamp, the command fails. To force the failover process regardless of any replication delay, set this timestamp to a date far in the past. Note: While this feature is in Preview, the REPLICATION_TIMESTAMP only tracks the catalog metadata, rather than Cloud Storage files. To keep data loss with a lower bound, see the Cloud Storage [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability) documentation.



## What's next

  * [Use the Lakehouse runtime catalog Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
