---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices/
title: Best practices for backup policy templates in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:56.305147+00:00
---

# Best practices for backup policy templates in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Best practices for backup policy templates in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page provides best practices for creating and managing Backup and DR backup policies using the appliance management console, including the following policy types:

  * **Production to Snapshot policies** : capture frequent snapshots of production data, with options for windowed or continuous schedules and different frequencies. You can also learn how to handle database log backups.

  * **OnVault policies** : send data to object storage, like Cloud Storage, for longer-term retention. This page also describes different types of OnVault policies such as _Snapshot to OnVault_ , _Direct to OnVault_ , and _OnVault to OnVault_.

  * **Production to Mirror policies** : use StreamSnap replication to replicate data to a remote appliance, enabling low recovery point objectives (RPOs). You can also learn more about how StreamSnap works and its benefits.




## Define a data capture window in the Backup and DR policy template

Define policy template schedules to meet the following requirements:

  * Data capture window requirements

  * RPOs

  * Recovery time objectives (RTOs)




For example, if a daily capture must be performed some time between 7:00 pm and 7:00 am, give the policy a capture window of 19:00 to 7:00. Giving the policy the widest window possible gives the maximum flexibility for the scheduler to schedule all needed jobs. The time window you specify defines the allowed start time for the data capture job. Jobs started at the end of the window are allowed to run through completion.

**Note:** In the appliance management console, the **Control Panel** tab in the **Appliance Settings** section lets you enable and disable all schedules. Disabling all schedules may result in numerous backup plan violations.**Note:** The time window used by all policies is in the UTC time zone format. For example, if you need the start time for a policy window as 15:00, in a time zone that is UTC+1, then set the policy start time to 14:00.

## Configure production to snapshot policy schedules

Backup and DR accesses recent data the most frequently. Because of this, you only need to retain several days of snapshots data if you also Configure OnVault policies with longer retention. This reduces storage requirements on the backup/recovery appliance so you can back up more data.

If you back up a workload to a backup/recovery appliance that would exceed its recommended storage capacity or snapshot limit, you will see a notification with a recommendation to back up the data to a different backup/recovery appliance.

**Caution:** Exceeding the capacity of a backup/recovery appliance can lead to failed jobs and unprotected data and failed restore operations.

You can schedule a backup snapshot that occurs during a specific frequency and time window or on a continuous basis. The minimum recommended frequency for a snapshot policy is one hour (local RPO) although database log backup scheduling can be run as often as every 15 minutes. You can also configure the snapshot frequency to meet your specific needs.

**Note:** When creating a snapshot policy for a database you have the option of also capturing its log files at a specified frequency. For more information, see [Database log protection in a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan-policy-best-practices#Log-protection).

### Configure a windowed schedule of one snapshot per window

Most Backup and DR _production to snapshot_ policies are designed to take a single snapshot of data in a 24-hour window. Windowed snapshot backups can be scheduled to take place within a window that might respect day boundaries, for example, 7:00 pm to 7:00 am.

You can create a snapshot policy schedule that crosses a day boundary and takes a single snapshot during a specific time window by configuring the following settings in the appliance management console:

  * Schedule type of **Windowed** (default)
  * Snap on these days: **Everyday except Never**
  * The window to open and close as needed, typically set from 19:00 to 07:00
  * The frequency to **Once Per Window**
  * The retention time (for example, retain for **2 days**)



With this windowed schedule, the day boundary (midnight) is ignored.

### Configure a windowed schedule of multiple snapshots in a window

In some cases you may want to capture multiple snapshots within a time window. This approach requires careful planning since it may result in the consumption of system resources and could lead to a situation where snapshots are constantly being taken.

You can create a snapshot policy schedule that takes multiple snapshots during a specific time window by configuring the following settings in the appliance management console:

  * Schedule type of **Windowed**(default)
  * Snap on these days: **Everyday except Never**
  * The window to open as needed, and may or may not span the day boundary.
  * A frequency that does not overlap the time required to take a snapshot. The default is every eight hours. The minimum recommended frequency for a snapshot policy is to run every **1 hour (local RPO)**.
  * The retention time (for example, retain for **2 days**)



With this approach, the job runs according to its frequency within the specified window. Any job already running at the close of the window continues to run until it completes.

### Configure a continuous schedule run daily at regular intervals

You can configure a snapshot policy schedule that continuously runs on a daily basis, 24 hours a day, 7 days a week, at a time interval of every _x_ minutes or hours. For example, you can create a continuous snapshot backups policy where jobs run daily every four hours, with the first job starting at 1:00 am.

You can create a snapshot policy that is scheduled to run continuously at a regularly set interval by configuring the following settings in the appliance management console:

  * Schedule type of **Continuous**
  * A frequency that does not overlap the time required to take a snapshot. The default is every eight hours. The minimum recommended frequency for a snapshot policy is to run every **1 hour (local RPO)**.
  * Time to initiate the first snapshot job.
  * The retention time (for example, retain for **2 days**)



You also have the option of scheduling a continuous job to run once per day (the longest continuous policy schedule period without defining a windowed policy schedule). In this case you would specify to **Run Every 24 hours** , which equals a continuous daily schedule.

## Configure OnVault policies

Backup and DR OnVault policies allow you to send data to an _Onvault pool_ in Cloud Storage, also known as an OnVault pool configuration. A schedule within the policy is used to send the most recent data to object storage backup. After the initial ingest of data, an OnVault capture operation follows the incremental forever data capture process.

When sending data to storage defined by the OnVault pool, an HTTPS connection is used to ensure data security over the network. The OnVault pool's compression option is on by default to minimize network traffic.

When accessing data in an OnVault pool's defined storage location, note the following considerations:

  * Appliances can create clones.
  * Appliances can mount data, but because data is first copied to the snapshot pool then mounted, it is not recommended.
  * LiveClones cannot be created.

**Note:** For best storage retention resiliency, use OnVault pools with multi-region storage.



You can create three types of Backup and DR OnVault policies:

  * _Snapshot to OnVault policies_ : capture data in a snapshot pool and then copy the data in the snapshot pool to a Cloud Storage bucket defined by an OnVault pool.

  * _Direct to OnVault policies_ : allow VMware VM backups to be sent directly to a Cloud Storage bucket defined by an OnVault pool.

  * _OnVault to OnVault policies_ : replicate data from one OnVault pool to another another OnVault pool.




### Create a Snapshot to OnVault policy

To create a _Snapshot to OnVault_ schedule that sends the most recent snapshot data to object storage defined by an OnVault pool within a defined window once a day, configure the following settings in the appliance management console:

  * Vault on these days: **Everyday**
  * The window to open and close as needed. Typically set to **19:00 to 18:50**
  * The retention time (for example, retain for **3 years**)

**Note:** Select the target OnVault pool in case your appliance was configured to use multiple OnVault pools.



### Create a Direct to OnVault policy

To create a _Direct to OnVault_ schedule that sends the most recent incremental updates directly to storage defined by an Onvault pool within a defined window once a day, configure the following settings in the appliance management console:

  * On these days: **Everyday**
  * The window to open and close as needed. Typically set to **19:00 to 18:50**
  * The retention time (for example, retain for **3 years**)

**Note:** When backing up VMware Engine VMs, it's a good idea to use multi-region storage buckets for OnVault to ensure backups are resilient across regions.



### OnVault to OnVault policy

To create an _OnVault to OnVault_ schedule that sends the most recent incremental updates directly to storage defined by an OnVault pool within a defined window once a day, configure the following settings in the appliance management console:

  * On these days: **Everyday**
  * The window to open and close as needed. Typically set to **19:00 to 18:50**
  * The retention time (for example, retain for **3 years**)
  * Verify the source OnVault pool is set correctly
  * Select the target OnVault pool. This is the second OnVault pool to which data will be replicated to from the source OnVault pool.



## Production to Mirror backup policies

Best practices for _Production to Mirror_ backup policies depend on which replication option you plan to use. This section outlines the policy best practices for the StreamSnap replication method offered by the appliance.

### Production to Mirror policies using StreamSnap replication

Production to Mirror backup policies that use StreamSnap replication configuration are tied to a specific snapshot policy. They use the schedule and frequency settings of the associated snapshot policy in the template.

**Note:** Before creating a StreamSnap replication policy, you must first create a snapshot policy.

StreamSnap replicates data snapshots to a remote backup/recovery appliance over a high quality network, which can provide RPOs as low as one hour. For VMware VMs, snapshot replication is streamed to the second backup/recovery appliance in parallel to the snapshot being copied. Streaming of a VMware VM is performed to avoid waiting until the local snapshot job completes before initiating replication.

**Note:** StreamSnap replication and local snapshots are integrated to avoid the creation of double snapshots. Each backup/recovery appliance lets you maintain multiple local snapshots and store local backups in the OnVault pool for long-term retention.

StreamSnap replication does the following:

  * Achieves **Recovery Point Objectives** as short as one hour. The StreamSnap replication policy relies on the associated production to snapshot policy for recovery point objectives and the other advanced snapshot settings. A StreamSnap policy can point to any snapshot policy with frequency of one hour or longer (remote recovery point objectives).
  * Uses an existing IP network to replicate data.
  * Replicates large amounts of data to remote users (for example, test and development environments).
  * Retains multiple point-in-time snapshot backups at the remote site, with retention behavior being driven by the settings in the StreamSnap policy.
  * Simplifies fail-over to a host on the remote site.
  * Enables incremental reverse replication (syncback) to the local backup/recovery appliance.
  * Compresses and encrypts replicated data to the second backup/recovery appliance. You can disable compression if the data is already compressed (for example, for images and videos).

**Note:** StreamSnap jobs run for non-DB, DB, and DB+Log types. To perform on-demand log replication of the database logs to a remote backup/recovery appliance, select the database in **App Manager** , then select **Replicate Logs**. For more information, see [Run on-demand database log replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

When you apply the backup template to an application or VM in the **App Manager** , the **Monitor** records the results of the StreamSnap job and it appears as a single job. Once replication is complete, two jobs appear in **Monitor** with a span **Succeeded** status; one for the snapshot job and one for the StreamSnap job (see [StreamSnap job error handling](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication#streamsnap-errors)). If there is a job failure, either for the StreamSnap job or the snapshot job, two job entries appear to identify which job was successful.

## BitLocker recovery considerations for Windows VMs

For Shielded VM boot disks, Google Cloud seals the BitLocker keys to the vTPM of the original instance. This means that if you restore the boot disk to a different instance, then the restoration might succeed but you won't be able to boot the VM until you supply the BitLocker recovery key.

Google doesn't have access to the BitLocker recovery keys. Therefore, when you protect Windows VMs with BitLocker, your backup strategy should include a plan to maintain access to the BitLocker recovery keys. Your DR testing should also include recovering the BitLocker recovery keys.

For more information, see [Best practices for securing Windows VMs with BitLocker](https://docs.cloud.google.com/compute/docs/instances/windows/windows-best-practices#best-practices-bitlocker).

## What's next

  * Get an overview of [backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [backup policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) of an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
