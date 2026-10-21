---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModalityTokenCount/
title: ModalityTokenCount \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:01:09.972784+00:00
---

# ModalityTokenCount  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModalityTokenCount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ModalityTokenCount Stay organized with collections  Save and categorize content based on your preferences. 

Represents a breakdown of token usage by modality.

This message is used in [CountTokensResponse][google.cloud.aiplatform.master.CountTokensResponse] and `[GenerateContentResponse.UsageMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse#UsageMetadata)` to provide a detailed view of how many tokens are used by each modality (e.g., text, image, video) in a request. This is particularly useful for multimodal models, allowing you to track and manage token consumption for billing and quota purposes.

Fields  
  
`modality` `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModalityTokenCount#Modality)`)` The modality that this token count applies to. | `tokenCount` `integer` The number of tokens counted for this modality. | JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModalityTokenCount#Modality)),
      "tokenCount": integer
    }  
  
## Modality

The modality of a `Part` of a `Content` message. A modality is the type of media, such as an image or a video. It is used to categorize the content of a `Part` for token counting purposes.

Enums  
---  
`MODALITY_UNSPECIFIED` | When a modality is not specified, it is treated as `TEXT`.  
`TEXT` | The `Part` contains plain text.  
`IMAGE` | The `Part` contains an image.  
`VIDEO` | The `Part` contains a video.  
`AUDIO` | The `Part` contains audio.  
`DOCUMENT` | The `Part` contains a document, such as a PDF.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
