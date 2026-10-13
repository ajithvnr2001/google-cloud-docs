---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/database-performance-snapshot-report-reference/
title: Database performance snapshot report reference \u00a0|\u00a0 AlloyDB Omni using containers: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:34.788159+00:00
---

# Database performance snapshot report reference  |  AlloyDB Omni using containers: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/database-performance-snapshot-report-reference/

This page documents AlloyDB Omni version **18.1.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/database-flags)



Send feedback 

#  Database performance snapshot report reference Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/reference/database-performance-snapshot-report-reference)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/reference/database-performance-snapshot-report-reference)

This document describes wait events in AlloyDB Omni performance snapshot reports. For more information, see [Optimize database performance by comparing database snapshots](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/optimize-database-performance-compare-snapshots). 

## Wait events in snapshot reports

The following table describes wait events that are supported by AlloyDB Omni performance snapshot reports. You can use wait events to help you identify performance issues and bottlenecks in your database.

**Wait event name** | **Event class** | **Description**  
---|---|---  
ColumnarCacheInvalidatedBlockBuild | IPC | Builds the shared invalidated blocks and waits until all workers finish building.  
ColumnarCacheInvalidatedBlockCopy | IPC | Copies the shared invalidated blocks into private memory and waits until all workers finish copying.  
ColumnarCacheBloomFilterConsolidate | IPC | Consolidates the bloom filter into the bloom filter created in the shared memory, and waits until all workers finish consolidating.  
AdaptiveVacuumFreezeXid | IPC | Waits until vacuum advances the oldest frozen XID or until the timeout expires. After the timeout expires, this wait event throws an error telling you to wait  
for autovacuum or to manually perform the vacuum.  
  
AdaptiveVacuumNewXidDelay | Timeout | New transaction ID delay when the oldest transaction ID age indicates that new transactions are to be throttled.  
CommitWaitFlush | I/O | Transaction commits wait for the flush pointer advance before returning to the client.  
XlogAdvanceWALBuffer | I/O | Transaction waits for available space in the Write-Ahead Logging (WAL) buffer.  
AioWaitSegmentSwitch | I/O | WAL writer waits for WAL segment file switch in asynchronous I/O mode.  
WalFlushDueToBufferReplacement | I/O | WAL flush due to buffer replacement.  
WalFlushOnBufEvictUnderExtend | I/O | WAL flush on buffer eviction under [lock:extend](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-LOCK-TABLE).  
WalFlushWhileTruncatingCLOG | I/O | WAL flush while truncating the commit log ([CLOG](https://pgpedia.info/c/clog.html)).  
WalFlushWhileTruncatingMultiXactData | I/O | WAL flush while truncating MultiXact Data.  
WalFlushDueToSLRUPageReplacement | I/O | WAL flush due to simple least-recently used (SLRU) page replacement.  
WalFlushByDDL | I/O | WAL flush by Data Definition Language (DDL).  
WalFlushDuringCheckPoint | I/O | WAL flush during checkpoint.   
  
A _checkpoint_ is the point in the write-ahead log sequence during which all data files are updated to reflect the information in the log. For more information, see [Checkpoint](https://www.postgresql.org/docs/current/sql-checkpoint.html).   
WalFlushBySmgrOperations | I/O | WAL flush by storage manager operations.  
WalFlushWhileReservingReplicationSlot | I/O | WAL flush while reserving a replication slot.  
WalFlushWhileSwitchingWALSegment | I/O | WAL flush while switching WAL segments.  
WalFlushByRelmapFile | I/O | WAL flush by the relation mapping file.  
VacuumDelayRead | I/O | Adaptive vacuum read delay.  
VacuumDelayWrite | I/O | Adaptive vacuum write delay.  
UltraFastCachePRead | I/O | Latency of a read from the AlloyDB UltraFast Cache.  
UltraFastCachePWrite | I/O | Latency of a write to the AlloyDB UltraFast Cache  
WalBatchWrite | I/O | Wait time for a minimal batch size to write WAL.  
StorageAwaitMayWrite | I/O | Time spent waiting for AlloyDB storage to process logs and allow more writes.  
StorageAdvanceFlushPosition | I/O | Time spent waiting to advance the flush position of AlloyDB storage.  
StorageDataFilePrefetch | I/O | Latency of prefetch reads from AlloyDB storage.  
StorageInProgressDataFileRead | I/O | Appears in `pg_stat_activity` while a storage read is in progress.   
StorageDataFileReadUncached | I/O | Latency of a read from AlloyDB storage.  
StorageQueryRelations | I/O | The time it takes to read relation sizes from storage.  
StorageLocalFileInit | I/O | The time it takes to read files data from storage and write to local files during startup.  
StorageWaitWalLogParsing | I/O | The time it takes to parse logs for AlloyDB storage.  
StorageWaitWalBufferSpace | I/O | Time spent waiting for space to free up in the AlloyDB storage buffer.  
StorageReadDir | I/O | The time it takes to read a directory's contents from one storage shard.  
  
## What's next

  * [Optimize database performance by comparing database snapshots](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/optimize-database-performance-compare-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
