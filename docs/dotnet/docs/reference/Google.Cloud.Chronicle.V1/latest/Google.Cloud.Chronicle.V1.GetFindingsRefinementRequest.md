---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest
title: Chronicle v1 API - Class GetFindingsRefinementRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:40.187612+00:00
---

# Chronicle v1 API - Class GetFindingsRefinementRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class GetFindingsRefinementRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class GetFindingsRefinementRequest : IMessage<GetFindingsRefinementRequest>, IEquatable<GetFindingsRefinementRequest>, IDeepCloneable<GetFindingsRefinementRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class GetFindingsRefinementRequest.

Request message for GetFindingsRefinement method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetFindingsRefinementRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetFindingsRefinementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetFindingsRefinementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetFindingsRefinementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### GetFindingsRefinementRequest()
    
    
    public GetFindingsRefinementRequest()

### GetFindingsRefinementRequest(GetFindingsRefinementRequest)
    
    
    public GetFindingsRefinementRequest(GetFindingsRefinementRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetFindingsRefinementRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest)`  
  
  
## Properties 

### FindingsRefinementName
    
    
    public FindingsRefinementName FindingsRefinementName { get; set; }

[FindingsRefinementName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.FindingsRefinementName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetFindingsRefinementRequest#Google_Cloud_Chronicle_V1_GetFindingsRefinementRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FindingsRefinementName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.FindingsRefinementName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the findings refinement to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/findingsRefinements/{findings_refinement}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
