---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest
title: API hub v1 API - Class CreatePluginInstanceRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:36.211674+00:00
---

# API hub v1 API - Class CreatePluginInstanceRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class CreatePluginInstanceRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)


    
    
    public sealed class CreatePluginInstanceRequest : IMessage<CreatePluginInstanceRequest>, IEquatable<CreatePluginInstanceRequest>, IDeepCloneable<CreatePluginInstanceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class CreatePluginInstanceRequest.

The [CreatePluginInstance][google.cloud.apihub.v1.ApiHubPlugin.CreatePluginInstance] method's request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreatePluginInstanceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### CreatePluginInstanceRequest()
    
    
    public CreatePluginInstanceRequest()

### CreatePluginInstanceRequest(CreatePluginInstanceRequest)
    
    
    public CreatePluginInstanceRequest(CreatePluginInstanceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreatePluginInstanceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The parent of the plugin instance resource. Format: `projects/{project}/locations/{location}/plugins/{plugin}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsPluginName
    
    
    public PluginName ParentAsPluginName { get; set; }

[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.CreatePluginInstanceRequest#Google_Cloud_ApiHub_V1_CreatePluginInstanceRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)` |   
  
### PluginInstance
    
    
    public PluginInstance PluginInstance { get; set; }

Required. The plugin instance to create.

**Property Value**  
---  
**Type** | **Description**  
`[PluginInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginInstance)` |   
  
### PluginInstanceId
    
    
    public string PluginInstanceId { get; set; }

Optional. The ID to use for the plugin instance, which will become the final component of the plugin instance's resource name. This field is optional.

  * If provided, the same will be used. The service will throw an error if the specified id is already used by another plugin instance in the plugin resource.
  * If not provided, a system generated id will be used.



This value should be 4-63 characters, and valid characters are /[a-z][A-Z][0-9]-_/.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
