---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse
title: Workload Manager v1 API - Class ListExecutionsResponse (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:40.145029+00:00
---

# Workload Manager v1 API - Class ListExecutionsResponse (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Workload Manager v1 API - Class ListExecutionsResponse (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class ListExecutionsResponse : IMessage<ListExecutionsResponse>, IEquatable<ListExecutionsResponse>, IDeepCloneable<ListExecutionsResponse>, IBufferMessage, IMessage, IPageResponse<Execution>, IEnumerable<Execution>, IEnumerable

Reference documentation and code samples for the Workload Manager v1 API class ListExecutionsResponse.

Response message for the ListExecutions RPC.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListExecutionsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageResponse](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageResponse-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Execution), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Execution), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.WorkloadManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1)

## Assembly

Google.Cloud.WorkloadManager.V1.dll

## Constructors 

### ListExecutionsResponse()
    
    
    public ListExecutionsResponse()

### ListExecutionsResponse(ListExecutionsResponse)
    
    
    public ListExecutionsResponse(ListExecutionsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListExecutionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.ListExecutionsResponse)`  
  
  
## Properties 

### Executions
    
    
    public RepeatedField<Execution> Executions { get; }

The list of Execution.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Execution)` |   
  
### NextPageToken
    
    
    public string NextPageToken { get; set; }

A token identifying a page of results the server should return.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Unreachable
    
    
    public RepeatedField<string> Unreachable { get; }

Locations that could not be reached.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### GetEnumerator()
    
    
    public IEnumerator<Execution> GetEnumerator()

Returns an enumerator that iterates through the resources in this response.

**Returns**  
---  
**Type** | **Description**  
`[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)[Execution](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.WorkloadManager.V1/latest/Google.Cloud.WorkloadManager.V1.Execution)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-22 UTC."],[],[]] 
