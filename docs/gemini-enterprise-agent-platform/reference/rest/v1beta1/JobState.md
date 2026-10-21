---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/JobState/
title: JobState \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:52:05.891550+00:00
---

# JobState  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/JobState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  JobState Stay organized with collections  Save and categorize content based on your preferences. 

Describes the state of a job.

Enums  
---  
`JOB_STATE_UNSPECIFIED` | The job state is unspecified.  
`JOB_STATE_QUEUED` | The job has been just created or resumed and processing has not yet begun.  
`JOB_STATE_PENDING` | The service is preparing to run the job.  
`JOB_STATE_RUNNING` | The job is in progress.  
`JOB_STATE_SUCCEEDED` | The job completed successfully.  
`JOB_STATE_FAILED` | The job failed.  
`JOB_STATE_CANCELLING` | The job is being cancelled. From this state the job may only go to either `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.  
`JOB_STATE_CANCELLED` | The job has been cancelled.  
`JOB_STATE_PAUSED` | The job has been stopped, and can be resumed.  
`JOB_STATE_EXPIRED` | The job has expired.  
`JOB_STATE_UPDATING` | The job is being updated. Only jobs in the `RUNNING` state can be updated. After updating, the job goes back to the `RUNNING` state.  
`JOB_STATE_PARTIALLY_SUCCEEDED` | The job is partially succeeded, some results may be missing due to errors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
