---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-edit/
title: Edit a backup plan for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:35.527957+00:00
---

# Edit a backup plan for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-edit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Edit a backup plan for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan)

This page explains how to edit and manage existing backup plans for vaulted backups. For a description of what backup plans are and how they are used, see [Backup plans in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). To create a backup plan, see [Create a backup plan for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

**Note:** When a backup plan is updated, all workloads that use the backup plan are updated asynchronously and automatically.

## Edit a backup plan

**Note:** When you edit a backup plan, you assign a backup rule that determines how long to retain the backup. If you are participating in the [30-day free trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial), then you will be charged for any backups that are retained beyond the end of the trial.

Use the following instructions to edit an existing backup plan for vaulted backups.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Select the backup plan that you want to edit, or check its box and click the more_verticon.

  3. Click **Edit**.

  4. You can edit the **Backup plan description** for the backup plan.

  5. You can add a new rule **Add rule** by clicking **Add Rule**.

In the **Add a backup rule** pane, enter your backup rule information and click **Save**.

     * **Name your backup rule** : Enter a name for the backup rule.
     * **Choose when to create backups** : Specify the recurrence and frequency of the backup.
     * **Window** : Select the **Timezone** , **Start time** , and **Endtime** for the backup job.
     * **Choose how long backups are kept before they are deleted** : Enter the duration in days that the backups should be retained before they are deleted. Note that this value must be equal to or greater than the [backup vault minimum enforced retention period](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention).

**Note:** If you are participating in the [30-day free trial](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial), then you will be charged for any backups that are retained beyond the end of the trial.
  6. You can also edit an existing rule or remove a rule from the backup plan by clicking the icons at the end of the rule row.

  7. Optionally set a **maximum custom on-demand retention**.

Your custom on-demand backups can be kept for up to the maximum custom on-demand retention. When you create an on-demand backup, set your retention or you can use an existing backup rule. If unspecified, the maximum limit for custom retention period uses a default value of the vault's minimum enforced retention period plus 30 days. This field is supported only for Compute Engine instances and disks for now. We will be extending the capability to other supported workloads as well.

Enter a value in days in **Maximum retention** This value must be greater than or equal to the vault's minimum enforced retention period: 1 day.

  8. Click **Save Changes**.




###  gcloud 

  1. Update a specific backup plan in the project. A backup plan can only be updated in regions supported by Backup and DR.
         
         gcloud backup-dr backup-plans update BACKUP_PLAN_NAME \
           --project=PROJECT_ID\
           --location=REGION \
           --description=DESCRIPTION \
           --backup-rule=BACKUP_RULE \
           --add-backup-rule=ADD_BACKUP_RULE \
           --remove-backup-rule=REMOVE_BACKUP_RULE
           --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `REGION`: the location where you want to create the backup plan.
     * `DESCRIPTION`: the updated description of the backup plan.
     * `BACKUP_RULE`: Full definition of an existing backup rule with updated values.
     * `ADD_BACKUP_RULE`: Parameters of the backup rule to be added to the backup plan. This flag can be repeated to add more backup rules.
     * `REMOVE_BACKUP_RULE`: The existing backup rule to be removed from the backup plan.
     * `MAX_ONDEMAND_RETENTION`: The maximum allowed custom retention period (in days) for on-demand backups created using this backup plan.

Example: To update two backup rules and description of an existing backup plan _sample-backup-plan_ in project _sample-project_ , at location _us-central1_ :

Run:
    
    gcloud alpha backup-dr backup-plans update sample-backup-plan \
      --project=sample-project --location=us-central1 \
      --backup-rule=BACKUP_RULE \
      --add-backup-rule=ADD_BACKUP_RULE \
      --description "This is a sample backup plan"
    

Example: To add backup rules to an existing backup plan _sample-backup-plan_ in project _sample-project_ , at location _us-central1_ :

Run:
    
    gcloud alpha backup-dr backup-plans update sample-backup-plan \
      --project=sample-project --location=us-central1 \
      --add-backup-rule BACKUP_RULE_1 --add-backup-rule BACKUP_RULE_2
    

Example: To remove a backup rule with ID _sample-daily-rule_ from an existing backup plan _sample-backup-plan_ in project _sample-project_ , at location _us-central1_ :

Run:
    
    gcloud alpha backup-dr backup-plans update sample-backup-plan \
      --project=sample-project --location=us-central1 \
      --remove-backup-rule sample-daily-rule
    

Example: To override backup rules in an existing backup plan _sample-backup-plan_ in project _sample-project_ , at location _us-central1_ , pass a path containing backup rules in YAML or JSON format: This flag is mutually exclusive with --add-backup-rule, --remove-backup-rule and --backup-rule flags.

Run:
    
    gcloud alpha backup-dr backup-plans update sample-backup-plan \
      --project=sample-project --location=us-central1 \
      --backup-rules-from-file (FILE_PATH)
    

**Note:** See YAML or JSON for examples of filling in FILE_PATH details.

Examples of filling in BACKUP_RULE details

Properties in these examples:

     * `RULE_NAME`: the name of the backup rule.
     * `BACKUP_RETENTION`: the retention period of the backup. Note that the backup retention period must be equal to or greater than the backup vault enforced minimum retention period.
     * `RECURRENCE`: the frequency at which backups to be created. It can be hourly, daily, weekly, monthly, or yearly.
     * `HOURS`: the frequency of the hourly backups. Specify this value only if you set the recurrence to hourly. The minimum hourly is always set to six hours.
     * `TIME_ZONE`: the time zone for the backup plan, such as UTC. Use the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format to include the timezone for the backup plan.
     * `START_TIME`: the start time is the hour of the day in a 24 hour format. The start time must be before the end time and is inclusive for the backup window.
     * `END_TIME`: the end time is the hour of the day in a 24 hour format. The end time must be after the start time and is exclusive for the backup window.

Example: An hourly backup rule with hourly backup frequency of 6 hours, store the backup for 30 days, and expect the backups to run only between 10:00 to 20:00 UTC:
    
    rule-id=sample-hourly-rule,retention-days=30,recurrence=HOURLY,hourly-frequency=6,time-zone=UTC,backup-window-start=10,backup-window-end=20
    
      Properties for this example:
    
        rule-id = "sample-hourly-rule" \
        retention-days = 30 \
        recurrence = HOURLY \
        hourly-frequency = 6 \
        time-zone = UTC \
        backup-window-start = 10 \
        backup-window-end = 20
    

Example: Daily backup rule with daily backup frequency of 6 hours and store it for 7 days
    
    rule-id=sample-daily-rule,retention-days=7,recurrence=DAILY,backup-window-start=1,backup-window-end=14
    
      Properties for this example:
    
      rule-id = "sample-daily-rule" \
      retention-days = 7 \
      recurrence = DAILY \
      backup-window-start = 1 \
      backup-window-end = 14
    

YAML file example: 
    
    backup-rules:
        - rule-id: weekly-rule
          retention-days: 7
          recurrence: WEEKLY
          backup-window-start: 0
          backup-window-end: 23
          days-of-week: [MONDAY, TUESDAY]
          time-zone: UTC
        - rule-id: daily-rule
          retention-days: 1
          recurrence: DAILY
          backup-window-start: 1
          backup-window-end: 24
          time-zone: UTC
    

JSON file example: 
    
    {
      "backup-rules": [
      {
      "rule-id": "weekly-rule",
      "retention-days": 7,
      "recurrence": "WEEKLY",
      "backup-window-start": 0,
      "backup-window-end": 23,
      "days-of-week": ["MONDAY", "TUESDAY"],
      "time-zone": "UTC"
      },
      {
      "rule-id": "daily-rule",
      "retention-days": 1,
      "recurrence": "DAILY",
      "backup-window-start": 1,
      "backup-window-end": 24,
      "time-zone": "UTC"
          }
        ]
      }
    

Run $ [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) help for details.




## View revisions of a backup plan ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) only)

You can only review revisions to backup plans using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

###  gcloud 

  1. To list the revisions to a backup plan:
         
         gcloud alpha backup-dr backup-plan-revisions list \
           --backup-plan=BACKUP_PLAN
           --location=LOCATION \
         

Replace the following:

     * `BACKUP_PLAN`: the name of the edited backup plan.
     * `LOCATION`: the location of the edited backup plan.

Example: To list all backup plan revisions for a backup plan _my-backup-plan_ in location _us-central1_ , run:
    
    gcloud alpha backup-dr backup-plan-revisions list \
      --backup-plan=my-backup-plan --location=us-central1
    




## View backup plan update jobs

You can [view system jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console#view-system-jobs) in the Google Cloud console.

## What's next

  * [Back up Compute Engine instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
