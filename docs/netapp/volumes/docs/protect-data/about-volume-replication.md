---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication/
title: About volume replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:34.000294+00:00
---

# About volume replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  About volume replication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details for how to protect your data using volume replication.

## About volume replication

You can protect your data through cross-location volume replication, which asynchronously replicates a source volume in one location to a destination volume in a different location. This capability lets you use the replicated volume for critical application activity in case of a location-wide outage or disaster. The replicated volume can also be used as a read-only copy during normal usage.

Volume replication moves only used data blocks during the initial transfer, and only changed blocks transfer during incremental transfers. Only the bytes that transfer incur charges, which optimizes transfer times and lowers costs.

## Volume replication workflow

During volume replication, a process called **initial transfer** replicates all source volume content to the destination volume. The initial transfer process takes a snapshot on the source system and transfers its contents to the destination volume. After the initial transfer completes, the replication mirror status changes to **Mirrored**. As a result, the destination volume becomes read-only and reflects the contents of the source volume's snapshots, which includes all snapshots taken before the initial snapshot.

After the initial transfer process completes, the scheduled replication interval proceeds in the form of incremental updates in the following sequence:

  1. The process creates a new snapshot on the source volume.

  2. It calculates the data changed between the new and the previous snapshots.

  3. The process transfers these changes to the destination volume. The transfer status in the replication resource changes to **Transferring**.

After all the changes are transferred, the destination volume's contents transition from the old snapshot to the new snapshot.




## Settings modifications

As long as a replication is in a _mirrored_ state, any settings changes applied to either the source or destination volume are automatically applied to both volumes. However, the following settings aren't synchronized between the source and destination volumes:

  * **Labels and volume description** : these settings must be configured independently on the source and destination pools.

  * **Active Directory policy** : this policy is set on both the source and destination pools and can't be changed.

  * **CMEK policy** : this policy is set on both the source and destination pools and can't be changed.

  * **Backup policy** : this setting needs to be configured independently on both the source and destination volumes.

A backup schedule on a destination volume becomes active only once replication is stopped and it's inactive while the replication is in a _mirrored_ state.

  * **Backup vault** : this setting must be configured independently on the source and destination volumes.

  * **Auto-tiering** : this setting needs to be configured independently on the source and destination volumes.

  * **Make snapshot directory visible** : this setting can be configured only on the source volume. It can't be changed on destination volumes.

  * **Unix permissions** : this API parameter defines the initial UNIX permissions of the root inode, which is replicated to the destination volume during the replication process.

  * **Block volume deletion** : this setting must be configured independently on the source and destination volumes.

  * **Manual and auto QoS** : this setting can be configured manually or automatically, depending on the source and destination pool types. For volumes in an auto QoS pool, throughput is set by their size and service level. However, the throughput for volumes in a manual QoS pool can be configured on the source and destination volumes independently.




If the service level of the source volume is changed by moving it to a different pool, the destination volume isn't changed.

If the replication stops, the source and destination volumes become independent. Any data or settings changes made to either the source or destination volume aren't applied to the other volume. After resuming a stopped replication, the source volume settings overwrite the destination volume settings, with the exceptions listed in this section.

## Considerations for volume replication

Before you can perform a volume replication, consider the following:

  * For Standard, Premium, and Extreme service levels, NetApp Volumes supports volume replication between the following specific region pairs:

    * `asia-southeast1` and `australia-southeast1`

    * `europe-west2` and `europe-west3`

    * `europe-west2` and `europe-west4`

    * `europe-west3` and `europe-west4`

    * `europe-west3` and `europe-west6`

    * `europe-west4` and `europe-west6`

    * `europe-southwest1` and `europe-west3`

    * `northamerica-northeast1` and `northamerica-northeast2`

    * `northamerica-northeast1` and `us-central1`

    * `australia-southeast1` and `asia-southeast1`

    * `us-central1` and `us-east4`

    * `us-central1` and `us-west2`

    * `us-central1` and `us-west3`

    * `us-central1` and `us-west4`

    * `us-east4` and `us-west2`

    * `us-east4` and `us-west4`

    * `us-west2` and `us-west4`

    * `us-west3` and `us-west4`

  * For the Flex Unified service level, volume replication is supported between zones within the same region group. Replication to a different zone within the same region is also supported. The following table lists the region groups across different locations:

| **Locations**  
---|---  
| Americas | Asia-Pacific | Europe, Middle East, and Africa  
**Region group** |  `southamerica-east1`   
`us-central1`   
`us-east1`   
`us-east4`   
`us-east5`   
`us-south1`   
`us-west1`   
`us-west2`   
`us-west3`   
`us-west4` |  `asia-east1`   
`asia-northeast1`   
`asia-northeast2`   
`asia-south1`   
`asia-southeast1`   
`australia-southeast1`   
`australia-southeast2` |  `europe-southwest1`   
`europe-west1`   
`europe-west2`   
`europe-west3`   
`europe-west4`   
`europe-west9`   
`me-west1`  
  * For the Flex File service level, volume replication is supported between regions that are part of the same region group. The following table lists the region groups across different locations:

| **Locations**  
---|---  
| Americas | Asia-Pacific | Europe, Middle East, and Africa  
**Region group** |  `southamerica-east1`   
`southamerica-west1`   
`northamerica-northeast1`   
`northamerica-northeast2`   
`us-central1`   
`us-east1`   
`us-east4`   
`us-east5`   
`us-south1`   
`us-west1`   
`us-west2`   
`us-west3`   
`us-west4` |  `asia-east1`   
`asia-east2`   
`asia-northeast1`   
`asia-northeast2`   
`asia-northeast3`   
`asia-south1`   
`asia-south2`   
`asia-southeast1`   
`asia-southeast2`   
`australia-southeast1`   
`australia-southeast2` |  `africa-south1`   
`europe-central2`   
`europe-north1`   
`europe-southwest1`   
`europe-west1`   
`europe-west2`   
`europe-west3`   
`europe-west4`   
`europe-west6`   
`europe-west8`   
`europe-west9`   
`europe-west10`   
`europe-west12`   
`me-central1`   
`me-central2`   
`me-west1`  
  * **Quota assignment** : Depending on your project replication requirements, you might need to increase the quota for the number of replicated source and destination volumes for a specific region or service level. To request a quota increase, use the [Google Cloud console NetApp Volumes Quotas page](https://console.cloud.google.com/apis/api/netapp.googleapis.com/quotas).

  * **Topological support** : Volume replication doesn't support cascading and fan in and out topologies. For example, a volume can't be both a source and destination volume.

  * **Source and destination volume location** :

    * For the Flex Unified Default-mode service level: the following considerations are applicable.

      * Both source and destination volumes must be in the same project and region group. You can replicate volumes to another zone within the same region.

      * You can replicate volumes within regular Flex Unified pools or within large capacity Flex Unified pools, but not between these two pool types.

      * You can replicate volumes within the same project.

      * Cross-project volume replication between source and destination volumes is a feature available by request. To request access to this feature, contact [sales](https://cloud.google.com/contact). You create replications using the API, Google Cloud CLI, or Terraform, but you can manage them in the Google Cloud console. To create a cross-project replication, you need `netapp.replications.create` permissions for both projects. Unlike standard volume replications, cross-project replications don't replicate export rules between the source and destination volumes. If you use VPC Service Controls, see [Limitations of VPC Service Controls for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter#vpcsc-limitations) to understand cross-project volume replication.

    * For the Flex File service level: both the source and destination volumes must exist in the same project and region group. Replication to a different zone within the same region isn't supported.

    * For Standard, Premium, and Extreme service levels: the following considerations are applicable.

      * Replication is supported when both the source and destination volumes are within the same project. The destination volume must be in a different region pair.

      * Cross-project volume replication between source and destination volumes is a feature available by request. To request access to this feature, contact [sales](https://cloud.google.com/contact). While these replications are created using only API, Google Cloud CLI, or Terraform, their subsequent management can be done using the Google Cloud console. To create a cross-project replication, you need the `netapp.replications.create` permissions for both projects. Unlike general volume replications, cross-project replications don't replicate export rules between source and destination volumes. If you use VPC Service Controls, see [Limitations of VPC Service Controls for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter#vpcsc-limitations) to understand cross-project volume replication.

    * The source and destination volumes can exist in different VPCs.

  * **Service level-based support** : Source and destination volumes must have the same service level, except for volumes on Premium and Extreme service levels, which can be mixed in a replication. To replicate to or from Flex Unified ONTAP-mode, see [Replicate with ONTAP](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview), where the ONTAP-mode pool is the ONTAP system. Replication between ONTAP-mode systems or ONTAP-based systems and ONTAP-mode is standard ONTAP SnapMirror replication, which you must manage accordingly. For more information, see [Learn about ONTAP SnapMirror asynchronous disaster recovery](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-disaster-recovery-concept.html#data-protection-relationships).




## Volume replication pricing

NetApp Volumes charges for replication separately from volume capacity. Charges are based on the number of bytes transferred between primary and secondary volumes. For more information, see [NetApp Volumes pricing](https://cloud.google.com/netapp/volumes/pricing).

## Recovery point objective (RPO)

Since volume replication is a scheduled, asynchronous replication, the content of the destination volume always lags behind the source volume. The recovery point objective (RPO) specifies how current the data is on your destination volume and which point in time version of your data is stored. In case of a disaster, RPO helps you find out the amount of data you lost.

You can determine the RPO of volume replication by either checking lag times or replication snapshots. Though lag time provides a quick way to estimate RPO, replication snapshots are a more accurate measure.

  * **Lag time** : The elapsed time since the creation of the snapshot on the source volume that was last replicated to the destination volume. Lag time represents the difference in age of the destination volume data in relation to the source volume data. It updates every five minutes and provides an overview of the RPO. If your replication is skipping replication intervals, a warning warning icon displays next to the lag time in Google Cloud console. If it continues to occur, your data change rate on the source volume is too high to transfer within a replication interval. We recommend that you choose a longer replication interval or ignore the warning for one-off situations like heavy data modification activity on the source.

  * **Replication snapshots** : Replication snapshots are captures of data exactly as the data appears at a specific moment in time. Replication snapshots provide the most accurate look at RPO. Volume replication uses two rolling snapshots for replication. The timestamp of the latest replication snapshot on the destination volume specifies the point-in-time (UTC) of the latest data on destination volume.

You can derive the timestamp (`replication-<timestamp>`) from the replication snapshot name, which follows the UTC format (`YYYY-MM-DD-HHMMSS`).




### Requirements for storage pools

The storage pools with source and destination volumes must meet the following requirements:

  * Must be a part of a valid location pair or region group, depending on the service level

  * Must have the same Active Directory policy configuration

  * Must point to the same Active Directory

  * Must have the same LDAP settings




### Replication schedule

The replication schedule attempts to run the replication at designated intervals. If a previous replication is in progress, the replication for the current cycle skips and checks again at the next interval. This behavior is most common during the initial replication, which transfers the initial volume blocks and takes the longest time to replication. The replication schedule runs based on the following times for each schedule type:

Replication schedule frequency | Time of scheduled operation  
---|---  
Every 10 minutes | `:00, :10, :20, :30, :40, :50`  
Hourly | `:05` after the top of each hour  
Daily | `:10` after midnight each day  
  
## What's next

[Create a volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
