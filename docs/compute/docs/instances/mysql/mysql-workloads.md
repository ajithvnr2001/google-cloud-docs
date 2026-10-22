---
url: https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads/
title: Configure MySQL on Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:37.752443+00:00
---

# Configure MySQL on Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure MySQL on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine offers a range of different instance types and storage options for reading and writing data from your MySQL databases. To ensure that you achieve the best performance and cost for your database workloads, we recommend running on newer-generation infrastructure as a service (IaaS) products.

The following configuration recommendations take into account that MySQL workloads are often used in read-heavy systems, such as online transaction processing (OLTP) or the database backing a typical web application. They also account for common configuration choices, such as using version 8.0 or later of MySQL and using the [`InnoDB` storage engine](https://dev.mysql.com/doc/refman/8.4/en/innodb-introduction.html). For performance-sensitive workloads, you might need to adjust your configurations to fit. We recommend using this guide as a starting point for your deployment, and then testing with your actual workload to validate that your configuration meets your needs.

## Choose your virtual machine (VM)

For MySQL workloads, we recommend using the latest generation of C and N machine families, as they include shapes that work well for most practical MySQL configurations. For an introduction to these machine series, see the following [Google Cloud blog post](https://cloud.google.com/blog/products/compute/a-closer-look-at-compute-engine-c4-and-n4-machine-series). These machine families use [Titanium](https://cloud.google.com/titanium) and are based on [recent generations of Intel, AMD, and Axion processors](https://docs.cloud.google.com/compute/docs/cpu-platforms).

### Focus on performance

For performance-sensitive workloads, such as business-critical MySQL databases, we recommend the latest [C4](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) and [C4A](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) instances if they're available in your region. If you can't access them, the [C3](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_series) and [C3D](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_series) instances offer a similar focus on performance.

These instances offer the lowest and most consistent latency for compute-bound operations, and include the following useful features for performance-focused workloads:

  * Control over host maintenance events with [advance notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event)
  * Control of single-core turbo boosting for greater performance consistency
  * [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for higher network bandwidth



If you're using a C4A, C3, or C3D instance, you can also use Local solid-state drives (Local SSDs) to meet specific performance requirements.

### Optimize for cost

For workloads where your primary priority is optimizing cost, such as MySQL databases with low to medium levels of traffic or databases used in testing or development environments, we recommend that you use the latest N4 instances. These instances use Compute Engine's next generation _dynamic resource management_ to optimize your total cost while maintaining solid performance, without the strong guarantees that C4, C4A, C3, and C3D offer. For more details, see [Next generation dynamic resource management](https://docs.cloud.google.com/compute/docs/dynamic-resource-management).

## Configure your VM's size

For any VM that you use, it's important to choose the right VM size for the level of MySQL performance that you're aiming for.

If you're aiming for high write transaction per second (TPS) performance, the main factor to consider is your block storage. For more details, see Configure block storage, following on this page.

If you're aiming for high read queries per second (QPS) performance, we strongly recommend that you use MySQL's RAM-based buffer pool to cache hot data and reduce disk accesses. To maximize these benefits, take the following steps:

  * Choose a VM size that ensures that the _working set_ , or total amount of data that your database processes at once, fits into the buffer pool.
  * Size the buffer pool to use most of the RAM on the VM.



To minimize the cost of sizing your VM like this, we recommend using a VM with a high ratio of RAM to virtual CPUs (vCPUs), to avoid paying for vCPUs that you don't use.

For an ideal balance for most MySQL workloads, determine your workload's working set, then choose the smallest `highmem` instance shape that fits that working set in RAM. `highmem` instance shapes have about 8 GB of RAM per vCPU. This gives you enough memory to cache a large working set, while keeping enough CPU to handle a high query load.

For workloads with large working sets but low query rates, using N4 instances, you can further optimize your total cost by using [custom machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines#custom_machine_types) with [extended memory](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#extendedmemory) to further increase the RAM-to-vCPU ratio.

## Configure your VM's network bandwidth

For most MySQL use cases, you can stick to the default network bandwidth limits for your instance. If this works for your needs, you don't need to upgrade to `Tier_1` networking.

## Configure block storage

Google Cloud Hyperdisk is the only generation of durable block storage available for recent Compute Engine VM families. We believe that Hyperdisk Balanced is the best fit for the vast majority of MySQL workloads. For more information about Hyperdisk, visit the [Hyperdisk documentation](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).

### Google Cloud Hyperdisk

Hyperdisk Balanced offers the following features:

  * Solid state drive (SSD) latency at low cost
  * High-performance configurations for applications that need it
  * [Better than 99.999% durability](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#durability_hyperdisks) to protect against the industry-wide risk of hardware failure and silent data corruption
  * Encryption of all Hyperdisk data at rest with Google-managed or customer-managed encryption keys



#### Select your performance level

With Hyperdisk Balanced, you select your performance level independently from the storage size for the disk, so you can optimize your database's performance while only paying for the input/output (I/O) resources that your workload needs. If a MySQL database's buffer pool is larger than its working set, then during steady-state operations, it can serve almost all read queries out of the buffer pool, without touching the disk.

To select a performance level for your Hyperdisk volume, consider your MySQL write workload, with a particular emphasis on the following:

  * Access to `InnoDB` redo logs
  * Subsequent updates to `InnoDB` data files and indexes



Outside of steady-state operations, database maintenance events can also cause spikier disk performance. The frequency with which this occurs tends to scale with your database's write workload, so it's more likely in situations such as post-crash recovery using redo logs or a backup system that copies itself by reading all database changes since the last backup.

#### Size your disk

There are three common strategies for sizing your disk performance limits:

  1. **Use the default configuration.** Each disk comes with at least 3,000 input/output per second (IOPS) and 140 MiBps of throughput. This suffices for basic MySQL workloads and operating system (OS) boot volumes. If your use case outgrows this, you can [modify the volume's provisioned performance](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks) on-demand without stopping your workload.
  2. **Measure your existing usage.** If your database is already running in another environment, record its disk IOPS and throughput at a granularity of one minute or less. After you have one to two weeks of data, so that your sample set includes some fluctuation in load and normal maintenance events, select a high-percentile value from that dataset, and add a small buffer to account for organic growth or unexpected usage.
  3. **Estimate your needs, and then modify them later.** If you don't have an existing data source, you might have to estimate your performance needs initially, and then tune them further after deployment. We recommend provisioning a higher value than you think you'll need initially, so that your workload doesn't encounter performance bottlenecks, and then eventually reducing the provisioned performance to fit your workload.

**Caution:** To avoid performance bottlenecks, we recommend testing with your actual workload, or a simulation of it, before you put it into production.

#### Increase your disk's performance

You can increase each Hyperdisk Balanced disk's performance up to a maximum of 160,000 IOPS and 2,400 MBps of throughput. The size of your VM helps determine Hyperdisk's maximum performance limits, so if you want very high Hyperdisk performance, you might need to increase your VM's number of cores. If your most demanding workloads need higher disk performance than a single Hyperdisk Balanced disk can provide, you can use one of the following methods to stripe together multiple Hyperdisk Balanced disks:

  * Upgrade to Hyperdisk Extreme
  * Use a different software redundant array of independent disks (RAID) mechanism, such as [mdadm](https://en.wikipedia.org/wiki/Mdadm)



As you scale your MySQL databases, you can dynamically increase the capacity and performance of your disks without downtime. This helps the performance of online analytical processing (OLAP)-style workloads doing large complex joins which can't fit in RAM and spill to disk. In rare cases, MySQL workloads which require extremely low storage latency and can tolerate data loss can store their full dataset on Local SSD. You can also use the following hybrid solutions to improve read latency and limit reductions in durability:

  * Mirror your dataset between a Hyperdisk and a Local SSD.
  * Use a volume manager to configure Local SSD as a cache for data stored on an underlying Hyperdisk.



#### Take advantage of additional Hyperdisk features

Hyperdisk also gives you the following features, which can augment or simplify on-premises high availability and disaster recovery workflows:

  * [Synchronous](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) and [asynchronous](https://docs.cloud.google.com/compute/docs/disks/async-pd/about) replication
  * [Instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots)
  * [Clones](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks)
  * [Snapshots backed up to Cloud Storage](https://docs.cloud.google.com/compute/docs/disks/snapshots)



For more information about configuring these features with MySQL for Compute Engine, see the high availability section that follows on this page.

### Local SSDs

Some Compute Engine machine families let you use Local SSDs instead of Hyperdisk. These aren't durable storage, but MySQL workloads often use them to store [temporary tablespaces](https://dev.mysql.com/doc/refman/8.0/en/innodb-temporary-tablespace.html).

For information on using Local SSDs for scaling MySQL databases, see Dynamic disk resizing, which follows on this page.

## Additional Compute Engine features

You can use the following Compute Engine features to help optimize your MySQL deployment.

### Cloud Monitoring

To monitor your VM's performance and usage of infrastructure services, use Google Cloud console. On the **VM Instances** page, in the **Observability** tab, you can monitor performance-related metrics like CPU and memory utilization, networking bandwidth, and provisioned performance of your instances. Similarly, on the **Disks** page, in the **Observability** tab, you can monitor the throughput and IOPS of your disk volumes.

To customize the performance metrics that you see, use Cloud Monitoring to build queries. You can select the specific performance metrics that you want to view for your infrastructure services. For MySQL-specific metrics, Compute Engine offers a [MySQL workload plug-in](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#opsagent-mysql).

## Best practices for configuring your operating system

  * **Use an appropriate file system.** Google focuses on optimizing for Linux's ext4 and XFS file systems; however, most file systems are appropriate for use with MySQL.
  * **Turn off Transparent Huge Pages (THP) in your base operating system configuration.** For steps to turn off THP, see the [THP documentation](https://www.percona.com/blog/transparent-huge-pages-refresher).
  * **If you're using Linux, use the`relatime`, and `lazytime` flags for file system mount configuration.** This reduces performance overheads associated with updating the `atime`, `mtime`, and `ctime` values on files when they're read, modified, or have their metadata changed.



## Best practices for configuring MySQL

We recommend that you use the following configuration settings for MySQL.

  * **Use a recent version of MySQL.** Google focuses on optimizing for MySQL version 8.0 and later versions.
  * **Increase the size of the buffer pool.** MySQL uses its buffer pool to improve read performance by caching data in RAM, reducing disk accesses. By default, MySQL's buffer pool size is 128MiB, which is too small for most practical use cases. We recommend that you increase the size of [`innodb_buffer_pool_size`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_buffer_pool_size) to be larger than the size of the [working set](https://en.wikipedia.org/wiki/Working_set) that your application accesses in the database. This usually consists of the following steps:

    1. Measure or estimate the size of your working set on a running copy of your MySQL instance.
    2. Choose a virtual machine (VM) size and shape with enough RAM to fit that working set.
    3. Configure the size of the buffer pool on the VM to take up the majority of the available RAM.
  * **Turn on the doublewrite buffer.** MySQL has a [doublewrite buffer](https://dev.mysql.com/doc/refman/8.0/en/innodb-doublewrite-buffer.html) that helps protect against _torn writes_ , a failure mode where a write that covers multiple blocks on disk might only be partially committed if a hardware or power failure occurs in the middle of the write. To benefit from this protection, turn on [`innodb_doublewrite`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_doublewrite).

**Note:** In some scenarios, it's safe to turn off the doublewrite buffer. For more information, see Turn off the MySQL doublewrite buffer, following on this page.
  * **Set the value of[`innodb_flush_log_at_trx_commit`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit) to `1`.** This ensures that write transactions are durable on disk when they're committed.

  * **To reduce performance overhead, specify a value for[`innodb_flush_method`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_method).** For MySQL version 8.0.14 and later versions, set the value of `innodb_flush_method` to `O_DIRECT_NO_FSYNC`, which is optimal, but only present in these versions. For MySQL versions earlier than 8.0.14, set the value of `innodb_flush_method` to `O_DIRECT`.

  * **In high-availability replication scenarios, set the value of the primary database instance's[`sync_binlog`](https://dev.mysql.com/doc/refman/8.0/en/replication-options-binary-log.html#sysvar_sync_binlog) to `1`.** MySQL uses its binary log to communicate changes from the primary database to the secondary database, so this ensures that the binary logs are committed at transaction commit time, with the lowest possible replication lag and recovery point objective (RPO) between the databases.

  * **When using MySQL on C-series machine families, turn on[`innodb_numa_interleave`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_numa_interleave).** This ensures that MySQL's buffer pool can take advantage of non-uniform memory access (NUMA) policies.




### When to turn off the doublewrite buffer

MySQL's doublewrite buffer, which protects against torn writes, has a performance overhead of up to 25% for MySQL write transactions and can increase transaction latency. Google Cloud Hyperdisk offers built-in [torn write protection](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#torn-write-protection). If you're using MySQL to write directly to an ext4 file system running on Hyperdisk, then you can turn off the doublewrite buffer, provided that you correctly configured your file system and intermediate software layers.

For Hyperdisk's torn-write protection to be effective, you must configure the file system and other intermediate software layers between the database and the disk to avoid introducing torn writes above the disk layer. The following list provides examples of configurations that can introduce torn writes above the Hyperdisk layer:

  * Running your MySQL instance inside of containers, including Google Kubernetes Engine or self-hosted Kubernetes.
  * Storing your MySQL files on an XFS file system, which doesn't support large enough block sizes in most Linux kernel configurations.
  * Storing your MySQL files on a redundant array of independent disks (RAID) configuration that causes disk striping, including [`mdadm`](https://en.wikipedia.org/wiki/Mdadm) for Linux or [Storage Spaces](https://support.microsoft.com/en-us/windows/storage-spaces-in-windows-b6c8b540-b8d8-fb8a-e7ab-4a75ba11f9f2) and [Storage Spaces Direct](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/storage-spaces-direct-overview) for Windows.
  * Storing your MySQL files on top of a volume manager, including [Logical Volume Manager (LVM)](https://en.wikipedia.org/wiki/Logical_Volume_Manager_\(Linux\)) for Linux or Storage Spaces and Storage Spaces Direct for Windows.
  * Storing your MySQL files on Hyperdisk with a [Local solid-state drive (SSD)](https://cloud.google.com/products/local-ssd) configured as a cache, using `lvmcache`, `dm-cache`, or `bcache` for Linux or Storage Spaces for Windows.

**Note:** If you only store the MySQL temporary tablespace on Local SSD, there's no risk of introducing torn writes.
  * Running your MySQL instance inside of a VM using [nested virtualization](https://docs.cloud.google.com/compute/docs/instances/nested-virtualization/overview).




While you can set up the preceding configurations so that they don't introduce torn writes, we don't recommend that you turn off the doublewrite buffer when using them, because of the difficulty of validating that a given configuration is safe.

### (Optional) Turn off the doublewrite buffer

To turn off the doublewrite buffer, complete the following steps:

  1. On the ext4 file system, you must enable the [`bigalloc`](https://archive.kernel.org/oldwiki/ext4.wiki.kernel.org/index.php/Bigalloc.html) feature and configure the file system's cluster size to 16KiB, or a larger power of 2 multiple of 16KiB. This ensures MySQL's writes won't be broken up into separate IOs by the file system before being issued to Hyperdisk. Failing to raise the limit or using any value smaller than 16KiB won't protect against torn writes. As an example with 16KiB cluster size, this is configured at file system creation time:
         
         mkfs.ext4 -O bigalloc -C 16384 /dev/<device-name>
         

  2. Disable [`innodb_doublewrite`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_doublewrite) and set [`innodb_flush_method`](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_flush_method) to `O_DIRECT` or `O_DIRECT_NO_FSYNC` (depending on your version of MySQL as described above).




## Configure high availability (HA) and a backup solution

We strongly recommend that you protect all of your critical MySQL workloads by configuring high availability (HA) and backup solutions for them. For both HA and backup, the following factors are most important:

  * Your [Recovery Time Objective (RTO)](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Time_Objective), or how quickly you can recover from a failure.
  * Your [Recovery Point Objective (RPO)](https://en.wikipedia.org/wiki/IT_disaster_recovery#Recovery_Point_Objective), or how close before the time of the failure you're able to restore the data from.



HA solutions generally target near-zero RTO and RPO, but only protect against infrastructure failures. Backup solutions target longer RTO and RPO windows, but provide coverage for a larger set of failure scenarios, such as the following:

  * Accidental data deletion
  * Ransomware attacks
  * Natural disasters



### Configure high availability (HA)

HA features use storage and compute redundancy to ensure that your MySQL database has reduced downtime in the event of a host failure or outage, letting client applications access its data even when an instance or zone is unavailable.

MySQL allows replication in the following modes:

  * **Asynchronous mode.** In asynchronous mode, the primary acknowledges write transactions as soon as they're committed locally, so if there's an outage on the primary, then a small amount of recently-written data might be lost during failover, as the RPO is close to zero, but not actually zero.
  * **Semisynchronous mode.** In semisynchronous mode, the primary waits to acknowledge the transaction until a configurable number of replicas has acknowledged receipt of the transaction. This greatly increases the chance that no data loss occurs during an unplanned failover, as the RPO is effectively zero.



For both modes, RTO is determined by how quickly health checks do the following:

  1. Identify a failed instance.
  2. Trigger failover.
  3. Notify clients that the failover instance is now the primary, by using the domain name system (DNS) or another way of identifying the database server.



In either replication mode, you must have a failover instance to replicate to. You can locate that instance in any of the following places:

  * The same zone that the primary instance is located in
  * A different zone within the region that the primary is located in
  * A different region than the primary is located in



To maintain high availability even during zonal outages, we recommend the following configuration:

  * **Locate your primary and failover instances in different zones,** whether or not they're within the same region.
  * **Use asynchronous replication.** This is because, if you're using semisynchronous replication, locating your primary and failover instances in separate zones can cause high latency for write transaction commits.
  * **If you require zero RPO, use Hyperdisk Balanced High Availability** , which lets you synchronously replicate a disk across two zones in the same region. For details, see [Google's guide on providing HA services using Hyperdisk High Availability](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk). When you configure Hyperdisk Balanced High Availability, we recommend integrating with [Stateful Managed Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) to diagnose instance health issues and automate recovery actions.



### Configure a backup and data resilience plan

Backup and data resilience plans help to prevent data loss during failures like accidental data deletion, ransomware attacks, and natural disasters. You can also use them as cold storage for compliance and auditing requirements. For MySQL, there are many backup methodologies to choose from, some of which act at the database level, and some of which act at the storage volume level. As you select a methodology, you should primarily consider your RTO and RPO requirements.

#### Back up at the database level

For database-level backups, consider using the following options that MySQL provides:

  * **Incremental backups based on binary logging,** which create logical data dumps. These include the following: 
    * [mysqldump](https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html)
    * [mysqlpump](https://dev.mysql.com/doc/refman/8.0/en/mysqlpump.html)
  * **Tools that manage the backup process for you,** such as [MySQL Enterprise Backup](https://www.mysql.com/products/enterprise/backup.html).



For more information about MySQL's database-level backup options, see [Backup and Recovery](https://dev.mysql.com/doc/refman/8.0/en/backup-and-recovery.html) in the MySQL documentation.

For any of these options, you must have a secondary storage system to copy the backup data into. We recommend the following tools:

  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Filestore](https://docs.cloud.google.com/filestore)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)



#### Use Hyperdisk to snapshot and clone at the storage level

For storage-level backups, we recommend using Hyperdisk products to snapshot, clone, and otherwise capture a point-in-time view of your MySQL database. The RPO for this approach depends on how frequently you take snapshots of your database, and the RTO depends on which specific solution you use.

If fast recovery is important to you, and you only require backup coverage within a zone, we recommend that you use Hyperdisk's _instant snapshots_. Instant snapshots capture data at a specific point in time incrementally, and can rapidly restore the data to a new Hyperdisk volume through [disk cloning](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks), providing an RTO of minutes. They let you recover data when a disk's contents have been overwritten, deleted, or corrupted, and are available locally in the same zone or region as the source disk. For more information, see [About instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots)

For disaster recovery scenarios, in which data must be stored with higher redundancy than the original disk, and in a separate location to make sure that a single disaster doesn't affect all replicas of the data, we recommend that you use Hyperdisk's _archive and standard disk snapshots_. Archive and standard disk snapshots create a copy of the data in the disk at a point in time and store it with high redundancy in an immutable format. When you create multiple snapshots of a disk, such as with a [snapshot schedule](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules), Hyperdisk only stores incremental changes. Archive and standard disk snapshots are a good fit if you can tolerate higher RTO, because the data copy from snapshot storage back into VM storage can mean that they take a longer time to restore. For more information, see [Create archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).

Hyperdisk's instant snapshots and its archive and standard snapshots are both crash-consistent within a single disk. This means that when you restore from a snapshot, your MySQL database must run the normal [InnoDB recovery steps](https://dev.mysql.com/doc/refman/8.0/en/innodb-recovery.html) to bring its logs and data files back to a consistent state. Depending on the configuration of your InnoDB redo log, this can lengthen the RTO. The following patterns can further complicate your efforts to create a consistent database snapshot:

  * Your MySQL database files are spread across multiple volumes.
  * You're using Linux software RAID utilities, such as [`mdadm`](https://en.wikipedia.org/wiki/Mdadm).
  * You've separated MySQL's configured storage locations across filesystems on different disks.



To create a snapshot which doesn't require recovery after a snapshot restore, complete the following steps:

  1. Temporarily lock write access to the MySQL database.
  2. Flush all in-progress buffers to disk by using the [`LOCK INSTANCE FOR BACKUP`](https://dev.mysql.com/doc/refman/8.0/en/lock-instance-for-backup.html) and [`FLUSH TABLES WITH READ LOCK`](https://dev.mysql.com/doc/refman/8.0/en/flush.html#flush-tables-with-read-lock) commands.
  3. Initiate the snapshot operations.
  4. For multi-disk scenarios, after you've flushed at the MySQL level, execute the [`sync`](https://en.wikipedia.org/wiki/Sync_\(Unix\)) and `fsfreeze` commands on the server to flush all in-progress writes to disk and pause new incoming writes at the file system level.

**Note:** The MySQL commands and `fsfreeze` prevent data modification while they're in effect, so while the snapshot operation is in progress, to allow your database to continue write operations, you must release the respective locks in reverse acquisition order.



After you've captured the initial snapshot of your database, you don't need to continue locking your disk, because Hyperdisk rapidly captures the point-in-time view and then can asynchronously process any subsequent storage copying steps. If you need these steps for snapshot consistency, and you want to remove this write impact on the primary database, you can also run backup against a database replica rather than the primary database.

## What's next

  * For best practices and tips for running MySQL workloads on Compute Engine, see [Configure MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/mysql-workloads).
  * For more information about Cloud SQL, see the [Cloud SQL for MySQL documentation](https://docs.cloud.google.com/sql/docs/mysql).
  * Browse the MySQL installation options from Cloud Marketplace in the Google Cloud console:

[Go to Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?q=mysql)

  * To manually install MySQL on a Compute Engine instance, see [Install MySQL on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/mysql/setup-mysql).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
