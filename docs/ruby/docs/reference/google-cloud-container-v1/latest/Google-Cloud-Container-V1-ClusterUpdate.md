---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate/
title: Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::ClusterUpdate (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:28.736307+00:00
---

# Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::ClusterUpdate (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Kubernetes Engine V1 API - Class Google::Cloud::Container::V1::ClusterUpdate (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.1  0.33.1  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.0  0.16.3  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.3 

Reference documentation and code samples for the Kubernetes Engine V1 API class Google::Cloud::Container::V1::ClusterUpdate.

ClusterUpdate describes an update to the cluster. Exactly one update can be applied to a cluster with each request, so at most one field can be provided.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #additional_pod_ranges_config
    
    
    def additional_pod_ranges_config() -> ::Google::Cloud::Container::V1::AdditionalPodRangesConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs. 



### #additional_pod_ranges_config=
    
    
    def additional_pod_ranges_config=(value) -> ::Google::Cloud::Container::V1::AdditionalPodRangesConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs. 



**Returns**

  * ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs. 



### #desired_additional_ip_ranges_config
    
    
    def desired_additional_ip_ranges_config() -> ::Google::Cloud::Container::V1::DesiredAdditionalIPRangesConfig

**Returns**

  * ([::Google::Cloud::Container::V1::DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredAdditionalIPRangesConfig)) — The desired config for additional subnetworks attached to the cluster. 



### #desired_additional_ip_ranges_config=
    
    
    def desired_additional_ip_ranges_config=(value) -> ::Google::Cloud::Container::V1::DesiredAdditionalIPRangesConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredAdditionalIPRangesConfig)) — The desired config for additional subnetworks attached to the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredAdditionalIPRangesConfig)) — The desired config for additional subnetworks attached to the cluster. 



### #desired_addons_config
    
    
    def desired_addons_config() -> ::Google::Cloud::Container::V1::AddonsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AddonsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AddonsConfig)) — Configurations for the various addons available to run in the cluster. 



### #desired_addons_config=
    
    
    def desired_addons_config=(value) -> ::Google::Cloud::Container::V1::AddonsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AddonsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AddonsConfig)) — Configurations for the various addons available to run in the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::AddonsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AddonsConfig)) — Configurations for the various addons available to run in the cluster. 



### #desired_anonymous_authentication_config
    
    
    def desired_anonymous_authentication_config() -> ::Google::Cloud::Container::V1::AnonymousAuthenticationConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AnonymousAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AnonymousAuthenticationConfig)) — Configuration for limiting anonymous access to all endpoints except the health checks. 



### #desired_anonymous_authentication_config=
    
    
    def desired_anonymous_authentication_config=(value) -> ::Google::Cloud::Container::V1::AnonymousAuthenticationConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AnonymousAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AnonymousAuthenticationConfig)) — Configuration for limiting anonymous access to all endpoints except the health checks. 



**Returns**

  * ([::Google::Cloud::Container::V1::AnonymousAuthenticationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AnonymousAuthenticationConfig)) — Configuration for limiting anonymous access to all endpoints except the health checks. 



### #desired_authenticator_groups_config
    
    
    def desired_authenticator_groups_config() -> ::Google::Cloud::Container::V1::AuthenticatorGroupsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AuthenticatorGroupsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AuthenticatorGroupsConfig)) — The desired authenticator groups config for the cluster. 



### #desired_authenticator_groups_config=
    
    
    def desired_authenticator_groups_config=(value) -> ::Google::Cloud::Container::V1::AuthenticatorGroupsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AuthenticatorGroupsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AuthenticatorGroupsConfig)) — The desired authenticator groups config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::AuthenticatorGroupsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AuthenticatorGroupsConfig)) — The desired authenticator groups config for the cluster. 



### #desired_auto_ipam_config
    
    
    def desired_auto_ipam_config() -> ::Google::Cloud::Container::V1::AutoIpamConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AutoIpamConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AutoIpamConfig)) — AutoIpamConfig contains all information related to Auto IPAM 



### #desired_auto_ipam_config=
    
    
    def desired_auto_ipam_config=(value) -> ::Google::Cloud::Container::V1::AutoIpamConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AutoIpamConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AutoIpamConfig)) — AutoIpamConfig contains all information related to Auto IPAM 



**Returns**

  * ([::Google::Cloud::Container::V1::AutoIpamConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AutoIpamConfig)) — AutoIpamConfig contains all information related to Auto IPAM 



### #desired_autopilot_cluster_policy_config
    
    
    def desired_autopilot_cluster_policy_config() -> ::Google::Cloud::Container::V1::ClusterPolicyConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ClusterPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterPolicyConfig)) — The desired autopilot cluster policies that to be enforced in the cluster. 



### #desired_autopilot_cluster_policy_config=
    
    
    def desired_autopilot_cluster_policy_config=(value) -> ::Google::Cloud::Container::V1::ClusterPolicyConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ClusterPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterPolicyConfig)) — The desired autopilot cluster policies that to be enforced in the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::ClusterPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterPolicyConfig)) — The desired autopilot cluster policies that to be enforced in the cluster. 



### #desired_autopilot_workload_policy_config
    
    
    def desired_autopilot_workload_policy_config() -> ::Google::Cloud::Container::V1::WorkloadPolicyConfig

**Returns**

  * ([::Google::Cloud::Container::V1::WorkloadPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadPolicyConfig)) — WorkloadPolicyConfig is the configuration related to GCW workload policy 



### #desired_autopilot_workload_policy_config=
    
    
    def desired_autopilot_workload_policy_config=(value) -> ::Google::Cloud::Container::V1::WorkloadPolicyConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::WorkloadPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadPolicyConfig)) — WorkloadPolicyConfig is the configuration related to GCW workload policy 



**Returns**

  * ([::Google::Cloud::Container::V1::WorkloadPolicyConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadPolicyConfig)) — WorkloadPolicyConfig is the configuration related to GCW workload policy 



### #desired_binary_authorization
    
    
    def desired_binary_authorization() -> ::Google::Cloud::Container::V1::BinaryAuthorization

**Returns**

  * ([::Google::Cloud::Container::V1::BinaryAuthorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BinaryAuthorization)) — The desired configuration options for the Binary Authorization feature. 



### #desired_binary_authorization=
    
    
    def desired_binary_authorization=(value) -> ::Google::Cloud::Container::V1::BinaryAuthorization

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::BinaryAuthorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BinaryAuthorization)) — The desired configuration options for the Binary Authorization feature. 



**Returns**

  * ([::Google::Cloud::Container::V1::BinaryAuthorization](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-BinaryAuthorization)) — The desired configuration options for the Binary Authorization feature. 



### #desired_cluster_autoscaling
    
    
    def desired_cluster_autoscaling() -> ::Google::Cloud::Container::V1::ClusterAutoscaling

**Returns**

  * ([::Google::Cloud::Container::V1::ClusterAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterAutoscaling)) — Cluster-level autoscaling configuration. 



### #desired_cluster_autoscaling=
    
    
    def desired_cluster_autoscaling=(value) -> ::Google::Cloud::Container::V1::ClusterAutoscaling

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ClusterAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterAutoscaling)) — Cluster-level autoscaling configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ClusterAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterAutoscaling)) — Cluster-level autoscaling configuration. 



### #desired_compliance_posture_config
    
    
    def desired_compliance_posture_config() -> ::Google::Cloud::Container::V1::CompliancePostureConfig

**Returns**

  * ([::Google::Cloud::Container::V1::CompliancePostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CompliancePostureConfig)) — Deprecated: Compliance Posture is no longer supported. For more details, see https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation.

Enable/Disable Compliance Posture features for the cluster. 




### #desired_compliance_posture_config=
    
    
    def desired_compliance_posture_config=(value) -> ::Google::Cloud::Container::V1::CompliancePostureConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::CompliancePostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CompliancePostureConfig)) — Deprecated: Compliance Posture is no longer supported. For more details, see https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation.

Enable/Disable Compliance Posture features for the cluster. 




**Returns**

  * ([::Google::Cloud::Container::V1::CompliancePostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CompliancePostureConfig)) — Deprecated: Compliance Posture is no longer supported. For more details, see https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation.

Enable/Disable Compliance Posture features for the cluster. 




### #desired_containerd_config
    
    
    def desired_containerd_config() -> ::Google::Cloud::Container::V1::ContainerdConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ContainerdConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ContainerdConfig)) — The desired containerd config for the cluster. 



### #desired_containerd_config=
    
    
    def desired_containerd_config=(value) -> ::Google::Cloud::Container::V1::ContainerdConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ContainerdConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ContainerdConfig)) — The desired containerd config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::ContainerdConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ContainerdConfig)) — The desired containerd config for the cluster. 



### #desired_control_plane_egress
    
    
    def desired_control_plane_egress() -> ::Google::Cloud::Container::V1::ControlPlaneEgress

**Returns**

  * ([::Google::Cloud::Container::V1::ControlPlaneEgress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEgress)) — The desired control plane egress control config for the cluster. 



### #desired_control_plane_egress=
    
    
    def desired_control_plane_egress=(value) -> ::Google::Cloud::Container::V1::ControlPlaneEgress

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ControlPlaneEgress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEgress)) — The desired control plane egress control config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::ControlPlaneEgress](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEgress)) — The desired control plane egress control config for the cluster. 



### #desired_control_plane_endpoints_config
    
    
    def desired_control_plane_endpoints_config() -> ::Google::Cloud::Container::V1::ControlPlaneEndpointsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ControlPlaneEndpointsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEndpointsConfig)) — [Control plane endpoints][google.container.v1.Cluster.control_plane_endpoints_config] configuration. 



### #desired_control_plane_endpoints_config=
    
    
    def desired_control_plane_endpoints_config=(value) -> ::Google::Cloud::Container::V1::ControlPlaneEndpointsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ControlPlaneEndpointsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEndpointsConfig)) — [Control plane endpoints][google.container.v1.Cluster.control_plane_endpoints_config] configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ControlPlaneEndpointsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ControlPlaneEndpointsConfig)) — [Control plane endpoints][google.container.v1.Cluster.control_plane_endpoints_config] configuration. 



### #desired_cost_management_config
    
    
    def desired_cost_management_config() -> ::Google::Cloud::Container::V1::CostManagementConfig

**Returns**

  * ([::Google::Cloud::Container::V1::CostManagementConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CostManagementConfig)) — The desired configuration for the fine-grained cost management feature. 



### #desired_cost_management_config=
    
    
    def desired_cost_management_config=(value) -> ::Google::Cloud::Container::V1::CostManagementConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::CostManagementConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CostManagementConfig)) — The desired configuration for the fine-grained cost management feature. 



**Returns**

  * ([::Google::Cloud::Container::V1::CostManagementConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-CostManagementConfig)) — The desired configuration for the fine-grained cost management feature. 



### #desired_database_encryption
    
    
    def desired_database_encryption() -> ::Google::Cloud::Container::V1::DatabaseEncryption

**Returns**

  * ([::Google::Cloud::Container::V1::DatabaseEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatabaseEncryption)) — Configuration of etcd encryption. 



### #desired_database_encryption=
    
    
    def desired_database_encryption=(value) -> ::Google::Cloud::Container::V1::DatabaseEncryption

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DatabaseEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatabaseEncryption)) — Configuration of etcd encryption. 



**Returns**

  * ([::Google::Cloud::Container::V1::DatabaseEncryption](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatabaseEncryption)) — Configuration of etcd encryption. 



### #desired_datapath_provider
    
    
    def desired_datapath_provider() -> ::Google::Cloud::Container::V1::DatapathProvider

**Returns**

  * ([::Google::Cloud::Container::V1::DatapathProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatapathProvider)) — The desired datapath provider for the cluster. 



### #desired_datapath_provider=
    
    
    def desired_datapath_provider=(value) -> ::Google::Cloud::Container::V1::DatapathProvider

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DatapathProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatapathProvider)) — The desired datapath provider for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::DatapathProvider](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DatapathProvider)) — The desired datapath provider for the cluster. 



### #desired_default_enable_private_nodes
    
    
    def desired_default_enable_private_nodes() -> ::Boolean

**Returns**

  * (::Boolean) — Override the default setting of whether future created nodes have private IP addresses only, namely [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig#Google__Cloud__Container__V1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1::NetworkConfig#default_enable_private_nodes \(method\)")



### #desired_default_enable_private_nodes=
    
    
    def desired_default_enable_private_nodes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Override the default setting of whether future created nodes have private IP addresses only, namely [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig#Google__Cloud__Container__V1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1::NetworkConfig#default_enable_private_nodes \(method\)")



**Returns**

  * (::Boolean) — Override the default setting of whether future created nodes have private IP addresses only, namely [NetworkConfig.default_enable_private_nodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig#Google__Cloud__Container__V1__NetworkConfig_default_enable_private_nodes_instance_ "Google::Cloud::Container::V1::NetworkConfig#default_enable_private_nodes \(method\)")



### #desired_default_snat_status
    
    
    def desired_default_snat_status() -> ::Google::Cloud::Container::V1::DefaultSnatStatus

**Returns**

  * ([::Google::Cloud::Container::V1::DefaultSnatStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DefaultSnatStatus)) — The desired status of whether to disable default sNAT for this cluster. 



### #desired_default_snat_status=
    
    
    def desired_default_snat_status=(value) -> ::Google::Cloud::Container::V1::DefaultSnatStatus

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DefaultSnatStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DefaultSnatStatus)) — The desired status of whether to disable default sNAT for this cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::DefaultSnatStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DefaultSnatStatus)) — The desired status of whether to disable default sNAT for this cluster. 



### #desired_disable_l4_lb_firewall_reconciliation
    
    
    def desired_disable_l4_lb_firewall_reconciliation() -> ::Boolean

**Returns**

  * (::Boolean) — Enable/Disable L4 LB VPC firewall reconciliation for the cluster. 



### #desired_disable_l4_lb_firewall_reconciliation=
    
    
    def desired_disable_l4_lb_firewall_reconciliation=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable/Disable L4 LB VPC firewall reconciliation for the cluster. 



**Returns**

  * (::Boolean) — Enable/Disable L4 LB VPC firewall reconciliation for the cluster. 



### #desired_dns_config
    
    
    def desired_dns_config() -> ::Google::Cloud::Container::V1::DNSConfig

**Returns**

  * ([::Google::Cloud::Container::V1::DNSConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DNSConfig)) — DNSConfig contains clusterDNS config for this cluster. 



### #desired_dns_config=
    
    
    def desired_dns_config=(value) -> ::Google::Cloud::Container::V1::DNSConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DNSConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DNSConfig)) — DNSConfig contains clusterDNS config for this cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::DNSConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DNSConfig)) — DNSConfig contains clusterDNS config for this cluster. 



### #desired_emulated_version
    
    
    def desired_emulated_version() -> ::String

**Returns**

  * (::String) — Optional. The desired emulated version for the cluster. 



### #desired_emulated_version=
    
    
    def desired_emulated_version=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The desired emulated version for the cluster. 



**Returns**

  * (::String) — Optional. The desired emulated version for the cluster. 



### #desired_enable_cilium_clusterwide_network_policy
    
    
    def desired_enable_cilium_clusterwide_network_policy() -> ::Boolean

**Returns**

  * (::Boolean) — Enable/Disable Cilium Clusterwide Network Policy for the cluster. 



### #desired_enable_cilium_clusterwide_network_policy=
    
    
    def desired_enable_cilium_clusterwide_network_policy=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable/Disable Cilium Clusterwide Network Policy for the cluster. 



**Returns**

  * (::Boolean) — Enable/Disable Cilium Clusterwide Network Policy for the cluster. 



### #desired_enable_fqdn_network_policy
    
    
    def desired_enable_fqdn_network_policy() -> ::Boolean

**Returns**

  * (::Boolean) — Enable/Disable FQDN Network Policy for the cluster. 



### #desired_enable_fqdn_network_policy=
    
    
    def desired_enable_fqdn_network_policy=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable/Disable FQDN Network Policy for the cluster. 



**Returns**

  * (::Boolean) — Enable/Disable FQDN Network Policy for the cluster. 



### #desired_enable_multi_networking
    
    
    def desired_enable_multi_networking() -> ::Boolean

**Returns**

  * (::Boolean) — Enable/Disable Multi-Networking for the cluster 



### #desired_enable_multi_networking=
    
    
    def desired_enable_multi_networking=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable/Disable Multi-Networking for the cluster 



**Returns**

  * (::Boolean) — Enable/Disable Multi-Networking for the cluster 



### #desired_enable_private_endpoint
    
    
    def desired_enable_private_endpoint() -> ::Boolean

**Returns**

  * (::Boolean) — Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 




### #desired_enable_private_endpoint=
    
    
    def desired_enable_private_endpoint=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 




**Returns**

  * (::Boolean) — Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true. 




### #desired_enterprise_config
    
    
    def desired_enterprise_config() -> ::Google::Cloud::Container::V1::DesiredEnterpriseConfig

**Returns**

  * ([::Google::Cloud::Container::V1::DesiredEnterpriseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredEnterpriseConfig)) — The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier. 




### #desired_enterprise_config=
    
    
    def desired_enterprise_config=(value) -> ::Google::Cloud::Container::V1::DesiredEnterpriseConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::DesiredEnterpriseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredEnterpriseConfig)) — The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier. 




**Returns**

  * ([::Google::Cloud::Container::V1::DesiredEnterpriseConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-DesiredEnterpriseConfig)) — The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier. 




### #desired_fleet
    
    
    def desired_fleet() -> ::Google::Cloud::Container::V1::Fleet

**Returns**

  * ([::Google::Cloud::Container::V1::Fleet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-Fleet)) — The desired fleet configuration for the cluster. 



### #desired_fleet=
    
    
    def desired_fleet=(value) -> ::Google::Cloud::Container::V1::Fleet

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::Fleet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-Fleet)) — The desired fleet configuration for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::Fleet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-Fleet)) — The desired fleet configuration for the cluster. 



### #desired_gateway_api_config
    
    
    def desired_gateway_api_config() -> ::Google::Cloud::Container::V1::GatewayAPIConfig

**Returns**

  * ([::Google::Cloud::Container::V1::GatewayAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GatewayAPIConfig)) — The desired config of Gateway API on this cluster. 



### #desired_gateway_api_config=
    
    
    def desired_gateway_api_config=(value) -> ::Google::Cloud::Container::V1::GatewayAPIConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::GatewayAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GatewayAPIConfig)) — The desired config of Gateway API on this cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::GatewayAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GatewayAPIConfig)) — The desired config of Gateway API on this cluster. 



### #desired_gcfs_config
    
    
    def desired_gcfs_config() -> ::Google::Cloud::Container::V1::GcfsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::GcfsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GcfsConfig)) — The desired GCFS config for the cluster 



### #desired_gcfs_config=
    
    
    def desired_gcfs_config=(value) -> ::Google::Cloud::Container::V1::GcfsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::GcfsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GcfsConfig)) — The desired GCFS config for the cluster 



**Returns**

  * ([::Google::Cloud::Container::V1::GcfsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GcfsConfig)) — The desired GCFS config for the cluster 



### #desired_identity_service_config
    
    
    def desired_identity_service_config() -> ::Google::Cloud::Container::V1::IdentityServiceConfig

**Returns**

  * ([::Google::Cloud::Container::V1::IdentityServiceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IdentityServiceConfig)) — The desired Identity Service component configuration. 



### #desired_identity_service_config=
    
    
    def desired_identity_service_config=(value) -> ::Google::Cloud::Container::V1::IdentityServiceConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::IdentityServiceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IdentityServiceConfig)) — The desired Identity Service component configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::IdentityServiceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IdentityServiceConfig)) — The desired Identity Service component configuration. 



### #desired_image
    
    
    def desired_image() -> ::String

**Returns**

  * (::String) — The desired name of the image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



### #desired_image=
    
    
    def desired_image=(value) -> ::String

**Parameter**

  * **value** (::String) — The desired name of the image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



**Returns**

  * (::String) — The desired name of the image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



### #desired_image_project
    
    
    def desired_image_project() -> ::String

**Returns**

  * (::String) — The project containing the desired image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



### #desired_image_project=
    
    
    def desired_image_project=(value) -> ::String

**Parameter**

  * **value** (::String) — The project containing the desired image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



**Returns**

  * (::String) — The project containing the desired image to use for this node. This is used to create clusters using a custom image. NOTE: Set the "desired_node_pool" field as well. 



### #desired_image_type
    
    
    def desired_image_type() -> ::String

**Returns**

  * (::String) — The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well. 



### #desired_image_type=
    
    
    def desired_image_type=(value) -> ::String

**Parameter**

  * **value** (::String) — The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well. 



**Returns**

  * (::String) — The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well. 



### #desired_in_transit_encryption_config
    
    
    def desired_in_transit_encryption_config() -> ::Google::Cloud::Container::V1::InTransitEncryptionConfig

**Returns**

  * ([::Google::Cloud::Container::V1::InTransitEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-InTransitEncryptionConfig)) — Specify the details of in-transit encryption. 



### #desired_in_transit_encryption_config=
    
    
    def desired_in_transit_encryption_config=(value) -> ::Google::Cloud::Container::V1::InTransitEncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::InTransitEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-InTransitEncryptionConfig)) — Specify the details of in-transit encryption. 



**Returns**

  * ([::Google::Cloud::Container::V1::InTransitEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-InTransitEncryptionConfig)) — Specify the details of in-transit encryption. 



### #desired_intra_node_visibility_config
    
    
    def desired_intra_node_visibility_config() -> ::Google::Cloud::Container::V1::IntraNodeVisibilityConfig

**Returns**

  * ([::Google::Cloud::Container::V1::IntraNodeVisibilityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IntraNodeVisibilityConfig)) — The desired config of Intra-node visibility. 



### #desired_intra_node_visibility_config=
    
    
    def desired_intra_node_visibility_config=(value) -> ::Google::Cloud::Container::V1::IntraNodeVisibilityConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::IntraNodeVisibilityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IntraNodeVisibilityConfig)) — The desired config of Intra-node visibility. 



**Returns**

  * ([::Google::Cloud::Container::V1::IntraNodeVisibilityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-IntraNodeVisibilityConfig)) — The desired config of Intra-node visibility. 



### #desired_k8s_beta_apis
    
    
    def desired_k8s_beta_apis() -> ::Google::Cloud::Container::V1::K8sBetaAPIConfig

**Returns**

  * ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Desired Beta APIs to be enabled for cluster. 



### #desired_k8s_beta_apis=
    
    
    def desired_k8s_beta_apis=(value) -> ::Google::Cloud::Container::V1::K8sBetaAPIConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Desired Beta APIs to be enabled for cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Desired Beta APIs to be enabled for cluster. 



### #desired_l4ilb_subsetting_config
    
    
    def desired_l4ilb_subsetting_config() -> ::Google::Cloud::Container::V1::ILBSubsettingConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ILBSubsettingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ILBSubsettingConfig)) — The desired L4 Internal Load Balancer Subsetting configuration. 



### #desired_l4ilb_subsetting_config=
    
    
    def desired_l4ilb_subsetting_config=(value) -> ::Google::Cloud::Container::V1::ILBSubsettingConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ILBSubsettingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ILBSubsettingConfig)) — The desired L4 Internal Load Balancer Subsetting configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ILBSubsettingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ILBSubsettingConfig)) — The desired L4 Internal Load Balancer Subsetting configuration. 



### #desired_locations
    
    
    def desired_locations() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed. 




### #desired_locations=
    
    
    def desired_locations=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed. 




**Returns**

  * (::Array<::String>) — The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed. 




### #desired_logging_config
    
    
    def desired_logging_config() -> ::Google::Cloud::Container::V1::LoggingConfig

**Returns**

  * ([::Google::Cloud::Container::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LoggingConfig)) — The desired logging configuration. 



### #desired_logging_config=
    
    
    def desired_logging_config=(value) -> ::Google::Cloud::Container::V1::LoggingConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LoggingConfig)) — The desired logging configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::LoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LoggingConfig)) — The desired logging configuration. 



### #desired_logging_service
    
    
    def desired_logging_service() -> ::String

**Returns**

  * (::String) — The logging service the cluster should use to write logs. Currently available options:

    * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
    * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
    * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions. 




### #desired_logging_service=
    
    
    def desired_logging_service=(value) -> ::String

**Parameter**

  * **value** (::String) — The logging service the cluster should use to write logs. Currently available options:

    * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
    * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
    * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions. 




**Returns**

  * (::String) — The logging service the cluster should use to write logs. Currently available options:

    * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
    * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
    * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions. 




### #desired_managed_machine_learning_diagnostics_config
    
    
    def desired_managed_machine_learning_diagnostics_config() -> ::Google::Cloud::Container::V1::ManagedMachineLearningDiagnosticsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedMachineLearningDiagnosticsConfig)) — The desired managed machine learning diagnostics configuration. 



### #desired_managed_machine_learning_diagnostics_config=
    
    
    def desired_managed_machine_learning_diagnostics_config=(value) -> ::Google::Cloud::Container::V1::ManagedMachineLearningDiagnosticsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedMachineLearningDiagnosticsConfig)) — The desired managed machine learning diagnostics configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedMachineLearningDiagnosticsConfig)) — The desired managed machine learning diagnostics configuration. 



### #desired_managed_opentelemetry_config
    
    
    def desired_managed_opentelemetry_config() -> ::Google::Cloud::Container::V1::ManagedOpenTelemetryConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ManagedOpenTelemetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedOpenTelemetryConfig)) — The desired managed open telemetry configuration. 



### #desired_managed_opentelemetry_config=
    
    
    def desired_managed_opentelemetry_config=(value) -> ::Google::Cloud::Container::V1::ManagedOpenTelemetryConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ManagedOpenTelemetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedOpenTelemetryConfig)) — The desired managed open telemetry configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ManagedOpenTelemetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ManagedOpenTelemetryConfig)) — The desired managed open telemetry configuration. 



### #desired_master_authorized_networks_config
    
    
    def desired_master_authorized_networks_config() -> ::Google::Cloud::Container::V1::MasterAuthorizedNetworksConfig

**Returns**

  * ([::Google::Cloud::Container::V1::MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MasterAuthorizedNetworksConfig)) — The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead. 




### #desired_master_authorized_networks_config=
    
    
    def desired_master_authorized_networks_config=(value) -> ::Google::Cloud::Container::V1::MasterAuthorizedNetworksConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MasterAuthorizedNetworksConfig)) — The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead. 




**Returns**

  * ([::Google::Cloud::Container::V1::MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MasterAuthorizedNetworksConfig)) — The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead. 




### #desired_master_version
    
    
    def desired_master_version() -> ::String

**Returns**

  * (::String) — 

The Kubernetes version to change the master to.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the default Kubernetes version



### #desired_master_version=
    
    
    def desired_master_version=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The Kubernetes version to change the master to.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the default Kubernetes version



**Returns**

  * (::String) — 

The Kubernetes version to change the master to.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the default Kubernetes version



### #desired_mesh_certificates
    
    
    def desired_mesh_certificates() -> ::Google::Cloud::Container::V1::MeshCertificates

**Returns**

  * ([::Google::Cloud::Container::V1::MeshCertificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MeshCertificates)) — Configuration for issuance of mTLS keys and certificates to Kubernetes pods. 



### #desired_mesh_certificates=
    
    
    def desired_mesh_certificates=(value) -> ::Google::Cloud::Container::V1::MeshCertificates

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::MeshCertificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MeshCertificates)) — Configuration for issuance of mTLS keys and certificates to Kubernetes pods. 



**Returns**

  * ([::Google::Cloud::Container::V1::MeshCertificates](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MeshCertificates)) — Configuration for issuance of mTLS keys and certificates to Kubernetes pods. 



### #desired_monitoring_config
    
    
    def desired_monitoring_config() -> ::Google::Cloud::Container::V1::MonitoringConfig

**Returns**

  * ([::Google::Cloud::Container::V1::MonitoringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MonitoringConfig)) — The desired monitoring configuration. 



### #desired_monitoring_config=
    
    
    def desired_monitoring_config=(value) -> ::Google::Cloud::Container::V1::MonitoringConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::MonitoringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MonitoringConfig)) — The desired monitoring configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::MonitoringConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-MonitoringConfig)) — The desired monitoring configuration. 



### #desired_monitoring_service
    
    
    def desired_monitoring_service() -> ::String

**Returns**

  * (::String) — The monitoring service the cluster should use to write metrics. Currently available options:

    * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
    * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
    * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions. 




### #desired_monitoring_service=
    
    
    def desired_monitoring_service=(value) -> ::String

**Parameter**

  * **value** (::String) — The monitoring service the cluster should use to write metrics. Currently available options:

    * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
    * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
    * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions. 




**Returns**

  * (::String) — The monitoring service the cluster should use to write metrics. Currently available options:

    * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
    * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
    * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions. 




### #desired_network_performance_config
    
    
    def desired_network_performance_config() -> ::Google::Cloud::Container::V1::NetworkConfig::ClusterNetworkPerformanceConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NetworkConfig::ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig-ClusterNetworkPerformanceConfig)) — The desired network performance config. 



### #desired_network_performance_config=
    
    
    def desired_network_performance_config=(value) -> ::Google::Cloud::Container::V1::NetworkConfig::ClusterNetworkPerformanceConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NetworkConfig::ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig-ClusterNetworkPerformanceConfig)) — The desired network performance config. 



**Returns**

  * ([::Google::Cloud::Container::V1::NetworkConfig::ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkConfig-ClusterNetworkPerformanceConfig)) — The desired network performance config. 



### #desired_network_tier_config
    
    
    def desired_network_tier_config() -> ::Google::Cloud::Container::V1::NetworkTierConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NetworkTierConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTierConfig)) — The desired network tier configuration for the cluster. 



### #desired_network_tier_config=
    
    
    def desired_network_tier_config=(value) -> ::Google::Cloud::Container::V1::NetworkTierConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NetworkTierConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTierConfig)) — The desired network tier configuration for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::NetworkTierConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTierConfig)) — The desired network tier configuration for the cluster. 



### #desired_node_creation_config
    
    
    def desired_node_creation_config() -> ::Google::Cloud::Container::V1::NodeCreationConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeCreationConfig)) — Optional. The desired NodeCreationConfig for the cluster. 



### #desired_node_creation_config=
    
    
    def desired_node_creation_config=(value) -> ::Google::Cloud::Container::V1::NodeCreationConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeCreationConfig)) — Optional. The desired NodeCreationConfig for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeCreationConfig)) — Optional. The desired NodeCreationConfig for the cluster. 



### #desired_node_kubelet_config
    
    
    def desired_node_kubelet_config() -> ::Google::Cloud::Container::V1::NodeKubeletConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for the cluster. 



### #desired_node_kubelet_config=
    
    
    def desired_node_kubelet_config=(value) -> ::Google::Cloud::Container::V1::NodeKubeletConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for the cluster. 



### #desired_node_pool_auto_config_kubelet_config
    
    
    def desired_node_pool_auto_config_kubelet_config() -> ::Google::Cloud::Container::V1::NodeKubeletConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_auto_config_kubelet_config=
    
    
    def desired_node_pool_auto_config_kubelet_config=(value) -> ::Google::Cloud::Container::V1::NodeKubeletConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodeKubeletConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodeKubeletConfig)) — The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_auto_config_linux_node_config
    
    
    def desired_node_pool_auto_config_linux_node_config() -> ::Google::Cloud::Container::V1::LinuxNodeConfig

**Returns**

  * ([::Google::Cloud::Container::V1::LinuxNodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LinuxNodeConfig)) — The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here. 




### #desired_node_pool_auto_config_linux_node_config=
    
    
    def desired_node_pool_auto_config_linux_node_config=(value) -> ::Google::Cloud::Container::V1::LinuxNodeConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::LinuxNodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LinuxNodeConfig)) — The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here. 




**Returns**

  * ([::Google::Cloud::Container::V1::LinuxNodeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-LinuxNodeConfig)) — The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here. 




### #desired_node_pool_auto_config_network_tags
    
    
    def desired_node_pool_auto_config_network_tags() -> ::Google::Cloud::Container::V1::NetworkTags

**Returns**

  * ([::Google::Cloud::Container::V1::NetworkTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTags)) — The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_auto_config_network_tags=
    
    
    def desired_node_pool_auto_config_network_tags=(value) -> ::Google::Cloud::Container::V1::NetworkTags

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NetworkTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTags)) — The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



**Returns**

  * ([::Google::Cloud::Container::V1::NetworkTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NetworkTags)) — The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_auto_config_resource_manager_tags
    
    
    def desired_node_pool_auto_config_resource_manager_tags() -> ::Google::Cloud::Container::V1::ResourceManagerTags

**Returns**

  * ([::Google::Cloud::Container::V1::ResourceManagerTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceManagerTags)) — The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_auto_config_resource_manager_tags=
    
    
    def desired_node_pool_auto_config_resource_manager_tags=(value) -> ::Google::Cloud::Container::V1::ResourceManagerTags

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ResourceManagerTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceManagerTags)) — The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



**Returns**

  * ([::Google::Cloud::Container::V1::ResourceManagerTags](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceManagerTags)) — The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters. 



### #desired_node_pool_autoscaling
    
    
    def desired_node_pool_autoscaling() -> ::Google::Cloud::Container::V1::NodePoolAutoscaling

**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool. 



### #desired_node_pool_autoscaling=
    
    
    def desired_node_pool_autoscaling=(value) -> ::Google::Cloud::Container::V1::NodePoolAutoscaling

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolAutoscaling)) — Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool. 



### #desired_node_pool_id
    
    
    def desired_node_pool_id() -> ::String

**Returns**

  * (::String) — The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster. 



### #desired_node_pool_id=
    
    
    def desired_node_pool_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster. 



**Returns**

  * (::String) — The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster. 



### #desired_node_pool_logging_config
    
    
    def desired_node_pool_logging_config() -> ::Google::Cloud::Container::V1::NodePoolLoggingConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolLoggingConfig)) — The desired node pool logging configuration defaults for the cluster. 



### #desired_node_pool_logging_config=
    
    
    def desired_node_pool_logging_config=(value) -> ::Google::Cloud::Container::V1::NodePoolLoggingConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NodePoolLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolLoggingConfig)) — The desired node pool logging configuration defaults for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::NodePoolLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NodePoolLoggingConfig)) — The desired node pool logging configuration defaults for the cluster. 



### #desired_node_version
    
    
    def desired_node_version() -> ::String

**Returns**

  * (::String) — 

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the Kubernetes master version



### #desired_node_version=
    
    
    def desired_node_version=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the Kubernetes master version



**Returns**

  * (::String) — 

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

    * "latest": picks the highest valid Kubernetes version
    * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
    * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
    * "1.X.Y-gke.N": picks an explicit Kubernetes version
    * "-": picks the Kubernetes master version



### #desired_notification_config
    
    
    def desired_notification_config() -> ::Google::Cloud::Container::V1::NotificationConfig

**Returns**

  * ([::Google::Cloud::Container::V1::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NotificationConfig)) — The desired notification configuration. 



### #desired_notification_config=
    
    
    def desired_notification_config=(value) -> ::Google::Cloud::Container::V1::NotificationConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NotificationConfig)) — The desired notification configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::NotificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-NotificationConfig)) — The desired notification configuration. 



### #desired_pod_autoscaling
    
    
    def desired_pod_autoscaling() -> ::Google::Cloud::Container::V1::PodAutoscaling

**Returns**

  * ([::Google::Cloud::Container::V1::PodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodAutoscaling)) — The desired config for pod autoscaling. 



### #desired_pod_autoscaling=
    
    
    def desired_pod_autoscaling=(value) -> ::Google::Cloud::Container::V1::PodAutoscaling

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::PodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodAutoscaling)) — The desired config for pod autoscaling. 



**Returns**

  * ([::Google::Cloud::Container::V1::PodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PodAutoscaling)) — The desired config for pod autoscaling. 



### #desired_private_cluster_config
    
    
    def desired_private_cluster_config() -> ::Google::Cloud::Container::V1::PrivateClusterConfig

**Returns**

  * ([::Google::Cloud::Container::V1::PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig)) — The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also [ClusterUpdate.desired_enable_private_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_enable_private_endpoint_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_enable_private_endpoint \(method\)") for modifying other fields within [PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig "Google::Cloud::Container::V1::PrivateClusterConfig \(class\)").

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead. 




### #desired_private_cluster_config=
    
    
    def desired_private_cluster_config=(value) -> ::Google::Cloud::Container::V1::PrivateClusterConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig)) — The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also [ClusterUpdate.desired_enable_private_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_enable_private_endpoint_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_enable_private_endpoint \(method\)") for modifying other fields within [PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig "Google::Cloud::Container::V1::PrivateClusterConfig \(class\)").

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead. 




**Returns**

  * ([::Google::Cloud::Container::V1::PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig)) — The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also [ClusterUpdate.desired_enable_private_endpoint](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_enable_private_endpoint_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_enable_private_endpoint \(method\)") for modifying other fields within [PrivateClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateClusterConfig "Google::Cloud::Container::V1::PrivateClusterConfig \(class\)").

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead. 




### #desired_private_ipv6_google_access
    
    
    def desired_private_ipv6_google_access() -> ::Google::Cloud::Container::V1::PrivateIPv6GoogleAccess

**Returns**

  * ([::Google::Cloud::Container::V1::PrivateIPv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateIPv6GoogleAccess)) — The desired state of IPv6 connectivity to Google Services. 



### #desired_private_ipv6_google_access=
    
    
    def desired_private_ipv6_google_access=(value) -> ::Google::Cloud::Container::V1::PrivateIPv6GoogleAccess

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::PrivateIPv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateIPv6GoogleAccess)) — The desired state of IPv6 connectivity to Google Services. 



**Returns**

  * ([::Google::Cloud::Container::V1::PrivateIPv6GoogleAccess](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivateIPv6GoogleAccess)) — The desired state of IPv6 connectivity to Google Services. 



### #desired_privileged_admission_config
    
    
    def desired_privileged_admission_config() -> ::Google::Cloud::Container::V1::PrivilegedAdmissionConfig

**Returns**

  * ([::Google::Cloud::Container::V1::PrivilegedAdmissionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivilegedAdmissionConfig)) — The desired privileged admission config for the cluster. 



### #desired_privileged_admission_config=
    
    
    def desired_privileged_admission_config=(value) -> ::Google::Cloud::Container::V1::PrivilegedAdmissionConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::PrivilegedAdmissionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivilegedAdmissionConfig)) — The desired privileged admission config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::PrivilegedAdmissionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-PrivilegedAdmissionConfig)) — The desired privileged admission config for the cluster. 



### #desired_rbac_binding_config
    
    
    def desired_rbac_binding_config() -> ::Google::Cloud::Container::V1::RBACBindingConfig

**Returns**

  * ([::Google::Cloud::Container::V1::RBACBindingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RBACBindingConfig)) — RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created. 



### #desired_rbac_binding_config=
    
    
    def desired_rbac_binding_config=(value) -> ::Google::Cloud::Container::V1::RBACBindingConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::RBACBindingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RBACBindingConfig)) — RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created. 



**Returns**

  * ([::Google::Cloud::Container::V1::RBACBindingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RBACBindingConfig)) — RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created. 



### #desired_release_channel
    
    
    def desired_release_channel() -> ::Google::Cloud::Container::V1::ReleaseChannel

**Returns**

  * ([::Google::Cloud::Container::V1::ReleaseChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ReleaseChannel)) — The desired release channel configuration. 



### #desired_release_channel=
    
    
    def desired_release_channel=(value) -> ::Google::Cloud::Container::V1::ReleaseChannel

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ReleaseChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ReleaseChannel)) — The desired release channel configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::ReleaseChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ReleaseChannel)) — The desired release channel configuration. 



### #desired_resource_usage_export_config
    
    
    def desired_resource_usage_export_config() -> ::Google::Cloud::Container::V1::ResourceUsageExportConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ResourceUsageExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceUsageExportConfig)) — The desired configuration for exporting resource usage. 



### #desired_resource_usage_export_config=
    
    
    def desired_resource_usage_export_config=(value) -> ::Google::Cloud::Container::V1::ResourceUsageExportConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ResourceUsageExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceUsageExportConfig)) — The desired configuration for exporting resource usage. 



**Returns**

  * ([::Google::Cloud::Container::V1::ResourceUsageExportConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ResourceUsageExportConfig)) — The desired configuration for exporting resource usage. 



### #desired_rollback_safe_upgrade
    
    
    def desired_rollback_safe_upgrade() -> ::Google::Cloud::Container::V1::RollbackSafeUpgrade

**Returns**

  * ([::Google::Cloud::Container::V1::RollbackSafeUpgrade](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RollbackSafeUpgrade)) — Optional. The desired rollback safe upgrade configuration. 



### #desired_rollback_safe_upgrade=
    
    
    def desired_rollback_safe_upgrade=(value) -> ::Google::Cloud::Container::V1::RollbackSafeUpgrade

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::RollbackSafeUpgrade](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RollbackSafeUpgrade)) — Optional. The desired rollback safe upgrade configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::RollbackSafeUpgrade](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-RollbackSafeUpgrade)) — Optional. The desired rollback safe upgrade configuration. 



### #desired_secret_manager_config
    
    
    def desired_secret_manager_config() -> ::Google::Cloud::Container::V1::SecretManagerConfig

**Returns**

  * ([::Google::Cloud::Container::V1::SecretManagerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretManagerConfig)) — Enable/Disable Secret Manager Config. 



### #desired_secret_manager_config=
    
    
    def desired_secret_manager_config=(value) -> ::Google::Cloud::Container::V1::SecretManagerConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::SecretManagerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretManagerConfig)) — Enable/Disable Secret Manager Config. 



**Returns**

  * ([::Google::Cloud::Container::V1::SecretManagerConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretManagerConfig)) — Enable/Disable Secret Manager Config. 



### #desired_secret_sync_config
    
    
    def desired_secret_sync_config() -> ::Google::Cloud::Container::V1::SecretSyncConfig

**Returns**

  * ([::Google::Cloud::Container::V1::SecretSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretSyncConfig)) — Configuration for sync Secret Manager secrets as k8s secrets. 



### #desired_secret_sync_config=
    
    
    def desired_secret_sync_config=(value) -> ::Google::Cloud::Container::V1::SecretSyncConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::SecretSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretSyncConfig)) — Configuration for sync Secret Manager secrets as k8s secrets. 



**Returns**

  * ([::Google::Cloud::Container::V1::SecretSyncConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecretSyncConfig)) — Configuration for sync Secret Manager secrets as k8s secrets. 



### #desired_security_posture_config
    
    
    def desired_security_posture_config() -> ::Google::Cloud::Container::V1::SecurityPostureConfig

**Returns**

  * ([::Google::Cloud::Container::V1::SecurityPostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecurityPostureConfig)) — Enable/Disable Security Posture API features for the cluster. 



### #desired_security_posture_config=
    
    
    def desired_security_posture_config=(value) -> ::Google::Cloud::Container::V1::SecurityPostureConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::SecurityPostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecurityPostureConfig)) — Enable/Disable Security Posture API features for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::SecurityPostureConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-SecurityPostureConfig)) — Enable/Disable Security Posture API features for the cluster. 



### #desired_service_external_ips_config
    
    
    def desired_service_external_ips_config() -> ::Google::Cloud::Container::V1::ServiceExternalIPsConfig

**Returns**

  * ([::Google::Cloud::Container::V1::ServiceExternalIPsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ServiceExternalIPsConfig)) — ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field. 



### #desired_service_external_ips_config=
    
    
    def desired_service_external_ips_config=(value) -> ::Google::Cloud::Container::V1::ServiceExternalIPsConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ServiceExternalIPsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ServiceExternalIPsConfig)) — ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field. 



**Returns**

  * ([::Google::Cloud::Container::V1::ServiceExternalIPsConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ServiceExternalIPsConfig)) — ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field. 



### #desired_shielded_nodes
    
    
    def desired_shielded_nodes() -> ::Google::Cloud::Container::V1::ShieldedNodes

**Returns**

  * ([::Google::Cloud::Container::V1::ShieldedNodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ShieldedNodes)) — Configuration for Shielded Nodes. 



### #desired_shielded_nodes=
    
    
    def desired_shielded_nodes=(value) -> ::Google::Cloud::Container::V1::ShieldedNodes

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::ShieldedNodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ShieldedNodes)) — Configuration for Shielded Nodes. 



**Returns**

  * ([::Google::Cloud::Container::V1::ShieldedNodes](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ShieldedNodes)) — Configuration for Shielded Nodes. 



### #desired_stack_type
    
    
    def desired_stack_type() -> ::Google::Cloud::Container::V1::StackType

**Returns**

  * ([::Google::Cloud::Container::V1::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-StackType)) — The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type. 



### #desired_stack_type=
    
    
    def desired_stack_type=(value) -> ::Google::Cloud::Container::V1::StackType

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-StackType)) — The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type. 



**Returns**

  * ([::Google::Cloud::Container::V1::StackType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-StackType)) — The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type. 



### #desired_user_managed_keys_config
    
    
    def desired_user_managed_keys_config() -> ::Google::Cloud::Container::V1::UserManagedKeysConfig

**Returns**

  * ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The desired user managed keys config for the cluster. 



### #desired_user_managed_keys_config=
    
    
    def desired_user_managed_keys_config=(value) -> ::Google::Cloud::Container::V1::UserManagedKeysConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The desired user managed keys config for the cluster. 



**Returns**

  * ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The desired user managed keys config for the cluster. 



### #desired_vertical_pod_autoscaling
    
    
    def desired_vertical_pod_autoscaling() -> ::Google::Cloud::Container::V1::VerticalPodAutoscaling

**Returns**

  * ([::Google::Cloud::Container::V1::VerticalPodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-VerticalPodAutoscaling)) — Cluster-level Vertical Pod Autoscaling configuration. 



### #desired_vertical_pod_autoscaling=
    
    
    def desired_vertical_pod_autoscaling=(value) -> ::Google::Cloud::Container::V1::VerticalPodAutoscaling

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::VerticalPodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-VerticalPodAutoscaling)) — Cluster-level Vertical Pod Autoscaling configuration. 



**Returns**

  * ([::Google::Cloud::Container::V1::VerticalPodAutoscaling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-VerticalPodAutoscaling)) — Cluster-level Vertical Pod Autoscaling configuration. 



### #desired_workload_identity_config
    
    
    def desired_workload_identity_config() -> ::Google::Cloud::Container::V1::WorkloadIdentityConfig

**Returns**

  * ([::Google::Cloud::Container::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadIdentityConfig)) — Configuration for Workload Identity. 



### #desired_workload_identity_config=
    
    
    def desired_workload_identity_config=(value) -> ::Google::Cloud::Container::V1::WorkloadIdentityConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadIdentityConfig)) — Configuration for Workload Identity. 



**Returns**

  * ([::Google::Cloud::Container::V1::WorkloadIdentityConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-WorkloadIdentityConfig)) — Configuration for Workload Identity. 



### #enable_k8s_beta_apis
    
    
    def enable_k8s_beta_apis() -> ::Google::Cloud::Container::V1::K8sBetaAPIConfig

**Returns**

  * ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Kubernetes open source beta apis enabled on the cluster. Only beta apis 



### #enable_k8s_beta_apis=
    
    
    def enable_k8s_beta_apis=(value) -> ::Google::Cloud::Container::V1::K8sBetaAPIConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Kubernetes open source beta apis enabled on the cluster. Only beta apis 



**Returns**

  * ([::Google::Cloud::Container::V1::K8sBetaAPIConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-K8sBetaAPIConfig)) — Kubernetes open source beta apis enabled on the cluster. Only beta apis 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned. 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned. 



**Returns**

  * (::String) — The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned. 



### #gke_auto_upgrade_config
    
    
    def gke_auto_upgrade_config() -> ::Google::Cloud::Container::V1::GkeAutoUpgradeConfig

**Returns**

  * ([::Google::Cloud::Container::V1::GkeAutoUpgradeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GkeAutoUpgradeConfig)) — Configuration for GKE auto upgrade. 



### #gke_auto_upgrade_config=
    
    
    def gke_auto_upgrade_config=(value) -> ::Google::Cloud::Container::V1::GkeAutoUpgradeConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::GkeAutoUpgradeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GkeAutoUpgradeConfig)) — Configuration for GKE auto upgrade. 



**Returns**

  * ([::Google::Cloud::Container::V1::GkeAutoUpgradeConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-GkeAutoUpgradeConfig)) — Configuration for GKE auto upgrade. 



### #removed_additional_pod_ranges_config
    
    
    def removed_additional_pod_ranges_config() -> ::Google::Cloud::Container::V1::AdditionalPodRangesConfig

**Returns**

  * ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument. 



### #removed_additional_pod_ranges_config=
    
    
    def removed_additional_pod_ranges_config=(value) -> ::Google::Cloud::Container::V1::AdditionalPodRangesConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument. 



**Returns**

  * ([::Google::Cloud::Container::V1::AdditionalPodRangesConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-AdditionalPodRangesConfig)) — The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument. 



### #user_managed_keys_config
    
    
    def user_managed_keys_config() -> ::Google::Cloud::Container::V1::UserManagedKeysConfig

**Returns**

  * ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The Custom keys configuration for the cluster.

This field is deprecated. Use [ClusterUpdate.desired_user_managed_keys_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_user_managed_keys_config_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_user_managed_keys_config \(method\)") instead. 




### #user_managed_keys_config=
    
    
    def user_managed_keys_config=(value) -> ::Google::Cloud::Container::V1::UserManagedKeysConfig

**Parameter**

  * **value** ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The Custom keys configuration for the cluster.

This field is deprecated. Use [ClusterUpdate.desired_user_managed_keys_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_user_managed_keys_config_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_user_managed_keys_config \(method\)") instead. 




**Returns**

  * ([::Google::Cloud::Container::V1::UserManagedKeysConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-UserManagedKeysConfig)) — The Custom keys configuration for the cluster.

This field is deprecated. Use [ClusterUpdate.desired_user_managed_keys_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-container-v1/latest/Google-Cloud-Container-V1-ClusterUpdate#Google__Cloud__Container__V1__ClusterUpdate_desired_user_managed_keys_config_instance_ "Google::Cloud::Container::V1::ClusterUpdate#desired_user_managed_keys_config \(method\)") instead. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
