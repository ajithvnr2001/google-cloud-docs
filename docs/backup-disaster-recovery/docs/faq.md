---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/faq/
title: Frequently Asked Questions about appliance-managed backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:35:27.172652+00:00
---

# Frequently Asked Questions about appliance-managed backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Frequently Asked Questions about appliance-managed backups Stay organized with collections  Save and categorize content based on your preferences. 

Where can I find information about Backup and DR pricing?
    Backup and DR pricing information is detailed on the [Backup and DR pricing page](https://cloud.google.com/backup-disaster-recovery/pricing).
When is a workload considered to be under management by Backup and DR?
    Backup and DR billing (also called SKU usage) considers any workload with at least one un-expired backup using the service. Backup images can be retained in a snapshot or OnVault pool for extended periods of time (years) for compliance purposes when the source workload is no longer actively being protected.
Does backup compression impact usage?
    The compression achieved by the system in snapshot and OnVault pools doesn't affect the usage measurement, as the usage count is based on the frontend workload size and not the backend storage consumption.
How does replication between backup/recovery appliances affect usage?
    Backup and DR measures usage based on frontend workload size. It does not take into account how many copies are retained or where they are retained. Adding an appliance for DR purposes won't affect Backup and DR SKU usage.
How do prune paths and exclude lists affect Backup and DR billing?
    

If your file system workload has 3 TiB of data, and you use prune paths and exclude lists to eliminate 1 TiB of files from management, and you use Backup and DR agent to back up the file system, then the usage is measured based on the actual amount of data managed, which in this example is 2 TiB.

If you back up the file system without the Backup and DR agent (such as with agentless whole VMware/Compute Engine VM backup), then the usage is measured based on the size of the volume(s), which is 3 TiB.

Usage count for my workload seems to be lower than what it reported yesterday, why is that?
    

Backup and DR usage is based on the most recent successful copy, not the largest recoverable copy. Workloads shrink or expand over a time (irrespective of the change rates involved). When the workload size shrinks, it reflects on the usage reading from the most recent backup.

How does the database change rate affect usage?
    

Backup and DR measures usage based on the size of the last successful copy. So for a 4 TiB Oracle database with a 10% daily change rate, but the size of the database is always 4 TiB, the usage calculation will be 4 TiB. Unless the size of the workload changes, the change rate does not directly impact the usage calculation.

How do I avoid paying for double-protection if I protect a workload and its VM?
    

Backup and DR counts usage for a VMware VM and its workloads separately, which can lead to double counting. If you manage a SQL Server workload running on a VMware VM using the Backup and DR agent and if you also manage the entire VMware VM, then the SQL database is counted separately from and in addition to the VM. The best practice in such scenarios is to manage the OS volume of the VM and the workloads residing on the VMs separately. This effectively eliminates double protection and thus double counting.

Do you count only the database size or do you include the log files in usage measurement?
    

Backup and DR measures only the managed database files that are needed for a consistent database backup. It does not count log files towards usage measurement.

How do I verify my usage for VMware VMs?
    

Backup and DR usage measurements for VMware VMs are consistent with the vCenter reported size for that VM.

`du -h *.vmdk` output from the appropriate VM folder on the server matches the usage count.

How do I verify my usage for Oracle database?
    Backup and DR usage measurements for Oracle are based on the allocated size for the database. Here is a sample query to verify the Oracle database size.

`select (d.total + c.total) total from (select sum(bytes) total from v$datafile) d, (select sum(block_size*file_size_blks) total from v$controlfile) c;`

Then subtract the following: `select sum(bytes) free from dba_free_space;`

How do I verify my usage for file systems?
    Backup and DR usage measurements for file system based on workloads: 

  * Windows - used file system size reported by DiskManager
  * Linux - used file system size reported by `df - k`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
