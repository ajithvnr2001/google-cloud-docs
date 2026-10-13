---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent
title: BigQuery Audit Data Logging v1 API - Class JobCompletedEvent (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:07.171069+00:00
---

# BigQuery Audit Data Logging v1 API - Class JobCompletedEvent (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Audit Data Logging v1 API - Class JobCompletedEvent (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.3.0/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.2.0/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.1.0/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.0.0/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)


    
    
    public sealed class JobCompletedEvent : IMessage<JobCompletedEvent>, IEquatable<JobCompletedEvent>, IDeepCloneable<JobCompletedEvent>, IBufferMessage, IMessage

Reference documentation and code samples for the BigQuery Audit Data Logging v1 API class JobCompletedEvent.

Query job completed event.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > JobCompletedEvent

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[JobCompletedEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[JobCompletedEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[JobCompletedEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Logging.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1)

## Assembly

Google.Cloud.BigQuery.Logging.V1.dll

## Constructors 

### JobCompletedEvent()
    
    
    public JobCompletedEvent()

### JobCompletedEvent(JobCompletedEvent)
    
    
    public JobCompletedEvent(JobCompletedEvent other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[JobCompletedEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.JobCompletedEvent)`  
  
  
## Properties 

### EventName
    
    
    public string EventName { get; set; }

Name of the event.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Job
    
    
    public Job Job { get; set; }

Job information.

**Property Value**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.Job)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
