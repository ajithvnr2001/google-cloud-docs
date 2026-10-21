---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices/
title: Best practices for SQL Server instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:50:15.788837+00:00
---

# Best practices for SQL Server instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for SQL Server instances Stay organized with collections  Save and categorize content based on your preferences. 

You can apply several best practices to optimize Compute Engine instances that run Microsoft SQL Server. To learn how to set up a high-performance SQL Server instance, read [Creating a high-performance SQL Server instance](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance).

## Use Workload Manager to evaluate and deploy SQL Server

SQL Server evaluation in [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/about-evaluations) provides you the ability to scan your SQL Server deployments with a set of predefined Google Cloud recommendations for optimal performance directly from the Google Cloud console. For more information, see [Agent for SQL Server setup instructions](https://docs.cloud.google.com/workload-manager/docs/set-up-agent-for-sql-server).

The [Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment) tool in Workload Manager lets you configure and deploy enterprise applications on Google Cloud. You can also use Guided Deployment Automation to configure a deployment for your workload, and then generate Terraform and Ansible infrastructure as code (IaC) that you can export for further customization or use in an existing deployment pipeline. For more information, see [Guided Deployment Automation](https://docs.cloud.google.com/workload-manager/docs/deploy/about-wlm-deployment).

## Configure Windows

This section describes how to optimize the Microsoft Windows operating system for SQL Server performance when running on Compute Engine.

### Set up Windows firewall

**Best practice:** Use the Windows Server Advanced Firewall, and specify the IP addresses of your client computers.

The Windows Advanced Firewall is an important security component in Windows Server. When you set up your SQL Server environment so that it can connect to the database from other client machines, configure the firewall to allow incoming traffic:
    
    
    netsh advfirewall firewall add rule name="SQL Access" ^
    dir=in action=allow ^
    program="%programfiles%\Microsoft SQL Server\MSSQL12.MSSQLSERVER\MSSQL\Binn\sqlservr.exe" ^
    remoteip=LOCAL_SUBNET
    

When you use this firewall rule, it is a good practice to specify the IP address of your client machines. Specify a comma-delimited list of IP addresses without blank spaces for the `remoteip` parameter in place of `LOCAL_SUBNET`. Also, note that the path for the `program` parameter might change depending on the version of SQL Server that you use.

The SQL Server application image includes a `SQL Server` Windows firewall rule. This rule is fairly unrestricted, so consider disabling it before your system goes to production.

### Tune network connections

**Best practice:** Use the operating system's default network settings.

The default network settings on most operating systems are configured for connections on small computers that are connected to moderately fast networks. Such settings are usually sufficient. Furthermore, conservative defaults make sure that network traffic doesn't overwhelm the network and connected computers.

On Compute Engine, compute instances are attached to a [network designed by Google](http://googleresearch.blogspot.com/2015/08/pulling-back-curtain-on-googles-network.html) that offers high capacity and performance. The physical servers running your Compute Engine instances are highly optimized to take advantage of this network capacity. The virtual network drivers in your instances are also optimized, which makes the default values sufficient for most use cases.

### Install antivirus

**Best practice:** Follow the Microsoft guidance for antivirus software.

If you are running Windows, you should be running some antivirus software. Malware and software viruses present a significant risk to any system connected to a network, and antivirus software is a simple mitigation step you can use to protect your data. However, if the antivirus software is not configured correctly, it can negatively impact your database performance. [Microsoft provides advice about how to choose antivirus software](https://learn.microsoft.com/en-US/troubleshoot/sql/database-engine/security/antivirus-and-sql-server).

## Optimize for performance and stability

This section provides information about how to optimize SQL Server performance on Compute Engine and describes operational activities to help keep it running smoothly.

### Move data files and log files to a new disk

**Best practice:** Use a separate SSD persistent disk for log and data files.

By default, the preconfigured image for SQL Server comes with everything installed on the boot persistent disk, which mounts as the `C:` drive. Consider [attaching a secondary SSD persistent disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk#create_disk) and moving the log files and data files to the new disk.

### Use a Local SSD to improve IOPS

**Best practice:** Create new SQL Server instances with one or more [local SSDs](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#create_local_ssd) to store the `tempdb` and Windows paging files.

The ephemeral nature of local SSD technology makes it a poor candidate for use with your critical databases and important files. However the `tempdb` and Windows paging file are both temporary files, so both are great candidates to move to a local SSD. This offloads a significant number of I/O operations from your SSD persistent disks. For more information about setting this up, see [Setting up TempDB](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance#setting_up_tempdb).

### Parallel query processing

**Best practice:** Set the `max degree of parallelism` to `8`.

The recommended default setting for `max degree of parallelism` is to match it to the number of CPUs on the server. However, there is a point where breaking a query into 16 or 32 chunks, executing them all on different vCPUs and then consolidating it all back to a single result takes a lot more time than if only one vCPU had run the query. In practice, 8 works as a good default value.

**Best practice:** Monitor for `CXPACKET` waits and incrementally increase `cost threshold for parallelism`.

This setting goes hand in hand with `max degree of parallelism`. Each unit represents a combination of CPU and I/O work required to perform a query with a serial execution plan before it is considered for a parallel execution plan. The default value is 5. Although we give no specific recommendation to change the default value, it is worth keeping an eye on and, if necessary, increasing it incrementally by 5 during load testing. One key indicator that this value might need to be increased is the presence of `CXPACKET` waits. Although the presence of `CXPACKET` waits does not necessarily indicate that this setting should change, it's a good place to start.

**Best practice:** Monitor for different wait types, and adjust the global parallel processing settings or set them at the individual database level.

Individual databases can have different parallelism needs. You can set these settings globally, and set `Max DOP` at the individual database level. You should observe your unique workloads, monitor for waits, and then adjust the values accordingly.

[The SQLSkills site](https://www.sqlskills.com/help/sql-server-performance-tuning-using-wait-statistics/) offers a useful performance guide that covers wait statistics inside the database. Following this guide can help you understand what is waiting and how to mitigate the delays.

### Handle transaction logs

**Best practice:** Monitor the growth of the transaction log on your system. Consider disabling autogrowth and setting your log file to a fixed size, based on your average daily log accumulation.

One of the most overlooked sources of performance loss and intermittent slowdowns is the unmanaged growth of the transaction log. When your database is configured to use the `Full` recovery model, you can perform a restore to any point in time, but your transaction logs fill up faster. By default, when the transaction log file is full, SQL Server increases the size of the file to add more empty space to write more transactions and blocks all activity on the database until it finishes. SQL Server grows each log file based off of its **Maximum File Size** and the **File Growth** setting.

When the file has reached its maximum size limit and cannot grow, the system issues a [9002 error](https://msdn.microsoft.com/en-us/library/ms175495.aspx) and puts the database into read-only mode. If the file can grow, SQL Server expands the file size and zeroes out the empty space. The setting for **File Growth** defaults to 10% of the log file's current size. This is not a good default setting for performance because the larger your file grows, the longer it takes to create the new, empty space.

**Best practice:** Schedule regular backups of the transaction log.

Regardless of the maximum size and growth settings, schedule regular [transaction log backups](https://msdn.microsoft.com/en-us/library/ms179478\(v=sql.120\).aspx), which, by default, truncates old log entries and lets the system reuse existing file space. This simple maintenance task can help to avoid performance dips at your peak traffic times.

### Optimize Virtual Log Files

**Best practice:** Monitor Virtual Log File growth and take action to prevent log file fragmentation.

The physical transaction log file is segmented into Virtual Log Files (VLF). New VLFs are created every time the physical transaction log file has to grow. If you did not disable auto-growth, and growth is happening too frequently, too many VLFs are created. This activity can result in log file fragmentation, which is similar to disk fragmentation and can adversely affect performance.

SQL Server 2014 introduced a more efficient algorithm for determining how many VLFs to create during auto-growth. Generally, if the growth is less than 1/8 the size of the current log file, SQL Server creates one VLF within that new segment. Previously, it would create 8 VLFs for growth between 64 MB and 1 GB, and 16 VLFs for growth over 1 GB. You can use the TSQL script below to check how many VLFs your database currently has. If it has thousands of files, consider manually shrinking and resizing your log file.
    
    
    --Check VLFs substitute your database name below
    USE YOUR_DB
    DECLARE @vlf_count INT
    DBCC LOGINFO
    SET @vlf_count = @@ROWCOUNT
    SELECT VLFs = @vlf_count
    

You can read more about VLFs on [Brent Ozar's website](https://www.brentozar.com/blitz/high-virtual-log-file-vlf-count/).

### Avoid index fragmentation

**Best practice:** Regularly defragment the indexes on your most heavily modified tables.

The indexes in your tables can become fragmented, which can lead to poor performance of any queries using these indexes. A regular maintenance schedule should include reorganizing the indexes on your most heavily modified tables. You can run the following Transact-SQL script for your database to show the indexes and their fragmentation percentage. You can see in the example results that the `PK_STOCK` index is 95% fragmented. In the following 'SELECT' statement, replace 'YOUR_DB' with the name of your database:
    
    
    SELECT stats.index_id as id, name, avg_fragmentation_in_percent
    FROM sys.dm_db_index_physical_stats (DB_ID(N'YOUR_DB'), NULL, NULL, NULL, NULL) AS stats
        JOIN sys.indexes AS indx ON stats.object_id = indx.object_id
          AND stats.index_id = indx.index_id AND name IS NOT NULL;
    
    RESULTS
    -------------------------------
    Id    name          avg_fragmentation_in_percent
    -------------------------------
    1 ORDERS_I1 0
    2 ORDERS_I2 0
    1 ORDER_LINE_I1 0.01
    1 PK_STOCK95.5529819557039
    1 PK_WAREHOUSE0.8
    

When your indexes are too fragmented, you can reorganize them by using a basic `ALTER` script. Here is an example script that prints the `ALTER` statements you can run for each of your tables' indexes:
    
    
    SELECT
    'ALTER INDEX ALL ON ' + table_name + ' REORGANIZE;
    GO'
    FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = 'YOUR_DB'
    

Choose the tables from the result set that have the highest fragmentation, and then execute those statements incrementally. Consider scheduling this or a similar script as one of your regular maintenance jobs.

If you are restoring a database from another location to Google Cloud, you should rebuild, or at least reorganize, the indexes, then update usage. Replace `YOUR_DB` with the name of your database: 
    
    
    dbcc updateusage (YOUR_DB) GO USE YOUR_DB
    GO

### Format secondary disks

**Best practice:** Format secondary disks with a 64 KB allocation unit.

SQL Server stores data in units of storage called [extents](https://docs.microsoft.com/en-us/sql/relational-databases/pages-and-extents-architecture-guide?view=sql-server-ver15#extents). Extents are 64 KB in size and are made up of eight, contiguous memory pages that are also 8 KB in size. Formatting a disk with a 64 KB allocation unit lets SQL Server read and write extents more efficiently, which increases I/O performance from the disk.

To format secondary disks with a 64 KB allocation unit, run the following PowerShell command, which searches for all new and uninitialized disks in a system and formats the disks with the 64 KB allocation unit:
    
    
    Get-Disk | Where-Object {$_.PartitionStyle -eq 'RAW'} | Initialize-Disk -PartitionStyle GPT -PassThru | New-Partition -AssignDriveLetter -UseMaximumSize | Format-Volume -FileSystem NTFS -AllocationUnitSize 65536 -Confirm:$FALSE
    

## Back up data

**Best practice:** Backup your data regularly using Google's backup and disaster recovery solutions for optimal protection. We recommend backing up your data at least once a day.

Google's backup and disaster recovery solutions provide the following benefits for Microsoft SQL Server:

  * **Efficient incremental forever backup** with true point in-time recovery that helps in performing backup in less time than conventional backups, while reducing the impact on production servers. It also reduces both bandwidth and storage consumption for low Recovery Point Objective (RPO) and Total Cost of Ownership (TCO).
  * **Mount and migrate recoveries** (M&M) for backups stored in Cloud Storage for low RTO.
  * **Comprehensive integration with SQL Server capabilities** including support for SQL Server availability group clusters and multiple recovery options across scenarios.
  * **Central pane of management** including dedicated monitoring, alerting and reporting capabilities for all of your backups.



Learn more:

  * [Backup and DR Service Product Overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)
  * [Feature list for Backup and DR Service ](https://docs.cloud.google.com/backup-disaster-recovery#all-features)
  * [Protect and recover Microsoft SQL Server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sql-server-backup-recovery)
  * [Backup and DR Service Pricing](https://cloud.google.com/backup-disaster-recovery/pricing)
  * [Pricing Calculator](https://cloud.google.com/products/calculator-legacy)



## Monitor data

**Best practice:** Use Cloud Monitoring.

You can [install the Cloud Monitoring agent for Microsoft Windows](https://docs.cloud.google.com/monitoring/agent/install-agent#agent-install-windows) to send several monitoring data points into the Cloud Monitoring system.

By using [data collection capabilities](https://msdn.microsoft.com/en-us/library/bb677179.aspx), you can fine tune the information you want to monitor, and send it to [the built-in management data warehouse](https://msdn.microsoft.com/en-us/library/bb677306\(v=sql.130\).aspx). The management data warehouse can run on the same server you are monitoring, or the data can be streamed to another SQL Server instance running the warehouse.

## Bulk-load data

**Best practice:** Use a separate database to stage and transform bulk data before moving it to production servers.

It's likely that you will need to load large amounts of data into your system at least once, if not regularly. This is a resource-intensive operation, and you might reach the [persistent disk IOPS limit](https://docs.cloud.google.com/compute/docs/disks/performance#type_comparison) when you do bulk loads.

You can reduce the disk I/O and CPU consumption of bulk load operations, and also speed up the execution time of your batch jobs. To do this, create a completely separate database that uses the `Simple` recovery model, and then use that database for staging and transforming the bulk dataset before you insert it into your production database. You can also put this new database on a local SSD drive, if you have enough space. Using a local SSD for the recovery database reduces the resource consumption of your bulk operations and the time required to complete the jobs. The final benefit is that your backup job for the production data won't have to back up all those bulk operations in the transaction log, so it is a smaller job and runs faster.

**Note:** Bulk Logged is another recovery model that you might consider for your bulk loading operations. It uses more disk space, more disk I/O, and requires you to regularly run backup jobs on your transaction logs, but it is not as thorough as the Full recovery model.

## Validate your setup

**Best practice:** Test your configuration to validate that it performs as expected.

Whenever you set up a new system, you should plan on validating the configuration and running some performance tests. [This stored procedure](http://www.brentozar.com/blitz/) is a great resource for evaluating your SQL Server configuration. Take some time later to read about the configuration flags, and run the procedure.

## Optimize SQL Server Enterprise Edition

SQL Server Enterprise Edition has a long list of added capabilities over Standard Edition. If you are migrating an existing license to Google Cloud, there are some performance options that you might consider implementing.

### Use compressed tables

**Best practice:** Enable table and index compression.

It might seem counterintuitive that compressing tables could make your system perform faster, but, in most cases, that's what happens. The tradeoff is using a small amount of CPU cycles to compress the data and eliminate the extra disk I/O required to read and write the bigger blocks. Generally, the less disk I/O your system uses, the better its performance. Instructions for estimating and enabling table and index compression are [on the MSDN website](https://msdn.microsoft.com/en-us/library/hh710070\(v=sql.120\).aspx).

**Note:** The table and index compression options are also available for SQL Server Standard Edition 2016 SP1 and later.

### Enable the buffer pool extension

**Best practice:** Use the buffer pool extension to speed data access.

The buffer pool is where the system stores _clean pages_. In simple terms, it stores copies of your data, mirroring what it looks like on disk. When the data changes in memory, it's called a _dirty page_. Dirty pages must be flushed to disk to save the changes. When your database is larger than your available memory, that puts pressure on the buffer pool, and clean pages might be dropped. When the clean pages are dropped, the system must read from disk the next time it accesses the dropped data.

The [buffer pool extension feature](https://msdn.microsoft.com/en-us/library/dn133176.aspx) lets you push clean pages to a local SSD, instead of dropping them. This works along the same lines as virtual memory, which is to say, by _swapping_ , and gives you access to the clean pages on the local SSD, which is faster than going to the regular disk to fetch the data.

This technique is not nearly as fast as having enough memory, but it can give you a modest increase in throughput when your available memory is low. You can read more about buffer pool extensions and review some benchmarking results on [Brent Ozar's site](https://www.brentozar.com/archive/2014/04/sql-server-2014-buffer-pool-extensions/).

## Optimize SQL Server licensing costs

To reduce your licensing costs, reduce the number of vCPUs used by the instance. You can customize the number of visible cores or disable SMT for the instance.

### Disable simultaneous Multithreading (SMT)

**Best practice:** Set the number of threads per core to 1 for most SQL Server workloads

Simultaneous multithreading (SMT), commonly known as Hyper-Threading Technology (HTT) on Intel processors, is a feature that lets a single CPU core be logically shared as two threads. On Compute Engine, SMT is enabled on most compute instances by default, which means that each vCPU in the instance runs on a single thread and each physical CPU core is shared by two vCPUs.

On Compute Engine, you can configure the [number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core), which effectively turns SMT off. When the number of threads per core is set to 1, vCPUs don't share physical CPU cores. This configuration significantly impacts licensing costs for Windows Server and SQL Server. When the number of threads per core is set to 1, the number of vCPUs in a compute instance is halved, which also halves the number of Windows Server and SQL Server licenses required. This can significantly decrease the total workload cost.

However, configuring the number of threads per core also impacts workload performance. Applications that are written to be multi-threaded can take advantage of this feature by breaking up computing work into smaller parallelizable chunks that are scheduled across multiple logical cores. This parallelization of work often increases the overall system throughput by better utilizing the available core resources. For example, when one thread is stalled, the other thread can use the core.

The exact performance impact of SMT on SQL Server depends on workload characteristics and the hardware platform used because SMT implementation differs between hardware generations. Workloads with a high volume of small transactions, for example OLTP workloads, can often take advantage of SMT, and benefit from a larger performance increase. In contrast, workloads that are less parallelizable, for example OLAP workloads, benefit less from SMT. Although these patterns have been noticed generally, consider evaluating the performance impact of SMT on a per workload basis to determine the impact of setting the number of threads per core to 1.

The most cost effective configuration for the majority of SQL Server workloads involves setting the number of threads per core to 1. Any performance decline can be offset by utilizing a larger compute instance. In most cases, the 50% decrease in licensing cost is greater than the increased cost of the larger compute instance.

#### Example: Consider a SQL Server is deployed in the `n2-standard-16` configuration

By default, the number of cores visible in the operating system is 16, which means that 16 vCPUs of Windows Server and 16 vCPUs of SQL Server licenses are required to run the server.
    
    
    PS C:\> Get-WmiObject -Class Win32_processor | Select-Object NumberOfCores, @{Name="Thread(s) per core";Expression={$_.NumberOfLogicalProcessors/$_.NumberOfCores}}
    
    NumberOfCores Thread(s) per core
    ------------- ------------------
                8                  2
    

After following the [steps to disable SMT](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) on the SQL Server the new configuration is:
    
    
    PS C:\> Get-WmiObject -Class Win32_processor | Select-Object NumberOfCores, @{Name="Thread(s) per core";Expression={$_.NumberOfLogicalProcessors/$_.NumberOfCores}}
    
    NumberOfCores Thread(s) per core
    ------------- ------------------
                8                  1
    

Now that only 8 cores are visible in the operating system, the server only requires 8 vCPUs for Windows Server and SQL Server to run.

### Reduce the number of visible cores

**Best practice:** Customize the number of visible cores to manage SQL Server licensing costs.

In addition to disabling SMT, you can customize the number of visible CPU cores on your compute instance. By default, compute instances show all available vCPUs to the operating system. If you specify a custom number of visible cores, then the operating system sees only the cores that you specify. This configuration reduces the number of required SQL Server licenses because you need licenses only for the visible cores.

If you customize the visible cores, then you can optimize your licensing costs without changing the machine type. This feature is useful if your workload requires a specific amount of memory but doesn't need all the vCPUs that are included in the machine type.

For more information, see [Customize visible cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores).

## What's next

  * [Creating a high-performance SQL Server instance](https://docs.cloud.google.com/compute/docs/tutorials/creating-high-performance-sql-server-instance)
  * [Creating SQL Server instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)
  * [Creating Windows instances](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
