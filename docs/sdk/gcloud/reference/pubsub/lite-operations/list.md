---
url: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list/
title: gcloud pubsub lite-operations list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:25:57.755896+00:00
---

# gcloud pubsub lite-operations list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud pubsub lite-operations list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud pubsub lite-operations list - list Pub/Sub Lite operations 
SYNOPSIS
    

`gcloud pubsub lite-operations list` `--location`=`LOCATION` [`--done`=`DONE`] [`--subscription`=`SUBSCRIPTION`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     List Pub/Sub Lite operations. 

The optional `--subscription` flag can be used to filter operations for a Pub/Sub Lite subscription. The optional `--done` flag can be used to filter by operation completion status. These flags are ignored if `--filter` is set. 

To describe a listed operation, run: 
    
    
    gcloud pubsub lite-operations list operation-id --location=us-central1-a

EXAMPLES
     To list Pub/Sub Lite operations, run: 
    
    
    gcloud pubsub lite-operations list --location=us-central1-a --limit=50

To list incomplete Pub/Sub Lite operations, run: 
    
    
    gcloud pubsub lite-operations list --location=us-central1-a --done=false

To list Pub/Sub Lite operations for a subscription, run: 
    
    
    gcloud pubsub lite-operations list --location=us-central1-a --subscription=my-subscription --limit=50

To list incomplete Pub/Sub Lite operations for a subscription, run: 
    
    
    gcloud pubsub lite-operations list --location=us-central1-a --subscription=my-subscription --done=false

REQUIRED FLAGS
    

Location resource - Location to list operations for. This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--location` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`--location`=`LOCATION`
     ID of the location or fully qualified identifier for the location. 

To set the `location` attribute: 

  * provide the argument `--location` on the command line. 


FLAGS
    

`--done`=`DONE`
     Filter operations by completion status. This flag is ignored if `--filter` is set. `DONE` must be one of: `false`, `true`. 
`--subscription`=`SUBSCRIPTION`
     Filter operations by target subscription. This flag is ignored if `--filter` is set. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`
     Maximum number of resources to list. The default is `unlimited`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `pubsublite/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/pubsub/lite/docs>
NOTES
     These variants are also available: 
    
    
    [gcloud alpha pubsub lite-operations list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/pubsub/lite-operations/list)
    
    
    [gcloud beta pubsub lite-operations list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/pubsub/lite-operations/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
