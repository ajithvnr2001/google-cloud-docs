---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication/
title: Data replication to another backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:59.806378+00:00
---

# Data replication to another backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Data replication to another backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Replication of copy data to remote storage protects the data in the event of disaster at the primary site and reduces the amount of storage required at the primary site. The goal of replication is to get your data back in situations of data loss and impact to your production systems due to issues such as a hardware failure, software issues, or a site event. Data replication also supports the creation of remote copies of Test/Dev, QA, and analytics data. Data can be replicated from one backup/recovery appliance to a second (remote) appliance or to the cloud for recovery, disaster recovery, or test and development purposes.

Your backup templates determine the method, schedule, and frequency of how data replication to a remote site is to be performed. The backup template defines how to move and store data efficiently to the remote backup/recovery appliance. Data replication is controlled by the individual template policies:

  * Production to Mirror policies protect your application or VM data against a site failure by having a full copy of that data mirrored to a remote production site. Applications are kept up-to-date and can be re-started at a moment's notice at the remote site by accessing data from the remote DR copy. Data mirroring can be considered as access optimized replication to a remote site. For details see Production to Mirror Policy Replication.

  * Snapshot to OnVault policies use an HTTPS connection to send data to storage defined by an OnVault Pool. The compress option is on by default in OnVault Pools. For details see the Send snapshots to one or more OnVault pools section.




## Send snapshots to one or more OnVault pools

The snapshot to OnVault policy lets you send snapshot data to a location defined by an OnVault pool. A schedule within the policy is used to send the most recent snapshot taken by the policy template's production to snapshot policy to the location defined by the OnVault pool. OnVault pool storage is typically used for long-term retention. For details on the OnVault pool, see [Send snapshots to one or more OnVault pools](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/storage-pools).

When sending data to a storage defined by an OnVault pool, an HTTPS connection is used to ensure data security over the network. The OnVault pool's compression option is on by default to minimize network traffic.

After the initial ingest of the full snapshot, only the changes to data are sent to the OnVault pool. This is the same incremental forever model used by other policies.

When accessing data in an OnVault pool's storage, consider the following:

  * Backup/recovery appliances can create clones.

  * LiveClones cannot be created.




### OnVault to multiple OnVault pools

Application data can be sent to multiple OnVault targets in the cloud. Each OnVault target is controlled by separate policies so frequency of update and retentions can be different (e.g., frequent local updates with short retention, together with less frequent updates to cloud with long-term retention).

Multi-target OnVault is supported with all application types, including Direct-to-OnVault with VMware VMs. In this case, the data is written directly to the first OnVault pool, bypassing the snapshot pool, and then read from the first OnVault pool and sent to the others.

## Production to mirror policy replication

Production to mirror policies provide a means to replicate a copy of the application or VM data to a target backup/recovery appliance and to have data access without a restore window, providing for very low RTO. As needed, you have the ability to perform a failback to the production site with an identical set of data that is mirrored between the local and remote backup/recovery appliances.

### StreamSnap

StreamSnap facilitates high-availability by allowing you to keep a remote copy of an application's storage and configuration up-to-date and ready for a failover scenario. When a StreamSnap-managed application fails, you mount a failover backup of the application from the remote site. When the problem has been resolved, then you can restore the syncback backup to the local site with the latest changes and then failback the application to the production site.

StreamSnap replicates data snapshots to a remote backup/recovery appliance over a high quality bandwidth IP network, which can provide RPOs as low as one hour.

  * For VMware VMs, snapshot replication is streamed to the second backup/recovery appliance in parallel. Streaming of a VMware VM is performed to avoid waiting until the local snapshot job completes before initiating replication.

  * For non-VMware VM applications, snapshot replication occurs after the local snapshot job is complete.


**Note:** StreamSnap replication and local snapshots are integrated to avoid the creation of double snapshots. The backup/recovery appliance lets you maintain multiple local snapshots and store local backups in an OnVault pool for long-term retention.

Production to mirror policies with StreamSnap replication are tied to a specific production to snapshot policy. They use the schedule and frequency settings of their associated production to snapshot policy.

You can retain backups from multiple available points in time at the remote site by applying retention in a StreamSnap policy. When retaining backups at the remote appliance, a new backup will be created at the remote appliance with an expiration date determined by the policy settings. Each remote backup supports all operations available with a local backup when accessed from the **App Manager**.

StreamSnap replication requires a reliable network connection to replicate data snapshots to the remote appliance. The bandwidth required on the network connection is directly related to the application size (initial copy) and amount of change (for incremental updates).

Backup and DR data replication technology:

  * Protects data in the event of potential loss or damage, across remote locations, data centers, and geographies. Should a disruption occur, data replication delivers rapid resumption of the access and use of that data.
  * Makes the most effective use of network bandwidth by leveraging compression technology.
  * Eliminates the need for a dedicated WAN accelerator/optimizer.
  * Preserves write-order, even across multiple LUNs in a consistency group.
  * Integrates with Backup and DR resiliency director.
  * Encrypts data using the AES-256 encryption standard. Authentication between appliances is performed using 2048-bit RSA certificates.



## Methods of replication

Your backup templates determine the method, schedule, and frequency of how data replication to a remote site is to be performed. The backup template defines how to move and store data efficiently to the remote backup/recovery appliance. Resource profiles define where to store data. Data can be stored locally or a remote backup/recovery appliance to which data will be replicated.

Data replication can be implemented through a variety of different methods:

  * **Data Mirroring** : Production to mirror policies protect your application or VM data against a site failure by having a full copy of that data mirrored to a remote production site. Applications are kept up-to-date and can be re-started at a moment's notice at the remote site by accessing data from the remote DR copy. Data mirroring can be considered as access-optimized replication to a remote site. Data mirroring between a production and mirrored site is available in the StreamSnap replication method. For more information, see the [Production to Mirror Replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prod-mirror) page.
  * **Snapshot to OnVault and direct to OnVault** : OnVault policies send data over the network to Cloud Storage. These policies allow you to send application and VM data to storage defined by a Backup and DR OnVault pool. For more information, see the [Replicate to object storage defined by a Backup and DR OnVault pool](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/data-replication) page.

**Note:** To perform copy data replication between a primary (local) backup/recovery appliance and a remote appliance for storage, make sure both appliances are configured and joined (exchange security certificates), operating in non-sharing mode. You join the primary and remote appliances as described in [Configure Joined Appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-control-panel#join).



These are the benefits of each method of replication.

Replication Method | Recommended Use | Advantages | Disadvantages  
---|---|---|---  
**Snapshot to OnVault or direct to OnVault** | Short, medium, and long-term retention. | Cost effective   
Compression reduces bandwidth consumption   
Data is encrypted in-flight and, optionally, at rest | Higher bandwidth usage.   
Applications cannot be run in storage defined by an OnVault pool.   
**Data Mirroring: StreamSnap** | Disaster recovery for applications that require a shorter RPO. | RPO as short as an hour with near -instant data access and failover   
Compressed and encrypted   
Replicates large amounts of data as well.   
Retains backups from multiple available points in time at the remote appliance   
StreamSnap technology can be used for log replication between local and remote appliances | Higher bandwidth consumption  
  
## Select a storage pool for replicated data

To select the destination storage pool that is to be used to store the incoming StreamSnap replication data:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance.
  3. Click **Configure Appliance** to open the **Appliance Configuration** page.
  4. Go to **System** , then **Configuration** , then **Appliance Settings**.
  5. Click the **Storage** tab. A drop-down menu appears where you can select the destination snapshot pool for replicated data that comes to this backup/recovery appliance.
  6. (Optional for VMware only) You can override this setting for VMware VMs if you want them to go to an ESX datastore instead. Check the **VM override** box and make the following selections:

     * Select a vCenter to manage the operation. This vCenter should ideally be at the DR site.
     * Select an ESXi host to host the VMware VMs. This ESXi host should also be at the DR site and must be powered on and available at all times. You can only select one ESXi host.
     * Select the datastores to hold the DR data. The datastores must have space to hold the replicated VMDKs (Virtual Disks). If you select multiple datastores, the backup/recovery appliance will use each one in turn.

The backup/recovery appliance will create new VMs at the DR site using the name `DR-<original VM name>`. For example, if the source VM is called **testvm** , then the DR copy will be called **DR-testvm**. If the VM already exists and is powered off, the backup/recovery appliance uses it as the target for the replicated VMs.

**Note:** When you configure VMware override, it affects the incoming StreamSnap replication to the backup/recovery appliance you are logged onto. If you require the DR appliance to create its DR copy in a VMware datastore rather than the DR appliance's Snapshot pool, be sure to set the VMware override at the DR appliance site.
  7. Click the gray **Save Settings** button.




## Configure StreamSnap replication

Based on your production to mirror requirements for replicating a copy of your data to a second backup/recovery appliance, you can execute the failover of a StreamSnap replication backup to a mirrored data production site at a second backup/recovery appliance. Subsequently, changes made at the DR site can be replicated back (failback) to your production environment at the local backup/recovery appliance.

  * Multiple syncback backups can be used to replicate cumulative changes made at the DR site back to production.
  * Syncback backups can be mounted, cloned, or restored at the production site to restore access.



To manage an application or VM using a StreamSnap replication policy, perform the following:

  1. Verify that both appliances are configured and joined (exchange security certificates), operating in **Sharing Mode**.
  2. In the **Backup Plans** , create a template that includes one of each of the following:

     * **Production to Snapshot policy**. Production to mirror policies that use the StreamSnap replication option are tied to a specific snapshot policy. The StreamSnap policy requires the schedule and frequency settings of the associated snapshot policy in the template. You will be prevented from saving the StreamSnap replication policy without an associated base snapshot policy in the template.
     * **Production to Mirror policy**. The production to mirror policy uses StreamSnap replication. Remote backups support all operations available with a local backup when accessed in the **App Manager**.
**Note:** If you enable the database log backup advanced settings as part of the snapshot policy associated with StreamSnap replication, and you enable the **Replicate Logs (Using StreamSnap Technology)** setting, database logs will be replicated to the remote appliance. If log replication does not occur until the database has been replicated to the remote appliance. At least one successful replication of the database must be completed first before a log will be visible on the remote appliance.
  3. In the **Backup Plans** , create a resource profile that specifies where to store data locally as well as where to replicate data. See the [Create a resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile) page.

  4. In the **App Manager** , select the application data that you want to manage, then apply the policy template to manage applications or VMs.

Snapshots are taken locally and replicated to a remote appliance. The data is then available on the remote appliance to provide the flexibility of instant access. Backups appear on the remote system when you click the **Remote Snap** button in the **Restore** window in **App Manager**.

  5. Test failover to the remote appliance as described in [Test failover](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/failover-and-failback#test-fail)

  6. Based on your production to mirror requirements for replicating a copy of your data to a second appliance, you can execute the failover of a StreamSnap replication backup to a production site at a second appliance. Subsequently, changes made at the DR site can be replicated back (failback) to your production environment at the local appliance. For details, see the [Failover and failback](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/failover-and-failback) page.




## StreamSnap job error handling

When a backup template includes a StreamSnap replication policy and a snapshot policy, and you apply that backup template to an application or VM, the **Monitor** records the results of the StreamSnap job. While it is running, the StreamSnap job appears as a single job in **Monitor**. Once replication is complete, two jobs appear in **Monitor** ; one for the snapshot job and a second for the StreamSnap job.

Note the following ways a backup/recovery appliance tracks those jobs:

  * If replication succeeds, two separate job entries appear in the list of jobs in the **Jobs** page with a **Succeeded** status. Both job entries have the same **Job Name** , except that the StreamSnap job also includes an S suffix in its **Job Name**.
  * If there is a job failure, for either the StreamSnap job or the snapshot job, two job entries appear in the list of jobs in the **Jobs** page to identify which job was successful and which job failed.

**Note:** Failover, test failover, and syncback jobs that have been triggered for a StreamSnap backup appear in the list of **Jobs** when you filter the StreamSnap job type. The appliance Monitor service does not distinguish between the two backups as they relate to failover, test failover, and syncback job types.

The start and end times of the StreamSnap job entry and the snapshot job entry will be identical in **Monitor**. The actual amount of time taken for the snapshot phase is listed in the **Statistics** page for the StreamSnap job.

The following table outlines the job history and error handling behavior based on the success or failure of the snapshot policy and the StreamSnap replication policy when used to protect an application.

Protection Scenario | Job History Behavior  
---|---  
Both the snapshot and StreamSnap jobs succeed | Two separate job entries appear in the list of jobs with **Succeeded** status when the job completes. Both job entries have the same **Job Name** , except that the StreamSnap job also includes an S suffix in its **Job Name**.   
Snapshot job succeeds, StreamSnap job fails | For the snapshot job, one job entry appears in the list of jobs with **Succeeded** status.   
The StreamSnap job is retried up to three times.  
Both the snapshot and StreamSnap jobs fail but then the appliance attempts a retry | One StreamSnap job entry appears in the list of jobs with **Retried** status.   
If the snapshot job succeeds but the StreamSnap job still fails, this results in two job entries and there will be no further retries for StreamSnap.  
Both the individual snapshot and StreamSnap jobs fail after maximum number of retries | One StreamSnap job entry appears in the list of jobs with **Failed** status.   
  
## StreamSnap replication retries

StreamSnap replication (SnapReplicate) replicates a point-in-time snapshot of the original application. See the [Create a StreamSnap replication production to mirror policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prod-mirror) page for more information.

### Benefits

  * StreamSnap replication to different hosts can run concurrently, as a result the replication to multiple hosts can be completed much faster.

  * In case the snapshot phase of a StreamSnap job succeeds but the StreamSnap phase fails, the StreamSnap phase is retried up to three additional times before the StreamSnap job fails. The StreamSnap job has a suffix of S followed by the alphabet a, b, or c, signifying the number of retries.

  * If the snapshot job fails, it is retried. If a retry succeeds, then the replicate job can proceed. If the snapshot job fails even after retries, only then is the StreamSnap job fails.

  * When you run a new StreamSnap job while an existing StreamSnap job is already running, the new StreamSnap job is automatically split into two jobs (snap+replicate) before it is queued. In this scenario, the snap portion of the second job can run in parallel with the replicate portion of the second job. The replicate portion of the second job waits for the snapshot job to complete before it activates.




## On-demand snapshot replication

The appliance management console lets you replicate the local snapshot or a StreamSnap from any paired appliance to any paired appliance using the **Replicate** option from the image details section drop-down. The replication will always be the changes from the selected backup to the most recent one at the remote site. Because of this, it is ideal to replicate backups from oldest to newest if there are several backups to be replicated. You can provide your own retention period while replicating the backup. See the Replicate a backup section.

### Replicate a backup

Use these instructions to replicate a backup:

  1. Click the **App Manager** tab and select the **Applications** option from the drop-down list.

The **Applications** page opens.

  2. Select the application with the backup that you want to replicate, then choose **Access** from the drop-down list at the bottom right corner of the **Applications** page. The **Access** page opens listing captured backups in the timeline ramp view. Both snapshot and remote backup types, including StreamSnap backups can be selected and replicated.

  3. Select a backup and then select **Replicate** from the list of access operations.

The **Replicate** page opens.

  4. From the **Destination** drop-down, select the destination appliance for replication.

  5. From the **Expiration** section, select one of the following options for the newly replicated backup:

     * **Same as source** : Select **Same as Source** if you want to set the same expiration date as the source backup.
     * **Retain** : Select **Retain** if you want to set the expiration duration for the replicated backup in hours, days, weeks, months, or years.
     * **Expire on** : Select **Expire on** if you want to expire for a specify the and specify the expiration date for the replicate.
     * **Expire on** : Select **Expire on** and specify the expiration date for the replicated backup.
     * **Never Expire** : Select **Never** expire if you do not want to expire the replicate backup anytime.
  6. Click **Submit**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
