---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/update/
title: gcloud beta container backup-restore backup-plans update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:11.803748+00:00
---

# gcloud beta container backup-restore backup-plans update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plans/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container backup-restore backup-plans update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container backup-restore backup-plans update - update a backup plan 
SYNOPSIS
    

`gcloud beta container backup-restore backup-plans update` (`BACKUP_PLAN` : `--location`=`LOCATION`) [`--async`] [`--deactivated`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--all-namespaces` | `--selected-applications`=`SELECTED_APPLICATIONS` | `--selected-namespace-labels`=`SELECTED_NAMESPACE_LABELS` | `--selected-namespaces`=[`SELECTED_NAMESPACES`,…]] [`--backup-delete-lock-days`=`BACKUP_DELETE_LOCK_DAYS` `--backup-retain-days`=`BACKUP_RETAIN_DAYS` `--locked`] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`--encryption-key`=`ENCRYPTION_KEY` `--include-secrets` `--include-volume-data` `--permissive-mode`] [`--paused` `--cron-schedule`=`CRON_SCHEDULE` `--exclusion-windows-file`=`EXCLUSION_WINDOWS_FILE` `--target-rpo-minutes`=`TARGET_RPO_MINUTES`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Backup for GKE backup plan. 
EXAMPLES
     To update a backup plan ``my-backup-plan`` in project ``my-project`` in location ``us-central1`` to add new description, run: 
    
    
    gcloud beta container backup-restore backup-plans update my-backup-plan --project=my-project --location=us-central1 --description="New description"

POSITIONAL ARGUMENTS
    

Backup plan resource - Name of the backup plan to update. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/backupPlans/<backupPlan>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `BACKUP_PLAN --project=<project> --location=<location>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_plan` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_PLAN`
     ID of the backup plan or fully qualified identifier for the backup plan. 

To set the `backup_plan` attribute: 

  * provide the argument `backup_plan` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `backup_plan` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkebackup/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--deactivated`
     If set, no further changes may be made to this backup plan and no further backups may be created for this plan. Backup deletion is still allowed. 
`--description`=`DESCRIPTION`
     Optional text description for the backup plan. 
`--etag`=`ETAG`
     The etag is used for optimistic concurrency control as a way to help prevent simultaneous updates or deletes of a resource from overwriting each other. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--all-namespaces`
     Scope of the backup includes resources from all namespaces. Mutually exclusive with --selected-namespaces, --selected-applications and \--selected-namespace-labels. 
`--selected-applications`=`SELECTED_APPLICATIONS`
     List of ProtectedApplication instances whose resources are included in the backup. Mutually exclusive with --all-namespaces, --selected-namespaces and \--selected-namespace-labels. e.g: \--selected-applications=namespace1/foo,namespace2/bar 
`--selected-namespace-labels`=`SELECTED_NAMESPACE_LABELS`
     List of Namespace labels whose resources are included in the backup. Mutually exclusive with --all-namespaces, --selected-namespaces and \--selected-applications. e.g: \--selected-namespace-labels=namespacelabel1=value1,namespacelabel2=value2 
`--selected-namespaces`=[`SELECTED_NAMESPACES`,…]
     List of namespaces whose resources are included in the backup. Mutually exclusive with --all-namespaces, --selected-applications and \--selected-namespace-labels. e.g: --selected-namespaces=foo,bar 
`--backup-delete-lock-days`=`BACKUP_DELETE_LOCK_DAYS`
     Number of days a backup produced via this plan cannot be deleted. 

Must be less than or equal to 90 days. If 0, delete operations are allowed. Updating this field does not affect existing backups. Backups created after a successful update will inherit this new value. 

`--backup-retain-days`=`BACKUP_RETAIN_DAYS`
     Number of days after which a backup produced via this plan is automatically deleted. 

Must be less than or equal to 365 days. If not set (value is 0), backups are not automatically deleted. If set, must be greater than the value for backup_delete_lock_days. Updating this field does not affect existing backups. Backups created after a successful update will inherit this new value. 

`--locked`
     If set, subsequent updates are not allowed to the backup plan's retention policy and this value cannot be changed. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta container backup-restore backup-plans update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta container backup-restore backup-plans update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
`--encryption-key`=`ENCRYPTION_KEY`
     Encryption key used for encrypting the backup. 

At this time, only the Cloud Key Management Service (Cloud KMS) is supported. Value must be entered as a relative name, e.g.: `projects/<project>/locations/<location>/keyRings/<key-ring>/cryptoKeys/<key>`. 

`--include-secrets`
     If true, secret resources are included in the backup if they fall within the scope. If unset, the default is false. 
`--include-volume-data`
     If true, snapshots are created for PD volumes corresponding to PersistentVolumeClaims that fall within the scope. If unset, the default is false. 
`--permissive-mode`
     If true, backups won't fail when Backup for GKE detects Kubernetes configuration that is known to cause restore failures. 
`--paused`
     If set, automatic backup creation is suppressed. When unset, automatic backup creation resumes with the next scheduled create event. 
`--cron-schedule`=`CRON_SCHEDULE`
     Schedule on which backups will be automatically created. 

Use standard [cron](http://en.wikipedia.org/wiki/Cron#Overview) syntax. For example, `10 3 * * *` will automatically create a backup at 0310 every day. All times are interpreted as UTC. The minimum interval between scheduled backups is 10 minutes. 

`--exclusion-windows-file`=`EXCLUSION_WINDOWS_FILE`
     If provided, defines an array of exclusion windows for RPO based schedules from the given config file in yaml. Only used together with --target-rpo-minutes for creation and rpo-based plans during update. 
`--target-rpo-minutes`=`TARGET_RPO_MINUTES`
     Schedule backups based on target RPO minutes instead of fixed cron schedules. Cannot be used with --cron-schedule. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkebackup/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container backup-restore backup-plans update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/backup-plans/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
