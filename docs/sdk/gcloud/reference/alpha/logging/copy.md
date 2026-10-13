---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/copy/
title: gcloud alpha logging copy \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:29.730257+00:00
---

# gcloud alpha logging copy  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/logging/copy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha logging copy Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha logging copy - copy log entries 
SYNOPSIS
    

`gcloud alpha logging copy` `BUCKET_ID` `DESTINATION` `--location`=`LOCATION` [`--log-filter`=`LOG_FILTER`] [`--billing-account`=`BILLING_ACCOUNT_ID` | `--folder`=`FOLDER_ID` | `--organization`=`ORGANIZATION_ID` | `--project`=`PROJECT_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha logging copy starts the process to copy log entries from a log bucket to a destination. 
EXAMPLES
     To start a copy log entries operation, run: 
    
    
    gcloud alpha logging copy BUCKET_ID DESTINATION --location=LOCATION

To copy log entries in a specific time window, run: 
    
    
    gcloud alpha logging copy BUCKET_ID DESTINATION --location=LOCATION --log-filter='timestamp<="2021-05-31T23:59:59Z" AND
     timestamp>="2021-05-31T00:00:00Z"'

POSITIONAL ARGUMENTS
    

`BUCKET_ID`
     Id of the log bucket to copy logs from. Example: my-bucket 
`DESTINATION`
     Destination to copy logs to. Example: Cloud Storage bucket: storage.googleapis.com/my-cloud-storage-bucket 
REQUIRED FLAGS
    

`--location`=`LOCATION`
     Location of the log bucket. 
OPTIONAL FLAGS
    

`--log-filter`=`LOG_FILTER`
     A filter specifying which log entries to copy. The filter must be no more than 20k characters. An empty filter matches all log entries. 
At most one of these can be specified: 

`--billing-account`=`BILLING_ACCOUNT_ID`
     Billing account of the log entries to copy. 
`--folder`=`FOLDER_ID`
     Folder of the log entries to copy. 
`--organization`=`ORGANIZATION_ID`
     Organization of the log entries to copy. 
`--project`=`PROJECT_ID`
     Project of the log entries to copy. 

The Google Cloud project ID to use for this invocation. If omitted, then the current project is assumed; the current project can be listed using `gcloud config list --format='text(core.project)'` and can be set using `gcloud config set project PROJECTID`. 

`--project` and its fallback `core/project` property play two roles in the invocation: they specify both the project of the resource to operate on, and the project for API enablement checks, quota, and billing. To specify a different project for quota and billing, use the `--billing-project` flag or the `billing/quota_project` property. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud logging copy](https://docs.cloud.google.com/sdk/gcloud/reference/logging/copy)
    
    
    [gcloud beta logging copy](https://docs.cloud.google.com/sdk/gcloud/reference/beta/logging/copy)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-15 UTC."],[],[]] 
