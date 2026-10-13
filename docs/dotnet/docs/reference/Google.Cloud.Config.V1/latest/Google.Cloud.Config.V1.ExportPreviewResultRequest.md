---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest
title: Infrastructure Manager v1 API - Class ExportPreviewResultRequest (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:04.765569+00:00
---

# Infrastructure Manager v1 API - Class ExportPreviewResultRequest (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Infrastructure Manager v1 API - Class ExportPreviewResultRequest (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class ExportPreviewResultRequest : IMessage<ExportPreviewResultRequest>, IEquatable<ExportPreviewResultRequest>, IDeepCloneable<ExportPreviewResultRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Infrastructure Manager v1 API class ExportPreviewResultRequest.

A request to export preview results.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExportPreviewResultRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Config.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1)

## Assembly

Google.Cloud.Config.V1.dll

## Constructors 

### ExportPreviewResultRequest()
    
    
    public ExportPreviewResultRequest()

### ExportPreviewResultRequest(ExportPreviewResultRequest)
    
    
    public ExportPreviewResultRequest(ExportPreviewResultRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExportPreviewResultRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The preview whose results should be exported. The preview value is in the format: 'projects/{project_id}/locations/{location}/previews/{preview}'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsPreviewName
    
    
    public PreviewName ParentAsPreviewName { get; set; }

[PreviewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.PreviewName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.ExportPreviewResultRequest#Google_Cloud_Config_V1_ExportPreviewResultRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PreviewName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Config.V1/latest/Google.Cloud.Config.V1.PreviewName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
