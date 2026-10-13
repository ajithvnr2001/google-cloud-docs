---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/list/
title: gcloud container ai profiles list \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:22.485055+00:00
---

# gcloud container ai profiles list  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container ai profiles list Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container ai profiles list - list compatible accelerator profiles 
SYNOPSIS
    

`gcloud container ai profiles list` [`--format`=`FORMAT`] [`--model`=`MODEL`] [`--model-server`=`MODEL_SERVER`] [`--model-server-version`=`MODEL_SERVER_VERSION`] [`--pricing-model`=`PRICING_MODEL`] [`--serving-stack`=`SERVING_STACK`] [`--serving-stack-version`=`SERVING_STACK_VERSION`] [`--target-cost-per-million-input-tokens`=`TARGET_COST_PER_MILLION_INPUT_TOKENS`] [`--target-cost-per-million-output-tokens`=`TARGET_COST_PER_MILLION_OUTPUT_TOKENS`] [`--target-input-length`=`TARGET_INPUT_LENGTH`] [`--target-itl-milliseconds`=`TARGET_ITL_MILLISECONDS`] [`--target-ntpot-milliseconds`=`TARGET_NTPOT_MILLISECONDS`] [`--target-output-length`=`TARGET_OUTPUT_LENGTH`] [`--target-ttft-milliseconds`=`TARGET_TTFT_MILLISECONDS`] [`--use-case`=`USE_CASE`] [`--filter`=`EXPRESSION`] [`--limit`=`LIMIT`] [`--page-size`=`PAGE_SIZE`] [`--sort-by`=[`FIELD`,…]] [`--uri`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command lists all supported accelerators with their performance details. By default, the supported accelerators are displayed in a table format with select information for each accelerator. To see all details, use --format=yaml or \--format=csvprofile. 

To get supported model, model servers, and model server versions, run `gcloud container ai profiles models list`, `gcloud container ai profiles model-servers list`, and `gcloud container ai profiles model-server-versions list`. 

FLAGS
    

`--format`=`FORMAT`
     The output format. Default is profile, which displays the profile information in a table format, including cost conversions. csvprofile displays the profile information in a CSV format.Options include csvprofile, profile, and yaml. 
`--model`=`MODEL`
     The model. 
`--model-server`=`MODEL_SERVER`
     The model server. 
`--model-server-version`=`MODEL_SERVER_VERSION`
     The model server version. If omitted, the most recently benchmarked version is used. Other options include the model server version of a profile, or 'all' to return all versions. 
`--pricing-model`=`PRICING_MODEL`
     The pricing model to use to calculate token cost. Currently, this supports on-demand, spot, 3-years-cud, 1-year-cud 
`--serving-stack`=`SERVING_STACK`
     The serving stack to filter profiles by. If not provided, profiles for all serving stacks that support the given model and model server will be returned. 
`--serving-stack-version`=`SERVING_STACK_VERSION`
     The serving stack version. If omitted, the most recently benchmarked version is used. Other options include the serving stack version of a profile, or 'all' to return all versions. 
`--target-cost-per-million-input-tokens`=`TARGET_COST_PER_MILLION_INPUT_TOKENS`
     The target cost per million input tokens to filter profiles by, unit is 1 USD up to 5 decimal places. 
`--target-cost-per-million-output-tokens`=`TARGET_COST_PER_MILLION_OUTPUT_TOKENS`
     The target cost per million output tokens to filter profiles by, unit is 1 USD up to 5 decimal places. 
`--target-input-length`=`TARGET_INPUT_LENGTH`
     If specified, results will only show profiles that have an input length within 20% of the specified one. Only works alongside output length. 
`--target-itl-milliseconds`=`TARGET_ITL_MILLISECONDS`
     If specified, results will only show profiles with instance types that can meet the latency target and will show their throughput performances at the target inter-token latency (ITL). 
`--target-ntpot-milliseconds`=`TARGET_NTPOT_MILLISECONDS`
     The target normalized time per output token (NTPOT) in milliseconds. NTPOT is measured as the request_latency / output_tokens. If this field is set, the command will only return accelerators that can meet the target ntpot milliseconds and display their throughput performance at the target latency. Otherwise, the command will return all accelerators and display their highest throughput performance. 
`--target-output-length`=`TARGET_OUTPUT_LENGTH`
     If specified, results will only show profiles that have an output length within 20% of the specified one. Only works alongside input length. 
`--target-ttft-milliseconds`=`TARGET_TTFT_MILLISECONDS`
     The target time to first token (TTFT) in milliseconds. TTFT is measured as the request_latency / output_tokens. If this field is set, the command will only return profiles that can meet the target ttft milliseconds and display their throughput performance at the target latency. Otherwise, the command will return all profiles and display their highest throughput performance. 
`--use-case`=`USE_CASE`
     If specified, results will only show profiles that match the provided use case. Options are: Advanced Customer Support, Code Completion, Text Summarization, Chatbot (ShareGPT), Text Generation, Deep Research 
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
