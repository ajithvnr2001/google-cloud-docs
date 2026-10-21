---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/restore-channels/create/
title: gcloud alpha container backup-restore restore-channels create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:59:30.770224+00:00
---

# gcloud alpha container backup-restore restore-channels create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/restore-channels/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha container backup-restore restore-channels create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha container backup-restore restore-channels create - create a restore channel 
SYNOPSIS
    

`gcloud alpha container backup-restore restore-channels create` (`RESTORE_CHANNEL` : `--location`=`LOCATION`) `--destination-project`=`DESTINATION_PROJECT` [`--async`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create a Backup for GKE restore channel. 
EXAMPLES
     To create a restore channel ``my-restore-channel`` in project ``my-project`` in location ``us-central1`` with destination project ``projects/restore-project``, run: 
    
    
    gcloud alpha container backup-restore restore-channels create my-restore-channel --project=my-project --location=us-central1 --destination-project=projects/restore-project

POSITIONAL ARGUMENTS
    

Restore channel resource - Name of the restore channel to create. Once the channel is created, this name can't be changed. This must be 63 or fewer characters long and must be unique within the project and location. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/restoreChannels/<restoreChannel>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `RESTORE_CHANNEL --project=<project> --location=<location>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `restore_channel` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`RESTORE_CHANNEL`
     ID of the restore channel or fully qualified identifier for the restore channel. 

To set the `restore_channel` attribute: 

  * provide the argument `restore_channel` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `restore_channel` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkebackup/location`. 


REQUIRED FLAGS
    

`--destination-project`=`DESTINATION_PROJECT`
     The project where Restores are allowed to be created. The format is `projects/{project}`. Project can be project number or project ID. E.g. `projects/1234567890` or `projects/my-project`. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     The description of the restore channel. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkebackup/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta container backup-restore restore-channels create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-channels/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
