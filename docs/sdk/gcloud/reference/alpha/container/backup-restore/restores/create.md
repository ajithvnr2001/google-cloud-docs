---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/restores/create/
title: gcloud alpha container backup-restore restores create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:06.076489+00:00
---

# gcloud alpha container backup-restore restores create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/restores/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container backup-restore restores create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container backup-restore restores create - creates a restore 
SYNOPSIS
    

`gcloud alpha container backup-restore restores create` (`RESTORE` : `--location`=`LOCATION` `--restore-plan`=`RESTORE_PLAN`) `--backup`=`BACKUP` [`--description`=`DESCRIPTION`] [`--filter-file`=`FILTER_FILE`] [`--labels`=[`KEY`=`VALUE`,…]] [`--volume-data-restore-policy-overrides-file`=`VOLUME_DATA_RESTORE_POLICY_OVERRIDES_FILE`] [`--async` | `--wait-for-completion`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Creates a Backup for GKE restore. 
EXAMPLES
     To create a restore ``my-restore`` in location ``us-central1`` under restore plan ``my-restore-plan``, run: 
    
    
    gcloud alpha container backup-restore restores create my-restore --project=my-project --location=us-central1 --restore-plan=my-restore-plan --backup=projects/my-project/locations/us-east1/backupPlans/my-backup-plan/backups/my-backup

POSITIONAL ARGUMENTS
    

Restore resource - Name of the restore to create. Once the restore is created, this name can't be changed. This must be 63 or fewer characters long and must be unique within the project and location. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/restorePlans/<restorePlan>/restores/<restore>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `<restore> --project=<project> --location=<location> --restore-plan=<restorePlan>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `restore` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RESTORE`
     ID of the restore or fully qualified identifier for the restore. 

To set the `name` attribute: 

  * provide the argument `restore` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `restore` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkebackup/location`. 


`--restore-plan`=`RESTORE_PLAN`
     Restore Plan name. 

To set the `restore-plan` attribute: 

  * provide the argument `restore` on the command line with a fully specified name; 
  * provide the argument `--restore-plan` on the command line; 
  * set the property `gkebackup/restore_plan`. 


REQUIRED FLAGS
    

`--backup`=`BACKUP`
     Name of the backup from which to restore under the backup plan specified in restore plan. Format: projects/<project>/locations/<location>/backupPlans/<backupPlan>/backups/<backup>. 
OPTIONAL FLAGS
    

`--description`=`DESCRIPTION`
     Optional text description for the restore. 
`--filter-file`=`FILTER_FILE`
     JSON/YAML file containing the configuration of the fine-grained restore filter which can be used to further refine the resource selection of the Restore beyond the coarse-grained scope defined in the RestorePlan. 

For more information about examples and how to use this filter, please refer to the Backup for GKE documentation: <https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore>. 

`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--volume-data-restore-policy-overrides-file`=`VOLUME_DATA_RESTORE_POLICY_OVERRIDES_FILE`
     If provided, defines an array of volume data restore policy overrides from the given config file in yaml. 
At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--wait-for-completion`
     Wait for the created restore to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta container backup-restore restores create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restores/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
