---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest
title: Assured Workloads v1 API - Class UpdateWorkloadRequest (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:52:08.440312+00:00
---

# Assured Workloads v1 API - Class UpdateWorkloadRequest (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Assured Workloads v1 API - Class UpdateWorkloadRequest (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.6.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.5.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.4.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.3.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.2.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.1.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/2.0.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.1.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/1.0.0/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)


    
    
    public sealed class UpdateWorkloadRequest : IMessage<UpdateWorkloadRequest>, IEquatable<UpdateWorkloadRequest>, IDeepCloneable<UpdateWorkloadRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Assured Workloads v1 API class UpdateWorkloadRequest.

Request for Updating a workload.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateWorkloadRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AssuredWorkloads.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1)

## Assembly

Google.Cloud.AssuredWorkloads.V1.dll

## Constructors 

### UpdateWorkloadRequest()
    
    
    public UpdateWorkloadRequest()

### UpdateWorkloadRequest(UpdateWorkloadRequest)
    
    
    public UpdateWorkloadRequest(UpdateWorkloadRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.UpdateWorkloadRequest)`  
  
  
## Properties 

### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The list of fields to be updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### Workload
    
    
    public Workload Workload { get; set; }

Required. The workload to update. The workload's `name` field is used to identify the workload to be updated. Format: organizations/{org_id}/locations/{location_id}/workloads/{workload_id}

**Property Value**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AssuredWorkloads.V1/latest/Google.Cloud.AssuredWorkloads.V1.Workload)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
