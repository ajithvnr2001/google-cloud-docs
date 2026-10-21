---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage/
title: Method: tensorboards.readUsage \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:44:14.124642+00:00
---

# Method: tensorboards.readUsage  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: tensorboards.readUsage Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.tensorboards.readUsage

Returns a list of monthly active users for a given TensorBoard instance.

### Endpoint

get  `https://{service-endpoint}/v1/{tensorboard}:readUsage`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`tensorboard` `string` Required. The name of the Tensorboard resource. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

### Request body

The request body must be empty.

### Response body

Response message for `[TensorboardService.ReadTensorboardUsage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage#google.cloud.aiplatform.v1.TensorboardService.ReadTensorboardUsage)`. If successful, the response body contains data with the following structure: | Fields  
  
`monthlyUsageData` `map (key: string, value: object (`[PerMonthUsageData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage#PerMonthUsageData)`))` Maps year-month (YYYYMM) string to per month usage data. | JSON representation  
---  
      
    
    {
      "monthlyUsageData": {
        string: {
          object ([PerMonthUsageData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage#PerMonthUsageData))
        },
        ...
      }
    }  
  
## PerMonthUsageData

Per month usage data

Fields  
  
`userUsageData[]` `object (`[PerUserUsageData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage#PerUserUsageData)`)` Usage data for each user in the given month. | JSON representation  
---  
      
    
    {
      "userUsageData": [
        {
          object ([PerUserUsageData](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.tensorboards/readUsage#PerUserUsageData))
        }
      ]
    }  
  
## PerUserUsageData

Per user usage data.

Fields  
  
`username` `string` user's username | `viewCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of times the user has read data within the Tensorboard. | JSON representation  
---  
      
    
    {
      "username": string,
      "viewCount": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
