---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ComputeTokensResponse/
title: ComputeTokensResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:13:59.098452+00:00
---

# ComputeTokensResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ComputeTokensResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ComputeTokensResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for ComputeTokens RPC call.

Fields  
  
`tokensInfo[]` `object (`[TokensInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ComputeTokensResponse#TokensInfo)`)` Lists of tokens info from the input. A ComputeTokensRequest could have multiple instances with a prompt in each instance. We also need to return lists of tokens info for the request with multiple instances. | JSON representation  
---  
      
    
    {
      "tokensInfo": [
        {
          object ([TokensInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ComputeTokensResponse#TokensInfo))
        }
      ]
    }  
  
## TokensInfo

Tokens info with a list of tokens and the corresponding list of token ids.

Fields  
  
`tokens[]` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A list of tokens from the input.A base64-encoded string. | `tokenIds[]` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A list of token ids from the input. | `role` `string` Optional. Optional fields for the role from the corresponding Content. | JSON representation  
---  
      
    
    {
      "tokens": [
        string
      ],
      "tokenIds": [
        string
      ],
      "role": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
