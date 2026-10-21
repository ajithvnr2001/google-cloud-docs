---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backup-plans/create/
title: gcloud beta backup-dr backup-plans create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:00.341915+00:00
---

# gcloud beta backup-dr backup-plans create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backup-plans/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta backup-dr backup-plans create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta backup-dr backup-plans create - creates a new Backup Plan 
SYNOPSIS
    

`gcloud beta backup-dr backup-plans create` (`BACKUP_PLAN` : `--location`=`LOCATION`) `--backup-vault`=`BACKUP_VAULT` `--resource-type`=`RESOURCE_TYPE` [`--async`] [`--backup-rule`=[`PROPERTY`=`VALUE`,…]] [`--compute-instance-properties`=[`PROPERTY`=`VALUE`,…]] [`--description`=`DESCRIPTION`] [`--disk-properties`=[`PROPERTY`=`VALUE`,…]] [`--labels`=[`KEY`=`VALUE`,…]] [`--log-retention-days`=`LOG_RETENTION_DAYS`] [`--max-custom-on-demand-retention-days`=`MAX_CUSTOM_ON_DEMAND_RETENTION_DAYS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a new backup plan in the project. It can only be created in locations where Backup and DR is available. 
EXAMPLES
     To create a new backup plan ``sample-backup-plan`` for Compute Engine instances in project ``sample-project``, at location ``us-central1``, with resource-type ``compute.<UNIVERSE_DOMAIN>/Instance`` and backup-vault ``backup-vault`` with 2 backup-rules: 

run: 
    
    
    gcloud beta backup-dr backup-plans create sample-backup-plan --project=sample-project --location=us-central1 --resource-type 'compute.<UNIVERSE_DOMAIN>/Instance' --backup-vault <BACKUP-VAULT> --backup-rule <BACKUP-RULE> --backup-rule <BACKUP-RULE>

To create a new backup plan ``sample-filestore-backup-plan`` for Filestore instances in project ``sample-project``, at location ``us-central1``, with resource-type ``file.<UNIVERSE_DOMAIN>/Instance`` and backup-vault ``backup-vault`` with 1 backup-rule: 

run: 
    
    
    gcloud beta backup-dr backup-plans create sample-filestore-backup-plan --project=sample-project --location=us-central1 --resource-type 'file.<UNIVERSE_DOMAIN>/Instance' --backup-vault <BACKUP-VAULT> --backup-rule <BACKUP-RULE>

Backup Rule Examples: 

1\. Hourly backup rule with hourly backup frequency of 6 hours and store it for 30 days, and expect the backups to run only between 10:00 to 20:00 UTC 

<BACKUP-RULE>: rule-id=sample-hourly-rule,retention-days=30,recurrence=HOURLY,hourly-frequency=6,time-zone=UTC,backup-window-start=10,backup-window-end=20 

Properties: 

  * rule-id = "sample-hourly-rule" 
  * retention-days = 30 
  * recurrence = HOURLY 
  * hourly-frequency = 6 
  * time-zone = UTC 
  * backup-window-start = 10 
  * backup-window-end = 20 



2\. Daily backup rule with daily backup frequency of 6 hours and store it for 7 days 

<BACKUP-RULE>: rule-id=sample-daily-rule,retention-days=7,recurrence=DAILY,backup-window-start=1,backup-window-end=14 

Properties: 

  * rule-id = "sample-daily-rule" 
  * retention-days = 7 
  * recurrence = DAILY 
  * backup-window-start = 1 
  * backup-window-end = 14 



3\. Weekly backup rule with weekly backup frequency on every MONDAY & FRIDAY and store it for 21 days 

<BACKUP-RULE>: rule-id=sample-weekly-rule,retention-days=21,recurrence=WEEKLY,days-of-week="MONDAY FRIDAY",backup-window-start=10,backup-window-end=20 

Properties: 

  * rule-id = "sample-weekly-rule" 
  * retention-days: 21 
  * recurrence = WEEKLY 
  * days-of-week = "MONDAY FRIDAY" 
  * backup-window-start = 10 
  * backup-window-end = 20 


POSITIONAL ARGUMENTS
    

Backup Plan resource - Name of the backup plan to be created. Once the backup plan is created, this name can't be changed. The name must be unique for a project and location. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `BACKUP_PLAN` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_PLAN`
     ID of the Backup Plan or fully qualified identifier for the Backup Plan. 

To set the `name` attribute: 

  * provide the argument `BACKUP_PLAN` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Backup Plan. 

To set the `location` attribute: 

  * provide the argument `BACKUP_PLAN` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

Backup Vault resource - The backup vault where the backups gets stored using this backup plan. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 



This must be specified. 

`--backup-vault`=`BACKUP_VAULT`
     ID of the Backup Vault or fully qualified identifier for the Backup Vault. 

To set the `name` attribute: 

  * provide the argument `--backup-vault` on the command line. 


`--resource-type`=`RESOURCE_TYPE`
     Type of resource to which the backup plan should be applied. 

For example: 

  * `compute.<UNIVERSE_DOMAIN>/Instance` for Compute Engine instances. 
  * `file.<UNIVERSE_DOMAIN>/Instance` for Filestore instances. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
`--backup-rule`=[`PROPERTY`=`VALUE`,…]
     Backup rule that defines parameters for when and how a backup is created. This flag can be repeated to create more backup rules. Parameters for the backup rule include: 

`rule-id`
     Name of the backup rule. The name must be unique and start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. 
`retention-days`
     Duration for which backup data should be retained. It must be defined in "days". The value should be greater than or equal to the enforced retention period set for the backup vault. 
`recurrence`
     Frequency for the backup schedule. It must be either: HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY. 
`backup-window-start`
     Start time of the interval during which backup jobs should be executed. It can be defined as backup-window-start=2, that means backup window starts at 2 a.m. The start time and end time must have an interval of 6 hours. 
`backup-window-end`
     End time of the interval during which backup jobs should be executed. It can be defined as backup-window-end=14, that means backup window ends at 2 p.m. The start time and end time must have an interval of 6 hours. 

Jobs are queued at the beginning of the window and will be marked as `SKIPPED` if they do not start by the end time. Jobs that are in progress will not be canceled at the end time. 

`time-zone`
     The time zone to be used for the backup schedule. The value must exist in the [IANA tz database](https://www.iana.org/time-zones). The default value is UTC. E.g., Europe/Paris 
Following flags are mutually exclusive: 
`hourly-frequency`
     Frequency for hourly backups. An hourly frequency of 2 means backup jobs will run every 2 hours from start time till the end time defined. The hourly frequency must be between 4 and 23. The value is needed only if recurrence type is HOURLY. 
`days-of-week`
     Days of the week when the backup job should be executed. The value is needed if recurrence type is WEEKLY. E.g., MONDAY,TUESDAY 
`days-of-month`
     Days of the month when the backup job should be executed. The value is needed only if recurrence type is YEARLY. E.g.,"1,5,14" 
`months`
     Month for the backup schedule. The value is needed only if recurrence type is YEARLY. E.g., JANUARY, MARCH 
`week-day-of-month`
     Recurring day of the week in the month or year when the backup job should be executed. E.g. FIRST-SUNDAY, THIRD-MONDAY. The value can only be provided if the recurrence type is MONTHLY or YEARLY. Allowed values for the number of week - FIRST, SECOND, THIRD, FOURTH, LAST. Allowed values for days of the week - MONDAY to SUNDAY. 
E.g., "rule-id=sample-daily-rule,recurrence=WEEKLY,backup-window-start=2,backup-window-end=14,retention-days=20,days-of-week='SUNDAY MONDAY'" 
`--compute-instance-properties`=[`PROPERTY`=`VALUE`,…]
     Workload-specific properties for Compute Engine instance backups generated by this plan. 

`guest-flush`
     Indicates whether to perform a guest flush operation before taking a compute backup. When set to true, the system will attempt to ensure application-consistent backups. When set to false, the system will create crash-consistent backups. Default value is false. 
Following properties are mutually exclusive: 
`boot-disk-only`
     Indicates whether to backup only the boot disk of the compute instance. When set to true, only the boot disk is backed up. 
`disk-exclusion-labels`
     Key-value pairs of labels used to identify disks to be excluded from backup for the compute instance. 

Examples: --compute-instance-properties=guest-flush=true,boot-disk-only=true \--compute-instance-properties=disk-exclusion-labels=backup=exclude 

`--description`=`DESCRIPTION`
     Provide a description of the backup plan, such as specific use cases and relevant details, in 2048 characters or less. 

E.g., This is a backup plan that performs a daily backup at 6 p.m. and retains data for 3 months. 

`--disk-properties`=[`PROPERTY`=`VALUE`,…]
     Workload-specific properties for disk backups generated by this plan. 

`guest-flush`
     Indicates whether to perform a guest flush operation before taking a disk backup. When set to true, the system will attempt to ensure application-consistent backups. When set to false, the system will create crash-consistent backups. Default value is false. 

Example: --disk-properties=guest-flush=true 

`--labels`=[`KEY`=`VALUE`,…]
     If you have assigned labels to your resources for grouping, you can provide the label using this flag.A label is a key-value pair. 

Keys must start with a lowercase character and contain only hyphens (-), underscores (`), lowercase characters, and numbers. Values must contain only hyphens (-), underscores (`), lowercase characters, and numbers. 

`--log-retention-days`=`LOG_RETENTION_DAYS`
     Configures how long logs will be stored. It is defined in "days". This value should be greater than or equal to minimum enforced retention duration of the backup vault. 
`--max-custom-on-demand-retention-days`=`MAX_CUSTOM_ON_DEMAND_RETENTION_DAYS`
     Configure the maximum retention period for on-demand backups. The value must be greater than or equal to the minimum enforced retention period set on the backup vault. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Creates a new backup plan 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud backup-dr backup-plans create](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plans/create)
    
    
    [gcloud alpha backup-dr backup-plans create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plans/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
