---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService
title: Compute Engine v1 API - Class BackendService (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:30.747140+00:00
---

# Compute Engine v1 API - Class BackendService (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class BackendService (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BackendService : IMessage<BackendService>, IEquatable<BackendService>, IDeepCloneable<BackendService>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class BackendService.

Represents a Backend Service resource.

A backend service defines how Google Cloud load balancers distribute traffic. The backend service configuration contains a set of values, such as the protocol used to connect to backends, various distribution and session settings, health checks, and timeouts. These settings provide fine-grained control over how your load balancer behaves. Most of the settings have default values that allow for easy configuration if you need to get started quickly.

Backend services in Google Compute Engine can be either regionally or globally scoped.

  * [Global](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices)
  * [Regional](https://cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices)



For more information, seeBackend Services.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackendService

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackendService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackendService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackendService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### BackendService()
    
    
    public BackendService()

### BackendService(BackendService)
    
    
    public BackendService(BackendService other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackendService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendService)`  
  
  
## Properties 

### AffinityCookieTtlSec
    
    
    public int AffinityCookieTtlSec { get; set; }

Lifetime of cookies in seconds. This setting is applicable to Application Load Balancers and Traffic Director and requires GENERATED_COOKIE or HTTP_COOKIE session affinity.

If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value is two weeks (1,209,600).

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Backends
    
    
    public RepeatedField<Backend> Backends { get; }

The list of backends that serve this BackendService.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Backend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Backend)` |   
  
### CdnPolicy
    
    
    public BackendServiceCdnPolicy CdnPolicy { get; set; }

Cloud CDN configuration for this BackendService. Only available for specified load balancer types.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceCdnPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceCdnPolicy)` |   
  
### CircuitBreakers
    
    
    public CircuitBreakers CircuitBreakers { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[CircuitBreakers](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CircuitBreakers)` |   
  
### CompressionMode
    
    
    public string CompressionMode { get; set; }

Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header. Check the CompressionMode enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConnectionDraining
    
    
    public ConnectionDraining ConnectionDraining { get; set; }

connectionDraining cannot be specified with haPolicy.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionDraining](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ConnectionDraining)` |   
  
### ConnectionTrackingPolicy
    
    
    public BackendServiceConnectionTrackingPolicy ConnectionTrackingPolicy { get; set; }

Connection Tracking configuration for this BackendService. Connection tracking policy settings are only available for external passthrough Network Load Balancers and internal passthrough Network Load Balancers.

connectionTrackingPolicy cannot be specified with haPolicy.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceConnectionTrackingPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceConnectionTrackingPolicy)` |   
  
### ConsistentHash
    
    
    public ConsistentHashLoadBalancerSettings ConsistentHash { get; set; }

Consistent Hash-based load balancing can be used to provide soft session affinity based on HTTP headers, cookies or other properties. This load balancing policy is applicable only for HTTP connections. The affinity to a particular destination host will be lost when one or more hosts are added/removed from the destination service. This field specifies parameters that control consistent hashing. This field is only applicable whenlocalityLbPolicy is set to MAGLEV orRING_HASH.

This field is applicable to either:

  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and load_balancing_scheme set to INTERNAL_MANAGED.
  * A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED.



**Property Value**  
---  
**Type** | **Description**  
`[ConsistentHashLoadBalancerSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ConsistentHashLoadBalancerSettings)` |   
  
### CreationTimestamp
    
    
    public string CreationTimestamp { get; set; }

Output only. [Output Only] Creation timestamp inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CustomMetrics
    
    
    public RepeatedField<BackendServiceCustomMetric> CustomMetrics { get; }

List of custom metrics that are used for theWEIGHTED_ROUND_ROBIN locality_lb_policy.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BackendServiceCustomMetric](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceCustomMetric)` |   
  
### CustomRequestHeaders
    
    
    public RepeatedField<string> CustomRequestHeaders { get; }

Headers that the load balancer adds to proxied requests. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CustomResponseHeaders
    
    
    public RepeatedField<string> CustomResponseHeaders { get; }

Headers that the load balancer adds to proxied responses. See [Creating custom headers](https://cloud.google.com/load-balancing/docs/custom-headers).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

An optional description of this resource. Provide this property when you create the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EdgeSecurityPolicy
    
    
    public string EdgeSecurityPolicy { get; set; }

[Output Only] The resource URL for the edge security policy associated with this backend service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableCDN
    
    
    public bool EnableCDN { get; set; }

If true, enables Cloud CDN for the backend service of a global external Application Load Balancer.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ExternalManagedMigrationState
    
    
    public string ExternalManagedMigrationState { get; set; }

Specifies the canary migration state. Possible values are PREPARE, TEST_BY_PERCENTAGE, and TEST_ALL_TRAFFIC.

To begin the migration from EXTERNAL to EXTERNAL_MANAGED, the state must be changed to PREPARE. The state must be changed to TEST_ALL_TRAFFIC before the loadBalancingScheme can be changed to EXTERNAL_MANAGED. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate traffic by percentage using externalManagedMigrationTestingPercentage.

Rolling back a migration requires the states to be set in reverse order. So changing the scheme from EXTERNAL_MANAGED to EXTERNAL requires the state to be set to TEST_ALL_TRAFFIC at the same time. Optionally, the TEST_BY_PERCENTAGE state can be used to migrate some traffic back to EXTERNAL or PREPARE can be used to migrate all traffic back to EXTERNAL. Check the ExternalManagedMigrationState enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExternalManagedMigrationTestingPercentage
    
    
    public float ExternalManagedMigrationTestingPercentage { get; set; }

Determines the fraction of requests that should be processed by the Global external Application Load Balancer.

The value of this field must be in the range [0, 100].

Session affinity options will slightly affect this routing behavior, for more details, see:Session Affinity.

This value can only be set if the loadBalancingScheme in the BackendService is set to EXTERNAL (when using the classic Application Load Balancer) and the migration state is TEST_BY_PERCENTAGE.

**Property Value**  
---  
**Type** | **Description**  
`[float](https://learn.microsoft.com/dotnet/api/system.single)` |   
  
### FailoverPolicy
    
    
    public BackendServiceFailoverPolicy FailoverPolicy { get; set; }

Requires at least one backend instance group to be defined as a backup (failover) backend. For load balancers that have configurable failover: [Internal passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/internal/failover-overview) and [external passthrough Network Load Balancers](https://cloud.google.com/load-balancing/docs/network/networklb-failover-overview). failoverPolicy cannot be specified with haPolicy.failoverPolicy cannot be used by global external Passthrough Network Load Balancers.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceFailoverPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceFailoverPolicy)` |   
  
### Fingerprint
    
    
    public string Fingerprint { get; set; }

Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a BackendService. An up-to-date fingerprint must be provided in order to update the BackendService, otherwise the request will fail with error 412 conditionNotMet.

To see the latest fingerprint, make a get() request to retrieve a BackendService.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HaPolicy
    
    
    public BackendServiceHAPolicy HaPolicy { get; set; }

Configures self-managed High Availability (HA) for External and Internal Protocol Forwarding.

The backends of this regional backend service must only specify zonal network endpoint groups (NEGs) of type GCE_VM_IP.

When haPolicy is set for an Internal Passthrough Network Load Balancer, the regional backend service must set the network field. All zonal NEGs must belong to the same network. However, individual NEGs can belong to different subnetworks of that network.

When haPolicy is specified, the set of attached network endpoints across all backends comprise an High Availability domain from which one endpoint is selected as the active endpoint (the leader) that receives all traffic.

haPolicy can be added only at backend service creation time. Once set up, it cannot be deleted.

Note that haPolicy is not for load balancing, and therefore cannot be specified with sessionAffinity, connectionTrackingPolicy, and failoverPolicy.

haPolicy requires customers to be responsible for tracking backend endpoint health and electing a leader among the healthy endpoints. Therefore, haPolicy cannot be specified with healthChecks. haPolicy can only be specified for External Passthrough Network Load Balancers and Internal Passthrough Network Load Balancers.haPolicy cannot be used by global external Passthrough Network Load Balancers.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceHAPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceHAPolicy)` |   
  
### HasAffinityCookieTtlSec
    
    
    public bool HasAffinityCookieTtlSec { get; }

Gets whether the "affinity_cookie_ttl_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCompressionMode
    
    
    public bool HasCompressionMode { get; }

Gets whether the "compression_mode" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCreationTimestamp
    
    
    public bool HasCreationTimestamp { get; }

Gets whether the "creation_timestamp" field is set

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
  
### HasEdgeSecurityPolicy
    
    
    public bool HasEdgeSecurityPolicy { get; }

Gets whether the "edge_security_policy" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasEnableCDN
    
    
    public bool HasEnableCDN { get; }

Gets whether the "enable_c_d_n" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExternalManagedMigrationState
    
    
    public bool HasExternalManagedMigrationState { get; }

Gets whether the "external_managed_migration_state" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExternalManagedMigrationTestingPercentage
    
    
    public bool HasExternalManagedMigrationTestingPercentage { get; }

Gets whether the "external_managed_migration_testing_percentage" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasFingerprint
    
    
    public bool HasFingerprint { get; }

Gets whether the "fingerprint" field is set

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
  
### HasIpAddressSelectionPolicy
    
    
    public bool HasIpAddressSelectionPolicy { get; }

Gets whether the "ip_address_selection_policy" field is set

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
  
### HasLoadBalancingScheme
    
    
    public bool HasLoadBalancingScheme { get; }

Gets whether the "load_balancing_scheme" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLocalityLbPolicy
    
    
    public bool HasLocalityLbPolicy { get; }

Gets whether the "locality_lb_policy" field is set

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
  
### HasPort
    
    
    public bool HasPort { get; }

Gets whether the "port" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPortName
    
    
    public bool HasPortName { get; }

Gets whether the "port_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProtocol
    
    
    public bool HasProtocol { get; }

Gets whether the "protocol" field is set

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
  
### HasSecurityPolicy
    
    
    public bool HasSecurityPolicy { get; }

Gets whether the "security_policy" field is set

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
  
### HasServiceLbPolicy
    
    
    public bool HasServiceLbPolicy { get; }

Gets whether the "service_lb_policy" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSessionAffinity
    
    
    public bool HasSessionAffinity { get; }

Gets whether the "session_affinity" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTimeoutSec
    
    
    public bool HasTimeoutSec { get; }

Gets whether the "timeout_sec" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HealthChecks
    
    
    public RepeatedField<string> HealthChecks { get; }

The list of URLs to the healthChecks, httpHealthChecks (legacy), or httpsHealthChecks (legacy) resource for health checking this backend service. Not all backend services support legacy health checks. See Load balancer guide. Currently, at most one health check can be specified for each backend service. Backend services with instance group or zonal NEG backends must have a health check unless haPolicy is specified. Backend services with internet or serverless NEG backends must not have a health check.

healthChecks[] cannot be specified with haPolicy.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Iap
    
    
    public BackendServiceIAP Iap { get; set; }

The configurations for Identity-Aware Proxy on this resource. Not available for internal passthrough Network Load Balancers and external passthrough Network Load Balancers.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceIAP](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceIAP)` |   
  
### Id
    
    
    public ulong Id { get; set; }

[Output Only] The unique identifier for the resource. This identifier is defined by the server.

**Property Value**  
---  
**Type** | **Description**  
`[ulong](https://learn.microsoft.com/dotnet/api/system.uint64)` |   
  
### IpAddressSelectionPolicy
    
    
    public string IpAddressSelectionPolicy { get; set; }

Specifies a preference for traffic sent from the proxy to the backend (or from the client to the backend for proxyless gRPC). The possible values are:

  * IPV4_ONLY: Only send IPv4 traffic to the backends of the backend service (Instance Group, Managed Instance Group, Network Endpoint Group), regardless of traffic from the client to the proxy. Only IPv4 health checks are used to check the health of the backends. This is the default setting.
  * PREFER_IPV6: Prioritize the connection to the endpoint's IPv6 address over its IPv4 address (provided there is a healthy IPv6 address).
  * IPV6_ONLY: Only send IPv6 traffic to the backends of the backend service (Instance Group, Managed Instance Group, Network Endpoint Group), regardless of traffic from the client to the proxy. Only IPv6 health checks are used to check the health of the backends.



This field is applicable to either:

  * Advanced global external Application Load Balancer (load balancing scheme EXTERNAL_MANAGED),
  * Regional external Application Load Balancer,
  * Internal proxy Network Load Balancer (load balancing scheme INTERNAL_MANAGED),
  * Regional internal Application Load Balancer (load balancing scheme INTERNAL_MANAGED),
  * Traffic Director with Envoy proxies and proxyless gRPC (load balancing scheme INTERNAL_SELF_MANAGED). Check the IpAddressSelectionPolicy enum for the list of possible values.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Kind
    
    
    public string Kind { get; set; }

Output only. [Output Only] Type of resource. Always compute#backendService for backend services.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LoadBalancingScheme
    
    
    public string LoadBalancingScheme { get; set; }

Specifies the load balancer type. A backend service created for one type of load balancer cannot be used with another. For more information, refer to Backend services product and scheme table. Check the LoadBalancingScheme enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocalityLbPolicies
    
    
    public RepeatedField<BackendServiceLocalityLoadBalancingPolicyConfig> LocalityLbPolicies { get; }

A list of locality load-balancing policies to be used in order of preference. When you use localityLbPolicies, you must set at least one value for either the localityLbPolicies[].policy or the localityLbPolicies[].customPolicy field. localityLbPolicies overrides any value set in the localityLbPolicy field.

For an example of how to use this field, seeDefine a list of preferred policies.

Caution: This field and its children are intended for use in a service mesh that includes gRPC clients only. Envoy proxies can't use backend services that have this configuration.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BackendServiceLocalityLoadBalancingPolicyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceLocalityLoadBalancingPolicyConfig)` |   
  
### LocalityLbPolicy
    
    
    public string LocalityLbPolicy { get; set; }

The load balancing algorithm used within the scope of the locality. The possible values are:

  * ROUND_ROBIN: This is a simple policy in which each healthy backend is selected in round robin order. This is the default.
  * LEAST_REQUEST: An O(1) algorithm which selects two random healthy hosts and picks the host which has fewer active requests.
  * RING_HASH: The ring/modulo hash load balancer implements consistent hashing to backends. The algorithm has the property that the addition/removal of a host from a set of N hosts only affects 1/N of the requests.
  * RANDOM: The load balancer selects a random healthy host.
  * ORIGINAL_DESTINATION: Backend host is selected based on the client connection metadata, i.e., connections are opened to the same address as the destination address of the incoming connection before the connection was redirected to the load balancer.
  * MAGLEV: used as a drop in replacement for the ring hash load balancer. Maglev is not as stable as ring hash but has faster table lookup build times and host selection times. For more information about Maglev, see Maglev: A Fast and Reliable Software Network Load Balancer.
  * WEIGHTED_ROUND_ROBIN: Per-endpoint Weighted Round Robin Load Balancing using weights computed from Backend reported Custom Metrics. If set, the Backend Service responses are expected to contain non-standard HTTP response header field Endpoint-Load-Metrics. The reported metrics to use for computing the weights are specified via thecustomMetrics field.
  * WEIGHTED_MAGLEV: Per-endpoint weighted load balancing via health check reported weights. If set, the backend service must configure an HTTP-based Health Check, and health check replies are expected to contain the non-standard HTTP response header fieldX-Load-Balancing-Endpoint-Weight to specify the per-endpoint weights. If set, load balancing is weighted based on the per-endpoint weights reported in the last processed health check replies, as long as every instance either reported a valid weight or had UNAVAILABLE_WEIGHT. Otherwise, load balancing remains equal-weight.



This field is applicable to either:

  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and load_balancing_scheme set to INTERNAL_MANAGED.
  * A global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED, INTERNAL_MANAGED, or EXTERNAL_MANAGED.



If sessionAffinity is not configured—that is, if session affinity remains at the default value of NONE—then the default value for localityLbPolicy is ROUND_ROBIN. If session affinity is set to a value other than NONE, then the default value for localityLbPolicy isMAGLEV.

Only ROUND_ROBIN and RING_HASH are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.

localityLbPolicy cannot be specified with haPolicy. Check the LocalityLbPolicy enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LogConfig
    
    
    public BackendServiceLogConfig LogConfig { get; set; }

This field denotes the logging options for the load balancer traffic served by this backend service. If logging is enabled, logs will be exported to Stackdriver.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceLogConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceLogConfig)` |   
  
### MaxStreamDuration
    
    
    public Duration MaxStreamDuration { get; set; }

Specifies the default maximum duration (timeout) for streams to this service. Duration is computed from the beginning of the stream until the response has been completely processed, including all retries. A stream that does not complete in this duration is closed.

If not specified, there will be no timeout limit, i.e. the maximum duration is infinite.

This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service.

This field is only allowed when the loadBalancingScheme of the backend service is INTERNAL_SELF_MANAGED.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Duration)` |   
  
### Metadatas
    
    
    public MapField<string, string> Metadatas { get; }

Deployment metadata associated with the resource to be set by a GKE hub controller and read by the backend RCTH

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    public string Network { get; set; }

The URL of the network to which this backend service belongs.

This field must be set for Internal Passthrough Network Load Balancers when the haPolicy is enabled, and for External Passthrough Network Load Balancers when the haPolicy fastIpMove is enabled.

This field can only be specified when the load balancing scheme is set toINTERNAL, or when the load balancing scheme is set toEXTERNAL and haPolicy fastIpMove is enabled.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkPassThroughLbTrafficPolicy
    
    
    public BackendServiceNetworkPassThroughLbTrafficPolicy NetworkPassThroughLbTrafficPolicy { get; set; }

Configures traffic steering properties of internal passthrough Network Load Balancers.

networkPassThroughLbTrafficPolicy cannot be specified with haPolicy.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceNetworkPassThroughLbTrafficPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceNetworkPassThroughLbTrafficPolicy)` |   
  
### OrchestrationInfo
    
    
    public BackendServiceOrchestrationInfo OrchestrationInfo { get; set; }

Information about the resource or system that manages the backend service.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceOrchestrationInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceOrchestrationInfo)` |   
  
### OutlierDetection
    
    
    public OutlierDetection OutlierDetection { get; set; }

Settings controlling the ejection of unhealthy backend endpoints from the load balancing pool of each individual proxy instance that processes the traffic for the given backend service. If not set, this feature is considered disabled.

Results of the outlier detection algorithm (ejection of endpoints from the load balancing pool and returning them back to the pool) are executed independently by each proxy instance of the load balancer. In most cases, more than one proxy instance handles the traffic received by a backend service. Thus, it is possible that an unhealthy endpoint is detected and ejected by only some of the proxies, and while this happens, other proxies may continue to send requests to the same unhealthy endpoint until they detect and eject the unhealthy endpoint.

Applicable backend endpoints can be:

  * VM instances in an Instance Group
  * Endpoints in a Zonal NEG (GCE_VM_IP, GCE_VM_IP_PORT)
  * Endpoints in a Hybrid Connectivity NEG (NON_GCP_PRIVATE_IP_PORT)
  * Serverless NEGs, that resolve to Cloud Run, App Engine, or Cloud Functions Services
  * Private Service Connect NEGs, that resolve to Google-managed regional API endpoints or managed services published using Private Service Connect



Applicable backend service types can be:

  * A global backend service with the loadBalancingScheme set to INTERNAL_SELF_MANAGED or EXTERNAL_MANAGED.
  * A regional backend service with the service protocol set to HTTP, HTTPS, HTTP2 or H2C, and loadBalancingScheme set to INTERNAL_MANAGED or EXTERNAL_MANAGED. Not supported for Serverless NEGs.



Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.

**Property Value**  
---  
**Type** | **Description**  
`[OutlierDetection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OutlierDetection)` |   
  
### Params
    
    
    public BackendServiceParams Params { get; set; }

Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceParams](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceParams)` |   
  
### Port
    
    
    public int Port { get; set; }

Deprecated in favor of portName. The TCP port to connect on the backend. The default value is 80. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit port.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PortName
    
    
    public string PortName { get; set; }

A named port on a backend instance group representing the port for communication to the backend VMs in that group. The named port must be [defined on each backend instance group](https://cloud.google.com/load-balancing/docs/backend-service#named_ports). This parameter has no meaning if the backends are NEGs. For internal passthrough Network Load Balancers and external passthrough Network Load Balancers, omit port_name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Protocol
    
    
    public string Protocol { get; set; }

The protocol this BackendService uses to communicate with backends.

Possible values are HTTP, HTTPS, HTTP2, H2C, TCP, SSL, UDP, GRPC, or UNSPECIFIED, depending on the chosen load balancer or Traffic Director configuration. Refer to Load balancing features for more information.

Must be set to GRPC when the backend service is referenced by a URL map that is bound to target gRPC proxy. Check the Protocol enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Region
    
    
    public string Region { get; set; }

Output only. [Output Only] URL of the region where the regional backend service resides. This field is not applicable to global backend services. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecurityPolicy
    
    
    public string SecurityPolicy { get; set; }

[Output Only] The resource URL for the security policy associated with this backend service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecuritySettings
    
    
    public SecuritySettings SecuritySettings { get; set; }

This field specifies the security settings that apply to this backend service. This field is applicable to a global backend service with the load_balancing_scheme set to INTERNAL_SELF_MANAGED.

**Property Value**  
---  
**Type** | **Description**  
`[SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecuritySettings)` |   
  
### SelfLink
    
    
    public string SelfLink { get; set; }

[Output Only] Server-defined URL for the resource.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceBindings
    
    
    public RepeatedField<string> ServiceBindings { get; }

URLs of networkservices.ServiceBinding resources.

Can only be set if load balancing scheme is INTERNAL_SELF_MANAGED. If set, lists of backends and health checks must be both empty.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceLbPolicy
    
    
    public string ServiceLbPolicy { get; set; }

URL to networkservices.ServiceLbPolicy resource.

Can only be set if load balancing scheme is EXTERNAL_MANAGED, INTERNAL_MANAGED or INTERNAL_SELF_MANAGED for a global backend service, and EXTERNAL_MANAGED or INTERNAL_MANAGED for a regional backend service. For a global backend service, the service lb policy must be global. For a regional backend service, the service lb policy must be regional and in the same region.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SessionAffinity
    
    
    public string SessionAffinity { get; set; }

Type of session affinity to use. The default is NONE.

Only NONE and HEADER_FIELD are supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true.

For more details, see: [Session Affinity](https://cloud.google.com/load-balancing/docs/backend-service#session_affinity).

sessionAffinity cannot be specified with haPolicy. Check the SessionAffinity enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StrongSessionAffinityCookie
    
    
    public BackendServiceHttpCookie StrongSessionAffinityCookie { get; set; }

Describes the HTTP cookie used for stateful session affinity. This field is applicable and required if the sessionAffinity is set toSTRONG_COOKIE_AFFINITY.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceHttpCookie](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceHttpCookie)` |   
  
### Subsetting
    
    
    public Subsetting Subsetting { get; set; }

subsetting cannot be specified with haPolicy.

**Property Value**  
---  
**Type** | **Description**  
`[Subsetting](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.Subsetting)` |   
  
### TimeoutSec
    
    
    public int TimeoutSec { get; set; }

The backend service timeout has a different meaning depending on the type of load balancer. For more information see, Backend service settings. The default is 30 seconds. The full range of timeout values allowed goes from 1 through 2,147,483,647 seconds.

This value can be overridden in the PathMatcher configuration of the UrlMap that references this backend service.

Not supported when the backend service is referenced by a URL map that is bound to target gRPC proxy that has validateForProxyless field set to true. Instead, use maxStreamDuration.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### TlsSettings
    
    
    public BackendServiceTlsSettings TlsSettings { get; set; }

Configuration for Backend Authenticated TLS and mTLS. May only be specified when the backend protocol is SSL, HTTPS or HTTP2.

**Property Value**  
---  
**Type** | **Description**  
`[BackendServiceTlsSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceTlsSettings)` |   
  
### UsedBy
    
    
    public RepeatedField<BackendServiceUsedBy> UsedBy { get; }

Output only. [Output Only] List of resources referencing given backend service.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[BackendServiceUsedBy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServiceUsedBy)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
