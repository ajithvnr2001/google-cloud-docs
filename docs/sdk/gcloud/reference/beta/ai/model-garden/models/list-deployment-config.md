---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list-deployment-config/
title: gcloud beta ai model-garden models list-deployment-config \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:18.255839+00:00
---

# gcloud beta ai model-garden models list-deployment-config  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/model-garden/models/list-deployment-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai model-garden models list-deployment-config Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai model-garden models list-deployment-config - list the machine specifications supported by and verified for a model in Model Garden 
SYNOPSIS
    

`gcloud beta ai model-garden models list-deployment-config` `--model`=`MODEL` [`--hugging-face-access-token`=`HUGGING_FACE_ACCESS_TOKEN`] [`--filter`=`EXPRESSION`] [`--sort-by`=[`FIELD`,…]] [`GCLOUD_WIDE_FLAG …`]
EXAMPLES
     To list the supported machine specifications for `google/gemma2@gemma-2-9b`, run: 
    
    
    [gcloud ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list-deployment-config) --model=google/gemma2@gemma-2-9b

To list the supported machine specifications for a Hugging Face model `meta-llama/Meta-Llama-3-8B`, run: 
    
    
    [gcloud ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list-deployment-config) --model=meta-llama/Meta-Llama-3-8B

REQUIRED FLAGS
    

`--model`=`MODEL`
     The model to be deployed. If it is a Model Garden model, it should be in the format of `{publisher_name}/{model_name}@{model_version_name}, e.g. `google/gemma2@gemma-2-2b`. If it is a Hugging Face model, it should be in the convention of Hugging Face models, e.g. `meta-llama/Meta-Llama-3-8B`. `
FLAGS
    

`--hugging-face-access-token`=`HUGGING_FACE_ACCESS_TOKEN`
     The access token from Hugging Face needed to read the model artifacts of gated models in order to generate the deployment configs. It is only needed when the Hugging Face model to deploy is gated and not verified by Model Garden. You can use the `gcloud ai alpha/beta model-garden models list` command to find out which ones are verified by Model Garden. 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
`--sort-by`=[`FIELD`,…]
     Comma-separated list of resource field key names to sort by. The default order is ascending. Prefix a field with ``~´´ for descending order on that field. This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/ai/model-garden/models/list-deployment-config)
    
    
    [gcloud alpha ai model-garden models list-deployment-config](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/model-garden/models/list-deployment-config)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
