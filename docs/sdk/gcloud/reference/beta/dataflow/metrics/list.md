---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/metrics/list/
title: gcloud beta dataflow metrics list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:19:06.600516+00:00
---

# gcloud beta dataflow metrics list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/metrics/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataflow metrics list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataflow metrics list - retrieves the metrics from a specific job 
SYNOPSIS
    

`gcloud beta dataflow metrics list` `JOB_ID` [`--changed-after`=`CHANGED_AFTER`] [`--hide-committed`] [`--region`=`REGION_ID`] [`--source`=`SOURCE`; default="all"] [`--tentative`] [`--transform`=`TRANSFORM`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command can be used to explore the job's metrics at a fine-grained level. 
EXAMPLES
     Filter metrics with the given name: 
    
    
    gcloud beta dataflow metrics list JOB --filter="name=ElementCount"

Filter child metrics with matching transforms: 
    
    
    gcloud beta dataflow metrics list JOB --transform=WordCount

Filter child output metrics: 
    
    
    gcloud beta dataflow metrics list JOB --transform=WordCount/Write.*out

Filter all output metrics: 
    
    
    gcloud beta dataflow metrics list JOB --transform=.*out

Filter all custom-defined user metrics 
    
    
    gcloud beta dataflow metrics list JOB --source=user

Filter metrics with a scalar value greater than a threshold. 
    
    
    gcloud beta dataflow metrics list JOB --filter="scalar > 50"

List metrics that have changed in the last 2 weeks: 
    
    
    gcloud beta dataflow metrics list JOB --changed-after=-P2W

POSITIONAL ARGUMENTS
    

`JOB_ID`
     Job ID to operate on. 
FLAGS
    

`--changed-after`=`CHANGED_AFTER`
     Only display metrics that have changed after the given time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. For example, `2018-01-01` is the first day of the year, and `-P2W` is 2 weeks ago. 
`--hide-committed`
     If true, hide committed values. 
`--region`=`REGION_ID`
     Region ID of the job's regional endpoint. Defaults to 'us-central1'. 
`--source`=`SOURCE`; default="all"
     Set the metrics source. `SOURCE` must be one of: 

`all`
     Retrieves all metrics. 
`service`
     Retrieves only dataflow service metrics. 
`user`
     Retrieves only custom user metrics. 
`--tentative`
     If true, display tentative values. 
`--transform`=`TRANSFORM`
     Filters only the metrics that prefix match the given regex. 
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
    
    
    [gcloud alpha dataflow metrics list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/metrics/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
