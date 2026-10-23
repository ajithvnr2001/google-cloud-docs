---
url: https://docs.cloud.google.com/application-design-center/docs/configure-gke-autopilot-cluster/
title: Configure a GKE Autopilot cluster \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:59.083699+00:00
---

# Configure a GKE Autopilot cluster  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-gke-autopilot-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a GKE Autopilot cluster Stay organized with collections  Save and categorize content based on your preferences. 

A [GKE Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) lets Google manage your infrastructure configuration, including your nodes, scaling, security, and other preconfigured settings. Autopilot is optimized to run most production workloads and provisions compute resources based on your Kubernetes manifests.

This document describes the connections and parameters you can configure when using App Design Center to create a GKE Autopilot cluster. The configuration parameters are based on the [GKE Autopilot cluster Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/tree/main/modules/gke-autopilot-cluster).

## Required configuration parameters

If your template includes a GKE Autopilot cluster, you must configure the following parameters before you deploy.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Name** | The name of the cluster. | [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview)  
| **Project Id** | The project where you want to create the GKE Autopilot cluster. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
| **Region** or **Zone** | The location (region or zone) in which the cluster is created. | [Cluster availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#availability)  
| **Network** | [network](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.network) | [Explore GKE networking documentation and use cases](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)  
| **Subnetwork** | [subnetwork](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.subnetwork) | [Explore GKE networking documentation and use cases](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)  
Master Authorized Networks Config | **CIDR Block Display name** | [displayName](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.CidrBlock.FIELDS.display_name) | [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)  
Master Authorized Networks Config | **CIDR Block** | [cidrBlock](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.CidrBlock.FIELDS.cidr_block) | [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)  
Workload Identity Config | **Workload Pool** | [workloadPool](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.WorkloadIdentityConfig.FIELDS.workload_pool) | [Use Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Description** | [description](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.description) |   
| **Node Locations** | [locations](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) | [Location and distribution of the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#nodes-location)  
| **Deletion Protection** | Whether Terraform is prevented from destroying the cluster. Deleting this cluster using terraform destroy or terraform apply will only succeed if this field is false in the Terraform state. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#deletion_protection-1)  
Master Authorized Networks Config | **Gcp Public Cidrs Access Enabled** | [gcpPublicCidrsAccessEnabled](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.MasterAuthorizedNetworksConfig.FIELDS.gcp_public_cidrs_access_enabled) | [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)  
Master Authorized Networks Config | **Private Endpoint Enforcement Enabled** | [privateEndpointEnforcementEnabled](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.MasterAuthorizedNetworksConfig.FIELDS.private_endpoint_enforcement_enabled) | [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)  
Addons Config | **GCP Filestore CSI Driver Config** | [GcpFilestoreCsiDriverConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#gcpfilestorecsidriverconfig) | [Access Filestore instances with the Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)  
**GKE Backup Agent Config** | [GkeBackupAgentConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#gkebackupagentconfig) | [backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)  
**Ray Operator Config** | [RayOperatorConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#rayoperatorconfig) | [About Ray on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview)  
**Ray Cluster Logging Config** | [RayClusterLoggingConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#rayclusterloggingconfig) | [Collect and view logs and metrics for Ray clusters on Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/collect-view-logs-metrics)  
**Ray Cluster Monitoring Config** | [RayClusterMonitoringConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#rayclustermonitoringconfig)  
| **Cluster Ipv4 Cidr** | [clusterIpv4Cidr](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.cluster_ipv4_cidr) | [Create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips)  
Cluster Autoscaling | **Auto Provisioning Defaults** | [AutoprovisioningNodePoolDefaults](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#autoprovisioningnodepooldefaults) | [About node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-auto-provisioning)  
Binary Authorization | **Evaluation mode** | [BinaryAuthorization](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#binaryauthorization) | [Use Binary Authorization](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#using-binary-authorization)  
Service External IPs Config | **Enabled** | [ServiceExternalIpsConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#serviceexternalipsconfig) | [Exposing applications using services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps)  
Mesh Certificates | **Enable Certificates** | [meshCertificates](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#meshcertificates) | [](https://docs.cloud.google.com/application-design-center/docs/configure-gke-autopilot-cluster/)  
Database Encryption | ****| [DatabaseEncryption](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#databaseencryption) | [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)  
Enable K8s Beta Apis | **Enabled APIs** | [K8sBetaApisConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#k8sbetaapiconfig) | [Use Kubernetes beta APIs with GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis)  
Ip Allocation Policy | ****| [IpAllocationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#ipallocationpolicy) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
Logging Config | **Enable Components** | [enableComponents](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.LoggingComponentConfig.FIELDS.enable_components) | [About GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs)  
Maintenance Policy | ****| [MaintenancePolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#maintenancepolicy) | [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions)  
Master Auth | ****| [clientCertificateConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.MasterAuth.FIELDS.client_certificate_config) | [Authenticate to the Kubernetes API server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication)  
| **Min Master Version** | [min_master_version](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#min_master_version-1) | [Versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning)  
Monitoring Config | **Enable Components** | [enableComponents](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#monitoringcomponentconfig) | [Configure metrics collection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics)  
Node Pool Auto Config | **Insecure Kubelet Readonly Port Enabled** | [insecureKubeletReadonlyPortEnabled](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeKubeletConfig#FIELDS.insecure_kubelet_readonly_port_enabled) | [Disable the kubelet read-only port in GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port)  
**Resource Manager Tags** | [resourceManagerTags](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.resource_manager_tags) | [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)  
**Network Tags** | [tags](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.tags) | [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)  
**Linux Node Config** | [LinuxNodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/LinuxNodeConfig) | [Linux cgroup mode configuration options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#cgroup-mode-options)  
Notification Config | **Pubsub enabled** | [PubSub](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.PubSub.FIELDS.enabled) | [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications)  
**Topic** | [topic](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.PubSub.FIELDS.topic)  
**Filter Event Type** | [filter](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.PubSub.FIELDS.filter)  
Confidential Nodes | **Enabled** | [ConfidentialNodes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ConfidentialNodes) | [Encrypt workload data in-use with Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)  
Pod Security Policy Config | **Enabled** | [podSecurityPolicyConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#podsecuritypolicyconfig) | [PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-security-policies)  
Pod Autoscaling | **HPA Profile** | [PodAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#podautoscaling) | [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)  
Vertical Pod Autoscaling | **Enabled** | [VerticalPodAutoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#verticalpodautoscaling) | [Vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)  
Secret Manager Config | **Enabled** | [SecretManagerConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#secretmanagerconfig) | [Protect your data with secret management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#secret_management)  
Authenticator Groups Config | **Security Group** | [AuthenticatorGroupsConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#authenticatorgroupsconfig) | [Configure Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/google-groups-rbac)  
Control Plane Endpoints Config | **DNS Endpoint Config** | [](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#controlplaneendpointsconfig) | [About network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation)  
Private Cluster Config | ****| [PrivateClusterConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.PrivateClusterConfig) | [Creating a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/legacy/network-isolation)  
Cluster Telemetry | **Type** | [clusterTelemetry](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#clustertelemetry) |   
Release Channel | ****| [ReleaseChannel](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#releasechannel) | [About release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels)  
| **Resource Labels** | [resourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.resource_labels) | [Create and manage cluster and node pool labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels)  
Cost Management Config | **Enabled** | [CostManagementConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#costmanagementconfig) | [Get key spending insights for your GKE resource allocation and cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations)  
Resource Usage Export Config | **Enabled** | [ResourceUsageExportConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#resourceusageexportconfig) | [Understanding cluster resource usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering)  
Identity Service Config | **Enabled** | [IdentityServiceConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#identityserviceconfig) | [Use external identity providers to authenticate to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/oidc)  
| **Enable L4 Ilb Subsetting** | [enableL4ilbSubsetting](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.NetworkConfig.FIELDS.enable_l4ilb_subsetting) | [Create an internal load balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)  
| **Disable L4 Lb Firewall Reconciliation** | [disableL4LbFirewallReconciliation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.NetworkConfig.FIELDS.disable_l4_lb_firewall_reconciliation) | [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules)  
| **Enable Multi Networking** | [enableMultiNetworking](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.NetworkConfig.FIELDS.enable_multi_networking) | [About multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods)  
| **In Transit Encryption Config** | [InTransitEncryptionConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#intransitencryptionconfig) | [About FIPS-validated encryption in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-fips-compliance)  
| **Enable Fqdn Network Policy** | [enableFqdnNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.NetworkConfig.FIELDS.enable_fqdn_network_policy) | [Control Pod egress traffic using FQDN network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/fqdn-network-policies)  
| **Enable Cilium Clusterwide Network Policy** | [enableCiliumClusterwideNetworkPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.NetworkConfig.FIELDS.enable_cilium_clusterwide_network_policy) | [Control cluster-wide communication using network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cilium-network-policy)  
| **Private Ipv6 Google Access** | [PrivateIpv6GoogleAccess](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#privateipv6googleaccess) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
| **Datapath Provider** | [DatapathProvider](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#datapathprovider) | [Using GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2)  
Default Snat Status | ****| [defaultSnatStatus](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#defaultsnatstatus) | [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent)  
Dns Config | ****| [DNSConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#dnsconfig) | [Using Cloud DNS for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns)  
Gateway Api Config | ****| [GatewayAPIConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#gatewayapiconfig) | [About Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)  
Protect Config | ****| [ProtectConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#protectconfig) |   
security posture Config | ****| [SecurityPostureConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#securitypostureconfig) | [About the security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)  
Fleet | **Project** | [Fleet](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#fleet) | [Fleet management](https://docs.cloud.google.com/kubernetes-engine/docs/fleets-overview)  
Workload Alts Config | **Enable Alts** | [WorkloadALTSConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1beta1/projects.locations.clusters#workloadaltsconfig)  
Enterprise Config | **Desired Tier** | [EnterpriseConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#enterpriseconfig) |   
| **Allow Net Admin** | [allowNetAdmin](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.WorkloadPolicyConfig.FIELDS.allow_net_admin) | [GKE Autopilot security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security)  
| **Timeouts** | [Timeouts](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#timeouts)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
