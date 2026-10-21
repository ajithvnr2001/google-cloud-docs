---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/jobs/list/
title: gcloud beta dataflow jobs list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:18.058046+00:00
---

# gcloud beta dataflow jobs list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/jobs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta dataflow jobs list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta dataflow jobs list - lists all jobs in a particular project, optionally filtered by region 
SYNOPSIS
    

`gcloud beta dataflow jobs list` [`--created-after`=`CREATED_AFTER`] [`--created-before`=`CREATED_BEFORE`] [`--region`=`REGION`] [`--status`=`STATUS`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`; default=100] [`--page-size`=`PAGE_SIZE`; default=20] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` By default, 100 jobs in the current project are listed; this can be overridden with the gcloud --project flag, and the --limit flag. 

Using the --region flag will only list jobs from the given regional endpoint. 

EXAMPLES
     Filter jobs with the given name: 
    
    
    gcloud beta dataflow jobs list --filter="name=my-wordcount"

List jobs with from a given region: 
    
    
    gcloud beta dataflow jobs list --region="europe-west1"

List jobs created this year: 
    
    
    gcloud beta dataflow jobs list --created-after=2018-01-01

List jobs created more than a week ago: 
    
    
    gcloud beta dataflow jobs list --created-before=-P1W

FLAGS
    

`--created-after`=`CREATED_AFTER`
     Filter the jobs to those created after the given time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. For example, `2018-01-01` is the first day of the year, and `-P2W` is 2 weeks ago. 
`--created-before`=`CREATED_BEFORE`
     Filter the jobs to those created before the given time. See $ [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on time formats. 
`--region`=`REGION`
     Only resources from the given region are queried. If not provided, an attempt will be made to query from all available regions. In the event of an outage, jobs from certain regions may not be available. 
`--status`=`STATUS`
     Filter the jobs to those with the selected status. `STATUS` must be one of: 

`active`
     Filters the jobs that are running ordered on the creation timestamp. 
`all`
     Returns running jobs first, ordered on creation timestamp, then, returns all terminated jobs ordered on the termination timestamp. 
`terminated`
     Filters the jobs that have a terminated state, ordered on the termination timestamp. Example terminated states: Done, Updated, Cancelled, etc. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`; default=100
     Maximum number of resources to list. The default is `100`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`; default=20
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is `20`. Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud dataflow jobs list](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
