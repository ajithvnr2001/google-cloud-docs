---
url: https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/
title: gcloud ai endpoints \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:44.674036+00:00
---

# gcloud ai endpoints  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud ai endpoints Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud ai endpoints - manage Vertex AI endpoints 
SYNOPSIS
    

`gcloud ai endpoints` `COMMAND` [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     An endpoint contains one or more deployed models, all of which must have the same interface but may come from different models. An endpoint is to obtain online prediction and explanation from one of its deployed models. 

When you communicate with Vertex AI services, you identify a specific endpoint that is deployed in the cloud using a combination of the current project, the region, and the endpoint. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

COMMANDS
     ``COMMAND`` is one of the following: 

`[create](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/create)`
     Create a new Vertex AI endpoint. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/delete)`
     Delete an existing Vertex AI endpoint. 
`[deploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/deploy-model)`
     Deploy a model to an existing Vertex AI endpoint. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/describe)`
     Describe an existing Vertex AI endpoint. 
`[direct-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-predict)`
     Run Vertex AI online direct prediction. 
`[direct-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/direct-raw-predict)`
     Run Vertex AI online direct raw prediction. 
`[explain](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/explain)`
     Request an online explanation from an Vertex AI endpoint. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/list)`
     List existing Vertex AI endpoints. 
`[predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/predict)`
     Run Vertex AI online prediction. 
`[raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/raw-predict)`
     Run Vertex AI online raw prediction. 
`[stream-direct-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-direct-predict)`
     Run Vertex AI online stream direct prediction. 
`[stream-direct-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-direct-raw-predict)`
     Run Vertex AI online stream direct raw prediction. 
`[stream-raw-predict](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/stream-raw-predict)`
     Run Vertex AI online stream raw prediction. 
`[undeploy-model](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/undeploy-model)`
     Undeploy a model from an existing Vertex AI endpoint. 
`[update](https://docs.cloud.google.com/sdk/gcloud/reference/ai/endpoints/update)`
     Update an existing Vertex AI endpoint. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha ai endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints)
    
    
    [gcloud beta ai endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/beta/ai/endpoints)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
