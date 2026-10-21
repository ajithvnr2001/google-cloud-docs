---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/benchmarks/list/
title: gcloud container ai profiles benchmarks list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:55.287133+00:00
---

# gcloud container ai profiles benchmarks list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/benchmarks/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container ai profiles benchmarks list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container ai profiles benchmarks list - list benchmarks for a given model and model server 
SYNOPSIS
    

`gcloud container ai profiles benchmarks list` `--model`=`MODEL` `--model-server`=`MODEL_SERVER` [`--format`=`FORMAT`] [`--instance-type`=`INSTANCE_TYPE`] [`--model-server-version`=`MODEL_SERVER_VERSION`] [`--pricing-model`=`PRICING_MODEL`] [`--serving-stack`=`SERVING_STACK`] [`--serving-stack-version`=`SERVING_STACK_VERSION`] [`--use-case`=`USE_CASE`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command lists all benchmarking data for a given model and model server. By default, the benchmarks are displayed in a CSV format. 

For examples of visualizing the benchmarking data, see the accompanying Colab notebook: <https://colab.research.google.com/github/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/notebooks/giq_visualizations.ipynb>

REQUIRED FLAGS
    

`--model`=`MODEL`
     The model. 
`--model-server`=`MODEL_SERVER`
     The model server. 
FLAGS
    

`--format`=`FORMAT`
     The format to print the output in. Default is csvprofile, which displays the profile information in a CSV format, including cost conversions. 
`--instance-type`=`INSTANCE_TYPE`
     The instance type. If not specified, this defaults to any instance type. 
`--model-server-version`=`MODEL_SERVER_VERSION`
     The model server version. If omitted, the most recently benchmarked version is used. Other options include the model server version of a profile, or 'all' to return all versions. 
`--pricing-model`=`PRICING_MODEL`
     The pricing model to use to calculate token cost. Currently, this supports on-demand, spot, 3-years-cud, 1-year-cud. 
`--serving-stack`=`SERVING_STACK`
     The serving stack to filter benchmarking data by. If not provided, benchmarking data for all serving stacks that support the given model and model server will be returned. 
`--serving-stack-version`=`SERVING_STACK_VERSION`
     The serving stack version. If omitted, the most recently benchmarked version is used. Other options include the serving stack version of a profile, or 'all' to return all versions. 
`--use-case`=`USE_CASE`
     If specified, results will only show profiles that match the provided use case. Options are: Advanced Customer Support, Code Completion, Text Summarization, Chatbot (ShareGPT), Code Generation, Deep Research. If omitted, defaults to Chatbot (ShareGPT). 
LIST COMMAND FLAGS
    

`--filter`=`EXPRESSION`
     Apply a Boolean filter `EXPRESSION` to each resource item to be listed. If the expression evaluates `True`, then that item is listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters). This flag interacts with other flags that are applied in this order: `--flatten`, `--sort-by`, `--filter`, `--limit`. 
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
