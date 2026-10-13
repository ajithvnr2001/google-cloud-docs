---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest
title: Database Migration v1 API - Class SearchBackgroundJobsRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:04.392355+00:00
---

# Database Migration v1 API - Class SearchBackgroundJobsRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class SearchBackgroundJobsRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)


    
    
    public sealed class SearchBackgroundJobsRequest : IMessage<SearchBackgroundJobsRequest>, IEquatable<SearchBackgroundJobsRequest>, IDeepCloneable<SearchBackgroundJobsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class SearchBackgroundJobsRequest.

Request message for 'SearchBackgroundJobs' request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchBackgroundJobsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchBackgroundJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchBackgroundJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchBackgroundJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### SearchBackgroundJobsRequest()
    
    
    public SearchBackgroundJobsRequest()

### SearchBackgroundJobsRequest(SearchBackgroundJobsRequest)
    
    
    public SearchBackgroundJobsRequest(SearchBackgroundJobsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchBackgroundJobsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest)`  
  
  
## Properties 

### CompletedUntilTime
    
    
    public Timestamp CompletedUntilTime { get; set; }

Optional. If provided, only returns jobs that completed until (not including) the given timestamp.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ConversionWorkspace
    
    
    public string ConversionWorkspace { get; set; }

Required. Name of the conversion workspace resource whose jobs are listed, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConversionWorkspaceAsConversionWorkspaceName
    
    
    public ConversionWorkspaceName ConversionWorkspaceAsConversionWorkspaceName { get; set; }

[ConversionWorkspaceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConversionWorkspaceName)-typed view over the [ConversionWorkspace](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.SearchBackgroundJobsRequest#Google_Cloud_CloudDms_V1_SearchBackgroundJobsRequest_ConversionWorkspace) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConversionWorkspaceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.ConversionWorkspaceName)` |   
  
### MaxSize
    
    
    public int MaxSize { get; set; }

Optional. The maximum number of jobs to return. The service may return fewer than this value. If unspecified, at most 100 jobs are returned. The maximum value is 100; values above 100 are coerced to 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReturnMostRecentPerJobType
    
    
    public bool ReturnMostRecentPerJobType { get; set; }

Optional. Whether or not to return just the most recent job per job type,

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
