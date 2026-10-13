---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint
title: Agent Registry v1 API - Class Endpoint (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:38.525073+00:00
---

# Agent Registry v1 API - Class Endpoint (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Agent Registry v1 API - Class Endpoint (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class Endpoint : IMessage<Endpoint>, IEquatable<Endpoint>, IDeepCloneable<Endpoint>, IBufferMessage, IMessage

Reference documentation and code samples for the Agent Registry v1 API class Endpoint.

Represents an Endpoint.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Endpoint

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AgentRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1)

## Assembly

Google.Cloud.AgentRegistry.V1.dll

## Constructors 

### Endpoint()
    
    
    public Endpoint()

### Endpoint(Endpoint)
    
    
    public Endpoint(Endpoint other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Endpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint)`  
  
  
## Properties 

### Attributes
    
    
    public MapField<string, Struct> Attributes { get; }

Output only. Attributes of the Endpoint.

Valid values:

  * `agentregistry.googleapis.com/system/RuntimeReference`: {"uri": "//..."} - the URI of the underlying resource hosting the Endpoint, for example, the GKE Deployment.



**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

Output only. Description of an Endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Output only. Display name for the Endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndpointId
    
    
    public string EndpointId { get; set; }

Output only. A stable, globally unique identifier for Endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EndpointName
    
    
    public EndpointName EndpointName { get; set; }

[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.EndpointName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Endpoint#Google_Cloud_AgentRegistry_V1_Endpoint_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[EndpointName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.EndpointName)` |   
  
### Interfaces
    
    
    public RepeatedField<Interface> Interfaces { get; }

Required. The connection details for the Endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Interface](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AgentRegistry.V1/latest/Google.Cloud.AgentRegistry.V1.Interface)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the Endpoint. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Update time.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
