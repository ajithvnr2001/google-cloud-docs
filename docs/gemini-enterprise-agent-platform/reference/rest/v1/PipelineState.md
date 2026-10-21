---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PipelineState/
title: PipelineState \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:21:36.020098+00:00
---

# PipelineState  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/PipelineState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PipelineState Stay organized with collections  Save and categorize content based on your preferences. 

Describes the state of a pipeline.

Enums  
---  
`PIPELINE_STATE_UNSPECIFIED` | The pipeline state is unspecified.  
`PIPELINE_STATE_QUEUED` | The pipeline has been created or resumed, and processing has not yet begun.  
`PIPELINE_STATE_PENDING` | The service is preparing to run the pipeline.  
`PIPELINE_STATE_RUNNING` | The pipeline is in progress.  
`PIPELINE_STATE_SUCCEEDED` | The pipeline completed successfully.  
`PIPELINE_STATE_FAILED` | The pipeline failed.  
`PIPELINE_STATE_CANCELLING` | The pipeline is being cancelled. From this state, the pipeline may only go to either PIPELINE_STATE_SUCCEEDED, PIPELINE_STATE_FAILED or PIPELINE_STATE_CANCELLED.  
`PIPELINE_STATE_CANCELLED` | The pipeline has been cancelled.  
`PIPELINE_STATE_PAUSED` | The pipeline has been stopped, and can be resumed.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
