---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests
title: REST Resource: projects.locations.global.connectivityTests \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:27.812777+00:00
---

# REST Resource: projects.locations.global.connectivityTests  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.global.connectivityTests Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConnectivityTest
    * JSON representation
  * Endpoint
    * JSON representation
  * ForwardingRuleTarget
  * LoadBalancerType
  * CloudFunctionEndpoint
    * JSON representation
  * AppEngineVersionEndpoint
    * JSON representation
  * CloudRunRevisionEndpoint
    * JSON representation
  * NetworkType
  * ReachabilityDetails
    * JSON representation
  * Result
  * Trace
    * JSON representation
  * EndpointInfo
    * JSON representation
  * Step
    * JSON representation
  * State
  * InstanceInfo
    * JSON representation
  * Status
  * FirewallInfo
    * JSON representation
  * FirewallRuleType
  * TargetType
  * RouteInfo
    * JSON representation
  * RouteType
  * NextHopType
  * RouteScope
  * GoogleServiceInfo
    * JSON representation
  * GoogleServiceType
  * ForwardingRuleInfo
    * JSON representation
  * HybridSubnetInfo
    * JSON representation
  * VpnGatewayInfo
    * JSON representation
  * VpnTunnelInfo
    * JSON representation
  * RoutingType
  * InterconnectAttachmentInfo
    * JSON representation
  * Type
  * VpcConnectorInfo
    * JSON representation
  * DirectVpcEgressConnectionInfo
    * JSON representation
  * ServerlessExternalConnectionInfo
    * JSON representation
  * DeliverInfo
    * JSON representation
  * Target
  * GoogleServiceType
  * ForwardInfo
    * JSON representation
  * Target
  * AbortInfo
    * JSON representation
  * Cause
  * DropInfo
    * JSON representation
  * Cause
  * LoadBalancerInfo
    * JSON representation
  * LoadBalancerType
  * LoadBalancerBackend
    * JSON representation
  * HealthCheckFirewallState
  * BackendType
  * NetworkInfo
    * JSON representation
  * GKEMasterInfo
    * JSON representation
  * GkePodInfo
    * JSON representation
  * IpMasqueradingSkippedInfo
    * JSON representation
  * Reason
  * GkeNetworkPolicyInfo
    * JSON representation
  * GkeNetworkPolicySkippedInfo
    * JSON representation
  * Reason
  * CloudSQLInstanceInfo
    * JSON representation
  * RedisInstanceInfo
    * JSON representation
  * RedisClusterInfo
    * JSON representation
  * CloudFunctionInfo
    * JSON representation
  * AppEngineVersionInfo
    * JSON representation
  * CloudRunRevisionInfo
    * JSON representation
  * CloudRunJobInfo
    * JSON representation
  * NatInfo
    * JSON representation
  * Type
  * CloudNatGatewayType
  * ProxyConnectionInfo
    * JSON representation
  * LoadBalancerBackendInfo
    * JSON representation
  * HealthCheckFirewallsConfigState
  * StorageBucketInfo
    * JSON representation
  * ServerlessNegInfo
    * JSON representation
  * NgfwPacketInspectionInfo
    * JSON representation
  * PrivateConnectionInfo
    * JSON representation
  * ProbingDetails
    * JSON representation
  * ProbingResult
  * ProbingAbortCause
  * LatencyDistribution
    * JSON representation
  * LatencyPercentile
    * JSON representation
  * EdgeLocation
    * JSON representation
  * SingleEdgeResponse
    * JSON representation
  * Methods



## Resource: ConnectivityTest

A Connectivity Test for a network reachability analysis.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "source": {
        object ([Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint))
      },
      "destination": {
        object ([Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint))
      },
      "protocol": string,
      "relatedProjects": [
        string
      ],
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "reachabilityDetails": {
        object ([ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ReachabilityDetails))
      },
      "probingDetails": {
        object ([ProbingDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingDetails))
      },
      "roundTrip": boolean,
      "returnReachabilityDetails": {
        object ([ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ReachabilityDetails))
      },
      "bypassFirewallChecks": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the resource using the form: `projects/{projectId}/locations/global/connectivityTests/{testId}`  
`description` |  `string` The user-supplied description of the Connectivity Test. Maximum of 512 characters.  
`source` |  `object (`[Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint)`)` Required. Source specification of the Connectivity Test.You can use a combination of source IP address, URI of a supported endpoint, project ID, or VPC network to identify the source location.Reachability analysis might proceed even if the source location is ambiguous. However, the test result might include endpoints or use a source that you don't intend to test.  
`destination` |  `object (`[Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint)`)` Required. Destination specification of the Connectivity Test.You can use a combination of destination IP address, URI of a supported endpoint, project ID, or VPC network to identify the destination location.Reachability analysis proceeds even if the destination location is ambiguous. However, the test result might include endpoints or use a destination that you don't intend to test.  
`protocol` |  `string` IP Protocol of the test. When not provided, "TCP" is assumed.  
`relatedProjects[]` |  `string` Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries.  
`displayName` |  `string` Output only. The display name of a Connectivity Test.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the test was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the test's configuration was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`reachabilityDetails` |  `object (`[ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ReachabilityDetails)`)` Output only. The reachability details of this test from the latest run. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`probingDetails` |  `object (`[ProbingDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingDetails)`)` Output only. The probing details of this test from the latest run, present for applicable tests only. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`roundTrip` |  `boolean` Whether run analysis for the return path from destination to source. Default value is false.  
`returnReachabilityDetails` |  `object (`[ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ReachabilityDetails)`)` Output only. The reachability details of this test from the latest run for the return path. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`bypassFirewallChecks` |  `boolean` Whether the analysis should skip firewall checking. Default value is false.  
  
## Endpoint

Source or destination of the Connectivity Test.

JSON representation  
---  
      
    
    {
      "ipAddress": string,
      "port": integer,
      "instance": string,
      "forwardingRule": string,
      "gkeMasterCluster": string,
      "fqdn": string,
      "cloudSqlInstance": string,
      "redisInstance": string,
      "redisCluster": string,
      "gkePod": string,
      "dmsPrivateConnection": string,
      "cloudFunction": {
        object ([CloudFunctionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudFunctionEndpoint))
      },
      "appEngineVersion": {
        object ([AppEngineVersionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AppEngineVersionEndpoint))
      },
      "cloudRunRevision": {
        object ([CloudRunRevisionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunRevisionEndpoint))
      },
      "cloudRunJob": string,
      "network": string,
      "networkType": enum ([NetworkType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NetworkType)),
      "projectId": string,
      "forwardingRuleTarget": enum ([ForwardingRuleTarget](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardingRuleTarget)),
      "loadBalancerId": string,
      "loadBalancerType": enum ([LoadBalancerType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerType))
    }  
  
Fields  
---  
`ipAddress` |  `string` The IP address of the endpoint, which can be an external or internal IP.  
`port` |  `integer` The IP protocol port of the endpoint. Only applicable when protocol is TCP or UDP.  
`instance` |  `string` A Compute Engine instance URI.  
`forwardingRule` |  `string` A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Applicable only to destination endpoint. Format: `projects/{project}/global/forwardingRules/{id}` or `projects/{project}/regions/{region}/forwardingRules/{id}`  
`gkeMasterCluster` |  `string` A cluster URI for [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).  
`fqdn` |  `string` DNS endpoint of [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Requires gkeMasterCluster to be set, can't be used simultaneoulsly with ipAddress or network. Applicable only to destination endpoint.  
`cloudSqlInstance` |  `string` A [Cloud SQL](https://cloud.google.com/sql) instance URI.  
`redisInstance` |  `string` A [Redis Instance](https://cloud.google.com/memorystore/docs/redis) URI. Applicable only to destination endpoint.  
`redisCluster` |  `string` A [Redis Cluster](https://cloud.google.com/memorystore/docs/cluster) URI. Applicable only to destination endpoint.  
`gkePod` |  `string` A [GKE Pod](https://cloud.google.com/kubernetes-engine/docs/concepts/pod) URI.  
`dmsPrivateConnection` |  `string` A [DMS Private Connection](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections) name format: projects/{project}/locations/{location}/privateConnections/{privateConnection}.  
`cloudFunction` |  `object (`[CloudFunctionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudFunctionEndpoint)`)` A [Cloud Function](https://cloud.google.com/functions). Applicable only to source endpoint.  
`appEngineVersion` |  `object (`[AppEngineVersionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AppEngineVersionEndpoint)`)` An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions). Applicable only to source endpoint.  
`cloudRunRevision` |  `object (`[CloudRunRevisionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunRevisionEndpoint)`)` A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) Applicable only to source endpoint.  
`cloudRunJob` |  `string` A [Cloud Run](https://cloud.google.com/run) [job](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs#Job) URI. Applicable only to source endpoint. The format is: projects/{project}/locations/{location}/jobs/{job}  
`network` |  `string` A VPC network URI. For source endpoints, used according to the `networkType`. For destination endpoints, used only when the source is an external IP address endpoint, and the destination is an internal IP address endpoint.  
`networkType` |  `enum (`[NetworkType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NetworkType)`)` For source endpoints, type of the network where the endpoint is located. Not relevant for destination endpoints.  
`projectId` |  `string` For source endpoints, endpoint project ID. Used according to the `networkType`. Not relevant for destination endpoints.  
`forwardingRuleTarget` |  `enum (`[ForwardingRuleTarget](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardingRuleTarget)`)` Output only. Specifies the type of the target of the forwarding rule.  
`loadBalancerId` |  `string` Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers.  
`loadBalancerType` |  `enum (`[LoadBalancerType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerType)`)` Output only. Type of the load balancer the forwarding rule points to.  
  
## ForwardingRuleTarget

Type of the target of a forwarding rule.

Enums  
---  
`FORWARDING_RULE_TARGET_UNSPECIFIED` | Forwarding rule target is unknown.  
`INSTANCE` | Compute Engine instance for protocol forwarding.  
`LOAD_BALANCER` | Load Balancer. The specific type can be found from `[loadBalancerType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Endpoint.FIELDS.load_balancer_type)`.  
`VPN_GATEWAY` | Classic Cloud VPN Gateway.  
`PSC` | Forwarding Rule is a Private Service Connect endpoint.  
  
## LoadBalancerType

Type of a load balancer. For more information, see [Summary of Google Cloud load balancers](https://cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers).

Enums  
---  
`LOAD_BALANCER_TYPE_UNSPECIFIED` | Forwarding rule points to a different target than a load balancer or a load balancer type is unknown.  
`HTTPS_ADVANCED_LOAD_BALANCER` | Global external HTTP(S) load balancer.  
`HTTPS_LOAD_BALANCER` | Global external HTTP(S) load balancer (classic)  
`REGIONAL_HTTPS_LOAD_BALANCER` | Regional external HTTP(S) load balancer.  
`INTERNAL_HTTPS_LOAD_BALANCER` | Internal HTTP(S) load balancer.  
`SSL_PROXY_LOAD_BALANCER` | External SSL proxy load balancer.  
`TCP_PROXY_LOAD_BALANCER` | External TCP proxy load balancer.  
`INTERNAL_TCP_PROXY_LOAD_BALANCER` | Internal regional TCP proxy load balancer.  
`NETWORK_LOAD_BALANCER` | External TCP/UDP Network load balancer.  
`LEGACY_NETWORK_LOAD_BALANCER` | Target-pool based external TCP/UDP Network load balancer.  
`TCP_UDP_INTERNAL_LOAD_BALANCER` | Internal TCP/UDP load balancer.  
  
## CloudFunctionEndpoint

Wrapper for Cloud Function attributes.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` A [Cloud Function](https://cloud.google.com/functions) name.  
  
## AppEngineVersionEndpoint

Wrapper for the App Engine service version attributes.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions) name.  
  
## CloudRunRevisionEndpoint

Wrapper for Cloud Run revision attributes.

JSON representation  
---  
      
    
    {
      "uri": string,
      "serviceUri": string
    }  
  
Fields  
---  
`uri` |  `string` A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) URI. The format is: projects/{project}/locations/{location}/revisions/{revision}  
`serviceUri` |  `string` Output only. The URI of the Cloud Run service that the revision belongs to. The format is: projects/{project}/locations/{location}/services/{service}  
  
## NetworkType

The type of the network of the IP address endpoint. Relevant for the source IP address endpoints.

Enums  
---  
`NETWORK_TYPE_UNSPECIFIED` | Unspecified. The test will analyze all possible IP address locations. This might take longer and produce inaccurate or ambiguous results, so prefer specifying an explicit network type.The `projectId` field should be set to the project where the GCP endpoint is located, or where the non-GCP endpoint should be reachable from (via routes to non-GCP networks). The project might also be inferred from the Connectivity Test project or other projects referenced in the request.  
`GCP_NETWORK` | A VPC network. Should be used for internal IP addresses in VPC networks. The `network` field should be set to the URI of this network. Only endpoints within this network will be considered.  
`NON_GCP_NETWORK` | A non-GCP network (for example, an on-premises network or another cloud provider network). Should be used for internal IP addresses outside of Google Cloud. The `network` field should be set to the URI of the VPC network containing a corresponding Cloud VPN tunnel, Cloud Interconnect VLAN attachment, or a router appliance instance. Only endpoints reachable from the provided VPC network via the routes to non-GCP networks will be considered.  
`INTERNET` | Internet. Should be used for internet-routable external IP addresses or IP addresses for global Google APIs and services.  
  
## ReachabilityDetails

Results of the configuration analysis from the last run of the test.

JSON representation  
---  
      
    
    {
      "result": enum ([Result](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Result)),
      "verifyTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "traces": [
        {
          object ([Trace](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Trace))
        }
      ]
    }  
  
Fields  
---  
`result` |  `enum (`[Result](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Result)`)` The overall result of the test's configuration analysis.  
`verifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time of the configuration analysis.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/Shared.Types/ListOperationsResponse#Status)`)` The details of a failure or a cancellation of reachability analysis.  
`traces[]` |  `object (`[Trace](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Trace)`)` Result may contain a list of traces if a test has multiple possible paths in the network, such as when destination endpoint is a load balancer with multiple backends.  
  
## Result

The overall result of the test's configuration analysis.

Enums  
---  
`RESULT_UNSPECIFIED` | No result was specified.  
`REACHABLE` | Possible scenarios are:

  * The configuration analysis determined that a packet originating from the source is expected to reach the destination.
  * The analysis didn't complete because the user lacks permission for some of the resources in the trace. However, at the time the user's permission became insufficient, the trace had been successful so far.

  
`UNREACHABLE` | A packet originating from the source is expected to be dropped before reaching the destination.  
`AMBIGUOUS` | The source and destination endpoints do not uniquely identify the test location in the network, and the reachability result contains multiple traces. For some traces, a packet could be delivered, and for others, it would not be. This result is also assigned to configuration analysis of return path if on its own it should be REACHABLE, but configuration analysis of forward path is AMBIGUOUS.  
`UNDETERMINED` | The configuration analysis did not complete. Possible reasons are:

  * A permissions error occurred--for example, the user might not have read permission for all of the resources named in the test.
  * An internal error occurred.
  * The analyzer received an invalid or unsupported argument or was unable to identify a known endpoint.

  
  
## Trace

Trace represents one simulated packet forwarding path.

  * Each trace contains multiple ordered steps.
  * Each step is in a particular state with associated configuration.
  * State is categorized as final or non-final states.
  * Each final state has a reason associated.
  * Each trace must end with a final state (the last step).


    
    
      |---------------------Trace----------------------|
      Step1(State) Step2(State) ---  StepN(State(final))
    

JSON representation  
---  
      
    
    {
      "endpointInfo": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo))
      },
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Step))
        }
      ],
      "forwardTraceId": integer
    }  
  
Fields  
---  
`endpointInfo` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo)`)` Derived from the source and destination endpoints definition specified by user request, and validated by the data plane model. If there are multiple traces starting from different source locations, then the endpointInfo may be different between traces.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Step)`)` A trace of a test contains multiple steps from the initial state to the final state (delivered, dropped, forwarded, or aborted).The steps are ordered by the processing sequence within the simulated network state machine. It is critical to preserve the order of the steps and avoid reordering or sorting them.  
`forwardTraceId` |  `integer` ID of trace. For forward traces, this ID is unique for each trace. For return traces, it matches ID of associated forward trace. A single forward trace can be associated with none, one or more than one return trace.  
  
## EndpointInfo

For display only. The specification of the endpoints for the test. EndpointInfo is derived from source and destination Endpoint and validated by the backend data plane model.

JSON representation  
---  
      
    
    {
      "sourceIp": string,
      "destinationIp": string,
      "protocol": string,
      "sourcePort": integer,
      "destinationPort": integer,
      "sourceNetworkUri": string,
      "destinationNetworkUri": string,
      "sourceAgentUri": string
    }  
  
Fields  
---  
`sourceIp` |  `string` Source IP address.  
`destinationIp` |  `string` Destination IP address.  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`sourcePort` |  `integer` Source port. Only valid when protocol is TCP or UDP.  
`destinationPort` |  `integer` Destination port. Only valid when protocol is TCP or UDP.  
`sourceNetworkUri` |  `string` URI of the network where this packet originates from. Format: `projects/{projectId}/global/networks/{network_id}`  
`destinationNetworkUri` |  `string` URI of the network where this packet is sent to. Format: `projects/{projectId}/global/networks/{network_id}`  
`sourceAgentUri` |  `string` URI of the source telemetry agent this packet originates from.  
  
## Step

A simulated forwarding path is composed of multiple steps. Each step has a well-defined state and an associated configuration.

JSON representation  
---  
      
    
    {
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#State)),
      "causesDrop": boolean,
      "projectId": string,
    
      // Union field step_info can be only one of the following:
      "instance": {
        object ([InstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#InstanceInfo))
      },
      "firewall": {
        object ([FirewallInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#FirewallInfo))
      },
      "route": {
        object ([RouteInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteInfo))
      },
      "endpoint": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo))
      },
      "googleService": {
        object ([GoogleServiceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceInfo))
      },
      "forwardingRule": {
        object ([ForwardingRuleInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardingRuleInfo))
      },
      "hybridSubnet": {
        object ([HybridSubnetInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HybridSubnetInfo))
      },
      "vpnGateway": {
        object ([VpnGatewayInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpnGatewayInfo))
      },
      "vpnTunnel": {
        object ([VpnTunnelInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpnTunnelInfo))
      },
      "interconnectAttachment": {
        object ([InterconnectAttachmentInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#InterconnectAttachmentInfo))
      },
      "vpcConnector": {
        object ([VpcConnectorInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpcConnectorInfo))
      },
      "directVpcEgressConnection": {
        object ([DirectVpcEgressConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DirectVpcEgressConnectionInfo))
      },
      "serverlessExternalConnection": {
        object ([ServerlessExternalConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ServerlessExternalConnectionInfo))
      },
      "deliver": {
        object ([DeliverInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DeliverInfo))
      },
      "forward": {
        object ([ForwardInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardInfo))
      },
      "abort": {
        object ([AbortInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AbortInfo))
      },
      "drop": {
        object ([DropInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DropInfo))
      },
      "loadBalancer": {
        object ([LoadBalancerInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerInfo))
      },
      "network": {
        object ([NetworkInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NetworkInfo))
      },
      "gkeMaster": {
        object ([GKEMasterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GKEMasterInfo))
      },
      "gkePod": {
        object ([GkePodInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkePodInfo))
      },
      "ipMasqueradingSkipped": {
        object ([IpMasqueradingSkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#IpMasqueradingSkippedInfo))
      },
      "gkeNetworkPolicy": {
        object ([GkeNetworkPolicyInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkeNetworkPolicyInfo))
      },
      "gkeNetworkPolicySkipped": {
        object ([GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkeNetworkPolicySkippedInfo))
      },
      "cloudSqlInstance": {
        object ([CloudSQLInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudSQLInstanceInfo))
      },
      "redisInstance": {
        object ([RedisInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RedisInstanceInfo))
      },
      "redisCluster": {
        object ([RedisClusterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RedisClusterInfo))
      },
      "cloudFunction": {
        object ([CloudFunctionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudFunctionInfo))
      },
      "appEngineVersion": {
        object ([AppEngineVersionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AppEngineVersionInfo))
      },
      "cloudRunRevision": {
        object ([CloudRunRevisionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunRevisionInfo))
      },
      "cloudRunJob": {
        object ([CloudRunJobInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunJobInfo))
      },
      "nat": {
        object ([NatInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NatInfo))
      },
      "proxyConnection": {
        object ([ProxyConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProxyConnectionInfo))
      },
      "loadBalancerBackendInfo": {
        object ([LoadBalancerBackendInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerBackendInfo))
      },
      "storageBucket": {
        object ([StorageBucketInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#StorageBucketInfo))
      },
      "serverlessNeg": {
        object ([ServerlessNegInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ServerlessNegInfo))
      },
      "ngfwPacketInspection": {
        object ([NgfwPacketInspectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NgfwPacketInspectionInfo))
      },
      "dmsPrivateConnection": {
        object ([PrivateConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#PrivateConnectionInfo))
      },
      "datastreamPrivateConnection": {
        object ([PrivateConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#PrivateConnectionInfo))
      }
      // End of list of possible types for union field step_info.
    }  
  
Fields  
---  
`description` |  `string` A description of the step. Usually this is a summary of the state.  
`state` |  `enum (`[State](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#State)`)` Each step is in one of the pre-defined states.  
`causesDrop` |  `boolean` This is a step that leads to the final state Drop.  
`projectId` |  `string` Project ID that contains the configuration this step is validating.  
Union field `step_info`. Configuration or metadata associated with each step. The configuration is filtered based on viewer's permission. If a viewer has no permission to view the configuration in this step, for non-final states a special state is populated (VIEWER_PERMISSION_MISSING), and for final state the configuration is cleared. `step_info` can be only one of the following:  
`instance` |  `object (`[InstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#InstanceInfo)`)` Display information of a Compute Engine instance.  
`firewall` |  `object (`[FirewallInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#FirewallInfo)`)` Display information of a Compute Engine firewall rule.  
`route` |  `object (`[RouteInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteInfo)`)` Display information of a Compute Engine route.  
`endpoint` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo)`)` Display information of the source and destination under analysis. The endpoint information in an intermediate state may differ with the initial input, as it might be modified by state like NAT, or Connection Proxy.  
`googleService` |  `object (`[GoogleServiceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceInfo)`)` Display information of a Google service  
`forwardingRule` |  `object (`[ForwardingRuleInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardingRuleInfo)`)` Display information of a Compute Engine forwarding rule.  
`hybridSubnet` |  `object (`[HybridSubnetInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HybridSubnetInfo)`)` Display information of a hybrid subnet.  
`vpnGateway` |  `object (`[VpnGatewayInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpnGatewayInfo)`)` Display information of a Compute Engine VPN gateway.  
`vpnTunnel` |  `object (`[VpnTunnelInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpnTunnelInfo)`)` Display information of a Compute Engine VPN tunnel.  
`interconnectAttachment` |  `object (`[InterconnectAttachmentInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#InterconnectAttachmentInfo)`)` Display information of an interconnect attachment.  
`vpcConnector` |  `object (`[VpcConnectorInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#VpcConnectorInfo)`)` Display information of a VPC connector.  
`directVpcEgressConnection` |  `object (`[DirectVpcEgressConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DirectVpcEgressConnectionInfo)`)` Display information of a serverless direct VPC egress connection.  
`serverlessExternalConnection` |  `object (`[ServerlessExternalConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ServerlessExternalConnectionInfo)`)` Display information of a serverless public (external) connection.  
`deliver` |  `object (`[DeliverInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DeliverInfo)`)` Display information of the final state "deliver" and reason.  
`forward` |  `object (`[ForwardInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ForwardInfo)`)` Display information of the final state "forward" and reason.  
`abort` |  `object (`[AbortInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AbortInfo)`)` Display information of the final state "abort" and reason.  
`drop` |  `object (`[DropInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#DropInfo)`)` Display information of the final state "drop" and reason.  
`loadBalancer  
**(deprecated)**` |  `object (`[LoadBalancerInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerInfo)`)` This item is deprecated!Display information of the load balancers. Deprecated in favor of the `loadBalancerBackendInfo` field, not used in new tests.  
`network` |  `object (`[NetworkInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NetworkInfo)`)` Display information of a Google Cloud network.  
`gkeMaster` |  `object (`[GKEMasterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GKEMasterInfo)`)` Display information of a Google Kubernetes Engine cluster master.  
`gkePod` |  `object (`[GkePodInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkePodInfo)`)` Display information of a Google Kubernetes Engine Pod.  
`ipMasqueradingSkipped` |  `object (`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#IpMasqueradingSkippedInfo)`)` Display information of the reason why GKE Pod IP masquerading was skipped.  
`gkeNetworkPolicy` |  `object (`[GkeNetworkPolicyInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkeNetworkPolicyInfo)`)` Display information of a GKE Network Policy.  
`gkeNetworkPolicySkipped` |  `object (`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GkeNetworkPolicySkippedInfo)`)` Display information of the reason why GKE Network Policy evaluation was skipped.  
`cloudSqlInstance` |  `object (`[CloudSQLInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudSQLInstanceInfo)`)` Display information of a Cloud SQL instance.  
`redisInstance` |  `object (`[RedisInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RedisInstanceInfo)`)` Display information of a Redis Instance.  
`redisCluster` |  `object (`[RedisClusterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RedisClusterInfo)`)` Display information of a Redis Cluster.  
`cloudFunction` |  `object (`[CloudFunctionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudFunctionInfo)`)` Display information of a Cloud Function.  
`appEngineVersion` |  `object (`[AppEngineVersionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#AppEngineVersionInfo)`)` Display information of an App Engine service version.  
`cloudRunRevision` |  `object (`[CloudRunRevisionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunRevisionInfo)`)` Display information of a Cloud Run revision.  
`cloudRunJob` |  `object (`[CloudRunJobInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudRunJobInfo)`)` Display information of a Cloud Run job.  
`nat` |  `object (`[NatInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NatInfo)`)` Display information of a NAT.  
`proxyConnection` |  `object (`[ProxyConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProxyConnectionInfo)`)` Display information of a ProxyConnection.  
`loadBalancerBackendInfo` |  `object (`[LoadBalancerBackendInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerBackendInfo)`)` Display information of a specific load balancer backend.  
`storageBucket` |  `object (`[StorageBucketInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#StorageBucketInfo)`)` Display information of a Storage Bucket. Used only for return traces.  
`serverlessNeg` |  `object (`[ServerlessNegInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ServerlessNegInfo)`)` Display information of a Serverless network endpoint group backend. Used only for return traces.  
`ngfwPacketInspection` |  `object (`[NgfwPacketInspectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NgfwPacketInspectionInfo)`)` Display information of a layer 7 packet inspection by the firewall.  
`dmsPrivateConnection` |  `object (`[PrivateConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#PrivateConnectionInfo)`)` Display information of a DMS Private Connection.  
`datastreamPrivateConnection` |  `object (`[PrivateConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#PrivateConnectionInfo)`)` Display information of a Datastream Private Connection.  
  
## State

Type of states that are defined in the network state machine. Each step in the packet trace is in a specific state.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`START_FROM_INSTANCE` | Initial state: packet originating from a Compute Engine instance. An InstanceInfo is populated with starting instance information.  
`START_FROM_INTERNET` | Initial state: packet originating from the internet. The endpoint information is populated.  
`START_FROM_GOOGLE_SERVICE` | Initial state: packet originating from a Google service. The googleService information is populated.  
`START_FROM_PRIVATE_NETWORK` | Initial state: packet originating from a VPC or on-premises network with internal source IP. If the source is a VPC network visible to the user, a NetworkInfo is populated with details of the network.  
`START_FROM_GKE_MASTER` | Initial state: packet originating from a Google Kubernetes Engine cluster master. A GKEMasterInfo is populated with starting instance information.  
`START_FROM_CLOUD_SQL_INSTANCE` | Initial state: packet originating from a Cloud SQL instance. A CloudSQLInstanceInfo is populated with starting instance information.  
`START_FROM_GKE_POD` | Initial state: packet originating from a Google Kubernetes Engine Pod. A GkePodInfo is populated with starting Pod information.  
`START_FROM_REDIS_INSTANCE` | Initial state: packet originating from a Redis instance. A RedisInstanceInfo is populated with starting instance information.  
`START_FROM_REDIS_CLUSTER` | Initial state: packet originating from a Redis Cluster. A RedisClusterInfo is populated with starting Cluster information.  
`START_FROM_CLOUD_FUNCTION` | Initial state: packet originating from a Cloud Function. A CloudFunctionInfo is populated with starting function information.  
`START_FROM_APP_ENGINE_VERSION` | Initial state: packet originating from an App Engine service version. An AppEngineVersionInfo is populated with starting version information.  
`START_FROM_CLOUD_RUN_REVISION` | Initial state: packet originating from a Cloud Run revision. A CloudRunRevisionInfo is populated with starting revision information.  
`START_FROM_CLOUD_RUN_JOB` | Initial state: packet originating from a Cloud Run Job. A CloudRunJobInfo is populated with starting Job information.  
`START_FROM_STORAGE_BUCKET` | Initial state: packet originating from a Storage Bucket. Used only for return traces. The storageBucket information is populated.  
`START_FROM_PSC_PUBLISHED_SERVICE` | Initial state: packet originating from a published service that uses Private Service Connect. Used only for return traces.  
`START_FROM_SERVERLESS_NEG` | Initial state: packet originating from a serverless network endpoint group backend. Used only for return traces. The serverlessNeg information is populated.  
`START_FROM_DMS_PRIVATE_CONNECTION` | Initial state: packet originating from a DMS Private Connection.  
`START_FROM_DATASTREAM_PRIVATE_CONNECTION` | Initial state: packet originating from a Datastream Private Connection.  
`APPLY_INGRESS_FIREWALL_RULE` | Config checking state: verify ingress firewall rule.  
`APPLY_EGRESS_FIREWALL_RULE` | Config checking state: verify egress firewall rule.  
`APPLY_ROUTE` | Config checking state: verify route.  
`APPLY_FORWARDING_RULE` | Config checking state: match forwarding rule.  
`ANALYZE_LOAD_BALANCER_BACKEND` | Config checking state: verify load balancer backend configuration.  
`SPOOFING_APPROVED` | Config checking state: packet sent or received under foreign IP address and allowed.  
`ARRIVE_AT_INSTANCE` | Forwarding state: arriving at a Compute Engine instance.  
`ARRIVE_AT_INTERNAL_LOAD_BALANCER` | Forwarding state: arriving at a Compute Engine internal load balancer.This item is deprecated!  
`ARRIVE_AT_EXTERNAL_LOAD_BALANCER` | Forwarding state: arriving at a Compute Engine external load balancer.This item is deprecated!  
`ARRIVE_AT_HYBRID_SUBNET` | Forwarding state: arriving at a hybrid subnet. Appropriate routing configuration will be determined here.  
`ARRIVE_AT_VPN_GATEWAY` | Forwarding state: arriving at a Cloud VPN gateway.  
`ARRIVE_AT_VPN_TUNNEL` | Forwarding state: arriving at a Cloud VPN tunnel.  
`ARRIVE_AT_INTERCONNECT_ATTACHMENT` | Forwarding state: arriving at an interconnect attachment.  
`ARRIVE_AT_VPC_CONNECTOR` | Forwarding state: arriving at a VPC connector.  
`ARRIVE_AT_GKE_POD` | Forwarding state: arriving at a GKE Pod.  
`DIRECT_VPC_EGRESS_CONNECTION` | Forwarding state: for packets originating from a serverless endpoint forwarded through Direct VPC egress.  
`SERVERLESS_EXTERNAL_CONNECTION` | Forwarding state: for packets originating from a serverless endpoint forwarded through public (external) connectivity.  
`NGFW_PACKET_INSPECTION` | Forwarding state: Layer 7 packet inspection by the firewall endpoint based on the configured security profile group.  
`NAT` | Transition state: packet header translated. The `nat` field is populated with the translation information.  
`SKIP_GKE_POD_IP_MASQUERADING` | Transition state: GKE Pod IP masquerading is skipped. The `ipMasqueradingSkipped` field is populated with the reason.  
`SKIP_GKE_INGRESS_NETWORK_POLICY` | Transition state: GKE Ingress Network Policy is skipped. The `gkeNetworkPolicySkipped` field is populated with the reason.  
`SKIP_GKE_EGRESS_NETWORK_POLICY` | Transition state: GKE Egress Network Policy is skipped. The `gkeNetworkPolicySkipped` field is populated with the reason.  
`APPLY_INGRESS_GKE_NETWORK_POLICY` | Config checking state: verify ingress GKE network policy.  
`APPLY_EGRESS_GKE_NETWORK_POLICY` | Config checking state: verify egress GKE network policy.  
`PROXY_CONNECTION` | Transition state: original connection is terminated and a new proxied connection is initiated.  
`DELIVER` | Final state: packet could be delivered.  
`DROP` | Final state: packet could be dropped.  
`FORWARD` | Final state: packet could be forwarded to a network with an unknown configuration.  
`ABORT` | Final state: analysis is aborted.  
`VIEWER_PERMISSION_MISSING` | Special state: viewer of the test result does not have permission to see the configuration in this step.  
  
## InstanceInfo

For display only. Metadata associated with a Compute Engine instance.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "interface": string,
      "networkUri": string,
      "internalIp": string,
      "externalIp": string,
      "networkTags": [
        string
      ],
      "serviceAccount": string,
      "pscNetworkAttachmentUri": string,
      "running": boolean,
      "status": enum ([Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Status))
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine instance.  
`uri` |  `string` URI of a Compute Engine instance in format "projects/{project}/zones/{zone}/instances/{instance}"  
`interface` |  `string` Name of the network interface of a Compute Engine instance.  
`networkUri` |  `string` URI of a Compute Engine network in format "projects/{project}/global/networks/{network}"  
`internalIp` |  `string` Internal IP address of the network interface.  
`externalIp` |  `string` External IP address of the network interface.  
`networkTags[]` |  `string` Network tags configured on the instance.  
`serviceAccount  
**(deprecated)**` |  `string` This item is deprecated!Service account authorized for the instance.  
`pscNetworkAttachmentUri` |  `string` URI of the PSC network attachment the NIC is attached to (if relevant) in format "projects/{project}/regions/{region}/networkAttachments/{network_attachment}"  
`running  
**(deprecated)**` |  `boolean` This item is deprecated!Indicates whether the Compute Engine instance is running. Deprecated: use the `status` field instead.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Status)`)` The status of the instance.  
  
## Status

The status of the instance. We treat all states other than "RUNNING" as not running.

Enums  
---  
`STATUS_UNSPECIFIED` | Default unspecified value.  
`RUNNING` | The instance is running.  
`NOT_RUNNING` | The instance has any status other than "RUNNING".  
  
## FirewallInfo

For display only. Metadata associated with a VPC firewall rule, an implied VPC firewall rule, or a firewall policy rule.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "direction": string,
      "action": string,
      "priority": integer,
      "networkUri": string,
      "targetTags": [
        string
      ],
      "targetServiceAccounts": [
        string
      ],
      "policy": string,
      "policyUri": string,
      "firewallRuleType": enum ([FirewallRuleType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#FirewallRuleType)),
      "policyPriority": integer,
      "targetType": enum ([TargetType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#TargetType))
    }  
  
Fields  
---  
`displayName` |  `string` The display name of the firewall rule. This field might be empty for firewall policy rules.  
`uri` |  `string` The URI of the firewall rule in format "projects/{project}/global/firewalls/{firewall}". This field is not applicable to implied VPC firewall rules.  
`direction` |  `string` Possible values: INGRESS, EGRESS  
`action` |  `string` Possible values: ALLOW, DENY, APPLY_SECURITY_PROFILE_GROUP  
`priority` |  `integer` The priority of the firewall rule.  
`networkUri` |  `string` The URI of the VPC network that the firewall rule is associated with in format "projects/{project}/global/networks/{network}". This field is not applicable to hierarchical firewall policy rules.  
`targetTags[]` |  `string` The target tags defined by the VPC firewall rule. This field is not applicable to firewall policy rules.  
`targetServiceAccounts[]` |  `string` The target service accounts specified by the firewall rule.  
`policy` |  `string` The name of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules.  
`policyUri` |  `string` The URI of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules. Format: * `locations/global/firewallPolicies/{policyId}` (hierarchical policy) * `projects/{projectId}/global/firewallPolicies/{policyId}` (global network firewall policy) * `projects/{projectId}/regions/{region}/firewallPolicies/{policyId}` (regional network firewall policy)  
`firewallRuleType` |  `enum (`[FirewallRuleType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#FirewallRuleType)`)` The firewall rule's type.  
`policyPriority` |  `integer` The priority of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules.  
`targetType` |  `enum (`[TargetType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#TargetType)`)` Target type of the firewall rule.  
  
## FirewallRuleType

The firewall rule's type.

Enums  
---  
`FIREWALL_RULE_TYPE_UNSPECIFIED` | Unspecified type.  
`HIERARCHICAL_FIREWALL_POLICY_RULE` | Hierarchical firewall policy rule. For details, see [Hierarchical firewall policies overview](https://cloud.google.com/vpc/docs/firewall-policies).  
`VPC_FIREWALL_RULE` | VPC firewall rule. For details, see [VPC firewall rules overview](https://cloud.google.com/vpc/docs/firewalls).  
`IMPLIED_VPC_FIREWALL_RULE` | Implied VPC firewall rule. For details, see [Implied rules](https://cloud.google.com/vpc/docs/firewalls#default_firewall_rules).  
`SERVERLESS_VPC_ACCESS_MANAGED_FIREWALL_RULE` | Implicit firewall rules that are managed by serverless VPC access to allow ingress access. They are not visible in the Google Cloud console. For details, see [VPC connector's implicit rules](https://cloud.google.com/functions/docs/networking/connecting-vpc#restrict-access).  
`NETWORK_FIREWALL_POLICY_RULE` | User-defined global network firewall policy rule. For details, see [Network firewall policies](https://cloud.google.com/vpc/docs/network-firewall-policies).  
`NETWORK_REGIONAL_FIREWALL_POLICY_RULE` | User-defined regional network firewall policy rule. For details, see [Regional network firewall policies](https://cloud.google.com/firewall/docs/regional-firewall-policies).  
`SYSTEM_NETWORK_FIREWALL_POLICY_RULE` | System-defined global network firewall policy rule.  
`SYSTEM_REGIONAL_NETWORK_FIREWALL_POLICY_RULE` | System-defined regional network firewall policy rule.  
`UNSUPPORTED_FIREWALL_POLICY_RULE` | Firewall policy rule containing attributes not yet supported in Connectivity tests. Firewall analysis is skipped if such a rule can potentially be matched. Please see the [list of unsupported configurations](https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#unsupported-configs).  
`TRACKING_STATE` | Tracking state for response traffic created when request traffic goes through allow firewall rule. For details, see [firewall rules specifications](https://cloud.google.com/firewall/docs/firewalls#specifications)  
`ANALYSIS_SKIPPED` | Firewall analysis was skipped due to executing Connectivity Test in the BypassFirewallChecks mode  
  
## TargetType

Target type of the firewall rule.

Enums  
---  
`TARGET_TYPE_UNSPECIFIED` | Target type is not specified. In this case we treat the rule as applying to INSTANCES target type.  
`INSTANCES` | Firewall rule applies to instances.  
`INTERNAL_MANAGED_LB` | Firewall rule applies to internal managed load balancers.  
  
## RouteInfo

For display only. Metadata associated with a Compute Engine route.

JSON representation  
---  
      
    
    {
      "routeType": enum ([RouteType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteType)),
      "nextHopType": enum ([NextHopType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NextHopType)),
      "routeScope": enum ([RouteScope](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteScope)),
      "displayName": string,
      "uri": string,
      "region": string,
      "destIpRange": string,
      "nextHop": string,
      "networkUri": string,
      "priority": integer,
      "instanceTags": [
        string
      ],
      "srcIpRange": string,
      "destPortRanges": [
        string
      ],
      "srcPortRanges": [
        string
      ],
      "protocols": [
        string
      ],
      "nextHopUri": string,
      "nextHopNetworkUri": string,
      "originatingRouteUri": string,
      "originatingRouteDisplayName": string,
      "nccHubRouteUri": string,
      "nccHubUri": string,
      "nccSpokeUri": string,
      "advertisedRouteSourceRouterUri": string,
      "advertisedRouteNextHopUri": string
    }  
  
Fields  
---  
`routeType` |  `enum (`[RouteType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteType)`)` Type of route.  
`nextHopType` |  `enum (`[NextHopType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#NextHopType)`)` Type of next hop.  
`routeScope  
**(deprecated)**` |  `enum (`[RouteScope](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RouteScope)`)` This item is deprecated!Indicates where route is applicable. Deprecated, routes with NCC_HUB scope are not included in the trace in new tests.  
`displayName` |  `string` Name of a route.  
`uri` |  `string` URI of a route in format "projects/{project}/global/routes/{route}". SUBNET, STATIC, PEERING_SUBNET (only for peering network) and POLICY_BASED routes only.  
`region` |  `string` Region of the route. DYNAMIC, PEERING_DYNAMIC, POLICY_BASED and ADVERTISED routes only. If set for POLICY_BASED route, this is a region of VLAN attachments for Cloud Interconnect the route applies to. If set to "all" for POLICY_BASED route, the route applies to VLAN attachments of Cloud Interconnect in all regions.  
`destIpRange` |  `string` Destination IP range of the route.  
`nextHop  
**(deprecated)**` |  `string` This item is deprecated!String type of the next hop of the route (for example, "VPN tunnel"). Deprecated in favor of the nextHopType and nextHopUri fields, not used in new tests.  
`networkUri` |  `string` URI of a VPC network where route is located in format "projects/{project}/global/networks/{network}".  
`priority` |  `integer` Priority of the route.  
`instanceTags[]` |  `string` Instance tags of the route.  
`srcIpRange` |  `string` Source IP address range of the route. POLICY_BASED routes only.  
`destPortRanges[]` |  `string` Destination port ranges of the route. POLICY_BASED routes only.  
`srcPortRanges[]` |  `string` Source port ranges of the route. POLICY_BASED routes only.  
`protocols[]` |  `string` Protocols of the route. POLICY_BASED routes only.  
`nextHopUri` |  `string` URI of the next hop resource.  
`nextHopNetworkUri` |  `string` URI of a VPC network where the next hop resource is located in format "projects/{project}/global/networks/{network}".  
`originatingRouteUri` |  `string` For PEERING_SUBNET and PEERING_STATIC routes, the URI of the originating SUBNET/STATIC route. Format: `projects/{projectId}/global/routes/{route_id}`  
`originatingRouteDisplayName` |  `string` For PEERING_SUBNET, PEERING_STATIC and PEERING_DYNAMIC routes, the name of the originating SUBNET/STATIC/DYNAMIC route.  
`nccHubRouteUri` |  `string` For PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub, the URI of the corresponding route in NCC Hub's routing table. Format: `projects/{projectId}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}/routes/{route_id}`  
`nccHubUri` |  `string` URI of the NCC Hub the route is advertised by in format "projects/{project}/locations/global/hubs/{hub}". PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub only.  
`nccSpokeUri` |  `string` URI of the destination NCC Spoke in format "projects/{project}/locations/{location}/spokes/{spoke}" (regional) or "projects/{project}/locations/global/spokes/{spoke}" (global). PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub only.  
`advertisedRouteSourceRouterUri` |  `string` For ADVERTISED dynamic routes, the URI of the Cloud Router that advertised the corresponding IP prefix in format "projects/{project}/regions/{region}/routers/{router}".  
`advertisedRouteNextHopUri  
**(deprecated)**` |  `string` This item is deprecated!For ADVERTISED routes, the URI of their next hop, i.e. the URI of the hybrid endpoint (VPN tunnel, Interconnect attachment, NCC router appliance) the advertised prefix is advertised through, or URI of the source peered network. Deprecated in favor of the nextHopUri field, not used in new tests.  
  
## RouteType

Type of route:

Enums  
---  
`ROUTE_TYPE_UNSPECIFIED` | Unspecified type. Default value.  
`SUBNET` | Route is a subnet route automatically created by the system.  
`STATIC` | Static route created by the user, including the default route to the internet.  
`DYNAMIC` | Dynamic route exchanged between BGP peers.  
`PEERING_SUBNET` | A subnet route received from peering network or NCC Hub.  
`PEERING_STATIC` | A static route received from peering network.  
`PEERING_DYNAMIC` | A dynamic route received from peering network or NCC Hub.  
`POLICY_BASED` | Policy based route.  
`ADVERTISED` | Advertised route. Synthetic route which is used to transition from the StartFromPrivateNetwork state in Connectivity tests.  
  
## NextHopType

Type of next hop:

Enums  
---  
`NEXT_HOP_TYPE_UNSPECIFIED` | Unspecified type. Default value.  
`NEXT_HOP_IP` | Next hop is an IP address.  
`NEXT_HOP_INSTANCE` | Next hop is a Compute Engine instance.  
`NEXT_HOP_NETWORK` | Next hop is a VPC network gateway.  
`NEXT_HOP_PEERING` | Next hop is a peering VPC. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located.  
`NEXT_HOP_INTERCONNECT` | Next hop is an interconnect.  
`NEXT_HOP_VPN_TUNNEL` | Next hop is a VPN tunnel.  
`NEXT_HOP_VPN_GATEWAY` | Next hop is a VPN gateway. This scenario only happens when tracing connectivity from an on-premises network to Google Cloud through a VPN. The analysis simulates a packet departing from the on-premises network through a VPN tunnel and arriving at a Cloud VPN gateway.  
`NEXT_HOP_INTERNET_GATEWAY` | Next hop is an internet gateway.  
`NEXT_HOP_BLACKHOLE` | Next hop is blackhole; that is, the next hop either does not exist or is unusable.  
`NEXT_HOP_ILB` | Next hop is the forwarding rule of an Internal Load Balancer.  
`NEXT_HOP_ROUTER_APPLIANCE` | Next hop is a [router appliance instance](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).  
`NEXT_HOP_NCC_HUB` | Next hop is an NCC hub. This scenario only happens when the user doesn't have permissions to the project where the next hop resource is located.  
`SECURE_WEB_PROXY_GATEWAY` | Next hop is Secure Web Proxy Gateway.  
  
## RouteScope

Indicates where routes are applicable.

Enums  
---  
`ROUTE_SCOPE_UNSPECIFIED` | Unspecified scope. Default value.  
`NETWORK` | Route is applicable to packets in Network.  
`NCC_HUB` | Route is applicable to packets using NCC Hub's routing table.  
  
## GoogleServiceInfo

For display only. Details of a Google Service sending packets to a VPC network. Although the source IP might be a publicly routable address, some Google Services use special routes within Google production infrastructure to reach Compute Engine Instances. <https://cloud.google.com/vpc/docs/routes#special_return_paths>

JSON representation  
---  
      
    
    {
      "sourceIp": string,
      "googleServiceType": enum ([GoogleServiceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceType))
    }  
  
Fields  
---  
`sourceIp` |  `string` Source IP address.  
`googleServiceType` |  `enum (`[GoogleServiceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceType)`)` Recognized type of a Google Service.  
  
## GoogleServiceType

Recognized type of a Google Service.

Enums  
---  
`GOOGLE_SERVICE_TYPE_UNSPECIFIED` | Unspecified Google Service.  
`IAP` | Identity aware proxy. <https://cloud.google.com/iap/docs/using-tcp-forwarding>  
`GFE_PROXY_OR_HEALTH_CHECK_PROBER` | One of two services sharing IP ranges: * Load Balancer proxy * Centralized Health Check prober <https://cloud.google.com/load-balancing/docs/firewall-rules>  
`CLOUD_DNS` | Connectivity from Cloud DNS to forwarding targets or alternate name servers that use private routing. <https://cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules> <https://cloud.google.com/dns/docs/policies#firewall-rules>  
`GOOGLE_API` | private.googleapis.com and restricted.googleapis.com  
`GOOGLE_API_PSC` | Google API via Private Service Connect. <https://cloud.google.com/vpc/docs/configure-private-service-connect-apis>  
`GOOGLE_API_VPC_SC` | Google API via VPC Service Controls. <https://cloud.google.com/vpc/docs/configure-private-service-connect-apis>  
`SERVERLESS_VPC_ACCESS` | Google API via Serverless VPC Access. <https://cloud.google.com/vpc/docs/serverless-vpc-access>  
  
## ForwardingRuleInfo

For display only. Metadata associated with a Compute Engine forwarding rule.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "matchedProtocol": string,
      "matchedPortRange": string,
      "vip": string,
      "target": string,
      "networkUri": string,
      "region": string,
      "loadBalancerName": string,
      "pscServiceAttachmentUri": string,
      "pscGoogleApiTarget": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of the forwarding rule.  
`uri` |  `string` URI of the forwarding rule in format "projects/{project}/global/forwardingRules/{forwardingRule}" (global) or "projects/{project}/regions/{region}/forwardingRules/{forwardingRule}" (regional).  
`matchedProtocol` |  `string` Protocol defined in the forwarding rule that matches the packet.  
`matchedPortRange` |  `string` Port range defined in the forwarding rule that matches the packet.  
`vip` |  `string` VIP of the forwarding rule.  
`target` |  `string` Target type of the forwarding rule.  
`networkUri` |  `string` URI of a VPC network where the forwarding rule is located in format "projects/{project}/global/networks/{network}".  
`region` |  `string` Region of the forwarding rule. Set only for regional forwarding rules.  
`loadBalancerName` |  `string` Name of the load balancer the forwarding rule belongs to. Empty for forwarding rules not related to load balancers (like PSC forwarding rules).  
`pscServiceAttachmentUri` |  `string` URI of the PSC service attachment this forwarding rule targets (if applicable) in format "projects/{project}/regions/{region}/serviceAttachments/{service_attachment}".  
`pscGoogleApiTarget` |  `string` PSC Google API target this forwarding rule targets (if applicable).  
  
## HybridSubnetInfo

For display only. Metadata associated with a hybrid subnet.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a hybrid subnet.  
`uri` |  `string` URI of the hybrid subnet. Format: `projects/{projectId}/regions/{region}/subnetworks/{subnetwork_id}`  
`region` |  `string` Name of a Google Cloud region where the hybrid subnet is configured.  
  
## VpnGatewayInfo

For display only. Metadata associated with a Compute Engine VPN gateway.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "ipAddress": string,
      "vpnTunnelUri": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPN gateway.  
`uri` |  `string` URI of the VPN gateway. Format: * `projects/{projectId}/regions/{region}/vpnGateways/{vpn_gateway_id}` (HA VPN gateway) * `projects/{projectId}/regions/{region}/targetVpnGateways/{target_vpn_gateway_id}` (Classic VPN gateway)  
`networkUri` |  `string` URI of the VPC network where the VPN gateway is configured. Format: `projects/{projectId}/global/networks/{network_id}`  
`ipAddress` |  `string` IP address of the VPN gateway.  
`vpnTunnelUri` |  `string` URI of the VPN tunnel associated with the VPN gateway. There may be multiple VPN tunnels configured on a VPN gateway, and only the one relevant to the test is displayed. Format: `projects/{projectId}/regions/{region}/vpnTunnels/{vpn_tunnel_id}`  
`region` |  `string` Name of a Google Cloud region where this VPN gateway is configured.  
  
## VpnTunnelInfo

For display only. Metadata associated with a Compute Engine VPN tunnel.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "sourceGateway": string,
      "remoteGateway": string,
      "remoteGatewayIp": string,
      "sourceGatewayIp": string,
      "networkUri": string,
      "region": string,
      "routingType": enum ([RoutingType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RoutingType))
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPN tunnel.  
`uri` |  `string` URI of the VPN tunnel. Format: `projects/{projectId}/regions/{region}/vpnTunnels/{vpn_tunnel_id}`  
`sourceGateway` |  `string` URI of the VPN gateway at local end of the tunnel. Format: * `projects/{projectId}/regions/{region}/vpnGateways/{vpn_gateway_id}` (HA VPN gateway) * `projects/{projectId}/regions/{region}/targetVpnGateways/{target_vpn_gateway_id}` (Classic VPN gateway)  
`remoteGateway` |  `string` URI of a VPN gateway at remote end of the tunnel. Format: * `projects/{projectId}/regions/{region}/vpnGateways/{vpn_gateway_id}` (GCP HA VPN gateway) * `projects/{projectId}/global/peerVpnGateways/{peer_vpn_gateway_id}` (GCP peer VPN gateway)  
`remoteGatewayIp` |  `string` Remote VPN gateway's IP address.  
`sourceGatewayIp` |  `string` Local VPN gateway's IP address.  
`networkUri` |  `string` URI of the VPC network where the VPN tunnel is configured. Format: `projects/{projectId}/global/networks/{network_id}`  
`region` |  `string` Name of a Google Cloud region where this VPN tunnel is configured.  
`routingType` |  `enum (`[RoutingType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#RoutingType)`)` Type of the routing policy.  
  
## RoutingType

Types of VPN routing policy. For details, refer to [Networks and Tunnel routing](https://cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing/).

Enums  
---  
`ROUTING_TYPE_UNSPECIFIED` | Unspecified type. Default value.  
`ROUTE_BASED` | Route based VPN.  
`POLICY_BASED` | Policy based routing.  
`DYNAMIC` | Dynamic (BGP) routing.  
  
## InterconnectAttachmentInfo

For display only. Metadata associated with an Interconnect attachment.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "interconnectUri": string,
      "region": string,
      "cloudRouterUri": string,
      "type": enum ([Type](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Type)),
      "l2AttachmentMatchedIpAddress": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of an Interconnect attachment.  
`uri` |  `string` URI of the Interconnect attachment. Format: `projects/{projectId}/regions/{region}/interconnectAttachments/{attachment_id}`  
`interconnectUri` |  `string` URI of the Interconnect. Format: `projects/{projectId}/global/interconnects/{interconnect_id}`  
`region` |  `string` Name of a Google Cloud region where the Interconnect attachment is configured.  
`cloudRouterUri` |  `string` URI of the Cloud Router to be used for dynamic routing. Format: `projects/{projectId}/regions/{region}/routers/{router_id}`  
`type` |  `enum (`[Type](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Type)`)` The type of interconnect attachment this is.  
`l2AttachmentMatchedIpAddress` |  `string` Appliance IP address that was matched for L2_DEDICATED attachments.  
  
## Type

What type of interconnect attachment this is.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`DEDICATED` | Attachment to a dedicated interconnect.  
`PARTNER` | Attachment to a partner interconnect, created by the customer.  
`PARTNER_PROVIDER` | Attachment to a partner interconnect, created by the partner.  
`L2_DEDICATED` | Attachment to a L2 interconnect, created by the customer.  
  
## VpcConnectorInfo

For display only. Metadata associated with a VPC connector.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPC connector.  
`uri` |  `string` URI of a VPC connector. Format: `projects/{projectId}/locations/{location}/connectors/{connector_id}`  
`location` |  `string` Location in which the VPC connector is deployed.  
  
## DirectVpcEgressConnectionInfo

For display only. Metadata associated with a serverless direct VPC egress connection.

JSON representation  
---  
      
    
    {
      "networkUri": string,
      "subnetworkUri": string,
      "selectedIpRange": string,
      "selectedIpAddress": string,
      "region": string
    }  
  
Fields  
---  
`networkUri` |  `string` URI of the VPC network for direct egress. Format: `projects/{projectId}/global/networks/{network_id}`  
`subnetworkUri` |  `string` URI of the subnetwork for direct egress. Format: `projects/{projectId}/regions/{region}/subnetworks/{subnetwork_id}`  
`selectedIpRange` |  `string` Selected IP range.  
`selectedIpAddress` |  `string` Selected starting IP address, from the selected IP range.  
`region` |  `string` Region in which the Direct VPC egress is deployed.  
  
## ServerlessExternalConnectionInfo

For display only. Metadata associated with a serverless public connection.

JSON representation  
---  
      
    
    {
      "selectedIpAddress": string
    }  
  
Fields  
---  
`selectedIpAddress` |  `string` Selected starting IP address, from the Google dynamic address pool.  
  
## DeliverInfo

Details of the final state "deliver" and associated resource.

JSON representation  
---  
      
    
    {
      "target": enum ([Target](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Target)),
      "resourceUri": string,
      "ipAddress": string,
      "storageBucket": string,
      "pscGoogleApiTarget": string,
      "googleServiceType": enum ([GoogleServiceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceType_1))
    }  
  
Fields  
---  
`target` |  `enum (`[Target](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Target)`)` Target type where the packet is delivered to.  
`resourceUri` |  `string` URI of the resource that the packet is delivered to. For example: * `"projects/{project}/zones/{zone}/instances/{instance}"` * `"projects/{project}/regions/{region}/networkEndpointGroups/{network_endpoint_group}"`  
`ipAddress` |  `string` IP address of the target (if applicable).  
`storageBucket` |  `string` Name of the Cloud Storage Bucket the packet is delivered to (if applicable).  
`pscGoogleApiTarget` |  `string` PSC Google API target the packet is delivered to (if applicable).  
`googleServiceType` |  `enum (`[GoogleServiceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#GoogleServiceType_1)`)` Recognized type of a Google Service the packet is delivered to (if applicable).  
  
## Target

Deliver target types:

Enums  
---  
`TARGET_UNSPECIFIED` | Target not specified.  
`INSTANCE` | Target is a Compute Engine instance.  
`INTERNET` | Target is the internet.  
`GOOGLE_API` | Target is a Google API.  
`GKE_MASTER` | Target is a Google Kubernetes Engine cluster master.  
`CLOUD_SQL_INSTANCE` | Target is a Cloud SQL instance.  
`PSC_PUBLISHED_SERVICE` | Target is a published service that uses [Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-services).  
`PSC_GOOGLE_API` | Target is Google APIs that use [Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis).  
`PSC_VPC_SC` | Target is a VPC-SC that uses [Private Service Connect](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis).  
`SERVERLESS_NEG` | Target is a serverless network endpoint group.  
`STORAGE_BUCKET` | Target is a Cloud Storage bucket.  
`PRIVATE_NETWORK` | Target is a private network. Used only for return traces.  
`CLOUD_FUNCTION` | Target is a Cloud Function. Used only for return traces.  
`APP_ENGINE_VERSION` | Target is a App Engine service version. Used only for return traces.  
`CLOUD_RUN_REVISION` | Target is a Cloud Run revision. Used only for return traces.  
`GOOGLE_MANAGED_SERVICE` | Target is a Google-managed service. Used only for return traces.  
`REDIS_INSTANCE` | Target is a Redis Instance.  
`REDIS_CLUSTER` | Target is a Redis Cluster.  
`GKE_POD` | Target is a GKE Pod.  
`CLOUD_RUN_JOB` | Target is a Cloud Run Job. Used only for return traces.  
`DMS_PRIVATE_CONNECTION` | Target is a DMS Private Connection. Used only for return traces.  
`DATASTREAM_PRIVATE_CONNECTION` | Target is a Datastream Private Connection. Used only for return traces.  
  
## GoogleServiceType

Recognized type of a Google Service.

Enums  
---  
`GOOGLE_SERVICE_TYPE_UNSPECIFIED` | Unspecified Google Service.  
`IAP` | Identity aware proxy. <https://cloud.google.com/iap/docs/using-tcp-forwarding>  
`GFE_PROXY_OR_HEALTH_CHECK_PROBER` | One of two services sharing IP ranges: * Load Balancer proxy * Centralized Health Check prober <https://cloud.google.com/load-balancing/docs/firewall-rules>  
`CLOUD_DNS` | Connectivity from Cloud DNS to forwarding targets or alternate name servers that use private routing. <https://cloud.google.com/dns/docs/zones/forwarding-zones#firewall-rules> <https://cloud.google.com/dns/docs/policies#firewall-rules>  
`PRIVATE_GOOGLE_ACCESS` | private.googleapis.com and restricted.googleapis.com  
`SERVERLESS_VPC_ACCESS` | Google API via Private Service Connect. <https://cloud.google.com/vpc/docs/configure-private-service-connect-apis> Google API via Serverless VPC Access. <https://cloud.google.com/vpc/docs/serverless-vpc-access>  
  
## ForwardInfo

Details of the final state "forward" and associated resource.

JSON representation  
---  
      
    
    {
      "target": enum ([Target](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Target_1)),
      "resourceUri": string,
      "ipAddress": string
    }  
  
Fields  
---  
`target` |  `enum (`[Target](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Target_1)`)` Target type where this packet is forwarded to.  
`resourceUri` |  `string` URI of the resource that the packet is forwarded to. Format: * `projects/{projectId}/global/networks/{network_id}` (VPC peering network) * `projects/{projectId}/regions/{region}/vpnGateways/{vpn_gateway_id}` (VPN gateway)  
`ipAddress` |  `string` IP address of the target (if applicable).  
  
## Target

Forward target types.

Enums  
---  
`TARGET_UNSPECIFIED` | Target not specified.  
`PEERING_VPC` | Forwarded to a VPC peering network.  
`VPN_GATEWAY` | Forwarded to a Cloud VPN gateway.  
`INTERCONNECT` | Forwarded to a Cloud Interconnect connection.  
`GKE_MASTER` | Forwarded to a Google Kubernetes Engine Container cluster master.This item is deprecated!  
`IMPORTED_CUSTOM_ROUTE_NEXT_HOP` | Forwarded to the next hop of a custom route imported from a peering VPC.  
`CLOUD_SQL_INSTANCE` | Forwarded to a Cloud SQL instance.This item is deprecated!  
`ANOTHER_PROJECT` | Forwarded to a VPC network in another project.  
`NCC_HUB` | Forwarded to an NCC Hub.  
`ROUTER_APPLIANCE` | Forwarded to a router appliance.  
`SECURE_WEB_PROXY_GATEWAY` | Forwarded to a Secure Web Proxy Gateway.  
  
## AbortInfo

Details of the final state "abort" and associated resource.

JSON representation  
---  
      
    
    {
      "cause": enum ([Cause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Cause)),
      "resourceUri": string,
      "ipAddress": string,
      "projectsMissingPermission": [
        string
      ]
    }  
  
Fields  
---  
`cause` |  `enum (`[Cause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Cause)`)` Causes that the analysis is aborted.  
`resourceUri` |  `string` URI of the resource that caused the abort. Format: * `projects/{projectId}/global/networks/{network_id}` (VPC network) * `projects/{projectId}/zones/{zone}/instances/{instance_id}` (VM instance)  
`ipAddress` |  `string` IP address that caused the abort.  
`projectsMissingPermission[]` |  `string` List of project IDs the user specified in the request but lacks access to. In this case, analysis is aborted with the PERMISSION_DENIED cause.  
  
## Cause

Abort cause types:

Enums  
---  
`CAUSE_UNSPECIFIED` | Cause is unspecified.  
`UNKNOWN_NETWORK` | Aborted due to unknown network. Deprecated, not used in the new tests.This item is deprecated!  
`UNKNOWN_PROJECT` | Aborted because no project information can be derived from the test input. Deprecated, not used in the new tests.This item is deprecated!  
`NO_EXTERNAL_IP` | Aborted because traffic is sent from a public IP to an instance without an external IP. Deprecated, not used in the new tests.This item is deprecated!  
`UNINTENDED_DESTINATION` | Aborted because none of the traces matches destination information specified in the input test request. Deprecated, not used in the new tests.This item is deprecated!  
`SOURCE_ENDPOINT_NOT_FOUND` | Aborted because the source endpoint could not be found. Deprecated, not used in the new tests.This item is deprecated!  
`MISMATCHED_SOURCE_NETWORK` | Aborted because the source network does not match the source endpoint. Deprecated, not used in the new tests.This item is deprecated!  
`DESTINATION_ENDPOINT_NOT_FOUND` | Aborted because the destination endpoint could not be found. Deprecated, not used in the new tests.This item is deprecated!  
`MISMATCHED_DESTINATION_NETWORK` | Aborted because the destination network does not match the destination endpoint. Deprecated, not used in the new tests.This item is deprecated!  
`UNKNOWN_IP` | Aborted because no endpoint with the packet's destination IP address is found.  
`GOOGLE_MANAGED_SERVICE_UNKNOWN_IP` | Aborted because no endpoint with the packet's destination IP is found in the Google-managed project.  
`SOURCE_IP_ADDRESS_NOT_IN_SOURCE_NETWORK` | Aborted because the source IP address doesn't belong to any of the subnets of the source VPC network.  
`PERMISSION_DENIED` | Aborted because user lacks permission to access all or part of the network configurations required to run the test.  
`PERMISSION_DENIED_NO_CLOUD_NAT_CONFIGS` | Aborted because user lacks permission to access Cloud NAT configs required to run the test.  
`PERMISSION_DENIED_NO_NEG_ENDPOINT_CONFIGS` | Aborted because user lacks permission to access Network endpoint group endpoint configs required to run the test.  
`PERMISSION_DENIED_NO_CLOUD_ROUTER_CONFIGS` | Aborted because user lacks permission to access Cloud Router configs required to run the test.  
`NO_SOURCE_LOCATION` | Aborted because no valid source or destination endpoint can be derived from the test request.  
`NO_SOURCE_GCP_NETWORK_LOCATION` | Aborted because the source IP address is not contained within the subnet ranges of the provided VPC network.  
`NO_SOURCE_NON_GCP_NETWORK_LOCATION` | Aborted because the source IP address is not contained within the destination ranges of the routes towards non-GCP networks in the provided VPC network.  
`NO_SOURCE_INTERNET_LOCATION` | Aborted because the source IP address can't be resolved as an Internet IP address.  
`INVALID_ARGUMENT` | Aborted because the source or destination endpoint specified in the request is invalid. Some examples: - The request might contain malformed resource URI, project ID, or IP address. - The request might contain inconsistent information (for example, the request might include both the instance and the network, but the instance might not have a NIC in that network).  
`TRACE_TOO_LONG` | Aborted because the number of steps in the trace exceeds a certain limit. It might be caused by a routing loop.  
`INTERNAL_ERROR` | Aborted due to internal server error.  
`UNSUPPORTED` | Aborted because the test scenario is not supported.  
`MISMATCHED_IP_VERSION` | Aborted because the source and destination resources have no common IP version.  
`GKE_KONNECTIVITY_PROXY_UNSUPPORTED` | Aborted because the connection between the control plane and the node of the source cluster is initiated by the node and managed by the Konnectivity proxy.  
`RESOURCE_CONFIG_NOT_FOUND` | Aborted because expected resource configuration was missing.  
`VM_INSTANCE_CONFIG_NOT_FOUND` | Aborted because expected VM instance configuration was missing.  
`NETWORK_CONFIG_NOT_FOUND` | Aborted because expected network configuration was missing.  
`FIREWALL_CONFIG_NOT_FOUND` | Aborted because expected firewall configuration was missing.  
`ROUTE_CONFIG_NOT_FOUND` | Aborted because expected route configuration was missing.  
`GOOGLE_MANAGED_SERVICE_AMBIGUOUS_PSC_ENDPOINT` | Aborted because PSC endpoint selection for the Google-managed service is ambiguous (several PSC endpoints satisfy test input).  
`GOOGLE_MANAGED_SERVICE_AMBIGUOUS_ENDPOINT` | Aborted because endpoint selection for the Google-managed service is ambiguous (several endpoints satisfy test input).  
`SOURCE_PSC_CLOUD_SQL_UNSUPPORTED` | Aborted because tests with a PSC-based Cloud SQL instance as a source are not supported.  
`SOURCE_EXTERNAL_CLOUD_SQL_UNSUPPORTED` | Aborted because tests with the external database as a source are not supported. In such replication scenarios, the connection is initiated by the Cloud SQL replica instance.  
`SOURCE_REDIS_CLUSTER_UNSUPPORTED` | Aborted because tests with a Redis Cluster as a source are not supported.  
`SOURCE_REDIS_INSTANCE_UNSUPPORTED` | Aborted because tests with a Redis Instance as a source are not supported.  
`SOURCE_FORWARDING_RULE_UNSUPPORTED` | Aborted because tests with a forwarding rule as a source are not supported.  
`NON_ROUTABLE_IP_ADDRESS` | Aborted because one of the endpoints is a non-routable IP address (loopback, link-local, etc).  
`UNKNOWN_ISSUE_IN_GOOGLE_MANAGED_PROJECT` | Aborted due to an unknown issue in the Google-managed project.  
`UNSUPPORTED_GOOGLE_MANAGED_PROJECT_CONFIG` | Aborted due to an unsupported configuration of the Google-managed project.  
`NO_SERVERLESS_IP_RANGES` | Aborted because the source endpoint is a Cloud Run revision with direct VPC access enabled, but there are no reserved serverless IP ranges.  
`IP_VERSION_PROTOCOL_MISMATCH` | Aborted because the used protocol is not supported for the used IP version.  
`GKE_POD_UNKNOWN_ENDPOINT_LOCATION` | Aborted because selected GKE Pod endpoint location is unknown. This is often the case for "Pending" Pods, which don't have assigned IP addresses yet.  
`RESPONSE_TOO_LARGE` | Aborted because the response size exceeds the limit.  
  
## DropInfo

Details of the final state "drop" and associated resource.

JSON representation  
---  
      
    
    {
      "cause": enum ([Cause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Cause_1)),
      "resourceUri": string,
      "sourceIp": string,
      "destinationIp": string,
      "region": string,
      "sourceGeolocationCode": string,
      "destinationGeolocationCode": string
    }  
  
Fields  
---  
`cause` |  `enum (`[Cause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Cause_1)`)` Cause that the packet is dropped.  
`resourceUri` |  `string` URI of the resource that caused the drop. Format: * `projects/{projectId}/global/firewalls/{firewall_id}` (firewall rule) * `projects/{projectId}/global/routes/{route_id}` (route)  
`sourceIp` |  `string` Source IP address of the dropped packet (if relevant).  
`destinationIp` |  `string` Destination IP address of the dropped packet (if relevant).  
`region` |  `string` Region of the dropped packet (if relevant).  
`sourceGeolocationCode` |  `string` Geolocation (region code) of the source IP address (if relevant).  
`destinationGeolocationCode` |  `string` Geolocation (region code) of the destination IP address (if relevant).  
  
## Cause

Drop cause types:

Enums  
---  
`CAUSE_UNSPECIFIED` | Cause is unspecified.  
`UNKNOWN_EXTERNAL_ADDRESS` | Destination external address cannot be resolved to a known target. If the address is used in a Google Cloud project, provide the project ID as test input.  
`FOREIGN_IP_DISALLOWED` | A Compute Engine instance can only send or receive a packet with a foreign IP address if ip_forward is enabled.  
`FIREWALL_RULE` | Dropped due to a firewall rule, unless allowed due to connection tracking.  
`NO_ROUTE` | Dropped due to no matching routes.  
`ROUTE_BLACKHOLE` | Dropped due to invalid route. Route's next hop is a blackhole.  
`ROUTE_WRONG_NETWORK` | Packet is sent to a wrong (unintended) network. Example: you trace a packet from VM1:Network1 to VM2:Network2, however, the route configured in Network1 sends the packet destined for VM2's IP address to Network3.  
`ROUTE_NEXT_HOP_IP_ADDRESS_NOT_RESOLVED` | Route's next hop IP address cannot be resolved to a GCP resource.  
`ROUTE_NEXT_HOP_RESOURCE_NOT_FOUND` | Route's next hop resource is not found.  
`ROUTE_NEXT_HOP_INSTANCE_WRONG_NETWORK` | Route's next hop instance doesn't have a NIC in the route's network.  
`ROUTE_NEXT_HOP_INSTANCE_NON_PRIMARY_IP` | Route's next hop IP address is not a primary IP address of the next hop instance.  
`ROUTE_NEXT_HOP_FORWARDING_RULE_IP_MISMATCH` | Route's next hop forwarding rule doesn't match next hop IP address.  
`ROUTE_NEXT_HOP_VPN_TUNNEL_NOT_ESTABLISHED` | Route's next hop VPN tunnel is down (does not have valid IKE SAs).  
`ROUTE_NEXT_HOP_FORWARDING_RULE_TYPE_INVALID` | Route's next hop forwarding rule type is invalid (it's not a forwarding rule of the internal passthrough load balancer).  
`NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV6_ADDRESS` | Packet is sent from the Internet to the private IPv6 address.  
`NO_ROUTE_FROM_INTERNET_TO_PRIVATE_IPV4_ADDRESS` | Packet is sent from the Internet to the private IPv4 address.  
`NO_ROUTE_FROM_EXTERNAL_IPV6_SOURCE_TO_PRIVATE_IPV6_ADDRESS` | Packet is sent from the external IPv6 source address of an instance to the private IPv6 address of an instance.  
`VPN_TUNNEL_LOCAL_SELECTOR_MISMATCH` | The packet does not match a policy-based VPN tunnel local selector.  
`VPN_TUNNEL_REMOTE_SELECTOR_MISMATCH` | The packet does not match a policy-based VPN tunnel remote selector.  
`PRIVATE_TRAFFIC_TO_INTERNET` | Packet with internal destination address sent to the internet gateway.  
`PRIVATE_GOOGLE_ACCESS_DISALLOWED` | Endpoint with only an internal IP address tries to access Google API and services, but Private Google Access is not enabled in the subnet or is not applicable.  
`PRIVATE_GOOGLE_ACCESS_VIA_VPN_TUNNEL_UNSUPPORTED` | Source endpoint tries to access Google API and services through the VPN tunnel to another network, but Private Google Access needs to be enabled in the source endpoint network.  
`NO_EXTERNAL_ADDRESS` | Endpoint with only an internal IP address tries to access external hosts, but there is no matching Cloud NAT gateway in the subnet.  
`UNKNOWN_INTERNAL_ADDRESS` | Destination internal address cannot be resolved to a known target. If this is a shared VPC scenario, verify if the service project ID is provided as test input. Otherwise, verify if the IP address is being used in the project.  
`FORWARDING_RULE_MISMATCH` | Forwarding rule's protocol and ports do not match the packet header.  
`FORWARDING_RULE_NO_INSTANCES` | Forwarding rule does not have backends configured.  
`FIREWALL_BLOCKING_LOAD_BALANCER_BACKEND_HEALTH_CHECK` | Firewalls block the health check probes to the backends and cause the backends to be unavailable for traffic from the load balancer. For more details, see [Health check firewall rules](https://cloud.google.com/load-balancing/docs/health-checks#firewall_rules).  
`FIREWALL_BLOCKING_LOAD_BALANCER_ENVOY_PROXY_HEALTH_CHECK` | Firewalls block health check probes to the Envoy proxies that power this load balancer.  
`INGRESS_FIREWALL_TAGS_UNSUPPORTED_BY_DIRECT_VPC_EGRESS` | Matching ingress firewall rules by network tags for packets sent via serverless VPC direct egress is unsupported. Behavior is undefined. <https://cloud.google.com/run/docs/configuring/vpc-direct-vpc#limitations>  
`INSTANCE_NOT_RUNNING` | Packet is sent from or to a Compute Engine instance that is not in a running state.  
`GKE_CLUSTER_NOT_RUNNING` | Packet sent from or to a GKE cluster that is not in running state.  
`GKE_POD_NOT_RUNNING` | Packet sent from or to a GKE Pod that is not in running state.  
`CLOUD_SQL_INSTANCE_NOT_RUNNING` | Packet sent from or to a Cloud SQL instance that is not in running state.  
`REDIS_INSTANCE_NOT_RUNNING` | Packet sent from or to a Redis Instance that is not in running state.  
`REDIS_CLUSTER_NOT_RUNNING` | Packet sent from or to a Redis Cluster that is not in running state.  
`TRAFFIC_TYPE_BLOCKED` | The type of traffic is blocked and the user cannot configure a firewall rule to enable it. See [Always blocked traffic](https://cloud.google.com/vpc/docs/firewalls#blockedtraffic) for more details.  
`GKE_MASTER_UNAUTHORIZED_ACCESS` | Access to Google Kubernetes Engine cluster master's endpoint is not authorized. See [Access to the cluster endpoints](https://cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#access_to_the_cluster_endpoints) for more details.  
`CLOUD_SQL_INSTANCE_UNAUTHORIZED_ACCESS` | Access to the Cloud SQL instance endpoint is not authorized. See [Authorizing with authorized networks](https://cloud.google.com/sql/docs/mysql/authorize-networks) for more details.  
`DROPPED_INSIDE_GKE_SERVICE` | Packet was dropped inside Google Kubernetes Engine Service.  
`DROPPED_INSIDE_CLOUD_SQL_SERVICE` | Packet was dropped inside Cloud SQL Service.  
`DROPPED_INSIDE_DMS_PRIVATE_CONNECTION` | Packet was dropped inside DMS Private Connection.  
`DROPPED_INSIDE_DATASTREAM_PRIVATE_CONNECTION` | Packet was dropped inside Datastream Private Connection.  
`GOOGLE_MANAGED_SERVICE_NO_PEERING` | Packet was dropped because there is no peering between the originating network and the Google Managed Services Network.  
`GOOGLE_MANAGED_SERVICE_NO_PSC_ENDPOINT` | Packet was dropped because the Google-managed service uses Private Service Connect (PSC), but the PSC endpoint is not found in the project.  
`GKE_PSC_ENDPOINT_MISSING` | Packet was dropped because the GKE cluster uses Private Service Connect (PSC), but the PSC endpoint is not found in the project.  
`CLOUD_SQL_INSTANCE_NO_IP_ADDRESS` | Packet was dropped because the Cloud SQL instance has neither a private nor a public IP address.  
`GKE_CONTROL_PLANE_REGION_MISMATCH` | Packet was dropped because a GKE cluster private endpoint is unreachable from a region different from the cluster's region.  
`PUBLIC_GKE_CONTROL_PLANE_TO_PRIVATE_DESTINATION` | Packet sent from a public GKE cluster control plane to a private IP address.  
`GKE_CONTROL_PLANE_NO_ROUTE` | Packet was dropped because there is no route from a GKE cluster control plane to a destination network.  
`CLOUD_SQL_INSTANCE_NOT_CONFIGURED_FOR_EXTERNAL_TRAFFIC` | Packet sent from a Cloud SQL instance to an external IP address is not allowed. The Cloud SQL instance is not configured to send packets to external IP addresses.  
`PUBLIC_CLOUD_SQL_INSTANCE_TO_PRIVATE_DESTINATION` | Packet sent from a Cloud SQL instance with only a public IP address to a private IP address.  
`CLOUD_SQL_INSTANCE_NO_ROUTE` | Packet was dropped because there is no route from a Cloud SQL instance to a destination network.  
`CLOUD_SQL_CONNECTOR_REQUIRED` | Packet was dropped because the Cloud SQL instance requires all connections to use Cloud SQL connectors and to target the Cloud SQL proxy port (3307).  
`CLOUD_FUNCTION_NOT_ACTIVE` | Packet could be dropped because the Cloud Function is not in an active status.  
`VPC_CONNECTOR_NOT_SET` | Packet could be dropped because no VPC connector is set.  
`VPC_CONNECTOR_NOT_RUNNING` | Packet could be dropped because the VPC connector is not in a running state.  
`VPC_CONNECTOR_SERVERLESS_TRAFFIC_BLOCKED` | Packet could be dropped because the traffic from the serverless service to the VPC connector is not allowed.  
`VPC_CONNECTOR_HEALTH_CHECK_TRAFFIC_BLOCKED` | Packet could be dropped because the health check traffic to the VPC connector is not allowed.  
`FORWARDING_RULE_REGION_MISMATCH` | Packet could be dropped because it was sent from a different region to a regional forwarding without global access.  
`PSC_CONNECTION_NOT_ACCEPTED` | The Private Service Connect endpoint is in a project that is not approved to connect to the service.  
`PSC_ENDPOINT_ACCESSED_FROM_PEERED_NETWORK` | The packet is sent to the Private Service Connect endpoint over the peering, but [it's not supported](https://cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises).  
`PSC_NEG_PRODUCER_ENDPOINT_NO_GLOBAL_ACCESS` | The packet is sent to the Private Service Connect backend (network endpoint group), but the producer PSC forwarding rule does not have global access enabled.  
`PSC_NEG_PRODUCER_FORWARDING_RULE_MULTIPLE_PORTS` | The packet is sent to the Private Service Connect backend (network endpoint group), but the producer PSC forwarding rule has multiple ports specified.  
`CLOUD_SQL_PSC_NEG_UNSUPPORTED` | The packet is sent to the Private Service Connect backend (network endpoint group) targeting a Cloud SQL service attachment, but this configuration is not supported.  
`NO_NAT_SUBNETS_FOR_PSC_SERVICE_ATTACHMENT` | No NAT subnets are defined for the PSC service attachment.  
`PSC_TRANSITIVITY_NOT_PROPAGATED` | PSC endpoint is accessed via NCC, but PSC transitivity configuration is not yet propagated.  
`HYBRID_NEG_NON_DYNAMIC_ROUTE_MATCHED` | The packet sent from the hybrid NEG proxy matches a non-dynamic route, but such a configuration is not supported.  
`HYBRID_NEG_NON_LOCAL_DYNAMIC_ROUTE_MATCHED` | The packet sent from the hybrid NEG proxy matches a dynamic route with a next hop in a different region, but such a configuration is not supported.  
`CLOUD_RUN_REVISION_NOT_READY` | Packet sent from a Cloud Run revision that is not ready.  
`CLOUD_RUN_JOB_NOT_READY` | Packet sent from a Cloud Run job that is not ready.  
`DROPPED_INSIDE_PSC_SERVICE_PRODUCER` | Packet was dropped inside Private Service Connect service producer.  
`LOAD_BALANCER_HAS_NO_PROXY_SUBNET` | Packet sent to a load balancer, which requires a proxy-only subnet and the subnet is not found.  
`CLOUD_NAT_NO_ADDRESSES` | Packet sent to Cloud Nat without active NAT IPs.  
`ROUTING_LOOP` | Packet is stuck in a routing loop.  
`DROPPED_INSIDE_GOOGLE_MANAGED_SERVICE` | Packet is dropped inside a Google-managed service due to being delivered in return trace to an endpoint that doesn't match the endpoint the packet was sent from in forward trace. Used only for return traces.  
`LOAD_BALANCER_BACKEND_INVALID_NETWORK` | Packet is dropped due to a load balancer backend instance not having a network interface in the network expected by the load balancer.  
`BACKEND_SERVICE_NAMED_PORT_NOT_DEFINED` | Packet is dropped due to a backend service named port not being defined on the instance group level.  
`DESTINATION_IS_PRIVATE_NAT_IP_RANGE` | Packet is dropped due to a destination IP range being part of a Private NAT IP range.  
`DROPPED_INSIDE_REDIS_INSTANCE_SERVICE` | Generic drop cause for a packet being dropped inside a Redis Instance service project.  
`REDIS_INSTANCE_UNSUPPORTED_PORT` | Packet is dropped due to an unsupported port being used to connect to a Redis Instance. Port 6379 should be used to connect to a Redis Instance.  
`REDIS_INSTANCE_CONNECTING_FROM_PUPI_ADDRESS` | Packet is dropped due to connecting from PUPI address to a PSA based Redis Instance.  
`REDIS_INSTANCE_NO_ROUTE_TO_DESTINATION_NETWORK` | Packet is dropped due to no route to the destination network.  
`REDIS_INSTANCE_NO_EXTERNAL_IP` | Redis Instance does not have an external IP address.  
`REDIS_INSTANCE_UNSUPPORTED_PROTOCOL` | Packet is dropped due to an unsupported protocol being used to connect to a Redis Instance. Only TCP connections are accepted by a Redis Instance.  
`DROPPED_INSIDE_REDIS_CLUSTER_SERVICE` | Generic drop cause for a packet being dropped inside a Redis Cluster service project.  
`REDIS_CLUSTER_UNSUPPORTED_PORT` | Packet is dropped due to an unsupported port being used to connect to a Redis Cluster. Ports 6379 and 11000 to 13047 should be used to connect to a Redis Cluster.  
`REDIS_CLUSTER_NO_EXTERNAL_IP` | Redis Cluster does not have an external IP address.  
`REDIS_CLUSTER_UNSUPPORTED_PROTOCOL` | Packet is dropped due to an unsupported protocol being used to connect to a Redis Cluster. Only TCP connections are accepted by a Redis Cluster.  
`NO_ADVERTISED_ROUTE_TO_GCP_DESTINATION` | Packet from the non-GCP (on-prem) or unknown GCP network is dropped due to the destination IP address not belonging to any IP prefix advertised via BGP by the Cloud Router.  
`NO_TRAFFIC_SELECTOR_TO_GCP_DESTINATION` | Packet from the non-GCP (on-prem) or unknown GCP network is dropped due to the destination IP address not belonging to any IP prefix included to the local traffic selector of the VPN tunnel.  
`NO_KNOWN_ROUTE_FROM_PEERED_NETWORK_TO_DESTINATION` | Packet from the unknown peered network is dropped due to no known route from the source network to the destination IP address.  
`PRIVATE_NAT_TO_PSC_ENDPOINT_UNSUPPORTED` | Sending packets processed by the Private NAT Gateways to the Private Service Connect endpoints is not supported.  
`PSC_PORT_MAPPING_PORT_MISMATCH` | Packet is sent to the PSC port mapping service, but its destination port does not match any port mapping rules.  
`PSC_PORT_MAPPING_WITHOUT_PSC_CONNECTION_UNSUPPORTED` | Sending packets directly to the PSC port mapping service without going through the PSC connection is not supported.  
`UNSUPPORTED_ROUTE_MATCHED_FOR_NAT64_DESTINATION` | Packet with destination IP address within the reserved NAT64 range is dropped due to matching a route of an unsupported type.  
`TRAFFIC_FROM_HYBRID_ENDPOINT_TO_INTERNET_DISALLOWED` | Packet could be dropped because hybrid endpoint like a VPN gateway or Interconnect is not allowed to send traffic to the Internet.  
`NO_MATCHING_NAT64_GATEWAY` | Packet with destination IP address within the reserved NAT64 range is dropped due to no matching NAT gateway in the subnet.  
`NO_CONFIGURED_PRIVATE_NAT64_RULE` | Packet is dropped due to matching a Private NAT64 gateway with no rules for source IPv6 addresses.  
`LOAD_BALANCER_BACKEND_IP_VERSION_MISMATCH` | Packet is dropped due to being sent to a backend of a passthrough load balancer that doesn't use the same IP version as the frontend.  
`NO_KNOWN_ROUTE_FROM_NCC_NETWORK_TO_DESTINATION` | Packet from the unknown NCC network is dropped due to no known route from the source network to the destination IP address.  
`CLOUD_NAT_PROTOCOL_UNSUPPORTED` | Packet is dropped by Cloud NAT due to using an unsupported protocol.  
`L2_INTERCONNECT_UNSUPPORTED_PROTOCOL` | Packet is dropped due to using an unsupported protocol (any other than UDP) for L2 Interconnect.  
`L2_INTERCONNECT_UNSUPPORTED_PORT` | Packet is dropped due to using an unsupported port (any other than 6081) for L2 Interconnect.  
`L2_INTERCONNECT_DESTINATION_IP_MISMATCH` | Packet is dropped due to destination IP not matching the appliance mapping IPs configured on the L2 Interconnect attachment.  
`NCC_ROUTE_WITHIN_HYBRID_SUBNET_UNSUPPORTED` | Packet could be dropped because it matches a route associated with an NCC spoke in the hybrid subnet context, but such a configuration is not supported.  
`HYBRID_SUBNET_REGION_MISMATCH` | Packet is dropped because the region of the hybrid subnet is different from the region of the next hop of the route matched within this hybrid subnet.  
`HYBRID_SUBNET_NO_ROUTE` | Packet is dropped because no matching route was found in the hybrid subnet.  
`GKE_NETWORK_POLICY` | Packet is dropped by GKE Network Policy.  
`NO_VALID_ROUTE_FROM_GOOGLE_MANAGED_NETWORK_TO_DESTINATION` | Packet is dropped because there is no valid matching route from the network of the Google-managed service to the destination.  
`PRIVATE_CONNECTION_NO_RUNNING_INSTANCE` | Packet is dropped due to no running instance found for private connection.  
  
## LoadBalancerInfo

For display only. Metadata associated with a load balancer.

JSON representation  
---  
      
    
    {
      "loadBalancerType": enum ([LoadBalancerType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerType_1)),
      "healthCheckUri": string,
      "backends": [
        {
          object ([LoadBalancerBackend](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerBackend))
        }
      ],
      "backendType": enum ([BackendType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#BackendType)),
      "backendUri": string
    }  
  
Fields  
---  
`loadBalancerType` |  `enum (`[LoadBalancerType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerType_1)`)` Type of the load balancer.  
`healthCheckUri  
**(deprecated)**` |  `string` This item is deprecated!URI of the health check for the load balancer. Deprecated and no longer populated as different load balancer backends might have different health checks.  
`backends[]` |  `object (`[LoadBalancerBackend](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LoadBalancerBackend)`)` Information for the loadbalancer backends.  
`backendType` |  `enum (`[BackendType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#BackendType)`)` Type of load balancer's backend configuration.  
`backendUri` |  `string` URI of the backend associated with the load balancer. Format: * `projects/{projectId}/regions/{region}/backendServices/{backend_service_id}` * `projects/{projectId}/global/backendServices/{backend_service_id}` * `projects/{projectId}/regions/{region}/targetPools/{target_pool_id}` * `projects/{projectId}/zones/{zone}/targetInstances/{target_instance_id}`  
  
## LoadBalancerType

The type definition for a load balancer:

Enums  
---  
`LOAD_BALANCER_TYPE_UNSPECIFIED` | Type is unspecified.  
`INTERNAL_TCP_UDP` | Internal TCP/UDP load balancer.  
`NETWORK_TCP_UDP` | Network TCP/UDP load balancer.  
`HTTP_PROXY` | HTTP(S) proxy load balancer.  
`TCP_PROXY` | TCP proxy load balancer.  
`SSL_PROXY` | SSL proxy load balancer.  
  
## LoadBalancerBackend

For display only. Metadata associated with a specific load balancer backend.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "healthCheckFirewallState": enum ([HealthCheckFirewallState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HealthCheckFirewallState)),
      "healthCheckAllowingFirewallRules": [
        string
      ],
      "healthCheckBlockingFirewallRules": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine instance or network endpoint.  
`uri` |  `string` URI of the backend instance or network endpoint. Format: * `projects/{projectId}/zones/{zone}/instances/{instance_id}` (instance) * `projects/{projectId}/zones/{zone}/networkEndpointGroups/{neg_id}` (zonal NEG) * `projects/{projectId}/regions/{region}/networkEndpointGroups/{neg_id}` (regional NEG) * `projects/{projectId}/global/networkEndpointGroups/{neg_id}` (global NEG)  
`healthCheckFirewallState` |  `enum (`[HealthCheckFirewallState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HealthCheckFirewallState)`)` State of the health check firewall configuration.  
`healthCheckAllowingFirewallRules[]` |  `string` A list of firewall rule URIs allowing probes from health check IP ranges.  
`healthCheckBlockingFirewallRules[]` |  `string` A list of firewall rule URIs blocking probes from health check IP ranges.  
  
## HealthCheckFirewallState

State of a health check firewall configuration:

Enums  
---  
`HEALTH_CHECK_FIREWALL_STATE_UNSPECIFIED` | State is unspecified. Default state if not populated.  
`CONFIGURED` | There are configured firewall rules to allow health check probes to the backend.  
`MISCONFIGURED` | There are firewall rules configured to allow partial health check ranges or block all health check ranges. If a health check probe is sent from denied IP ranges, the health check to the backend will fail. Then, the backend will be marked unhealthy and will not receive traffic sent to the load balancer.  
  
## BackendType

The type definition for a load balancer backend configuration:

Enums  
---  
`BACKEND_TYPE_UNSPECIFIED` | Type is unspecified.  
`BACKEND_SERVICE` | Backend Service as the load balancer's backend.  
`TARGET_POOL` | Target Pool as the load balancer's backend.  
`TARGET_INSTANCE` | Target Instance as the load balancer's backend.  
  
## NetworkInfo

For display only. Metadata associated with a Compute Engine network.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "matchedSubnetUri": string,
      "matchedIpRange": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine network.  
`uri` |  `string` URI of a Compute Engine network in format "projects/{project}/global/networks/{network}"  
`matchedSubnetUri` |  `string` URI of the subnet matching the source IP address of the test in format "projects/{project}/regions/{region}/subnetworks/{subnetwork}"  
`matchedIpRange` |  `string` The IP range of the subnet matching the source IP address of the test.  
`region` |  `string` The region of the subnet matching the source IP address of the test.  
  
## GKEMasterInfo

For display only. Metadata associated with a Google Kubernetes Engine (GKE) cluster master.

JSON representation  
---  
      
    
    {
      "clusterUri": string,
      "clusterNetworkUri": string,
      "internalIp": string,
      "externalIp": string,
      "dnsEndpoint": string
    }  
  
Fields  
---  
`clusterUri` |  `string` URI of the GKE cluster. Format: * `projects/{projectId}/locations/{location}/clusters/{cluster_id}` (regional cluster) * `projects/{projectId}/zones/{zone}/clusters/{cluster_id}` (zonal cluster)  
`clusterNetworkUri` |  `string` URI of the GKE cluster network. Format: `projects/{projectId}/global/networks/{network_id}`  
`internalIp` |  `string` Internal IP address of a GKE cluster control plane.  
`externalIp` |  `string` External IP address of a GKE cluster control plane.  
`dnsEndpoint` |  `string` DNS endpoint of a GKE cluster control plane.  
  
## GkePodInfo

For display only. Metadata associated with a Google Kubernetes Engine (GKE) Pod.

JSON representation  
---  
      
    
    {
      "podUri": string,
      "ipAddress": string,
      "networkUri": string
    }  
  
Fields  
---  
`podUri` |  `string` URI of a GKE Pod. For Pods in regional Clusters, the URI format is: `projects/{project}/locations/{location}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}` For Pods in zonal Clusters, the URI format is: `projects/{project}/zones/{zone}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}`  
`ipAddress` |  `string` IP address of a GKE Pod. If the Pod is dual-stack, this is the IP address relevant to the trace.  
`networkUri` |  `string` URI of the network containing the GKE Pod. Format: `projects/{projectId}/global/networks/{network_id}`  
  
## IpMasqueradingSkippedInfo

For display only. Contains information about why IP masquerading was skipped for the packet.

JSON representation  
---  
      
    
    {
      "reason": enum ([Reason](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Reason)),
      "nonMasqueradeRange": string
    }  
  
Fields  
---  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Reason)`)` Reason why IP masquerading was not applied.  
`nonMasqueradeRange` |  `string` The matched non-masquerade IP range. Only set if reason is DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE or DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE.  
  
## Reason

Reason why IP masquerading was skipped.

Enums  
---  
`REASON_UNSPECIFIED` | Unused default value.  
`DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE` | Masquerading not applied because destination IP is in one of configured non-masquerade ranges.  
`DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE` | Masquerading not applied because destination IP is in one of default non-masquerade ranges.  
`DESTINATION_ON_SAME_NODE` | Masquerading not applied because destination is on the same Node.  
`DEFAULT_SNAT_DISABLED` | Masquerading not applied because ip-masq-agent doesn't exist and default SNAT is disabled.  
`NO_MASQUERADING_FOR_IPV6` | Masquerading not applied because the packet's IP version is IPv6.  
`POD_USES_NODE_NETWORK_NAMESPACE` | Masquerading not applied because the source Pod uses the host Node's network namespace, including the Node's IP address.  
`NO_MASQUERADING_FOR_RETURN_PACKET` | Masquerading not applied because the packet is a return packet.  
  
## GkeNetworkPolicyInfo

For display only. Metadata associated with a GKE Network Policy.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "direction": string,
      "action": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the Network Policy.  
`uri` |  `string` The URI of the Network Policy. Format for a Network Policy in a zonal cluster: `projects/<projectId>/zones/<zone>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>` Format for a Network Policy in a regional cluster: `projects/<projectId>/locations/<location>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>`  
`direction` |  `string` Possible values: INGRESS, EGRESS  
`action` |  `string` Possible values: ALLOW, DENY  
  
## GkeNetworkPolicySkippedInfo

For display only. Contains information about why GKE Network Policy evaluation was skipped.

JSON representation  
---  
      
    
    {
      "reason": enum ([Reason](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Reason_1))
    }  
  
Fields  
---  
`reason` |  `enum (`[Reason](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Reason_1)`)` Reason why Network Policy evaluation was skipped.  
  
## Reason

Enums  
---  
`REASON_UNSPECIFIED` | Unused default value.  
`NETWORK_POLICY_DISABLED` | Network Policy is disabled on the cluster.  
`INGRESS_SOURCE_ON_SAME_NODE` | Ingress traffic to a Pod from a source on the same Node is always allowed.  
`EGRESS_FROM_NODE_NETWORK_NAMESPACE_POD` | Egress traffic from a Pod that uses the Node's network namespace is not subject to Network Policy.  
`NETWORK_POLICY_NOT_APPLIED_TO_RESPONSE_TRAFFIC` | Network Policy is not applied to response traffic. This is because GKE Network Policy evaluation is stateful in both GKE Dataplane V2 (eBPF) and legacy (iptables) implementations.  
`NETWORK_POLICY_ANALYSIS_UNSUPPORTED` | Network Policy evaluation is currently not supported for clusters with FQDN Network Policies enabled.  
  
## CloudSQLInstanceInfo

For display only. Metadata associated with a Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "internalIp": string,
      "externalIp": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud SQL instance.  
`uri` |  `string` URI of a Cloud SQL instance in format "projects/{project}/instances/{instance}"  
`networkUri` |  `string` URI of a Cloud SQL instance network or empty string if the instance does not have one. In format "projects/{project}/global/networks/{network}".  
`internalIp` |  `string` Internal IP address of a Cloud SQL instance.  
`externalIp` |  `string` External IP address of a Cloud SQL instance.  
`region` |  `string` Region in which the Cloud SQL instance is running.  
  
## RedisInstanceInfo

For display only. Metadata associated with a Cloud Redis Instance.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "primaryEndpointIp": string,
      "readEndpointIp": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Redis Instance.  
`uri` |  `string` URI of a Cloud Redis Instance in format "projects/{project}/locations/{location}/instances/{instance}"  
`networkUri` |  `string` URI of a Cloud Redis Instance network in format "projects/{project}/global/networks/{network}".  
`primaryEndpointIp` |  `string` Primary endpoint IP address of a Cloud Redis Instance.  
`readEndpointIp` |  `string` Read endpoint IP address of a Cloud Redis Instance (if applicable).  
`region` |  `string` Region in which the Cloud Redis Instance is defined.  
  
## RedisClusterInfo

For display only. Metadata associated with a Redis Cluster.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "discoveryEndpointIpAddress": string,
      "secondaryEndpointIpAddress": string,
      "location": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Redis Cluster.  
`uri` |  `string` URI of a Redis Cluster in format "projects/{projectId}/locations/{location}/clusters/{cluster_id}"  
`networkUri` |  `string` URI of the network containing the Redis Cluster endpoints in format "projects/{projectId}/global/networks/{network_id}".  
`discoveryEndpointIpAddress` |  `string` Discovery endpoint IP address of a Redis Cluster.  
`secondaryEndpointIpAddress` |  `string` Secondary endpoint IP address of a Redis Cluster.  
`location` |  `string` Name of the region in which the Redis Cluster is defined. For example, "us-central1".  
  
## CloudFunctionInfo

For display only. Metadata associated with a Cloud Function.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string,
      "versionId": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Function.  
`uri` |  `string` URI of the Cloud Function. Format: `projects/{projectId}/locations/{location}/functions/{function_id}`  
`location` |  `string` Location in which the Cloud Function is deployed.  
`versionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Latest successfully deployed version id of the Cloud Function.  
  
## AppEngineVersionInfo

For display only. Metadata associated with an App Engine version.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "runtime": string,
      "environment": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of an App Engine version.  
`uri` |  `string` URI of the App Engine version. Format: `apps/{app_id}/services/{service_id}/versions/{versionId}`  
`runtime` |  `string` Runtime of the App Engine version.  
`environment` |  `string` App Engine execution environment for a version.  
  
## CloudRunRevisionInfo

For display only. Metadata associated with a Cloud Run revision.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string,
      "serviceUri": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Run revision.  
`uri` |  `string` URI of the Cloud Run revision. Format: `projects/{projectId}/locations/{location}/revisions/{revision_id}`  
`location` |  `string` Location in which this revision is deployed.  
`serviceUri` |  `string` URI of Cloud Run service this revision belongs to. Format: `projects/{projectId}/locations/{location}/services/{service_id}`  
  
## CloudRunJobInfo

For display only. Metadata associated with a Cloud Run job.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Run job.  
`uri` |  `string` URI of the Cloud Run job. Format: `projects/{projectId}/locations/{location}/jobs/{job_id}`  
`location` |  `string` Location in which this job is deployed.  
  
## NatInfo

For display only. Metadata associated with NAT.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Type_1)),
      "protocol": string,
      "networkUri": string,
      "oldSourceIp": string,
      "newSourceIp": string,
      "oldDestinationIp": string,
      "newDestinationIp": string,
      "oldSourcePort": integer,
      "newSourcePort": integer,
      "oldDestinationPort": integer,
      "newDestinationPort": integer,
      "routerUri": string,
      "natGatewayName": string,
      "cloudNatGatewayType": enum ([CloudNatGatewayType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudNatGatewayType))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#Type_1)`)` Type of NAT.  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`networkUri` |  `string` URI of the VPC network where NAT translation takes place. Format: `projects/{projectId}/global/networks/{network_id}`  
`oldSourceIp` |  `string` Source IP address before NAT translation.  
`newSourceIp` |  `string` Source IP address after NAT translation.  
`oldDestinationIp` |  `string` Destination IP address before NAT translation.  
`newDestinationIp` |  `string` Destination IP address after NAT translation.  
`oldSourcePort` |  `integer` Source port before NAT translation. Only valid when protocol is TCP or UDP.  
`newSourcePort` |  `integer` Source port after NAT translation. Only valid when protocol is TCP or UDP.  
`oldDestinationPort` |  `integer` Destination port before NAT translation. Only valid when protocol is TCP or UDP.  
`newDestinationPort` |  `integer` Destination port after NAT translation. Only valid when protocol is TCP or UDP.  
`routerUri` |  `string` URI of the Cloud Router. Only valid when type is CLOUD_NAT. Format: `projects/{projectId}/regions/{region}/routers/{router_id}`  
`natGatewayName` |  `string` The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT.  
`cloudNatGatewayType` |  `enum (`[CloudNatGatewayType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#CloudNatGatewayType)`)` Type of Cloud NAT gateway. Only valid when `type` is CLOUD_NAT.  
  
## Type

Types of NAT.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`INTERNAL_TO_EXTERNAL` | From Compute Engine instance's internal address to external address.  
`EXTERNAL_TO_INTERNAL` | From Compute Engine instance's external address to internal address.  
`CLOUD_NAT` | Cloud NAT Gateway.  
`PRIVATE_SERVICE_CONNECT` | Private service connect NAT.  
`GKE_POD_IP_MASQUERADING` | GKE Pod IP address masquerading.  
  
## CloudNatGatewayType

Types of Cloud NAT gateway.

Enums  
---  
`CLOUD_NAT_GATEWAY_TYPE_UNSPECIFIED` | Type is unspecified.  
`PUBLIC_NAT44` | Public NAT gateway.  
`PUBLIC_NAT64` | Public NAT64 gateway.  
`PRIVATE_NAT_NCC` | Private NAT gateway for NCC.  
`PRIVATE_NAT_HYBRID` | Private NAT gateway for hybrid connectivity.  
`PRIVATE_NAT64` | Private NAT64 gateway.  
  
## ProxyConnectionInfo

For display only. Metadata associated with ProxyConnection.

JSON representation  
---  
      
    
    {
      "protocol": string,
      "oldSourceIp": string,
      "newSourceIp": string,
      "oldDestinationIp": string,
      "newDestinationIp": string,
      "oldSourcePort": integer,
      "newSourcePort": integer,
      "oldDestinationPort": integer,
      "newDestinationPort": integer,
      "subnetUri": string,
      "networkUri": string
    }  
  
Fields  
---  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`oldSourceIp` |  `string` Source IP address of an original connection.  
`newSourceIp` |  `string` Source IP address of a new connection.  
`oldDestinationIp` |  `string` Destination IP address of an original connection  
`newDestinationIp` |  `string` Destination IP address of a new connection.  
`oldSourcePort` |  `integer` Source port of an original connection. Only valid when protocol is TCP or UDP.  
`newSourcePort` |  `integer` Source port of a new connection. Only valid when protocol is TCP or UDP.  
`oldDestinationPort` |  `integer` Destination port of an original connection. Only valid when protocol is TCP or UDP.  
`newDestinationPort` |  `integer` Destination port of a new connection. Only valid when protocol is TCP or UDP.  
`subnetUri` |  `string` URI of the proxy subnet. Format: `projects/{projectId}/regions/{region}/subnetworks/{subnetwork_id}`  
`networkUri` |  `string` URI of the VPC network where connection is proxied. Format: `projects/{projectId}/global/networks/{network_id}`  
  
## LoadBalancerBackendInfo

For display only. Metadata associated with the load balancer backend.

JSON representation  
---  
      
    
    {
      "name": string,
      "instanceUri": string,
      "backendServiceUri": string,
      "instanceGroupUri": string,
      "networkEndpointGroupUri": string,
      "backendBucketUri": string,
      "pscServiceAttachmentUri": string,
      "pscGoogleApiTarget": string,
      "healthCheckUri": string,
      "healthCheckFirewallsConfigState": enum ([HealthCheckFirewallsConfigState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HealthCheckFirewallsConfigState))
    }  
  
Fields  
---  
`name` |  `string` Display name of the backend. For example, it might be an instance name for the instance group backends, or an IP address and port for zonal network endpoint group backends.  
`instanceUri` |  `string` URI of the backend instance (if applicable) in format "projects/{project}/zones/{zone}/instances/{instance}". Populated for instance group backends, and zonal NEG backends.  
`backendServiceUri` |  `string` URI of the backend service this backend belongs to (if applicable) in format "projects/{project}/regions/{region}/backendServices/{backend_service}" (regional) or "projects/{project}/global/backendServices/{backend_service}" (global).  
`instanceGroupUri` |  `string` URI of the instance group this backend belongs to (if applicable) in format "projects/{project}/zones/{zone}/instanceGroups/{instance_group}".  
`networkEndpointGroupUri` |  `string` URI of the network endpoint group this backend belongs to (if applicable) Format: * `projects/{projectId}/zones/{zone}/networkEndpointGroups/{neg_id}` (zonal NEG) * `projects/{projectId}/regions/{region}/networkEndpointGroups/{neg_id}` (regional NEG) * `projects/{projectId}/global/networkEndpointGroups/{neg_id}` (global NEG)  
`backendBucketUri` |  `string` URI of the backend bucket this backend targets (if applicable) in format "projects/{project}/global/backendBuckets/{backend_bucket}".  
`pscServiceAttachmentUri` |  `string` URI of the PSC service attachment this PSC NEG backend targets (if applicable) in format "projects/{project}/regions/{region}/serviceAttachments/{service_attachment}".  
`pscGoogleApiTarget` |  `string` PSC Google API target this PSC NEG backend targets (if applicable).  
`healthCheckUri` |  `string` URI of the health check attached to this backend (if applicable). Format: * `projects/{projectId}/global/healthChecks/{health_check_id}` * `projects/{projectId}/regions/{region}/healthChecks/{health_check_id}` * `projects/{projectId}/global/httpHealthChecks/{health_check_id}` (legacy)  
`healthCheckFirewallsConfigState` |  `enum (`[HealthCheckFirewallsConfigState](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#HealthCheckFirewallsConfigState)`)` Output only. Health check firewalls configuration state for the backend. This is a result of the static firewall analysis (verifying that health check traffic from required IP ranges to the backend is allowed or not). The backend might still be unhealthy even if these firewalls are configured. Please refer to the documentation for more information: <https://cloud.google.com/load-balancing/docs/firewall-rules>  
  
## HealthCheckFirewallsConfigState

Health check firewalls configuration state enum.

Enums  
---  
`HEALTH_CHECK_FIREWALLS_CONFIG_STATE_UNSPECIFIED` | Configuration state unspecified. It usually means that the backend has no health check attached, or there was an unexpected configuration error preventing Connectivity tests from verifying health check configuration.  
`FIREWALLS_CONFIGURED` | Firewall rules (policies) allowing health check traffic from all required IP ranges to the backend are configured.  
`FIREWALLS_PARTIALLY_CONFIGURED` | Firewall rules (policies) allow health check traffic only from a part of required IP ranges.  
`FIREWALLS_NOT_CONFIGURED` | Firewall rules (policies) deny health check traffic from all required IP ranges to the backend.  
`FIREWALLS_UNSUPPORTED` | The network contains firewall rules of unsupported types, so Connectivity tests were not able to verify health check configuration status. Please refer to the documentation for the list of unsupported configurations: <https://cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview#unsupported-configs>  
  
## StorageBucketInfo

For display only. Metadata associated with Storage Bucket.

JSON representation  
---  
      
    
    {
      "bucket": string
    }  
  
Fields  
---  
`bucket` |  `string` Cloud Storage Bucket name.  
  
## ServerlessNegInfo

For display only. Metadata associated with the serverless network endpoint group backend.

JSON representation  
---  
      
    
    {
      "negUri": string
    }  
  
Fields  
---  
`negUri` |  `string` URI of the serverless network endpoint group in format "projects/{project}/regions/{region}/networkEndpointGroups/{network_endpoint_group}".  
  
## NgfwPacketInspectionInfo

For display only. Metadata associated with a layer 7 packet inspection by the firewall.

JSON representation  
---  
      
    
    {
      "securityProfileGroupUri": string
    }  
  
Fields  
---  
`securityProfileGroupUri` |  `string` URI of the security profile group associated with this firewall packet inspection. Format: `organizations/{organization_id}/locations/global/securityProfileGroups/{security_profile_group_id}`  
  
## PrivateConnectionInfo

For display only. Metadata associated with a Private Connection.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` URI of the Private Connection in format "projects/{projectId}/locations/{location}/privateConnections/{private_connection_id}"  
  
## ProbingDetails

Results of active probing from the last run of the test.

JSON representation  
---  
      
    
    {
      "result": enum ([ProbingResult](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingResult)),
      "verifyTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "abortCause": enum ([ProbingAbortCause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingAbortCause)),
      "sentProbeCount": integer,
      "successfulProbeCount": integer,
      "endpointInfo": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo))
      },
      "probingLatency": {
        object ([LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyDistribution))
      },
      "destinationEgressLocation": {
        object ([EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EdgeLocation))
      },
      "edgeResponses": [
        {
          object ([SingleEdgeResponse](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#SingleEdgeResponse))
        }
      ],
      "probedAllDevices": boolean
    }  
  
Fields  
---  
`result` |  `enum (`[ProbingResult](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingResult)`)` The overall result of active probing.  
`verifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that reachability was assessed through active probing.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/Shared.Types/ListOperationsResponse#Status)`)` Details about an internal failure or the cancellation of active probing.  
`abortCause` |  `enum (`[ProbingAbortCause](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingAbortCause)`)` The reason probing was aborted.  
`sentProbeCount` |  `integer` Number of probes sent.  
`successfulProbeCount` |  `integer` Number of probes that reached the destination.  
`endpointInfo` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EndpointInfo)`)` The source and destination endpoints derived from the test input and used for active probing.  
`probingLatency` |  `object (`[LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyDistribution)`)` Latency as measured by active probing in one direction: from the source to the destination endpoint.  
`destinationEgressLocation` |  `object (`[EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EdgeLocation)`)` The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.  
`edgeResponses[]` |  `object (`[SingleEdgeResponse](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#SingleEdgeResponse)`)` Probing results for all edge devices.  
`probedAllDevices` |  `boolean` Whether all relevant edge devices were probed.  
  
## ProbingResult

Overall probing result of the test.

Enums  
---  
`PROBING_RESULT_UNSPECIFIED` | No result was specified.  
`REACHABLE` | At least 95% of packets reached the destination.  
`UNREACHABLE` | No packets reached the destination.  
`REACHABILITY_INCONSISTENT` | Less than 95% of packets reached the destination.  
`UNDETERMINED` | Reachability could not be determined. Possible reasons are: * The user lacks permission to access some of the network resources required to run the test. * No valid source endpoint could be derived from the request. * An internal error occurred.  
  
## ProbingAbortCause

Abort cause types.

Enums  
---  
`PROBING_ABORT_CAUSE_UNSPECIFIED` | No reason was specified.  
`PERMISSION_DENIED` | The user lacks permission to access some of the network resources required to run the test.  
`NO_SOURCE_LOCATION` | No valid source endpoint could be derived from the request.  
  
## LatencyDistribution

Describes measured latency distribution.

JSON representation  
---  
      
    
    {
      "latencyPercentiles": [
        {
          object ([LatencyPercentile](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyPercentile))
        }
      ]
    }  
  
Fields  
---  
`latencyPercentiles[]` |  `object (`[LatencyPercentile](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyPercentile)`)` Representative latency percentiles.  
  
## LatencyPercentile

Latency percentile rank and value.

JSON representation  
---  
      
    
    {
      "percent": integer,
      "latencyMicros": string
    }  
  
Fields  
---  
`percent` |  `integer` Percentage of samples this data point applies to.  
`latencyMicros` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` percent-th percentile of latency observed, in microseconds. Fraction of percent/100 of samples have latency lower or equal to the value of this field.  
  
## EdgeLocation

Representation of a network edge location as per <https://cloud.google.com/vpc/docs/edge-locations>.

JSON representation  
---  
      
    
    {
      "metropolitanArea": string
    }  
  
Fields  
---  
`metropolitanArea` |  `string` Name of the metropolitan area.  
  
## SingleEdgeResponse

Probing results for a single edge device.

JSON representation  
---  
      
    
    {
      "result": enum ([ProbingResult](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingResult)),
      "sentProbeCount": integer,
      "successfulProbeCount": integer,
      "probingLatency": {
        object ([LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyDistribution))
      },
      "destinationEgressLocation": {
        object ([EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EdgeLocation))
      },
      "destinationRouter": string
    }  
  
Fields  
---  
`result` |  `enum (`[ProbingResult](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#ProbingResult)`)` The overall result of active probing for this egress device.  
`sentProbeCount` |  `integer` Number of probes sent.  
`successfulProbeCount` |  `integer` Number of probes that reached the destination.  
`probingLatency` |  `object (`[LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#LatencyDistribution)`)` Latency as measured by active probing in one direction: from the source to the destination endpoint.  
`destinationEgressLocation` |  `object (`[EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests#EdgeLocation)`)` The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.  
`destinationRouter` |  `string` Router name in the format '{router}.{metroshard}'. For example: pf01.aaa01, pr02.aaa01.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/create)`

|  Creates a new Connectivity Test.  
  
### `[delete](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/delete)`

|  Deletes a specific `ConnectivityTest`.  
  
### `[get](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/get)`

|  Gets the details of a specific Connectivity Test.  
  
### `[getIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/list)`

|  Lists all Connectivity Tests owned by a project.  
  
### `[patch](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/patch)`

|  Updates the configuration of an existing `ConnectivityTest`.  
  
### `[rerun](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/rerun)`

|  Rerun an existing `ConnectivityTest`.  
  
### `[setIamPolicy](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.global.connectivityTests/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 
