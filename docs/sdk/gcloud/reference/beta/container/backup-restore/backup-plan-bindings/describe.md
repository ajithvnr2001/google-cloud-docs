---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plan-bindings/describe/
title: gcloud beta container backup-restore backup-plan-bindings describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:10.353216+00:00
---

# gcloud beta container backup-restore backup-plan-bindings describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plan-bindings/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container backup-restore backup-plan-bindings describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container backup-restore backup-plan-bindings describe - describe a backup plan binding 
SYNOPSIS
    

`gcloud beta container backup-restore backup-plan-bindings describe` (`BACKUP_PLAN_BINDING` : `--backup-channel`=`BACKUP_CHANNEL` `--location`=`LOCATION`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe a Backup for GKE backup plan binding. 
EXAMPLES
     To describe a backup plan binding ``my-backup-plan-binding`` in project ``my-project`` in location ``us-central1`` under backup channel ``my-backup-channel``, run: 
    
    
    [gcloud beta container backup-restore backup-plan-bindings](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backup-plan-bindings) describe my-backup-plan-binding --backup-channel=my-backup-channel --project=my-project --location=us-central1

POSITIONAL ARGUMENTS
    

Backup plan binding resource - Name of the backup plan binding to describe. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/backupChannels/<backupChannel>/backupPlanBindings/<backupPlanBinding>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `BACKUP_PLAN_BINDING --project=<project> --location=<location> --backup-channel=<backupChannel>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_plan_binding` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_PLAN_BINDING`
     ID of the backup plan binding or fully qualified identifier for the backup plan binding. 

To set the `backup_plan_binding` attribute: 

  * provide the argument `backup_plan_binding` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--backup-channel`=`BACKUP_CHANNEL`
     Backup Channel name. 

To set the `backup-channel` attribute: 

  * provide the argument `backup_plan_binding` on the command line with a fully specified name; 
  * provide the argument `--backup-channel` on the command line. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `backup_plan_binding` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkebackup/location`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkebackup/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container backup-restore backup-plan-bindings describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/backup-plan-bindings/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
