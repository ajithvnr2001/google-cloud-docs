---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup
title: Compute Engine v1 API - Class NetworkEndpointGroup (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:33.497122+00:00
---

# Compute Engine v1 API - Class NetworkEndpointGroup (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class NetworkEndpointGroup (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class NetworkEndpointGroup : IMessage<NetworkEndpointGroup>, IEquatable<NetworkEndpointGroup>, IDeepCloneable<NetworkEndpointGroup>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class NetworkEndpointGroup.

Represents a collection of network endpoints.

A network endpoint group (NEG) defines how a set of endpoints should be reached, whether they are reachable, and where they are located. For more information about using NEGs for different use cases, seeNetwork endpoint groups overview.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API \- To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API \- To manage NEGs with global scope (such as global internet NEGs):global API

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > NetworkEndpointGroup

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[NetworkEndpointGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[NetworkEndpointGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[NetworkEndpointGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### NetworkEndpointGroup()
    
    
    public NetworkEndpointGroup()

### NetworkEndpointGroup(NetworkEndpointGroup)
    
    
    public NetworkEndpointGroup(NetworkEndpointGroup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[NetworkEndpointGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroup)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Optional. Metadata defined as annotations on the network endpoint group.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AppEngine
    
    
    public NetworkEndpointGroupAppEngine AppEngine { get; set; }

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupAppEngine](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupAppEngine)` |   
  
### CloudFunction
    
    
    public NetworkEndpointGroupCloudFunction CloudFunction { get; set; }

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudFunction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudFunction)` |   
  
### CloudRun
    
    
    public NetworkEndpointGroupCloudRun CloudRun { get; set; }

Optional. Only valid when networkEndpointType isSERVERLESS. Only one of cloudRun,appEngine or cloudFunction may be set.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupCloudRun](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupCloudRun)` |   
  
### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

Output only. [Output Only] Creation timestamp inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultPort
    
    
    public int DefaultPort { get; set; }

The default port used if the port number is not specified in the network endpoint.

Optional. If the network endpoint type is either GCE_VM_IP,SERVERLESS or PRIVATE_SERVICE_CONNECT, this field must not be specified.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Description
    
    
    public string Description { get; set; }

An optional description of this resource. Provide this property when you create the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCreationTimestamp
    
    
    public bool HasCreationTimestamp { get; }

Gets whether the "creation_timestamp" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDefaultPort
    
    
    public bool HasDefaultPort { get; }

Gets whether the "default_port" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDescription
    
    
    public bool HasDescription { get; }

Gets whether the "description" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasId
    
    
    public bool HasId { get; }

Gets whether the "id" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasKind
    
    
    public bool HasKind { get; }

Gets whether the "kind" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasName
    
    
    public bool HasName { get; }

Gets whether the "name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNetwork
    
    
    public bool HasNetwork { get; }

Gets whether the "network" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasNetworkEndpointType
    
    
    public bool HasNetworkEndpointType { get; }

Gets whether the "network_endpoint_type" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPscTargetService
    
    
    public bool HasPscTargetService { get; }

Gets whether the "psc_target_service" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRegion
    
    
    public bool HasRegion { get; }

Gets whether the "region" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSelfLink
    
    
    public bool HasSelfLink { get; }

Gets whether the "self_link" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSize
    
    
    public bool HasSize { get; }

Gets whether the "size" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubnetwork
    
    
    public bool HasSubnetwork { get; }

Gets whether the "subnetwork" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasZone
    
    
    public bool HasZone { get; }

Gets whether the "zone" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Id
    
    
    public ulong Id { get; set; }

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] Type of the resource. Alwayscompute#networkEndpointGroup for network endpoint group.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType GCE_VM_IP_PORT,GCE_VM_IP_PORTMAP or NON_GCP_PRIVATE_IP_PORT, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set toSERVERLESS or PRIVATE_SERVICE_CONNECT and for global NEGs. For all other network endpoint types, this field is required.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkEndpointType
    
    
    public string NetworkEndpointType { get; set; }

Type of network endpoints in this network endpoint group. Can be one ofGCE_VM_IP, GCE_VM_IP_PORT,NON_GCP_PRIVATE_IP_PORT, INTERNET_FQDN_PORT,INTERNET_IP_PORT, SERVERLESS,PRIVATE_SERVICE_CONNECT, GCE_VM_IP_PORTMAP. Check the NetworkEndpointType enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PscData
    
    
    public NetworkEndpointGroupPscData PscData { get; set; }

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkEndpointGroupPscData](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupPscData)` |   
  
### PscTargetService
    
    
    public string PscTargetService { get; set; }

The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: asia-northeast3-cloudkms.googleapis.com.

Optional. Only valid when networkEndpointType isPRIVATE_SERVICE_CONNECT.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Region
    
    
    public string Region { get; set; }

Output only. [Output Only] The URL of theregion where the network endpoint group is located.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

Output only. [Output Only] Server-defined URL for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Size
    
    
    public int Size { get; set; }

Output only. [Output only] Number of network endpoints in the network endpoint group.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Subnetwork
    
    
    public string Subnetwork { get; set; }

Optional URL of the subnetwork to which all network endpoints in the NEG belong.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Zone
    
    
    public string Zone { get; set; }

Output only. [Output Only] The URL of thezone where the network endpoint group is located.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
