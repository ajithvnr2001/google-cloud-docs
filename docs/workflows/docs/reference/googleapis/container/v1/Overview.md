---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview/
title: Types overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:43.123175+00:00
---

# Types overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Types overview Stay organized with collections  Save and categorize content based on your preferences. 

## AcceleratorConfig

AcceleratorConfig represents a Hardware Accelerator request. Fields  
---  
`acceleratorCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of the accelerator cards exposed to an instance.  
`acceleratorType` |  `string` The accelerator type resource name. List of supported accelerators [here](https://cloud.google.com/compute/docs/gpus)  
`gpuPartitionSize` |  `string` Size of partitions to create on the GPU. Valid values are described in the NVIDIA [mig user guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning).  
  
## AddonsConfig

Configuration for the addons that can be automatically spun up in the cluster, enabling additional functionality. Fields  
---  
`cloudRunConfig` |  `object ([CloudRunConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#CloudRunConfig))` Configuration for the Cloud Run addon, which allows the user to use a managed Knative service.  
`configConnectorConfig` |  `object ([ConfigConnectorConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ConfigConnectorConfig))` Configuration for the ConfigConnector add-on, a Kubernetes extension to manage hosted GCP services through the Kubernetes API  
`dnsCacheConfig` |  `object ([DnsCacheConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DnsCacheConfig))` Configuration for NodeLocalDNS, a dns cache running on cluster nodes  
`gcePersistentDiskCsiDriverConfig` |  `object ([GcePersistentDiskCsiDriverConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#GcePersistentDiskCsiDriverConfig))` Configuration for the Compute Engine Persistent Disk CSI driver.  
`gcpFilestoreCsiDriverConfig` |  `object ([GcpFilestoreCsiDriverConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#GcpFilestoreCsiDriverConfig))` Configuration for the GCP Filestore CSI driver.  
`horizontalPodAutoscaling` |  `object ([HorizontalPodAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#HorizontalPodAutoscaling))` Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.  
`httpLoadBalancing` |  `object ([HttpLoadBalancing](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#HttpLoadBalancing))` Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.  
`kubernetesDashboard` |  `object ([KubernetesDashboard](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#KubernetesDashboard))` Configuration for the Kubernetes Dashboard. This addon is deprecated, and will be disabled in 1.15. It is recommended to use the Cloud Console to manage and monitor your Kubernetes clusters, workloads and applications. For more information, see: https://cloud.google.com/kubernetes-engine/docs/concepts/dashboards  
`networkPolicyConfig` |  `object ([NetworkPolicyConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NetworkPolicyConfig))` Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes.  
  
## AuthenticatorGroupsConfig

Configuration for returning group information from authenticators. Fields  
---  
`enabled` |  `boolean` Whether this cluster should return group membership lookups during authentication using a group of security groups.  
`securityGroup` |  `string` The name of the security group-of-groups to be used. Only relevant if enabled = true.  
  
## AutoUpgradeOptions

AutoUpgradeOptions defines the set of options for the user to control how the Auto Upgrades will proceed. Fields  
---  
`autoUpgradeStartTime` |  `string` [Output only] This field is set when upgrades are about to commence with the approximate start time for the upgrades, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`description` |  `string` [Output only] This field is set when upgrades are about to commence with the description of the upgrade.  
  
## Autopilot

Autopilot is the configuration for Autopilot settings on the cluster. Fields  
---  
`enabled` |  `boolean` Enable Autopilot  
  
## AutoprovisioningNodePoolDefaults

AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP. Fields  
---  
`bootDiskKmsKey` |  `string` The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption  
`diskSizeGb` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.  
`diskType` |  `string` Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced') If unspecified, the default disk type is 'pd-standard'  
`imageType` |  `string` The image type to use for NAP created node.  
`management` |  `object ([NodeManagement](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeManagement))` Specifies the node management options for NAP created node-pools.  
`minCpuPlatform` |  `string` Minimum CPU platform to be used for NAP created node pools. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as minCpuPlatform: Intel Haswell or minCpuPlatform: Intel Sandy Bridge. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform) To unset the min cpu platform field pass "automatic" as field value.  
`oauthScopes[]` |  `string` Scopes that are used by NAP when creating node pools.  
`serviceAccount` |  `string` The Google Cloud Platform Service Account to be used by the node VMs.  
`shieldedInstanceConfig` |  `object ([ShieldedInstanceConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ShieldedInstanceConfig))` Shielded Instance options.  
`upgradeSettings` |  `object ([UpgradeSettings](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#UpgradeSettings))` Specifies the upgrade settings for NAP created node pools  
  
## BigQueryDestination

Parameters for using BigQuery as the destination of resource usage export. Fields  
---  
`datasetId` |  `string` The ID of a BigQuery Dataset.  
  
## BinaryAuthorization

Configuration for Binary Authorization. Fields  
---  
`enabled` |  `boolean` Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Binary Authorization.  
  
## CancelOperationRequest

CancelOperationRequest cancels a single operation. Fields  
---  
`name` |  `string` The name (project, location, operation id) of the operation to cancel. Specified in the format `projects/*/locations/*/operations/*`.  
`operationId` |  `string` Deprecated. The server-assigned `name` of the operation. This field has been deprecated and replaced by the name field.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation resides. This field has been deprecated and replaced by the name field.  
  
## CidrBlock

CidrBlock contains an optional name and one CIDR block. Fields  
---  
`cidrBlock` |  `string` cidr_block must be specified in CIDR notation.  
`displayName` |  `string` display_name is an optional field for users to identify CIDR blocks.  
  
## ClientCertificateConfig

Configuration for client certificates on the cluster. Fields  
---  
`issueClientCertificate` |  `boolean` Issue a client certificate.  
  
## CloudRunConfig

Configuration options for the Cloud Run feature. Fields  
---  
`disabled` |  `boolean` Whether Cloud Run addon is enabled for this cluster.  
`loadBalancerType` |  `enum` Which load balancer type is installed for Cloud Run.  
Enum type. Can be one of the following:  
`LOAD_BALANCER_TYPE_UNSPECIFIED` | Load balancer type for Cloud Run is unspecified.  
`LOAD_BALANCER_TYPE_EXTERNAL` | Install external load balancer for Cloud Run.  
`LOAD_BALANCER_TYPE_INTERNAL` | Install internal load balancer for Cloud Run.  
  
## Cluster

A Google Kubernetes Engine cluster. Fields  
---  
`addonsConfig` |  `object ([AddonsConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AddonsConfig))` Configurations for the various addons available to run in the cluster.  
`authenticatorGroupsConfig` |  `object ([AuthenticatorGroupsConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AuthenticatorGroupsConfig))` Configuration controlling RBAC group membership information.  
`autopilot` |  `object ([Autopilot](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Autopilot))` Autopilot configuration for the cluster.  
`autoscaling` |  `object ([ClusterAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ClusterAutoscaling))` Cluster-level autoscaling configuration.  
`binaryAuthorization` |  `object ([BinaryAuthorization](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#BinaryAuthorization))` Configuration for Binary Authorization.  
`clusterIpv4Cidr` |  `string` The IP address range of the container pods in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`). Leave blank to have one automatically chosen or specify a `/14` block in `10.0.0.0/8`.  
`conditions[]` |  `object ([StatusCondition](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#StatusCondition))` Which conditions caused the current cluster state.  
`confidentialNodes` |  `object ([ConfidentialNodes](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ConfidentialNodes))` Configuration of Confidential Nodes  
`createTime` |  `string` [Output only] The time the cluster was created, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`currentMasterVersion` |  `string` [Output only] The current software version of the master endpoint.  
`currentNodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` [Output only] The number of nodes currently in the cluster. Deprecated. Call Kubernetes API directly to retrieve node information.  
`currentNodeVersion` |  `string` [Output only] Deprecated, use [NodePools.version](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools) instead. The current version of the node software components. If they are currently at multiple versions because they're in the process of being upgraded, this reflects the minimum version of all nodes.  
`databaseEncryption` |  `object ([DatabaseEncryption](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DatabaseEncryption))` Configuration of etcd encryption.  
`defaultMaxPodsConstraint` |  `object ([MaxPodsConstraint](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MaxPodsConstraint))` The default constraint on the maximum number of pods that can be run simultaneously on a node in the node pool of this cluster. Only honored if cluster created with IP Alias support.  
`description` |  `string` An optional description of this cluster.  
`enableKubernetesAlpha` |  `boolean` Kubernetes alpha features are enabled on this cluster. This includes alpha API groups (e.g. v1alpha1) and features that may not be production ready in the kubernetes version of the master and nodes. The cluster has no SLA for uptime and master/node upgrades are disabled. Alpha enabled clusters are automatically deleted thirty days after creation.  
`enableTpu` |  `boolean` Enable the ability to use Cloud TPUs in this cluster.  
`endpoint` |  `string` [Output only] The IP address of this cluster's master endpoint. The endpoint can be accessed from the internet at `https://username:password@endpoint/`. See the `masterAuth` property of this resource for username and password information.  
`expireTime` |  `string` [Output only] The time the cluster will be automatically deleted in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`id` |  `string` Output only. Unique id for the cluster.  
`initialClusterVersion` |  `string` The initial Kubernetes version for this cluster. Valid versions are those found in validMasterVersions returned by getServerConfig. The version can be upgraded over time; such upgrades are reflected in currentMasterVersion and currentNodeVersion. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "","-": picks the default Kubernetes version  
`initialNodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of nodes to create in this cluster. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "node_config") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. This field is deprecated, use node_pool.initial_node_count instead.  
`instanceGroupUrls[]` |  `string` Deprecated. Use node_pools.instance_group_urls.  
`ipAllocationPolicy` |  `object ([IPAllocationPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#IPAllocationPolicy))` Configuration for cluster IP allocation.  
`labelFingerprint` |  `string` The fingerprint of the set of labels for this cluster.  
`legacyAbac` |  `object ([LegacyAbac](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LegacyAbac))` Configuration for the legacy ABAC authorization mode.  
`location` |  `string` [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides.  
`locations[]` |  `string` The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. This field provides a default value if [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) are not specified during node pool creation. Warning: changing cluster locations will update the [NodePool.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters.nodePools#NodePool.FIELDS.locations) of all node pools and will result in nodes being added and/or removed.  
`loggingConfig` |  `object ([LoggingConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LoggingConfig))` Logging configuration for the cluster.  
`loggingService` |  `string` The logging service the cluster should use to write logs. Currently available options: * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15). * `none` \- no logs will be exported from the cluster. If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.  
`maintenancePolicy` |  `object ([MaintenancePolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MaintenancePolicy))` Configure the maintenance policy for this cluster.  
`masterAuth` |  `object ([MasterAuth](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MasterAuth))` The authentication information for accessing the master endpoint. If unspecified, the defaults are used: For clusters before v1.12, if master_auth is unspecified, `username` will be set to "admin", a random password will be generated, and a client certificate will be issued.  
`masterAuthorizedNetworksConfig` |  `object ([MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MasterAuthorizedNetworksConfig))` The configuration options for master authorized networks feature.  
`monitoringConfig` |  `object ([MonitoringConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MonitoringConfig))` Monitoring configuration for the cluster.  
`monitoringService` |  `string` The monitoring service the cluster should use to write metrics. Currently available options: * "monitoring.googleapis.com/kubernetes" - The Cloud Monitoring service with a Kubernetes-native resource model * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * `none` \- No metrics will be exported from the cluster. If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.  
`name` |  `string` The name of this cluster. The name must be unique within this project and location (e.g. zone or region), and can be up to 40 characters with the following restrictions: * Lowercase letters, numbers, and hyphens only. * Must start with a letter. * Must end with a number or a letter.  
`network` |  `string` The name of the Google Compute Engine [network](https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. If left unspecified, the `default` network will be used.  
`networkConfig` |  `object ([NetworkConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NetworkConfig))` Configuration for cluster networking.  
`networkPolicy` |  `object ([NetworkPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NetworkPolicy))` Configuration options for the NetworkPolicy feature.  
`nodeConfig` |  `object ([NodeConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeConfig))` Parameters used in creating the cluster's nodes. For requests, this field should only be used in lieu of a "node_pool" object, since this configuration (along with the "initial_node_count") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a node_pool at the same time. For responses, this field will be populated with the node configuration of the first node pool. (For configuration of each node pool, see `node_pool.config`) If unspecified, the defaults are used. This field is deprecated, use node_pool.config instead.  
`nodeIpv4CidrSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` [Output only] The size of the address space on each node for hosting containers. This is provisioned from within the `container_ipv4_cidr` range. This field will only be set when cluster is in route-based network mode.  
`nodePools[]` |  `object ([NodePool](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePool))` The node pools associated with this cluster. This field should not be set if "node_config" or "initial_node_count" are specified.  
`notificationConfig` |  `object ([NotificationConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NotificationConfig))` Notification configuration of the cluster.  
`privateClusterConfig` |  `object ([PrivateClusterConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#PrivateClusterConfig))` Configuration for private cluster.  
`releaseChannel` |  `object ([ReleaseChannel](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ReleaseChannel))` Release channel configuration.  
`resourceLabels` |  `map (key: string, value: string)` The resource labels for the cluster to use to annotate any related Google Compute Engine resources.  
`resourceUsageExportConfig` |  `object ([ResourceUsageExportConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ResourceUsageExportConfig))` Configuration for exporting resource usages. Resource usage export is disabled when this config is unspecified.  
`selfLink` |  `string` [Output only] Server-defined URL for the resource.  
`servicesIpv4Cidr` |  `string` [Output only] The IP address range of the Kubernetes services in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`). Service addresses are typically put in the last `/16` from the container CIDR.  
`shieldedNodes` |  `object ([ShieldedNodes](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ShieldedNodes))` Shielded Nodes configuration.  
`status` |  `enum` [Output only] The current status of this cluster.  
Enum type. Can be one of the following:  
`STATUS_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the cluster is being created.  
`RUNNING` | The RUNNING state indicates the cluster has been created and is fully usable.  
`RECONCILING` | The RECONCILING state indicates that some work is actively being done on the cluster, such as upgrading the master or node software. Details can be found in the `statusMessage` field.  
`STOPPING` | The STOPPING state indicates the cluster is being deleted.  
`ERROR` | The ERROR state indicates the cluster is unusable. It will be automatically deleted. Details can be found in the `statusMessage` field.  
`DEGRADED` | The DEGRADED state indicates the cluster requires user action to restore full functionality. Details can be found in the `statusMessage` field.  
`statusMessage` |  `string` [Output only] Deprecated. Use conditions instead. Additional information about the current status of this cluster, if available.  
`subnetwork` |  `string` The name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/subnetworks) to which the cluster is connected.  
`tpuIpv4CidrBlock` |  `string` [Output only] The IP address range of the Cloud TPUs in this cluster, in [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `1.2.3.4/29`).  
`verticalPodAutoscaling` |  `object ([VerticalPodAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#VerticalPodAutoscaling))` Cluster-level Vertical Pod Autoscaling configuration.  
`workloadIdentityConfig` |  `object ([WorkloadIdentityConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#WorkloadIdentityConfig))` Configuration for the use of Kubernetes Service Accounts in GCP IAM policies.  
`zone` |  `string` [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field is deprecated, use location instead.  
  
## ClusterAutoscaling

ClusterAutoscaling contains global, per-cluster information required by Cluster Autoscaler to automatically adjust the size of the cluster and create/delete node pools based on the current needs. Fields  
---  
`autoprovisioningLocations[]` |  `string` The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes can be created by NAP.  
`autoprovisioningNodePoolDefaults` |  `object ([AutoprovisioningNodePoolDefaults](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AutoprovisioningNodePoolDefaults))` AutoprovisioningNodePoolDefaults contains defaults for a node pool created by NAP.  
`autoscalingProfile` |  `enum` Defines autoscaling behaviour.  
Enum type. Can be one of the following:  
`PROFILE_UNSPECIFIED` | No change to autoscaling configuration.  
`OPTIMIZE_UTILIZATION` | Prioritize optimizing utilization of resources.  
`BALANCED` | Use default (balanced) autoscaling configuration.  
`enableNodeAutoprovisioning` |  `boolean` Enables automatic node pool creation and deletion.  
`resourceLimits[]` |  `object ([ResourceLimit](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ResourceLimit))` Contains global constraints regarding minimum and maximum amount of resources in the cluster.  
  
## ClusterUpdate

ClusterUpdate describes an update to the cluster. Exactly one update can be applied to a cluster with each request, so at most one field can be provided. Fields  
---  
`desiredAddonsConfig` |  `object ([AddonsConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AddonsConfig))` Configurations for the various addons available to run in the cluster.  
`desiredAuthenticatorGroupsConfig` |  `object ([AuthenticatorGroupsConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AuthenticatorGroupsConfig))` The desired authenticator groups config for the cluster.  
`desiredAutopilot` |  `object ([Autopilot](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Autopilot))` The desired Autopilot configuration for the cluster.  
`desiredBinaryAuthorization` |  `object ([BinaryAuthorization](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#BinaryAuthorization))` The desired configuration options for the Binary Authorization feature.  
`desiredClusterAutoscaling` |  `object ([ClusterAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ClusterAutoscaling))` Cluster-level autoscaling configuration.  
`desiredDatabaseEncryption` |  `object ([DatabaseEncryption](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DatabaseEncryption))` Configuration of etcd encryption.  
`desiredDatapathProvider` |  `enum` The desired datapath provider for the cluster.  
Enum type. Can be one of the following:  
`DATAPATH_PROVIDER_UNSPECIFIED` | Default value.  
`LEGACY_DATAPATH` | Use the IPTables implementation based on kube-proxy.  
`ADVANCED_DATAPATH` | Use the eBPF based GKE Dataplane V2 with additional features. See the [GKE Dataplane V2 documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for more.  
`desiredDefaultSnatStatus` |  `object ([DefaultSnatStatus](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DefaultSnatStatus))` The desired status of whether to disable default sNAT for this cluster.  
`desiredImageType` |  `string` The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.  
`desiredIntraNodeVisibilityConfig` |  `object ([IntraNodeVisibilityConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#IntraNodeVisibilityConfig))` The desired config of Intra-node visibility.  
`desiredL4ilbSubsettingConfig` |  `object ([ILBSubsettingConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ILBSubsettingConfig))` The desired L4 Internal Load Balancer Subsetting configuration.  
`desiredLocations[]` |  `string` The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. This list must always include the cluster's primary zone. Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.  
`desiredLoggingConfig` |  `object ([LoggingConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LoggingConfig))` The desired logging configuration.  
`desiredLoggingService` |  `string` The logging service the cluster should use to write logs. Currently available options: * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15). * `none` \- no logs will be exported from the cluster. If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.  
`desiredMasterAuthorizedNetworksConfig` |  `object ([MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MasterAuthorizedNetworksConfig))` The desired configuration options for master authorized networks feature.  
`desiredMasterVersion` |  `string` The Kubernetes version to change the master to. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the default Kubernetes version  
`desiredMonitoringConfig` |  `object ([MonitoringConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MonitoringConfig))` The desired monitoring configuration.  
`desiredMonitoringService` |  `string` The monitoring service the cluster should use to write metrics. Currently available options: * "monitoring.googleapis.com/kubernetes" - The Cloud Monitoring service with a Kubernetes-native resource model * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * `none` \- No metrics will be exported from the cluster. If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.  
`desiredNodePoolAutoscaling` |  `object ([NodePoolAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePoolAutoscaling))` Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.  
`desiredNodePoolId` |  `string` The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family" or "desired_node_pool_autoscaling" is specified and there is more than one node pool on the cluster.  
`desiredNodeVersion` |  `string` The Kubernetes version to change the nodes to (typically an upgrade). Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the Kubernetes master version  
`desiredNotificationConfig` |  `object ([NotificationConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NotificationConfig))` The desired notification configuration.  
`desiredPrivateClusterConfig` |  `object ([PrivateClusterConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#PrivateClusterConfig))` The desired private cluster configuration.  
`desiredPrivateIpv6GoogleAccess` |  `enum` The desired state of IPv6 connectivity to Google Services.  
Enum type. Can be one of the following:  
`PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED` | Default value. Same as DISABLED  
`PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED` | No private access to or from Google Services  
`PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE` | Enables private IPv6 access to Google Services from GKE  
`PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL` | Enables priate IPv6 access to and from Google Services  
`desiredReleaseChannel` |  `object ([ReleaseChannel](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ReleaseChannel))` The desired release channel configuration.  
`desiredResourceUsageExportConfig` |  `object ([ResourceUsageExportConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ResourceUsageExportConfig))` The desired configuration for exporting resource usage.  
`desiredShieldedNodes` |  `object ([ShieldedNodes](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ShieldedNodes))` Configuration for Shielded Nodes.  
`desiredVerticalPodAutoscaling` |  `object ([VerticalPodAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#VerticalPodAutoscaling))` Cluster-level Vertical Pod Autoscaling configuration.  
`desiredWorkloadIdentityConfig` |  `object ([WorkloadIdentityConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#WorkloadIdentityConfig))` Configuration for Workload Identity.  
  
## CompleteIPRotationRequest

CompleteIPRotationRequest moves the cluster master back into single-IP mode. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster id) of the cluster to complete IP rotation. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://developers.google.com/console/help/new/#projectnumber). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## ConfidentialNodes

ConfidentialNodes is configuration for the confidential nodes feature, which makes nodes run on confidential VMs. Fields  
---  
`enabled` |  `boolean` Whether Confidential Nodes feature is enabled for all nodes in this cluster.  
  
## ConfigConnectorConfig

Configuration options for the Config Connector add-on. Fields  
---  
`enabled` |  `boolean` Whether Cloud Connector is enabled for this cluster.  
  
## ConsumptionMeteringConfig

Parameters for controlling consumption metering. Fields  
---  
`enabled` |  `boolean` Whether to enable consumption metering for this cluster. If enabled, a second BigQuery table will be created to hold resource consumption records.  
  
## CreateClusterRequest

CreateClusterRequest creates a cluster. Fields  
---  
`cluster` |  `object ([Cluster](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Cluster))` Required. A [cluster resource](https://cloud.google.com/container-engine/reference/rest/v1/projects.locations.clusters)  
`parent` |  `string` The parent (project and location) where the cluster will be created. Specified in the format `projects/*/locations/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the parent field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the parent field.  
  
## CreateNodePoolRequest

CreateNodePoolRequest creates a node pool for a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster. This field has been deprecated and replaced by the parent field.  
`nodePool` |  `object ([NodePool](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePool))` Required. The node pool to create.  
`parent` |  `string` The parent (project, location, cluster id) where the node pool will be created. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://developers.google.com/console/help/new/#projectnumber). This field has been deprecated and replaced by the parent field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the parent field.  
  
## DailyMaintenanceWindow

Time window specified for daily maintenance operations. Fields  
---  
`duration` |  `string` [Output only] Duration of the time window, automatically chosen to be smallest possible in the given scenario. Duration will be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "PTnHnMnS".  
`startTime` |  `string` Time within the maintenance window to start the maintenance operations. Time format should be in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) format "HH:MM", where HH : [00-23] and MM : [00-59] GMT.  
  
## DatabaseEncryption

Configuration of etcd encryption. Fields  
---  
`keyName` |  `string` Name of CloudKMS key to use for the encryption of secrets in etcd. Ex. projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key  
`state` |  `enum` Denotes the state of etcd encryption.  
Enum type. Can be one of the following:  
`UNKNOWN` | Should never be set  
`ENCRYPTED` | Secrets in etcd are encrypted.  
`DECRYPTED` | Secrets in etcd are stored in plain text (at etcd level) - this is unrelated to Compute Engine level full disk encryption.  
  
## DefaultSnatStatus

DefaultSnatStatus contains the desired state of whether default sNAT should be disabled on the cluster. Fields  
---  
`disabled` |  `boolean` Disables cluster default sNAT rules.  
  
## DnsCacheConfig

Configuration for NodeLocal DNSCache Fields  
---  
`enabled` |  `boolean` Whether NodeLocal DNSCache is enabled for this cluster.  
  
## GcePersistentDiskCsiDriverConfig

Configuration for the Compute Engine PD CSI driver. Fields  
---  
`enabled` |  `boolean` Whether the Compute Engine PD CSI driver is enabled for this cluster.  
  
## GcpFilestoreCsiDriverConfig

Configuration for the GCP Filestore CSI driver. Fields  
---  
`enabled` |  `boolean` Whether the GCP Filestore CSI driver is enabled for this cluster.  
  
## GetJSONWebKeysResponse

GetJSONWebKeysResponse is a valid JSON Web Key Set as specififed in rfc 7517 Fields  
---  
`cacheHeader` |  `object ([HttpCacheControlResponseHeader](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#HttpCacheControlResponseHeader))` OnePlatform automatically extracts this field and uses it to set the HTTP Cache-Control header.  
`keys[]` |  `object ([Jwk](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Jwk))` The public component of the keys used by the cluster to sign token requests.  
  
## GetOpenIDConfigResponse

GetOpenIDConfigResponse is an OIDC discovery document for the cluster. See the OpenID Connect Discovery 1.0 specification for details. Fields  
---  
`cacheHeader` |  `object ([HttpCacheControlResponseHeader](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#HttpCacheControlResponseHeader))` OnePlatform automatically extracts this field and uses it to set the HTTP Cache-Control header.  
`claims_supported[]` |  `string` Supported claims.  
`grant_types[]` |  `string` Supported grant types.  
`id_token_signing_alg_values_supported[]` |  `string` supported ID Token signing Algorithms.  
`issuer` |  `string` OIDC Issuer.  
`jwks_uri` |  `string` JSON Web Key uri.  
`response_types_supported[]` |  `string` Supported response types.  
`subject_types_supported[]` |  `string` Supported subject types.  
  
## HorizontalPodAutoscaling

Configuration options for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods. Fields  
---  
`disabled` |  `boolean` Whether the Horizontal Pod Autoscaling feature is enabled in the cluster. When enabled, it ensures that metrics are collected into Stackdriver Monitoring.  
  
## HttpCacheControlResponseHeader

RFC-2616: cache control support Fields  
---  
`age` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` 14.6 response cache age, in seconds since the response is generated  
`directive` |  `string` 14.9 request and response directives  
`expires` |  `string` 14.21 response cache expires, in RFC 1123 date format  
  
## HttpLoadBalancing

Configuration options for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster. Fields  
---  
`disabled` |  `boolean` Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled, it runs a small pod in the cluster that manages the load balancers.  
  
## ILBSubsettingConfig

ILBSubsettingConfig contains the desired config of L4 Internal LoadBalancer subsetting on this cluster. Fields  
---  
`enabled` |  `boolean` Enables l4 ILB subsetting for this cluster.  
  
## IPAllocationPolicy

Configuration for controlling how IPs are allocated in the cluster. Fields  
---  
`clusterIpv4Cidr` |  `string` This field is deprecated, use cluster_ipv4_cidr_block.  
`clusterIpv4CidrBlock` |  `string` The IP address range for the cluster pod IPs. If this field is set, then `cluster.cluster_ipv4_cidr` must be left blank. This field is only applicable when `use_ip_aliases` is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
`clusterSecondaryRangeName` |  `string` The name of the secondary range to be used for the cluster CIDR block. The secondary range will be used for pod IP addresses. This must be an existing secondary range associated with the cluster subnetwork. This field is only applicable with use_ip_aliases is true and create_subnetwork is false.  
`createSubnetwork` |  `boolean` Whether a new subnetwork will be created automatically for the cluster. This field is only applicable when `use_ip_aliases` is true.  
`nodeIpv4Cidr` |  `string` This field is deprecated, use node_ipv4_cidr_block.  
`nodeIpv4CidrBlock` |  `string` The IP address range of the instance IPs in this cluster. This is applicable only if `create_subnetwork` is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
`servicesIpv4Cidr` |  `string` This field is deprecated, use services_ipv4_cidr_block.  
`servicesIpv4CidrBlock` |  `string` The IP address range of the services IPs in this cluster. If blank, a range will be automatically chosen with the default size. This field is only applicable when `use_ip_aliases` is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
`servicesSecondaryRangeName` |  `string` The name of the secondary range to be used as for the services CIDR block. The secondary range will be used for service ClusterIPs. This must be an existing secondary range associated with the cluster subnetwork. This field is only applicable with use_ip_aliases is true and create_subnetwork is false.  
`subnetworkName` |  `string` A custom subnetwork name to be used if `create_subnetwork` is true. If this field is empty, then an automatic name will be chosen for the new subnetwork.  
`tpuIpv4CidrBlock` |  `string` The IP address range of the Cloud TPUs in this cluster. If unspecified, a range will be automatically chosen with the default size. This field is only applicable when `use_ip_aliases` is true. If unspecified, the range will use the default size. Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask. Set to a [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) from the RFC-1918 private networks (e.g. `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) to pick a specific range to use.  
`useIpAliases` |  `boolean` Whether alias IPs will be used for pod IPs in the cluster. This is used in conjunction with use_routes. It cannot be true if use_routes is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode  
`useRoutes` |  `boolean` Whether routes will be used for pod IPs in the cluster. This is used in conjunction with use_ip_aliases. It cannot be true if use_ip_aliases is true. If both use_ip_aliases and use_routes are false, then the server picks the default IP allocation mode  
  
## IntraNodeVisibilityConfig

IntraNodeVisibilityConfig contains the desired config of the intra-node visibility on this cluster. Fields  
---  
`enabled` |  `boolean` Enables intra node visibility for this cluster.  
  
## Jwk

Jwk is a JSON Web Key as specified in RFC 7517 Fields  
---  
`alg` |  `string` Algorithm.  
`crv` |  `string` Used for ECDSA keys.  
`e` |  `string` Used for RSA keys.  
`kid` |  `string` Key ID.  
`kty` |  `string` Key Type.  
`n` |  `string` Used for RSA keys.  
`use` |  `string` Permitted uses for the public keys.  
`x` |  `string` Used for ECDSA keys.  
`y` |  `string` Used for ECDSA keys.  
  
## KubernetesDashboard

Configuration for the Kubernetes Dashboard. Fields  
---  
`disabled` |  `boolean` Whether the Kubernetes Dashboard is enabled for this cluster.  
  
## LegacyAbac

Configuration for the legacy Attribute Based Access Control authorization mode. Fields  
---  
`enabled` |  `boolean` Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM.  
  
## LinuxNodeConfig

Parameters that can be configured on Linux nodes. Fields  
---  
`sysctls` |  `map (key: string, value: string)` The Linux kernel parameters to be applied to the nodes and all pods running on the nodes. The following parameters are supported. net.core.netdev_max_backlog net.core.rmem_max net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse  
  
## ListClustersResponse

ListClustersResponse is the result of ListClustersRequest. Fields  
---  
`clusters[]` |  `object ([Cluster](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Cluster))` A list of clusters in the project in the specified zone, or across all ones.  
`missingZones[]` |  `string` If any zones are listed here, the list of clusters returned may be missing those zones.  
  
## ListNodePoolsResponse

ListNodePoolsResponse is the result of ListNodePoolsRequest. Fields  
---  
`nodePools[]` |  `object ([NodePool](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePool))` A list of node pools for a cluster.  
  
## ListOperationsResponse

ListOperationsResponse is the result of ListOperationsRequest. Fields  
---  
`missingZones[]` |  `string` If any zones are listed here, the list of operations returned may be missing the operations from those zones.  
`operations[]` |  `object ([Operation](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Operation))` A list of operations in the project in the specified zone.  
  
## ListUsableSubnetworksResponse

ListUsableSubnetworksResponse is the response of ListUsableSubnetworksRequest. Fields  
---  
`nextPageToken` |  `string` This token allows you to get the next page of results for list requests. If the number of results is larger than `page_size`, use the `next_page_token` as a value for the query parameter `page_token` in the next request. The value will become empty when there are no more pages.  
`subnetworks[]` |  `object ([UsableSubnetwork](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#UsableSubnetwork))` A list of usable subnetworks in the specified network project.  
  
## LoggingComponentConfig

LoggingComponentConfig is cluster logging component configuration. Fields  
---  
`enableComponents[]` |  `string` Select components to collect logs. An empty set would disable all logging.  
  
## LoggingConfig

LoggingConfig is cluster logging configuration. Fields  
---  
`componentConfig` |  `object ([LoggingComponentConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LoggingComponentConfig))` Logging components configuration  
  
## MaintenancePolicy

MaintenancePolicy defines the maintenance policy to be used for the cluster. Fields  
---  
`resourceVersion` |  `string` A hash identifying the version of this policy, so that updates to fields of the policy won't accidentally undo intermediate changes (and so that users of the API unaware of some fields won't accidentally remove other fields). Make a `get()` request to the cluster to get the current resource version and include it with requests to set the policy.  
`window` |  `object ([MaintenanceWindow](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MaintenanceWindow))` Specifies the maintenance window in which maintenance may be performed.  
  
## MaintenanceWindow

MaintenanceWindow defines the maintenance window to be used for the cluster. Fields  
---  
`dailyMaintenanceWindow` |  `object ([DailyMaintenanceWindow](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DailyMaintenanceWindow))` DailyMaintenanceWindow specifies a daily maintenance operation window.  
`maintenanceExclusions` |  `map (key: string, value: object ([TimeWindow](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#TimeWindow)))` Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.  
`recurringWindow` |  `object ([RecurringTimeWindow](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#RecurringTimeWindow))` RecurringWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time.  
  
## MasterAuth

The authentication information for accessing the master endpoint. Authentication can be done using HTTP basic auth or using client certificates. Fields  
---  
`clientCertificate` |  `string` [Output only] Base64-encoded public certificate used by clients to authenticate to the cluster endpoint.  
`clientCertificateConfig` |  `object ([ClientCertificateConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ClientCertificateConfig))` Configuration for client certificate authentication on the cluster. For clusters before v1.12, if no configuration is specified, a client certificate is issued.  
`clientKey` |  `string` [Output only] Base64-encoded private key used by clients to authenticate to the cluster endpoint.  
`clusterCaCertificate` |  `string` [Output only] Base64-encoded public certificate that is the root of trust for the cluster.  
`password` |  `string` The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password. If a password is provided for cluster creation, username must be non-empty. Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication  
`username` |  `string` The username to use for HTTP basic authentication to the master endpoint. For clusters v1.6.0 and later, basic authentication can be disabled by leaving username unspecified (or setting it to the empty string). Warning: basic authentication is deprecated, and will be removed in GKE control plane versions 1.19 and newer. For a list of recommended authentication methods, see: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication  
  
## MasterAuthorizedNetworksConfig

Configuration options for the master authorized networks feature. Enabled master authorized networks will disallow all external traffic to access Kubernetes master through HTTPS except traffic from the given CIDR blocks, Google Compute Engine Public IPs and Google Prod IPs. Fields  
---  
`cidrBlocks[]` |  `object ([CidrBlock](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#CidrBlock))` cidr_blocks define up to 50 external networks that could access Kubernetes master through HTTPS.  
`enabled` |  `boolean` Whether or not master authorized networks is enabled.  
  
## MaxPodsConstraint

Constraints applied to pods. Fields  
---  
`maxPodsPerNode` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Constraint enforced on the max num of pods per node.  
  
## Metric

Progress metric is (string, int|float|string) pair. Fields  
---  
`doubleValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` For metrics with floating point value.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` For metrics with integer value.  
`name` |  `string` Required. Metric name, e.g., "nodes total", "percent done".  
`stringValue` |  `string` For metrics with custom values (ratios, visual progress, etc.).  
  
## MonitoringComponentConfig

MonitoringComponentConfig is cluster monitoring component configuration. Fields  
---  
`enableComponents[]` |  `string` Select components to collect metrics. An empty set would disable all monitoring.  
  
## MonitoringConfig

MonitoringConfig is cluster monitoring configuration. Fields  
---  
`componentConfig` |  `object ([MonitoringComponentConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MonitoringComponentConfig))` Monitoring components configuration  
  
## NetworkConfig

NetworkConfig reports the relative names of network & subnetwork. Fields  
---  
`datapathProvider` |  `enum` The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation.  
Enum type. Can be one of the following:  
`DATAPATH_PROVIDER_UNSPECIFIED` | Default value.  
`LEGACY_DATAPATH` | Use the IPTables implementation based on kube-proxy.  
`ADVANCED_DATAPATH` | Use the eBPF based GKE Dataplane V2 with additional features. See the [GKE Dataplane V2 documentation](https://cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2) for more.  
`defaultSnatStatus` |  `object ([DefaultSnatStatus](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#DefaultSnatStatus))` Whether the cluster disables default in-node sNAT rules. In-node sNAT rules will be disabled when default_snat_status is disabled. When disabled is set to false, default IP masquerade rules will be applied to the nodes to prevent sNAT on cluster internal traffic.  
`enableIntraNodeVisibility` |  `boolean` Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.  
`enableL4ilbSubsetting` |  `boolean` Whether L4ILB Subsetting is enabled for this cluster.  
`network` |  `string` Output only. The relative name of the Google Compute Engine network(https://cloud.google.com/compute/docs/networks-and-firewalls#networks) to which the cluster is connected. Example: projects/my-project/global/networks/my-network  
`privateIpv6GoogleAccess` |  `enum` The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4)  
Enum type. Can be one of the following:  
`PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED` | Default value. Same as DISABLED  
`PRIVATE_IPV6_GOOGLE_ACCESS_DISABLED` | No private access to or from Google Services  
`PRIVATE_IPV6_GOOGLE_ACCESS_TO_GOOGLE` | Enables private IPv6 access to Google Services from GKE  
`PRIVATE_IPV6_GOOGLE_ACCESS_BIDIRECTIONAL` | Enables priate IPv6 access to and from Google Services  
`subnetwork` |  `string` Output only. The relative name of the Google Compute Engine [subnetwork](https://cloud.google.com/compute/docs/vpc) to which the cluster is connected. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet  
  
## NetworkPolicy

Configuration options for the NetworkPolicy feature. https://kubernetes.io/docs/concepts/services-networking/networkpolicies/ Fields  
---  
`enabled` |  `boolean` Whether network policy is enabled on the cluster.  
`provider` |  `enum` The selected network policy provider.  
Enum type. Can be one of the following:  
`PROVIDER_UNSPECIFIED` | Not set  
`CALICO` | Tigera (Calico Felix).  
  
## NetworkPolicyConfig

Configuration for NetworkPolicy. This only tracks whether the addon is enabled or not on the Master, it does not track whether network policy is enabled for the nodes. Fields  
---  
`disabled` |  `boolean` Whether NetworkPolicy is enabled for this cluster.  
  
## NodeConfig

Parameters that describe the nodes in a cluster. Fields  
---  
`accelerators[]` |  `object ([AcceleratorConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AcceleratorConfig))` A list of hardware accelerators to be attached to each node. See https://cloud.google.com/compute/docs/gpus for more information about support for GPUs.  
`bootDiskKmsKey` |  `string` The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool. This should be of the form projects/[KEY_PROJECT_ID]/locations/[LOCATION]/keyRings/[RING_NAME]/cryptoKeys/[KEY_NAME]. For more information about protecting resources with Cloud KMS Keys please see: https://cloud.google.com/compute/docs/disks/customer-managed-encryption  
`diskSizeGb` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.  
`diskType` |  `string` Type of the disk attached to each node (e.g. 'pd-standard', 'pd-ssd' or 'pd-balanced') If unspecified, the default disk type is 'pd-standard'  
`gvnic` |  `object ([VirtualNIC](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#VirtualNIC))` Enable or disable gvnic in the node pool.  
`imageType` |  `string` The image type to use for this node. Note that for a given image type, the latest version of it will be used.  
`kubeletConfig` |  `object ([NodeKubeletConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeKubeletConfig))` Node kubelet configs.  
`labels` |  `map (key: string, value: string)` The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version -- it's best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/  
`linuxNodeConfig` |  `object ([LinuxNodeConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LinuxNodeConfig))` Parameters that can be configured on Linux nodes.  
`localSsdCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of local SSD disks to be attached to the node. The limit for this value is dependent upon the maximum number of disks available on a machine per zone. See: https://cloud.google.com/compute/docs/disks/local-ssd for more information.  
`machineType` |  `string` The name of a Google Compute Engine [machine type](https://cloud.google.com/compute/docs/machine-types) If unspecified, the default machine type is `e2-medium`.  
`metadata` |  `map (key: string, value: string)` The metadata key/value pairs assigned to instances in the cluster. Keys must conform to the regexp `[a-zA-Z0-9-_]+` and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the reserved keys: - "cluster-location" - "cluster-name" - "cluster-uid" - "configure-sh" - "containerd-configure-sh" - "enable-os-login" - "gci-ensure-gke-docker" - "gci-metrics-enabled" - "gci-update-strategy" - "instance-template" - "kube-env" - "startup-script" - "user-data" - "disable-address-manager" - "windows-startup-script-ps1" - "common-psm1" - "k8s-node-setup-psm1" - "install-ssh-psm1" - "user-profile-psm1" Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value's size must be less than or equal to 32 KB. The total size of all keys and values must be less than 512 KB.  
`minCpuPlatform` |  `string` Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as `minCpuPlatform: "Intel Haswell"` or `minCpuPlatform: "Intel Sandy Bridge"`. For more information, read [how to specify min CPU platform](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform)  
`nodeGroup` |  `string` Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on [sole tenant nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes).  
`oauthScopes[]` |  `string` The set of Google API scopes to be made available on all of the node VMs under the "default" service account. The following scopes are recommended, but not required, and by default are not included: * `https://www.googleapis.com/auth/compute` is required for mounting persistent storage on your nodes. * `https://www.googleapis.com/auth/devstorage.read_only` is required for communicating with **gcr.io** (the [Google Container Registry](https://cloud.google.com/container-registry/)). If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.  
`preemptible` |  `boolean` Whether the nodes are created as preemptible VM instances. See: https://cloud.google.com/compute/docs/instances/preemptible for more information about preemptible VM instances.  
`reservationAffinity` |  `object ([ReservationAffinity](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ReservationAffinity))` The optional reservation affinity. Setting this field will apply the specified [Zonal Compute Reservation](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) to this node pool.  
`sandboxConfig` |  `object ([SandboxConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#SandboxConfig))` Sandbox configuration for this node.  
`serviceAccount` |  `string` The Google Cloud Platform Service Account to be used by the node VMs. Specify the email address of the Service Account; otherwise, if no Service Account is specified, the "default" service account is used.  
`shieldedInstanceConfig` |  `object ([ShieldedInstanceConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ShieldedInstanceConfig))` Shielded Instance options.  
`tags[]` |  `string` The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.  
`taints[]` |  `object ([NodeTaint](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeTaint))` List of kubernetes taints to be applied to each node. For more information, including usage and the valid values, see: https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/  
`workloadMetadataConfig` |  `object ([WorkloadMetadataConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#WorkloadMetadataConfig))` The workload metadata configuration for this node.  
  
## NodeKubeletConfig

Node kubelet configs. Fields  
---  
`cpuCfsQuota` |  `boolean` Enable CPU CFS quota enforcement for containers that specify CPU limits. This option is enabled by default which makes kubelet use CFS quota (https://www.kernel.org/doc/Documentation/scheduler/sched-bwc.txt) to enforce container CPU limits. Otherwise, CPU limits will not be enforced at all. Disable this option to mitigate CPU throttling problems while still having your pods to be in Guaranteed QoS class by specifying the CPU limits. The default value is 'true' if unspecified.  
`cpuCfsQuotaPeriod` |  `string` Set the CPU CFS quota period value 'cpu.cfs_period_us'. The string must be a sequence of decimal numbers, each with optional fraction and a unit suffix, such as "300ms". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h". The value must be a positive duration.  
`cpuManagerPolicy` |  `string` Control the CPU management policy on the node. See https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/ The following values are allowed. - "none": the default, which represents the existing scheduling behavior. - "static": allows pods with certain resource characteristics to be granted increased CPU affinity and exclusivity on the node. The default value is 'none' if unspecified.  
  
## NodeManagement

NodeManagement defines the set of node management services turned on for the node pool. Fields  
---  
`autoRepair` |  `boolean` A flag that specifies whether the node auto-repair is enabled for the node pool. If enabled, the nodes in this node pool will be monitored and, if they fail health checks too many times, an automatic repair action will be triggered.  
`autoUpgrade` |  `boolean` A flag that specifies whether node auto-upgrade is enabled for the node pool. If enabled, node auto-upgrade helps keep the nodes in your node pool up to date with the latest release version of Kubernetes.  
`upgradeOptions` |  `object ([AutoUpgradeOptions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AutoUpgradeOptions))` Specifies the Auto Upgrade knobs for the node pool.  
  
## NodeNetworkConfig

Parameters for node pool-level network config. Fields  
---  
`createPodRange` |  `boolean` Input only. Whether to create a new range for pod IPs in this node pool. Defaults are provided for `pod_range` and `pod_ipv4_cidr_block` if they are not specified. If neither `create_pod_range` or `pod_range` are specified, the cluster-level default (`ip_allocation_policy.cluster_ipv4_cidr_block`) is used. Only applicable if `ip_allocation_policy.use_ip_aliases` is true. This field cannot be changed after the node pool has been created.  
`podIpv4CidrBlock` |  `string` The IP address range for pod IPs in this node pool. Only applicable if `create_pod_range` is true. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. `/14`) to have a range chosen with a specific netmask. Set to a [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation (e.g. `10.96.0.0/14`) to pick a specific range to use. Only applicable if `ip_allocation_policy.use_ip_aliases` is true. This field cannot be changed after the node pool has been created.  
`podRange` |  `string` The ID of the secondary range for pod IPs. If `create_pod_range` is true, this ID is used for the new range. If `create_pod_range` is false, uses an existing secondary range with this ID. Only applicable if `ip_allocation_policy.use_ip_aliases` is true. This field cannot be changed after the node pool has been created.  
  
## NodePool

NodePool contains the name and configuration for a cluster's node pool. Node pools are a set of nodes (i.e. VM's), with a common configuration and specification, under the control of the cluster master. They may have a set of Kubernetes labels applied to them, which may be used to reference them during pod scheduling. They may also be resized up or down, to accommodate the workload. Fields  
---  
`autoscaling` |  `object ([NodePoolAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePoolAutoscaling))` Autoscaler configuration for this NodePool. Autoscaler is enabled only if a valid configuration is present.  
`conditions[]` |  `object ([StatusCondition](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#StatusCondition))` Which conditions caused the current node pool state.  
`config` |  `object ([NodeConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeConfig))` The node configuration of the pool.  
`initialNodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The initial node count for the pool. You must ensure that your Compute Engine [resource quota](https://cloud.google.com/compute/quotas) is sufficient for this number of instances. You must also have available firewall and routes quota.  
`instanceGroupUrls[]` |  `string` [Output only] The resource URLs of the [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances) associated with this node pool.  
`locations[]` |  `string` The list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the NodePool's nodes should be located. If this value is unspecified during node pool creation, the [Cluster.Locations](https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.locations) value will be used, instead. Warning: changing node pool locations will result in nodes being added and/or removed.  
`management` |  `object ([NodeManagement](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeManagement))` NodeManagement configuration for this NodePool.  
`maxPodsConstraint` |  `object ([MaxPodsConstraint](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MaxPodsConstraint))` The constraint on the maximum number of pods that can be run simultaneously on a node in the node pool.  
`name` |  `string` The name of the node pool.  
`networkConfig` |  `object ([NodeNetworkConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeNetworkConfig))` Networking configuration for this NodePool. If specified, it overrides the cluster-level defaults.  
`podIpv4CidrSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` [Output only] The pod CIDR block size per node in this node pool.  
`selfLink` |  `string` [Output only] Server-defined URL for the resource.  
`status` |  `enum` [Output only] The status of the nodes in this pool instance.  
Enum type. Can be one of the following:  
`STATUS_UNSPECIFIED` | Not set.  
`PROVISIONING` | The PROVISIONING state indicates the node pool is being created.  
`RUNNING` | The RUNNING state indicates the node pool has been created and is fully usable.  
`RUNNING_WITH_ERROR` | The RUNNING_WITH_ERROR state indicates the node pool has been created and is partially usable. Some error state has occurred and some functionality may be impaired. Customer may need to reissue a request or trigger a new update.  
`RECONCILING` | The RECONCILING state indicates that some work is actively being done on the node pool, such as upgrading node software. Details can be found in the `statusMessage` field.  
`STOPPING` | The STOPPING state indicates the node pool is being deleted.  
`ERROR` | The ERROR state indicates the node pool may be unusable. Details can be found in the `statusMessage` field.  
`statusMessage` |  `string` [Output only] Deprecated. Use conditions instead. Additional information about the current status of this node pool instance, if available.  
`upgradeSettings` |  `object ([UpgradeSettings](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#UpgradeSettings))` Upgrade settings control disruption and speed of the upgrade.  
`version` |  `string` The version of the Kubernetes of this node.  
  
## NodePoolAutoscaling

NodePoolAutoscaling contains information required by cluster autoscaler to adjust the size of the node pool to the current cluster usage. Fields  
---  
`autoprovisioned` |  `boolean` Can this node pool be deleted automatically.  
`enabled` |  `boolean` Is autoscaling enabled for this node pool.  
`maxNodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum number of nodes in the NodePool. Must be >= min_node_count. There has to be enough quota to scale up the cluster.  
`minNodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Minimum number of nodes in the NodePool. Must be >= 1 and <= max_node_count.  
  
## NodeTaint

Kubernetes taint is comprised of three fields: key, value, and effect. Effect can only be one of three types: NoSchedule, PreferNoSchedule or NoExecute. See [here](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration) for more information, including usage and the valid values. Fields  
---  
`effect` |  `enum` Effect for taint.  
Enum type. Can be one of the following:  
`EFFECT_UNSPECIFIED` | Not set  
`NO_SCHEDULE` | NoSchedule  
`PREFER_NO_SCHEDULE` | PreferNoSchedule  
`NO_EXECUTE` | NoExecute  
`key` |  `string` Key for taint.  
`value` |  `string` Value for taint.  
  
## NotificationConfig

NotificationConfig is the configuration of notifications. Fields  
---  
`pubsub` |  `object ([PubSub](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#PubSub))` Notification config for Pub/Sub.  
  
## Operation

This operation resource represents operations that may have happened or are happening on the cluster. All fields are output only. Fields  
---  
`clusterConditions[]` |  `object ([StatusCondition](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#StatusCondition))` Which conditions caused the current cluster state. Deprecated. Use field error instead.  
`detail` |  `string` Detailed operation progress, if available.  
`endTime` |  `string` [Output only] The time the operation completed, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`error` |  `object ([Status](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Status))` The error result of the operation in case of failure.  
`location` |  `string` [Output only] The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) or [region](https://cloud.google.com/compute/docs/regions-zones/regions-zones#available) in which the cluster resides.  
`name` |  `string` The server-assigned ID for the operation.  
`nodepoolConditions[]` |  `object ([StatusCondition](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#StatusCondition))` Which conditions caused the current node pool state. Deprecated. Use field error instead.  
`operationType` |  `enum` The operation type.  
Enum type. Can be one of the following:  
`TYPE_UNSPECIFIED` | Not set.  
`CREATE_CLUSTER` | Cluster create.  
`DELETE_CLUSTER` | Cluster delete.  
`UPGRADE_MASTER` | A master upgrade.  
`UPGRADE_NODES` | A node upgrade.  
`REPAIR_CLUSTER` | Cluster repair.  
`UPDATE_CLUSTER` | Cluster update.  
`CREATE_NODE_POOL` | Node pool create.  
`DELETE_NODE_POOL` | Node pool delete.  
`SET_NODE_POOL_MANAGEMENT` | Set node pool management.  
`AUTO_REPAIR_NODES` | Automatic node pool repair.  
`AUTO_UPGRADE_NODES` | Automatic node upgrade.  
`SET_LABELS` | Set labels.  
`SET_MASTER_AUTH` | Set/generate master auth materials  
`SET_NODE_POOL_SIZE` | Set node pool size.  
`SET_NETWORK_POLICY` | Updates network policy for a cluster.  
`SET_MAINTENANCE_POLICY` | Set the maintenance policy.  
`progress` |  `object ([OperationProgress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#OperationProgress))` Output only. [Output only] Progress information for an operation.  
`selfLink` |  `string` Server-defined URL for the resource.  
`startTime` |  `string` [Output only] The time the operation started, in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`status` |  `enum` The current status of the operation.  
Enum type. Can be one of the following:  
`STATUS_UNSPECIFIED` | Not set.  
`PENDING` | The operation has been created.  
`RUNNING` | The operation is currently running.  
`DONE` | The operation is done, either cancelled or completed.  
`ABORTING` | The operation is aborting.  
`statusMessage` |  `string` Output only. If an error has occurred, a textual description of the error. Deprecated. Use the field error instead.  
`targetLink` |  `string` Server-defined URL for the target of the operation.  
`zone` |  `string` The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the operation is taking place. This field is deprecated, use location instead.  
  
## OperationProgress

Information about operation (or operation stage) progress. Fields  
---  
`metrics[]` |  `object ([Metric](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#Metric))` Progress metric bundle, for example: metrics: [{name: "nodes done", int_value: 15}, {name: "nodes total", int_value: 32}] or metrics: [{name: "progress", double_value: 0.56}, {name: "progress scale", double_value: 1.0}]  
`name` |  `string` A non-parameterized string describing an operation stage. Unset for single-stage operations.  
`stages[]` |  `object ([OperationProgress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#OperationProgress))` Substages of an operation or a stage.  
`status` |  `enum` Status of an operation stage. Unset for single-stage operations.  
Enum type. Can be one of the following:  
`STATUS_UNSPECIFIED` | Not set.  
`PENDING` | The operation has been created.  
`RUNNING` | The operation is currently running.  
`DONE` | The operation is done, either cancelled or completed.  
`ABORTING` | The operation is aborting.  
  
## PrivateClusterConfig

Configuration options for private clusters. Fields  
---  
`enablePrivateEndpoint` |  `boolean` Whether the master's internal IP address is used as the cluster endpoint.  
`enablePrivateNodes` |  `boolean` Whether nodes have internal IP addresses only. If enabled, all nodes are given only RFC 1918 private addresses and communicate with the master via private networking.  
`masterGlobalAccessConfig` |  `object ([PrivateClusterMasterGlobalAccessConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#PrivateClusterMasterGlobalAccessConfig))` Controls master global access settings.  
`masterIpv4CidrBlock` |  `string` The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning internal IP addresses to the master or set of masters, as well as the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network.  
`peeringName` |  `string` Output only. The peering name in the customer VPC used by this cluster.  
`privateEndpoint` |  `string` Output only. The internal IP address of this cluster's master endpoint.  
`publicEndpoint` |  `string` Output only. The external IP address of this cluster's master endpoint.  
  
## PrivateClusterMasterGlobalAccessConfig

Configuration for controlling master global access settings. Fields  
---  
`enabled` |  `boolean` Whenever master is accessible globally or not.  
  
## PubSub

Pub/Sub specific notification config. Fields  
---  
`enabled` |  `boolean` Enable notifications for Pub/Sub.  
`topic` |  `string` The desired Pub/Sub topic to which notifications will be sent by GKE. Format is `projects/{project}/topics/{topic}`.  
  
## RecurringTimeWindow

Represents an arbitrary window of time that recurs. Fields  
---  
`recurrence` |  `string` An RRULE (https://tools.ietf.org/html/rfc5545#section-3.8.5.3) for how this window reccurs. They go on for the span of time between the start and end time. For example, to have something repeat every weekday, you'd use: `FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR` To repeat some window daily (equivalent to the DailyMaintenanceWindow): `FREQ=DAILY` For the first weekend of every month: `FREQ=MONTHLY;BYSETPOS=1;BYDAY=SA,SU` This specifies how frequently the window starts. Eg, if you wanted to have a 9-5 UTC-4 window every weekday, you'd use something like: `start time = 2019-01-01T09:00:00-0400 end time = 2019-01-01T17:00:00-0400 recurrence = FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR` Windows can span multiple days. Eg, to make the window encompass every weekend from midnight Saturday till the last minute of Sunday UTC: `start time = 2019-01-05T00:00:00Z end time = 2019-01-07T23:59:00Z recurrence = FREQ=WEEKLY;BYDAY=SA` Note the start and end time's specific dates are largely arbitrary except to specify duration of the window and when it first starts. The FREQ values of HOURLY, MINUTELY, and SECONDLY are not supported.  
`window` |  `object ([TimeWindow](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#TimeWindow))` The window of the first recurrence.  
  
## ReleaseChannel

ReleaseChannel indicates which release channel a cluster is subscribed to. Release channels are arranged in order of risk. When a cluster is subscribed to a release channel, Google maintains both the master version and the node version. Node auto-upgrade defaults to true and cannot be disabled. Fields  
---  
`channel` |  `enum` channel specifies which release channel the cluster is subscribed to.  
Enum type. Can be one of the following:  
`UNSPECIFIED` | No channel specified.  
`RAPID` | RAPID channel is offered on an early access basis for customers who want to test new releases. WARNING: Versions available in the RAPID Channel may be subject to unresolved issues with no known workaround and are not subject to any SLAs.  
`REGULAR` | Clusters subscribed to REGULAR receive versions that are considered GA quality. REGULAR is intended for production users who want to take advantage of new features.  
`STABLE` | Clusters subscribed to STABLE receive versions that are known to be stable and reliable in production.  
  
## ReleaseChannelConfig

ReleaseChannelConfig exposes configuration for a release channel. Fields  
---  
`channel` |  `enum` The release channel this configuration applies to.  
Enum type. Can be one of the following:  
`UNSPECIFIED` | No channel specified.  
`RAPID` | RAPID channel is offered on an early access basis for customers who want to test new releases. WARNING: Versions available in the RAPID Channel may be subject to unresolved issues with no known workaround and are not subject to any SLAs.  
`REGULAR` | Clusters subscribed to REGULAR receive versions that are considered GA quality. REGULAR is intended for production users who want to take advantage of new features.  
`STABLE` | Clusters subscribed to STABLE receive versions that are known to be stable and reliable in production.  
`defaultVersion` |  `string` The default version for newly created clusters on the channel.  
`validVersions[]` |  `string` List of valid versions for the channel.  
  
## ReservationAffinity

[ReservationAffinity](https://cloud.google.com/compute/docs/instances/reserving-zonal-resources) is the configuration of desired reservation which instances could take capacity from. Fields  
---  
`consumeReservationType` |  `enum` Corresponds to the type of reservation consumption.  
Enum type. Can be one of the following:  
`UNSPECIFIED` | Default value. This should not be used.  
`NO_RESERVATION` | Do not consume from any reserved capacity.  
`ANY_RESERVATION` | Consume any reservation available.  
`SPECIFIC_RESERVATION` | Must consume from a specific reservation. Must specify key value fields for specifying the reservations.  
`key` |  `string` Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, specify "googleapis.com/reservation-name" as the key and specify the name of your reservation as its value.  
`values[]` |  `string` Corresponds to the label value(s) of reservation resource(s).  
  
## ResourceLimit

Contains information about amount of some resource in the cluster. For memory, value should be in GB. Fields  
---  
`maximum` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Maximum amount of the resource in the cluster.  
`minimum` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Minimum amount of the resource in the cluster.  
`resourceType` |  `string` Resource name "cpu", "memory" or gpu-specific string.  
  
## ResourceUsageExportConfig

Configuration for exporting cluster resource usages. Fields  
---  
`bigqueryDestination` |  `object ([BigQueryDestination](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#BigQueryDestination))` Configuration to use BigQuery as usage export destination.  
`consumptionMeteringConfig` |  `object ([ConsumptionMeteringConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ConsumptionMeteringConfig))` Configuration to enable resource consumption metering.  
`enableNetworkEgressMetering` |  `boolean` Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created in the cluster to meter network egress traffic.  
  
## RollbackNodePoolUpgradeRequest

RollbackNodePoolUpgradeRequest rollbacks the previously Aborted or Failed NodePool upgrade. This will be an no-op if the last upgrade successfully completed. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to rollback. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster, node pool id) of the node poll to rollback upgrade. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
`nodePoolId` |  `string` Deprecated. The name of the node pool to rollback. This field has been deprecated and replaced by the name field.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SandboxConfig

SandboxConfig contains configurations of the sandbox to use for the node. Fields  
---  
`type` |  `enum` Type of the sandbox to use for the node.  
Enum type. Can be one of the following:  
`UNSPECIFIED` | Default value. This should not be used.  
`GVISOR` | Run sandbox using gvisor.  
  
## ServerConfig

Kubernetes Engine service configuration. Fields  
---  
`channels[]` |  `object ([ReleaseChannelConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ReleaseChannelConfig))` List of release channel configurations.  
`defaultClusterVersion` |  `string` Version of Kubernetes the service deploys by default.  
`defaultImageType` |  `string` Default image type.  
`validImageTypes[]` |  `string` List of valid image types.  
`validMasterVersions[]` |  `string` List of valid master versions, in descending order.  
`validNodeVersions[]` |  `string` List of valid node upgrade target versions, in descending order.  
  
## SetAddonsConfigRequest

SetAddonsConfigRequest sets the addons associated with the cluster. Fields  
---  
`addonsConfig` |  `object ([AddonsConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#AddonsConfig))` Required. The desired configurations for the various addons available to run in the cluster.  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster) of the cluster to set addons. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetLabelsRequest

SetLabelsRequest sets the Google Cloud Platform labels on a Google Container Engine cluster, which will in turn set them for Google Compute Engine resources used by that cluster Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`labelFingerprint` |  `string` Required. The fingerprint of the previous set of labels for this resource, used to detect conflicts. The fingerprint is initially generated by Kubernetes Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash when updating or changing labels. Make a `get()` request to the resource to get the latest fingerprint.  
`name` |  `string` The name (project, location, cluster id) of the cluster to set labels. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://developers.google.com/console/help/new/#projectnumber). This field has been deprecated and replaced by the name field.  
`resourceLabels` |  `map (key: string, value: string)` Required. The labels to set for that cluster.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetLegacyAbacRequest

SetLegacyAbacRequest enables or disables the ABAC authorization mechanism for a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to update. This field has been deprecated and replaced by the name field.  
`enabled` |  `boolean` Required. Whether ABAC authorization will be enabled in the cluster.  
`name` |  `string` The name (project, location, cluster id) of the cluster to set legacy abac. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetLocationsRequest

SetLocationsRequest sets the locations of the cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`locations[]` |  `string` Required. The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located. Changing the locations a cluster is in will result in nodes being either created or removed from the cluster, depending on whether locations are being added or removed. This list must always include the cluster's primary zone.  
`name` |  `string` The name (project, location, cluster) of the cluster to set locations. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetLoggingServiceRequest

SetLoggingServiceRequest sets the logging service of a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`loggingService` |  `string` Required. The logging service the cluster should use to write logs. Currently available options: * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15). * `none` \- no logs will be exported from the cluster. If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.  
`name` |  `string` The name (project, location, cluster) of the cluster to set logging. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetMaintenancePolicyRequest

SetMaintenancePolicyRequest sets the maintenance policy for a cluster. Fields  
---  
`clusterId` |  `string` Required. The name of the cluster to update.  
`maintenancePolicy` |  `object ([MaintenancePolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MaintenancePolicy))` Required. The maintenance policy to be set for the cluster. An empty field clears the existing maintenance policy.  
`name` |  `string` The name (project, location, cluster id) of the cluster to set maintenance policy. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Required. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840).  
`zone` |  `string` Required. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides.  
  
## SetMasterAuthRequest

SetMasterAuthRequest updates the admin password of a cluster. Fields  
---  
`action` |  `enum` Required. The exact form of action to be taken on the master auth.  
Enum type. Can be one of the following:  
`UNKNOWN` | Operation is unknown and will error out.  
`SET_PASSWORD` | Set the password to a user generated value.  
`GENERATE_PASSWORD` | Generate a new password and set it to that.  
`SET_USERNAME` | Set the username. If an empty username is provided, basic authentication is disabled for the cluster. If a non-empty username is provided, basic authentication is enabled, with either a provided password or a generated one.  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster) of the cluster to set auth. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`update` |  `object ([MasterAuth](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#MasterAuth))` Required. A description of the update.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetMonitoringServiceRequest

SetMonitoringServiceRequest sets the monitoring service of a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`monitoringService` |  `string` Required. The monitoring service the cluster should use to write metrics. Currently available options: * "monitoring.googleapis.com/kubernetes" - The Cloud Monitoring service with a Kubernetes-native resource model * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15). * `none` \- No metrics will be exported from the cluster. If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.  
`name` |  `string` The name (project, location, cluster) of the cluster to set monitoring. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetNetworkPolicyRequest

SetNetworkPolicyRequest enables/disables network policy for a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster id) of the cluster to set networking policy. Specified in the format `projects/*/locations/*/clusters/*`.  
`networkPolicy` |  `object ([NetworkPolicy](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NetworkPolicy))` Required. Configuration options for the NetworkPolicy feature.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://developers.google.com/console/help/new/#projectnumber). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetNodePoolAutoscalingRequest

SetNodePoolAutoscalingRequest sets the autoscaler settings of a node pool. Fields  
---  
`autoscaling` |  `object ([NodePoolAutoscaling](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodePoolAutoscaling))` Required. Autoscaling configuration for the node pool.  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster, node pool) of the node pool to set autoscaler settings. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
`nodePoolId` |  `string` Deprecated. The name of the node pool to upgrade. This field has been deprecated and replaced by the name field.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetNodePoolManagementRequest

SetNodePoolManagementRequest sets the node management properties of a node pool. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to update. This field has been deprecated and replaced by the name field.  
`management` |  `object ([NodeManagement](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeManagement))` Required. NodeManagement configuration for the node pool.  
`name` |  `string` The name (project, location, cluster, node pool id) of the node pool to set management properties. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
`nodePoolId` |  `string` Deprecated. The name of the node pool to update. This field has been deprecated and replaced by the name field.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## SetNodePoolSizeRequest

SetNodePoolSizeRequest sets the size of a node pool. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to update. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster, node pool id) of the node pool to set size. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
`nodeCount` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Required. The desired node count for the pool.  
`nodePoolId` |  `string` Deprecated. The name of the node pool to update. This field has been deprecated and replaced by the name field.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## ShieldedInstanceConfig

A set of Shielded Instance options. Fields  
---  
`enableIntegrityMonitoring` |  `boolean` Defines whether the instance has integrity monitoring enabled. Enables monitoring and attestation of the boot integrity of the instance. The attestation is performed against the integrity policy baseline. This baseline is initially derived from the implicitly trusted boot image when the instance is created.  
`enableSecureBoot` |  `boolean` Defines whether the instance has Secure Boot enabled. Secure Boot helps ensure that the system only runs authentic software by verifying the digital signature of all boot components, and halting the boot process if signature verification fails.  
  
## ShieldedNodes

Configuration of Shielded Nodes feature. Fields  
---  
`enabled` |  `boolean` Whether Shielded Nodes features are enabled on all nodes in this cluster.  
  
## StartIPRotationRequest

StartIPRotationRequest creates a new IP for the cluster and then performs a node upgrade on each node pool to point to the new IP. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster id) of the cluster to start IP rotation. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://developers.google.com/console/help/new/#projectnumber). This field has been deprecated and replaced by the name field.  
`rotateCredentials` |  `boolean` Whether to rotate credentials during IP rotation.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## Status

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). Fields  
---  
`code` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The status code, which should be an enum value of google.rpc.Code.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.  
  
## StatusCondition

StatusCondition describes why a cluster or a node pool has a certain status (e.g., ERROR or DEGRADED). Fields  
---  
`canonicalCode` |  `enum` Canonical code of the condition.  
Enum type. Can be one of the following:  
`OK` | Not an error; returned on success HTTP Mapping: 200 OK  
`CANCELLED` | The operation was cancelled, typically by the caller. HTTP Mapping: 499 Client Closed Request  
`UNKNOWN` | Unknown error. For example, this error may be returned when a `Status` value received from another address space belongs to an error space that is not known in this address space. Also errors raised by APIs that do not return enough error information may be converted to this error. HTTP Mapping: 500 Internal Server Error  
`INVALID_ARGUMENT` | The client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (e.g., a malformed file name). HTTP Mapping: 400 Bad Request  
`DEADLINE_EXCEEDED` | The deadline expired before the operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire. HTTP Mapping: 504 Gateway Timeout  
`NOT_FOUND` | Some requested entity (e.g., file or directory) was not found. Note to server developers: if a request is denied for an entire class of users, such as gradual feature rollout or undocumented allowlist, `NOT_FOUND` may be used. If a request is denied for some users within a class of users, such as user-based access control, `PERMISSION_DENIED` must be used. HTTP Mapping: 404 Not Found  
`ALREADY_EXISTS` | The entity that a client attempted to create (e.g., file or directory) already exists. HTTP Mapping: 409 Conflict  
`PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. `PERMISSION_DENIED` must not be used for rejections caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for those errors). `PERMISSION_DENIED` must not be used if the caller can not be identified (use `UNAUTHENTICATED` instead for those errors). This error code does not imply the request is valid or the requested entity exists or satisfies other pre-conditions. HTTP Mapping: 403 Forbidden  
`UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation. HTTP Mapping: 401 Unauthorized  
`RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space. HTTP Mapping: 429 Too Many Requests  
`FAILED_PRECONDITION` | The operation was rejected because the system is not in a state required for the operation's execution. For example, the directory to be deleted is non-empty, an rmdir operation is applied to a non-directory, etc. Service implementors can use the following guidelines to decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use `UNAVAILABLE` if the client can retry just the failing call. (b) Use `ABORTED` if the client should retry at a higher level. For example, when a client-specified test-and-set fails, indicating the client should restart a read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client should not retry until the system state has been explicitly fixed. For example, if an "rmdir" fails because the directory is non-empty, `FAILED_PRECONDITION` should be returned since the client should not retry unless the files are deleted from the directory. HTTP Mapping: 400 Bad Request  
`ABORTED` | The operation was aborted, typically due to a concurrency issue such as a sequencer check failure or transaction abort. See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`. HTTP Mapping: 409 Conflict  
`OUT_OF_RANGE` | The operation was attempted past the valid range. E.g., seeking or reading past end-of-file. Unlike `INVALID_ARGUMENT`, this error indicates a problem that may be fixed if the system state changes. For example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to read at an offset that is not in the range [0,2^32-1], but it will generate `OUT_OF_RANGE` if asked to read from an offset past the current file size. There is a fair bit of overlap between `FAILED_PRECONDITION` and `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error) when it applies so that callers who are iterating through a space can easily look for an `OUT_OF_RANGE` error to detect when they are done. HTTP Mapping: 400 Bad Request  
`UNIMPLEMENTED` | The operation is not implemented or is not supported/enabled in this service. HTTP Mapping: 501 Not Implemented  
`INTERNAL` | Internal errors. This means that some invariants expected by the underlying system have been broken. This error code is reserved for serious errors. HTTP Mapping: 500 Internal Server Error  
`UNAVAILABLE` | The service is currently unavailable. This is most likely a transient condition, which can be corrected by retrying with a backoff. Note that it is not always safe to retry non-idempotent operations. See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`. HTTP Mapping: 503 Service Unavailable  
`DATA_LOSS` | Unrecoverable data loss or corruption. HTTP Mapping: 500 Internal Server Error  
`code` |  `enum` Machine-friendly representation of the condition Deprecated. Use canonical_code instead.  
Enum type. Can be one of the following:  
`UNKNOWN` | UNKNOWN indicates a generic condition.  
`GCE_STOCKOUT` | GCE_STOCKOUT indicates that Google Compute Engine resources are temporarily unavailable.  
`GKE_SERVICE_ACCOUNT_DELETED` | GKE_SERVICE_ACCOUNT_DELETED indicates that the user deleted their robot service account.  
`GCE_QUOTA_EXCEEDED` | Google Compute Engine quota was exceeded.  
`SET_BY_OPERATOR` | Cluster state was manually changed by an SRE due to a system logic error.  
`CLOUD_KMS_KEY_ERROR` | Unable to perform an encrypt operation against the CloudKMS key used for etcd level encryption.  
`CA_EXPIRING` | Cluster CA is expiring soon.  
`message` |  `string` Human-friendly representation of the condition  
  
## TimeWindow

Represents an arbitrary window of time. Fields  
---  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time that the window ends. The end time should take place after the start time.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time that the window first starts.  
  
## UpdateClusterRequest

UpdateClusterRequest updates the settings of a cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`name` |  `string` The name (project, location, cluster) of the cluster to update. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`update` |  `object ([ClusterUpdate](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ClusterUpdate))` Required. A description of the update.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## UpdateMasterRequest

UpdateMasterRequest updates the master of the cluster. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`masterVersion` |  `string` Required. The Kubernetes version to change the master to. Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the default Kubernetes version  
`name` |  `string` The name (project, location, cluster) of the cluster to update. Specified in the format `projects/*/locations/*/clusters/*`.  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## UpdateNodePoolRequest

UpdateNodePoolRequests update a node pool's image and/or version. Fields  
---  
`clusterId` |  `string` Deprecated. The name of the cluster to upgrade. This field has been deprecated and replaced by the name field.  
`gvnic` |  `object ([VirtualNIC](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#VirtualNIC))` Enable or disable gvnic on the node pool.  
`imageType` |  `string` Required. The desired image type for the node pool.  
`kubeletConfig` |  `object ([NodeKubeletConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#NodeKubeletConfig))` Node kubelet configs.  
`linuxNodeConfig` |  `object ([LinuxNodeConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#LinuxNodeConfig))` Parameters that can be configured on Linux nodes.  
`locations[]` |  `string` The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the node pool's nodes should be located. Changing the locations for a node pool will result in nodes being either created or removed from the node pool, depending on whether locations are being added or removed.  
`name` |  `string` The name (project, location, cluster, node pool) of the node pool to update. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.  
`nodePoolId` |  `string` Deprecated. The name of the node pool to upgrade. This field has been deprecated and replaced by the name field.  
`nodeVersion` |  `string` Required. The Kubernetes version to change the nodes to (typically an upgrade). Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior: - "latest": picks the highest valid Kubernetes version - "1.X": picks the highest valid patch+gke.N patch in the 1.X version - "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version - "1.X.Y-gke.N": picks an explicit Kubernetes version - "-": picks the Kubernetes master version  
`projectId` |  `string` Deprecated. The Google Developers Console [project ID or project number](https://support.google.com/cloud/answer/6158840). This field has been deprecated and replaced by the name field.  
`upgradeSettings` |  `object ([UpgradeSettings](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#UpgradeSettings))` Upgrade settings control disruption and speed of the upgrade.  
`workloadMetadataConfig` |  `object ([WorkloadMetadataConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#WorkloadMetadataConfig))` The desired workload metadata config for the node pool.  
`zone` |  `string` Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.  
  
## UpgradeAvailableEvent

UpgradeAvailableEvent is a notification sent to customers when a new available version is released. Fields  
---  
`releaseChannel` |  `object ([ReleaseChannel](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#ReleaseChannel))` The release channel of the version. If empty, it means a non-channel release.  
`resource` |  `string` Optional relative path to the resource. For example, the relative path of the node pool.  
`resourceType` |  `enum` The resource type of the release version.  
Enum type. Can be one of the following:  
`UPGRADE_RESOURCE_TYPE_UNSPECIFIED` | Default value. This shouldn't be used.  
`MASTER` | Master / control plane  
`NODE_POOL` | Node pool  
`version` |  `string` The release version available for upgrade.  
  
## UpgradeEvent

UpgradeEvent is a notification sent to customers by the cluster server when a resource is upgrading. Fields  
---  
`currentVersion` |  `string` The current version before the upgrade.  
`operation` |  `string` The operation associated with this upgrade.  
`operationStartTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time when the operation was started.  
`resource` |  `string` Optional relative path to the resource. For example in node pool upgrades, the relative path of the node pool.  
`resourceType` |  `enum` The resource type that is upgrading.  
Enum type. Can be one of the following:  
`UPGRADE_RESOURCE_TYPE_UNSPECIFIED` | Default value. This shouldn't be used.  
`MASTER` | Master / control plane  
`NODE_POOL` | Node pool  
`targetVersion` |  `string` The target version for the upgrade.  
  
## UpgradeSettings

These upgrade settings control the level of parallelism and the level of disruption caused by an upgrade. maxUnavailable controls the number of nodes that can be simultaneously unavailable. maxSurge controls the number of additional nodes that can be added to the node pool temporarily for the time of the upgrade to increase the number of available nodes. (maxUnavailable + maxSurge) determines the level of parallelism (how many nodes are being upgraded at the same time). Note: upgrades inevitably introduce some disruption since workloads need to be moved from old nodes to new, upgraded ones. Even if maxUnavailable=0, this holds true. (Disruption stays within the limits of PodDisruptionBudget, if it is configured.) Consider a hypothetical node pool with 5 nodes having maxSurge=2, maxUnavailable=1. This means the upgrade process upgrades 3 nodes simultaneously. It creates 2 additional (upgraded) nodes, then it brings down 3 old (not yet upgraded) nodes at the same time. This ensures that there are always at least 4 nodes available. Fields  
---  
`maxSurge` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of nodes that can be created beyond the current size of the node pool during the upgrade process.  
`maxUnavailable` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of nodes that can be simultaneously unavailable during the upgrade process. A node is considered available if its status is Ready.  
  
## UsableSubnetwork

UsableSubnetwork resource returns the subnetwork name, its associated network and the primary CIDR range. Fields  
---  
`ipCidrRange` |  `string` The range of internal addresses that are owned by this subnetwork.  
`network` |  `string` Network Name. Example: projects/my-project/global/networks/my-network  
`secondaryIpRanges[]` |  `object ([UsableSubnetworkSecondaryRange](https://docs.cloud.google.com/workflows/docs/reference/googleapis/container/v1/Overview#UsableSubnetworkSecondaryRange))` Secondary IP ranges.  
`statusMessage` |  `string` A human readable status message representing the reasons for cases where the caller cannot use the secondary ranges under the subnet. For example if the secondary_ip_ranges is empty due to a permission issue, an insufficient permission message will be given by status_message.  
`subnetwork` |  `string` Subnetwork Name. Example: projects/my-project/regions/us-central1/subnetworks/my-subnet  
  
## UsableSubnetworkSecondaryRange

Secondary IP range of a usable subnetwork. Fields  
---  
`ipCidrRange` |  `string` The range of IP addresses belonging to this subnetwork secondary range.  
`rangeName` |  `string` The name associated with this subnetwork secondary range, used when adding an alias IP range to a VM instance.  
`status` |  `enum` This field is to determine the status of the secondary range programmably.  
Enum type. Can be one of the following:  
`UNKNOWN` | UNKNOWN is the zero value of the Status enum. It's not a valid status.  
`UNUSED` | UNUSED denotes that this range is unclaimed by any cluster.  
`IN_USE_SERVICE` | IN_USE_SERVICE denotes that this range is claimed by a cluster for services. It cannot be used for other clusters.  
`IN_USE_SHAREABLE_POD` | IN_USE_SHAREABLE_POD denotes this range was created by the network admin and is currently claimed by a cluster for pods. It can only be used by other clusters as a pod range.  
`IN_USE_MANAGED_POD` | IN_USE_MANAGED_POD denotes this range was created by GKE and is claimed for pods. It cannot be used for other clusters.  
  
## VerticalPodAutoscaling

VerticalPodAutoscaling contains global, per-cluster information required by Vertical Pod Autoscaler to automatically adjust the resources of pods controlled by it. Fields  
---  
`enabled` |  `boolean` Enables vertical pod autoscaling.  
  
## VirtualNIC

Configuration of gVNIC feature. Fields  
---  
`enabled` |  `boolean` Whether gVNIC features are enabled in the node pool.  
  
## WorkloadIdentityConfig

Configuration for the use of Kubernetes Service Accounts in GCP IAM policies. Fields  
---  
`workloadPool` |  `string` The workload pool to attach all Kubernetes service accounts to.  
  
## WorkloadMetadataConfig

WorkloadMetadataConfig defines the metadata configuration to expose to workloads on the node pool. Fields  
---  
`mode` |  `enum` Mode is the configuration for how to expose metadata to workloads running on the node pool.  
Enum type. Can be one of the following:  
`MODE_UNSPECIFIED` | Not set.  
`GCE_METADATA` | Expose all Compute Engine metadata to pods.  
`GKE_METADATA` | Run the GKE Metadata Server on this node. The GKE Metadata Server exposes a metadata API to workloads that is compatible with the V1 Compute Metadata APIs exposed by the Compute Engine and App Engine Metadata Servers. This feature can only be enabled if Workload Identity is enabled at the cluster level.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
