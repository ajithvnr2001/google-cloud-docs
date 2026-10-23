---
url: https://docs.cloud.google.com/application-design-center/docs/configure-gke-node-pool/
title: Configure a GKE node pool \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:10.108187+00:00
---

# Configure a GKE node pool  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-gke-node-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a GKE node pool Stay organized with collections  Save and categorize content based on your preferences. 

A [GKE node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) is a group of nodes within a cluster that all have the same configuration. When you create a Standard mode cluster, the number of nodes and type of nodes that you specify are used to create the first node pool of the cluster.

This document describes the connections and parameters you can configure when using App Design Center to create a GKE node pool. The configuration parameters are based on the [GKE node pool Terraform module](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/tree/main/modules/gke-node-pool).

## Component connections

The following table includes the components that you can connect to a GKE node pool, and the resulting updates to your application and its generated Terraform code.

Component | Description | Background information  
---|---|---  
[GKE Standard cluster](https://docs.cloud.google.com/application-design-center/docs/configure-gke-standard-cluster) | Adds a node pool to the cluster configuration. | [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle)  
  
## Required configuration parameters

If your template includes a GKE node pool, you must configure the following parameters before you deploy.

Parameter name | Description and constraint information | Background information  
---|---|---  
**Cluster** | The name of the cluster in the format `projects/{project_id}/locations/{location}/clusters/{cluster}` or as the name of the cluster. | [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview)  
**Project Id** | The project where you want to create the GKE node pool. | [Configure default values for components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_default_values_for_components)  
**Region** | The location (region or zone) in which the node pool is created. | [Cluster availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#availability)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Name** | The name of the node pool. | [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview)  
Autoscaling | **Min Node Count** | [minNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling.FIELDS.min_node_count) | [About GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler)  
**Max Node Count** | [maxNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling.FIELDS.max_node_count)  
**Total Min Node Count** | [totalMinNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling.FIELDS.total_min_node_count)  
**Total Max Node Count** | [totalMaxNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling.FIELDS.total_max_node_count)  
**Location Policy** | [locationPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodePoolAutoscaling.FIELDS.location_policy)  
| **Initial Node Count** | [initialNodeCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.initial_node_count) | [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools)  
Management | **Auto Repair** | [autoRepair](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeManagement#FIELDS.auto_repair) | [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)  
**Auto Upgrade** | [autoUpgrade](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeManagement#FIELDS.auto_upgrade) | [Auto-upgrading nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades)  
| **Max Pods Per Node** | [maxPodsConstraint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.max_pods_constraint) | [Configure maximum Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr)  
| **Node Locations** | [locations](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) | [Location and distribution of the nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#nodes-location)  
| **Name Prefix** | [name_prefix](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool#name_prefix-1)  
Node Config | **Confidential nodes** | [ConfidentialNodes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ConfidentialNodes) | [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)  
**Disk Size Gb** | [diskSizeGb](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.disk_size_gb) | [About GKE node sizing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes)  
**Disk Type** | [diskType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.disk_type) | [Local ephemeral storage reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation)  
**Enable Confidential Storage** | [enableConfidentialStorage](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.enable_confidential_storage) | [Encrypt workload data in-use with Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)  
**Local SSD Encryption Mode** | [LocalSsdEncryptionMode](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#localssdencryptionmode) | [About Local SSD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd)  
**Ephemeral Storage Local Ssd Config** | [EphemeralStorageLocalSsdConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#ephemeralstoragelocalssdconfig) | [About Local SSD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd)  
**Fast Socket** | [FastSocket](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#fastsocket) | [Improve workload efficiency using NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket)  
**Local Nvme Ssd Block Config** | [LocalNvmeSsdBlockConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#localnvmessdblockconfig) | [About Local SSD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd)  
**Logging Variant** | [variant](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodePoolLoggingConfig#LoggingVariantConfig.FIELDS.variant) | [Adjust log throughput](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/adjust-log-throughput)  
**Secondary Boot Disks** | [secondaryBootDisks](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#secondarybootdisk) | [Use secondary boot disks to preload data or container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading)  
**Gcfs Config** | [GcfsConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.gcfs_config) | [Use image streaming to pull container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)  
**Gvnic** | [virtualNic](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#virtualnic) | [About multi-networking support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods)  
**Guest Accelerator** | [acceleratorConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#acceleratorconfig) | [Run GPUs in GKE Standard node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus)  
**Image Type** | [imageType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.image_type) | [Node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images)  
**Labels** | [labels](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.labels) | [Create and manage cluster and node pool labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels)  
**Resource Labels** | [resourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.resource_labels) | [Create and manage cluster and node pool labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels)  
**Max Run Duration** | [maxRunDuration](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.max_run_duration) | [Limit the run time of auto-created nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#limit-run-time)  
**Flex Start** | [flexStart](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.flex_start) | [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest)  
**Local SSD Count** | [localSsdCount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.local_ssd_count) | [About Local SSD for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd)  
**Machine Type** | [machineType](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.machine_type) | [Choose a machine type for a node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--machine-type)  
**Metadata** | [metadata](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.metadata) | [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview)  
**Min Cpu Platform** | [minCpuPlatform](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.min_cpu_platform) | [Choose a minimum CPU platform](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/min-cpu-platform)  
**Oauth Scopes** | [oauthScopes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.oauth_scopes) | [Access scopes in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/access-scopes)  
**Preemptible** | [preemptible](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.preemptible) | [Using preemptible VMs to run fault-tolerant workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms)  
**Reservation Affinity** | [reservationAffinity](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#reservationaffinity) | [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations)  
**Spot** | [spot](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.spot) | [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)  
**Sandbox Config** | [sandboxConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#sandboxconfig) | [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods)  
**Boot Disk Kms Key** | [boot_disk_kms_key](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.boot_disk_kms_key) | [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)  
**Service Account** | [serviceAccount](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.service_account) | [About service accounts in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/service-accounts)  
**Shielded Instance Config** | [ShieldedInstanceConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ShieldedInstanceConfig) | [Using Shielded GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)  
**Storage Pools** | [storage_pools](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.storage_pools) | [Storage for GKE clusters overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview)  
**Tags** | [tags](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.tags) | [Manage GKE resources using Tags](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags)  
**Resource Manager Tags** | [resourceManagerTags](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.resource_manager_tags) | [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview)  
**Taint** | [NodeTaint](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#nodetaint) | [Configure workload separation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation)  
**Workload Metadata Config** | [workloadMetadataConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#workloadmetadataconfig) | [Authenticate to Google Cloud APIs from GKE workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)  
**Kubelet Config** | [NodeKubeletConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeKubeletConfig) | [Customizing node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config)  
**Linux Node Config** | [LinuxNodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/LinuxNodeConfig) | [LinuxNodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/LinuxNodeConfig)  
**Windows Node Config** | [windowsNodeConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#windowsnodeconfig) | [Creating a cluster with Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows)  
**Containerd Config** | [ContainerdConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/ContainerdConfig) | [Containerd node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/using-containerd)  
**Node Group** | [node_group](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#FIELDS.node_group) | [Isolate your GKE workloads using sole-tenant nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sole-tenancy)  
**Sole Tenant Config** | [soleTenantConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/NodeConfig#soletenantconfig) | [Isolate your GKE workloads using sole-tenant nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sole-tenancy)  
Network Config | **Create Pod Range** | [createPodRange](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig.FIELDS.create_pod_range) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
**Enable Private Nodes** | [enablePrivateNodes](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig.FIELDS.enable_private_nodes) | [Customize your network isolation in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)  
**Pod Ipv4 Cidr Block** | [podIpv4CidrBlock](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig.FIELDS.pod_ipv4_cidr_block) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
**Pod Range** | [podRange](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig.FIELDS.pod_range) | [Adding Pod IPv4 address ranges](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr)  
**Additional Node Network Configs** | [AdditionalNodeNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#additionalnodenetworkconfig) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
**Additional Pod Network Configs** | [AdditionalPodNetworkConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#additionalpodnetworkconfig) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
**Pod Cidr Overprovision Config** | [podCidrOverprovisionConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.NodeNetworkConfig.FIELDS.pod_cidr_overprovision_config) | [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)  
**Network Performance Config** | [NetworkPerformanceConfig](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#networkperformanceconfig) | [Increase network bandwidth for clusters and nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-tier-1)  
| **Node Count** | [node_count](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_node_pool#node_count-1) | [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools)  
Upgrade Settings | **Max Surge** | [maxSurge](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings#FIELDS.max_surge) | [Configure node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies)  
**Max Unavailable** | [maxUnavailable](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings#FIELDS.max_unavailable)  
**Strategy** | [strategy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings#FIELDS.strategy)  
**Blue Green Settings** | [BlueGreenSettings](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/UpgradeSettings#bluegreensettings)  
| **Kubernetes Version** | [version](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.version) | [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning)  
Placement Policy | **Type** | [type](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy.FIELDS.type) | [Define compact placement for GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement)  
**Policy Name** | [PlacementPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy.FIELDS.policy_name) | [Define compact placement for GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement)  
**Tpu Topology** | [tpuTopology](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.PlacementPolicy.FIELDS.tpu_topology) | [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)  
Queued Provisioning | **Enabled** | [QueuedProvisioning](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#queuedprovisioning) | [Run a large-scale workload with flex-start with queued provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest)  
Timeouts |  | [Timeouts](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#timeouts) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
