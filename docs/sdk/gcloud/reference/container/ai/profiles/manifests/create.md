---
url: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/manifests/create/
title: gcloud container ai profiles manifests create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:22.756549+00:00
---

# gcloud container ai profiles manifests create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/container/ai/profiles/manifests/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud container ai profiles manifests create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud container ai profiles manifests create - generate ready-to-deploy Kubernetes manifests with compute, load balancing, and autoscaling capabilities 
SYNOPSIS
    

`gcloud container ai profiles manifests create` `--accelerator-type`=`ACCELERATOR_TYPE` `--model`=`MODEL` `--model-server`=`MODEL_SERVER` [`--model-bucket-uri`=`MODEL_BUCKET_URI`] [`--model-server-version`=`MODEL_SERVER_VERSION`] [`--namespace`=`NAMESPACE`] [`--output`=`OUTPUT`; default="all"] [`--output-path`=`OUTPUT_PATH`] [`--serving-stack`=`SERVING_STACK`] [`--serving-stack-version`=`SERVING_STACK_VERSION`] [`--target-itl-milliseconds`=`TARGET_ITL_MILLISECONDS`] [`--target-ntpot-milliseconds`=`TARGET_NTPOT_MILLISECONDS`] [`--target-ttft-milliseconds`=`TARGET_TTFT_MILLISECONDS`] [`--use-case`=`USE_CASE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     To get supported model, model servers, and model server versions, run `gcloud alpha container ai profiles model-and-server-combinations list`. To get supported accelerators with their performance metrics, run `gcloud alpha container ai profiles accelerators list`. 
REQUIRED FLAGS
    

`--accelerator-type`=`ACCELERATOR_TYPE`
     The accelerator type. 
`--model`=`MODEL`
     The model. 
`--model-server`=`MODEL_SERVER`
     The model server. 
OPTIONAL FLAGS
    

`--model-bucket-uri`=`MODEL_BUCKET_URI`
     The Google Cloud Storage bucket URI to load the model from. This URI must point to the directory containing the model's config file (config.json) and model weights. If unspecified, defaults to loading the model from Hugging Face. 
`--model-server-version`=`MODEL_SERVER_VERSION`
     The model server version. If omitted, the most recently benchmarked version is used. 
`--namespace`=`NAMESPACE`
     The namespace to deploy the manifests in. Default namespace is 'default'. 
`--output`=`OUTPUT`; default="all"
     The output to display. Default is all. `OUTPUT` must be one of: `manifest`, `comments`, `all`. 
`--output-path`=`OUTPUT_PATH`
     The path to save the output to. If not specified, output to the terminal. 
`--serving-stack`=`SERVING_STACK`
     The serving stack to filter manifests by. If not provided, will default to none. 
`--serving-stack-version`=`SERVING_STACK_VERSION`
     The serving stack version. If omitted, the most recently benchmarked version is used. 
`--target-itl-milliseconds`=`TARGET_ITL_MILLISECONDS`
     The target inter-token latency (ITL) in milliseconds. If this is set, the manifest will include Horizontal Pod Autoscaler (HPA) resources which automatically adjust the model server replica count in response to changes in model server load to keep p50 ITL below the specified threshold. If the provided target-itl-milliseconds is too low to achieve, the HPA manifest will not be generated. 
`--target-ntpot-milliseconds`=`TARGET_NTPOT_MILLISECONDS`
     The maximum normalized time per output token (NTPOT) in milliseconds. NTPOT is measured as the request_latency / output_tokens. If this is set, the manifests will include Horizontal Pod Autoscaler (HPA) resources which automatically adjust the model server replica count in response to changes in model server load to keep p50 NTPOT below the specified threshold. If the provided target-ntpot-milliseconds is too low to achieve, the HPA manifest will not be generated. 
`--target-ttft-milliseconds`=`TARGET_TTFT_MILLISECONDS`
     If specified, results will only show accelerators that can meet the latency target and will show their throughput performances at the target ttft target to achieve, the HPA manifest will not be generated. 
`--use-case`=`USE_CASE`
     The manifest will be optimized for this use case. Options are: Advanced Customer Support, Code Completion, Text Summarization, Chatbot (ShareGPT), Code Generation, Deep Research. If omitted, defaults to Chatbot (ShareGPT). 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud alpha container ai profiles manifests create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/ai/profiles/manifests/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
