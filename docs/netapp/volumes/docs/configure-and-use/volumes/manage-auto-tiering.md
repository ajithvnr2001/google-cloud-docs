---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering/
title: Manage auto-tiering \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:30.338737+00:00
---

# Manage auto-tiering  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage auto-tiering Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details on managing auto-tiering.

## About auto-tiering

Auto-tiering reduces the overall storage costs of volume usage. NetApp Volumes automatically moves infrequently used data to a slower, cost-efficient storage tier.

You can enable auto-tiering at the per volume level. When auto-tiering is enabled for a volume, NetApp Volumes identifies data that is infrequently used and moves that cold data from the primary _hot tier_ to a cheaper but slower _cold tier_. Your active data stays on the hot tier.

As a user, you create a volume with the right size to hold all of your data. Whether the data is located on the hot tier or cold tier, it is managed automatically by the volume and is transparent to an application or user accessing the volume using NFS or SMB. You can always see the full dataset.

NetApp Volumes determines whether to move cold data to the hot tier based on the access pattern. Reading the cold data with sequential reads, such as those associated with data copy, file-based backups, indexing, and antivirus scans, leaves the data on the cold tier. Reading the cold data with random reads moves the data back to the hot tier. This data stays in the hot tier until it cools off again.

Reading hot-tier data from the volume, whether you access it sequentially or randomly, resets the block temperature for those blocks and restarts the cooling process. If you need to run full-volume sequential file reads for antivirus scans, file-based backups, indexing, or similar tasks on the hot tier, schedule them less often than the configured cooling period.

For Premium and Extreme pools, auto-tiering can be enabled during storage pool creation or on existing pools. Once auto-tiering is enabled at the pool level, you must explicitly enable it for each volume. After auto-tiering is enabled on a pool or volume, it can't be disabled; but it can be paused and resumed on a per-volume basis.

For Flex Unified and Flex File custom performance pools, you can enable auto-tiering during storage pool creation or on existing pools. Both Flex Unified and Flex File require that you manage the pool and hot tier size. When you enable auto-tiering on an existing pool, the current pool size becomes the hot tier size. You can grow the pool beyond the hot tier size to accommodate cold data. Once you enable auto-tiering on a storage pool, you can create new volumes with or without auto-tiering; it's enabled by default. If you don't want auto-tiering enabled during volume creation, you must explicitly disable it.

Once auto-tiering is enabled on a volume, it can only be paused, but not disabled.

You can configure how long data remains _hot_ before being considered _cold_ by using a volume-specific _Cooling threshold_ parameter. The cooling threshold can be set between 2 to 183 days. The default cooling threshold is 31 days. Data that is cooled beyond the cooling threshold moves to the cold tier once a day.

### Auto-tiering considerations

The following considerations apply while you use auto-tiering:

  * When you use volume replication, the auto-tiering capability is controlled independently for the source and destination volume.

  * On storage pools with auto-tiering enabled, the cold block tracking will occur on existing volumes that don't have auto-tiering enabled. If you enable auto-tiering on these volumes, the old data immediately becomes eligible for tiering and might get moved to the cold tier on the next day.

  * For iSCSI volumes, auto-tiering applies only to snapshot data. Used blocks from the LUN won't be tiered, regardless of how often they are read. This helps ensure consistent latency.




## Performance and hot tier sizing

As a volume administrator, you must manage the auto-tiering parameters to achieve your capacity, performance, and cost objectives. This sizing workflow depends on the service level of the storage pool you want to auto-tier.

### Premium or Extreme type volumes

The performance of an auto-tiered volume depends on the sizes of the hot and cold tiers. Each GiB of hot tier size adds throughput capability of 64 KiBps for the Premium service level or 128 KiBps for the Extreme service level to the volume. While each GiB of cold tier size adds 2 KiBps of throughput capability to the volume with increased access latency. If you need more performance, just add additional capacity to the volume, as empty space in the volume is counted as hot tier capacity.

The hot tier consistently stores all inode metadata required for file and folder listing, as well as timestamp information.

### Flex type volumes

Auto-tiering is available for Flex Unified and Flex File custom-performance pools. You can enable it during storage pool creation or on existing pools. When enabling auto-tiering on an existing pool, you must select a hot-tier size that matches the current storage pool size. All volumes in the pool share the performance capability set at the pool level.

When creating a storage pool as an administrator, you must specify the size of the hot tier threshold as an additional parameter. The minimum size of the hot tier is 1 TiB. You must ensure that the hot tier has sufficient capacity to store your active data. If the hot tier is too small and data is written faster than the rate at which it cools and moves to the cold tier, the hot tier might become full. This can cause your applications to receive out-of-space write errors. Therefore, proper sizing and continuous monitoring are essential.

You can monitor hot tier size manually or enable a hot tier _auto-increase_ on the pool. When enabled, the hot tier automatically increases size by 10% when full, up to the storage pool's total size. Note that the size of a pool's hot tier can't be decreased. Therefore, avoid applying workloads that migrate large datasets of cold data into the pool. Otherwise, your hot tier will continue to grow, reducing your auto-tiering cost savings.

**Note:** Modifying the pool capacity, IOPS, or throughput might fail for up to four hours after an automatic increase in the hot tier threshold. If this occurs, wait four hours and retry the operation.

To prevent the hot tier from filling up from large cold data writes into a volume, especially during data migration, a hot tier bypass flag can be enabled to direct writes straight to the cold tier, bypassing the hot tier. Once the migration is finished, you can disable the flag and resume normal operation, where writes go to the hot tier first. Active data that bypassed the hot tier during migration is moved back to the hot tier upon the first random access.

The hot tier consistently stores all inode metadata required for file and folder listing, as well as timestamp information.

## Choose the right cooling threshold

The data block access frequency is monitored in 4 KiB intervals. Each day without access to a block makes it colder, and its temperature is measured in days. When a block's temperature reaches the cooling threshold value configured on the volume, the block is eligible to be moved to the cold tier. Only eligible blocks are moved to the cold tier daily. If the block is randomly accessed, the temperature is set to 0 days and the cooling cycle starts again.

The cooling threshold is defined at the volume level and can be set between 2 to 183 days for the Flex, Premium, and Extreme volumes.

Data on the cold tier is priced lower than data on the hot tier. Using a shorter cooling threshold moves data to the cold tier sooner, which can reduce the overall costs. Although setting the lowest cooling threshold appears beneficial, setting it too short might yield limited cost savings.

Data on the cold tier is slower to access than data on the hot tier. Using a cooling threshold which is too short can make access to your data slower. The overall volume performance depends on the hot tier capabilities.

Moving the data to and from the cold tier has data transfer costs. If you choose a short cooling threshold, data can move more frequently between the hot and cold tiers, which reduces the volume performance and increases the overall cost.

Using a cooling threshold that is too short can cause problems. The default cooling threshold value is 31 days.

## Auto-tiering pricing

Your billing is based on the allocated hot tier and utilized cold tier, each charged at their respective rate. For more information about pricing, see [Storage pool pricing](https://cloud.google.com/netapp/volumes/pricing).

The storage pool billing is based on the total cold tier size of all volumes within that pool. This total cold tier storage is then charged at the cold tier pricing, which is significantly less than the hot tier pricing.

The hot tier pricing depends on the type of service level:

  * For the Premium and Extreme service levels: the hot tier size is calculated as the _total pool capacity minus the cold tier size_ and is charged at the pool's hot tier pricing. If the pool's hot tier size is smaller than 2 TiB, then a minimum of 2 TiB is charged at the hot tier rate, and the remaining capacity is charged at the cold tier rate.

  * For the Flex service level: the allocated hot tier capacity is charged at the pool's hot tier pricing.




Auto-tiering doesn't affect the throughput and IOPS capability of the Flex Unified and Flex File custom-performance pools, but accessing cold data results in higher latency and reduced throughput.

Additionally, there is a charge for network traffic associated with moving data to or from the cold tier. For more information about pricing, see [Storage pool pricing](https://cloud.google.com/netapp/volumes/pricing).

## Enable auto-tiering

For volumes in storage pools with auto-tiering enabled, an **Auto-tiering** tab is displayed in the volume level details page. This indicates if tiering is enabled or disabled for the volume. If you click this tab, you can look up statistics, manage auto-tiering settings, and pause or unpause the tiering.

### Look up tiering statistics

NetApp Volumes provides auto-tiering statistics at both the volume and storage pool levels.

#### Volume level statistics

You can view the tiering statistics of a volume using Google Cloud console, Google Cloud CLI, or Cloud Monitoring.

Use the following instructions to look up tiering statistics of a volume using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click the name of the volume.

  3. If tiering is enabled on the volume, an **Auto-tiering** tab is displayed. Select the tab.

  4. Review the **Current hot tier data** and **Current cold tier data** fields.




### gcloud

Look up tiering statistics of a volume:
    
    
      gcloud netapp volumes describe VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --format="table(capacityGib,hotTierSizeUsedGib,coldTierSizeGib)"

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For Flex service levels, the command shows the size of the hot tier and the cold tier. For Premium and Extreme service levels, the hot tier size isn't displayed. The size of the hot tier can be calculated by _capacityGib minus coldTierSizeGib_.

For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/describe).

### Cloud Monitoring

Cloud Monitoring receives auto-tiering statistics for Premium and Extreme volumes, which can be visualized using metrics explorer or dashboards. The available metrics include the following:

  * `/volume/auto_tiering/tiered_bytes`: specifies the number of bytes stored in the hot tier and the cold tier. You can filter this metric using the `tier` label to view data for the hot tier or the cold tier.

  * `/volume/auto_tiering/cold_tier_read_byte_count`: the number of bytes read from the cold tier.

  * `/volume/auto_tiering/cold_tier_write_byte_count`: the number of bytes written to the cold tier.




For more information, see [Cloud Monitoring](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics).

#### Storage pool level statistics

Cloud Monitoring receives auto-tiering statistics for Premium and Extreme pools, which can be visualized using metrics explorer or dashboards. The available metrics include the following:

  * `/storage_pool/auto_tiering/tiered_bytes`: specifies the number of bytes stored in the hot tier and the cold tier. You can filter this metric using the `tier` label to view data for the hot tier or the cold tier.

  * `/storage_pool/auto_tiering/cold_tier_read_byte_count`: the number of bytes read from the cold tier.

  * `/storage_pool/auto_tiering/cold_tier_write_byte_count`: the number of bytes written to the cold tier.




For more information, see [Cloud Monitoring](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics).

### Edit auto-tiering parameters

Use the following instructions to edit the tiering parameters of a volume using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click the name of the volume.

  3. If tiering is enabled on the volume, an **Auto-tiering** tab is shown. Select the tab.

     * If tiering is enabled, click **Pause auto-tiering** to pause it.

     * If tiering is paused, click **Resume auto-tiering** to resume it.

  4. For Flex Unified and Flex File volumes, complete the following steps to enable or disable **Hot tier bypass** :

     1. Click the **Edit** icon (edit) next to **Hot tier bypass**. In the dialog that opens, select or clear the **Enable hot tier bypass** checkbox.

     2. Click **Save**.

  5. To change the cooling threshold, click **Edit cooling threshold** and enter a new value. Click **Save**.

**Important:** You can't change the cooling threshold while **Hot tier bypass** is enabled.



### gcloud

Edit the auto-tiering parameters using the following command:
    
    
      gcloud beta netapp volumes update VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION \
       --tiering-policy=tier-action=ENABLED_OR_DISABLED,cooling-threshold-days=DAYS,enable-hot-tier-bypass-mode=ON_OR_OFF

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.


**Note:** The `enable-hot-tier-bypass-mode` flag is available only in `gcloud beta`.

For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/update).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Modify an ONTAP volume's default FabricPool tiering policy](https://docs.netapp.com/us-en/ontap/fabricpool/migration-controls-override-tiering-policy-task.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

  * [Connect SMB clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients).

  * [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

  * [Connect iSCSI clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients).

  * [Connect large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
