---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend
title: Compute Engine v1 API - Class Backend (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:47.387602+00:00
---

# Compute Engine v1 API - Class Backend (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class Backend (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Backend : IMessage<Backend>, IEquatable<Backend>, IDeepCloneable<Backend>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class Backend.

Message containing information of one individual backend.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Backend

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### Backend()
    
    
    public Backend()

### Backend(Backend)
    
    
    public Backend(Backend other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend)`  
  
  
## Properties 

### BalancingMode
    
    
    public string BalancingMode { get; set; }

Specifies how to determine whether the backend of a load balancer can handle additional traffic or is fully loaded. For usage guidelines, see Connection balancing mode.

Backends must use compatible balancing modes. Backends of a backend service may use different balancing modes. For more information, see Supported balancing modes and target capacity settings and Restrictions and guidance for instance groups.

Note: Currently, if you use the API to configure incompatible balancing modes, the configuration might be accepted even though it has no impact and is ignored. Specifically, Backend.maxUtilization is ignored when Backend.balancingMode is RATE. In the future, this incompatible combination will be rejected. Check the BalancingMode enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CapacityScaler
    
    
    public float CapacityScaler { get; set; }

A multiplier applied to the backend's target capacity of its balancing mode. The default value is 1, which means the group serves up to 100% of its configured capacity (depending onbalancingMode). A setting of 0 means the group is completely drained, offering 0% of its available capacity. The valid ranges are 0.0 and [0.1,1.0]. You cannot configure a setting larger than 0 and smaller than0.1. You cannot configure a setting of 0 when there is only one backend attached to the backend service.

Not available with backends that don't support using abalancingMode. This includes backends such as global internet NEGs, regional serverless NEGs, and PSC NEGs.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### CustomMetrics
    
    
    public RepeatedField<BackendCustomMetric> CustomMetrics { get; }

List of custom metrics that are used for CUSTOM_METRICS BalancingMode.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BackendCustomMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendCustomMetric)` |   
  
### Description
    
    
    public string Description { get; set; }

An optional description of this resource. Provide this property when you create the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Failover
    
    
    public bool Failover { get; set; }

This field designates whether this is a failover backend. More than one failover backend can be configured for a given BackendService.

This field can only be used for a regional external Passthrough Network Load Balancer or a regional internal Passthrough Network Load Balancer.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Group
    
    
    public string Group { get; set; }

The fully-qualified URL of aninstance group or network endpoint group (NEG) resource. To determine what types of backends a load balancer supports, see the [Backend services overview](https://cloud.google.com/load-balancing/docs/backend-service#backends).

You must use the _fully-qualified_ URL (starting withhttps://www.googleapis.com/) to specify the instance group or NEG. Partial URLs are not supported.

If haPolicy is specified, backends must refer to NEG resources of type GCE_VM_IP.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasBalancingMode
    
    
    public bool HasBalancingMode { get; }

Gets whether the "balancing_mode" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCapacityScaler
    
    
    public bool HasCapacityScaler { get; }

Gets whether the "capacity_scaler" field is set

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
  
### HasFailover
    
    
    public bool HasFailover { get; }

Gets whether the "failover" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasGroup
    
    
    public bool HasGroup { get; }

Gets whether the "group" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxConnections
    
    
    public bool HasMaxConnections { get; }

Gets whether the "max_connections" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxConnectionsPerEndpoint
    
    
    public bool HasMaxConnectionsPerEndpoint { get; }

Gets whether the "max_connections_per_endpoint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxConnectionsPerInstance
    
    
    public bool HasMaxConnectionsPerInstance { get; }

Gets whether the "max_connections_per_instance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxInFlightRequests
    
    
    public bool HasMaxInFlightRequests { get; }

Gets whether the "max_in_flight_requests" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxInFlightRequestsPerEndpoint
    
    
    public bool HasMaxInFlightRequestsPerEndpoint { get; }

Gets whether the "max_in_flight_requests_per_endpoint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxInFlightRequestsPerInstance
    
    
    public bool HasMaxInFlightRequestsPerInstance { get; }

Gets whether the "max_in_flight_requests_per_instance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxRate
    
    
    public bool HasMaxRate { get; }

Gets whether the "max_rate" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxRatePerEndpoint
    
    
    public bool HasMaxRatePerEndpoint { get; }

Gets whether the "max_rate_per_endpoint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxRatePerInstance
    
    
    public bool HasMaxRatePerInstance { get; }

Gets whether the "max_rate_per_instance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxUtilization
    
    
    public bool HasMaxUtilization { get; }

Gets whether the "max_utilization" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPreference
    
    
    public bool HasPreference { get; }

Gets whether the "preference" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTrafficDuration
    
    
    public bool HasTrafficDuration { get; }

Gets whether the "traffic_duration" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MaxConnections
    
    
    public int MaxConnections { get; set; }

Defines a target maximum number of simultaneous connections. For usage guidelines, seeConnection balancing mode and Utilization balancing mode. Not available if the backend'sbalancingMode is RATE.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxConnectionsPerEndpoint
    
    
    public int MaxConnectionsPerEndpoint { get; set; }

Defines a target maximum number of simultaneous connections. For usage guidelines, seeConnection balancing mode and Utilization balancing mode.

Not available if the backend's balancingMode isRATE.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxConnectionsPerInstance
    
    
    public int MaxConnectionsPerInstance { get; set; }

Defines a target maximum number of simultaneous connections. For usage guidelines, seeConnection balancing mode and Utilization balancing mode.

Not available if the backend's balancingMode isRATE.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxInFlightRequests
    
    
    public int MaxInFlightRequests { get; set; }

Defines a maximum number of in-flight requests for the whole NEG or instance group. Not available if backend's balancingMode isRATE or CONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxInFlightRequestsPerEndpoint
    
    
    public int MaxInFlightRequestsPerEndpoint { get; set; }

Defines a maximum number of in-flight requests for a single endpoint. Not available if backend's balancingMode is RATE or CONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxInFlightRequestsPerInstance
    
    
    public int MaxInFlightRequestsPerInstance { get; set; }

Defines a maximum number of in-flight requests for a single VM. Not available if backend's balancingMode is RATE or CONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxRate
    
    
    public int MaxRate { get; set; }

Defines a maximum number of HTTP requests per second (RPS). For usage guidelines, seeRate balancing mode and Utilization balancing mode.

Not available if the backend's balancingMode isCONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxRatePerEndpoint
    
    
    public float MaxRatePerEndpoint { get; set; }

Defines a maximum target for requests per second (RPS). For usage guidelines, seeRate balancing mode and Utilization balancing mode.

Not available if the backend's balancingMode isCONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### MaxRatePerInstance
    
    
    public float MaxRatePerInstance { get; set; }

Defines a maximum target for requests per second (RPS). For usage guidelines, seeRate balancing mode and Utilization balancing mode.

Not available if the backend's balancingMode isCONNECTION.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### MaxUtilization
    
    
    public float MaxUtilization { get; set; }

Optional parameter to define a target capacity for theUTILIZATION balancing mode. The valid range is[0.0, 1.0].

For usage guidelines, seeUtilization balancing mode.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### OrchestrationInfo
    
    
    public BackendBackendOrchestrationInfo OrchestrationInfo { get; set; }

Information about the resource or system that manages the backend.

**Property Value**  
---  
**Type** | **Description**  
`[BackendBackendOrchestrationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBackendOrchestrationInfo)` |   
  
### Preference
    
    
    public string Preference { get; set; }

This field indicates whether this backend should be fully utilized before sending traffic to backends with default preference. The possible values are:

  * PREFERRED: Backends with this preference level will be filled up to their capacity limits first, based on RTT.
  * DEFAULT: If preferred backends don't have enough capacity, backends in this layer would be used and traffic would be assigned based on the load balancing algorithm you use. This is the default



For global external Passthrough Network Load Balancers, the following restrictions apply:

  * At most one backend can be marked as PREFERRED.
  * PREFERRED and DEFAULT backends cannot reside in the same Cloud region. Check the Preference enum for the list of possible values.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TrafficDuration
    
    
    public string TrafficDuration { get; set; }

Check the TrafficDuration enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
