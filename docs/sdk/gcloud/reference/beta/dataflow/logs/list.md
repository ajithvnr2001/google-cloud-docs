---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/logs/list/
title: gcloud beta dataflow logs list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:18.689592+00:00
---

# gcloud beta dataflow logs list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/logs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataflow logs list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataflow logs list - retrieve the job logs for a specific job 
SYNOPSIS
    

`gcloud beta dataflow logs list` `JOB_ID` [`--after`=`AFTER`] [`--before`=`BEFORE`] [`--importance`=`IMPORTANCE`; default="warning"] [`--region`=`REGION_ID`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Retrieves the job logs from a specified job using the Dataflow Messages API with at least the specified importance level. Can also be used to display logs between a given time period using the --before and --after flags. These logs are produced by the service and are distinct from worker logs. Worker logs can be found in Cloud Logging. 
EXAMPLES
     Retrieve only error logs: 
    
    
    gcloud beta dataflow logs list --importance=error

Retrieve all logs after some date: 
    
    
    gcloud beta dataflow logs list --after="2016-08-12 00:00:00"

Retrieve logs from this year: 
    
    
    gcloud beta dataflow logs list --after=2018-01-01

Retrieve logs more than a week old: 
    
    
    gcloud beta dataflow logs list --before=-P1W

POSITIONAL ARGUMENTS
    

`JOB_ID`
     Job ID to operate on. 
FLAGS
    

`--after`=`AFTER`
     Only display messages logged after the given time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. For example, `2018-01-01` is the first day of the year, and `-P2W` is 2 weeks ago. 
`--before`=`BEFORE`
     Only display messages logged before the given time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--importance`=`IMPORTANCE`; default="warning"
     Minimum importance a message must have to be displayed. `IMPORTANCE` must be one of: `debug`, `detailed`, `warning`, `error`. 
`--region`=`REGION_ID`
     Region ID of the job's regional endpoint. Defaults to 'us-central1'. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha dataflow logs list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/logs/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
