---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/create/
title: gcloud alpha filestore snapshots create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:34:46.745821+00:00
---

# gcloud alpha filestore snapshots create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/filestore/snapshots/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha filestore snapshots create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha filestore snapshots create - create a Filestore snapshot 
SYNOPSIS
    

`gcloud alpha filestore snapshots create` `SNAPSHOT` `--file-share`=`FILE_SHARE` `--instance`=`INSTANCE` `--instance-zone`=`INSTANCE_ZONE` [`--async`] [`--labels`=[`KEY`=`VALUE`,…]] [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Take a Filestore snapshot of an instance file share. 

This command can fail for the following reasons: 

  * An instance with the same name already exists. 
  * The active account does not have permission to create snapshots. 


EXAMPLES
     To create a snapshot with the name 'my-snapshot' from an instance called 'my-instance' in 'us-central1-c' and the source file share called 'my-fs', run: 
    
    
    gcloud alpha filestore snapshots create my-snapshot --instance=my-instance --file-share=my-fs --instance-zone=us-central1-c

To create a snapshot with the name 'my-snapshot' in a particular region like 'us-central1' from an instance called 'my-instance' in 'us-central1-c' and the source file share called 'my-fs', run: 
    
    
    gcloud alpha filestore snapshots create my-snapshot --instance=my-instance --file-share=my-fs --instance-zone=us-central1-c --region=us-central1

POSITIONAL ARGUMENTS
    

`SNAPSHOT`
     Arguments and flags that specify the Filestore snapshot you want to create. 
REQUIRED FLAGS
    

`--file-share`=`FILE_SHARE`
     File share name on the Filestore instance to snapshot. 
`--instance`=`INSTANCE`
     Share name of the Filestore instance you want to snapshot. 
`--instance-zone`=`INSTANCE_ZONE`
     Zone of the Filestore instance. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 
`--region`=`REGION`
     Region (e.g. us-central1) for the regional snapshot. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `file/v1p1alpha1` API. The full documentation for this API can be found at: <https://cloud.google.com/filestore/>
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
