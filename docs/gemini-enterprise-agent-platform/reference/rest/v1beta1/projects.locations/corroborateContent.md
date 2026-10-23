---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/corroborateContent/
title: Method: locations.corroborateContent \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:06.325679+00:00
---

# Method: locations.corroborateContent  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/corroborateContent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: locations.corroborateContent Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.corroborateContent

Given an input text, it returns a score that evaluates the factuality of the text. It also extracts and returns claims from the text and provides supporting facts.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}:corroborateContent`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to corroborate text. The users must have permission to make a call in the project. Format: `projects/{project}/locations/{location}`.

### Request body

The request body contains data with the following structure: | Fields  
  
`facts[]` `object (`[Fact](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Fact)`)` Optional. Facts used to generate the text can also be used to corroborate the text. | `parameters` `object (`[Parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/corroborateContent#Parameters)`)` Optional. Parameters that can be set to override default settings per request. | `content` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Optional. Input content to corroborate, only text format is supported for now.

### Response body

Response message for locations.corroborateContent. If successful, the response body contains data with the following structure: | Fields  
  
`claims[]` `object (`[Claim](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/corroborateContent#Claim)`)` Claims that are extracted from the input content and facts that support the claims. | `corroborationScore` `number` confidence score of corroborating content. value is [0,1] with 1 is the most confidence. | JSON representation  
---  
      
    
    {
      "claims": [
        {
          object ([Claim](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations/corroborateContent#Claim))
        }
      ],
      "corroborationScore": number
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.ragCorpora.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Parameters

Parameters that can be overrided per request.

Fields  
  
`citationThreshold` `number` Optional. Only return claims with citation score larger than the threshold. | JSON representation  
---  
      
    
    {
      "citationThreshold": number
    }  
  
## Claim

Claim that is extracted from the input text and facts that support it.

Fields  
  
`factIndexes[]` `integer` Indexes of the facts supporting this claim. | `startIndex` `integer` Index in the input text where the claim starts (inclusive). | `endIndex` `integer` Index in the input text where the claim ends (exclusive). | `score` `number` confidence score of this corroboration. | JSON representation  
---  
      
    
    {
      "factIndexes": [
        integer
      ],
      "startIndex": integer,
      "endIndex": integer,
      "score": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
