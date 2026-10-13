---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest
title: Google Cloud Tasks v2beta3 API - Class RunTaskRequest (3.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:06.950922+00:00
---

# Google Cloud Tasks v2beta3 API - Class RunTaskRequest (3.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2beta3 API - Class RunTaskRequest (3.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

3.0.0-beta09 (latest)  3.0.0-beta08  2.0.0-beta08 
    
    
    public sealed class RunTaskRequest : IMessage<RunTaskRequest>, IEquatable<RunTaskRequest>, IDeepCloneable<RunTaskRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2beta3 API class RunTaskRequest.

Request message for forcing a task to run now using [RunTask][google.cloud.tasks.v2beta3.CloudTasks.RunTask].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RunTaskRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3)

## Assembly

Google.Cloud.Tasks.V2Beta3.dll

## Constructors 

### RunTaskRequest()
    
    
    public RunTaskRequest()

### RunTaskRequest(RunTaskRequest)
    
    
    public RunTaskRequest(RunTaskRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RunTaskRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The task name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResponseView
    
    
    public Task.Types.View ResponseView { get; set; }

The response_view specifies which subset of the [Task][google.cloud.tasks.v2beta3.Task] will be returned.

By default response_view is [BASIC][google.cloud.tasks.v2beta3.Task.View.BASIC]; not all information is retrieved by default because some data, such as payloads, might be desirable to return only when needed because of its large size or because of the sensitivity of data that it contains.

Authorization for [FULL][google.cloud.tasks.v2beta3.Task.View.FULL] requires `cloudtasks.tasks.fullView` [Google IAM](https://cloud.google.com/iam/) permission on the [Task][google.cloud.tasks.v2beta3.Task] resource.

**Property Value**  
---  
**Type** | **Description**  
`[Task](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.Task)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.Task.Types)[View](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.Task.Types.View)` |   
  
### TaskName
    
    
    public TaskName TaskName { get; set; }

[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.RunTaskRequest#Google_Cloud_Tasks_V2Beta3_RunTaskRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[TaskName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2Beta3/latest/Google.Cloud.Tasks.V2Beta3.TaskName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
