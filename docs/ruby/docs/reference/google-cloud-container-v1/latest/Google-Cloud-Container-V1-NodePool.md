---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool/
title: Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodePool (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:27.650307+00:00
---

# Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodePool (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::NodePool (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.1  0.33.1  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.3 

Reference documentation and code samples for the Kubernetes Engine V1 API class Google::Cloud::Container::V1::NodePool.

NodePool contains the name and configuration for a cluster's node pool. Node pools are a set of nodes (i.e. VM's), with a common configuration and specification, under the control of the cluster master. They may have a set of Kubernetes labels applied to them, which may be used to reference them during pod scheduling. They may also be resized up or down, to accommodate the workload.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #autoscaling
    
    
    def autoscaling() -> ::Google::Cloud::Container::V1::NodePoolAutoscaling

**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present. 



### #autoscaling=
    
    
    def autoscaling=(value) -> ::Google::Cloud::Container::V1::NodePoolAutoscaling

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present. 



### #best_effort_provisioning
    
    
    def best_effort_provisioning() -> ::Google::Cloud::Container::V1::BestEffortProvisioning

**Returns**

  * ([::Google::Cloud::Container::V1::BestEffortProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BestEffortProvisioning)) — Enable best effort provisioning for nodes 



### #best_effort_provisioning=
    
    
    def best_effort_provisioning=(value) -> ::Google::Cloud::Container::V1::BestEffortProvisioning

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::BestEffortProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BestEffortProvisioning)) — Enable best effort provisioning for nodes 



**Returns**

  * ([::Google::Cloud::Container::V1::BestEffortProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BestEffortProvisioning)) — Enable best effort provisioning for nodes 



### #conditions
    
    
    def conditions() -> ::Array<::Google::Cloud::Container::V1::StatusCondition>

**Returns**

  * (::Array<[::Google::Cloud::Container::V1::StatusCondition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-StatusCondition)>) — Output only. Which conditions caused the current node pool state. 



### #config
    
    
    def config() -> ::Google::Cloud::Container::V1::NodeConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeConfig)) — The node configuration of the pool. 



### #config=
    
    
    def config=(value) -> ::Google::Cloud::Container::V1::NodeConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeConfig)) — The node configuration of the pool. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeConfig)) — The node configuration of the pool. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — Output only. This checksum is computed by the server based on the value of node pool fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. 



### #initial_node_count
    
    
    def initial_node_count() -> ::Integer

**Returns**

  * (::Integer) — The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. 



### #initial_node_count=
    
    
    def initial_node_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. 



**Returns**

  * (::Integer) — The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. 



### #instance_group_urls
    
    
    def instance_group_urls() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Output only. The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool. During the node pool blue-green upgrade operation, the URLs contain both blue and green resources. 



### #kubelet_cert_info
    
    
    def kubelet_cert_info() -> ::Google::Cloud::Container::V1::NodePool::KubeletCertInfo

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::KubeletCertInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-KubeletCertInfo)) — Output only. Contains expiry information about the kubelet certificate. 



### #locations
    
    
    def locations() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located.

If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead.

Warning: changing node pool locations will result in nodes being added and/or removed. 




### #locations=
    
    
    def locations=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located.

If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead.

Warning: changing node pool locations will result in nodes being added and/or removed. 




**Returns**

  * (::Array<::String>) — The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located.

If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead.

Warning: changing node pool locations will result in nodes being added and/or removed. 




### #maintenance_policy
    
    
    def maintenance_policy() -> ::Google::Cloud::Container::V1::NodePool::NodePoolMaintenancePolicy

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::NodePoolMaintenancePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodePoolMaintenancePolicy)) — Optional. Specifies the maintenance policy for the node pool. 



### #maintenance_policy=
    
    
    def maintenance_policy=(value) -> ::Google::Cloud::Container::V1::NodePool::NodePoolMaintenancePolicy

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePool::NodePoolMaintenancePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodePoolMaintenancePolicy)) — Optional. Specifies the maintenance policy for the node pool. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::NodePoolMaintenancePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodePoolMaintenancePolicy)) — Optional. Specifies the maintenance policy for the node pool. 



### #management
    
    
    def management() -> ::Google::Cloud::Container::V1::NodeManagement

**Returns**

  * ([::Google::Cloud::Container::V1::NodeManagement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeManagement)) — NodeManagement configuration for this NodePool. 



### #management=
    
    
    def management=(value) -> ::Google::Cloud::Container::V1::NodeManagement

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeManagement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeManagement)) — NodeManagement configuration for this NodePool. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeManagement](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeManagement)) — NodeManagement configuration for this NodePool. 



### #max_pods_constraint
    
    
    def max_pods_constraint() -> ::Google::Cloud::Container::V1::MaxPodsConstraint

**Returns**

  * ([::Google::Cloud::Container::V1::MaxPodsConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MaxPodsConstraint)) — The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool. 



### #max_pods_constraint=
    
    
    def max_pods_constraint=(value) -> ::Google::Cloud::Container::V1::MaxPodsConstraint

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::MaxPodsConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MaxPodsConstraint)) — The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool. 



**Returns**

  * ([::Google::Cloud::Container::V1::MaxPodsConstraint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MaxPodsConstraint)) — The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — The name of the node pool. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the node pool. 



**Returns**

  * (::String) — The name of the node pool. 



### #network_config
    
    
    def network_config() -> ::Google::Cloud::Container::V1::NodeNetworkConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig)) — Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults. 



### #network_config=
    
    
    def network_config=(value) -> ::Google::Cloud::Container::V1::NodeNetworkConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig)) — Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeNetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeNetworkConfig)) — Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults. 



### #node_drain_config
    
    
    def node_drain_config() -> ::Google::Cloud::Container::V1::NodePool::NodeDrainConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::NodeDrainConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodeDrainConfig)) — Specifies the node drain configuration for this node pool. 



### #node_drain_config=
    
    
    def node_drain_config=(value) -> ::Google::Cloud::Container::V1::NodePool::NodeDrainConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePool::NodeDrainConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodeDrainConfig)) — Specifies the node drain configuration for this node pool. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::NodeDrainConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-NodeDrainConfig)) — Specifies the node drain configuration for this node pool. 



### #placement_policy
    
    
    def placement_policy() -> ::Google::Cloud::Container::V1::NodePool::PlacementPolicy

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::PlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-PlacementPolicy)) — Specifies the node placement policy. 



### #placement_policy=
    
    
    def placement_policy=(value) -> ::Google::Cloud::Container::V1::NodePool::PlacementPolicy

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePool::PlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-PlacementPolicy)) — Specifies the node placement policy. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::PlacementPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-PlacementPolicy)) — Specifies the node placement policy. 



### #pod_ipv4_cidr_size
    
    
    def pod_ipv4_cidr_size() -> ::Integer

**Returns**

  * (::Integer) — Output only. The pod CIDR block size per node in this node pool. 



### #queued_provisioning
    
    
    def queued_provisioning() -> ::Google::Cloud::Container::V1::NodePool::QueuedProvisioning

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::QueuedProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-QueuedProvisioning)) — Specifies the configuration of queued provisioning. 



### #queued_provisioning=
    
    
    def queued_provisioning=(value) -> ::Google::Cloud::Container::V1::NodePool::QueuedProvisioning

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePool::QueuedProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-QueuedProvisioning)) — Specifies the configuration of queued provisioning. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::QueuedProvisioning](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-QueuedProvisioning)) — Specifies the configuration of queued provisioning. 



### #self_link
    
    
    def self_link() -> ::String

**Returns**

  * (::String) — Output only. Server-defined URL for the resource. 



### #status
    
    
    def status() -> ::Google::Cloud::Container::V1::NodePool::Status

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-Status)) — Output only. The status of the nodes in this pool instance. 



### #status_message
    
    
    def status_message() -> ::String

**Returns**

  * (::String) — Output only. Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available. 



### #update_info
    
    
    def update_info() -> ::Google::Cloud::Container::V1::NodePool::UpdateInfo

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::UpdateInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-UpdateInfo)) — Output only. Update info contains relevant information during a node pool update. 



### #upgrade_settings
    
    
    def upgrade_settings() -> ::Google::Cloud::Container::V1::NodePool::UpgradeSettings

**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::UpgradeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-UpgradeSettings)) — Upgrade settings control disruption and speed of the upgrade. 



### #upgrade_settings=
    
    
    def upgrade_settings=(value) -> ::Google::Cloud::Container::V1::NodePool::UpgradeSettings

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePool::UpgradeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-UpgradeSettings)) — Upgrade settings control disruption and speed of the upgrade. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePool::UpgradeSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePool-UpgradeSettings)) — Upgrade settings control disruption and speed of the upgrade. 



### #version
    
    
    def version() -> ::String

**Returns**

  * (::String) — The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version). 



### #version=
    
    
    def version=(value) -> ::String

**Parameter**

  * **value** (::String) — The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version). 



**Returns**

  * (::String) — The version of Kubernetes running on this NodePool's nodes. If unspecified, it defaults as described [here](https://cloud.google.com/kubernetes-engine/versioning#specifying_node_version). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
