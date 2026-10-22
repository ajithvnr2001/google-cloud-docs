---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup/
title: Back up Cloud SQL instances to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:19.021461+00:00
---

# Back up Cloud SQL instances to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up Cloud SQL instances to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to back up Cloud SQL instances to a backup vault, which provides immutability and enforced retention.

In the Google Cloud console, you can back up Cloud SQL instances to a backup vault by applying backup plans. You can back up in either of these two ways. Both methods allow you to store your backups securely in a backup vault, providing a reliable way to recover your Cloud SQL instances in case of data loss or other unexpected events.

  * **Scheduled backups** : automatically back up Cloud SQL instances at specific intervals, such as daily, weekly, monthly, or yearly.
  * **On-demand backups**. You can create on-demand backups whenever needed. On-demand backups are useful for creating backups before making significant changes to your databases or for ad hoc data protection.

**Note:** Enable a [30-day introductory trial for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial) to explore a unified, centralized backup solution featuring immutable backup vaults.

## Before you begin

  1. Enable the Backup and DR API where the Cloud SQL instances are located.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).

  3. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

  4. Assign IAM roles and permissions to the backup user.

  5. Grant backup vault access in the Cloud SQL project.

  6. Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.

  7. **For CMEK-enabled instances** : if the source Cloud SQL instance is protected with a customer-managed encryption key (CMEK), you must grant the `roles/cloudkms.cryptoKeyEncrypterDecrypter` Identity and Access Management role to the Backup and DR service agent. This permission is required on the Cloud Key Management Service key used by the source Cloud SQL instance.

The Backup and DR service agent is in the project where the backup vault is located. Grant this role to the service account before attempting to protect CMEK-enabled Cloud SQL instances.




## IAM roles and permissions for the backup user

To get the permissions that you need to configure scheduled backups or run on-demand backups, ask your administrator to grant you the following IAM roles on your backup vault project: 

  * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)
  * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure scheduled backups or run on-demand backups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure scheduled backups or run on-demand backups:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.fetchForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.updateForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.getForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance`
  * `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`
  * `backupdr.backupPlans.useForCloudSqlInstance`
  * `backupdr.locations.list`
  * `backupdr.operations.get`
  * `cloudasset.assets.searchAllResources`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Dynamic permissions required for each API call

The following table lists the dynamic permissions required for each API call:

Resource | Action to be performed on the resource | Permissions required for each API call | Project to assign permission to  
---|---|---|---  
Backup vault | Create backup vault | `backupdr.backupVaults.create` | Admin project  
| Delete backup vault | `backupdr.backupVaults.delete` | Admin project  
| Update backup vault | `backupdr.backupVaults.update` | Admin project  
| List backup vaults | `backupdr.backupVaults.list` | Admin project  
| Get backup vault | `backupdr.backupVaults.get` | Admin project  
Backup plan | Create backup plan | `backupdr.backupPlans.create` | Admin project  
| Delete backup plan | `backupdr.backupPlans.delete` | Admin project  
| Get backup plan | `backupdr.backupPlans.get` | Admin project  
| List backup plans | `backupdr.backupPlans.list` | Admin project  
Backup plan associations | Create backup plan association | `cloudsql.instances.updateBackupDrConfig`  
`backupdr.backupPlanAssociations.createForCloudSqlInstance`  
`backupdr.backupPlans.useForCloudSqlInstance` | Workload project  
Workload project  
Admin project  
| Delete backup plan association | `backupdr.backupPlanAssociations.deleteForCloudSqlInstance`  
`cloudsql.instances.updateBackupDrConfig` | Workload project  
Workload project  
| Trigger an on-demand backup on backup plan association | `backupdr.backupPlanAssociations.triggerBackupForCloudSqlInstance` | Workload project  
| Get backup plan association | `backupdr.backupPlanAssociations.getForCloudSqlInstance` | Workload project  
| List backup plan associations | `backupdr.backupPlanAssociations.list` | Workload project  
| Fetch backup plan associations | `backupdr.backupPlanAssociations.fetchForCloudSqlInstance` | Workload project  
| Change backup plan associations | `backupdr.backupPlanAssociations.updateForCloudSqlInstance` | Workload project  
Data source | Get data source | `backupdr.bvdataSources.get` | Admin project  
| List data source | `backupdr.backupPlanAssociations.list` | Admin project  
| Point-in-time recovery restore | `backupdr.bvdataSources.useReadOnlyForCloudSqlInstance` | Admin project  
Backups | Get backup | `backupdr.bvbackups.get` | Admin project  
| List backups | `backupdr.bvbackups.list` | Admin project  
| Fetch backups | `backupdr.bvbackups.fetchForCloudSqlInstance` | Admin project  
| Delete backup | `backupdr.bvbackups.delete` | Admin project  
| Restore backup | `backupdr.bvbackups.useReadOnlyForCloudSqlInstance` | Admin project  
Data source references | Get data source reference | `backupdr.dataSourceReferences.getForCloudSqlInstance` | Workload project  
| List data source references | `backupdr.dataSourceReferences.list` | Workload project  
| Fetch data source references | `backupdr.dataSourceReferences.fetchForCloudSqlInstance` | Workload project  
Operations | List operations | `backupdr.operations.list` | Respective project  
| Get operations | `backupdr.operations.get` | Respective project  
  
## Grant backup vault access in the Cloud SQL project

To back up a Cloud SQL instance in a project different from where the backup vault is created, you must grant the **Backup and DR Cloud SQL Operator** (`roles/backupdr.cloudSqlOperator`) IAM role to the backup vault service agent within the Cloud SQL project. If the backup vault project where the backups will be stored is different from the Cloud SQL project then assign the role to the backup vault service agent within the Cloud SQL project.

To back up a Cloud SQL instance in the same project where the backup vault is created, no roles are required to be granted.

For information about granting roles to the backup vault service agent within the project you intend to back up, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service_agent).

## Configure a scheduled backup

Use the following instructions to configure a scheduled backup for Cloud SQL instances.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. From the **Resource Type** list, select **Cloud SQL**.

  4. From the **Project** list, select a project where the Cloud SQL instance is located.

  5. From the **Region** list, select the region where your instances are located.

  6. From the **Resources** list, click **Browse**. Choose the Cloud SQL instance that you want to back up and click **Done**.

  7. Click **Continue**.

  8. From the **Backup plan** list, click **Select**.

  9. Choose a backup plan that you want to protect the Cloud SQL instances with.

  10. Click **Done**.

  11. Review the backup details and click **Schedule**.




###  gcloud 

  1. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create) and a Cloud SQL instance.

  2. Configure a scheduled backup using the `gcloud backup-dr backup-plan-associations create` command:
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
               --location=CSQL_REGION \
               --project=CSQL_PROJECT_ID \
               --resource=projects/CSQL_PROJECT_ID/instances/CSQL_INSTANCE_ID \
               --resource-type=sqladmin.googleapis.com/Instance \
               --backup-plan=projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.

     * `CSQL_REGION`: the region where the Cloud SQL instances are located.

     * `CSQL_PROJECT_ID`: the name of the project where the Cloud SQL instances are located.

     * `CSQL_INSTANCE_ID`: the Cloud SQL instance ID.

     * `PROJECT_ID`: the name of the project where backup plans exist.

     * `LOCATION`: the location of the instance.

     * `BACKUP_PLAN`: the name of the backup plan.




### Terraform

You can use a [Terraform resource to configure a scheduled backup](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/backup_dr_backup_plan_association).
    
    
    # Before creating a backup plan association, you need to create backup plan (google_backup_dr_backup_plan)
    # and Cloud SQL Instance (google_sql_database_instance).
    resource "google_backup_dr_backup_plan_association" "csql_association" {
      provider                   = google-beta
      location                   = "us-central1"
      backup_plan_association_id = "my-csql-bpa"
      resource                   = "projects/${google_sql_database_instance.default.project}/instances/${google_sql_database_instance.default.name}"
      resource_type              = "sqladmin.googleapis.com/Instance"
      backup_plan                = google_backup_dr_backup_plan.csql_default.name
    }
    

## Change the associated backup plan for a Cloud SQL instance

You can swap the backup plan that's applied to a Cloud SQL instance to another backup plan instead. The backup plan you want to change to must meet the following criteria:

  * The backup plan the same backup vault.

  * The backup plan is in the same region as the Cloud SQL instance.




Use the following instructions to change the backup plan associated with a Cloud SQL instance.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have (or previously had) backup plans applied or their backups stored in a backup vault within a project.

  2. Select the data source that will get a different plan. Either from the backup details page for the backup, or from the more_vert menu, select **Change backup plan**. The **Select a backup plan** window lists only the backup plans that are valid for this instance.

  3. Select a backup plan and click **Apply**.




###  gcloud 

  * Change the assigned backup plan.
        
        gcloud backup-dr backup-plan-associations update BACKUP_PLAN_ASSOCIATION_NAME \
          --workload-project=INSTANCE_PROJECT_ID \
          --location=INSTANCE_REGION \
          --backup-plan=BACKUP_PLAN \
          --project=SELECTED_BACKUP_PLAN_PROJECT_ID
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association resource.

    * `INSTANCE_PROJECT_ID`: the project ID of the Cloud SQL instance.

    * `INSTANCE_REGION`: the location of the Cloud SQL instance.

    * `BACKUP_PLAN`: the name of the backup plan that you are switching to.

    * `SELECTED_BACKUP_PLAN_PROJECT_ID`: the project ID of the selected backup plan.




## List instances for which backups are scheduled

Use the following instructions to list the Cloud SQL instances for which backups are scheduled.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. At the top of the table, select **Filter table** > **Resource type**. Select **Cloud SQL**. This limits the display to only the Cloud SQL instances that have backup plans applied and their backups stored in a backup vault within a project.




###  gcloud 

List Cloud SQL instances for which backups are scheduled using the `gcloud alpha backup-dr backup-plan-associations fetch-for-resource-type` command:
    
    
      gcloud alpha backup-dr backup-plan-associations fetch-for-resource-type sqladmin.googleapis.com/Instance \
      --location=LOCATION \
      --project=PROJECT_ID
    

Replace the following:

  * LOCATION: the location of the scheduled backups.

  * PROJECT_ID: the name of the project where the Cloud SQL instances are located.




## On-demand backups

You can initiate an on-demand backup for a Cloud SQL instance with a backup plan by triggering the backup rule of your choice to run immediately. On-demand backups typically capture only the data changed since the last incremental backup.

When creating an on-demand backup, you can choose a rule from the backup plan associated with the Cloud SQL instance. This rule determines when the on-demand backup gets deleted. You can check the backup job status from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

**Note:** You can only run one backup job at a time. If an on-demand or scheduled backup job is already in progress, then attempting to start another on-demand backup job, the new job fails with the `Unable to queue the operation` error.

### Create an on-demand backup

Use the following instructions to create an on-demand backup.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the resource to back up. Either from the more_vert menu, or from the details page for the resource, select **Create on-demand backup**. 

  3. In the **Create an on-demand backup** window, select a backup rule to use and click **Create**.

  4. To view the status of the on-demand backup job, click **Notifications**.


**Note:** The on-demand backup is stored in the backup vault that is configured with the associated backup plan.

###  gcloud 

  1. Create an on-demand backup. Initiate an on-demand backup using an existing backup plan association. Specify a rule ID to determine the expiration period for this single, on-demand backup:
         
         gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
         --backup-rule-id=RULE_ID \
         --project=PROJECT_ID \
         --location=LOCATION \
         [--no-async]
         

Replace the following:

     * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association. 

**Note:** To get a list of backup plans associated with the Cloud SQL instance, run the command `gcloud alpha backup-dr backup-plan-associations fetch-for-resource-type sqladmin.googleapis.com/Instance --location=LOCATION --project=PROJECT_ID`
     * RULE_ID: the backup rule name that you want to associate to run on-demand backups.

     * PROJECT_ID: the name of the project.

     * LOCATION: the location of the scheduled backups.




## Remove protection from a Cloud SQL instance

You can remove protection from a Cloud SQL instance by removing the backup plan applied to the instance. Removing a backup plan from a Cloud SQL instance doesn't delete any backups created while the backup plan was in use. You can still access and manage these existing backups until they expire.

Use the following instructions to remove protection from a Cloud SQL instance:

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click the name of the database that you want to remove a backup plan from.

  3. Select **Remove backup plan**.




###  gcloud 

Unprotect a Cloud SQL instance.
    
    
      gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME \
      --project=PROJECT_ID \
      --location=LOCATION
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association that you want to delete.

  * PROJECT_ID: the name of the project.

  * LOCATION: the location of the scheduled backup.




## Limitations

For Cloud SQL instances encrypted with CMEK, Backup and DR proactively validates permissions. If the Backup and DR service agent from the backup vault's project does not have the necessary `roles/cloudkms.cryptoKeyEncrypterDecrypter` role on the source instance's KMS key, the backup plan association creation fails. Ensure the required IAM permissions are in place before associating a backup plan.

## What's next

  * [Restore a Cloud SQL instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-restore).

  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
