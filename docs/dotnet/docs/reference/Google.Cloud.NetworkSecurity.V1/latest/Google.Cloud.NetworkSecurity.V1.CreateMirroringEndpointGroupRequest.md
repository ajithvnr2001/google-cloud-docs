---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest
title: Network Security v1 API - Class CreateMirroringEndpointGroupRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:07.322264+00:00
---

# Network Security v1 API - Class CreateMirroringEndpointGroupRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1 API - Class CreateMirroringEndpointGroupRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class CreateMirroringEndpointGroupRequest : IMessage<CreateMirroringEndpointGroupRequest>, IEquatable<CreateMirroringEndpointGroupRequest>, IDeepCloneable<CreateMirroringEndpointGroupRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Security v1 API class CreateMirroringEndpointGroupRequest.

Request message for CreateMirroringEndpointGroup.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateMirroringEndpointGroupRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateMirroringEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateMirroringEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateMirroringEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1)

## Assembly

Google.Cloud.NetworkSecurity.V1.dll

## Constructors 

### CreateMirroringEndpointGroupRequest()
    
    
    public CreateMirroringEndpointGroupRequest()

### CreateMirroringEndpointGroupRequest(CreateMirroringEndpointGroupRequest)
    
    
    public CreateMirroringEndpointGroupRequest(CreateMirroringEndpointGroupRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateMirroringEndpointGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest)`  
  
  
## Properties 

### MirroringEndpointGroup
    
    
    public MirroringEndpointGroup MirroringEndpointGroup { get; set; }

Required. The endpoint group to create.

**Property Value**  
---  
**Type** | **Description**  
`[MirroringEndpointGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.MirroringEndpointGroup)` |   
  
### MirroringEndpointGroupId
    
    
    public string MirroringEndpointGroupId { get; set; }

Required. The ID to use for the endpoint group, which will become the final component of the endpoint group's resource name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource where this endpoint group will be created. Format: projects/{project}/locations/{location}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1/latest/Google.Cloud.NetworkSecurity.V1.CreateMirroringEndpointGroupRequest#Google_Cloud_NetworkSecurity_V1_CreateMirroringEndpointGroupRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `request_id` is provided. See <https://google.aip.dev/155> for more details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-01 UTC."],[],[]] 
