---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings/
title: LlmModelSettings \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:46.803517+00:00
---

# LlmModelSettings  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  LlmModelSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Parameters
    * JSON representation
  * InputTokenLimit
  * OutputTokenLimit



Settings for LLM models.

JSON representation  
---  
      
    
    {
      "model": string,
      "promptText": string,
      "parameters": {
        object ([Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#Parameters))
      }
    }  
  
Fields  
---  
`model` |  `string` The selected LLM model.  
`promptText` |  `string` The custom prompt to use.  
`parameters` |  `object (`[Parameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#Parameters)`)` Generative model parameters.  
  
## Parameters

Generative model parameters to control the model behavior.

JSON representation  
---  
      
    
    {
      "temperature": number,
      "inputTokenLimit": enum ([InputTokenLimit](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#InputTokenLimit)),
      "outputTokenLimit": enum ([OutputTokenLimit](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#OutputTokenLimit))
    }  
  
Fields  
---  
`temperature` |  `number` The temperature used for sampling during response generation. Value ranges from 0 to 1. Temperature controls the degree of randomness in token selection. Lower temperature means less randomness, while higher temperature means more randomness. Valid range: [0.0, 1.0]  
`inputTokenLimit` |  `enum (`[InputTokenLimit](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#InputTokenLimit)`)` The input token limit. This setting is currently only supported by playbooks.  
`outputTokenLimit` |  `enum (`[OutputTokenLimit](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3beta1/LlmModelSettings#OutputTokenLimit)`)` The output token limit. This setting is currently only supported by playbooks. Only one of outputTokenLimit and max_output_tokens is allowed to be set.  
  
## InputTokenLimit

The input token limits for 1 LLM call. For the limit of each model, see <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models> for more information.

Enums  
---  
`INPUT_TOKEN_LIMIT_UNSPECIFIED` | Limit not specified. Treated as 'INPUT_TOKEN_LIMIT_SHORT'.  
`INPUT_TOKEN_LIMIT_SHORT` | Input token limit up to 8k.  
`INPUT_TOKEN_LIMIT_MEDIUM` | Input token limit up to 32k.  
`INPUT_TOKEN_LIMIT_LONG` | Input token limit up to 100k.  
  
## OutputTokenLimit

The output token limits for 1 LLM call. The limits are subject to change. For the limit of each model, see <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models> for more information.

Enums  
---  
`OUTPUT_TOKEN_LIMIT_UNSPECIFIED` | Limit not specified.  
`OUTPUT_TOKEN_LIMIT_SHORT` | Input token limit up to 512 tokens.  
`OUTPUT_TOKEN_LIMIT_MEDIUM` | Input token limit up to 1k.  
`OUTPUT_TOKEN_LIMIT_LONG` | Input token limit up to 2k.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
