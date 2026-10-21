---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig/
title: RagEngineConfig \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:10:56.483569+00:00
---

# RagEngineConfig  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagEngineConfig Stay organized with collections  Save and categorize content based on your preferences. 

Config for RagEngine.

Fields  
  
`name` `string` Identifier. The name of the RagEngineConfig. Format: `projects/{project}/locations/{location}/ragEngineConfig` | `ragManagedDbConfig` `object (`[RagManagedDbConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#RagManagedDbConfig)`)` The config of the RagManagedDb used by RagEngine. | JSON representation  
---  
      
    
    {
      "name": string,
      "ragManagedDbConfig": {
        object ([RagManagedDbConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#RagManagedDbConfig))
      }
    }  
  
## RagManagedDbConfig

Configuration message for RagManagedDb used by RagEngine.

Fields  
  
`tier` `Union type`  
  
The tier of the RagManagedDb. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`enterprise  
**(deprecated)**` `object (`[Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Enterprise)`)` This item is deprecated!Sets the RagManagedDb to the Enterprise tier. | `scaled  
**(deprecated)**` `object (`[Scaled](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Scaled)`)` This item is deprecated!Deprecated: Use `mode` instead to set the tier under Spanner. Sets the RagManagedDb to the Scaled tier. | `basic  
**(deprecated)**` `object (`[Basic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Basic)`)` This item is deprecated!Deprecated: Use `mode` instead to set the tier under Spanner. Sets the RagManagedDb to the Basic tier. | `unprovisioned  
**(deprecated)**` `object (`[Unprovisioned](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Unprovisioned)`)` This item is deprecated!Deprecated: Use `mode` instead to set the tier under Spanner. Sets the RagManagedDb to the Unprovisioned tier. End of mutually exclusive fields. | `mode` `Union type`  
  
The choice of backend for your RagEngine. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`serverless` `object (`[Serverless](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Serverless)`)` Sets the backend to be the serverless mode offered by RAG Engine. | `spanner` `object (`[Spanner](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Spanner)`)` Sets the RAG Engine backend to be RagManagedDb, built on top of Spanner.NOTE: This is the default mode (w/ Basic Tier) if not explicitly chosen. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // tier
      "enterprise": {
        object ([Enterprise](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Enterprise))
      },
      "scaled": {
        object ([Scaled](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Scaled))
      },
      "basic": {
        object ([Basic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Basic))
      },
      "unprovisioned": {
        object ([Unprovisioned](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Unprovisioned))
      }
      // Union type
    
      // mode
      "serverless": {
        object ([Serverless](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Serverless))
      },
      "spanner": {
        object ([Spanner](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Spanner))
      }
      // Union type
    }  
  
## Enterprise

This type has no fields.

This item is deprecated!

Enterprise tier offers production grade performance along with autoscaling functionality. It is suitable for customers with large amounts of data or performance sensitive workloads.

## Scaled

This type has no fields.

Scaled tier offers production grade performance along with autoscaling functionality. It is suitable for customers with large amounts of data or performance sensitive workloads.

## Basic

This type has no fields.

Basic tier is a cost-effective and low compute tier suitable for the following cases: * Experimenting with RagManagedDb. * Small data size. * Latency insensitive workload. * Only using RAG Engine with external vector DBs.

NOTE: This is the default tier under Spanner mode if not explicitly chosen.

## Unprovisioned

This type has no fields.

Disables the RAG Engine service and deletes all your data held within this service. This will halt the billing of the service.

NOTE: Once deleted the data cannot be recovered. To start using RAG Engine again, you will need to update the tier by calling the UpdateRagEngineConfig API.

## Serverless

This type has no fields.

message to configure the serverless mode offered by RAG Engine.

## Spanner

message to configure the Spanner database used by RagManagedDb.

Fields  
  
`tier` `Union type`  
  
The tier of the RagManagedDb, built on top of Spanner. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`scaled` `object (`[Scaled](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Scaled)`)` Sets the RagManagedDb to the Scaled tier. | `basic` `object (`[Basic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Basic)`)` Sets the RagManagedDb to the Basic tier. This is the default tier for Spanner mode if not explicitly chosen. | `unprovisioned` `object (`[Unprovisioned](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Unprovisioned)`)` Sets the RagManagedDb to the Unprovisioned tier. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // tier
      "scaled": {
        object ([Scaled](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Scaled))
      },
      "basic": {
        object ([Basic](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Basic))
      },
      "unprovisioned": {
        object ([Unprovisioned](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagEngineConfig#Unprovisioned))
      }
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
