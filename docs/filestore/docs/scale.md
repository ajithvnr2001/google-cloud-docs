---
url: https://docs.cloud.google.com/filestore/docs/scale/
title: Scale capacity \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:25.794652+00:00
---

# Scale capacity  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/scale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Scale capacity Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to increase or decrease the capacity of your Filestore instances.

**Note:** For information about performance scaling, see the [performance documentation](https://docs.cloud.google.com/filestore/docs/performance#performance-scaling).

When using Filestore, we recommend that you [monitor the utilization of your Filestore instances](https://docs.cloud.google.com/filestore/docs/monitoring-instances) so that you can adjust capacity as needed. For example, if you notice that a zonal-tier instance with a higher capacity range (previously high scale SSD) no longer needs all of its allocated capacity, you may consider scaling it down. Similarly, if you notice that you are running out of capacity, you may want to scale up capacity to prevent your applications from breaking. If the file system runs out of inodes, you also need to add capacity. To check the inode usage, run:
    
    
      df -i
    

The command returns something similar to the following:
    
    
      Filesystem           Inodes  IUsed      IFree  IUse%  Mounted on
      10.0.0.2:/vol1    134217728     13  134217715     1%  /mnt/test
    

## Inode usage

Each file stored on the file share consumes one inode. If the file system runs out of inodes, you won't be able to store more files on the file share even if you haven't reached the maximum allocated capacity. The only way to add inodes is by adding capacity. However, reaching the maximum inodes is rare and is only a concern if you need to store numerous small files.

For a better understanding of an instance's available capacity, see [Anticipating capacity](https://docs.cloud.google.com/filestore/docs/monitoring-instances#anticpating-capacity).

## Differences in scaling behavior by service tier

Scaling an instance does not affect its availability and can be performed while the instance is in use. The following table shows how file share capacity can be scaled based on the [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers):

Service tier | Basic HDD | Basic SSD | Zonal, lower capacity | Zonal, higher capacity | Regional, lower capacity | Regional, higher capacity | Enterprise  
---|---|---|---|---|---|---|---  
Scaling direction | Up only | Up only | Up and down | Up and down | Up and down | Up and down | Up and down  
Scaling increment | 1 GiB | 1 GiB | 256 GiB | 2.5 TiB | 1 GiB | 2.5 TiB | 256 GiB  
Minimum capacity | 1 TiB | 2.5 TiB | 1 TiB | 10 TiB | 100 GiB | 10 TiB | 1 TiB  
Maximum capacity | 63.9 TiB | 63.9 TiB | 9.75 TiB | 100 TiB | 10,239 GiB | 100 TiB | 10 TiB  
  
Scaling the capacity of a zonal tier instance with a higher capacity range can take longer than enterprise and basic tier instances. The actual time required varies depending on the amount of data stored in the instance and the load on the Filestore instance. To ensure that your instances don't run out of capacity, perform these operations in advance.

When a scaling operation is taking place, you cannot cancel the operation or make any other edits to the instance, but read and write operations are uninterrupted. You also cannot scale an enterprise-tier and zonal-tier instance to a capacity level that's lower than what's needed for storing its existing file data and metadata. Attempting to do so results in an error.

## Instructions for editing an instance

###  Google Cloud console 

To edit Filestore instances using the Google Cloud console, navigate to the **Edit instance** page, where you can edit the instance description, manage IP-based access control rules, and scale the file share performance:

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the instance ID of the instance you want to edit.

  3. On the **Instance details** page, click **Edit** to go to the **Edit instance** page.

  4. In the **Edit capacity** field, enter the new capacity value.

  5. Click **Save**.




###  gcloud 

#### Before you begin

To use the gcloud CLI, you must either [install the Cloud SDK](https://docs.cloud.google.com/sdk/downloads) or use the Cloud Shell that's built into the Google Cloud console:

[Go to the Google Cloud console](https://console.cloud.google.com/)

#### `gcloud` command for editing an instance

You can edit a Filestore instance by running the [`instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/update) command.
    
    
     gcloud filestore instances update instance-id \
         --project="project-id" \
         --location=location \
         --file-share=name="file-share-name",capacity=file-share-size
    

where:

  * instance-id is the instance ID of the Filestore instance you want to edit.
  * project-id is the project ID of the Google Cloud project that contains the Filestore instance. You can skip this flag if the Filestore instance is in the `gcloud` default project. You can set the default project by running:
        
        gcloud config set project project-id
        

  * location is the location where the Filestore instance resides. For enterprise instances, specify a region. For all other instances, specify a zone. For example, `us-central1-a`.

Run the `gcloud filestore zones list` command to get a list of supported zones. You can skip this flag if the Filestore instance is in the `gcloud` default zone. You can set the default zone by running:
        
        gcloud config set filestore/zone zone
        

  * file-share-name is the name of the file share that is served from the Filestore instance. File share names cannot be changed after instance creation.

  * file-share-size is the new size you want for the file share. You can specify the file share size in whole numbers using either `GiB` (default) or `TiB`. For example, `10TiB`.

To see your available quota, go to the Quotas page in the Google Cloud console:

[Go to the Quotas page](https://console.cloud.google.com/iam-admin/quotas)

  * Optional: For a detailed list of available flags, see the [`gcloud filestore instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/update) reference page.




## What's next

  * [Known issues](https://docs.cloud.google.com/filestore/docs/known-issues)
  * [Troubleshoot performance-related issues](https://docs.cloud.google.com/filestore/docs/troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
