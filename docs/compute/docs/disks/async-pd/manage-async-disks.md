---
url: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-async-disks/
title: Manage disks that use Asynchronous Replication \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:05:02.540555+00:00
---

# Manage disks that use Asynchronous Replication  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-async-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage disks that use Asynchronous Replication Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resize and clone Asynchronous Replication disks.

Asynchronous Replication is useful for [low-RPO, low-RTO](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) disaster recovery. To learn more about Asynchronous Replication, see [About Asynchronous Replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/about).

## Limitations

  * Primary and secondary disks must be the same size. If you resize a primary disk that is actively replicating, then the secondary disk is automatically resized. If the secondary disk fails to resize automatically, then you must manually resize it to the same size as the primary disk. Replication is paused until the secondary disk is the same size as the primary disk.
  * You can't clone primary disks from a consistency group. You must clone primary disks individually. However, you can clone secondary disks from a consistency group.



## Before you begin

  * [Create a primary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_primary_disk).
  * [Create a secondary disk](https://docs.cloud.google.com/compute/docs/disks/async-pd/configure#create_a_secondary_disk).
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




## Resize disks

If you require additional storage space or increased performance limits, you can increase the size of a primary disk to up to 64 TiB. You can't decrease the size of a disk.

When you resize a primary disk that is actively replicating to a secondary disk, the secondary disk size is increased to the same size as the primary disk. If the secondary disk fails to resize automatically, then you must manually resize it to the same size as the primary disk.

For information about how to increase the size of a disk, see [Increase the size of a disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#increase_the_size_of_a_disk).

## Clone disks

You can clone a single primary or secondary disk, or all secondary disks in a consistency group.

### Clone a single disk

Clone a Asynchronous Replication disk using the methods described in [Create a disk clone](https://docs.cloud.google.com/compute/docs/disks/create-disk-from-source#create-clone).

### Clone all disks in a consistency group

Before you can clone secondary disks from a consistency group, you must [create a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group) in the secondary region for the disks that you want to clone, then [add the secondary disks to the consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#add_a_disk_to_a_consistency_group).

Clone all secondary disks in a consistency group using the Google Cloud console, the gcloud CLI, or REST.

###  Console 

Clone all secondary disks in a consistency group by doing the following:

  1. In the Google Cloud console, go to the **Asynchronous replication** page.

[Go to Asynchronous replication](https://console.cloud.google.com/compute/asynchronousReplication)

  2. Click the **Consistency groups** tab.

  3. Click the name of the consistency group that contains the secondary disks.

  4. Click **Clone consistency group**. The **Clone consistency group** window opens.

  5. Click **Clone consistency group**.




###  gcloud 

Clone all secondary disks in a consistency group using the [`gcloud compute disks bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/bulk/create):
    
    
    gcloud compute disks bulk create \
      --source-consistency-group-policy=CONSISTENCY_GROUP \
      --LOCATION_FLAG=LOCATION
    

Replace the following:

  * `CONSISTENCY_GROUP`: the URL of the consistency group that contains the secondary disks to clone. For example, `projects/PROJECT/regions/REGION/resourcePolicies/CONSISTENCY_GROUP_NAME`.
  * `LOCATION_FLAG`: the location flag for the disks in the consistency group. For regional disks, use `--region`. For zonal disks, use `--zone`.
  * `LOCATION`: the region or zone that the disks in the consistency group are located in. For regional disks, use the region. For zonal disks, use the zone. The clones are created in this location.



###  REST 

Clone all secondary disks in a consistency group using one of the following methods:

  * To clone zonal disks in a consistency group, use the [`disks.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/bulkInsert):
        
        POST https://compute.googleapis.com/compute/v1/projects/CLONE_PROJECT/zones/ZONE/disks/bulkInsert
        
        {
        "sourceConsistencyGroupPolicy": "projects/CONSISTENCY_GROUP_PROJECT/regions/CONSISTENCY_GROUP_REGION/resourcePolicies/CONSISTENCY_GROUP_NAME",
        }
        

  * To clone regional disks in a consistency group, use the [`regionDisks.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionDisks/bulkInsert):
        
        POST https://compute.googleapis.com/compute/v1/projects/CLONE_PROJECT/regions/REGION/regionDisks/bulkInsert
        
        {
         "sourceConsistencyGroupPolicy": "projects/CONSISTENCY_GROUP_PROJECT/regions/CONSISTENCY_GROUP_REGION/resourcePolicies/CONSISTENCY_GROUP_NAME",
        }
        




Replace the following:

  * `CLONE_PROJECT`: the project to create the disk clones in.
  * `ZONE`: the zone to create the disk clones in.
  * `REGION`: the region to create the disk clones in.
  * `CONSISTENCY_GROUP_PROJECT`: the project that contains the consistency group.
  * `CONSISTENCY_GROUP_REGION`: the region where the consistency group is located.
  * `CONSISTENCY_GROUP_NAME`: the name of the consistency group.



## What's next

  * Learn how to [manage consistency groups](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups).
  * Learn how to [manage replication](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-replication#start_replication).
  * Learn how to [failover and failback](https://docs.cloud.google.com/compute/docs/disks/async-pd/failover-failback).
  * Learn how to [monitor Asynchronous Replication performance](https://docs.cloud.google.com/compute/docs/disks/async-pd/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
