---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/manage-storage-pool/
title: Manage your storage pool \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:29.468456+00:00
---

# Manage your storage pool  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/manage-storage-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your storage pool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to edit storage pool settings or delete a storage pool.

## Edit storage pool settings

You can change the following settings after you create a storage pool:

  * **Storage pool capacity** : you can adjust capacity in 1 GiB increments.

    * **Standard, Premium, and Extreme service levels** : you can increase and decrease pool capacity. You can't decrease it below the total capacity of the attached volumes to the pool.

    * **Flex Unified and Flex File service levels** : you can increase pool capacity, but you can't decrease it. You can only increase capacity once every four hours.

  * **Performance** : pools with the Flex Unified or Flex zonal custom performance service levels let you adjust throughput. You can adjust throughput once every four hours.

  * **Active Directory policy** : you can attach an Active Directory policy to a pool that doesn't already have one. You can modify the Active Directory policy, but you can't replace an existing policy with a new one.

Adding an Active Directory policy doesn't affect existing volumes in a pool.

  * **Auto-tiering settings** : for Premium and Extreme pools, you can enable auto-tiering only once for a pool. This setting can't be changed after you enable it.

For Flex Unified and Flex File pools with custom-performance and auto-tiering, you can adjust the _Hot tier threshold_ by increasing its size. You can also enable or disable _auto-increase_.

  * **Pool description and labels** : you can change the pool description and manage its labels.




## Switch active and replica zones

Regional storage pools of the Flex Unified or Flex File service level replicate data synchronously between two zones. The active zone serves all volumes of the pool, while the replica zone acts as a standby. If the active zone stops working, NetApp Volumes automatically switches the NFS, SMB, or iSCSI service to the replica zone. While this switch happens after a brief I/O pause, file service operations resume without any data loss.

File service operations from clients in the previously active zone can have increased latency because of the cross-zone traffic with the newly active zone. Note that cross-zone exit from the clients can incur a Compute Engine inter-zone data transfer charge. For pricing information, see [Network Pricing](https://cloud.google.com/vpc/network-pricing).

You can also trigger a zone switch manually, and this can also cause an I/O pause.

### Limitations

The following limitations apply when a storage pool is in a switched-over state:

  * The storage pool upgrades are paused until the storage pool is switched back to the original zone.

  * Operations such as capacity, throughput, and IOPS updates aren't available until the pool is switched back to the original zone.




### Switch a zone

Use the following instructions to switch a zone manually using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Storage pools**.

  3. Click the name of the regional Flex Unified or Flex File storage pool you want to fail over.

  4. Click **Switch active/replica zones**.

  5. Review the current zone versus replica zone settings and the new settings that appear in the dialog.

  6. Click **Switch** to proceed.

  7. Read through the confirmation dialog and enter the name of the pool and then click **Switch**.




After the switch operation ends, your active zone and replica zone will have changed roles.

### gcloud

Switch a zone manually for a regional pool:
    
    
        gcloud netapp storage-pools switch POOL_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \

Replace the following information:

  * `POOL_NAME`: the name of the storage pool.

  * `PROJECT_ID`: the name of the project.

  * `LOCATION`: the location of the pool.




For more information about additional optional flags, see [Google Cloud SDK documentation on storage-pools switch](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/switch).

## Delete a storage pool

You can delete storage pools to control charges. Use the following instructions to delete a storage pool.

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Storage pools**.

  3. Select the storage pool you want to delete.

  4. Click **Delete**.

  5. To confirm deletion, enter the name of the storage pool.

  6. Click **Delete**.




## What's next

Read about [volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
