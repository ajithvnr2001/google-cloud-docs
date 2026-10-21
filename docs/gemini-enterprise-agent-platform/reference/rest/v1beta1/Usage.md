---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage/
title: Usage \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:32:10.143485+00:00
---

# Usage  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Usage Stay organized with collections  Save and categorize content based on your preferences. 

Statistics on the interaction request's token usage.

Fields  
  
`totalInputTokens` `integer` Number of tokens in the prompt (context). | `inputTokensByModality[]` `object (`[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens)`)` A breakdown of input token usage by modality. | `totalCachedTokens` `integer` Number of tokens in the cached part of the prompt (the cached content). | `cachedTokensByModality[]` `object (`[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens)`)` A breakdown of cached token usage by modality. | `totalOutputTokens` `integer` Total number of tokens across all the generated responses. | `outputTokensByModality[]` `object (`[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens)`)` A breakdown of output token usage by modality. | `totalToolUseTokens` `integer` Number of tokens present in tool-use prompt(s). | `toolUseTokensByModality[]` `object (`[ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens)`)` A breakdown of tool-use token usage by modality. | `totalThoughtTokens` `integer` Number of tokens of thoughts for thinking models. | `totalTokens` `integer` Total token count for the interaction request (prompt + responses + other internal tokens). | `groundingToolCount[]` `object (`[GroundingToolCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#GroundingToolCount)`)` Grounding tool count. | JSON representation  
---  
      
    
    {
      "totalInputTokens": integer,
      "inputTokensByModality": [
        {
          object ([ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens))
        }
      ],
      "totalCachedTokens": integer,
      "cachedTokensByModality": [
        {
          object ([ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens))
        }
      ],
      "totalOutputTokens": integer,
      "outputTokensByModality": [
        {
          object ([ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens))
        }
      ],
      "totalToolUseTokens": integer,
      "toolUseTokensByModality": [
        {
          object ([ModalityTokens](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#ModalityTokens))
        }
      ],
      "totalThoughtTokens": integer,
      "totalTokens": integer,
      "groundingToolCount": [
        {
          object ([GroundingToolCount](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#GroundingToolCount))
        }
      ]
    }  
  
## ModalityTokens

The token count for a single response modality.

Fields  
  
`modality` `enum (`[ResponseModality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ResponseModality)`)` The modality associated with the token count. | `tokens` `integer` Number of tokens for the modality. | JSON representation  
---  
      
    
    {
      "modality": enum ([ResponseModality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ResponseModality)),
      "tokens": integer
    }  
  
## GroundingToolCount

The number of grounding tool counts.

Fields  
  
`type` `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#Type)`)` The grounding tool type associated with the count. | `count` `integer` The number of grounding tool counts. | JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Usage#Type)),
      "count": integer
    }  
  
## Type

The type of grounding tool.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`GOOGLE_SEARCH` | Grounding with Google Web Search and Image Search, & Web Grounding for Enterprise.  
`GOOGLE_MAPS` | Grounding with Google Maps.  
`RETRIEVAL` | Grounding with customer's data, for example, VertexAISearch.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-01 UTC."],[],[]] 
