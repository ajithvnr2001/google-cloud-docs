---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.BatchCreateTasksMetadata.Types.State
title: Google Cloud Tasks v2beta3 API - Enum BatchCreateTasksMetadata.Types.State (3.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:52.393628+00:00
---

# Google Cloud Tasks v2beta3 API - Enum BatchCreateTasksMetadata.Types.State (3.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.BatchCreateTasksMetadata.Types.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2beta3 API - Enum BatchCreateTasksMetadata.Types.State (3.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.0-beta09 (latest)  3.0.0-beta08  2.0.0-beta08 
    
    
    public enum BatchCreateTasksMetadata.Types.State

Reference documentation and code samples for the Google Cloud Tasks v2beta3 API enum BatchCreateTasksMetadata.Types.State.

The state of the batch create operation.

## Namespace

[Google.Cloud.Tasks.V2Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3)

## Assembly

Google.Cloud.Tasks.V2Beta3.dll

## Fields   
  
---  
**Name** | **Description**  
`Cancelled` | The batch create was cancelled.  
`Failed` | The batch create has failed. This means the overall batch create operation failed to complete. This can happen due to an internal error preventing the operation from finishing.  
`PartiallySucceeded` | The batch create has finished with partial success. The tasks that failed to be created are reported in [failed_requests][google.cloud.tasks.v2beta3.BatchCreateTasksMetadata.failed_requests].  
`Running` | The batch create is running.  
`Succeeded` | The batch create has finished. All tasks in the request were successfully created.  
`Unspecified` | The default value. This value is used if the state is omitted.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
