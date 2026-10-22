---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/global-networking-v1/
title: KRM API networking.global.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:08.867512+00:00
---

# KRM API networking.global.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/networking/v1/global-networking-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API networking.global.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## networking.global.gdc.goog/v1

### BackendRef

Holds information about the backend.

_Appears in:_ \- BackendServiceSpec

Field | Description  
---|---  
`name` _string_ | A name of the referenced Backend object. The referenced Backend has to be in the same namespace as this backend service. This field is required. This field is immutable.  
`zone` _string_ | A name of zone in which the referenced backend is created in. This field is required. This field is immutable.  
  
### BackendService

Represents a load balancer configuration.

_Appears in:_ \- BackendServiceList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendService`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServiceSpec_ |   
`status` _BackendServiceStatus_ |   
  
### BackendServiceList

Contains a list of BackendService.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServiceList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendService array_ |   
  
### BackendServicePolicy

Represents policies to be applied to one or more load balancers.

_Appears in:_ \- BackendServicePolicyList \- BackendServicePolicyReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServicePolicySpec_ |   
`status` _BackendServicePolicyStatus_ |   
  
### BackendServicePolicyList

Contains a list of BackendServicePolicy.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendServicePolicy array_ |   
  
### BackendServicePolicyReplica

Represents policy replicas to be applied to one or more load balancers.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicyReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServicePolicySpec_ |   
`status` _BackendServicePolicyStatus_ |   
  
### BackendServicePolicyReplicaList

Contains a list of BackendServicePolicy.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServicePolicyReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendServicePolicy array_ |   
  
### BackendServicePolicyStatus

Represents the status of the Backend Service Policy.

_Appears in:_ \- BackendServicePolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _BackendServicePolicyZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with last seen time.  
  
### BackendServicePolicyZoneStatus

Represents the status of a given zone's health check.

_Appears in:_ \- BackendServicePolicyStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _BackendServicePolicyStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### BackendServiceReplica

Represents a backend service replica.

_Appears in:_ \- BackendServiceReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServiceReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackendServiceSpec_ |   
`status` _BackendServiceStatus_ |   
  
### BackendServiceReplicaList

Contains a list of BackendService.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `BackendServiceReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackendServiceReplica array_ |   
  
### BackendServiceSpec

Describes the attributes that a user expects from this backend service.

_Appears in:_ \- BackendService \- BackendServiceReplica

Field | Description  
---|---  
`backendRefs` _BackendRef array_ | A list of backends for this backend service. Only 1 Backend can be specified per Zone or per User Cluster. This field is optional. This field is mutable.  
`targetPorts` _TargetPort array_ | A list of target ports that this BackendService will translate. The provided port-protocol pair has to be unique in the list. This field is optional.  
`healthCheckName` _string_ | A name of the health check parameters object for this backend service. HealthCheck is applicable only for VM backends. It has to reference HealthCheck in the same namespace as this backend service. This field is optional. This field is immutable.  
  
### BackendServiceStatus

Represents the status of BackendService.

_Appears in:_ \- BackendService

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _BackendServiceZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with last seen time.  
  
### BackendServiceZoneStatus

_Appears in:_ \- BackendServiceStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _BackendServiceStatus_ | The reconciliation status of the replica collected from the zone.  
  
### ForwardingRuleExternal

Represents a frontend API to create external forwarding rule.

_Appears in:_ \- ForwardingRuleExternalList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternal`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleExternalSpec_ |   
`status` _ForwardingRuleExternalStatus_ |   
  
### ForwardingRuleExternalList

Contains a list of ForwardingRuleExternal.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternalList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleExternal array_ |   
  
### ForwardingRuleExternalReplica

Represents an external forwarding rule replica.

_Appears in:_ \- ForwardingRuleExternalReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternalReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleExternalSpec_ |   
`status` _ForwardingRuleExternalStatus_ |   
  
### ForwardingRuleExternalReplicaList

Contains a list of ForwardingRuleExternalReplica.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleExternalReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleExternalReplica array_ |   
  
### ForwardingRuleExternalStatus

Represents the status of forwarding rule.

_Appears in:_ \- ForwardingRuleExternal

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ForwardingRuleExternalZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with last seen time.  
`subnets` _SubnetReference array_ | Subnets holds the list of subnets that are used for this forwarding rule.  
  
### ForwardingRuleExternalZoneStatus

Represents the status of a given zone's external forwarding rule.

_Appears in:_ \- ForwardingRuleExternalStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ForwardingRuleExternalStatus_ | The reconciliation status of the replica collected from the zone.  
  
### ForwardingRuleInternal

Represents a frontend API to create internal forwarding rule.

_Appears in:_ \- ForwardingRuleInternalList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternal`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleInternalSpec_ |   
`status` _ForwardingRuleInternalStatus_ |   
  
### ForwardingRuleInternalList

Contains a list of ForwardingRuleInternal.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternalList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleInternal array_ |   
  
### ForwardingRuleInternalReplica

Represents an internal forwarding rule replica.

_Appears in:_ \- ForwardingRuleInternalReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternalReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ForwardingRuleInternalSpec_ |   
`status` _ForwardingRuleInternalStatus_ |   
  
### ForwardingRuleInternalReplicaList

Contains a list of ForwardingRuleInternalReplica.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ForwardingRuleInternalReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ForwardingRuleInternalReplica array_ |   
  
### ForwardingRuleInternalStatus

Represents the status of forwarding rule.

_Appears in:_ \- ForwardingRuleInternal

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ForwardingRuleInternalZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with last seen time.  
`subnets` _SubnetReference array_ | Subnets holds the list of subnets that are used for this forwarding rule.  
  
### ForwardingRuleInternalZoneStatus

Represents the status of a given zone's internal forwarding rule.

_Appears in:_ \- ForwardingRuleInternalStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ForwardingRuleInternalStatus_ | The reconciliation status of the replica collected from the zone.  
  
### HealthCheck

Specifies the backend service health checks.

_Appears in:_ \- HealthCheckList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `HealthCheck`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HealthCheckSpec_ |   
`status` _HealthCheckStatus_ |   
  
### HealthCheckList

Contains a list of HealthCheck.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `HealthCheckList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HealthCheck array_ |   
  
### HealthCheckReplica

Specifies the backend service health check replicas.

_Appears in:_ \- HealthCheckReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `HealthCheckReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _HealthCheckSpec_ |   
`status` _HealthCheckStatus_ |   
  
### HealthCheckReplicaList

Contains a list of HealthCheckReplica.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `HealthCheckReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _HealthCheckReplica array_ |   
  
### HealthCheckStatus

Represents the status of a health check.

_Appears in:_ \- HealthCheck

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _HealthCheckZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
`errorStatus` _ErrorStatus_ | ErrorStatus holds the most recent errors with last seen time.  
  
### HealthCheckZoneStatus

Represents the status of a given zone's health check.

_Appears in:_ \- HealthCheckStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _HealthCheckStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ManagedDNSZone

ManagedDNSZone represents a managed DNS zone.

_Appears in:_ \- ManagedDNSZoneList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ManagedDNSZone`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManagedDNSZoneSpec_ |   
`status` _ManagedDNSZoneStatus_ |   
  
### ManagedDNSZoneList

ManagedDNSZoneList represents a list of managed DNS zones.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ManagedDNSZoneList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManagedDNSZone array_ |   
  
### ManagedDNSZoneReplica

ManagedDNSZoneReplica represents a managed DNS zone.

_Appears in:_ \- ManagedDNSZoneReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ManagedDNSZoneReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ManagedDNSZoneSpec_ |   
`status` _ManagedDNSZoneReplicaStatus_ |   
  
### ManagedDNSZoneReplicaList

ManagedDNSZoneReplicaList represents a list of managed DNS zones.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ManagedDNSZoneReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ManagedDNSZoneReplica array_ |   
  
### ManagedDNSZoneReplicaStatus

ManagedDNSZoneReplicaStatus provides the status of a managed DNS zone.

_Appears in:_ \- ManagedDNSZoneReplica \- ManagedDNSZoneZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions that will be used: - Ready: This condition indicates whether the DNS zone has been added into the appropriate zonefile. - Deleting: The DNS zone was marked for deletion.  
`nameServers` _string array_ | Name servers hosting the DNS zone.  
  
### ManagedDNSZoneSpec

ManagedDNSZoneSpec provides the specification of a managed DNS zone.

_Appears in:_ \- ManagedDNSZone \- ManagedDNSZoneReplica

Field | Description  
---|---  
`dnsName` _string_ | The domain name for the DNS zone. We restrict MaxLength to 239 (instead of 253) because the reconciler creates downstream stub zones prefixed with "stub-public-" (12 chars) or "stub-private-" (13 chars). This ensures the generated stub zone resource name does not exceed the Kubernetes limit of 253 characters.  
`description` _string_ | Human readable DNS zone description. Optional field.  
`visibility` _Visibility_ | The visibility of the DNS zone, i.e., whether it is a public zone, or a private zone visible only to clients in the default customer VPC network.  
  
### ManagedDNSZoneStatus

ManagedDNSZoneStatus provides the overall status of a ManagedDNSZone.

_Appears in:_ \- ManagedDNSZone

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ManagedDNSZoneZoneStatus array_ | The list of rollout statuses for each GDC air-gapped zone that the resource is rolled out to.  
  
### ManagedDNSZoneZoneStatus

ManagedDNSZoneZoneStatus provides the status of a ManagedDNSZone rolling out to a particular GDC air-gapped zone.

_Appears in:_ \- ManagedDNSZoneStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ManagedDNSZoneReplicaStatus_ | The reconciliation status of the replica collected from the GDC air-gapped zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ProjectNetworkPolicy

`ProjectNetworkPolicy` contains the API schema.

_Appears in:_ \- ProjectNetworkPolicyList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicy`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectNetworkPolicySpec_ | The desired configuration for `ProjectNetworkPolicy` resource.  
`status` _ProjectNetworkPolicyStatus_ | The observed state for `ProjectNetworkPolicy` resource.  
  
### ProjectNetworkPolicyList

`ProjectNetworkPolicyList` defines a list of `ProjectNetworkPolicy` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicyList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectNetworkPolicy array_ |   
  
### ProjectNetworkPolicyReplica

`ProjectNetworkPolicyReplica` represents `ProjectNetworkPolicy` resources that are synced to a particular zonal API server.

_Appears in:_ \- ProjectNetworkPolicyReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicyReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ProjectNetworkPolicySpec_ | The desired configuration for `ProjectNetworkPolicy` resource.  
`status` _ProjectNetworkPolicyStatus_ | The desired configuration for the `ProjectNetworkPolicy` resource.  
  
### ProjectNetworkPolicyReplicaList

`ProjectNetworkPolicyReplicaList` defines a list of `ProjectNetworkPolicy` resources.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ProjectNetworkPolicyReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ProjectNetworkPolicyReplica array_ |   
  
### ProjectNetworkPolicyStatus

`ProjectNetworkPolicyStatus` defines the observed state of a `ProjectNetworkPolicy` resource.

_Appears in:_ \- ProjectNetworkPolicy

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ProjectNetworkPolicyZoneStatus array_ | The list of zone statuses where the resource is rolled out to.  
  
### ProjectNetworkPolicyZoneStatus

`ProjectNetworkPolicyZoneStatus` provides the status of an project network policy rolling out to a particular zone.

_Appears in:_ \- ProjectNetworkPolicyStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ProjectNetworkPolicyStatus_ | The reconciliation status of the replica collected from the zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### ResourceRecordSet

ResourceRecordSet represents a resource record set.

_Appears in:_ \- ResourceRecordSetList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ResourceRecordSet`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ResourceRecordSetSpec_ |   
`status` _ResourceRecordSetStatus_ |   
  
### ResourceRecordSetList

ResourceRecordSetList represents a list of resource record sets.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ResourceRecordSetList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ResourceRecordSet array_ |   
  
### ResourceRecordSetReplica

ResourceRecordSetReplica represents a resource record set.

_Appears in:_ \- ResourceRecordSetReplicaList

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ResourceRecordSetReplica`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ResourceRecordSetSpec_ |   
`status` _ResourceRecordSetReplicaStatus_ |   
  
### ResourceRecordSetReplicaList

ResourceRecordSetReplicaList represents a list of resource record sets.

Field | Description  
---|---  
`apiVersion` _string_ | `networking.global.gdc.goog/v1`  
`kind` _string_ | `ResourceRecordSetReplicaList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ResourceRecordSetReplica array_ |   
  
### ResourceRecordSetReplicaStatus

ResourceRecordSetReplicaStatus provides the status of a resource record set.

_Appears in:_ \- ResourceRecordSetReplica \- ResourceRecordSetZoneStatus

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions that will be used: - Ready: This condition indicates whether the RRset has been added to or updated in the appropriate zonefile. - Deleting: The RRset was marked for deletion.  
  
### ResourceRecordSetSpec

ResourceRecordSetSpec provides the specification of a resource record set.

_Appears in:_ \- ResourceRecordSet \- ResourceRecordSetReplica

Field | Description  
---|---  
`name` _string_ | The fully qualified domain name (FQDN) of the RRset.  
`ttlSeconds` _integer_ | The time to live in seconds for the RRset. This value indicates how long a resolver should serve cached versions of resource records in this RRset before querying for an updated version. Default value is 300.  
`type` _string_ | The type of the resource records in the RRset.  
`rrData` _string array_ | The data for all resource records in the RRset. Each entry represents a separate resource record.  
`dnsZone` _string_ | The managed DNS zone that the RRset belongs to. The name of the ManagedDNSZone CR in the same namespace as this ResourceRecordSet CR. The domain name of the managed DNS zone must be a suffix of the FQDN specified in the `Name` field above.  
  
### ResourceRecordSetStatus

ResourceRecordSetStatus provides the overall status of a ResourceRecordSet.

_Appears in:_ \- ResourceRecordSet

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observations of the overall state of the resource. Known condition types: Ready.  
`rollout` _RolloutStatus_ | The current strategy used to roll out the resource to each zone.  
`zones` _ResourceRecordSetZoneStatus array_ | The list of rollout statuses for each GDC air-gapped zone that the object is rolled out to.  
  
### ResourceRecordSetZoneStatus

ResourceRecordSetZoneStatus provides the status of a ResourceRecordSet rolling out to a particular GDC air-gapped zone.

_Appears in:_ \- ResourceRecordSetStatus

Field | Description  
---|---  
`name` _string_ | The name of the zone where the replica this status represents is in.  
`rolloutStatus` _ZoneRolloutStatus_ | The status of rolling out the replica to the zone.  
`replicaStatus` _ResourceRecordSetReplicaStatus_ | The reconciliation status of the replica collected from the GDC air-gapped zone. Any condition within the field that has an .observedGeneration less than .rolloutStatus.replicaGeneration is out of date.  
  
### Visibility

_Underlying type:_ `string`

_Appears in:_ \- ManagedDNSZoneSpec

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
