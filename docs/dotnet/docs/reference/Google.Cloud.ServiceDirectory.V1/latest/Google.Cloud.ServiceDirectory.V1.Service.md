---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service
title: Service Directory v1 API - Class Service (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:35.365374+00:00
---

# Service Directory v1 API - Class Service (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1 API - Class Service (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.6.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.5.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.4.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.3.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.2.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.1.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.0.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.4.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.3.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.2.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.1.0/Google.Cloud.ServiceDirectory.V1.Service)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.0.0/Google.Cloud.ServiceDirectory.V1.Service)


    
    
    public sealed class Service : IMessage<Service>, IEquatable<Service>, IDeepCloneable<Service>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Directory v1 API class Service.

An individual service. A service contains a name and optional metadata. A service must exist before [endpoints][google.cloud.servicedirectory.v1.Endpoint] can be added to it.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Service

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1)

## Assembly

Google.Cloud.ServiceDirectory.V1.dll

## Constructors 

### Service()
    
    
    public Service()

### Service(Service)
    
    
    public Service(Service other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Optional. Annotations for the service. This data can be consumed by service clients.

Restrictions:

  * The entire annotations dictionary may contain up to 2000 characters, spread accoss all key-value pairs. Annotations that go beyond this limit are rejected
  * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (/). The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_), dots (.), and alphanumerics between. The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots (.), not longer than 253 characters in total, followed by a slash (/). Annotations that fails to meet these requirements are rejected



Note: This field is equivalent to the `metadata` field in the v1beta1 API. They have the same syntax and read/write to the same location in Service Directory.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Endpoints
    
    
    public RepeatedField<Endpoint> Endpoints { get; }

Output only. Endpoints associated with this service. Returned on [LookupService.ResolveService][google.cloud.servicedirectory.v1.LookupService.ResolveService]. Control plane clients should use [RegistrationService.ListEndpoints][google.cloud.servicedirectory.v1.RegistrationService.ListEndpoints].

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Endpoint)` |   
  
### Name
    
    
    public string Name { get; set; }

Immutable. The resource name for the service in the format `projects/*/locations/*/namespaces/*/services/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceName
    
    
    public ServiceName ServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service#Google_Cloud_ServiceDirectory_V1_Service_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.ServiceName)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. The globally unique identifier of the service in the UUID4 format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
