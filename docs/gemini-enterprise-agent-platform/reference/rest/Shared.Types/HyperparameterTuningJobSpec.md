---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HyperparameterTuningJobSpec/
title: HyperparameterTuningJobSpec \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:51:25.685293+00:00
---

# HyperparameterTuningJobSpec  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/HyperparameterTuningJobSpec/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  HyperparameterTuningJobSpec Stay organized with collections  Save and categorize content based on your preferences. 

Fields  
  
`studySpec` `object (`[StudySpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/StudySpec)`)` Study configuration of the HyperparameterTuningJob. | `trialJobSpec` `object (`[CustomJobSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec)`)` The spec of a trial job. The same spec applies to the CustomJobs created in all the trials. | `maxTrialCount` `integer` The desired total number of Trials. | `parallelTrialCount` `integer` The desired number of Trials to run in parallel. | `maxFailedTrialCount` `integer` The number of failed Trials that need to be seen before failing the HyperparameterTuningJob.If set to 0, Agent Platform decides how many Trials must fail before the whole job fails. | JSON representation  
---  
      
    
    {
      "studySpec": {
        object ([StudySpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/StudySpec))
      },
      "trialJobSpec": {
        object ([CustomJobSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec))
      },
      "maxTrialCount": integer,
      "parallelTrialCount": integer,
      "maxFailedTrialCount": integer
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
