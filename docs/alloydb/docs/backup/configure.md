---
url: https://docs.cloud.google.com/alloydb/docs/backup/configure/
title: Configure backup plans \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:37.051108+00:00
---

# Configure backup plans  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure backup plans Stay organized with collections  Save and categorize content based on your preferences. 

To customize your data protection retention windows, encryption settings, and backup frequency in AlloyDB for PostgreSQL, you can adjust the default 14-day continuous backup configuration or set up an independent automated backup schedule:

  * Configure continuous backup and recovery.

  * Enable and configure an additional automated backup schedule.




## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Manage continuous backup and recovery

This section describes the Google Cloud CLI or Google Cloud console commands that you can use to configure, disable, or re-enable continuous backup and recovery on your cluster.

### Configure continuous backup

You can configure the recovery window and encryption settings of your cluster's continuous backup system.

If you decrease the recovery window's size, then AlloyDB immediately shortens the distance into the past that you can perform a point-in-time recovery. For example, if you reduce the window's size from 14 days to 7 days, then points in time more than 7 days in the past become unavailable for recovery.

If you increase the window's size, then the span of time available for point-in-time recovery grows in real time until it reaches the new limit that you specified. For example, if you change the window's size from 7 to 14 days, it takes an additional 7 days for the recovery window's effective size to grow to its new maximum of 14 days into the past.

After configuring the plan, it might take up to 24 hours for continuous backup and recovery to take a backup and enable its continuous recovery capability. If you want to accelerate the backup operation without waiting for 24 hours and to avoid data loss, then you can take an [on-demand](https://docs.cloud.google.com/alloydb/docs/backup/overview#on-demand-or) backup after you configure the plan.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Data protection**.

  4. Under **Continuous backups and recovery policy** , click **Edit**.

  5. In the **Recovery window (days)** field, enter a new recovery window size.

  6. If you want to encrypt this cluster's continuous backups and data-change logs using a specific [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the cluster's encryption configuration, follow these additional steps:

     1. Click **Advanced encryption options**.

        1. Click the **Customer-managed encryption key (CMEK)** radio button.

        2. Click the **Select a customer-managed key** list, and select a key.

  7. Click **Update**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To configure continuous backup and recovery on a cluster, use the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command.
    
    
    gcloud alloydb clusters update CLUSTER_ID \
      --continuous-backup-recovery-window-days=WINDOW_LENGTH \
      --region=REGION_ID \
      --project=PROJECT_ID

Replace the following:

  * `CLUSTER_ID`: The ID of the cluster.

  * `WINDOW_LENGTH`: The length of time, in days, of this cluster's continuous backup and recovery window. The value must be between `1` and `35`, inclusive.

The value of this argument defines both of the following aspects of continuous backup and recovery:

    * The maximum distance into the past, relative to the present, that you can [perform a point-in-time recovery](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr#cbr) based on continuous backups.

    * The length of time that AlloyDB retains continuous backups and data-change logs in storage. To ensure that you can restore to any point in time within your recovery window, AlloyDB retains backups and logs for one day longer than the specified value.

This argument is optional. If you do not include it, then AlloyDB sets the recovery window to 14 days.

    * `REGION_ID`: the ID of the region where the cluster is placed.
    * `PROJECT_ID`: the ID of the project where the cluster is placed.

If you want to encrypt this cluster's continuous backups and data-change logs using a specific [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the cluster's encryption configuration, provide these additional arguments:

    * `--continuous-backup-encryption-key=`KEY_ID: the ID of the CMEK key to use.

    * `--continuous-backup-encryption-key-keyring=`KEYRING_ID: the ID of the key's keyring.

    * `--continuous-backup-encryption-key-location=`LOCATION_ID: the ID of the keyring's region. Note that the region you specify must match the cluster's region.

    * `--continuous-backup-encryption-key-project=`PROJECT_ID: the keyring's project ID.

To use CMEK with AlloyDB, you need to complete some additional setup steps. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).




### Disable continuous backup and recovery

When you disable continuous backup, [point-in-time recovery](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr#cbr) becomes unavailable for your cluster. It becomes available again if you re-enable continuous backup, as described in the next section.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click the **Data protection** tab.

  4. Under **Continuous backups and recovery policy** , click **Edit**.

  5. Clear the **Google-managed continuous data protection** checkbox.

  6. Click **Update**.




### gcloud

To disable continuous backup and recovery on a cluster, use the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command.
    
    
      gcloud alloydb clusters update CLUSTER_ID \
          --no-enable-continuous-backup \
          --region=REGION_ID \
          --project=PROJECT_ID

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster.
  * `REGION_ID`: the ID of the region where the cluster is placed.
  * `PROJECT_ID`: the ID of the project where the cluster is placed. ### Enable continuous backup



If you re-enable continuous backup after previously disabling it, then point-in-time recovery becomes available again as well. The recovery window begins with the first subsequent backup that AlloyDB creates. To make point-in-time recovery available as soon as possible, [create an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand) right after re-enabling continuous backup. Otherwise, the recovery window commences with the next daily backup that AlloyDB takes.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Data protection**.

  4. Under **Continuous backups and recovery policy** , click **Edit**.

  5. Select the **Google-managed continuous data protection** checkbox.

  6. Click **Update**.




### gcloud

To re-enable your cluster's continuous backup configuration after disabling it, follow the same procedure as configuring continuous backup, adding an `--enable-continuous-backup` argument to the gcloud CLI command:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
        --enable-continuous-backup \
        --continuous-backup-recovery-window-days=WINDOW_LENGTH \
        --region=REGION_ID \
        --project=PROJECT_ID

Replace the following:

  * `CLUSTER_ID`: The ID of the cluster.

  * `WINDOW_LENGTH`: The length of time, in days, of this cluster's continuous backup and recovery window. The value must be between `1` and `35`, inclusive.

The value of this argument defines both of the following aspects of continuous backup and recovery:

    * The maximum distance into the past, relative to the present, that you can [perform a point-in-time recovery](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr#cbr) based on continuous backups.

    * The length of time that AlloyDB retains continuous backups and data-change logs in storage. To ensure that you can restore to any point in time within your recovery window, AlloyDB retains backups and logs for one day longer than the specified value.

This argument is optional. If you do not include it, then AlloyDB sets the recovery window to 14 days.

    * `REGION_ID`: the ID of the region where the cluster is placed.
    * `PROJECT_ID`: the ID of the project where the cluster is placed.

If you want to encrypt this cluster's continuous backups and data-change logs using a specific [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the cluster's encryption configuration, provide these additional arguments:

    * `--continuous-backup-encryption-key=`KEY_ID: the ID of the CMEK key to use.

    * `--continuous-backup-encryption-key-keyring=`KEYRING_ID: the ID of the key's keyring.

    * `--continuous-backup-encryption-key-location=`LOCATION_ID: the ID of the keyring's region. Note that the region you specify must match the cluster's region.

    * `--continuous-backup-encryption-key-project=`PROJECT_ID: the keyring's project ID.

To use CMEK with AlloyDB, you need to complete some additional setup steps. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).




## Configure additional automated backups

This section shows how to enable or disable an automated backup schedule on your cluster that works independently from the continuous backup system. This includes configuring how often AlloyDB takes these additional automated backups, and for how long it retains them.

### Automated backup configuration attributes

Each AlloyDB cluster can have one customizable automated backup configuration, which includes the following attributes:

  * A schedule for taking backups. You can set this to specific days of the week, and at specific times on those days.

  * A retention policy, expressed either as an amount of time to keep backups or as a number of backups to keep. By default, AlloyDB retains automated backups for 14 days.

Backups older than the retention policy are subject to automated deletion. For more information, see [Backup retention and deletion](https://docs.cloud.google.com/alloydb/docs/backup/overview#backup-retention).

  * The amount of time that AlloyDB waits before canceling an incomplete attempt to take a new automated backup. AlloyDB uses a default timeout of one hour.

  * A data-encryption preference: either the default Google-managed encryption or a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) that you provide.




### Enable and configure automated backups

### Console

The Google Cloud console lets you enable and disable automated backups, but it does not let you specify a backup schedule or other configuration. To do that, use the gcloud CLI instead.

If you enable automated backups on a cluster where you have not configured this feature, AlloyDB applies a default configuration that schedules one automated backup per day, with a 14-day retention window, using Google-managed encryption.

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Data protection**.

  4. Under **Automated backup policy** , click **Edit**.

  5. Select the **Automate backups** checkbox.

  6. Click **Update**.




### gcloud

To enable automated backups with the gcloud CLI, you must specify a backup schedule. All other configuration options are optional. AlloyDB applies the default values listed in the previous section to any configuration options that you don't explicitly set.

Each time you run this command to define a new automated backup configuration, AlloyDB completely replaces the cluster's current configuration with the new one.

To enable automated backups without specifying a complete configuration, use the Google Cloud console.

**Warning:** When you run the `gcloud alloydb clusters update` command to configure automated backups, you replace the cluster's entire existing automated backup policy with the new settings you provide.

Use the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command to define a schedule for creating automated backups:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
        --automated-backup-days-of-week=DAYS_LIST \
        --automated-backup-start-times=UTC_TIMES_LIST \
        --region=REGION_ID \
        --project=PROJECT_ID

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster you want to define the schedule for.

  * `DAYS_LIST`: a comma-separated list of one or more days when you want automated backups to be taken. Valid values are `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY`.

  * `UTC_TIMES_LIST`: a comma-separated list of one or more times when you want automated-backup operations to start on the specified days. Specify times in the format `HH:00` on a 24-hour cycle in UTC time.

  * `REGION_ID`: the ID of the region where the cluster is placed.

  * `PROJECT_ID`: the ID of the project where the cluster is placed.




This example sets a cluster to take an automated backup at midnight UTC on every Monday and Thursday:
    
    
    gcloud alloydb clusters update my-cluster \
        --automated-backup-days-of-week=MONDAY,THURSDAY \
        --automated-backup-start-times=00:00 \
        --region=us-central1 \
        --project=my-project

To encrypt scheduled backups using a CMEK key instead of the default Google-managed encryption, provide these additional arguments:

  * `--automated-backup-encryption-key=KEY_ID`: the ID of the CMEK key to use.

  * `--automated-backup-encryption-key-keyring=KEYRING_ID`: the ID of the key's keyring.

  * `--automated-backup-encryption-key-location=LOCATION_ID`: the ID of that keyring's region. Note that it must match the cluster's region.

  * `--automated-backup-encryption-key-project=PROJECT_ID`: the keyring's project ID.




To use CMEK with AlloyDB, you need to complete some additional setup steps. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).

You can also specify the automated backups retention policy, based on either a duration or a number of backups to keep. To do this, include either of the following arguments:

  * To have AlloyDB retain all automated backups for a certain amount of time, use `--automated-backup-retention-period=DURATION`.

Replace `DURATION` with a duration string, as described by [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). You can specify a duration as long as one year.

  * To have AlloyDB instead retain a certain number of backups, use `--automated-backup-retention-count=COUNT`.

Replace `COUNT` with the number of automated backups that AlloyDB should retain for up to one year.




### Disable automated backups

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Data protection**.

  4. Under **Automated backup policy** , click **Edit**.

  5. Clear the **Automate backups** checkbox.

  6. Click **Update**.




### gcloud

To disable automated backups, use the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command.
    
    
    gcloud alloydb clusters update CLUSTER_ID \
        --disable-automated-backup \
        --region=REGION_ID \
        --project=PROJECT_ID

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster to disable automated backups on.
  * `REGION_ID`: the ID of the region where the cluster is placed.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.



## View backup plans

You can view details about your cluster's automated or continuous backup plans.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Data protection**.




Find details about the cluster's backup plans in the **Continuous backups and recovery policy** and **Automated backup policy** tables.

### gcloud

  1. [Use the `gcloud alloydb clusters describe` command](https://docs.cloud.google.com/alloydb/docs/cluster-view#gcloud) to display details about the cluster.

  2. The `continuousBackupConfig` and `continuousBackupInfo` keys summarize the cluster's continuous backup and recovery configuration. This includes whether continuous backup is enabled, the size of its recovery window, and its encryption settings.

The `continuousBackupInfo` key also displays the continuous backup schedule: always one backup per day, every day.

  3. The `automatedBackupPolicy` key, if present, summarizes the cluster's automated backup configuration. This includes whether automated backup is enabled, and displays the backup schedule and encryption settings.




For example, the following output of a `gcloud alloydb clusters describe` command shows that the cluster has automated backup enabled, with backups taken every Monday and Thursday at around 1 AM UTC. It also has continuous backup enabled, with a 10-day recovery window.
    
    
    automatedBackupPolicy:
        enabled: true
        location: us-central1
        weeklySchedule:
            daysOfWeek:
            - MONDAY
            - THURSDAY
            startTimes:
            - hours: 1
    clusterType: PRIMARY
    continuousBackupConfig:
        enabled: true
        recoveryWindowDays: 10
    continuousBackupInfo:
        encryptionInfo:
            encryptionType: GOOGLE_DEFAULT_ENCRYPTION
        schedule:
        - MONDAY
        - TUESDAY
        - WEDNESDAY
        - THURSDAY
        - FRIDAY
        - SATURDAY
        - SUNDAY
    clusterType: PRIMARY
    createTime: '2023-01-23T02:42:56.953258476Z'
    databaseVersion: POSTGRES_14
    encryptionInfo:
        encryptionType: GOOGLE_DEFAULT_ENCRYPTION
    name: [...]
    reconciling: false
    state: READY
    uid: [...]
    updateTime: '2023-02-06T19:08:57.367222025Z'
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
