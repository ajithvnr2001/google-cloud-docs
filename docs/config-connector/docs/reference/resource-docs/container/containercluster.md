---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster/
title: ContainerCluster \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:41.662938+00:00
---

# ContainerCluster  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/container/containercluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ContainerCluster

**Note:** The ContainerCluster annotation can include [directives](https://docs.cloud.google.com/config-connector/docs/concepts/resources#object_metadata). If set to `true`, the `remove-default-node-pool` directive removes the default node pool created during cluster creation.**Note:** In `maintenancePolicy`, specify `startTime` and `endTime` in RFC3339 Zulu date format. Specify `recurrence` in RFC5545 RRULE format. GKE may accept other formats, but will return values in UTC, causing a permanent diff. For more details on how to debug and fix an issue which could lead to a permanent diff, please refer to the [Config Connector Troubleshooting page](https://docs.cloud.google.com/config-connector/docs/troubleshooting#resource_keeps_updating_every_5-15_mins)**Property** | **Value**  
---|---  
Google Cloud Service Name | Kubernetes Engine  
Google Cloud Service Documentation | [/kubernetes-engine/docs/](https://docs.cloud.google.com/kubernetes-engine/docs)  
Google Cloud REST Resource Name | v1.projects.locations.clusters  
Google Cloud REST Resource Documentation | [/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters)  
Config Connector Resource Short Names | containercluster  
gcpcontainercluster  
gcpcontainerclusters  
Config Connector Service Name | container.googleapis.com  
Config Connector Resource Fully Qualified Name | containerclusters.container.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Annotations

Fields  
---  
`cnrm.cloud.google.com/project-id`  
`cnrm.cloud.google.com/remove-default-node-pool`  
  
### Spec

#### Schema
    
    
    addonsConfig:
      cloudrunConfig:
        disabled: boolean
        loadBalancerType: string
      configConnectorConfig:
        enabled: boolean
      dnsCacheConfig:
        enabled: boolean
      gcePersistentDiskCsiDriverConfig:
        enabled: boolean
      gcpFilestoreCsiDriverConfig:
        enabled: boolean
      gcsFuseCsiDriverConfig:
        enabled: boolean
      gkeBackupAgentConfig:
        enabled: boolean
      horizontalPodAutoscaling:
        disabled: boolean
      httpLoadBalancing:
        disabled: boolean
      istioConfig:
        auth: string
        disabled: boolean
      kalmConfig:
        enabled: boolean
      networkPolicyConfig:
        disabled: boolean
      parallelstoreCsiDriverConfig:
        enabled: boolean
    allowNetAdmin: boolean
    authenticatorGroupsConfig:
      securityGroup: string
    binaryAuthorization:
      enabled: boolean
      evaluationMode: string
    clusterAutoscaling:
      autoProvisioningDefaults:
        bootDiskKMSKeyRef:
          external: string
          name: string
          namespace: string
        diskSize: integer
        imageType: string
        management:
          autoRepair: boolean
          autoUpgrade: boolean
          upgradeOptions:
          - autoUpgradeStartTime: string
            description: string
        minCpuPlatform: string
        oauthScopes:
        - string
        serviceAccountRef:
          external: string
          name: string
          namespace: string
        shieldedInstanceConfig:
          enableIntegrityMonitoring: boolean
          enableSecureBoot: boolean
        upgradeSettings:
          blueGreenSettings:
            nodePoolSoakDuration: string
            standardRolloutPolicy:
              batchNodeCount: integer
              batchPercentage: float
              batchSoakDuration: string
          maxSurge: integer
          maxUnavailable: integer
          strategy: string
      autoscalingProfile: string
      defaultComputeClassConfig:
        enabled: boolean
      enabled: boolean
      resourceLimits:
      - maximum: integer
        minimum: integer
        resourceType: string
    clusterIpv4Cidr: string
    clusterTelemetry:
      type: string
    confidentialNodes:
      confidentialInstanceType: string
      enabled: boolean
    controlPlaneEndpointsConfig:
      dnsEndpointConfig:
        allowExternalTraffic: boolean
        enableK8sTokensViaDns: boolean
      ipEndpointsConfig:
        enabled: boolean
    costManagementConfig:
      enabled: boolean
    databaseEncryption:
      keyName: string
      state: string
    datapathProvider: string
    defaultMaxPodsPerNode: integer
    defaultSnatStatus:
      disabled: boolean
    description: string
    disableL4LbFirewallReconciliation: boolean
    dnsConfig:
      clusterDns: string
      clusterDnsDomain: string
      clusterDnsScope: string
    enableAutopilot: boolean
    enableBinaryAuthorization: boolean
    enableCiliumClusterwideNetworkPolicy: boolean
    enableFqdnNetworkPolicy: boolean
    enableIntranodeVisibility: boolean
    enableK8sBetaApis:
      enabledApis:
      - string
    enableKubernetesAlpha: boolean
    enableL4IlbSubsetting: boolean
    enableLegacyAbac: boolean
    enableMultiNetworking: boolean
    enableShieldedNodes: boolean
    enableTpu: boolean
    gatewayApiConfig:
      channel: string
    identityServiceConfig:
      enabled: boolean
    inTransitEncryptionConfig: string
    initialNodeCount: integer
    ipAllocationPolicy:
      additionalIpRangesConfigs:
      - podIpv4RangeNames:
        - string
        status: string
        subnetworkRef:
          external: string
          name: string
          namespace: string
      additionalPodRangesConfig:
        podRangeNames:
        - string
      clusterIpv4CidrBlock: string
      clusterSecondaryRangeName: string
      podCidrOverprovisionConfig:
        disabled: boolean
      servicesIpv4CidrBlock: string
      servicesSecondaryRangeName: string
      stackType: string
    location: string
    loggingConfig:
      enableComponents:
      - string
    loggingService: string
    maintenancePolicy:
      dailyMaintenanceWindow:
        duration: string
        startTime: string
      maintenanceExclusion:
      - endTime: string
        exclusionName: string
        exclusionOptions:
          scope: string
        startTime: string
      recurringWindow:
        endTime: string
        recurrence: string
        startTime: string
    masterAuth:
      clientCertificate: string
      clientCertificateConfig:
        issueClientCertificate: boolean
      clientKey: string
      clusterCaCertificate: string
      password:
        value: string
        valueFrom:
          secretKeyRef:
            key: string
            name: string
      username: string
    masterAuthorizedNetworksConfig:
      cidrBlocks:
      - cidrBlock: string
        displayName: string
      gcpPublicCidrsAccessEnabled: boolean
    meshCertificates:
      enableCertificates: boolean
    minMasterVersion: string
    monitoringConfig:
      advancedDatapathObservabilityConfig:
      - enableMetrics: boolean
        relayMode: string
      enableComponents:
      - string
      managedPrometheus:
        enabled: boolean
    monitoringService: string
    networkPolicy:
      enabled: boolean
      provider: string
    networkRef:
      external: string
      name: string
      namespace: string
    networkingMode: string
    nodeConfig:
      advancedMachineFeatures:
        enableNestedVirtualization: boolean
        threadsPerCore: integer
      bootDiskKMSCryptoKeyRef:
        external: string
        name: string
        namespace: string
      confidentialNodes:
        confidentialInstanceType: string
        enabled: boolean
      containerdConfig:
        privateRegistryAccessConfig:
          certificateAuthorityDomainConfig:
          - fqdns:
            - string
            gcpSecretManagerCertificateConfig:
              secretRef:
                external: string
                name: string
                namespace: string
          enabled: boolean
        registryHosts:
        - hosts:
          - ca:
            - secretRef:
                external: string
                name: string
                namespace: string
            capabilities:
            - string
            client:
            - cert:
                secretRef:
                  external: string
                  name: string
                  namespace: string
              key:
                secretRef:
                  external: string
                  name: string
                  namespace: string
            dialTimeout: string
            header:
            - key: string
              value:
              - string
            host: string
            overridePath: boolean
          server: string
        writableCgroups:
          enabled: boolean
      diskSizeGb: integer
      diskType: string
      ephemeralStorageConfig:
        localSsdCount: integer
      ephemeralStorageLocalSsdConfig:
        dataCacheCount: integer
        localSsdCount: integer
      fastSocket:
        enabled: boolean
      gcfsConfig:
        enabled: boolean
      guestAccelerator:
      - count: integer
        gpuDriverInstallationConfig:
          gpuDriverVersion: string
        gpuPartitionSize: string
        gpuSharingConfig:
          gpuSharingStrategy: string
          maxSharedClientsPerGpu: integer
        type: string
      gvnic:
        enabled: boolean
      hostMaintenancePolicy:
        maintenanceInterval: string
      imageType: string
      kubeletConfig:
        cpuCfsQuota: boolean
        cpuCfsQuotaPeriod: string
        cpuManagerPolicy: string
        imageGcHighThresholdPercent: integer
        imageGcLowThresholdPercent: integer
        imageMaximumGcAge: string
        imageMinimumGcAge: string
        podPidsLimit: integer
      labels:
        string: string
      linuxNodeConfig:
        cgroupMode: string
        swapConfig:
          bootDiskProfile:
            swapSizeGib: integer
            swapSizePercent: integer
          dedicatedLocalSsdProfile:
            diskCount: integer
          enabled: boolean
          encryptionConfig:
            disabled: boolean
          ephemeralLocalSsdProfile:
            swapSizeGib: integer
            swapSizePercent: integer
        sysctls:
          string: string
      localNvmeSsdBlockConfig:
        localSsdCount: integer
      localSsdCount: integer
      loggingVariant: string
      machineType: string
      metadata:
        string: string
      minCpuPlatform: string
      nodeGroupRef:
        external: string
        name: string
        namespace: string
      oauthScopes:
      - string
      preemptible: boolean
      reservationAffinity:
        consumeReservationType: string
        key: string
        values:
        - string
      resourceLabels:
        string: string
      resourceManagerTags:
        string: string
      sandboxConfig:
        sandboxType: string
      serviceAccountRef:
        external: string
        name: string
        namespace: string
      shieldedInstanceConfig:
        enableIntegrityMonitoring: boolean
        enableSecureBoot: boolean
      soleTenantConfig:
        nodeAffinity:
        - key: string
          operator: string
          values:
          - string
      spot: boolean
      tags:
      - string
      taint:
      - effect: string
        key: string
        value: string
      workloadMetadataConfig:
        mode: string
        nodeMetadata: string
    nodeLocations:
    - string
    nodePoolAutoConfig:
      networkTags:
        tags:
        - string
      resourceManagerTags:
        string: string
    nodePoolDefaults:
      nodeConfigDefaults:
        gcfsConfig:
          enabled: boolean
        loggingVariant: string
    nodeVersion: string
    notificationConfig:
      pubsub:
        enabled: boolean
        filter:
          eventType:
          - string
        topicRef:
          external: string
          name: string
          namespace: string
    podSecurityPolicyConfig:
      enabled: boolean
    privateClusterConfig:
      enablePrivateEndpoint: boolean
      enablePrivateNodes: boolean
      masterGlobalAccessConfig:
        enabled: boolean
      masterIpv4CidrBlock: string
      peeringName: string
      privateEndpoint: string
      privateEndpointSubnetworkRef:
        external: string
        name: string
        namespace: string
      publicEndpoint: string
    privateIpv6GoogleAccess: string
    protectConfig:
      workloadConfig:
        auditMode: string
      workloadVulnerabilityMode: string
    releaseChannel:
      channel: string
    resourceID: string
    resourceUsageExportConfig:
      bigqueryDestination:
        datasetId: string
      enableNetworkEgressMetering: boolean
      enableResourceConsumptionMetering: boolean
    securityPostureConfig:
      mode: string
      vulnerabilityMode: string
    serviceExternalIpsConfig:
      enabled: boolean
    subnetworkRef:
      external: string
      name: string
      namespace: string
    verticalPodAutoscaling:
      enabled: boolean
    workloadIdentityConfig:
      identityNamespace: string
      workloadPool: string
    

Fields  
---  
`addonsConfig` _Optional_ |  `object` The configuration for addons supported by GKE.  
`addonsConfig.cloudrunConfig` _Optional_ |  `object` The status of the CloudRun addon. It is disabled by default. Set disabled = false to enable.  
`addonsConfig.cloudrunConfig.disabled` _Required*_ |  `boolean`  
`addonsConfig.cloudrunConfig.loadBalancerType` _Optional_ |  `string`  
`addonsConfig.configConnectorConfig` _Optional_ |  `object` The of the Config Connector addon.  
`addonsConfig.configConnectorConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.dnsCacheConfig` _Optional_ |  `object` The status of the NodeLocal DNSCache addon. It is disabled by default. Set enabled = true to enable.  
`addonsConfig.dnsCacheConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.gcePersistentDiskCsiDriverConfig` _Optional_ |  `object` Whether this cluster should enable the Google Compute Engine Persistent Disk Container Storage Interface (CSI) Driver. Set enabled = true to enable. The Compute Engine persistent disk CSI Driver is enabled by default on newly created clusters for the following versions: Linux clusters: GKE version 1.18.10-gke.2100 or later, or 1.19.3-gke.2100 or later.  
`addonsConfig.gcePersistentDiskCsiDriverConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.gcpFilestoreCsiDriverConfig` _Optional_ |  `object` The status of the Filestore CSI driver addon, which allows the usage of filestore instance as volumes. Defaults to disabled; set enabled = true to enable.  
`addonsConfig.gcpFilestoreCsiDriverConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.gcsFuseCsiDriverConfig` _Optional_ |  `object` The status of the GCS Fuse CSI driver addon, which allows the usage of GCS bucket as volumes. Defaults to disabled; set enabled = true to enable.  
`addonsConfig.gcsFuseCsiDriverConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.gkeBackupAgentConfig` _Optional_ |  `object` The status of the Backup for GKE Agent addon. It is disabled by default. Set enabled = true to enable.  
`addonsConfig.gkeBackupAgentConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.horizontalPodAutoscaling` _Optional_ |  `object` The status of the Horizontal Pod Autoscaling addon, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods. It ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service. It is enabled by default; set disabled = true to disable.  
`addonsConfig.horizontalPodAutoscaling.disabled` _Required*_ |  `boolean`  
`addonsConfig.httpLoadBalancing` _Optional_ |  `object` The status of the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster. It is enabled by default; set disabled = true to disable.  
`addonsConfig.httpLoadBalancing.disabled` _Required*_ |  `boolean`  
`addonsConfig.istioConfig` _Optional_ |  `object` The status of the Istio addon.  
`addonsConfig.istioConfig.auth` _Optional_ |  `string` The authentication type between services in Istio. Available options include AUTH_MUTUAL_TLS.  
`addonsConfig.istioConfig.disabled` _Required*_ |  `boolean` The status of the Istio addon, which makes it easy to set up Istio for services in a cluster. It is disabled by default. Set disabled = false to enable.  
`addonsConfig.kalmConfig` _Optional_ |  `object` Configuration for the KALM addon, which manages the lifecycle of k8s. It is disabled by default; Set enabled = true to enable.  
`addonsConfig.kalmConfig.enabled` _Required*_ |  `boolean`  
`addonsConfig.networkPolicyConfig` _Optional_ |  `object` Whether we should enable the network policy addon for the master. This must be enabled in order to enable network policy for the nodes. To enable this, you must also define a network_policy block, otherwise nothing will happen. It can only be disabled if the nodes already do not have network policies enabled. Defaults to disabled; set disabled = false to enable.  
`addonsConfig.networkPolicyConfig.disabled` _Required*_ |  `boolean`  
`addonsConfig.parallelstoreCsiDriverConfig` _Optional_ |  `object` The status of the Parallelstore CSI driver addon, which allows the usage of Parallelstore instance as volumes. Defaults to disabled; set enabled = true to enable.  
`addonsConfig.parallelstoreCsiDriverConfig.enabled` _Required*_ |  `boolean`  
`allowNetAdmin` _Optional_ |  `boolean` Enable NET_ADMIN for this cluster.  
`authenticatorGroupsConfig` _Optional_ |  `object` Configuration for the Google Groups for GKE feature.  
`authenticatorGroupsConfig.securityGroup` _Required*_ |  `string` The name of the RBAC security group for use with Google security groups in Kubernetes RBAC. Group name must be in format gke-security-groups@yourdomain.com.  
`binaryAuthorization` _Optional_ |  `object` Configuration options for the Binary Authorization feature.  
`binaryAuthorization.enabled` _Optional_ |  `boolean` DEPRECATED. Deprecated in favor of evaluation_mode. Enable Binary Authorization for this cluster.  
`binaryAuthorization.evaluationMode` _Optional_ |  `string` Mode of operation for Binary Authorization policy evaluation.  
`clusterAutoscaling` _Optional_ |  `object` Per-cluster configuration of Node Auto-Provisioning with Cluster Autoscaler to automatically adjust the size of the cluster and create/delete node pools based on the current needs of the cluster's workload. See the guide to using Node Auto-Provisioning for more details.  
`clusterAutoscaling.autoProvisioningDefaults` _Optional_ |  `object` Contains defaults for a node pool created by NAP.  
`clusterAutoscaling.autoProvisioningDefaults.bootDiskKMSKeyRef` _Optional_ |  `object` Immutable. The Customer Managed Encryption Key used to encrypt the boot disk attached to each node in the node pool.  
`clusterAutoscaling.autoProvisioningDefaults.bootDiskKMSKeyRef.external` _Optional_ |  `string` A reference to an externally managed KMSCryptoKey. Should be in the format `projects/[kms_project_id]/locations/[region]/keyRings/[key_ring_id]/cryptoKeys/[key]`.  
`clusterAutoscaling.autoProvisioningDefaults.bootDiskKMSKeyRef.name` _Optional_ |  `string` The `name` of a `KMSCryptoKey` resource.  
`clusterAutoscaling.autoProvisioningDefaults.bootDiskKMSKeyRef.namespace` _Optional_ |  `string` The `namespace` of a `KMSCryptoKey` resource.  
`clusterAutoscaling.autoProvisioningDefaults.diskSize` _Optional_ |  `integer` Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.  
`clusterAutoscaling.autoProvisioningDefaults.imageType` _Optional_ |  `string` The default image type used by NAP once a new node pool is being created.  
`clusterAutoscaling.autoProvisioningDefaults.management` _Optional_ |  `object` NodeManagement configuration for this NodePool.  
`clusterAutoscaling.autoProvisioningDefaults.management.autoRepair` _Optional_ |  `boolean` Specifies whether the node auto-repair is enabled for the node pool. If enabled, the nodes in this node pool will be monitored and, if they fail health checks too many times, an automatic repair action will be triggered.  
`clusterAutoscaling.autoProvisioningDefaults.management.autoUpgrade` _Optional_ |  `boolean` Specifies whether node auto-upgrade is enabled for the node pool. If enabled, node auto-upgrade helps keep the nodes in your node pool up to date with the latest release version of Kubernetes.  
`clusterAutoscaling.autoProvisioningDefaults.management.upgradeOptions` _Optional_ |  `list (object)` Specifies the Auto Upgrade knobs for the node pool.  
`clusterAutoscaling.autoProvisioningDefaults.management.upgradeOptions[]` _Optional_ |  `object`  
`clusterAutoscaling.autoProvisioningDefaults.management.upgradeOptions[].autoUpgradeStartTime` _Optional_ |  `string` This field is set when upgrades are about to commence with the approximate start time for the upgrades, in RFC3339 text format.  
`clusterAutoscaling.autoProvisioningDefaults.management.upgradeOptions[].description` _Optional_ |  `string` This field is set when upgrades are about to commence with the description of the upgrade.  
`clusterAutoscaling.autoProvisioningDefaults.minCpuPlatform` _Optional_ |  `string` Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform. Applicable values are the friendly names of CPU platforms, such as Intel Haswell.  
`clusterAutoscaling.autoProvisioningDefaults.oauthScopes` _Optional_ |  `list (string)` Scopes that are used by NAP when creating node pools.  
`clusterAutoscaling.autoProvisioningDefaults.oauthScopes[]` _Optional_ |  `string`  
`clusterAutoscaling.autoProvisioningDefaults.serviceAccountRef` _Optional_ |  `object`  
`clusterAutoscaling.autoProvisioningDefaults.serviceAccountRef.external` _Optional_ |  `string` The `email` field of an `IAMServiceAccount` resource.  
`clusterAutoscaling.autoProvisioningDefaults.serviceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`clusterAutoscaling.autoProvisioningDefaults.serviceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`clusterAutoscaling.autoProvisioningDefaults.shieldedInstanceConfig` _Optional_ |  `object` Shielded Instance options.  
`clusterAutoscaling.autoProvisioningDefaults.shieldedInstanceConfig.enableIntegrityMonitoring` _Optional_ |  `boolean` Immutable. Defines whether the instance has integrity monitoring enabled.  
`clusterAutoscaling.autoProvisioningDefaults.shieldedInstanceConfig.enableSecureBoot` _Optional_ |  `boolean` Immutable. Defines whether the instance has Secure Boot enabled.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings` _Optional_ |  `object` Specifies the upgrade settings for NAP created node pools.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings` _Optional_ |  `object` Settings for blue-green upgrade strategy.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings.nodePoolSoakDuration` _Optional_ |  `string` Time needed after draining entire blue pool. After this period, blue pool will be cleaned up. A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy` _Optional_ |  `object` Standard policy for the blue-green upgrade.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchNodeCount` _Optional_ |  `integer` Number of blue nodes to drain in a batch.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchPercentage` _Optional_ |  `float` Percentage of the bool pool nodes to drain in a batch. The range of this field should be (0.0, 1.0].  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchSoakDuration` _Optional_ |  `string` Soak time after each batch gets drained. A duration in seconds with up to nine fractional digits, ending with 's'. Example: "3.5s".  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.maxSurge` _Optional_ |  `integer` The maximum number of nodes that can be created beyond the current size of the node pool during the upgrade process.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.maxUnavailable` _Optional_ |  `integer` The maximum number of nodes that can be simultaneously unavailable during the upgrade process.  
`clusterAutoscaling.autoProvisioningDefaults.upgradeSettings.strategy` _Optional_ |  `string` Update strategy of the node pool.  
`clusterAutoscaling.autoscalingProfile` _Optional_ |  `string` Configuration options for the Autoscaling profile feature, which lets you choose whether the cluster autoscaler should optimize for resource utilization or resource availability when deciding to remove nodes from a cluster. Can be BALANCED or OPTIMIZE_UTILIZATION. Defaults to BALANCED.  
`clusterAutoscaling.defaultComputeClassConfig` _Optional_ |  `object` Default compute class is a configuration for default compute class.  
`clusterAutoscaling.defaultComputeClassConfig.enabled` _Required*_ |  `boolean` Enables default compute class.  
`clusterAutoscaling.enabled` _Optional_ |  `boolean` Whether node auto-provisioning is enabled. Resource limits for cpu and memory must be defined to enable node auto-provisioning.  
`clusterAutoscaling.resourceLimits` _Optional_ |  `list (object)` Global constraints for machine resources in the cluster. Configuring the cpu and memory types is required if node auto-provisioning is enabled. These limits will apply to node pool autoscaling in addition to node auto-provisioning.  
`clusterAutoscaling.resourceLimits[]` _Optional_ |  `object`  
`clusterAutoscaling.resourceLimits[].maximum` _Optional_ |  `integer` Maximum amount of the resource in the cluster.  
`clusterAutoscaling.resourceLimits[].minimum` _Optional_ |  `integer` Minimum amount of the resource in the cluster.  
`clusterAutoscaling.resourceLimits[].resourceType` _Required*_ |  `string` The type of the resource. For example, cpu and memory. See the guide to using Node Auto-Provisioning for a list of types.  
`clusterIpv4Cidr` _Optional_ |  `string` Immutable. The IP address range of the Kubernetes pods in this cluster in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8. This field will only work for routes-based clusters, where ip_allocation_policy is not defined.  
`clusterTelemetry` _Optional_ |  `object` Telemetry integration for the cluster.  
`clusterTelemetry.type` _Required*_ |  `string` Type of the integration.  
`confidentialNodes` _Optional_ |  `object` Immutable. Configuration for the confidential nodes feature, which makes nodes run on confidential VMs. Warning: This configuration can't be changed (or added/removed) after cluster creation without deleting and recreating the entire cluster.  
`confidentialNodes.confidentialInstanceType` _Optional_ |  `string` Immutable. Defines the type of technology used by the confidential node.  
`confidentialNodes.enabled` _Required*_ |  `boolean` Immutable. Whether Confidential Nodes feature is enabled for all nodes in this pool.  
`controlPlaneEndpointsConfig` _Optional_ |  `object` Configuration for all of the cluster's control plane endpoints. Currently supports only DNS endpoint configuration and disable IP endpoint. Other IP endpoint configurations are available in private_cluster_config.  
`controlPlaneEndpointsConfig.dnsEndpointConfig` _Optional_ |  `object` DNS endpoint configuration.  
`controlPlaneEndpointsConfig.dnsEndpointConfig.allowExternalTraffic` _Optional_ |  `boolean` Controls whether user traffic is allowed over this endpoint. Note that GCP-managed services may still use the endpoint even if this is false.  
`controlPlaneEndpointsConfig.dnsEndpointConfig.enableK8sTokensViaDns` _Optional_ |  `boolean` Controls whether the k8s token auth is allowed via DNS.  
`controlPlaneEndpointsConfig.ipEndpointsConfig` _Optional_ |  `object` IP endpoint configuration.  
`controlPlaneEndpointsConfig.ipEndpointsConfig.enabled` _Optional_ |  `boolean` Controls whether to allow direct IP access. When false, configuration of masterAuthorizedNetworksConfig, privateClusterConfig.enablePrivateEndpoint, privateClusterConfig.privateEndpointSubnetwork and privateClusterConfig.masterGlobalAccessConfig fields won't be used, and privateClusterConfig.privateEndpoint and privateClusterConfig.publicEndpoint fields won't be populated.  
`costManagementConfig` _Optional_ |  `object` Cost management configuration for the cluster.  
`costManagementConfig.enabled` _Required*_ |  `boolean` Whether to enable GKE cost allocation. When you enable GKE cost allocation, the cluster name and namespace of your GKE workloads appear in the labels field of the billing export to BigQuery. Defaults to false.  
`databaseEncryption` _Optional_ |  `object` Application-layer Secrets Encryption settings. The object format is {state = string, key_name = string}. Valid values of state are: "ENCRYPTED"; "DECRYPTED". key_name is the name of a CloudKMS key.  
`databaseEncryption.keyName` _Optional_ |  `string` The key to use to encrypt/decrypt secrets.  
`databaseEncryption.state` _Required*_ |  `string` ENCRYPTED, ALL_OBJECTS_ENCRYPTION_ENABLED or DECRYPTED.  
`datapathProvider` _Optional_ |  `string` Immutable. The desired datapath provider for this cluster. By default, uses the IPTables-based kube-proxy implementation.  
`defaultMaxPodsPerNode` _Optional_ |  `integer` Immutable. The default maximum number of pods per node in this cluster. This doesn't work on "routes-based" clusters, clusters that don't have IP Aliasing enabled.  
`defaultSnatStatus` _Optional_ |  `object` Whether the cluster disables default in-node sNAT rules. In-node sNAT rules will be disabled when defaultSnatStatus is disabled.  
`defaultSnatStatus.disabled` _Required*_ |  `boolean` When disabled is set to false, default IP masquerade rules will be applied to the nodes to prevent sNAT on cluster internal traffic.  
`description` _Optional_ |  `string` Immutable. Description of the cluster.  
`disableL4LbFirewallReconciliation` _Optional_ |  `boolean` Whether the cluster disables L4 LB firewall reconciliation.  
`dnsConfig` _Optional_ |  `object` Immutable. Configuration for Cloud DNS for Kubernetes Engine.  
`dnsConfig.clusterDns` _Optional_ |  `string` Which in-cluster DNS provider should be used.  
`dnsConfig.clusterDnsDomain` _Optional_ |  `string` The suffix used for all cluster service records.  
`dnsConfig.clusterDnsScope` _Optional_ |  `string` The scope of access to cluster DNS records.  
`enableAutopilot` _Optional_ |  `boolean` Immutable. Enable Autopilot for this cluster.  
`enableBinaryAuthorization` _Optional_ |  `boolean` DEPRECATED. Deprecated in favor of binary_authorization. Enable Binary Authorization for this cluster. If enabled, all container images will be validated by Google Binary Authorization.  
`enableCiliumClusterwideNetworkPolicy` _Optional_ |  `boolean` Whether Cilium cluster-wide network policy is enabled on this cluster.  
`enableFqdnNetworkPolicy` _Optional_ |  `boolean` Whether FQDN Network Policy is enabled on this cluster.  
`enableIntranodeVisibility` _Optional_ |  `boolean` Whether Intra-node visibility is enabled for this cluster. This makes same node pod to pod traffic visible for VPC network.  
`enableK8sBetaApis` _Optional_ |  `object` Configuration for Kubernetes Beta APIs.  
`enableK8sBetaApis.enabledApis` _Required*_ |  `list (string)` Enabled Kubernetes Beta APIs.  
`enableK8sBetaApis.enabledApis[]` _Required*_ |  `string`  
`enableKubernetesAlpha` _Optional_ |  `boolean` Immutable. Whether to enable Kubernetes Alpha features for this cluster. Note that when this option is enabled, the cluster cannot be upgraded and will be automatically deleted after 30 days.  
`enableL4IlbSubsetting` _Optional_ |  `boolean` Whether L4ILB Subsetting is enabled for this cluster.  
`enableLegacyAbac` _Optional_ |  `boolean` Whether the ABAC authorizer is enabled for this cluster. When enabled, identities in the system, including service accounts, nodes, and controllers, will have statically granted permissions beyond those provided by the RBAC configuration or IAM. Defaults to false.  
`enableMultiNetworking` _Optional_ |  `boolean` Immutable. Whether multi-networking is enabled for this cluster.  
`enableShieldedNodes` _Optional_ |  `boolean` Enable Shielded Nodes features on all nodes in this cluster. Defaults to true.  
`enableTpu` _Optional_ |  `boolean` Immutable. Whether to enable Cloud TPU resources in this cluster.  
`gatewayApiConfig` _Optional_ |  `object` Configuration for GKE Gateway API controller.  
`gatewayApiConfig.channel` _Required*_ |  `string` The Gateway API release channel to use for Gateway API.  
`identityServiceConfig` _Optional_ |  `object` Configuration for Identity Service which allows customers to use external identity providers with the K8S API.  
`identityServiceConfig.enabled` _Optional_ |  `boolean` Whether to enable the Identity Service component.  
`inTransitEncryptionConfig` _Optional_ |  `string` In-transit encryption options for the cluster. Possible values are IN_TRANSIT_ENCRYPTION_CONFIG_UNSPECIFIED, IN_TRANSIT_ENCRYPTION_DISABLED, IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT  
`initialNodeCount` _Optional_ |  `integer` Immutable. The number of nodes to create in this cluster's default node pool. In regional or multi-zonal clusters, this is the number of nodes per zone. Must be set if node_pool is not set. If you're using google_container_node_pool objects with no default node pool, you'll need to set this to a value of at least 1, alongside setting remove_default_node_pool to true.  
`ipAllocationPolicy` _Optional_ |  `object` Immutable. Configuration of cluster IP allocation for VPC-native clusters. Adding this block enables IP aliasing, making the cluster VPC-native instead of routes-based.  
`ipAllocationPolicy.additionalIpRangesConfigs` _Optional_ |  `list (object)` AdditionalIPRangesConfig is the configuration for additional pod secondary ranges supporting the ClusterUpdate message. Each AdditionalIPRangesConfig corresponds to a single subnetwork.  
`ipAllocationPolicy.additionalIpRangesConfigs[]` _Optional_ |  `object`  
`ipAllocationPolicy.additionalIpRangesConfigs[].podIpv4RangeNames` _Optional_ |  `list (string)` List of secondary ranges names within this subnetwork that can be used for pod IPs.  
`ipAllocationPolicy.additionalIpRangesConfigs[].podIpv4RangeNames[]` _Optional_ |  `string`  
`ipAllocationPolicy.additionalIpRangesConfigs[].status` _Optional_ |  `string` Status of the subnetwork, If in draining status, subnet will not be selected for new node pools.  
`ipAllocationPolicy.additionalIpRangesConfigs[].subnetworkRef` _Required*_ |  `object` The subnetwork path for the additional IP range. Format: projects/{project}/regions/{region}/subnetworks/{subnetwork}.  
`ipAllocationPolicy.additionalIpRangesConfigs[].subnetworkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeSubnetwork resource. Should be in the format "projects/{{projectID}}/regions/{{region}}/subnetworks/{{subnetworkID}}".  
`ipAllocationPolicy.additionalIpRangesConfigs[].subnetworkRef.name` _Optional_ |  `string` The name of a ComputeSubnetwork resource.  
`ipAllocationPolicy.additionalIpRangesConfigs[].subnetworkRef.namespace` _Optional_ |  `string` The namespace of a ComputeSubnetwork resource.  
`ipAllocationPolicy.additionalPodRangesConfig` _Optional_ |  `object` AdditionalPodRangesConfig is the configuration for additional pod secondary ranges supporting the ClusterUpdate message.  
`ipAllocationPolicy.additionalPodRangesConfig.podRangeNames` _Required*_ |  `list (string)` Name for pod secondary ipv4 range which has the actual range defined ahead.  
`ipAllocationPolicy.additionalPodRangesConfig.podRangeNames[]` _Required*_ |  `string`  
`ipAllocationPolicy.clusterIpv4CidrBlock` _Optional_ |  `string` Immutable. The IP address range for the cluster pod IPs. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.  
`ipAllocationPolicy.clusterSecondaryRangeName` _Optional_ |  `string` Immutable. The name of the existing secondary range in the cluster's subnetwork to use for pod IP addresses. Alternatively, cluster_ipv4_cidr_block can be used to automatically create a GKE-managed one.  
`ipAllocationPolicy.podCidrOverprovisionConfig` _Optional_ |  `object` Immutable. Configuration for cluster level pod cidr overprovision. Default is disabled=false.  
`ipAllocationPolicy.podCidrOverprovisionConfig.disabled` _Required*_ |  `boolean`  
`ipAllocationPolicy.servicesIpv4CidrBlock` _Optional_ |  `string` Immutable. The IP address range of the services IPs in this cluster. Set to blank to have a range chosen with the default size. Set to /netmask (e.g. /14) to have a range chosen with a specific netmask. Set to a CIDR notation (e.g. 10.96.0.0/14) from the RFC-1918 private networks (e.g. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) to pick a specific range to use.  
`ipAllocationPolicy.servicesSecondaryRangeName` _Optional_ |  `string` Immutable. The name of the existing secondary range in the cluster's subnetwork to use for service ClusterIPs. Alternatively, services_ipv4_cidr_block can be used to automatically create a GKE-managed one.  
`ipAllocationPolicy.stackType` _Optional_ |  `string` Immutable. The IP Stack type of the cluster. Choose between IPV4 and IPV4_IPV6. Default type is IPV4 Only if not set.  
`location` _Required_ |  `string` Immutable. The location (region or zone) in which the cluster master will be created, as well as the default node location. If you specify a zone (such as us-central1-a), the cluster will be a zonal cluster with a single cluster master. If you specify a region (such as us-west1), the cluster will be a regional cluster with multiple masters spread across zones in the region, and with default node locations in those zones as well.  
`loggingConfig` _Optional_ |  `object` Logging configuration for the cluster.  
`loggingConfig.enableComponents` _Required*_ |  `list (string)` GKE components exposing logs. Valid values include SYSTEM_COMPONENTS, APISERVER, CONTROLLER_MANAGER, SCHEDULER, and WORKLOADS.  
`loggingConfig.enableComponents[]` _Required*_ |  `string`  
`loggingService` _Optional_ |  `string` The logging service that the cluster should write logs to. Available options include logging.googleapis.com(Legacy Stackdriver), logging.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Logging), and none. Defaults to logging.googleapis.com/kubernetes.  
`maintenancePolicy` _Optional_ |  `object` The maintenance policy to use for the cluster.  
`maintenancePolicy.dailyMaintenanceWindow` _Optional_ |  `object` Time window specified for daily maintenance operations. Specify start_time in RFC3339 format "HH:MM", where HH : [00-23] and MM : [00-59] GMT.  
`maintenancePolicy.dailyMaintenanceWindow.duration` _Optional_ |  `string`  
`maintenancePolicy.dailyMaintenanceWindow.startTime` _Required*_ |  `string`  
`maintenancePolicy.maintenanceExclusion` _Optional_ |  `list (object)` Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.  
`maintenancePolicy.maintenanceExclusion[]` _Optional_ |  `object`  
`maintenancePolicy.maintenanceExclusion[].endTime` _Required*_ |  `string`  
`maintenancePolicy.maintenanceExclusion[].exclusionName` _Required*_ |  `string`  
`maintenancePolicy.maintenanceExclusion[].exclusionOptions` _Optional_ |  `object` Maintenance exclusion related options.  
`maintenancePolicy.maintenanceExclusion[].exclusionOptions.scope` _Required*_ |  `string` The scope of automatic upgrades to restrict in the exclusion window.  
`maintenancePolicy.maintenanceExclusion[].startTime` _Required*_ |  `string`  
`maintenancePolicy.recurringWindow` _Optional_ |  `object` Time window for recurring maintenance operations.  
`maintenancePolicy.recurringWindow.endTime` _Required*_ |  `string`  
`maintenancePolicy.recurringWindow.recurrence` _Required*_ |  `string`  
`maintenancePolicy.recurringWindow.startTime` _Required*_ |  `string`  
`masterAuth` _Optional_ |  `object` DEPRECATED. Basic authentication was removed for GKE cluster versions >= 1.19. The authentication information for accessing the Kubernetes master. Some values in this block are only returned by the API if your service account has permission to get credentials for your GKE cluster. If you see an unexpected diff unsetting your client cert, ensure you have the container.clusters.getCredentials permission.  
`masterAuth.clientCertificate` _Optional_ |  `string` Base64 encoded public certificate used by clients to authenticate to the cluster endpoint.  
`masterAuth.clientCertificateConfig` _Optional_ |  `object` Immutable. Whether client certificate authorization is enabled for this cluster.  
`masterAuth.clientCertificateConfig.issueClientCertificate` _Required*_ |  `boolean` Immutable. Whether client certificate authorization is enabled for this cluster.  
`masterAuth.clientKey` _Optional_ |  `string` Base64 encoded private key used by clients to authenticate to the cluster endpoint.  
`masterAuth.clusterCaCertificate` _Optional_ |  `string` Base64 encoded public certificate that is the root of trust for the cluster.  
`masterAuth.password` _Optional_ |  `object` The password to use for HTTP basic authentication when accessing the Kubernetes master endpoint.  
`masterAuth.password.value` _Optional_ |  `string` Value of the field. Cannot be used if 'valueFrom' is specified.  
`masterAuth.password.valueFrom` _Optional_ |  `object` Source for the field's value. Cannot be used if 'value' is specified.  
`masterAuth.password.valueFrom.secretKeyRef` _Optional_ |  `object` Reference to a value with the given key in the given Secret in the resource's namespace.  
`masterAuth.password.valueFrom.secretKeyRef.key` _Required*_ |  `string` Key that identifies the value to be extracted.  
`masterAuth.password.valueFrom.secretKeyRef.name` _Required*_ |  `string` Name of the Secret to extract a value from.  
`masterAuth.username` _Optional_ |  `string` The username to use for HTTP basic authentication when accessing the Kubernetes master endpoint. If not present basic auth will be disabled.  
`masterAuthorizedNetworksConfig` _Optional_ |  `object` The desired configuration options for master authorized networks. Omit the nested cidr_blocks attribute to disallow external access (except the cluster node IPs, which GKE automatically whitelists).  
`masterAuthorizedNetworksConfig.cidrBlocks` _Optional_ |  `list (object)` External networks that can access the Kubernetes cluster master through HTTPS.  
`masterAuthorizedNetworksConfig.cidrBlocks[]` _Optional_ |  `object`  
`masterAuthorizedNetworksConfig.cidrBlocks[].cidrBlock` _Required*_ |  `string` External network that can access Kubernetes master through HTTPS. Must be specified in CIDR notation.  
`masterAuthorizedNetworksConfig.cidrBlocks[].displayName` _Optional_ |  `string` Field for users to identify CIDR blocks.  
`masterAuthorizedNetworksConfig.gcpPublicCidrsAccessEnabled` _Optional_ |  `boolean` Whether master is accessible via Google Compute Engine Public IP addresses.  
`meshCertificates` _Optional_ |  `object` If set, and enable_certificates=true, the GKE Workload Identity Certificates controller and node agent will be deployed in the cluster.  
`meshCertificates.enableCertificates` _Required*_ |  `boolean` When enabled the GKE Workload Identity Certificates controller and node agent will be deployed in the cluster.  
`minMasterVersion` _Optional_ |  `string` The minimum version of the master. GKE will auto-update the master to new versions, so this does not guarantee the current master version--use the read-only master_version field to obtain that. If unset, the cluster's version will be set by GKE to the version of the most recent official release (which is not necessarily the latest version).  
`monitoringConfig` _Optional_ |  `object` Monitoring configuration for the cluster.  
`monitoringConfig.advancedDatapathObservabilityConfig` _Optional_ |  `list (object)` Configuration of Advanced Datapath Observability features.  
`monitoringConfig.advancedDatapathObservabilityConfig[]` _Optional_ |  `object`  
`monitoringConfig.advancedDatapathObservabilityConfig[].enableMetrics` _Required*_ |  `boolean` Whether or not the advanced datapath metrics are enabled.  
`monitoringConfig.advancedDatapathObservabilityConfig[].relayMode` _Optional_ |  `string` Mode used to make Relay available.  
`monitoringConfig.enableComponents` _Optional_ |  `list (string)` GKE components exposing metrics. Valid values include SYSTEM_COMPONENTS, APISERVER, SCHEDULER, CONTROLLER_MANAGER, STORAGE, HPA, POD, DAEMONSET, DEPLOYMENT, STATEFULSET and WORKLOADS.  
`monitoringConfig.enableComponents[]` _Optional_ |  `string`  
`monitoringConfig.managedPrometheus` _Optional_ |  `object` Configuration for Google Cloud Managed Services for Prometheus.  
`monitoringConfig.managedPrometheus.enabled` _Required*_ |  `boolean` Whether or not the managed collection is enabled.  
`monitoringService` _Optional_ |  `string` The monitoring service that the cluster should write metrics to. Automatically send metrics from pods in the cluster to the Google Cloud Monitoring API. VM metrics will be collected by Google Compute Engine regardless of this setting Available options include monitoring.googleapis.com(Legacy Stackdriver), monitoring.googleapis.com/kubernetes(Stackdriver Kubernetes Engine Monitoring), and none. Defaults to monitoring.googleapis.com/kubernetes.  
`networkPolicy` _Optional_ |  `object` Configuration options for the NetworkPolicy feature.  
`networkPolicy.enabled` _Required*_ |  `boolean` Whether network policy is enabled on the cluster.  
`networkPolicy.provider` _Optional_ |  `string` The selected network policy provider. Defaults to PROVIDER_UNSPECIFIED.  
`networkRef` _Optional_ |  `object` ComputeNetworkRef is a reference to a GCP ComputeNetwork.  
`networkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNetwork resource. Should be in the format "projects/{{projectID}}/global/networks/{{networkID}}".  
`networkRef.name` _Optional_ |  `string` The name of a ComputeNetwork resource.  
`networkRef.namespace` _Optional_ |  `string` The namespace of a ComputeNetwork resource.  
`networkingMode` _Optional_ |  `string` Immutable. Determines whether alias IPs or routes will be used for pod IPs in the cluster.  
`nodeConfig` _Optional_ |  `object` Immutable. The configuration of the nodepool.  
`nodeConfig.advancedMachineFeatures` _Optional_ |  `object` Immutable. Specifies options for controlling advanced machine features.  
`nodeConfig.advancedMachineFeatures.enableNestedVirtualization` _Optional_ |  `boolean` Immutable. Whether or not to enable nested virtualization (defaults to false).  
`nodeConfig.advancedMachineFeatures.threadsPerCore` _Optional_ |  `integer` Immutable. The number of threads per physical core. To disable simultaneous multithreading (SMT) set this to 1. If unset, the maximum number of threads supported per core by the underlying processor is assumed.  
`nodeConfig.bootDiskKMSCryptoKeyRef` _Optional_ |  `object`  
`nodeConfig.bootDiskKMSCryptoKeyRef.external` _Optional_ |  `string` A reference to an externally managed KMSCryptoKey. Should be in the format `projects/[kms_project_id]/locations/[region]/keyRings/[key_ring_id]/cryptoKeys/[key]`.  
`nodeConfig.bootDiskKMSCryptoKeyRef.name` _Optional_ |  `string` The `name` of a `KMSCryptoKey` resource.  
`nodeConfig.bootDiskKMSCryptoKeyRef.namespace` _Optional_ |  `string` The `namespace` of a `KMSCryptoKey` resource.  
`nodeConfig.confidentialNodes` _Optional_ |  `object` Immutable. Configuration for the confidential nodes feature, which makes nodes run on confidential VMs. Warning: This configuration can't be changed (or added/removed) after pool creation without deleting and recreating the entire pool.  
`nodeConfig.confidentialNodes.confidentialInstanceType` _Optional_ |  `string` Immutable. Defines the type of technology used by the confidential node.  
`nodeConfig.confidentialNodes.enabled` _Required*_ |  `boolean` Immutable. Whether Confidential Nodes feature is enabled for all nodes in this pool.  
`nodeConfig.containerdConfig` _Optional_ |  `object` Parameters for containerd customization.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig` _Optional_ |  `object` Parameters for private container registries configuration.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig` _Optional_ |  `list (object)` Private registry access configuration.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].fqdns` _Optional_ |  `list (string)` List of fully qualified domain names (FQDN). Specifying port is supported. Wildcards are NOT supported.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].fqdns[]` _Optional_ |  `string`  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].gcpSecretManagerCertificateConfig` _Optional_ |  `object` Google Secret Manager (GCP) certificate configuration.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].gcpSecretManagerCertificateConfig.secretRef` _Optional_ |  `object` SecretRef is a reference to a SecretManagerSecretVersion resource.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].gcpSecretManagerCertificateConfig.secretRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].gcpSecretManagerCertificateConfig.secretRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.certificateAuthorityDomainConfig[].gcpSecretManagerCertificateConfig.secretRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.privateRegistryAccessConfig.enabled` _Optional_ |  `boolean` Private registry access is enabled.  
`nodeConfig.containerdConfig.registryHosts` _Optional_ |  `list (object)` Configures containerd registry host configuration. Each registryHosts entry represents a hosts.toml file.  
`nodeConfig.containerdConfig.registryHosts[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.registryHosts[].hosts` _Optional_ |  `list (object)` Configures a list of host-specific configurations for the server.  
`nodeConfig.containerdConfig.registryHosts[].hosts[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca` _Optional_ |  `list (object)` Configures the registry host certificate.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca[].secretRef` _Optional_ |  `object` Reference to SecretManagerSecretVersion for the CA certificate.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca[].secretRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca[].secretRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].ca[].secretRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].capabilities` _Optional_ |  `list (string)` Represent the capabilities of the registry host, specifying what operations a host is capable of performing.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].capabilities[]` _Optional_ |  `string`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client` _Optional_ |  `list (object)` Configures the registry host client certificate and key.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].cert` _Optional_ |  `object` Configures the client certificate.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].cert.secretRef` _Optional_ |  `object` Reference to SecretManagerSecretVersion for the client certificate.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].cert.secretRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].cert.secretRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].cert.secretRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].key` _Optional_ |  `object` Configures the client private key.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].key.secretRef` _Optional_ |  `object` Reference to SecretManagerSecretVersion for the client key.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].key.secretRef.external` _Optional_ |  `string` If provided must be in the format `projects/*/secrets/*/versions/*`.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].key.secretRef.name` _Optional_ |  `string` The `name` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].client[].key.secretRef.namespace` _Optional_ |  `string` The `metadata.namespace` field of a `SecretManagerSecretVersion` resource.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].dialTimeout` _Optional_ |  `string` Specifies the maximum duration allowed for a connection attempt to complete.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].header` _Optional_ |  `list (object)` Configures the registry host headers.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].header[]` _Optional_ |  `object`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].header[].key` _Optional_ |  `string` Configures the header key.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].header[].value` _Optional_ |  `list (string)` Configures the header value.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].header[].value[]` _Optional_ |  `string`  
`nodeConfig.containerdConfig.registryHosts[].hosts[].host` _Optional_ |  `string` Configures the registry host/mirror.  
`nodeConfig.containerdConfig.registryHosts[].hosts[].overridePath` _Optional_ |  `boolean` Indicate the host's API root endpoint is defined in the URL path rather than by the API specification.  
`nodeConfig.containerdConfig.registryHosts[].server` _Optional_ |  `string` Defines the host name of the registry server.  
`nodeConfig.containerdConfig.writableCgroups` _Optional_ |  `object` Parameters for writable cgroups configuration.  
`nodeConfig.containerdConfig.writableCgroups.enabled` _Optional_ |  `boolean` Whether writable cgroups are enabled.  
`nodeConfig.diskSizeGb` _Optional_ |  `integer` Immutable. Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB.  
`nodeConfig.diskType` _Optional_ |  `string` Immutable. Type of the disk attached to each node. Such as pd-standard, pd-balanced or pd-ssd.  
`nodeConfig.ephemeralStorageConfig` _Optional_ |  `object` Immutable. Parameters for the ephemeral storage filesystem. If unspecified, ephemeral storage is backed by the boot disk.  
`nodeConfig.ephemeralStorageConfig.localSsdCount` _Required*_ |  `integer` Immutable. Number of local SSDs to use to back ephemeral storage. Uses NVMe interfaces. Each local SSD must be 375 or 3000 GB in size, and all local SSDs must share the same size.  
`nodeConfig.ephemeralStorageLocalSsdConfig` _Optional_ |  `object` Immutable. Parameters for the ephemeral storage filesystem. If unspecified, ephemeral storage is backed by the boot disk.  
`nodeConfig.ephemeralStorageLocalSsdConfig.dataCacheCount` _Optional_ |  `integer` Immutable. Number of local SSDs to be utilized for GKE Data Cache. Uses NVMe interfaces.  
`nodeConfig.ephemeralStorageLocalSsdConfig.localSsdCount` _Required*_ |  `integer` Immutable. Number of local SSDs to use to back ephemeral storage. Uses NVMe interfaces. Each local SSD must be 375 or 3000 GB in size, and all local SSDs must share the same size.  
`nodeConfig.fastSocket` _Optional_ |  `object` Enable or disable NCCL Fast Socket in the node pool.  
`nodeConfig.fastSocket.enabled` _Required*_ |  `boolean` Whether or not NCCL Fast Socket is enabled.  
`nodeConfig.gcfsConfig` _Optional_ |  `object` Immutable. GCFS configuration for this node.  
`nodeConfig.gcfsConfig.enabled` _Required*_ |  `boolean` Whether or not GCFS is enabled.  
`nodeConfig.guestAccelerator` _Optional_ |  `list (object)` Immutable. List of the type and count of accelerator cards attached to the instance.  
`nodeConfig.guestAccelerator[]` _Optional_ |  `object`  
`nodeConfig.guestAccelerator[].count` _Required*_ |  `integer` Immutable. The number of the accelerator cards exposed to an instance.  
`nodeConfig.guestAccelerator[].gpuDriverInstallationConfig` _Optional_ |  `object` Immutable. Configuration for auto installation of GPU driver.  
`nodeConfig.guestAccelerator[].gpuDriverInstallationConfig.gpuDriverVersion` _Required*_ |  `string` Immutable. Mode for how the GPU driver is installed.  
`nodeConfig.guestAccelerator[].gpuPartitionSize` _Optional_ |  `string` Immutable. Size of partitions to create on the GPU. Valid values are described in the NVIDIA mig user guide (https://docs.nvidia.com/datacenter/tesla/mig-user-guide/#partitioning).  
`nodeConfig.guestAccelerator[].gpuSharingConfig` _Optional_ |  `object` Immutable. Configuration for GPU sharing.  
`nodeConfig.guestAccelerator[].gpuSharingConfig.gpuSharingStrategy` _Required*_ |  `string` Immutable. The type of GPU sharing strategy to enable on the GPU node. Possible values are described in the API package (https://pkg.go.dev/google.golang.org/api/container/v1#GPUSharingConfig).  
`nodeConfig.guestAccelerator[].gpuSharingConfig.maxSharedClientsPerGpu` _Required*_ |  `integer` Immutable. The maximum number of containers that can share a GPU.  
`nodeConfig.guestAccelerator[].type` _Required*_ |  `string` Immutable. The accelerator type resource name.  
`nodeConfig.gvnic` _Optional_ |  `object` Immutable. Enable or disable gvnic in the node pool.  
`nodeConfig.gvnic.enabled` _Required*_ |  `boolean` Immutable. Whether or not gvnic is enabled.  
`nodeConfig.hostMaintenancePolicy` _Optional_ |  `object` Immutable. The maintenance policy for the hosts on which the GKE VMs run on.  
`nodeConfig.hostMaintenancePolicy.maintenanceInterval` _Required*_ |  `string` Immutable. .  
`nodeConfig.imageType` _Optional_ |  `string` The image type to use for this node. Note that for a given image type, the latest version of it will be used.  
`nodeConfig.kubeletConfig` _Optional_ |  `object` Node kubelet configs.  
`nodeConfig.kubeletConfig.cpuCfsQuota` _Optional_ |  `boolean` Enable CPU CFS quota enforcement for containers that specify CPU limits.  
`nodeConfig.kubeletConfig.cpuCfsQuotaPeriod` _Optional_ |  `string` Set the CPU CFS quota period value 'cpu.cfs_period_us'.  
`nodeConfig.kubeletConfig.cpuManagerPolicy` _Required*_ |  `string` Control the CPU management policy on the node.  
`nodeConfig.kubeletConfig.imageGcHighThresholdPercent` _Optional_ |  `integer` Percent of disk usage after which image garbage collection is always run.  
`nodeConfig.kubeletConfig.imageGcLowThresholdPercent` _Optional_ |  `integer` Percent of disk usage before which image garbage collection is never run. Lowest disk usage to garbage collect to.  
`nodeConfig.kubeletConfig.imageMaximumGcAge` _Optional_ |  `string` Maximum age an image can be unused before it is garbage collected.  
`nodeConfig.kubeletConfig.imageMinimumGcAge` _Optional_ |  `string` Minimum age for an unused image before it is garbage collected.  
`nodeConfig.kubeletConfig.podPidsLimit` _Optional_ |  `integer` Controls the maximum number of processes allowed to run in a pod.  
`nodeConfig.labels` _Optional_ |  `map (key: string, value: string)` Immutable. The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node.  
`nodeConfig.linuxNodeConfig` _Optional_ |  `object` Parameters that can be configured on Linux nodes.  
`nodeConfig.linuxNodeConfig.cgroupMode` _Optional_ |  `string` cgroupMode specifies the cgroup mode to be used on the node.  
`nodeConfig.linuxNodeConfig.swapConfig` _Optional_ |  `object` SwapConfig specifies the swap configuration on the nodes.  
`nodeConfig.linuxNodeConfig.swapConfig.bootDiskProfile` _Optional_ |  `object` BootDiskProfile specifies the configuration for swap on the node's boot disk.  
`nodeConfig.linuxNodeConfig.swapConfig.bootDiskProfile.swapSizeGib` _Optional_ |  `integer` Swap size in GiB.  
`nodeConfig.linuxNodeConfig.swapConfig.bootDiskProfile.swapSizePercent` _Optional_ |  `integer` Swap size as a percentage of the boot disk size.  
`nodeConfig.linuxNodeConfig.swapConfig.dedicatedLocalSsdProfile` _Optional_ |  `object` DedicatedLocalSsdProfile specifies the configuration for swap on dedicated local NVMe SSDs.  
`nodeConfig.linuxNodeConfig.swapConfig.dedicatedLocalSsdProfile.diskCount` _Optional_ |  `integer` The number of physical local NVMe SSD disks to attach.  
`nodeConfig.linuxNodeConfig.swapConfig.enabled` _Optional_ |  `boolean` Whether swap is enabled.  
`nodeConfig.linuxNodeConfig.swapConfig.encryptionConfig` _Optional_ |  `object` EncryptionConfig specifies the encryption configuration for swap.  
`nodeConfig.linuxNodeConfig.swapConfig.encryptionConfig.disabled` _Optional_ |  `boolean` If true, swap space will not be encrypted.  
`nodeConfig.linuxNodeConfig.swapConfig.ephemeralLocalSsdProfile` _Optional_ |  `object` EphemeralLocalSsdProfile specifies the configuration for swap on ephemeral local SSDs.  
`nodeConfig.linuxNodeConfig.swapConfig.ephemeralLocalSsdProfile.swapSizeGib` _Optional_ |  `integer` Swap size in GiB.  
`nodeConfig.linuxNodeConfig.swapConfig.ephemeralLocalSsdProfile.swapSizePercent` _Optional_ |  `integer` Swap size as a percentage of the ephemeral local SSD capacity.  
`nodeConfig.linuxNodeConfig.sysctls` _Optional_ |  `map (key: string, value: string)` The Linux kernel parameters to be applied to the nodes and all pods running on the nodes.  
`nodeConfig.localNvmeSsdBlockConfig` _Optional_ |  `object` Immutable. Parameters for raw-block local NVMe SSDs.  
`nodeConfig.localNvmeSsdBlockConfig.localSsdCount` _Required*_ |  `integer` Immutable. Number of raw-block local NVMe SSD disks to be attached to the node. Each local SSD is 375 GB in size.  
`nodeConfig.localSsdCount` _Optional_ |  `integer` Immutable. The number of local SSD disks to be attached to the node.  
`nodeConfig.loggingVariant` _Optional_ |  `string` Type of logging agent that is used as the default value for node pools in the cluster. Valid values include DEFAULT and MAX_THROUGHPUT.  
`nodeConfig.machineType` _Optional_ |  `string` Immutable. The name of a Google Compute Engine machine type.  
`nodeConfig.metadata` _Optional_ |  `map (key: string, value: string)` Immutable. The metadata key/value pairs assigned to instances in the cluster.  
`nodeConfig.minCpuPlatform` _Optional_ |  `string` Immutable. Minimum CPU platform to be used by this instance. The instance may be scheduled on the specified or newer CPU platform.  
`nodeConfig.nodeGroupRef` _Optional_ |  `object` Immutable. Setting this field will assign instances of this pool to run on the specified node group. This is useful for running workloads on sole tenant nodes.  
`nodeConfig.nodeGroupRef.external` _Optional_ |  `string` A reference to an externally managed ComputeNodeGroup resource. Should be in the format "projects/{{projectID}}/zones/{{zone}}/nodeGroups/{{nodeGroupID}}".  
`nodeConfig.nodeGroupRef.name` _Optional_ |  `string` The name of a ComputeNodeGroup resource.  
`nodeConfig.nodeGroupRef.namespace` _Optional_ |  `string` The namespace of a ComputeNodeGroup resource.  
`nodeConfig.oauthScopes` _Optional_ |  `list (string)` Immutable. The set of Google API scopes to be made available on all of the node VMs.  
`nodeConfig.oauthScopes[]` _Optional_ |  `string`  
`nodeConfig.preemptible` _Optional_ |  `boolean` Immutable. Whether the nodes are created as preemptible VM instances.  
`nodeConfig.reservationAffinity` _Optional_ |  `object` Immutable. The reservation affinity configuration for the node pool.  
`nodeConfig.reservationAffinity.consumeReservationType` _Required*_ |  `string` Immutable. Corresponds to the type of reservation consumption.  
`nodeConfig.reservationAffinity.key` _Optional_ |  `string` Immutable. The label key of a reservation resource.  
`nodeConfig.reservationAffinity.values` _Optional_ |  `list (string)` Immutable. The label values of the reservation resource.  
`nodeConfig.reservationAffinity.values[]` _Optional_ |  `string`  
`nodeConfig.resourceLabels` _Optional_ |  `map (key: string, value: string)` The GCE resource labels (a map of key/value pairs) to be applied to the node pool.  
`nodeConfig.resourceManagerTags` _Optional_ |  `map (key: string, value: string)` The resource manager tags (a map of key/value pairs) to be applied to GKE nodes. Keys must be in the format tagKeys/{tag_key_id}, and values are in the format tagValues/{tag_value_id}.  
`nodeConfig.sandboxConfig` _Optional_ |  `object` Immutable. Sandbox configuration for this node.  
`nodeConfig.sandboxConfig.sandboxType` _Required*_ |  `string` Type of the sandbox to use for the node (e.g. 'gvisor').  
`nodeConfig.serviceAccountRef` _Optional_ |  `object`  
`nodeConfig.serviceAccountRef.external` _Optional_ |  `string` The `email` field of an `IAMServiceAccount` resource.  
`nodeConfig.serviceAccountRef.name` _Optional_ |  `string` Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names  
`nodeConfig.serviceAccountRef.namespace` _Optional_ |  `string` Namespace of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/  
`nodeConfig.shieldedInstanceConfig` _Optional_ |  `object` Immutable. Shielded Instance options.  
`nodeConfig.shieldedInstanceConfig.enableIntegrityMonitoring` _Optional_ |  `boolean` Immutable. Defines whether the instance has integrity monitoring enabled.  
`nodeConfig.shieldedInstanceConfig.enableSecureBoot` _Optional_ |  `boolean` Immutable. Defines whether the instance has Secure Boot enabled.  
`nodeConfig.soleTenantConfig` _Optional_ |  `object` Immutable. Node affinity options for sole tenant node pools.  
`nodeConfig.soleTenantConfig.nodeAffinity` _Required*_ |  `list (object)` Immutable. .  
`nodeConfig.soleTenantConfig.nodeAffinity[]` _Required*_ |  `object`  
`nodeConfig.soleTenantConfig.nodeAffinity[].key` _Required*_ |  `string` Immutable. .  
`nodeConfig.soleTenantConfig.nodeAffinity[].operator` _Required*_ |  `string` Immutable. .  
`nodeConfig.soleTenantConfig.nodeAffinity[].values` _Required*_ |  `list (string)` Immutable. .  
`nodeConfig.soleTenantConfig.nodeAffinity[].values[]` _Required*_ |  `string`  
`nodeConfig.spot` _Optional_ |  `boolean` Immutable. Whether the nodes are created as spot VM instances.  
`nodeConfig.tags` _Optional_ |  `list (string)` The list of instance tags applied to all nodes.  
`nodeConfig.tags[]` _Optional_ |  `string`  
`nodeConfig.taint` _Optional_ |  `list (object)` List of Kubernetes taints to be applied to each node.  
`nodeConfig.taint[]` _Optional_ |  `object`  
`nodeConfig.taint[].effect` _Required*_ |  `string` Effect for taint.  
`nodeConfig.taint[].key` _Required*_ |  `string` Key for taint.  
`nodeConfig.taint[].value` _Required*_ |  `string` Value for taint.  
`nodeConfig.workloadMetadataConfig` _Optional_ |  `object` Immutable. The workload metadata configuration for this node.  
`nodeConfig.workloadMetadataConfig.mode` _Optional_ |  `string` Mode is the configuration for how to expose metadata to workloads running on the node.  
`nodeConfig.workloadMetadataConfig.nodeMetadata` _Optional_ |  `string` DEPRECATED. Deprecated in favor of mode. NodeMetadata is the configuration for how to expose metadata to the workloads running on the node.  
`nodeLocations` _Optional_ |  `list (string)` The list of zones in which the cluster's nodes are located. Nodes must be in the region of their regional cluster or in the same region as their cluster's zone for zonal clusters. If this is specified for a zonal cluster, omit the cluster's zone.  
`nodeLocations[]` _Optional_ |  `string`  
`nodePoolAutoConfig` _Optional_ |  `object` Node pool configs that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.  
`nodePoolAutoConfig.networkTags` _Optional_ |  `object` Collection of Compute Engine network tags that can be applied to a node's underlying VM instance.  
`nodePoolAutoConfig.networkTags.tags` _Optional_ |  `list (string)` List of network tags applied to auto-provisioned node pools.  
`nodePoolAutoConfig.networkTags.tags[]` _Optional_ |  `string`  
`nodePoolAutoConfig.resourceManagerTags` _Optional_ |  `map (key: string, value: string)` Collection of Resource Manager tags to be applied to GKE Autopilot node pools. Keys must be in the format tagKeys/{tag_key_id}, and values are in the format tagValues/{tag_value_id}.  
`nodePoolDefaults` _Optional_ |  `object` The default nodel pool settings for the entire cluster.  
`nodePoolDefaults.nodeConfigDefaults` _Optional_ |  `object` Subset of NodeConfig message that has defaults.  
`nodePoolDefaults.nodeConfigDefaults.gcfsConfig` _Optional_ |  `object` GCFS configuration for this node.  
`nodePoolDefaults.nodeConfigDefaults.gcfsConfig.enabled` _Required*_ |  `boolean` Whether or not GCFS is enabled.  
`nodePoolDefaults.nodeConfigDefaults.loggingVariant` _Optional_ |  `string` Type of logging agent that is used as the default value for node pools in the cluster. Valid values include DEFAULT and MAX_THROUGHPUT.  
`nodeVersion` _Optional_ |  `string`  
`notificationConfig` _Optional_ |  `object` The notification config for sending cluster upgrade notifications.  
`notificationConfig.pubsub` _Required*_ |  `object` Notification config for Cloud Pub/Sub.  
`notificationConfig.pubsub.enabled` _Required*_ |  `boolean` Whether or not the notification config is enabled.  
`notificationConfig.pubsub.filter` _Optional_ |  `object` Allows filtering to one or more specific event types. If event types are present, those and only those event types will be transmitted to the cluster. Other types will be skipped. If no filter is specified, or no event types are present, all event types will be sent.  
`notificationConfig.pubsub.filter.eventType` _Required*_ |  `list (string)` Can be used to filter what notifications are sent. Valid values include include UPGRADE_AVAILABLE_EVENT, UPGRADE_EVENT and SECURITY_BULLETIN_EVENT.  
`notificationConfig.pubsub.filter.eventType[]` _Required*_ |  `string`  
`notificationConfig.pubsub.topicRef` _Optional_ |  `object` The PubSubTopic to send the notification to.  
`notificationConfig.pubsub.topicRef.external` _Optional_ |  `string` A reference to an externally managed PubSubTopic resource. Should be in the format "projects/{{projectID}}/topics/{{topicID}}".  
`notificationConfig.pubsub.topicRef.name` _Optional_ |  `string` The name of a PubSubTopic resource.  
`notificationConfig.pubsub.topicRef.namespace` _Optional_ |  `string` The namespace of a PubSubTopic resource.  
`podSecurityPolicyConfig` _Optional_ |  `object` Configuration for the PodSecurityPolicy feature.  
`podSecurityPolicyConfig.enabled` _Required*_ |  `boolean` Enable the PodSecurityPolicy controller for this cluster. If enabled, pods must be valid under a PodSecurityPolicy to be created.  
`privateClusterConfig` _Optional_ |  `object` Configuration for private clusters, clusters with private nodes.  
`privateClusterConfig.enablePrivateEndpoint` _Optional_ |  `boolean` When true, the cluster's private endpoint is used as the cluster endpoint and access through the public endpoint is disabled. When false, either endpoint can be used.  
`privateClusterConfig.enablePrivateNodes` _Optional_ |  `boolean` Enables the private cluster feature, creating a private endpoint on the cluster. In a private cluster, nodes only have RFC 1918 private addresses and communicate with the master's private endpoint via private networking.  
`privateClusterConfig.masterGlobalAccessConfig` _Optional_ |  `object` Controls cluster master global access settings.  
`privateClusterConfig.masterGlobalAccessConfig.enabled` _Required*_ |  `boolean` Whether the cluster master is accessible globally or not.  
`privateClusterConfig.masterIpv4CidrBlock` _Optional_ |  `string` Immutable. The IP range in CIDR notation to use for the hosted master network. This range will be used for assigning private IP addresses to the cluster master(s) and the ILB VIP. This range must not overlap with any other ranges in use within the cluster's network, and it must be a /28 subnet. See Private Cluster Limitations for more details. This field only applies to private clusters, when enable_private_nodes is true.  
`privateClusterConfig.peeringName` _Optional_ |  `string` The name of the peering between this cluster and the Google owned VPC.  
`privateClusterConfig.privateEndpoint` _Optional_ |  `string` The internal IP address of this cluster's master endpoint.  
`privateClusterConfig.privateEndpointSubnetworkRef` _Optional_ |  `object` Immutable. Subnetwork in cluster's network where master's endpoint will be provisioned.  
`privateClusterConfig.privateEndpointSubnetworkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeSubnetwork resource. Should be in the format "projects/{{projectID}}/regions/{{region}}/subnetworks/{{subnetworkID}}".  
`privateClusterConfig.privateEndpointSubnetworkRef.name` _Optional_ |  `string` The name of a ComputeSubnetwork resource.  
`privateClusterConfig.privateEndpointSubnetworkRef.namespace` _Optional_ |  `string` The namespace of a ComputeSubnetwork resource.  
`privateClusterConfig.publicEndpoint` _Optional_ |  `string` The external IP address of this cluster's master endpoint.  
`privateIpv6GoogleAccess` _Optional_ |  `string` The desired state of IPv6 connectivity to Google Services. By default, no private IPv6 access to or from Google Services (all access will be via IPv4).  
`protectConfig` _Optional_ |  `object` Enable/Disable Protect API features for the cluster.  
`protectConfig.workloadConfig` _Optional_ |  `object` WorkloadConfig defines which actions are enabled for a cluster's workload configurations.  
`protectConfig.workloadConfig.auditMode` _Required*_ |  `string` Sets which mode of auditing should be used for the cluster's workloads. Accepted values are DISABLED, BASIC.  
`protectConfig.workloadVulnerabilityMode` _Optional_ |  `string` Sets which mode to use for Protect workload vulnerability scanning feature. Accepted values are DISABLED, BASIC.  
`releaseChannel` _Optional_ |  `object` Configuration options for the Release channel feature, which provide more control over automatic upgrades of your GKE clusters. Note that removing this field from your config will not unenroll it. Instead, use the "UNSPECIFIED" channel.  
`releaseChannel.channel` _Required*_ |  `string` The selected release channel. Accepted values are: * UNSPECIFIED: Not set. * RAPID: Weekly upgrade cadence; Early testers and developers who requires new features. * REGULAR: Multiple per month upgrade cadence; Production users who need features not yet offered in the Stable channel. * STABLE: Every few months upgrade cadence; Production users who need stability above all else, and for whom frequent upgrades are too risky.  
`resourceID` _Optional_ |  `string` Immutable. Optional. The name of the resource. Used for creation and acquisition. When unset, the value of `metadata.name` is used as the default.  
`resourceUsageExportConfig` _Optional_ |  `object` Configuration for the ResourceUsageExportConfig feature.  
`resourceUsageExportConfig.bigqueryDestination` _Required*_ |  `object` Parameters for using BigQuery as the destination of resource usage export.  
`resourceUsageExportConfig.bigqueryDestination.datasetId` _Required*_ |  `string` The ID of a BigQuery Dataset.  
`resourceUsageExportConfig.enableNetworkEgressMetering` _Optional_ |  `boolean` Whether to enable network egress metering for this cluster. If enabled, a daemonset will be created in the cluster to meter network egress traffic.  
`resourceUsageExportConfig.enableResourceConsumptionMetering` _Optional_ |  `boolean` Whether to enable resource consumption metering on this cluster. When enabled, a table will be created in the resource export BigQuery dataset to store resource consumption data. The resulting table can be joined with the resource usage table or with BigQuery billing export. Defaults to true.  
`securityPostureConfig` _Optional_ |  `object` Defines the config needed to enable/disable features for the Security Posture API.  
`securityPostureConfig.mode` _Optional_ |  `string` Sets the mode of the Kubernetes security posture API's off-cluster features. Available options include DISABLED and BASIC.  
`securityPostureConfig.vulnerabilityMode` _Optional_ |  `string` Sets the mode of the Kubernetes security posture API's workload vulnerability scanning. Available options include VULNERABILITY_DISABLED and VULNERABILITY_BASIC.  
`serviceExternalIpsConfig` _Optional_ |  `object` If set, and enabled=true, services with external ips field will not be blocked.  
`serviceExternalIpsConfig.enabled` _Required*_ |  `boolean` When enabled, services with exterenal ips specified will be allowed.  
`subnetworkRef` _Optional_ |  `object` ComputeSubnetworkRef is a reference to a GCP ComputeSubnetwork.  
`subnetworkRef.external` _Optional_ |  `string` A reference to an externally managed ComputeSubnetwork resource. Should be in the format "projects/{{projectID}}/regions/{{region}}/subnetworks/{{subnetworkID}}".  
`subnetworkRef.name` _Optional_ |  `string` The name of a ComputeSubnetwork resource.  
`subnetworkRef.namespace` _Optional_ |  `string` The namespace of a ComputeSubnetwork resource.  
`verticalPodAutoscaling` _Optional_ |  `object` Vertical Pod Autoscaling automatically adjusts the resources of pods controlled by it.  
`verticalPodAutoscaling.enabled` _Required*_ |  `boolean` Enables vertical pod autoscaling.  
`workloadIdentityConfig` _Optional_ |  `object` Configuration for the use of Kubernetes Service Accounts in GCP IAM policies.  
`workloadIdentityConfig.identityNamespace` _Optional_ |  `string` DEPRECATED. This field will be removed in a future major release as it has been deprecated in the API. Use `workloadPool` instead; `workloadPool` field will supersede this field. Enables workload identity.  
`workloadIdentityConfig.workloadPool` _Optional_ |  `string` The workload pool to attach all Kubernetes service accounts to.  
  
* Field is required when parent field is specified

### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    endpoint: string
    labelFingerprint: string
    masterVersion: string
    observedGeneration: integer
    observedState:
      controlPlaneEndpointsConfig:
        dnsEndpointConfig:
          endpoint: string
      masterAuth:
        clientCertificate: string
        clusterCaCertificate: string
      privateClusterConfig:
        privateEndpoint: string
        publicEndpoint: string
    operation: string
    selfLink: string
    servicesIpv4Cidr: string
    tpuIpv4CidrBlock: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the ContainerCluster's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`endpoint` |  `string` The IP address of this cluster's Kubernetes master.  
`labelFingerprint` |  `string` The fingerprint of the set of labels for this cluster.  
`masterVersion` |  `string` The current version of the master in the cluster. This may be different than the min_master_version set in the config if the master has been updated by GKE.  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`observedState` |  `object` The observed state of the underlying GCP resource.  
`observedState.controlPlaneEndpointsConfig` |  `object` Configuration for all of the cluster's control plane endpoints. Currently supports only DNS endpoint configuration and disable IP endpoint. Other IP endpoint configurations are available in private_cluster_config.  
`observedState.controlPlaneEndpointsConfig.dnsEndpointConfig` |  `object` DNS endpoint configuration.  
`observedState.controlPlaneEndpointsConfig.dnsEndpointConfig.endpoint` |  `string` The cluster's DNS endpoint.  
`observedState.masterAuth` |  `object` DEPRECATED. Basic authentication was removed for GKE cluster versions >= 1.19. The authentication information for accessing the Kubernetes master. Some values in this block are only returned by the API if your service account has permission to get credentials for your GKE cluster. If you see an unexpected diff unsetting your client cert, ensure you have the container.clusters.getCredentials permission.  
`observedState.masterAuth.clientCertificate` |  `string` Base64 encoded public certificate used by clients to authenticate to the cluster endpoint.  
`observedState.masterAuth.clusterCaCertificate` |  `string` Base64 encoded public certificate that is the root of trust for the cluster.  
`observedState.privateClusterConfig` |  `object` Configuration for private clusters, clusters with private nodes.  
`observedState.privateClusterConfig.privateEndpoint` |  `string` The internal IP address of this cluster's master endpoint.  
`observedState.privateClusterConfig.publicEndpoint` |  `string` The external IP address of this cluster's master endpoint.  
`operation` |  `string`  
`selfLink` |  `string` Server-defined URL for the resource.  
`servicesIpv4Cidr` |  `string` The IP address range of the Kubernetes services in this cluster, in CIDR notation (e.g. 1.2.3.4/29). Service addresses are typically put in the last /16 from the container CIDR.  
`tpuIpv4CidrBlock` |  `string` The IP address range of the Cloud TPUs in this cluster, in CIDR notation (e.g. 1.2.3.4/29).  
  
## Sample YAML(s)

### Autopilot Cluster
    
    
    apiVersion: container.cnrm.cloud.google.com/v1beta1
    kind: ContainerCluster
    metadata:
      name: containercluster-sample-autopilot
    spec:
      description: An autopilot cluster.
      enableAutopilot: true
      location: us-west1
      releaseChannel:
        channel: REGULAR
    

### In Transit Encryption Container Cluster
    
    
    apiVersion: container.cnrm.cloud.google.com/v1beta1
    kind: ContainerCluster
    metadata:
      labels:
        availability: dev
        target-audience: development
      name: containercluster-sample-intransit
    spec:
      description: Minimal VPC-Native cluster with Dataplane V2 and In-Transit Encryption.
      location: us-central1-a
      initialNodeCount: 1
      networkingMode: VPC_NATIVE
      ipAllocationPolicy:
        clusterIpv4CidrBlock: /20
        servicesIpv4CidrBlock: /20
      datapathProvider: ADVANCED_DATAPATH
      inTransitEncryptionConfig: IN_TRANSIT_ENCRYPTION_INTER_NODE_TRANSPARENT # or IN_TRANSIT_ENCRYPTION_DISABLED to disable
    

### Routes Based Container Cluster
    
    
    apiVersion: container.cnrm.cloud.google.com/v1beta1
    kind: ContainerCluster
    metadata:
      labels:
        availability: dev
        target-audience: development
      name: containercluster-sample-routesbased
    spec:
      description: A routes-based cluster confined to one zone configured for development.
      location: us-central1-a
      initialNodeCount: 1
      networkingMode: ROUTES
      clusterIpv4Cidr: 10.96.0.0/14
      masterAuthorizedNetworksConfig:
        cidrBlocks:
          - displayName: Trusted external network
            cidrBlock: 10.2.0.0/16
      addonsConfig:
        gcePersistentDiskCsiDriverConfig:
          enabled: true
        kalmConfig:
          enabled: true
        horizontalPodAutoscaling:
          disabled: true
        httpLoadBalancing:
          disabled: false
      loggingConfig:
        enableComponents:
          - "SYSTEM_COMPONENTS"
          - "WORKLOADS"
      monitoringConfig:
        enableComponents:
          - "SYSTEM_COMPONENTS"
      workloadIdentityConfig:
        # Replace ${PROJECT_ID?} with your project ID.
        workloadPool: "${PROJECT_ID?}.svc.id.goog"
    

### Vpc Native Container Cluster
    
    
    apiVersion: container.cnrm.cloud.google.com/v1beta1
    kind: ContainerCluster
    metadata:
      labels:
        availability: high
        target-audience: production
      name: containercluster-sample-vpcnative
    spec:
      description: A large regional VPC-native cluster set up with special networking considerations.
      location: us-central1
      initialNodeCount: 1
      defaultMaxPodsPerNode: 16
      nodeLocations:
        - us-central1-a
        - us-central1-b
        - us-central1-c
        - us-central1-f
      workloadIdentityConfig:
        # Workload Identity supports only a single namespace based on your project name.
        # Replace ${PROJECT_ID?} below with your project ID.
        workloadPool: ${PROJECT_ID?}.svc.id.goog
      networkingMode: VPC_NATIVE
      networkRef:
        name: containercluster-dep-vpcnative
      subnetworkRef:
        name: containercluster-dep-vpcnative
      ipAllocationPolicy:
        servicesSecondaryRangeName: servicesrange
        clusterSecondaryRangeName: clusterrange
      clusterAutoscaling:
        enabled: true
        autoscalingProfile: BALANCED
        resourceLimits:
        - resourceType: cpu
          maximum: 100
          minimum: 10
        - resourceType: memory
          maximum: 1000
          minimum: 100
      maintenancePolicy:
        dailyMaintenanceWindow:
          startTime: 00:00
      releaseChannel:
        channel: STABLE
      notificationConfig:
        pubsub:
          enabled: true
          topicRef:
            name: containercluster-dep-vpcnative
      enableBinaryAuthorization: true
      enableIntranodeVisibility: true
      enableShieldedNodes: true
      addonsConfig:
        networkPolicyConfig:
          disabled: false
        dnsCacheConfig:
          enabled: true
        configConnectorConfig:
          enabled: true
      networkPolicy:
        enabled: true
      podSecurityPolicyConfig:
        enabled: true
      verticalPodAutoscaling:
        enabled: true
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeNetwork
    metadata:
      name: containercluster-dep-vpcnative
    spec:
      routingMode: REGIONAL
      autoCreateSubnetworks: false
    ---
    apiVersion: compute.cnrm.cloud.google.com/v1beta1
    kind: ComputeSubnetwork
    metadata:
      name: containercluster-dep-vpcnative
    spec:
      ipCidrRange: 10.2.0.0/16
      region: us-central1
      networkRef:
        name: containercluster-dep-vpcnative
      secondaryIpRange:
      - rangeName: servicesrange
        ipCidrRange: 10.3.0.0/16
      - rangeName: clusterrange
        ipCidrRange: 10.4.0.0/16
    ---
    apiVersion: pubsub.cnrm.cloud.google.com/v1beta1
    kind: PubSubTopic
    metadata:
      name: containercluster-dep-vpcnative
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
