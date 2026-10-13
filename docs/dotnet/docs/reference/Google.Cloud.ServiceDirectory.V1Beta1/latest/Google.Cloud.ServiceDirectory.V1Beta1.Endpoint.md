---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint
title: Service Directory v1beta1 API - Class Endpoint (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:00.141988+00:00
---

# Service Directory v1beta1 API - Class Endpoint (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1beta1 API - Class Endpoint (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/2.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/1.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint)


    
    
    public sealed class Endpoint : IMessage<Endpoint>, IEquatable<Endpoint>, IDeepCloneable<Endpoint>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Directory v1beta1 API class Endpoint.

An individual endpoint that provides a [service][google.cloud.servicedirectory.v1beta1.Service]. The service must already exist to create an endpoint.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Endpoint

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceDirectory.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1)

## Assembly

Google.Cloud.ServiceDirectory.V1Beta1.dll

## Constructors 

### Endpoint()
    
    
    public Endpoint()

### Endpoint(Endpoint)
    
    
    public Endpoint(Endpoint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint)`  
  
  
## Properties 

### Address
    
    
    public string Address { get; set; }

Optional. An IPv4 or IPv6 address. Service Directory rejects bad addresses like:

  * `8.8.8`
  * `8.8.8.8:53`
  * `test:bad:address`
  * `[::1]`
  * `[::1]:8080`



Limited to 45 characters.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The timestamp when the endpoint was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### EndpointName
    
    
    public EndpointName EndpointName { get; set; }

[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint#Google_Cloud_ServiceDirectory_V1Beta1_Endpoint_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.EndpointName)` |   
  
### Metadata
    
    
    public MapField<string, string> Metadata { get; }

Optional. Metadata for the endpoint. This data can be consumed by service clients.

Restrictions:

  * The entire metadata dictionary may contain up to 512 characters, spread accoss all key-value pairs. Metadata that goes beyond this limit are rejected
  * Valid metadata keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Metadata that fails to meet these requirements are rejected



Note: This field is equivalent to the `annotations` field in the v1 API. They have the same syntax and read/write to the same location in Service Directory.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. The resource name for the endpoint in the format `projects/*/locations/*/namespaces/*/services/*/endpoints/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

Immutable. The Google Compute Engine network (VPC) of the endpoint in the format `projects/<project number>/locations/global/networks/*`.

The project must be specified by project number (project id is rejected). Incorrectly formatted networks are rejected, but no other validation is performed on this field (ex. network or project existence, reachability, or permissions).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.Endpoint#Google_Cloud_ServiceDirectory_V1Beta1_Endpoint_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.NetworkName)` |   
  
### Port
    
    
    public int Port { get; set; }

Optional. Service Directory rejects values outside of `[0, 65535]`.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. A globally unique identifier (in UUID4 format) for this endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The timestamp when the endpoint was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
