---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest
title: Vertex AI Notebooks v1beta1 API - Class ResetInstanceRequest (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:48.295165+00:00
---

# Vertex AI Notebooks v1beta1 API - Class ResetInstanceRequest (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v1beta1 API - Class ResetInstanceRequest (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/2.0.0-beta05/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/1.0.0-beta04/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest)


    
    
    public sealed class ResetInstanceRequest : IMessage<ResetInstanceRequest>, IEquatable<ResetInstanceRequest>, IDeepCloneable<ResetInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v1beta1 API class ResetInstanceRequest.

Request for reseting a notebook instance

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResetInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1)

## Assembly

Google.Cloud.Notebooks.V1Beta1.dll

## Constructors 

### ResetInstanceRequest()
    
    
    public ResetInstanceRequest()

### ResetInstanceRequest(ResetInstanceRequest)
    
    
    public ResetInstanceRequest(ResetInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResetInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V1Beta1/latest/Google.Cloud.Notebooks.V1Beta1.ResetInstanceRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
