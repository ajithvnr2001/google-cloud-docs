---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview/
title: Manage backup policies in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:24.671855+00:00
---

# Manage backup policies in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage backup policies in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup policies define schedules for jobs, when and how often to run a job, and how long to retain the data. A backup policy also lets you define whether its schedule runs within a window or continuously. Where applicable, backup policies let you define rules to determine if data protected by a policy meets your requirements. If data is protected according to your needs, it is considered compliant.

A backup template includes one or more of the following types of policies:

  * **Production to snapshot** : This policy defines when and how often production data is captured and how many snapshots are retained. Snapshots are intended for short-term retention. For more information, see Production to snapshot policies.
  * **OnVault** : These policies let you send captured backups to object storage. For an overview of OnVault policies, see [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault). Backup and DR provides two types of OnVault policies:

    * **Snapshot to OnVault** : This policy lets you replicate data captured in a snapshot pool to object storage defined by a Backup and DR OnVault storage pool. See [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#snap-vault). VMware VMs directly to object storage defined by an OnVault Storage Pool. See [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault) for details.
    * **OnVault to OnVault** : This policy enables data replication from the Direct to OnVault storage object to another OnVault destination. For more information, see [OnVault to OnVault policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault-onvault).
  * **Production to mirror** : This policy defines how data is replicated to a Mirror Pool (a snapshot pool on a remote backup/recovery appliance). Data in the Mirror Pool is intended for instant recovery in a disaster recovery scenario.




The backup plan enforces a specific policy development sequence when you define policies for a policy template. Some policies are unavailable depending on the type of policy template you develop. In addition, the types of policy templates and the minimum and maximum policy settings are specific to the backup/recovery appliance where they reside. Policy templates are applied to applications in the **App Manager**.

## Advanced Policy Settings

Policies include advanced settings for all applications supported by a backup/recovery appliance that use this policy. When you create a policy, you can define the advanced settings that are most appropriate for all applications to which the policy's template applies. Advanced settings for policies are detailed in [Configure advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).

You can override advanced settings defined in a policy for specific applications if the policy template **Allow Overrides on Policy Settings** parameter is set to **Yes**.

**Note:** The time window used by all policies is in UTC. For example, to set the start time for a policy window as 15:00, in a UTC+1 timezone, then set the policy start time to 14:00.

## Create a production to snapshot policy

Production to snapshot policies define how to capture application production data as snapshots. Snapshots are a fast virtualization step that help protect your data at a specific moment. For a set of best practices when developing a snapshot policy, see [Production to snapshot policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#prod-snap).

**Note:** Templates that are used to back up Compute Engine instances only contain production to snapshot policies. You cannot use a template that has OnVault or StreamSnap policies with a Compute Engine instance.

Use these instructions to create a policy to capture backups:

  1. In the appliance management console, click the **Backup Plans** tab, and then select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Click **Create Templates**.

The **Create Template** page opens with a new, empty backup template. See [Create a new template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template#create-temp) for details on creating a backup template.

  3. To create a production to snapshot policy, do one of the following actions:

     * Click **+** in the arrow between **Production** and **Snapshot** in the backup plan policy map.
     * Click **+Add** to the right of **snapshot** in the **Policies** area.

The production to snapshot policy configuration panel opens.

  4. In the **Policy Name** field, enter an alphanumeric text string. You can use spaces, underscores (_), and dashes (-), but don't include special characters.

  5. Specify the schedule type for the production to snapshot policy: **Windowed** or **Continuous**. The default is **Windowed**.

     * **Windowed**. This defines a discrete snapshot backup schedule that adheres to a specific frequency and time window. For example, you can perform a backup every 30 minutes, daily from 09:00 to 17:00 UTC. You can instruct the backup/recovery appliance to run multiple backup jobs at a specified frequency interval or once during a specified time window.
     * **Continuous**. Defines a continuous snapshot backup schedule. For example, you can perform a backup job every eight hours, starting the first job at 01:00 UTC. In this policy schedule, jobs run continuously (24/7) at the specified time interval.
  6. Configure the policy frequency settings based on the selected schedule type as shown in the following table.

Policy setting | Description  
---|---  
**Windowed** |   
On These Days | Configures the policy's frequency by defining an interval at which backups are captured. Based on this interval, the snapshot job runs once every specified number of days, weeks, months, or years. Click the link for this parameter to modify the run interval. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Except | Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily snapshot schedule every Friday, select **Weekly** and then select **Friday**. Click the link to the right of this parameter to modify the exception. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Within This Window | Defines a start and end time window for capturing backups.  
Run Once Per Window | Specifies that backups are captured once during the specified **Run Between** time window.  
Every | Specifies a repeat frequency duration (minutes or hours) for capturing backups during the specified **Run Between** time window. For example, every two hours.  
**Continuous** |   
Run Every | Specifies the time period to repeat backup capture.  
Start First Job At | Specifies the time of day at which to run the first job in the continuous cycle of backup captures.  
**Both Windowed and Continuous** |   
Retain For | Specifies how long to retain the backup. For example, retain the backup for two days.  
  7. Optionally, change the application priority from the **Priority** drop-down list. The default job priority is **Medium** , but you can change the priority to **High** or **Low**.

The backup plan scheduler identifies when one or more policies applied to applications are to run. It then initiates a job that places the policy into a queue when the scheduled start time occurs. Each policy type has a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state. This means that even if a job is supposed to start at a particular time, it executes only when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the system randomizes the selection of the application to run to ensure fairness across all applications of the same priority.

  8. Click **Advanced Policy Settings**.

The **Policy Settings** dialog opens.

The backup plan supports **Advanced Settings** for a snapshot policy. Advanced settings might be useful or required in some circumstances. For details, see [Configure advanced policy settings for a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings).

After you configure your advanced policy settings, click **Save Changes**.

  9. Click **Add Policy**. The **Templates** page opens.

  10. Click **Save Template**.




### Configure Full + Incremental backup schedules for databases

To set a schedule for data dumps:

  1. In the appliance management console, click the **App Manager** tab, and then select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the database instance that you want to schedule backups for. The filters can make it easier to find your database if you have many.

  3. Right-click the database instance and select **Manage backup configuration**.

  4. At the top of the Manage backup configuration page, click **Details & Settings**.

  5. In the **Application Details & Settings** page, under **Settings** , select **Use full+incremental backup**.

  6. For each day of the week, select whether you want a full or an incremental backup.

  7. Review the rest of the settings and then click **Save changes** and then **Okay** in the confirmation window.




## Create a snapshot to OnVault policy

The snapshot to OnVault policy lets you send snapshot data to one or more OnVault pools. A schedule within the policy sends the most recent snapshot taken by the policy template's snapshot policy to the OnVault pool. After the initial full backup, Snapshot to OnVault policies follow an incremental-forever model where only data changes are captured and sent to the OnVault pool. For a set of best practices when developing a OnVault policy, see [OnVault policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#onvault).

**Note:** Templates that are used to back up Compute Engine instances should only contain production to snapshot policies. You cannot use a template that has OnVault or StreamSnap policies with a Compute Engine instance.

### Send data to multiple OnVault pools

You can send snapshot data to multiple OnVault pools for these reasons:

  * Use local object storage for short or medium-term data retention, and then send the data to Cloud Storage for long-term data retention.
  * Use multiple on-premises and Cloud Storage targets for resilience.



When you define two or more snapshot to OnVault policies with different target pools are defined for a template, the OnVault icon shows a shadow to indicate that multiple target pools exist for this template. It also shows a number that corresponds to the number of different target pools to which data is sent.

**Note:** Before you create a snapshot to OnVault policy, you must first create a snapshot policy as described in the [Create production to snapshot policy][8] section. You cannot save the snapshot to OnVault template without a snapshot policy in the template.

Use these instructions to create a snapshot to OnVault policy:

  1. Click the **Backup Plans** tab, and then select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select a template that includes a snapshot policy.

The **Templates** page opens with the selected backup template.

  3. To create a snapshot to OnVault policy, do one of the following actions:

     * Click **+** in the arrow between **Snapshot** and **OnVault** in the backup plan policy map.
     * Click **+Add** to the right of **OnVault** in the **Policies** area of the **Templates** window.

The snapshot to OnVault policy configuration panel opens.

  4. In the **Policy Name** field, enter a descriptive alphanumeric text string. You can use spaces, underscores (_), and dashes (-), but you cannot include special characters.

  5. For scheduling, configure the policy frequency and schedule as shown in the following table.


Policy Setting | Description  
---|---  
**Windowed** |   
On These Days | Configures the policy's frequency by defining an interval at which backups are captured. Based on this interval, the job runs once every specified number of days, weeks, months, or years. Click the link to the right of this parameter to modify the **Run** interval. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Except | Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily schedule every Friday, select **Weekly** and then select **Friday**. Click the link to the right of this parameter to modify the exception. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Within this window | Defines a start and end time window for capturing backups.  
Run once per window | Specifies that backups are captured once during the specified **Run Between** time window.  
Every | Specifies a repeat frequency duration (minutes or hours) for capturing backups during the specified **Run Between** time window. For example, every two hours.  
**Continuous** |   
Run Every | Specifies the time period to repeat backup capture.  
Start First Job At | Specifies the time of day at which to run the first job in the continuous cycle of backup captures.  
**Both Windowed and Continuous** |   
Retain For | Specifies how long to retain the backup. For example, retain the backup for two days.  
  
  1. Optionally, change the application priority from the **Priority** drop-down list. The default job priority is **Medium** , but you can change the priority to **High** or **Low**.

The backup plan scheduler identifies when one or more policies applied to applications are to run. It then initiates a job that places the policy into a queue when the scheduled start time occurs. Each policy type has a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state. This means that even if a job is supposed to start at a particular time, it executes only when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the system randomizes the selection of the application to run to ensure fairness across all applications of the same priority.

  2. From the **Target Pool** drop-down list, select the OnVault pool where the snapshot data should be sent.

  3. Click **Add Policy**. The **Templates** window opens. Repeat the process to create another snapshot to OnVault policy with a different **Target Pool**.

  4. Click **Save Template**.




## Create a direct to OnVault policy

The Direct to OnVault policy lets you send VMs in your production environment to storage defined by the OnVault pool. A schedule within the policy sends the most recent production data to an object store. After the initial full backup, Direct to OnVault policies follow Backup and DR's incremental-forever model where only data changes are captured and sent to the object store.

**Note:** The Direct to OnVault policy type can only be used to back up VMware VMs. It cannot be used with other application types.

Use these instructions to create a direct to OnVault policy:

  1. Click the **Backup Plans** tab, and then select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select a template that includes an OnVault policy.

The **Templates** page opens with the selected backup template.

  3. Click **+Add** next to **Direct to OnVault** in the **Policies** area of the **Templates** page.

  4. In the **Policy Name** field, enter an alphanumeric text string. You can use spaces, underscores (_), and dashes (-), but don't include special characters.

  5. Configure the policy frequency schedule as shown in the following table.


Policy Setting | Description  
---|---  
**Windowed** |   
On These Days | Configures the policy's frequency by defining an interval at which backups are captured. Based on this interval, the job runs once every specified number of days, weeks, months, or years.  
| Click the link for this parameter to modify the **Run** interval. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Except | Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily schedule every Friday, select **Weekly** and then select **Friday**. Click the link to the right of this parameter to modify the exception. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Within This Window | Defines a start and end time window for capturing backups.  
Run Once Per Window | Specifies that backups are captured once during the specified **Run Between** time window.  
Every | Specifies a repeat frequency duration (minutes or hours) for capturing backups during the specified **Run Between** time window, for example, every two hours.  
**Continuous** |   
Run Every | Specifies the time period to repeat backup capture.  
Start First Job At | Specifies the time of day at which to run the first job in the continuous cycle of backup captures.  
**Both Windowed and Continuous** |   
Retain For | Specifies how long to retain the backup. For example, retain the backup for two days.  
  
  1. Optionally, change the application priority from the **Priority** drop-down list. The default job priority is **Medium** , but you can change the priority to **High** or **Low**.

The backup plan scheduler identifies when one or more policies applied to applications are to run. It then initiates a job that places the policy into a queue when the scheduled start time occurs. Each policy type has a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state. This means that even if a job is supposed to start at a particular time, it executes only when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the system randomizes the selection of the application to run to ensure fairness across all applications of the same priority.

  2. Click **Advanced Policy Settings** to configure advanced settings for the applications captured by this policy. See [Configure advanced policy settings for a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.

  3. Click **Update Policy**. The **Templates** page opens.

  4. Click **Save Template**.




## Create an OnVault replication policy

The OnVault replication policy lets you replicate data from the Direct to OnVault pool to a second OnVault destination. A schedule within the policy sends incremental changes from one OnVault pool to another. It makes the data available across multiple geographical locations for resiliency hosted by various vendors and clouds. Data replication from one OnVault pool to another is supported only when the data was first captured using Direct to OnVault.

Use these instructions to create an OnVault replication policy:

  1. Click the **Backup Plans** tab, and then select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Click **Edit** from the drop-down menu.

  3. Click **+** between **Production** and **OnVault** , and then configure a **Direct to OnVault** policy using instructions in Create a direct to OnVault policy.

  4. Next, click **+** next to **OnVault**.

The OnVault replication configuration panel opens.

  5. In the **Policy Name** field, enter an alphanumeric text string. You can use spaces, underscores (_), and dashes (-), but don't include special characters.

  6. Configure the policy frequency schedule as shown in the following table.


Policy Setting | Description  
---|---  
**Windowed** |   
On These Days | Configures the policy's frequency by defining an interval at which backups are captured. Based on this interval, the job runs once every specified number of days, weeks, months, or years.  
| Click the link for this parameter to modify the **Run** interval. The schedule appears in a calendar view. From this view you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Except | Defines an exception to the **Run** schedule. You can specify an **Except** value of daily, weekly, monthly, or yearly. For example, to skip the daily schedule every Friday, select **Weekly** and then select **Friday**.  
| Click the link for this parameter to modify the exception. The schedule appears in a calendar view. From this view, you can specify **Days** , **Weeks** , **Months** , or **Years**. The calendar view changes based on your selection.  
Within This Window | Defines a start and end time window for capturing backups.  
Run Once Per Window | Specifies that backups are captured once during the specified **Run Between** time window.  
Every | Specifies a repeat frequency duration (minutes or hours) for capturing backups during the specified **Run Between** time window. For example, every two hours.  
**Continuous** |   
Run Every | Specifies the time period to repeat backup capture.  
Start First Job At | Specifies the time of day at which to run the first job in the continuous cycle of backup captures.  
**Both Windowed and Continuous** |   
Retain For | Specifies how long to retain the backup. For example, retain the backup for two days.  
  
  1. Optionally, change the application priority from the **Priority** drop-down list. The default job priority is **Medium** , but you can change the priority to **High** or **Low**.

The backup plan scheduler identifies when one or more policies applied to applications are to run. It then initiates a job that places the policy into a queue when the scheduled start time occurs. Each policy type has a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state. This means that even if a job is supposed to start at a particular time, it executes only when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the system randomizes the selection of the application to run to ensure fairness across all applications of the same priority.

  2. From the **Target Pool** drop-down list, select the second OnVault pool where data is replicated.

  3. Click **Advanced Policy Settings** to configure advanced settings for the applications captured by this policy. See [Configure advanced policy settings for a backup plan policy](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for details.

  4. Click **Update Policy**. The **Templates** page opens.

  5. Click **Save Template**.




## Create a production to mirror policy

Production to mirror policies replicate snapshots of your production data to the mirror (snapshot pool) of a second backup/recovery appliance. These policy types help protect your application or VM data against a site failure by mirroring a full copy of that data to a remote production site. Applications are kept up to date and can be restarted at the remote site by accessing data from the remote DR copy.

You use a **Production to Mirror** policy in tandem with a resource profile that defines the replication destination as another backup/recovery appliance. Both the **Production to Mirror** policy and the resource profile are applied to applications in the **App Manager**.

StreamSnap replication replicates a point-in-time snapshot of the original application. See Create a streamsnap replication production to mirror policy for more information.

For a set of best practices when developing a production to mirror policy, see [Production to mirror policies](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-specific-best-practices#prod-mirror).

## Create a streamsnap replication production to mirror policy

Use these instructions to create a streamsnap production to mirror replication policy:

**Note:** Before you create a streamsnap replication policy, you must first create a snapshot policy as described in Create production to snapshot policy. **Production to Mirror** policies that use the streamsnap replication option are tied to a specific snapshot policy. They inherit the schedule and frequency settings, as well as the advanced settings, of the associated snapshot policy. You cannot save the streamsnap replication policy without an associated base snapshot policy.

  1. Click the **Backup Plans** tab, and then select **Templates** from the drop-down menu.

The **Templates** page opens.

  2. Select a template that includes a snapshot policy, and then select **Edit** from the drop-down menu.

The **Templates** page opens with the selected backup template.

  3. To create a streamsnap replication policy, do one of the following actions:

     * Click **+** between **Production** and **Mirror** in the backup plan policy map.
     * Click **+Add** next to **Mirror** in the **Policies** area of the **Templates** window.

The **Production to Mirror** policy configuration panel appears in the **Template** window.

  4. From **Replication Type** , select **StreamSnap** as the type of replication.

  5. In the **Policy Name** field, enter an alphanumeric text string. You can use spaces, underscores (_), and dashes (-), but don't include special characters.

  6. **Base Snapshot Policy** specifies a previously created snapshot policy in the template to use as the base snapshot policy for StreamSnap replication. A StreamSnap replication policy is always tied to a specific snapshot policy and uses its schedule and frequency settings. If more than one snapshot policy exists in the template, select the snapshot policy to use with the StreamSnap policy.

  7. Optionally, change the application priority from the **Priority** drop-down list. The default job priority for StreamSnap replication is **Medium** , but you can change the priority to **High** or **Low**.

The backup plan scheduler identifies when one or more policies applied to applications are to run. It then initiates a job that places the policy into a queue when the scheduled start time occurs. Each snapshot policy type has a pacing mechanism to ensure that the system is not overwhelmed with running jobs. This pacing mechanism uses job slots to achieve this steady state. This means that even if a job is supposed to start at a particular time, it executes only when a job slot is available.

If multiple applications are scheduled to run at the same time with the same job priority, the system randomizes the selection of the application to run to ensure fairness across all applications of the same priority.

**Note:** You can modify the priority of a Streamsnap replication when a job based on the policy template is running.
  8. To apply remote backup retention in a StreamSnap policy, choose from the following **Retention Options** :

     * **Only Keep the Most Recent Remote Image** : This option retains only the latest remote StreamSnap backup (default setting).
     * **Use Retention Specified in Snapshot Policy** : This option uses the same retention as the local (base) snapshot policy associated with this StreamSnap policy.
     * **Retain For** : This option retains the remote backup for a specific period (minutes, hours, days, weeks, months, or years). You define the retention period by selecting a choice from the drop-down list and then entering a specific value.

Backup/recovery appliances performing StreamSnap retention retain multiple point-in-time backups at the remote site, with retention behavior driven by this setting. When you retain backups at the remote backup/recovery appliance, a new backup is created at the remote appliance with a specific retention expiration date. Remote snapshot backups support all the same operations available with a local backup.

  9. By default, compression for StreamSnap replication is enabled. Compression increases the efficiency of StreamSnap replication to the remote backup/recovery appliance when transferring data over the network (for example, when replicating images and videos). When compression is enabled, all packets are compressed. The target backup/recovery appliance decompresses the packets before writing to the staging disk.

If compression is not needed for StreamSnap replication to the second backup/recovery appliance, click **Advanced Policy Settings** to access the **Policy Settings** dialog. Change the compress StreamSnap replication advanced setting to **Do not compress** , and then click **Save Changes**.

**Note:** Enabling compression might not always provide the best results. Compression uses additional CPU cycles but reduces network bandwidth consumption. If the available network bandwidth is better than system resources, such as CPUs, consider disabling compression.
  10. Click **Update Policy**. The **Templates** window opens.

  11. Click **Save Template**.




## What's next

  * Overview of [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-plan)
  * Create a [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template)
  * Create a [resource profile](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles)
  * Configure [advanced policy settings](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for an application backed up by the policy
  * [Apply a backup plan to an application](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-temp-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
