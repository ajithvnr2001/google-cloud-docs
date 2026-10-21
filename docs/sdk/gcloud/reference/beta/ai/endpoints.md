---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/
title: gcloud beta ai endpoints \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:12.794488+00:00
---

# gcloud beta ai endpoints  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta ai endpoints Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta ai endpoints - manage Vertex AI endpoints 
SYNOPSIS
    

`gcloud beta ai endpoints` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` An endpoint contains one or more deployed models, all of which must have the same interface but may come from different models. An endpoint is to obtain online prediction and explanation from one of its deployed models. 

When you communicate with Vertex AI services, you identify a specific endpoint that is deployed in the cloud using a combination of the current project, the region, and the endpoint. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/create)`
     `(BETA)` Create a new Vertex AI endpoint. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/delete)`
     `(BETA)` Delete an existing Vertex AI endpoint. 
`[deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/deploy-model)`
     `(BETA)` Deploy a model to an existing Vertex AI endpoint. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/describe)`
     `(BETA)` Describe an existing Vertex AI endpoint. 
`[direct-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/direct-predict)`
     `(BETA)` Run Vertex AI online direct prediction. 
`[direct-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/direct-raw-predict)`
     `(BETA)` Run Vertex AI online direct raw prediction. 
`[explain](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/explain)`
     `(BETA)` Request an online explanation from an Vertex AI endpoint. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/list)`
     `(BETA)` List existing Vertex AI endpoints. 
`[predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/predict)`
     `(BETA)` Run Vertex AI online prediction. 
`[raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/raw-predict)`
     `(BETA)` Run Vertex AI online raw prediction. 
`[stream-direct-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-direct-predict)`
     `(BETA)` Run Vertex AI online stream direct prediction. 
`[stream-direct-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-direct-raw-predict)`
     `(BETA)` Run Vertex AI online stream direct raw prediction. 
`[stream-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/stream-raw-predict)`
     `(BETA)` Run Vertex AI online stream raw prediction. 
`[undeploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/undeploy-model)`
     `(BETA)` Undeploy a model from an existing Vertex AI endpoint. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints/update)`
     `(BETA)` Update an existing Vertex AI endpoint. 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud ai endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints)
    
    
    [gcloud alpha ai endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
