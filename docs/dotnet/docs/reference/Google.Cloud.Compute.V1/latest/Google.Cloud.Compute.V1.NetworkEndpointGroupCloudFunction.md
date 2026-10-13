---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction
title: Compute Engine v1 API - Class NetworkEndpointGroupCloudFunction (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:46.284260+00:00
---

# Compute Engine v1 API - Class NetworkEndpointGroupCloudFunction (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class NetworkEndpointGroupCloudFunction (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class NetworkEndpointGroupCloudFunction : IMessage<NetworkEndpointGroupCloudFunction>, IEquatable<NetworkEndpointGroupCloudFunction>, IDeepCloneable<NetworkEndpointGroupCloudFunction>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class NetworkEndpointGroupCloudFunction.

Configuration for a Cloud Function network endpoint group (NEG). The function must be provided explicitly or in the URL mask.

Note: Cloud Function must be in the same project and located in the same region as the Serverless NEG.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > NetworkEndpointGroupCloudFunction

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### NetworkEndpointGroupCloudFunction()
    
    
    public NetworkEndpointGroupCloudFunction()

### NetworkEndpointGroupCloudFunction(NetworkEndpointGroupCloudFunction)
    
    
    public NetworkEndpointGroupCloudFunction(NetworkEndpointGroupCloudFunction other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction)`  
  
  
## Properties 

### Function
    
    
    public string Function { get; set; }

A user-defined name of the Cloud Function.

The function name is case-sensitive and must be 1-63 characters long.

Example value: func1.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasFunction
    
    
    public bool HasFunction { get; }

Gets whether the "function" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasUrlMask
    
    
    public bool HasUrlMask { get; }

Gets whether the "url_mask" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### UrlMask
    
    
    public string UrlMask { get; set; }

An URL mask is one of the main components of the Cloud Function.

A template to parse function field from a request URL. URL mask allows for routing to multiple Cloud Functions without having to create multiple Network Endpoint Groups and backend services.

For example, request URLs mydomain.com/function1 andmydomain.com/function2 can be backed by the same Serverless NEG with URL mask /<function>. The URL mask will parse them to { function = "function1" } and{ function = "function2" } respectively.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
