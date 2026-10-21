---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails
title: REST Resource: projects.locations.nasJobs.nasTrialDetails \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:08:26.017751+00:00
---

# REST Resource: projects.locations.nasJobs.nasTrialDetails  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.nasJobs.nasTrialDetails Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: NasTrialDetail

Represents a NasTrial details along with its parameters. If there is a corresponding train NasTrial, the train NasTrial is also returned.

Fields  
  
`name` `string` Output only. Resource name of the NasTrialDetail. | `parameters` `string` The parameters for the NasJob NasTrial. | `searchTrial` `object (`[NasTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial)`)` The requested search NasTrial. | `trainTrial` `object (`[NasTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial)`)` The train NasTrial corresponding to `[searchTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails#NasTrialDetail.FIELDS.search_trial)`. Only populated if `[searchTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails#NasTrialDetail.FIELDS.search_trial)` is used for training. | JSON representation  
---  
      
    
    {
      "name": string,
      "parameters": string,
      "searchTrial": {
        object ([NasTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial))
      },
      "trainTrial": {
        object ([NasTrial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/NasTrial))
      }
    }  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/get)`

|  Gets a NasTrialDetail.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.nasJobs.nasTrialDetails/list)`

|  List top NasTrialDetails of a NasJob.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
