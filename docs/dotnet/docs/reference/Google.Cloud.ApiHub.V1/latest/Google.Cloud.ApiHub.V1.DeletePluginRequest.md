---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest
title: API hub v1 API - Class DeletePluginRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:16.610173+00:00
---

# API hub v1 API - Class DeletePluginRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class DeletePluginRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.DeletePluginRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.DeletePluginRequest)


    
    
    public sealed class DeletePluginRequest : IMessage<DeletePluginRequest>, IEquatable<DeletePluginRequest>, IDeepCloneable<DeletePluginRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class DeletePluginRequest.

The [DeletePlugin][ApiHub.DeletePlugin] method's request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeletePluginRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### DeletePluginRequest()
    
    
    public DeletePluginRequest()

### DeletePluginRequest(DeletePluginRequest)
    
    
    public DeletePluginRequest(DeletePluginRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeletePluginRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the Plugin resource to delete. Format: `projects/{project}/locations/{location}/plugins/{plugin}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PluginName
    
    
    public PluginName PluginName { get; set; }

[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.DeletePluginRequest#Google_Cloud_ApiHub_V1_DeletePluginRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
