---
url: https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools/
title: Manage Hyperdisk pools \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:13:59.844954+00:00
---

# Manage Hyperdisk pools  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/manage-storage-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage Hyperdisk pools Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to list, describe, modify, and delete Hyperdisk pools.

**Note:** Hyperdisk Exapools are generally available with an allowlist. To modify or delete an Exapool, [contact your account team](https://docs.cloud.google.com/tam).

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

To get the permissions that you need to manage a pool, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM instance that can run as a service account: Service Account User (v1) (`roles/iam.serviceAccountUser` role) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage a pool. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage a pool:

  * To list the pools for a project and zone: `compute.storagePools.list`
  * To list the disks within a pool: `compute.storagePools.get`
  * To view the properties of a pool: `compute.storagePools.get`
  * To update the provisioned capacity or performance of a pool: 
    * `compute.storagePools.get`
    * `compute.storagePools.update`
  * To delete a pool: `compute.storagePools.delete`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

Limitations for managing pools:

  * You can't change the provisioning model for a pool. For example, you can't change a Standard capacity Storage Pool to an Advanced capacity Storage Pool or an Advanced performance Storage Pool to a Standard performance Storage Pool.
  * You can't move disks in or out of a pool; you have to recreate the disk from a standard snapshot. For more information, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk).
  * You can't [clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#clone), [create instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) of, or [configure Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) for disks in a pool.



Limitations specific to Storage Pools:

  * You can change the provisioned capacity or performance of a Storage Pool at most two times in a 24 hour period.
  * You can delete at most 5 Storage Pools per hour.
  * The Storage Pool management command either succeeds or fails immediately, but it can take up to 5 minutes to complete the action, and up to 30 minutes for the changes to appear.



Limitations specific to Exapools:

  * You must contact your account team to change the provisioned capacity, IOPS, or throughput of an Exapool.
  * You must contact your account team to delete an Exapool.



For the full list of limitations, see [Storage Pool limitations](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp_limitations) and [Exapools limitations](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#limitations).

## Value ranges when modifying pools

When creating a Storage Pool, the new values for size, IOPS, and throughput must be within the limits for the type of Storage Pool you are modifying. Also, you can only specify new values using supported incremental values.

For detailed performance provisioning limits, see [Limits for Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#sp_limitations) and [Size and performance limits for Exapools](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-exapools#exapool-limits).

## List the pools for a project

To see the pools that were created in a project, use the Google Cloud console, Google Cloud CLI, or REST.

###  Console 

  1. Go to the **Storage pools** page in the Google Cloud console.   
[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

The page displays the pools created within the selected project.

  3. Optional: Use the **Filter** bar to display only the pools that match the filter parameters, such as Location, Type, Name, and Pool capacity remaining.




###  gcloud 

To list all the pools created within the current project, use the [`gcloud compute storage-pools list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list).
    
    
    gcloud compute storage-pools list
    

To limit the results to a specific region or zone you can use the `--filter` flag, for example:

  * `--filter="zone ~ us`
  * `--filter="zone=us-east4-c"`



###  REST 

To show the pools created within a project and zone, construct a `GET` request using the [`storagePools.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the storage pool
  * ZONE: the zone where the pool is located, for example, `us-central1-a`.



## List the disks in a pool

To get a list of the disks created in a pool, use the Google Cloud console, Google Cloud CLI, or REST.

###  Console 

  1. Go to the **Storage pools** page in the Google Cloud console.   
[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

The page displays the pools created within the selected project.

  3. In the **Name** field, click the name of the pool that you want to view.

The **Manage storage pool** page opens.

  4. In the **Storage pool disks** section, you can see the disks that were created in the pool.




###  gcloud 

To list the disks that were created in a pool, use the [`gcloud compute storage-pools list-disks` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/list-disks).
    
    
    gcloud compute storage-pools list-disks STORAGE_POOL_NAME  \
        [--zone=ZONE]
    

Replace the following:

  * STORAGE_POOL_NAME: the name of the pool.
  * ZONE: Optional. The zone in which the pool is located, for example, `us-central1-a`.



###  REST 

To list the disks that are using a pool, construct a `GET` request using the [`storagePools.listDisks` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/listDisks).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME/listDisks
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the storage pool
  * ZONE: the zone where the pool is located, for example, `us-central1-a`.
  * STORAGE_POOL_NAME: the name of the pool.



## Describe a pool

To view the details of a pool, you can use the Google Cloud console, Google Cloud CLI, or REST.

###  Console 

  1. Go to the **Storage pools** page in the Google Cloud console.   
[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)

  2. Select the tab for **Exapools** or **Storage Pools**.

  3. For each pool listed on the page, you can view the following information:

     * Status
     * Name
     * Location
     * Pool type
     * Pool capacity
     * Pool capacity remaining
     * Pool IOPS
     * Pool IOPS remaining
     * Number of disks created in the pool
  4. In the **Name** field, click the name of the pool that you want to view.

The **Manage storage pool** page opens.

  5. In the tiles at the top of the page you can view the provisioned and used capacity, and the provisioned and used throughput and IOPS for the pool.

  6. In the **Storage pool settings** section, you can view additional properties of the pool, such as the creation time, capacity provisioning type, performance provisioning type, the total number of disks in the pool, and the utilization percentages for capacity, throughput, and IOPS.

  7. In the **Storage pool disks** section, you can view information about the disks created in the pool.

  8. Optional: For additional information about the pool usage, you can click the **Monitoring** tab to view graphs for various pool metrics. For more information, see [Monitor pools](https://docs.cloud.google.com/compute/docs/disks/monitor-pool-performance).




###  gcloud 

Use the [`gcloud compute storage-pools describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/describe) to view the details for a pool.
    
    
    gcloud compute storage-pools describe STORAGE_POOL_NAME  \
        [--zone=ZONE]
    

Replace the following:

  * STORAGE_POOL_NAME: the unique pool name.
  * ZONE: Optional. The zone in which the pool is located, for example, `us-central1-a`.



###  REST 

To retrieve details about a pool, construct a `GET` request using the [`storagePools.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the pool
  * ZONE: the zone where the pool is located, for example, `us-central1-a`
  * STORAGE_POOL_NAME: the name of the pool



## Modify a pool

You can increase or decrease the provisioned capacity, IOPS, or throughput of a pool.

### Modify a Storage Pool

To increase the capacity, IOPS, or throughput of a Storage Pool, you must have quota available for the project and region. It can take up to 30 minutes before the new provisioning values are displayed for the Storage Pool.

###  Console 

  1. Go to the **Storage pools** page in the Google Cloud console.   
[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)
  2. Select the **Storage Pools** tab.
  3. In the **Name** field, click the name of the Storage Pool that you want to modify.

The **Manage storage pool** page opens.

  4. Click edit **Edit**.

The **Edit storage pool** page opens.

  5. Optional: In the **Storage pool capacity** field, enter the new value for pool provisioned capacity. The new value must differ from the current value by at least 1 TiB and no more than 100 TiB. The new value can be larger or smaller than the current value. The minimum size can't be less than 10 TiB and the maximum size can't be more than 5 PiB.

  6. Optional: In the **Provisioned throughput** field, enter the new value for provisioned throughput.

  7. Optional: For Hyperdisk Balanced Storage Pools, in the **Provisioned IOPS** field, enter the new value for the provisioned IOPS.

  8. Click **Save** to update the Storage Pool.




###  gcloud 

Use the [`gcloud compute storage-pools update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/update) to modify a Storage Pool.
    
    
    gcloud compute storage-pools update STORAGE_POOL_NAME  \
        --zone=ZONE   \
        --provisioned-capacity=POOL_SIZETiB   \
        --provisioned-iops=IOPS   \
        --provisioned-throughput=THROUGHPUT   \
        --description=DESCRIPTION
    

Replace the following:

  * STORAGE_POOL_NAME: the name of the pool.
  * ZONE: Optional: the zone that the pool is located in, for example, `us-central1-a`.
  * POOL_SIZE: Optional: the pool provisioned capacity, in TiB.
  * IOPS: Optional: the pool provisioned IOPS. You can use this flag only with Hyperdisk Balanced Storage Pools.
  * THROUGHPUT: Optional: the pool provisioned throughput, in MiB/s.
  * DESCRIPTION: Optional: a descriptive string for the pool.



###  REST 

To update a pool, construct a `PATCH` request by using the [`storagePools.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/update).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME
    
    {
        "description": "DESCRIPTION",
        "poolProvisionedCapacityGb": "SIZE",
        "poolProvisionedIops": "IOPS",
        "poolProvisionedThroughput": "THROUGHPUT"
    }
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone where the pool is located, for example, `us-central1-a`.
  * STORAGE_POOL_NAME: the name of the pool.
  * DESCRIPTION: Optional: a text field to describe the pool.
  * SIZE: Optional: the new pool provisioned capacity, in GiB.
  * IOPS: Optional: the new value for pool provisioned IOPS. You can only specify this property when the pool contains disks of type `hyperdisk-balanced`.
  * THROUGHPUT: Optional: the new value for pool provisioned throughput, specified in MiB/s.



### Modify an Exapool

To change the provisioned capacity, IOPS, or throughput of an Exapool, [contact your account team](https://docs.cloud.google.com/tam).

## Delete a pool

Deleting a pool is irreversible. However, deleting a pool doesn't delete any snapshots made from disks that were created in the pool. You must delete the snapshots separately.

### Delete a Storage Pool

To delete or remove a Storage Pool, you must first delete all the disks within the Storage Pool. Then, use the Google Cloud console, Google Cloud CLI, or REST to delete the Storage Pool.

###  Console 

  1. Go to the **Storage pools** page in the Google Cloud console.   
[Go to the **Storage pools** page](https://console.cloud.google.com/compute/storagePools)
  2. 1\. Select the **Storage Pools** tab.
  3. In the **Name** field, click the name of the Storage Pool that you want to delete.

The **Manage storage pool** page opens.

  4. In the **Storage pool disks** section, verify there are no disks listed for the Storage Pool.

  5. Click delete **Delete pool**.




###  gcloud 

Use the [`gcloud compute storage-pools delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete) to delete a pool.
    
    
    gcloud compute storage-pools delete STORAGE_POOL_NAME  \
        --zone=ZONE   \
    

Replace the following:

  * STORAGE_POOL_NAME: the unique pool name.
  * ZONE: Optional: the zone in which the pool is located, for example, `us-central1-a`.



###  REST 

To remove a pool, construct a `DELETE` request for the [`storagePools.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/storagePools/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/storagePools/STORAGE_POOL_NAME
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone where the pool is located, for example, `us-central1-a`.
  * STORAGE_POOL_NAME: the unique pool name.



### Delete an Exapool

To delete an Exapool, [contact your account team](https://docs.cloud.google.com/tam).

## What's next?

  * Learn more about [Hyperdisk pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
