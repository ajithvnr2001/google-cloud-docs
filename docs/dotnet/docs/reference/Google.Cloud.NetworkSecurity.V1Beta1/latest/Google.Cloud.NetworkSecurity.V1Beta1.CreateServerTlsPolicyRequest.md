---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest
title: Network Security v1beta1 API - Class CreateServerTlsPolicyRequest (2.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:47.667253+00:00
---

# Network Security v1beta1 API - Class CreateServerTlsPolicyRequest (2.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Security v1beta1 API - Class CreateServerTlsPolicyRequest (2.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/2.0.0-beta07/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest)
  * [ 1.0.0-beta02 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/1.0.0-beta02/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest)


    
    
    public sealed class CreateServerTlsPolicyRequest : IMessage<CreateServerTlsPolicyRequest>, IEquatable<CreateServerTlsPolicyRequest>, IDeepCloneable<CreateServerTlsPolicyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Security v1beta1 API class CreateServerTlsPolicyRequest.

Request used by the CreateServerTlsPolicy method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateServerTlsPolicyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkSecurity.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1)

## Assembly

Google.Cloud.NetworkSecurity.V1Beta1.dll

## Constructors 

### CreateServerTlsPolicyRequest()
    
    
    public CreateServerTlsPolicyRequest()

### CreateServerTlsPolicyRequest(CreateServerTlsPolicyRequest)
    
    
    public CreateServerTlsPolicyRequest(CreateServerTlsPolicyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource of the ServerTlsPolicy. Must be in the format `projects/*/locations/{location}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.CreateServerTlsPolicyRequest#Google_Cloud_NetworkSecurity_V1Beta1_CreateServerTlsPolicyRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### ServerTlsPolicy
    
    
    public ServerTlsPolicy ServerTlsPolicy { get; set; }

Required. ServerTlsPolicy resource to be created.

**Property Value**  
---  
**Type** | **Description**  
`[ServerTlsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkSecurity.V1Beta1/latest/Google.Cloud.NetworkSecurity.V1Beta1.ServerTlsPolicy)` |   
  
### ServerTlsPolicyId
    
    
    public string ServerTlsPolicyId { get; set; }

Required. Short name of the ServerTlsPolicy resource to be created. This value should be 1-63 characters long, containing only letters, numbers, hyphens, and underscores, and should not start with a number. E.g. "server_mtls_policy".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
