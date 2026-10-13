---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest
title: Chronicle v1 API - Class ComputeAllFindingsRefinementActivitiesRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:45.774648+00:00
---

# Chronicle v1 API - Class ComputeAllFindingsRefinementActivitiesRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class ComputeAllFindingsRefinementActivitiesRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class ComputeAllFindingsRefinementActivitiesRequest : IMessage<ComputeAllFindingsRefinementActivitiesRequest>, IEquatable<ComputeAllFindingsRefinementActivitiesRequest>, IDeepCloneable<ComputeAllFindingsRefinementActivitiesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class ComputeAllFindingsRefinementActivitiesRequest.

Request message for ComputeAllFindingsRefinementActivities method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ComputeAllFindingsRefinementActivitiesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### ComputeAllFindingsRefinementActivitiesRequest()
    
    
    public ComputeAllFindingsRefinementActivitiesRequest()

### ComputeAllFindingsRefinementActivitiesRequest(ComputeAllFindingsRefinementActivitiesRequest)
    
    
    public ComputeAllFindingsRefinementActivitiesRequest(ComputeAllFindingsRefinementActivitiesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest)`  
  
  
## Properties 

### Instance
    
    
    public string Instance { get; set; }

Required. The ID of the Instance to retrieve counts for. Format: projects/{project}/locations/{location}/instances/{instance}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceAsInstanceName
    
    
    public InstanceName InstanceAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)-typed view over the [Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.ComputeAllFindingsRefinementActivitiesRequest#Google_Cloud_Chronicle_V1_ComputeAllFindingsRefinementActivitiesRequest_Instance) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.InstanceName)` |   
  
### Interval
    
    
    public Interval Interval { get; set; }

The time interval the activity is measured over.

**Property Value**  
---  
**Type** | **Description**  
`[Interval](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Interval.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
