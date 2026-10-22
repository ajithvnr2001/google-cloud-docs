---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create/
title: Manage a backup plan \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:43.958293+00:00
---

# Manage a backup plan  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage a backup plan Stay organized with collections  Save and categorize content based on your preferences. 

[Overview of backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan)

This page explains how to create and manage a backup plan for vaulted backups. For a description of what backup plans are and how they are used, see [Backup plans in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

## Before you begin

To get the permissions that you need to create and manage a backup plan, ask your administrator to grant you the [Backup and DR User V2 ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.userv2) (`roles/backupdr.userv2`) IAM role on your backup vault project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create and manage a backup plan. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage a backup plan:

  * `backupdr.backupPlans.create`
  * `backupdr.backupPlans.list`
  * `backupdr.backupPlans.get`
  * `backupdr.backupPlans.delete`
  * `backupdr.backupVaults.associate`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For guidance on granting a user the ability to apply backup plans in a given project (without the ability to create backup plans), see [Identity and Access Management roles and permissions for the backup user](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#backup-user).

## Create a backup plan

Use the following instructions to create a backup plan for vaulted backups:

###  Console 

  1. In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Click **Create Backup plan**.

  3. From the **Resource Type** list, select your target resource.

  4. For **Identity** , enter a unique name in the **Name** field and an optional description in the **Description** field.

  5. For **Location** , select the region where the plan is active from the **Region** list.

  6. For **Destination** , select the backup vault that stores the data from the **Backup vault** list.

  7. To configure backup rules, complete the following steps:

     1. Click **Add rule**.

     2. From the **Recurrence** list, select a recurrence frequency.

     3. For **Backup window** , select a start time and an end time.

     4. In the **Retention period** field, enter a retention period.

     5. For **On-Demand Retention** , enter a value (in days) in the **Maximum custom on-demand retention** field to cap the retention period for on-demand backups created using this backup plan. If unspecified, then the vault's minimum enforced retention plus 30 days is used as the default limit. The maximum value you can enter is 3,653 (`3653`) days.

     6. For databases, click the **Database Logs** toggle to the on position to enable transaction log protection.

  8. Click **Create**.




A backup plan and its linked backup vault must reside in the same project.

###  gcloud 

Create a backup plan with a backup rule for a Compute Engine instance.
    
    
        gcloud backup-dr backup-plans create BACKUP_PLAN_NAME   
    
          --location=REGION   
    
          --resource-type=RESOURCE_TYPE   
    
          --project=PROJECT_ID   
    
          --backup-vault=BACKUPVAULT_NAME   
    
          --backup-rule=rule-id=RULE_NAME,recurrence=RECURRENCE,hourly-frequency=HOURS,time-zone=TIME_ZONE,backup-window-start=START_TIME,backup-window-end=END_TIME,retention-days=BACKUP_RETENTION
       

Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan.

  * `REGION`: the Google Cloud region where you want to create the backup plan.

  * `RESOURCE_TYPE`: the resource type to be protected by the backup plan. Values are:

    * `compute.googleapis.com/Instance`

    * `compute.googleapis.com/Disk`

    * `sql.googleapis.com/Instance`

    * `alloydb.googleapis.com/Cluster`

    * `file.googleapis.com/Instance`

  * `PROJECT_ID`: the name of the project where the backup vault resides.

  * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.

  * `RULE_NAME`: the name of the backup rule.

  * `RECURRENCE`: the frequency at which backups are created. It can be hourly, daily, weekly, monthly, or yearly.

  * `HOURS`: the frequency of the hourly backups. Specify this value only if you set the recurrence to hourly. The minimum hourly is always set to six hours.

  * `TIME_ZONE`: the time zone for the backup plan, such as UTC. Use the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format to include the timezone for the backup plan.

  * `START_TIME`: the start time is the hour of the day in a 24-hour format. The start time must be before the end time and is inclusive for the backup window.

  * `END_TIME`: the end time is the hour of the day in a 24-hour format. The end time must be after the start time and is exclusive for the backup window.

  * `BACKUP_RETENTION`: the retention period of the backup. Note that the backup retention period must be equal to or greater than the backup vault enforced minimum retention period.

  * `MAX_ONDEMAND_RETENTION`: The optional `max-custom-on-demand-retention-days` flag sets the maximum allowed custom retention period (in days) and caps user-requested retention for on-demand backups created using this backup plan.

  * `LOG_RETENTION`: the retention duration in days for database transaction logs (Point-in-Time Recovery). This flag is only valid for AlloyDB and Cloud SQL workloads. The specified duration must be greater than or equal to the minimum enforced retention duration of the destination backup vault.

**Note:** For most resource types, retention periods are capped at 36,135 days (99 years). For Cloud SQL instances, retention periods are capped at 3,653 days (10 years). For AlloyDB clusters, retention periods are capped at 365 days.



### Terraform

You can use a [Terraform resource to create a backup plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/backup_dr_backup_plan) with an hourly, daily, weekly, monthly, or yearly backup frequency.
    
    
    # Before creating a backup plan, you need to create backup vault (google_backup_dr_backup_vault).
    resource "google_backup_dr_backup_plan" "default" {
      provider       = google-beta
      location       = "us-central1"
      backup_plan_id = "my-bp"
      resource_type  = "compute.googleapis.com/Instance"
      backup_vault   = google_backup_dr_backup_vault.default.name
      # log_retention_days = 2 # Only applicable for Cloud SQL
    
      backup_rules {
        rule_id               = "rule-1"
        backup_retention_days = 5
    
        standard_schedule {
          recurrence_type  = "HOURLY"
          hourly_frequency = 6
          time_zone        = "UTC"
    
          backup_window {
            start_hour_of_day = 0
            end_hour_of_day   = 24
          }
        }
      }
    }
    

**Note:** For a backup plan to protect a Compute Engine instance, use `compute.googleapis.com/Instance`.  
To protect disks, use `compute.googleapis.com/Disk`.  
To protect a Cloud SQL instance, use `sqladmin.googleapis.com/Instance`.

**Note:** When you create a backup plan, you assign a backup rule that determines how long to retain the backup. If you are participating in the [30-day trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial), then you will be charged for any backups that are retained beyond the end of the trial.

### Examples of backup plans with backup rules

  * Back up a Compute Engine instance every six hours and store the backups for 11 days.
        
        gcloud backup-dr backup-plans create bp-hourly   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=compute.googleapis.com/Instance   
        
                  --backup-vault=test-bv   
        
                  --backup-rule=rule-id=rule-hourly,recurrence=HOURLY,hourly-frequency=6,backup-window-start=5,backup-window-end=12,retention-days=11
          

  * Back up disks daily between 5 a.m. and 12 p.m. and store the backups for 12 days.
        
        gcloud backup-dr backup-plans create bp-daily   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=compute.googleapis.com/Disk   
        
                  --backup-vault=test-bv   
        
                  --backup-rule=rule-id=rule-daily,recurrence=DAILY,backup-window-start=5,backup-window-end=12,retention-days=12
          

  * Back up a Compute Engine instance on Monday and Wednesday between 5 a.m. and 12 p.m. and store the backups for 13 days.
        
        gcloud backup-dr backup-plans create bp-weekly   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=compute.googleapis.com/Instance   
        
                  --backup-vault=test-bv   
        
                  --backup-rule=rule-id=rule-weekly,recurrence=WEEKLY,days-of-week='MON WED',backup-window-start=5,backup-window-end=12,retention-days=13
          

  * Back up disks on 1st and 15th of every month between 5 a.m. and 12 p.m. and store the backups for 14 days.
        
        gcloud backup-dr backup-plans create bp-monthly   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=compute.googleapis.com/Disk   
        
                  --backup-vault=test-bv   
        
                  --backup-rule=rule-id=rule-monthly,recurrence=MONTHLY,days-of-month='1 15',backup-window-start=5,backup-window-end=12,retention-days=14
          

  * Back up a Compute Engine instance on the 10th, 20th, 30th of March, June, September, December of every year, and store the backups for 16 days.
        
        gcloud backup-dr backup-plans create bp-yearly   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=compute.googleapis.com/Instance   
        
                  --backup-vault=test-bv   
        
                  --backup-rule=rule-id=rule-yearly,recurrence=YEARLY,months='MAR JUN SEP DEC',days-of-month='10 20 30',backup-window-start=5,backup-window-end=12,retention-days=16
          

  * Back up an AlloyDB cluster daily between 2 a.m. and 8 a.m. with 30 days of backup retention and 13 days of transaction log retention for Point-in-Time Recovery (PITR).
        
        gcloud backup-dr backup-plans create bp-alloydb-daily   
        
                  --project=test-project --location=us-central1   
        
                  --resource-type=alloydb.googleapis.com/Cluster   
        
                  --backup-vault=test-bv   
        
                  --log-retention-days=13   
        
                  --backup-rule=rule-id=rule-alloydb,recurrence=DAILY,backup-window-start=2,backup-window-end=8,retention-days=30
          




### Create a backup plan with no backup rule

Create a backup plan with no backup rule. A backup plan can be valid without scheduled rules if `max_custom_on_demand_retention_days` is configured.
    
    
       gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
          --location=REGION \
          --resource-type=RESOURCE_TYPE \
          --project=PROJECT_ID \
          --backup-vault=BACKUPVAULT_NAME \
          --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
    

**Note:** Backup and DR supports the creation of backup plans with no backup rules for Compute Engine instances, disks, and Cloud SQL instances only.

## List backup plans

Use the following instructions to list backup plans.

###  Console 

In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

The **Backup plan** page lists all of the backup plans in your project.

###  gcloud 

List the backup plans.
    
    
        gcloud backup-dr backup-plans list   
    
          --location=LOCATION   
    
          --project=PROJECT_ID
       

Replace the following:

  * `LOCATION`: the location of the backup plans.

  * `PROJECT_ID`: the name of the project where the backup plans are created.




## View backup plan details

Use the following instructions to view backup plan details.

###  Console 

  1. In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. In the list of backup plans, click the name of the backup plan you want to view.

The backup plan contains the following information:

     * Resource type

     * Backup plan details

     * Backup vault name

     * Backup storage location

     * Backup retention period




###  gcloud 

  1. View the backup plan details.
         
         gcloud backup-dr backup-plans describe BACKUP_PLAN_NAME \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.

     * `LOCATION`: the location of the backup plan.

     * `PROJECT_ID`: the name of the project where the backup plan is created.




## Delete a backup plan

A backup plan cannot be deleted if you are using it to protect a resource. To delete a backup plan, first remove the backup plan from the resource and then delete it.

When you delete a backup plan:

  * Backups created while the plan was applied are not affected. Backups expire according to their retention periods and can be accessed until then.
  * Any automations that reference the plan will no longer work.



Use the following instructions to delete a backup plan.

###  Console 

  1. In the Google Cloud console, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. In the list of backup plans, click the name of the backup plan you want to delete.

  3. Click **Delete**.

  4. In the overlay window that appears, confirm you want to delete the backup plan and its contents.

  5. Click **Delete**.




###  gcloud 

  1. Delete a backup plan.
         
         gcloud backup-dr backup-plans delete BACKUP_PLAN_NAME \
            --location=LOCATION \
            --project=PROJECT_ID
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan that you want to delete.

     * `LOCATION`: the location of the backup plan.

     * `PROJECT_ID`: the name of the project where the backup plan is created.




## What's next

  * [Back up Compute Engine instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
