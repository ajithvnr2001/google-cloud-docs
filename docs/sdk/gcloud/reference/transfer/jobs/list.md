---
url: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/list/
title: gcloud transfer jobs list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:41:10.095574+00:00
---

# gcloud transfer jobs list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/transfer/jobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud transfer jobs list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud transfer jobs list - list Transfer Service transfer jobs 
SYNOPSIS
    

`gcloud transfer jobs list` [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`; default=256] [`--job-names`=[`JOB_NAMES`,…]] [`--job-statuses`=[`JOB_STATUSES`,…]] [`--expand-table`] [`--job-type`=`JOB_TYPE`; default="transfer"] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List Transfer Service transfer jobs in a given project to show their configurations and latest operations. 
EXAMPLES
     To list all jobs in your current project, run: 
    
    
    gcloud transfer jobs list

To list all disabled jobs in your project, run: 
    
    
    gcloud transfer jobs list --job-statuses=disabled

To list jobs 'foo' and 'bar', run: 
    
    
    gcloud transfer jobs list --job-names=foo,bar

To list all information about all jobs formatted as JSON, run: 
    
    
    gcloud transfer jobs list --format=json

To list all information about jobs 'foo' and 'bar' formatted as YAML, run: 
    
    
    gcloud transfer jobs list --job-names=foo,bar --format=YAML

FLAGS
    

`--limit`=`LIMIT`
     Return the first items from the API up to this limit. 
`--page-size`=`PAGE_SIZE`; default=256
     Retrieve batches of this many items from the API. 
`--job-names`=[`JOB_NAMES`,…]
     The names of the jobs you want to list. Separate multiple job names with commas (e.g., --job-names=foo,bar). If not specified, all jobs will be listed. 
`--job-statuses`=[`JOB_STATUSES`,…]
     List only jobs with the statuses you specify. Options include 'enabled', 'disabled', 'deleted' (case insensitive). Separate multiple statuses with commas (e.g., --job-statuses=enabled,deleted). If not specified, all jobs will be listed. 
`--expand-table`
     Include additional table columns (job name, source, destination, frequency, lastest operation name, job status) in command output. Tip: increase the size of your terminal before running the command. 
`--job-type`=`JOB_TYPE`; default="transfer"
     The type of the job you want to list. `JOB_TYPE` must be one of: `transfer`, `replication`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha transfer jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/transfer/jobs/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
