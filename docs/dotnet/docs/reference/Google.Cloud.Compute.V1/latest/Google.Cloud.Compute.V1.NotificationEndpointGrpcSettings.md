---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings
title: Compute Engine v1 API - Class NotificationEndpointGrpcSettings (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:40.935110+00:00
---

# Compute Engine v1 API - Class NotificationEndpointGrpcSettings (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class NotificationEndpointGrpcSettings (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class NotificationEndpointGrpcSettings : IMessage<NotificationEndpointGrpcSettings>, IEquatable<NotificationEndpointGrpcSettings>, IDeepCloneable<NotificationEndpointGrpcSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class NotificationEndpointGrpcSettings.

Represents a gRPC setting that describes one gRPC notification endpoint and the retry duration attempting to send notification to this endpoint.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > NotificationEndpointGrpcSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[NotificationEndpointGrpcSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[NotificationEndpointGrpcSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[NotificationEndpointGrpcSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### NotificationEndpointGrpcSettings()
    
    
    public NotificationEndpointGrpcSettings()

### NotificationEndpointGrpcSettings(NotificationEndpointGrpcSettings)
    
    
    public NotificationEndpointGrpcSettings(NotificationEndpointGrpcSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[NotificationEndpointGrpcSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NotificationEndpointGrpcSettings)`  
  
  
## Properties 

### Authority
    
    
    public string Authority { get; set; }

Optional. If specified, this field is used to set the authority header by the sender of notifications. See <https://tools.ietf.org/html/rfc7540#section-8.1.2.3>

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Endpoint
    
    
    public string Endpoint { get; set; }

Endpoint to which gRPC notifications are sent. This must be a valid gRPCLB DNS name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasAuthority
    
    
    public bool HasAuthority { get; }

Gets whether the "authority" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEndpoint
    
    
    public bool HasEndpoint { get; }

Gets whether the "endpoint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPayloadName
    
    
    public bool HasPayloadName { get; }

Gets whether the "payload_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRetryDurationSec
    
    
    public bool HasRetryDurationSec { get; }

Gets whether the "retry_duration_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PayloadName
    
    
    public string PayloadName { get; set; }

Optional. If specified, this field is used to populate the "name" field in gRPC requests.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ResendInterval
    
    
    public Duration ResendInterval { get; set; }

Optional. This field is used to configure how often to send a full update of all non-healthy backends. If unspecified, full updates are not sent. If specified, must be in the range between 600 seconds to 3600 seconds. Nanos are disallowed. Can only be set for regional notification endpoints.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Duration)` |   
  
### RetryDurationSec
    
    
    public uint RetryDurationSec { get; set; }

How much time (in seconds) is spent attempting notification retries until a successful response is received. Default is 30s. Limit is 20m (1200s). Must be a positive number.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
