---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/operations/list/
title: gcloud alpha transfer operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:50:59.324535+00:00
---

# gcloud alpha transfer operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha transfer operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha transfer operations list - list Transfer Service transfer operations 
SYNOPSIS
    

`gcloud alpha transfer operations list` [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`; default=256] [`--job-names`=[`JOB_NAMES`,…]] [`--operation-names`=[`OPERATION_NAMES`,…]] [`--operation-statuses`=[`OPERATION_STATUSES`,…]] [`--expand-table`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` List Transfer Service transfer operations to view their progress details at a glance. 
EXAMPLES
     To list all transfer operations in your current project, run: 
    
    
    gcloud alpha transfer operations list

To list all failed operations in your project, run: 
    
    
    gcloud alpha transfer operations list --operation-statuses=failed

To list operations 'foo' and 'bar', run: 
    
    
    gcloud alpha transfer operations list --operation-names=foo,bar

To list all operations in your current project as JSON, which provides all fields and formatting available in the API, run: 
    
    
    gcloud alpha transfer operations list --format=json

FLAGS
    

`--limit`=`LIMIT`
     Return the first items from the API up to this limit. 
`--page-size`=`PAGE_SIZE`; default=256
     Retrieve batches of this many items from the API. 
`--job-names`=[`JOB_NAMES`,…]
     The names of the jobs whose operations you want to list. Separate multiple job names with commas (e.g., --job-names=foo,bar). If not specified, operations for all jobs are listed. 
`--operation-names`=[`OPERATION_NAMES`,…]
     The names of operations you want to list. Separate multiple operation names with commas (e.g., --operation-names-name=foo,bar). If not specified, all operations are listed. 
`--operation-statuses`=[`OPERATION_STATUSES`,…]
     List only transfer operations with the statuses you specify. Options include 'in_progress', 'paused', 'success','failed', 'aborted'. Separate multiple statuses with commas (e.g., --operation-statuses=failed,aborted). 
`--expand-table`
     Include additional table columns (operation name, start time, status, data copied, status, has errors, job name) in command output. Tip: increase the size of your terminal before running the command. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud transfer operations list](https://docs.cloud.google.com/sdk/gcloud/reference/transfer/operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
