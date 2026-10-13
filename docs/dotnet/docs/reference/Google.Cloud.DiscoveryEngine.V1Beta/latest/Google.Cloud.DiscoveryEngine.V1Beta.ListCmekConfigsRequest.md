---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest
title: Discovery Engine v1beta API - Class ListCmekConfigsRequest (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:13.238171+00:00
---

# Discovery Engine v1beta API - Class ListCmekConfigsRequest (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class ListCmekConfigsRequest (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class ListCmekConfigsRequest : IMessage<ListCmekConfigsRequest>, IEquatable<ListCmekConfigsRequest>, IDeepCloneable<ListCmekConfigsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class ListCmekConfigsRequest.

Request message for [CmekConfigService.ListCmekConfigs][google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListCmekConfigsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListCmekConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListCmekConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListCmekConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### ListCmekConfigsRequest()
    
    
    public ListCmekConfigsRequest()

### ListCmekConfigsRequest(ListCmekConfigsRequest)
    
    
    public ListCmekConfigsRequest(ListCmekConfigsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListCmekConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The parent location resource name, such as `projects/{project}/locations/{location}`.

If the caller does not have permission to list [CmekConfig][google.cloud.discoveryengine.v1beta.CmekConfig]s under this location, regardless of whether or not a CmekConfig exists, a PERMISSION_DENIED error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.LocationName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListCmekConfigsRequest#Google_Cloud_DiscoveryEngine_V1Beta_ListCmekConfigsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.LocationName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
