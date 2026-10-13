---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest
title: Vertex AI Notebooks v2 API - Class DiagnoseInstanceRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:22.212575+00:00
---

# Vertex AI Notebooks v2 API - Class DiagnoseInstanceRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI Notebooks v2 API - Class DiagnoseInstanceRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.3.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.2.0/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.1.0/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/1.0.0/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest)


    
    
    public sealed class DiagnoseInstanceRequest : IMessage<DiagnoseInstanceRequest>, IEquatable<DiagnoseInstanceRequest>, IDeepCloneable<DiagnoseInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI Notebooks v2 API class DiagnoseInstanceRequest.

Request for creating a notebook instance diagnostic file.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DiagnoseInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DiagnoseInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DiagnoseInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DiagnoseInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Notebooks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2)

## Assembly

Google.Cloud.Notebooks.V2.dll

## Constructors 

### DiagnoseInstanceRequest()
    
    
    public DiagnoseInstanceRequest()

### DiagnoseInstanceRequest(DiagnoseInstanceRequest)
    
    
    public DiagnoseInstanceRequest(DiagnoseInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DiagnoseInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest)`  
  
  
## Properties 

### DiagnosticConfig
    
    
    public DiagnosticConfig DiagnosticConfig { get; set; }

Required. Defines flags that are used to run the diagnostic tool

**Property Value**  
---  
**Type** | **Description**  
`[DiagnosticConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnosticConfig)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.InstanceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.DiagnoseInstanceRequest#Google_Cloud_Notebooks_V2_DiagnoseInstanceRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Notebooks.V2/latest/Google.Cloud.Notebooks.V2.InstanceName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Format: `projects/{project_id}/locations/{location}/instances/{instance_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeoutMinutes
    
    
    public int TimeoutMinutes { get; set; }

Optional. Maxmium amount of time in minutes before the operation times out.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
