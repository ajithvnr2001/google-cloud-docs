---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest
title: API hub v1 API - Class ListPluginInstancesRequest (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:34.865081+00:00
---

# API hub v1 API - Class ListPluginInstancesRequest (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  API hub v1 API - Class ListPluginInstancesRequest (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.2.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.1.0/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/1.0.0/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)


    
    
    public sealed class ListPluginInstancesRequest : IPageRequest, IMessage<ListPluginInstancesRequest>, IEquatable<ListPluginInstancesRequest>, IDeepCloneable<ListPluginInstancesRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the API hub v1 API class ListPluginInstancesRequest.

The [ListPluginInstances][google.cloud.apihub.v1.ApiHubPlugin.ListPluginInstances] method's request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListPluginInstancesRequest

## Implements

[IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApiHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1)

## Assembly

Google.Cloud.ApiHub.V1.dll

## Constructors 

### ListPluginInstancesRequest()
    
    
    public ListPluginInstancesRequest()

### ListPluginInstancesRequest(ListPluginInstancesRequest)
    
    
    public ListPluginInstancesRequest(ListPluginInstancesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListPluginInstancesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

Optional. An expression that filters the list of plugin instances.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. The comparison operator must be one of: `<`, `>` or `=`. Filters are not case sensitive.

The following fields in the `PluginInstances` are eligible for filtering:

  * `state` \- The state of the Plugin Instance. Allowed comparison operators: `=`.



A filter function is also supported in the filter string. The filter function is `id(name)`. The `id(name)` function returns the id of the resource name. For example, `id(name) = \"plugin-instance-1\"` is equivalent to `name = \"projects/test-project-id/locations/test-location-id/plugins/plugin-1/instances/plugin-instance-1\"` provided the parent is `projects/test-project-id/locations/test-location-id/plugins/plugin-1`.

Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API. Here are a few examples:

  * `state = ENABLED` \- The plugin instance is in enabled state.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of hub plugins to return. The service may return fewer than this value. If unspecified, at most 50 hub plugins will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A page token, received from a previous `ListPluginInstances` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPluginInstances` must match the call that provided the page token.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource where this plugin will be created. Format: `projects/{project}/locations/{location}/plugins/{plugin}`. To list plugin instances for multiple plugins, use the - character instead of the plugin ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsPluginName
    
    
    public PluginName ParentAsPluginName { get; set; }

[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.ListPluginInstancesRequest#Google_Cloud_ApiHub_V1_ListPluginInstancesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PluginName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApiHub.V1/latest/Google.Cloud.ApiHub.V1.PluginName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
