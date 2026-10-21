---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/endpoints/operations/list/
title: gcloud alpha endpoints operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:16:26.093031+00:00
---

# gcloud alpha endpoints operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/endpoints/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha endpoints operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha endpoints operations list - list operations for a project 
SYNOPSIS
    

`gcloud alpha endpoints operations list` [`--filter`=`EXPRESSION`] [`--service`=`SERVICE`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This command will list operations for a service, optionally matching a particular filter. 
EXAMPLES
     To list all operations for a service named `api.endpoints.proj.cloud.goog`, run: 
    
    
    gcloud alpha endpoints operations list --service=api.endpoints.proj.cloud.goog

To list only operations which are complete, add the `--filter` argument with a status filter: 
    
    
    gcloud alpha endpoints operations list --service=api.endpoints.proj.cloud.goog --filter='done = true'

To list only operations begun after a certain point in time, add the `--filter` argument with an ISO 8601 datetime startTime filter: 
    
    
    gcloud alpha endpoints operations list --service=api.endpoints.proj.cloud.goog --filter='startTime >= "2017-02-01"'

FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates as True then that item is listed. 

The available filter fields are startTime and done. Unrecognized fields will cause an error. 

startTime is an ISO 8601 datetime and supports >=, >, <=, and < operators. The datetime value must be wrapped in quotation marks. For example: 
    
    
    --filter='startTime < "2017-03-20T16:02:32"'

done is a boolean value and supports = and != operators. 

`--service`=`SERVICE`
     The name of the service for which to list operations. 
LIST COMMAND FLAGS
    

`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--uri`
     Print a list of resource URIs instead of the default output, and change the command output to a list of URIs. If this flag is used with `--format`, the formatting is applied on this URI list. To display URIs alongside other keys instead, use the `uri()` transform. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud endpoints operations list](https://docs.cloud.google.com/sdk/gcloud/reference/endpoints/operations/list)
    
    
    [gcloud beta endpoints operations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/endpoints/operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
