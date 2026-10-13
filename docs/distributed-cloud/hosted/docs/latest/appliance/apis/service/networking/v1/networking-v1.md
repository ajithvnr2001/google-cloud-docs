---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/v1/networking-v1/
title: KRM API networking.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:03.095854+00:00
---

# KRM API networking.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/networking/v1/networking-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API networking.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## networking.gdc.goog/v1

Package v1 contains API Schema definitions for the networking v1 API group.

### AuthorizationPolicyRef

Represents a reference to the generated authorization policy.

_Appears in:_ \- OrganizationNetworkPolicyStatus

Field | Description  
---|---  
`name` _string_ | The name of the referent.  
`namespace` _string_ | The namespace of the referent.  
  
### BGPPeerInterface

Represents a reference to a BGP peer.

_Appears in:_ \- VPNBGPPeerSpec

Field | Description  
---|---  
`name` _string_ | The name of the BGP peer.  
`ip` _string_ | The IP address of the BGP peer.  
`asn` _integer_ | The Autonomous System Number.  
  
### Backend

Identifies endpoints for a load balancer.

_Appears in:_ \- BackendList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `Backend`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendSpec_ |   
`status` _BackendStatus_ |   
  
### BackendList

Contains list of Backends.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `BackendList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Backend array_ |   
  
### BackendRef

Holds information about the backend.

_Appears in:_ \- BackendServiceSpec

Field | Description  
---|---  
`name` _string_ | A name of the referenced Backend object. The referenced Backend has to be in the same namespace as this backend service. This field is required. This field is immutable.  
  
### BackendService

Represents a load balancer configuration.

_Appears in:_ \- BackendServiceList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `BackendService`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServiceSpec_ |   
`status` _BackendServiceStatus_ |   
  
### BackendServiceList

Contains a list of BackendService.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `BackendServiceList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendService array_ |   
  
### BackendServicePolicy

Represents policies to be applied to one or more load balancers.

_Appears in:_ \- BackendServicePolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServicePolicySpec_ |   
`status` _BackendServicePolicyStatus_ |   
  
### BackendServicePolicyList

Contains a list of BackendServicePolicy.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendServicePolicy array_ |   
  
### BackendServicePolicySpec

Describes the attributes that a user expects from this backend policy.

_Appears in:_ \- BackendServicePolicy

Field | Description  
---|---  
`sessionAffinity` _SessionAffinity_ | The Session Affinity mode applied to the Backend Policy. This field is optional. This field is immutable. Allowed values: - NONE requests will be routed to any backend. This is the default value. - CLIENT_IP_DST_PORT_PROTO requests from the same 4-tuple (source IP, destination IP, destination port, protocol) will be routed to the same destination backend. If multiple policies match the same BackendProject, the policies are ORed. A Backend Service will have Session Affinity enabled if any of the policies affecting it has Session Affinity enabled.  
`selectors` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | A selector defining which BackendService(s) this policy is applied to. This field is required. This field is immutable.  
  
### BackendServicePolicyStatus

Represents the status of the Backend Service Policy.

_Appears in:_ \- BackendServicePolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the Backend Service Policy. Known condition types are: * "Ready"  
  
### BackendServiceRef

Holds information about the backend.

_Appears in:_ \- ForwardingRuleExternalSpec \- ForwardingRuleInternalSpec \- ForwardingRuleSpecCommon

Field | Description  
---|---  
`name` _string_ | A name of the referenced backend service object. This field is required. This field is immutable.  
  
### BackendServiceSpec

Describes the attributes that a user expects from this backend service.

_Appears in:_ \- BackendService

Field | Description  
---|---  
`backendRefs` _BackendRef array_ | A list of backends for this backend service. Only 1 Backend can be specified per Zone or per User Cluster. This field is optional. This field is mutable.  
`targetPorts` _TargetPort array_ | A list of target ports that this BackendService will translate. This field is optional. This field is immutable.  
`healthCheckName` _string_ | A name of the health check parameters object for this backend service. HealthCheck is applicable only for VM backends. It has to reference HealthCheck in the same namespace as this backend service. This field is optional. This field is immutable.  
  
### BackendServiceStatus

Represents the status of BackendService.

_Appears in:_ \- BackendService

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the backend service. Known condition types are: * "Ready"  
`forwardingRuleRefs` _ForwardingRuleRef array_ | A list of forwarding rules using this backend service.  
  
### BackendSpec

Describes the attributes that a user expects from backend.

_Appears in:_ \- Backend

Field | Description  
---|---  
`clusterName` _string_ | A name of cluster to which the scope of the defined selectors should be limited to. This does not apply to VM workloads. This field is optional. This field is immutable.  
`endpointsLabels` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | A selector defining which endpoints (Pods or VMs) to use for this backend. This field is required. This field is immutable.  
  
### BackendStatus

Represents the status of backend.

_Appears in:_ \- Backend

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the backend. Known condition types are: * "Ready"  
  
### CIDRRef

Holds information about the CIDR.

_Appears in:_ \- ForwardingRuleExternalSpec \- ForwardingRuleInternalSpec \- ForwardingRuleSpecCommon

Field | Description  
---|---  
`name` _string_ | A name of the referenced cidr object. This field is required. This field is immutable.  
  
### ClusterNodeSelector

Represents the information used to locate a node or nodes inside of a specified cluster. Either cluster or node or both must be specified.

_Appears in:_ \- FlowLogFilter

Field | Description  
---|---  
`cluster` _string_ | The name of the cluster. If a value is not provided, all clusters will be searched for the desired node or nodes.  
`node` _string_ | A wildcard pattern used to search by the node name. For example, `k8s*` or `*.domain.com`.  
  
### FlowLog

Defines a list of flow log filters used for finding relevant flows. Flow events matching any of the provided filter rules are logged.

_Appears in:_ \- FlowLogList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `FlowLog`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _FlowLogSpec_ | The desired configuration for a flow log.  
`status` _FlowLogStatus_ | The observed state of a flow log.  
  
### FlowLogFilter

Defines a collection of filter criteria that is applied at the same time. Each flow log filter contains several optional matching fields. The matching logic for each filter follows these rules:   

    
    
    First, when a matching field is optional and not specified, it implies no
    filtering is applied on this field of a flow.
    For example, if no sources are provided, it means all sources are matched.
    
    
    Next, when multiple fields are specified in one filter, all fields must match
    the target flow.
    For example, if  a source value of `srcNS/pod1` and a destination value of `dstNS/pod2` are
    specified at the same time, it matches the flow from pod `srcNS/pod1`
    to destination `dstNS/pod2`.
    
    
    Finally, when a field is a list, specifying it multiple times means matching
    any of the values.
    

_Appears in:_ \- FlowLogSpec

Field | Description  
---|---  
`source` _NetworkEndpointFilter_ | A filter that filters flow events by a list of source rules.  
`destination` _NetworkEndpointFilter_ | A filter that filters flow events by a list of destination rules.  
`endpoint` _NetworkEndpointFilter_ | The endpoint filters flow events if the event source or destination matches any given endpoint in this list. If `endpoint` is set, `source` and `destination` must not be specified. When specified, each endpoint corresponds to two filters: one with `source` set to this endpoint and all other filter fields kept the same; Another with `destination` set to this endpoint and all other filter fields kept the same.  
`l4Protocols` _[Protocol](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#protocol-v1-core) array_ | A filter that filters flow events by L4 protocols defined in [v1.Protocol]. Each protocol must be specified at most once.  
`verdicts` _PolicyVerdict array_ | A filter that filters flow events by verdict classification.  
`clusterNodeSelectors` _ClusterNodeSelector array_ | A list of clusters and nodes used to match flows.  
  
### FlowLogList

Defines a list of flow log resources.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `FlowLogList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _FlowLog array_ | A list of flow log entries.  
  
### FlowLogSpec

Represents the flow log filters that are applied. When multiple filters are present, the flow is logged if at least one filter matches the flow event.

_Appears in:_ \- FlowLog

Field | Description  
---|---  
`enable` _boolean_ | Specifies if this flow log is enabled. When disabled, the backend flow filters are disabled, and no corresponding logs are collected. Defaults to `true` if not specified.  
`filters` _FlowLogFilter array_ | A list of filters used for matching flow events. Flow events matching any of the provided filter rules are logged.  
`lifetime` _Lifetime_ | The amount of time this flow log rules is applied for. After the time is reached, the flow logging rule is disabled. If empty, this flow logging rule is enabled indefinitely.  
`logDetailLevel` _LogDetailLevel_ | The fields that are logged for matching flow events. If empty, defaults to logging all fields.  
  
### FlowLogStatus

Defines the observed state of flow logs.

_Appears in:_ \- FlowLog

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The current status of flow logs. Known condition types are: `Reconciled`: The flow log is reconciled and provisioned successfully; and `Logging`: the flow log is currently reconciled and active.  
`clusters` _PropagationStatus array_ | The propagation status of this flow log in each cluster where the resource is propagated. The `Propagated` condition is set to `true` in the `Conditions` if this resource is synced to the cluster, and its `ObservedGeneration` is set to the generation of the propagated resource in the target cluster. If this resource is successfully pruned from a cluster, the corresponding `PropagationStatus` must be removed from the list.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the flow log becomes active. This field is set by reconciler when it first interacts with the object, or when the `FlowLogSpec` resource is changed.  
`endTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time the flow log becomes inactive. This field is set by reconciler as such: 

  1. When the flow has infinity life time (`FlowLogSpec.Lifetime` is unspecified), `EndTime` may be empty.
  2. When `FlowLogSpec.Lifetime.Expiration``is set, its value is copied to`EndTime`directly.</li> <li>When`FlowLogSpec.Lifetime.Duration`is set,`EndTime`will be set to the value of`StartTime`added to the value of`FlowLogSpec.Lifetime.Duration`

  
  
### ForwardingRuleExternal

Represents a frontend API to create external forwarding rule.

_Appears in:_ \- ForwardingRuleExternalList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternal`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleExternalSpec_ |   
`status` _ForwardingRuleExternalStatus_ |   
  
### ForwardingRuleExternalList

Contains a list of ForwardingRuleExternal.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternalList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleExternal array_ |   
  
### ForwardingRuleExternalSpec

Describes the attributes that a user expects from a forwarding rule.

_Appears in:_ \- ForwardingRuleExternal

Field | Description  
---|---  
`cidrRef` _CIDRRef_ | A reference to object holding the CIDR to use for this forwarding rule. It has to reference object in the same namespace as this forwarding rule. If not specified, an IPv4 /32 CIDR will be auto-reserved from the global or zonal IP pool. This field is optional. This field is immutable.  
`ports` _Port array_ | A list of L4 ports for which packets will be forwarded to the backends configured with this forwarding rule. At least one port has to be specified. For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same [CIDR, Protocol] pair if they share at least one port number. This field is required. This field is immutable.  
`backendServiceRef` _BackendServiceRef_ | A reference to BackendService used for this forwarding rule. It has to reference BackendService in the same namespace as this forwarding rule. This field is immutable once set.  
  
### ForwardingRuleExternalStatus

Represents the status of forwarding rule.

_Appears in:_ \- ForwardingRuleExternal

Field | Description  
---|---  
`cidr` _string_ | The resulting cidr value used for this forwarding rule.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the forwarding rule. Known condition types are: * "Ready"  
  
### ForwardingRuleInternal

Represents a frontend API to create internal forwarding rule.

_Appears in:_ \- ForwardingRuleInternalList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternal`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleInternalSpec_ |   
`status` _ForwardingRuleInternalStatus_ |   
  
### ForwardingRuleInternalList

Contains a list of ForwardingRuleInternal.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternalList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleInternal array_ |   
  
### ForwardingRuleInternalSpec

Describes the attributes that a user expects from a forwarding rule.

_Appears in:_ \- ForwardingRuleInternal

Field | Description  
---|---  
`cidrRef` _CIDRRef_ | A reference to object holding the CIDR to use for this forwarding rule. It has to reference object in the same namespace as this forwarding rule. If not specified, an IPv4 /32 CIDR will be auto-reserved from the global or zonal IP pool. This field is optional. This field is immutable.  
`ports` _Port array_ | A list of L4 ports for which packets will be forwarded to the backends configured with this forwarding rule. At least one port has to be specified. For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same [CIDR, Protocol] pair if they share at least one port number. This field is required. This field is immutable.  
`backendServiceRef` _BackendServiceRef_ | A reference to BackendService used for this forwarding rule. It has to reference BackendService in the same namespace as this forwarding rule. This field is immutable once set.  
  
### ForwardingRuleInternalStatus

Represents the status of forwarding rule.

_Appears in:_ \- ForwardingRuleInternal

Field | Description  
---|---  
`cidr` _string_ | The resulting cidr value used for this forwarding rule.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the forwarding rule. Known condition types are: * "Ready"  
  
### ForwardingRuleRef

Holds information about the forwarding rule.

_Appears in:_ \- BackendServiceStatus

Field | Description  
---|---  
`name` _string_ | A name of the referenced forwarding rule object. This field is required. This field is immutable.  
  
### ForwardingRuleSpecCommon

Describes common attributes that a user expects from a forwarding rule.

_Appears in:_ \- ForwardingRuleExternalSpec \- ForwardingRuleInternalSpec

Field | Description  
---|---  
`cidrRef` _CIDRRef_ | A reference to object holding the CIDR to use for this forwarding rule. It has to reference object in the same namespace as this forwarding rule. If not specified, an IPv4 /32 CIDR will be auto-reserved from the global or zonal IP pool. This field is optional. This field is immutable.  
`ports` _Port array_ | A list of L4 ports for which packets will be forwarded to the backends configured with this forwarding rule. At least one port has to be specified. For internal forwarding rules within the same VPC network, two or more forwarding rules cannot use the same [CIDR, Protocol] pair if they share at least one port number. This field is required. This field is immutable.  
`backendServiceRef` _BackendServiceRef_ | A reference to BackendService used for this forwarding rule. It has to reference BackendService in the same namespace as this forwarding rule. This field is immutable once set.  
  
### ForwardingRuleStatusCommon

Represents common status of ForwardingRule

_Appears in:_ \- ForwardingRuleExternalStatus \- ForwardingRuleInternalStatus

Field | Description  
---|---  
`cidr` _string_ | The resulting cidr value used for this forwarding rule.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the forwarding rule. Known condition types are: * "Ready"  
  
### GatewayInterfaceRef

Represents a reference to an interface on a VPNGateway or PeerGateway resource.

_Appears in:_ \- VPNTunnelSpec

Field | Description  
---|---  
`name` _string_ | The name of the gateway.  
`namespace` _string_ | The namespace of the gateway.  
`interface` _string_ | The name of the interface.  
  
### HealthCheck

Specifies the backend service health checks.

_Appears in:_ \- HealthCheckList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `HealthCheck`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HealthCheckSpec_ |   
`status` _HealthCheckStatus_ |   
  
### HealthCheckList

Contains a list of HealthCheck.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `HealthCheckList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HealthCheck array_ |   
  
### HealthCheckSpec

Describes the attributes that a user expects from a health check.

_Appears in:_ \- HealthCheck

Field | Description  
---|---  
`tcpHealthCheck` _TCPHealthCheck_ | Defines probes using TCP port.  
`checkIntervalSec` _integer_ | The amount of time in seconds from the start of one probe to the start of the next one. Defaults to 5. This field is immutable.  
`timeoutSec` _integer_ | A time (in seconds) to wait before claiming failure. Defaults to 5. This field is immutable.  
`healthyThreshold` _integer_ | A number of sequential probes that must succeed for the endpoint to be considered healthy. Defaults to 2. This field is immutable.  
`unhealthyThreshold` _integer_ | A number of sequential probes that must fail for the endpoint to be considered unhealthy. Defaults to 2. This field is immutable.  
  
### HealthCheckStatus

Represents the status of a health check.

_Appears in:_ \- HealthCheck

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions describing the current state of the health check. Known condition types are: * "Ready"  
  
### Lifetime

Defines the lifetime of a flow log. A value for `expiration` or `duration` must be specified, but not both.

_Appears in:_ \- FlowLogSpec

Field | Description  
---|---  
`expiration` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | The time when this filter rule expires and becomes inactive. Expiration must be a time in the future. It includes the time required to propagate resources down to child clusters so the value should account for an additional buffer of around one minute to ensure that all clusters can begin logging and capture the necessary traffic.  
`duration` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The amount of time the flow log will be active for, starting from when it is reconciled. It includes the time required to propagate resources down to child clusters so the value should account for an additional buffer of around one minute to ensure that all clusters can begin logging and capture the necessary traffic.  
  
### LogDetailLevel

_Underlying type:_ `string` A list of predefined combinations of fields that are logged when filtered flow events are captured.

_Appears in:_ \- FlowLogSpec

### ManagedServiceSubject

Defines a managed service target.

_Appears in:_ \- OrganizationNetworkPolicySubject

Field | Description  
---|---  
`matchTypes` _string array_ | The organization managed service types that the policy applies to.  
  
### NamespacePodSelector

Represents the information used to locate pods inside of the specified namespace. Specify a value for `namespace`, `pod`, or `namespace` and `pod`.

_Appears in:_ \- NetworkEndpointFilter

Field | Description  
---|---  
`namespace` _string_ | The flow events that match the namespace name. For example, `kube-system`.  
`pod` _string_ | The flow events that match the given pod name prefix. For example, `xwing`, `coredns-`.  
  
### NetworkEndpointFilter

Represents a filter that selects a set of network endpoints based on the filter conditions specified.

_Appears in:_ \- FlowLogFilter

Field | Description  
---|---  
`ipBlocks` _string array_ | A filter that selects flow events that match the IP address or IP address range. Each of the IP addresses can be specified as an exact match, like `1.1.1.1` or `1200:0000:AB00:1234:0000:2552:7777:1313`, or as a CIDR range like `1.1.1.0/24` or `1200:0000:AB00:1234:0000:2552:7777:1313/120`. If not specified, any IP address is matched.  
`labels` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta) array_ | A filter that selects flow events that match the label selector. Selectors support the full Kubernetes label selector syntax.  
`namespacePodSelectors` _NamespacePodSelector array_ | A list of namespaces and pods used to match flows.  
`ports` _IntOrString array_ | A filter that selects flows by their L4 ports. If this field is not provided, this matches all port numbers. An example value for a single port is `80`. If present, only traffic on the specified protocol and port is matched.  
  
### OrganizationNetworkPolicy

Defines the Schema for the `OrganizationNetworkPolicy` API.

_Appears in:_ \- OrganizationNetworkPolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `OrganizationNetworkPolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _OrganizationNetworkPolicySpec_ | The desired configuration for `OrganizationNetworkPolicy`.  
`status` _OrganizationNetworkPolicyStatus_ | The observed state for `OrganizationNetworkPolicy`.  
  
### OrganizationNetworkPolicyIngressRule

Defines a single ingress rule for a `OrganizationNetworkPolicy` resource.

_Appears in:_ \- OrganizationNetworkPolicySpec

Field | Description  
---|---  
`from` _OrganizationNetworkPolicyPeer array_ | A list of sources which are able to access the subject of the policy. Items in this list are combined using a logical `OR` operation. If this field is empty or missing, this rule matches all sources, the traffic is not restricted by source. If this field contains at least one item, this rule allows traffic only if the traffic matches at least one item in the `from` list. A maximum of one item must be specified.  
  
### OrganizationNetworkPolicyList

Defines a list of `OrganizationNetworkPolicy` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `OrganizationNetworkPolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _OrganizationNetworkPolicy array_ |   
  
### OrganizationNetworkPolicyPeer

Defines a peer to allow traffic from.

_Appears in:_ \- OrganizationNetworkPolicyIngressRule

Field | Description  
---|---  
`ipBlock` _[IPBlock](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#ipblock-v1-networking)_ | A policy on a particular `iPBlock`. If empty, it allows all traffic (0.0.0.0/0).  
  
### OrganizationNetworkPolicySpec

Defines the desired state of a `OrganizationNetworkPolicy` resource. The array of ingress rules for this policy applies to the specified target. When multiple rules are present, or when multiple policies are present, the rules for each are combined additively. Traffic is allowed if it matches at least one rule.

_Appears in:_ \- OrganizationNetworkPolicy

Field | Description  
---|---  
`subject` _OrganizationNetworkPolicySubject_ | The managed services of the organization network policies.  
`ingress` _OrganizationNetworkPolicyIngressRule array_ | The ingress rule for the traffic. If `ingress` is empty or missing, it does not allow any traffic. If this field contains at least one item, this rule allows traffic only if the traffic matches at least one item in the `from` field.  
  
### OrganizationNetworkPolicyStatus

Defines the observed state of `OrganizationNetworkPolicy` resource.

_Appears in:_ \- OrganizationNetworkPolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | If `ready` is `true`, it means that the `OrganizationNetworkPolicy` resource is successfully propagated to the Management API server. If `ready` is `false`, it means that the `OrganizationNetworkPolicy` has failed to propagate.  
`generatedauthorizationpolicies` _AuthorizationPolicyRef array_ | The list of authorization policies that are generated from the `OrganizationNetworkPolicy` resource.  
  
### OrganizationNetworkPolicySubject

Represents the organization service targets. Choose exactly one of the properties for the target.

_Appears in:_ \- OrganizationNetworkPolicySpec

Field | Description  
---|---  
`subjectType` _OrganizationNetworkPolicySubjectType_ | The type of entities the policy rules apply to. If not set, then it defaults to `ManagedService`.  
`services` _ManagedServiceSubject_ | The service to select. Supports the organization multi-tenant service, including `UIConsole` and `APIServer`.  
  
### OrganizationNetworkPolicySubjectType

_Underlying type:_ `string` Defines the target type of the policies.

_Appears in:_ \- OrganizationNetworkPolicySubject

### PeerGateway

PeerGateway represents a remote VPN endpoint. An interface on a PeerGateway should be used by a single VPNTunnel to establish an encrypted tunnel to the remote site.

_Appears in:_ \- PeerGatewayList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `PeerGateway`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _PeerGatewaySpec_ |   
`status` _PeerGatewayStatus_ |   
  
### PeerGatewayInterface

Represents a Gateway interface on which a tunnel is established.

_Appears in:_ \- PeerGatewaySpec

Field | Description  
---|---  
`name` _string_ | The name of the interface.  
`ip` _string_ | The IPv4 address of the interface.  
  
### PeerGatewayList

PeerGatewayList contains a list of PeerGateway.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `PeerGatewayList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _PeerGateway array_ | Items is a list of PeerGateway entries.  
  
### PeerGatewaySpec

PeerGatewaySpec defines the desired state of PeerGateway.

_Appears in:_ \- PeerGateway

Field | Description  
---|---  
`interfaces` _PeerGatewayInterface array_ | The list of interfaces on the Peer Gateway which will be used for VPN connections. Each interface should be used by one VPNTunnel.  
  
### PeerGatewayStatus

PeerGatewayStatus defines the observed state of PeerGateway.

_Appears in:_ \- PeerGateway

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Indicates the current status of PeerGateway. Known condition types are: - "Ready": The Peer Gateway is reconciled and used by a VPNTunnel. - "TunnelsEstablished": Each interface on the Peer Gateway is used by a VPNTunnel.  
  
### PolicyManagedServiceSubject

Defines a managed service target.

_Appears in:_ \- ProjectNetworkPolicySubject

Field | Description  
---|---  
`matchTypes` _string array_ | The managed service types that the policy applies to. Exactly one item must be specified.  
  
### PolicyProjects

Represents a collection of projects that is used to match a set of projects.

_Appears in:_ \- ProjectNetworkPolicyPeer \- ProjectSelector

Field | Description  
---|---  
`matchNames` _string array_ | The selected projects which are chosen within the organization based on their name. The project namespace is derived from the project network policy's namespace. If this field is empty or missing, this rule matches all projects. A maximum of one item must be specified.  
  
### PolicySubjectType

_Underlying type:_ `string` Defines the target type of the network policies.

_Appears in:_ \- ProjectNetworkPolicySubject

### PolicyType

_Underlying type:_ `string` Defines the direction of traffic on which the policy rules are applied.

_Appears in:_ \- ProjectNetworkPolicySpec

### PolicyVerdict

_Underlying type:_ `string` Defines a list of verdict classifying flows.

_Appears in:_ \- FlowLogFilter

### Port

Contains information on L4 port on which service needs to be served.

_Appears in:_ \- ForwardingRuleExternalSpec \- ForwardingRuleInternalSpec \- ForwardingRuleSpecCommon \- TargetPort

Field | Description  
---|---  
`protocol` _[Protocol](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#protocol-v1-core)_ | Specifies Layer-4 protocol which traffic must match. Only TCP and UDP are supported. This field is required. This field is immutable.  
`port` _integer_ | A number of the port that will be exposed by this service. This field is required. This field is immutable.  
  
### ProbeHandler

Defines the available probes for the health check. One and only one of the fields must be specified.

_Appears in:_ \- HealthCheckSpec

Field | Description  
---|---  
`tcpHealthCheck` _TCPHealthCheck_ | Defines probes using TCP port.  
  
### ProjectNetworkPolicy

Contains the Schema for the `ProjectNetworkPolicy` API.

_Appears in:_ \- ProjectNetworkPolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectNetworkPolicySpec_ | The desired configuration for `ProjectNetworkPolicy` resource.  
`status` _ProjectNetworkPolicyStatus_ | The observed state for `ProjectNetworkPolicy` resource.  
  
### ProjectNetworkPolicyEgressRule

Defines a single egress rule for a `ProjectNetworkPolicy` resource.

_Appears in:_ \- ProjectNetworkPolicySpec

Field | Description  
---|---  
`ports` _ProjectNetworkPolicyPort array_ | A list of the destination ports showing outgoing traffic. Each item in this list is combined using a logical `OR` operation. If this field is empty or missing, this rule matches all ports, traffic is not restricted by port. If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.  
`to` _ProjectNetworkPolicyPeer array_ | A list of destinations for outgoing traffic of the subject for this rule. Items in this list are combined using a logical `OR` operation. If this field is empty or missing, this rule matches all destinations , traffic is not restricted by destination. If this field contains at least one item, this rule allows traffic only if the traffic matches at least one item in the `to` list. A maximum of one item must be specified.  
  
### ProjectNetworkPolicyIngressRule

Defines a single ingress rule for a `ProjectNetworkPolicy` resource.

_Appears in:_ \- ProjectNetworkPolicySpec

Field | Description  
---|---  
`ports` _ProjectNetworkPolicyPort array_ | A list of ports for incoming traffic. Each item in this list is combined using a logical `OR` operation. If this field is empty or missing, this rule matches all ports, traffic is not restricted by port. If this field is present and contains at least one item, then this rule allows traffic only if the traffic matches at least one port in the list.  
`from` _ProjectNetworkPolicyPeer array_ | A list of sources which are able to access the subject of the policy. Items in this list are combined using a logical `OR` operation. If this field is empty or missing, this rule matches all sources , traffic is not restricted by source. If this field contains at least one item, this rule allows traffic only if the traffic matches at least one item in the `from` list. A maximum of one item must be specified.  
  
### ProjectNetworkPolicyList

Defines a list of `ProjectNetworkPolicy` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectNetworkPolicy array_ |   
  
### ProjectNetworkPolicyPeer

Represents a peer to allow traffic from. Exactly one of the subfields must be specified.

_Appears in:_ \- ProjectNetworkPolicyEgressRule \- ProjectNetworkPolicyIngressRule

Field | Description  
---|---  
`projects` _PolicyProjects_ | The projects to apply the network policy to.  
`projectSelector` _ProjectSelector_ | ProjectSelector selects projects and workloads within those projects as a source of traffic. If specified, allows traffic from workloads within the selected projects that match the workload selector.  
`ipBlock` _[IPBlock](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#ipblock-v1-networking)_ | A policy on a particular `iPBlock`. If empty, then all external IPs, excluding Kubernetes nodes and workloads in the organization, are selected.  
`ipBlocks` _[IPBlock](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#ipblock-v1-networking) array_ | A policy on particular `iPBlocks`. If empty, then all external IPs, excluding Kubernetes nodes and workloads in the organization, are selected.  
  
### ProjectNetworkPolicyPort

Represents a port to allow traffic on. If all subfields are empty, all TCP traffic is selected.

_Appears in:_ \- ProjectNetworkPolicyEgressRule \- ProjectNetworkPolicyIngressRule

Field | Description  
---|---  
`protocol` _[Protocol](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#protocol-v1-core)_ | The protocol which traffic must match. The options are TCP, UDP, or SCTP. If unspecified, this field defaults to TCP.  
`port` _IntOrString_ | The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol and port is matched.  
  
### ProjectNetworkPolicySpec

Defines the desired state of `ProjectNetworkPolicy` resource. The array of ingress or egress rules for this policy applies to the specified subject or target. When multiple rules are present, or when multiple policies are present, the rules for each are combined additively. In other words, traffic is allowed if it matches at least one rule.

_Appears in:_ \- ProjectNetworkPolicy

Field | Description  
---|---  
`subject` _ProjectNetworkPolicySubject_ | The target of the project network policies. If unspecified, all pods excluding the managed services in the project are selected.  
`policyType` _PolicyType_ | The direction of traffic on which the policy rules are applied. This must be set to one of `ingress` and `egress`. If not set, then it defaults to `ingress`.  
`ingress` _ProjectNetworkPolicyIngressRule array_ | A list of ingress rules for this policy. If this field is empty, the `ProjectNetworkPolicy` resource does not allow any traffic and serves solely to ensure that the subjects it selects are isolated by default.  
`egress` _ProjectNetworkPolicyEgressRule array_ | A the list of egress rules for this policy. If this field is empty, the `ProjectNetworkPolicy` resource does not allow any traffic and serves solely to ensure that subjects it selects are isolated by default.  
  
### ProjectNetworkPolicyStatus

Defines the observed state of a `ProjectNetworkPolicy` resource.

_Appears in:_ \- ProjectNetworkPolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | If `ready` is `true`, it means that all network policies are successfully propagated to all user clusters. if `ready` is `false`, it means that some, or all, network policies have failed to propagate.  
`propagatedName` _string_ | The name of the propagated network policy realized in all user clusters within the project. This field is expected to be set when the property of `SubjectType="UserWorkload"`.  
`clusters` _ClusterStatus array_ | The list of propagation status on the clusters. This field is expected to be set when the property of `SubjectType="UserWorkload"`.  
`propagatedManagedServiceNamespaces` _string array_ | The list of managed service namespaces that the policy is propagated to. This field is expected to be set when the property of `SubjectType="ManagedService"`.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds most recent errors with last seen time.  
  
### ProjectNetworkPolicySubject

Defines the target for project network policies.

_Appears in:_ \- ProjectNetworkPolicySpec

Field | Description  
---|---  
`subjectType` _PolicySubjectType_ | The type of entities the policy rules apply to. This must be set to one of `userWorkload` or `managedService`. If not set, then it defaults to `userWorkload`. If set to `userWorkload`, then all pods excluding the managed services in the project are selected. If set to `managedService`, then specified managed services are selected.  
`managedServices` _PolicyManagedServiceSubject_ | The managed services that the policy rules apply to. Must be specified only with `SubjectType="ManagedService"`.  
`workloadSelector` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | WorkloadSelector selects the workloads in the project to which the policy rules apply. If this field is nil or empty, this rule applies to all workloads in the project.  
  
### ProjectSelector

ProjectSelector selects projects and workloads.

_Appears in:_ \- ProjectNetworkPolicyPeer

Field | Description  
---|---  
`projects` _PolicyProjects_ | The projects to apply the network policy to. If empty, this rule matches all projects.  
`workloads` _[LabelSelector](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#labelselector-v1-meta)_ | The workloads to apply the network policy to. If empty, all workloads in the selected projects are included.  
  
### PropagationStatus

Defines the propagation status for a specific cluster.

_Appears in:_ \- FlowLogStatus

Field | Description  
---|---  
`cluster` _string_ | The cluster name where this resource is propagated.  
`node` _string_ | The node name where this resource is propagated.  
`namespace` _string_ | The namespace where this resource is propagated.  
`name` _string_ | The name of the propagated resource.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The current status of the programmed resources.  
  
### Route

Represents a route advertised or received over the tunnel.

_Appears in:_ \- VPNBGPPeerStatus

Field | Description  
---|---  
`prefix` _string_ | The network prefix of the route.  
  
### SessionAffinity

_Underlying type:_ `string` Session Affinity Type string

_Appears in:_ \- BackendServicePolicySpec

### SessionState

_Underlying type:_ `string` The state of the BGP session, like Established or NotEstablished.

_Appears in:_ \- VPNBGPPeerStatus

### TCPHealthCheck

Specifies parameters for TCP health check probes.

_Appears in:_ \- HealthCheckSpec \- ProbeHandler

Field | Description  
---|---  
`port` _integer_ | A number of the port on which the health check will be performed. Defaults to 80. This field is immutable.  
  
### TargetPort

Holds information about an L4 port that will be translated to specified targetPort.

_Appears in:_ \- BackendServiceSpec

Field | Description  
---|---  
`protocol` _[Protocol](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#protocol-v1-core)_ | Specifies Layer-4 protocol which traffic must match. Only TCP and UDP are supported. This field is required. This field is immutable.  
`port` _integer_ | A number of the port that will be exposed by this service. This field is required. This field is immutable.  
`targetPort` _integer_ | A port to which the Port value will be translated to. Value of TargetPort cannot be repeated in a given object. This field is required. This field is immutable.  
  
### TunnelState

_Underlying type:_ `string` The state of the Tunnel, like Established or Connecting.

_Appears in:_ \- VPNTunnelStatus

### VPNBGPPeer

VPNBGPPeer represents a BGP session over a VPN tunnel. A VPNBGPPeer establishes a BGP session between a BGP peer in an Organization and BGP peer of a remote site across a single VPNTunnel. A VPNBGPPeer should be used by a VPNTunnel.

_Appears in:_ \- VPNBGPPeerList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNBGPPeer`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VPNBGPPeerSpec_ |   
`status` _VPNBGPPeerStatus_ |   
  
### VPNBGPPeerList

VPNBGPPeerList contains a list of VPNBGPPeer.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNBGPPeerList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VPNBGPPeer array_ | Items is a list of VPNBGPPeer entries.  
  
### VPNBGPPeerSpec

VPNBGPPeerSpec defines the desired state of VPNBGPPeer. The IP for both the Remote and Local BGP peer must be in the same "/30" block from the "169.254.0.0/16" range.

_Appears in:_ \- VPNBGPPeer

Field | Description  
---|---  
`remote` _BGPPeerInterface_ | Represents the remote BGP peer.  
`local` _BGPPeerInterface_ | Represents the local BGP peer.  
  
### VPNBGPPeerStatus

VPNBGPPeerStatus defines the observed state of VPNBGPPeer. The Organization will create a BGP session with the remote site over the VPNTunnel that references this VPNBGPPeer. The local BGP peer will advertise all internal CIDR's of the Organization to the remote BGP peer. If the remote BGP peer advertises a CIDR that conflicts with the internal CIDR's of the Organization, the VPNBGPPeer "Ready" condition will be false.

_Appears in:_ \- VPNBGPPeer

Field | Description  
---|---  
`state` _SessionState_ | Represents the state of the BGP session between the local BGP peer and the remote BGP peer.  
`advertised` _Route array_ | Represents routes advertised to the remote site on the BGP session.  
`received` _Route array_ | Represents routes received from the remote site on the BGP session.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Indicates the current status of VPNBGPPeer. Known condition types are: - "Ready": The Peer Gateway is reconciled and used by a VPNTunnel. - "BGPSessionEstablished": Each interface on the Peer Gateway is used by a VPNTunnel. - "ReceivedRoutesReady": The routes received from the remote BGP peer do not interfere with routes in the internal CIDR of the Organization.  
  
### VPNGateway

VPNGateway represents an Organization VPN endpoint. An interface on a VPNGateway should be used by a VPNTunnel to establish an encrypted tunnel to a remote site.

_Appears in:_ \- VPNGatewayList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNGateway`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VPNGatewaySpec_ |   
`status` _VPNGatewayStatus_ |   
  
### VPNGatewayInterface

Represents an interface on the Gateway. An IP will be allocated for each interface and added in the status.

_Appears in:_ \- VPNGatewaySpec

Field | Description  
---|---  
`name` _string_ | The name of the interface.  
  
### VPNGatewayInterfaceStatus

Represents a Gateway interface on which a tunnel is established.

_Appears in:_ \- VPNGatewayStatus

Field | Description  
---|---  
`name` _string_ | The name of the interface.  
`ip` _string_ | The IPv4 address of the interface.  
  
### VPNGatewayList

VPNGatewayList contains a list of VPNGateway.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNGatewayList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VPNGateway array_ | Items is a list of VPNGateway entries.  
  
### VPNGatewaySpec

VPNGatewaySpec defines the desired state of VPNGateway. Define the name of the interfaces which should be assigned external IPv4 addresses by the VPNGateway. Each IPv4 address that is assigned to the interface is automatically chosen from an external address pool.

_Appears in:_ \- VPNGateway

Field | Description  
---|---  
`interfaces` _VPNGatewayInterface array_ | The names of each interface. VPNGateway will assign an external IPv4 address to each interface in the list.  
  
### VPNGatewayStatus

VPNGatewayStatus defines the observed state of VPNGateway.

_Appears in:_ \- VPNGateway

Field | Description  
---|---  
`interfaces` _VPNGatewayInterfaceStatus array_ | The list of interfaces on the VPNGateway. Each interface can be used by one VPNTunnel.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Indicates the current status of VPNGateway. Known condition types are: - "Ready": The VPNGateway is reconciled and used by a VPNTunnel. - "IPsAssigned": IPv4 addresses have been assigned to each interface on the VPNGateway. - "TunnelsAttached": Each interface on the VPNGateway is used by a VPNTunnel.  
  
### VPNTunnel

VPNTunnel represents an encrypted IPSec tunnel between an Organization network and a remote network. It connects a VPNGateway interface to a PeerGateway interface, and uses VPNBGPPeer to exchange routing information over the tunnel.

_Appears in:_ \- VPNTunnelList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNTunnel`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _VPNTunnelSpec_ |   
`status` _VPNTunnelStatus_ |   
  
### VPNTunnelList

VPNTunnelList contains a list of VPNTunnel.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.gdc.goog/v1`  
`kind` _string_ | `VPNTunnelList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _VPNTunnel array_ | Items is a list of VPNTunnel entries.  
  
### VPNTunnelSpec

VPNTunnelSpec defines the desired state of VPNTunnel. The tunnel that is established supports the IKEv2 protocol with PSK-based authentication. Packets going through the tunnel are encrypted using IPSec Tunnel mode, where the outer IP header is constructed using a VPNGateway interface IP and a PeerGateway interface IP. A VPNTunnel references a VPNGateway interface, a PeerGateway interface, a VPNBGPPeer resource, and a secret which contains the preshared key for the authentication.

_Appears in:_ \- VPNTunnel

Field | Description  
---|---  
`vpnInterface` _GatewayInterfaceRef_ | The interface on the VPNGateway that is used for the tunnel. The IP from the interface is used as the source IP for packets sent to the remote site over the tunnel.  
`peerInterface` _GatewayInterfaceRef_ | The interface on the PeerGateway that is used for the tunnel. The IP from the interface is used as the destination IP for packets sent to the remote site over the tunnel.  
`vpnBGPPeer` _[ObjectReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectreference-v1-core)_ | A reference to a VPNBGPPeer which specifies the dynamic routing over the tunnel.  
`ikeKey` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | The secret that contains the preshared key for initial authentication of the gateways.  
  
### VPNTunnelStatus

VPNTunnelStatus defines the observed state of VPNTunnel.

_Appears in:_ \- VPNTunnel

Field | Description  
---|---  
`state` _TunnelState_ | The current status of the tunnel.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Indicates the current status of VPNTunnel. Known condition types are: - "Ready": The VPNTunnel is reconciled and is in an established state. - "TunnelEstablished": The tunnel is in an established state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
