---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus
title: Service Management v1 API - Enum Rollout.Types.RolloutStatus (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:10.962736+00:00
---

# Service Management v1 API - Enum Rollout.Types.RolloutStatus (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Management v1 API - Enum Rollout.Types.RolloutStatus (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.4.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.3.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.2.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.1.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/2.0.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.5.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.4.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.3.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.2.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/1.1.0/Google.Cloud.ServiceManagement.V1.Rollout.Types.RolloutStatus)


    
    
    public enum Rollout.Types.RolloutStatus

Reference documentation and code samples for the Service Management v1 API enum Rollout.Types.RolloutStatus.

Status of a Rollout.

## Namespace

[Google.Cloud.ServiceManagement.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceManagement.V1/latest/Google.Cloud.ServiceManagement.V1)

## Assembly

Google.Cloud.ServiceManagement.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`Cancelled` | The Rollout has been cancelled. This can happen if you have overlapping Rollout pushes, and the previous ones will be cancelled.  
`Failed` | The Rollout has failed and the rollback attempt has failed too.  
`FailedRolledBack` | The Rollout has failed and rolled back to the previous successful Rollout.  
`InProgress` | The Rollout is in progress.  
`Pending` | The Rollout has not started yet and is pending for execution.  
`Success` | The Rollout has completed successfully.  
`Unspecified` | No status specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
