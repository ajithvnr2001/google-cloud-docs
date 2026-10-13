---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob
title: Cloud Channel v1 API - Class ReportJob (2.17.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:05.339594+00:00
---

# Cloud Channel v1 API - Class ReportJob (2.17.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Channel v1 API - Class ReportJob (2.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.17.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.16.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.16.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.15.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.15.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.14.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.14.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.13.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.12.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.11.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.10.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.9.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.8.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.7.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.6.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.5.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.4.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.3.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.2.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.1.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/2.0.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.7.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.6.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.5.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.4.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.3.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.2.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.1.0/Google.Cloud.Channel.V1.ReportJob)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/1.0.0/Google.Cloud.Channel.V1.ReportJob)


    
    
    [Obsolete]
    public sealed class ReportJob : IMessage<ReportJob>, IEquatable<ReportJob>, IDeepCloneable<ReportJob>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Channel v1 API class ReportJob.

The result of a [RunReportJob][] operation. Contains the name to use in [FetchReportResultsRequest.report_job][google.cloud.channel.v1.FetchReportResultsRequest.report_job] and the status of the operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReportJob

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReportJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReportJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReportJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Channel.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1)

## Assembly

Google.Cloud.Channel.V1.dll

## Constructors 

### ReportJob()
    
    
    public ReportJob()

### ReportJob(ReportJob)
    
    
    public ReportJob(ReportJob other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReportJob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The resource name of a report job. Name uses the format: `accounts/{account_id}/reportJobs/{report_job_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReportJobName
    
    
    [Obsolete]
    public ReportJobName ReportJobName { get; set; }

[ReportJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJobName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJob#Google_Cloud_Channel_V1_ReportJob_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ReportJobName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportJobName)` |   
  
### ReportStatus
    
    
    [Obsolete]
    public ReportStatus ReportStatus { get; set; }

The current status of report generation.

**Property Value**  
---  
**Type** | **Description**  
`[ReportStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Channel.V1/latest/Google.Cloud.Channel.V1.ReportStatus)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
