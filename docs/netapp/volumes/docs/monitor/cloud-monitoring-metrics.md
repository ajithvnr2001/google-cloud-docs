---
url: https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics/
title: Monitor NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:36.817668+00:00
---

# Monitor NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Monitor NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor Google Cloud NetApp Volumes resources and performance by collecting and analyzing metrics with Cloud Monitoring.

## Cloud Monitoring metrics

Various metrics for monitoring NetApp Volumes are available within [Cloud Monitoring](https://console.cloud.google.com/monitoring). Categories include volume, storage pool, and replication metrics.

You can select and chart individual metrics in [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer), create a dashboard with multiple charts, add alerting, or retrieve the metrics data with the Cloud Monitoring API.

## Monitored resources

`netapp.googleapis.com` precedes each monitored resource. For example, for **Volume** , the complete monitored resource is `netapp.googleapis.com/volume`.

Monitored resource | Resource metadata fields  
---|---  
`Volume` | `labels`  
  
`service_level`  
  
`storage_pool`  
  
`protocols`  
`StoragePool` | `labels`  
  
`service_level`  
`Replication` | `service_level`  
`BackupVault` | `backup_crypto_key_version`  
  
For Flex Unified ONTAP-mode, only the `StoragePool` resource is available. You must monitor all other resources within ONTAP.

## Resource metrics

`netapp.googleapis.com` precedes each metric. For example, the complete metric for `volume/bytes_used` metric is `netapp.googleapis.com/volume/bytes_used`.

Metrics are sampled and pushed to Cloud Monitoring every five minutes. In Cloud Monitoring Metrics Explorer, select a metric and use a minimum alignment period of five minutes for accurate results.

Metric name | Description | Monitored resource | Metric types | Unit  
---|---|---|---|---  
`/volume/backup_used` | Bytes backed up  
(baseline and   
incremental changes). | `/volume` |  | `byte`  
`/volume/bytes_used` | Capacity used to store  
data written as files and   
additional space used for  
snapshots. | `/volume` |  | `byte`  
`/volume/snapshot_bytes` | Capacity used   
for snapshots. | `/volume` |  | `byte`  
`/volume/allocated_bytes` | Capacity allocated to a volume  
from the storage pool. | `/volume` |  | `byte`  
`/volume/auto_tiering/tiered_bytes` | Auto-tiering volume used  
capacity by tiered types:  
cold or hot. | `/volume` | 

  * cold
  * hot

| `byte`  
`/volume/auto_tiering/cold_tier_read_byte_count` | Capacity read from the cold  
tier of the volume. | `/volume` |  | `byte`  
`/volume/auto_tiering/cold_tier_write_byte_count` | Capacity write to cold  
tier of the volume. | `/volume` |  | `byte`  
`/volume/operation_count` | Number of operations being   
performed on the volume by  
the clients. | `/volume` | 

  * read
  * write
  * metadata

| `1`  
`/volume/throughput` | Throughput for the  
operation type. | `/volume` | 

  * read
  * write
  * metadata

| `byte`  
`/volume/average_latency` | Volume I/O operation latency  
within the storage system | `/volume` | 

  * read
  * write
  * metadata

| `ms`  
`/volume/backup_current_transfer_bytes` | Amount of data transferred  
thus far for the current job. | `/volume` |  | `byte`  
`/volume/backup_healthy` | `FALSE` if a backup transfer is missed or failed. | `/volume` |  | `BOOL`  
`/volume/backup_last_transfer_duration` | Duration of the last transfer  
job. | `/volume` |  | `sec`  
`/volume/backup_last_transfer_size` | Size of the last transfer  
job. | `/volume` |  | `byte`  
`/volume/backup_transferring` | Status of backup:  
TRUE = transferring,  
FALSE = idle. | `/volume` |  | `BOOL`  
`/volume/inode_limit` | Inodes allocated for  
the volume (hard cap).   
  
Tied to allocated capacity  
(size) of the volume | `/volume` |  | `1`  
`/volume/inode_used` | Number of inodes in  
use on the volume. | `/volume` |  | `1`  
`/volume/throughput_limit` | Maximum throughput  
allocated for the volume. | `/volume` |  | `KiB/s`  
`/storage_pool/allocated` | Pool capacity allocated  
to volumes. | `/storagePool` |  | `byte`  
`/storage_pool/auto_tiering/tiered_bytes` | Storage pool capacity tiering  
types: cold, non cold. | `/storagePool` | 

  * cold
  * non-cold

| `byte`  
`/storage_pool/auto_tiering/cold_tier_read_byte_count` | Bytes read from the cold  
tier of the pool. | `/storagePool` |  | `byte`  
`/storage_pool/auto_tiering/cold_tier_write_byte_count` | Bytes written to the cold  
tier of the pool. | `/storagePool` |  | `byte`  
`/storage_pool/capacity` | Total size of the pool. | `/storagePool` |  | `byte`  
`/storage_pool/replication_status` | Status of replication for  
regional flex pools. 0 means  
out-of-sync , 1 means synced  
and 2 means catching-up. | `/storagePool` |  | `1`  
`/replication/healthy` | Values of `TRUE` if   
the relationship hasn't missed  
the last scheduled transfer  
and `FALSE` if a   
scheduled transfer is missed  
or is unhealthy. | `/replication` |  | `BOOL`  
`/replication/lag_time` | Time since snapshot for  
transfer was taken on   
source, including transfer duration. | `/replication` |  | `sec`  
`/replication/last_  
transfer_duration` | Duration of the last  
transfer job. | `/replication` |  | `sec`  
`/replication/last  
_transfer_size` | Size of the last transfer job. | `/replication` |  | `byte`  
`/replication/current  
/transfer_bytes` | Amount of data transferred   
thus far for the current job. | `/replication` |  | `byte`  
`/replication/transferring` | Status of replication: 

  * `TRUE` = Transferring
  * `FALSE` = Idle

| `/replication` |  | `BOOL`  
`/replication/total_  
transfer_byte_count` | Cumulative data transferred   
for the relationship since   
it was created. May reset to 0 | `/replication` |  | `byte`  
`/backup_vault/cmek_backup_rotation_state` | State of key rotation on  
the backup vault. | `/BackupVault` | State values 

  * 0 - Pending
  * 1 - In-progress
  * 2 - Completed
  * 3 - Failed

| `int`  
  
Cloud Monitoring also lets you set up alerting if metrics meet certain conditions. For example, you can use Cloud Monitoring to trigger administrative notifications before space in a volume runs out. See [Cloud Monitoring alerting](https://docs.cloud.google.com/netapp/volumes/docs/monitor/cloud-monitoring-metrics#resource_metrics).

## Track volume performance statistics with Cloud Monitoring

Cloud Monitoring tracks the following performance metrics per volume:

  * `/volume/operation_count`
  * `/volume/throughput`
  * `/volume/average_latency`



These metrics update every 5 minutes and provide an overview of performance trends for periods of one day or longer.

The metrics only reflect the service performance. Consider using monitoring tools available on the clients for more details. For example, the latency observed on the client may be higher than that reported by the service if the requests are queued up on the client before they are sent to the service.

## What's next

[Monitor volume usage](https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
