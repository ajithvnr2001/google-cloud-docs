---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.Job.Types.State
title: Google Cloud Scheduler v1 API - Enum Job.Types.State (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:19.954767+00:00
---

# Google Cloud Scheduler v1 API - Enum Job.Types.State (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.Job.Types.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Scheduler v1 API - Enum Job.Types.State (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.5.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.4.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.3.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.2.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.1.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.0.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/2.3.0/Google.Cloud.Scheduler.V1.Job.Types.State)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/2.2.0/Google.Cloud.Scheduler.V1.Job.Types.State)


    
    
    public enum Job.Types.State

Reference documentation and code samples for the Google Cloud Scheduler v1 API enum Job.Types.State.

State of the job.

## Namespace

[Google.Cloud.Scheduler.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1)

## Assembly

Google.Cloud.Scheduler.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`Disabled` | The job is disabled by the system due to error. The user cannot directly set a job to be disabled.  
`Enabled` | The job is executing normally.  
`Paused` | The job is paused by the user. It will not execute. A user can intentionally pause the job using [PauseJobRequest][google.cloud.scheduler.v1.PauseJobRequest].  
`Unspecified` | Unspecified state.  
`UpdateFailed` | The job state resulting from a failed [CloudScheduler.UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob] operation. To recover a job from this state, retry [CloudScheduler.UpdateJob][google.cloud.scheduler.v1.CloudScheduler.UpdateJob] until a successful response is received.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
