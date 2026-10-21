---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list/
title: gcloud beta ai model-garden models list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:17.922677+00:00
---

# gcloud beta ai model-garden models list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai model-garden models list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai model-garden models list - list the publisher models in Model Garden 
SYNOPSIS
    

`gcloud beta ai model-garden models list` [`--can-deploy-hugging-face-models`] [`--full-resource-name`] [`--model-filter`=`MODEL_FILTER`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`; default=1000] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` This command lists either all models in Model Garden or all Hugging Face models supported by Model Garden. 
EXAMPLES
     To list all models in Model Garden, run: 
    
    
    [gcloud ai model-garden models list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list)

To list Hugging Face models that can be deployed in Model Garden, run: 
    
    
    [gcloud ai model-garden models list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list) --can-deploy-hugging-face-models

To list models with `gemma` in their names, run: 
    
    
    [gcloud ai model-garden models list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list) --model-filter=gemma

Note: Since the number of Hugging Face models is large, the default limit is set to 500 with a page size of 100 when listing supported Hugging Face models. To override the limit or page size, specify the --limit or --page-size flags, respectively. To list all models in Model Garden, use `--limit=unlimited`. 

FLAGS
    

`--can-deploy-hugging-face-models`
     Whether to only list Hugging Face models that can be deployed. 
`--full-resource-name`
     Whether to return the full resource name of the model. 
`--model-filter`=`MODEL_FILTER`
     Filter to apply to the model names or the display names of the list of models. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--limit`=`LIMIT`; default=1000
     Maximum number of resources to list. The default is `1000`. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--page-size`=`PAGE_SIZE`
     Some services group resource list output into pages. This flag specifies the maximum number of resources per page. The default is determined by the service if it supports paging, otherwise it is `unlimited` (no paging). Paging may be applied before or after `--filter` and `--limit` depending on the service. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai model-garden models list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list)
    
    
    [gcloud alpha ai model-garden models list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
