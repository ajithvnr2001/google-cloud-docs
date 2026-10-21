---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan/
title: Plan a set of backups \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:42.261995+00:00
---

# Plan a set of backups  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Plan a set of backups Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to create a Backup for GKE backup plan, which is used for backing up your workloads in Google Kubernetes Engine (GKE).

Backup plans provide the configuration, location, and management functions for a sequence of backups. A backup plan contains a backup configuration including the source cluster, the selection of which workloads to back up, and the region in which backup artifacts produced under this plan are stored.

You can create one or more backup plans for each cluster. There are two main reasons why you might want more than one backup plan for a cluster:

  * You want to store your backup artifacts in multiple regions. In this case, create a backup plan for each region in which you want to store backups.
  * You want to partition the backups of your cluster, for example:

    * Instead of one very large backup taken at a single time of the day, you want multiple smaller backups distributed throughout the day.
    * You want to back up some portions of your cluster more often than others (such as daily backups for some namespaces and hourly backups for others).



We recommend that every cluster has at least one backup plan.

Backup for GKE doesn't support backing up a cluster from one project to another. You can only create a backup plan to a cluster within the same project where the cluster is created.

You can create a backup plan with a backup scheduling method to automatically create backups: smart scheduling or cron scheduling. We recommend smart scheduling for your backup plan. This ensures backups are automatically created to meet the [Recovery Point Objective (RPO)](https://en.wikipedia.org/wiki/Disaster_recovery) requirements. For more information, see [Automatic backup creation and deletion](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule).

If you don't want to create a backup plan with backup scheduling methods, you need to [manually back up](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup) your workloads. After creating a backup plan, you can create a backup from that plan.

## Before you begin

  * [Enable Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install)
  * [Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster)



## Required roles

To get the permissions that you need to create and manage a backup plan, ask your administrator to grant you the Backup for GKE Backup Admin (`roles/gkebackup.backupAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a backup plan

Create a backup plan by using the gcloud CLI or the Google Cloud console.

**Note:** This will automatically install the Backup for GKE [agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke#architecture) in the specified cluster. Installing the agent can take several minutes.

### gcloud

To create a backup plan with a schedule, run the following command:
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN_NAME \
        --project=PROJECT_ID \
        --location=BACKUP_LOCATION \
        --cluster=CLUSTER \
        --all-namespaces \
        --include-secrets \
        --include-volume-data \
        --encryption-key=ENCRYPTION_KEY \
        --target-rpo-minutes=TARGET_RPO_MINUTES \
        --exclusion-windows-file=EXCLUSION_WINDOWS_FILE \
        --cron-schedule=CRON_SCHEDULE \
        --backup-retain-days=RETAIN_DAYS \
        --backup-delete-lock-days=DELETE_LOCK_DAYS \
        --locked
    

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan that you want to create.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `BACKUP_LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, for example `us-central1`. See [About resource locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).
  * `CLUSTER`: the relative path to the cluster: 
    * Regional clusters: `projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME`
    * Zonal clusters: `projects/PROJECT_ID/locations/ZONE/clusters/CLUSTER_NAME`
  * `CLUSTER_NAME`: the name of the cluster to back up.
  * `--all-namespaces`: backs up all namespaces for the cluster.

Alternatively, specify:

    * `--selected-applications` with a list of [ProtectedApplications](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) as `NAMESPACE1/APP1,NAMESPACE2/APP2,...` to back up.
    * `--selected-namespaces` with a list of namespaces as `NAMESPACE1,NAMESPACE2,...` to back up.
    * `--selected-namespace-labels` with a list of namespace labels as `NAMESPACELABEL1=VALUE1,NAMESPACELABEL2=VALUE2,...` to back up.

You must specify one of these options when creating a backup plan.

  * `--include-secrets`: an optional argument to include `Secret` resources if they are in the scope of the backup.

  * `--include-volume-data`: an optional argument to include persistent volume data in the backup. Don't set this argument if you want to create empty volumes during restore.

  * `ENCRYPTION_KEY`: an optional argument to define the path to a customer-managed encryption key. See [About CMEK encryption](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek).

  * `TARGET_RPO_MINUTES`: required argument if `EXCLUSION_WINDOWS_FILE` is set. Specify the target [RPO](https://en.wikipedia.org/wiki/Disaster_recovery) in minutes. Smart scheduling uses this value to automatically create backups. The minimum is 60 minutes (1 hour) and maximum is 86400 minutes (60 days). You can't set both `TARGET_RPO_MINUTES` and `CRON_SCHEDULE` simultaneously in one backup plan.

  * `EXCLUSION_WINDOWS_FILE`: an optional argument to define time windows during which backup cannot happen. All times are interpreted as UTC. This argument is available only when `TARGET_RPO_MINUTES` is set.

**Note:** Backup jobs are scheduled to start and finish outside the window duration as much as possible, but ongoing jobs won't be canceled if an exclusion window begins when jobs are in progress.
  * `CRON_SCHEDULE`: an optional argument to define a cron schedule that automatically creates backups and supports standard [cron](https://en.wikipedia.org/wiki/Cron) syntax. For example `"10 3 * * *"` creates a backup at 3:10 AM every day. All times are interpreted as UTC. The minimum interval between scheduled backups is 10 minutes. You can't set both `CRON_SCHEDULE` and `TARGET_RPO_MINUTES` simultaneously in one backup plan.

  * `RETAIN_DAYS`: required argument if `TARGET_RPO_MINUTES` or `CRON_SCHEDULE` is set. Specify the number of days to retain the backup. Backups for this plan are automatically deleted after the retention period expires.

  * `DELETE_LOCK_DAYS`: an optional argument to specify the number of days during which backups cannot be deleted. If this value is set, then backups created for that plan cannot be deleted (either automatically or manually) until that lifetime expires.

**Caution:** If you have a delete lock on a backup, you cannot delete that backup, the plan that contains the backup, or the project that contains the plan, until the lock expires.
  * `--locked`: an optional argument to lock the retention policy for the backup plan.




For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/create) documentation.

**Create a backup plan for all namespaces with a RPO of 24 hours and a single exclusion window**

Create a window.yaml file, containing a YAML array of `exclusionWindows`.
    
    
    exclusionWindows:
    - startTime:
        hours: 1
        minutes: 0
      duration: "3600s"
      singleOccurrenceDate:
        day: 1
        month: 3
        year: 2024
    

The following command creates a backup plan for all namespaces with a target RPO of 24 hours and no backups are allowed from 1 AM to 2 AM on March 1, 2024. Backups are retained for seven days and locked for three days after creation:
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN \
        --location=LOCATION \
        --cluster=CLUSTER \
        --all-namespaces \
        --include-secrets \
        --include-volume-data \
        --target-rpo-minutes=1440 \
        --exclusion-windows-file=window.yaml \
        --backup-retain-days=7 \
        --backup-delete-lock-days=3 \
        --locked
    

**Create a backup plan for all namespaces with 2 hours RPO and multiple exclusion windows**

Create a window.yaml file, containing a YAML array of `exclusionWindows`: one weekly window and one single occurrence window.
    
    
    exclusionWindows:
    - startTime:
        hours: 15
        minutes: 0
      duration: "5400s"
      daysOfWeek:
        daysOfWeek:
        - MONDAY
        - FRIDAY
    - startTime:
        hours: 1
        minutes: 0
      duration: "3600s"
      singleOccurrenceDate:
        day: 1
        month: 3
        year: 2024
    

The following command creates a backup plan for all namespaces with 2 hours target RPO and no backups allowed from 1 AM to 2 AM on March 1, 2024 and 3 PM to 4:30 PM every Monday and Friday. Backups are retained for seven days and locked for three days after creation:
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN \
        --location=LOCATION \
        --cluster=CLUSTER \
        --all-namespaces \
        --include-secrets \
        --include-volume-data \
        --target-rpo-minutes=120 \
        --exclusion-windows-file=window.yaml \
        --backup-retain-days=7 \
        --backup-delete-lock-days=3 \
        --locked
    

**Create a backup plan for all namespaces with a daily cron schedule**

The following command creates a backup plan to schedule daily backup for all namespaces at 5:20 AM every day. Backups are retained for seven days and locked for three days after creation:
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN \
        --location=LOCATION \
        --cluster=CLUSTER \
        --all-namespaces \
        --include-secrets \
        --include-volume-data \
        --cron-schedule="20 5 * * *" \
        --backup-retain-days=7 \
        --backup-delete-lock-days=3 \
        --locked
    

**Create a backup plan for a selected namespace with an hourly cron schedule**

The following command creates a backup plan to schedule hourly backup for the selected namespace ( my-ns ) at minute 15 every hour. Backups are retained for three days after creation:
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN \
        --location=LOCATION \
        --cluster=CLUSTER \
        --selected-namespaces=my-ns \
        --include-secrets \
        --include-volume-data \
        --cron-schedule="15 * * * *" \
        --backup-retain-days=3
    

**Create a backup plan for a selected`ProtectedApplication`**

The following command creates a backup plan to select the [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) ( my-ns/my-app ).
    
    
    gcloud beta container backup-restore backup-plans create BACKUP_PLAN \
        --location=LOCATION \
        --cluster=CLUSTER \
        --selected-applications=my-ns1/my-app1,my-ns2/my-app2 \
        --include-secrets \
        --include-volume-data
    

**Note:** To use this scope for a backup, you must first create `ProtectedApplications` in the cluster. See [ProtectedApplications](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).

### Console

Use the following instructions to create a backup plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click **Create a backup plan**.

  4. In the **Plan details** section, do the following:

     1. Select the cluster to back up.
     2. Enter the backup plan name and optional description.
     3. Choose a location for the backup.
  5. To automatically create backups, in the **Backup schedule** section, select the **Enable backup schedule** checkbox, and then choose one of the following methods:

**Note:** All backup schedules are interpreted in UTC timezone.
     1. Select **Smart schedule** and do the following:

        1. In the **Target RPO** field, enter the **RPO** for the backup plan and then select the RPO value in **Minutes** , **Hours** , or **Days** from the drop-down.
        2. Optional: Select the **Define a single recurring backup exclusion window** checkbox for the backup exclusion. 
           1. Choose **Daily** or **Weekly** from the exclusion window.
           2. In the **Repeats on** section, select which days of the week to exclude from the backup plan. This field is only displayed for weekly exclusion window.
           3. In the **Window start time** field, enter the start time for the backup plan exclusion.
           4. In the **Duration** field, enter the backup plan exclusion duration and then select **Seconds** , **Minutes** , or **Hours** from the drop-down.
        3. Optional: If you want to create one or more single occurrence backup exclusion window, select **Define one or more backup exclusion dates** checkbox, and do the following: 
           1. Click **Add exclusion date**.
           2. In the **Start date and time for exclusion window** field, click the calendar_month icon and then select the **Date** and **Time** for the backups.
           3. In the **Duration** field, enter the backup plan exclusion duration and then select **Seconds** , **Minutes** , or **Hours** from the drop-down.
     2. Select **Cron schedule** and enter a **CRON expression** using standard [cron](https://en.wikipedia.org/wiki/Cron) syntax. For example, `10 3 * * *` creates a backup at 3:10 AM every day. The minimum interval between scheduled backups is 10 minutes.

  6. In the **Retention policy** section, do the following:

     1. Set the number of days to retain the backup before the backup is automatically deleted.
     2. Set the number of days during which backups cannot be deleted.
     3. To lock the retention policy, click the lock icon to turn the lock from **Off** to **On.**
  7. In the **Configure backup scope and encryption** section, do the following:

     1. Select the scope for the backup plan:

        * Click **Entire cluster (including all namespaces)** to back up all namespaced resources in the backup.
        * Click **Selected namespaces within this cluster** to choose the namespaces you want to include in the backup plan.
        * Click **Selected protected applications within this cluster** to add resources by specifying the namespace and application name.
     2. Click the **Secrets** checkbox to include [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) resources.

     3. Click the **Persistent volume data** checkbox if you want the volume data in your backup. If you choose to skip volume data, you cannot restore volume data during restore. However, you will have two options to choose volume data when restoring: **Provision new volumes** or **Reuse existing volumes**.

     4. To enable CMEK encryption, you must first grant the access to the appropriate CMEK keys (see [About CMEK encryption](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek)).

        1. Click the **Use a customer-managed encryption key** checkbox to select a key.
  8. Review the backup plan details and click **Create plan**.




### Terraform

Create a `google_gke_backup_backup_plan` resource.
    
    
    resource "google_gke_backup_backup_plan" "basic" {
       name = "BACKUP_PLAN"
       cluster = google_container_cluster.CLUSTER.id
       location = "LOCATION"
       retention_policy {
         backup_retain_days = 7
       }
       backup_schedule {
         cron_schedule = "17 3 * * *"
       }
       backup_config {
         include_volume_data = true
         include_secrets = true
         all_namespaces = true
       }
    }
    

Replace the following:

  * `BACKUP_PLAN`: the name of the backup plan that you want to create.
  * `CLUSTER`: the name of your `google_container_cluster` resource.
  * `LOCATION` \- the region where you want to store the backups.



For more information, see [gke_backup_backup_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_backup_plan).

**Note:** Google recommends [creating a restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan) after creating a backup plan to ensure that your backups can be restored.

## View a backup plan

View a backup plan and its details by using the gcloud CLI or the Google Cloud console.

### gcloud

To list all the backup plans within the project and region, run the following command:
    
    
    gcloud beta container backup-restore backup-plans list \
        --project=PROJECT_ID \
        --location=LOCATION
    

For **`list`** commands only, you can provide `-` as the value for any parameters except `PROJECT_ID`. The `-` value acts as a wildcard. The `-` value is the default for any parameter if you don't specify a command-line option or set a property.

For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/list) documentation.

To see the details of a backup plan, run the following command:
    
    
    gcloud beta container backup-restore backup-plans describe BACKUP_PLAN \
         --project=PROJECT_ID \
         --location=LOCATION
    

For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/describe) documentation.

### Console

Use the following instructions to view a backup plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine.](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup Plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click the **Details** tab to see the plan details.




## Update a backup plan

You can update the backup plan information, such as its description, backup scope, backup mode, encryption, or backup schedule. You can also modify the retention policy of the backup plan, such as how long to retain the backups or the period of time during which backups cannot be deleted.

**Note:** Any updates to the backup plan apply only to backups created after the backup plan is updated. Updates to the backup plan don't affect existing backups.

Update a backup plan by using the gcloud CLI or the Google Cloud console.

### gcloud

To update a backup plan, for example by adding a new description, run the following command:
    
    
    gcloud beta container backup-restore backup-plans update BACKUP_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION \
        --description=DESCRIPTION
    

For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/update) documentation.

### Console

Use the following instructions to update a backup plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup Plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click the **Details** tab to edit the plan details.

  6. Click _edit_ **Edit** to edit a plan section and click **Save changes**.




## Pause a backup schedule

Backup plans can be paused manually or automatically to pause the backup schedules. When the backup plan is paused, automatic backups aren't created. However, you can still create manual backups. For instructions, see [Create a manual backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup#manual).

  * **Manual pause** : You can manually pause a backup plan using Google Cloud console, gcloud, or terraform.
  * **Automatic pause** : Backup for GKE can automatically pause a backup plan in the following scenarios:

    * When initiating a backup (scheduled or manual), if any of the following errors occur:

      * **`StatusInvalidCluster`** : The `StatusInvalidCluster` error indicates an unrecoverable condition where the cluster name is invalid or metadata information of the cluster is unavailable.
      * **`GKEMetadataNotEnabledOnNodepool`** : The `GKEMetadataNotEnabledOnNodepool` error represents an unrecoverable condition where the cluster has Workload Identity Federation for GKE enabled, but `GKE_METADATA` is not configured on any node pool, preventing the agent from functioning correctly.
      * **`AgentNotInstalled`** : The `AgentNotInstalled` error indicates an unrecoverable condition where the cluster doesn't have the necessary agent custom resource definitions installed, implying improper agent installation.
    * If a backup remains in the _Creating_ phase for an hour, it might indicate connectivity issues between the cluster and Google Cloud or agent misconfiguration.

    * To prevent repeated backup failures, the backup plan might be automatically paused if it exhibits a pattern of prolonged or frequent unsuccessful backup attempts. This situation typically occurs when the system detects a significant period without a successful backup or a consistent series of recent failures, which indicates a persistent underlying issue.

If the backup plan was paused due to backup failures, you can troubleshoot the backup failure issue by checking the **Current RPO risk** field on the **Backup plan** details page and the **Status reason** field on the recent failed backups. If the pause is unintentional and the issue is resolved, resume the backup plan to continue automatic backups.




You can set up alerts for paused backup plans and unpause them when the underlying issues are fixed. For instructions, see [Set up alerts for paused backup plans](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/alerts-backup-plan).

### gcloud

To pause a backup schedule, run the following command:
    
    
    gcloud beta container backup-restore backup-plans update BACKUP_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION \
        --paused
    

For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/update) documentation.

### Console

Use the following instructions to pause a backup schedule in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup Plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click **Pause Schedule** and then click **Pause Schedule** in the confirmation dialog.




### Terraform
    
    
       resource "google_gke_backup_backup_plan" "basic" {
         name = "BACKUP_PLAN"
         cluster = google_container_cluster.CLUSTER.id
         location = "LOCATION"
         backup_schedule {
           paused = True
         }
         backup_config {
           include_volume_data = true
           include_secrets = true
           all_namespaces = true
         }
       }
    

Replace the following:

  * `BACKUP_PLAN`: the name of the backup plan that you want to pause.
  * `CLUSTER`: the name of your `google_container_cluster` resource.
  * `LOCATION`: the location of the backup plan.



## Resume a backup plan

### Console

Use the following instructions to resume a backup plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click **Resume schedule** and then click **Resume schedule** in the confirmation dialog.




### Terraform
    
    
       resource "google_gke_backup_backup_plan" "basic" {
         name = "BACKUP_PLAN"
         cluster = google_container_cluster.CLUSTER.id
         location = "LOCATION"
         backup_schedule {
           paused = false
         }
         backup_config {
           include_volume_data = true
           include_secrets = true
           all_namespaces = true
         }
       }
    

Replace the following:

  * `BACKUP_PLAN`: the name of the backup plan that you want to resume.
  * `CLUSTER`: the name of your `google_container_cluster` resource.
  * `LOCATION`: the location of the backup plan.



## Delete a backup plan

You can delete a backup plan by using the gcloud CLI or the Google Cloud console. You cannot delete a backup plan if the plan contains any backups.

### gcloud

To delete a backup plan, run the following command:
    
    
    gcloud beta container backup-restore backup-plans delete BACKUP_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION
    

For the full list of options, refer to the [`gcloud beta container backup-restore backup-plans delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/delete) documentation.

### Console

Use the following instructions to delete a backup plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backup Plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click _delete_ **Delete plan**.

  6. Type the backup plan name and then click **Delete backup plan** in the confirmation dialog.




## What's next

  * Learn more about [planning a set of restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan).
  * Learn more about [manually backing up your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
