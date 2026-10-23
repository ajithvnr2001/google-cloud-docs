---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies/
title: Restrict actions on GKE resources using custom organization policies \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:05.554388+00:00
---

# Restrict actions on GKE resources using custom organization policies  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Restrict actions on GKE resources using custom organization policies Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `container.googleapis.com/Cluster`
  * `container.googleapis.com/NodePool`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

## Limitations

The following limitations apply to using the Organization Policy Service with GKE:

  * The following output-only fields aren't supported:

    * `projects.locations.clusters.masterAuth.clientKey`
    * `projects.locations.clusters.masterAuth.password`
  * You can't conditionally enforce organization policies based on the [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) that are attached to GKE clusters.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Ensure that you know your [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).



### Required roles

To get the permissions that you need to use organization policies with GKE, ask your administrator to grant you the following IAM roles: 

  * Create and manage organization policies: [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) on the organization, folder, or project 
  * Create a cluster: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## GKE supported resources

The following table lists the GKE resources that you can reference in custom constraints. 

Resource | Field  
---|---  
container.googleapis.com/Cluster |  `resource.addonsConfig.cloudRunConfig.disabled`  
`resource.addonsConfig.cloudRunConfig.loadBalancerType`  
`resource.addonsConfig.configConnectorConfig.enabled`  
`resource.addonsConfig.dnsCacheConfig.enabled`  
`resource.addonsConfig.gcePersistentDiskCsiDriverConfig.enabled`  
`resource.addonsConfig.gcpFilestoreCsiDriverConfig.enabled`  
`resource.addonsConfig.gcsFuseCsiDriverConfig.enabled`  
`resource.addonsConfig.gkeBackupAgentConfig.enabled`  
`resource.addonsConfig.highScaleCheckpointingConfig.enabled`  
`resource.addonsConfig.horizontalPodAutoscaling.disabled`  
`resource.addonsConfig.httpLoadBalancing.disabled`  
`resource.addonsConfig.kubernetesDashboard.disabled`  
`resource.addonsConfig.networkPolicyConfig.disabled`  
`resource.addonsConfig.parallelstoreCsiDriverConfig.enabled`  
`resource.addonsConfig.rayOperatorConfig.enabled`  
`resource.addonsConfig.rayOperatorConfig.rayClusterLoggingConfig.enabled`  
`resource.addonsConfig.rayOperatorConfig.rayClusterMonitoringConfig.enabled`  
`resource.addonsConfig.statefulHAConfig.enabled`  
`resource.addonsConfig.wizSensorConfig.enabled`  
`resource.alphaClusterFeatureGates`  
`resource.anonymousAuthenticationConfig.mode`  
`resource.authenticatorGroupsConfig.enabled`  
`resource.authenticatorGroupsConfig.securityGroup`  
`resource.autopilot.enabled`  
`resource.autopilot.privilegedAdmissionConfig.allowlistPaths`  
`resource.autopilot.workloadPolicyConfig.allowNetAdmin`  
`resource.autopilot.workloadPolicyConfig.autopilotCompatibilityAuditingEnabled`  
`resource.autoscaling.autoprovisioningLocations`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.bootDiskKmsKey`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.diskSizeGb`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.diskType`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.imageType`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.insecureKubeletReadonlyPortEnabled`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.management.autoRepair`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.management.autoUpgrade`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.minCpuPlatform`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.oauthScopes`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.serviceAccount`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.shieldedInstanceConfig.enableIntegrityMonitoring`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.shieldedInstanceConfig.enableSecureBoot`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.blueGreenSettings.nodePoolSoakDuration`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchNodeCount`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchPercentage`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchSoakDuration`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.maxSurge`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.maxUnavailable`  
`resource.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.strategy`  
`resource.autoscaling.autoscalingProfile`  
`resource.autoscaling.enableNodeAutoprovisioning`  
`resource.autoscaling.resourceLimits.maximum`  
`resource.autoscaling.resourceLimits.minimum`  
`resource.autoscaling.resourceLimits.resourceType`  
`resource.binaryAuthorization.enabled`  
`resource.binaryAuthorization.evaluationMode`  
`resource.binaryAuthorization.policyBindings.name`  
`resource.clusterIpv4Cidr`  
`resource.compliancePostureConfig.complianceStandards.standard`  
`resource.compliancePostureConfig.mode`  
`resource.conditions.code`  
`resource.conditions.message`  
`resource.confidentialNodes.confidentialInstanceType`  
`resource.confidentialNodes.enabled`  
`resource.controlPlaneEgress.mode`  
`resource.controlPlaneEndpointsConfig.dnsEndpointConfig.allowExternalTraffic`  
`resource.controlPlaneEndpointsConfig.dnsEndpointConfig.endpoint`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.cidrBlocks.cidrBlock`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.cidrBlocks.displayName`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.enabled`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.gcpPublicCidrsAccessEnabled`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.authorizedNetworksConfig.privateEndpointEnforcementEnabled`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.enabled`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.enablePublicEndpoint`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.globalAccess`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.privateEndpoint`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.privateEndpointSubnetwork`  
`resource.controlPlaneEndpointsConfig.ipEndpointsConfig.publicEndpoint`  
`resource.costManagementConfig.enabled`  
`resource.currentNodeCount`  
`resource.databaseEncryption.keyName`  
`resource.databaseEncryption.state`  
`resource.defaultMaxPodsConstraint.maxPodsPerNode`  
`resource.description`  
`resource.enableK8sBetaApis.enabledApis`  
`resource.enableKubernetesAlpha`  
`resource.enterpriseConfig.clusterTier`  
`resource.fleet.membership`  
`resource.fleet.preRegistered`  
`resource.fleet.project`  
`resource.identityServiceConfig.enabled`  
`resource.initialClusterVersion`  
`resource.initialNodeCount`  
`resource.ipAllocationPolicy.clusterIpv4Cidr`  
`resource.ipAllocationPolicy.clusterIpv4CidrBlock`  
`resource.ipAllocationPolicy.clusterSecondaryRangeName`  
`resource.ipAllocationPolicy.createSubnetwork`  
`resource.ipAllocationPolicy.ipv6AccessType`  
`resource.ipAllocationPolicy.nodeIpv4Cidr`  
`resource.ipAllocationPolicy.nodeIpv4CidrBlock`  
`resource.ipAllocationPolicy.podCidrOverprovisionConfig.disable`  
`resource.ipAllocationPolicy.servicesIpv4Cidr`  
`resource.ipAllocationPolicy.servicesIpv4CidrBlock`  
`resource.ipAllocationPolicy.servicesSecondaryRangeName`  
`resource.ipAllocationPolicy.stackType`  
`resource.ipAllocationPolicy.subnetworkName`  
`resource.ipAllocationPolicy.tpuIpv4CidrBlock`  
`resource.ipAllocationPolicy.useIpAliases`  
`resource.ipAllocationPolicy.useRoutes`  
`resource.labelFingerprint`  
`resource.legacyAbac.enabled`  
`resource.location`  
`resource.locations`  
`resource.loggingConfig.componentConfig.enableComponents`  
`resource.loggingService`  
`resource.maintenancePolicy.resourceVersion`  
`resource.maintenancePolicy.window.dailyMaintenanceWindow.startTime`  
`resource.maintenancePolicy.window.maintenanceExclusions[*].endTime`  
`resource.maintenancePolicy.window.maintenanceExclusions[*].maintenanceExclusionOptions.scope`  
`resource.maintenancePolicy.window.maintenanceExclusions[*].startTime`  
`resource.maintenancePolicy.window.recurringWindow.recurrence`  
`resource.maintenancePolicy.window.recurringWindow.window.endTime`  
`resource.maintenancePolicy.window.recurringWindow.window.maintenanceExclusionOptions.scope`  
`resource.maintenancePolicy.window.recurringWindow.window.startTime`  
`resource.masterAuth.clientCertificateConfig.issueClientCertificate`  
`resource.masterAuth.username`  
`resource.masterAuthorizedNetworksConfig.cidrBlocks.cidrBlock`  
`resource.masterAuthorizedNetworksConfig.cidrBlocks.displayName`  
`resource.masterAuthorizedNetworksConfig.enabled`  
`resource.masterAuthorizedNetworksConfig.gcpPublicCidrsAccessEnabled`  
`resource.masterAuthorizedNetworksConfig.privateEndpointEnforcementEnabled`  
`resource.meshCertificates.enableCertificates`  
`resource.monitoringConfig.advancedDatapathObservabilityConfig.enableMetrics`  
`resource.monitoringConfig.advancedDatapathObservabilityConfig.enableRelay`  
`resource.monitoringConfig.advancedDatapathObservabilityConfig.relayMode`  
`resource.monitoringConfig.componentConfig.enableComponents`  
`resource.monitoringConfig.managedPrometheusConfig.autoMonitoringConfig.scope`  
`resource.monitoringConfig.managedPrometheusConfig.enabled`  
`resource.monitoringService`  
`resource.name`  
`resource.network`  
`resource.networkConfig.datapathProvider`  
`resource.networkConfig.defaultEnablePrivateNodes`  
`resource.networkConfig.defaultSnatStatus.disabled`  
`resource.networkConfig.disableL4LbFirewallReconciliation`  
`resource.networkConfig.dnsConfig.additiveVpcScopeDnsDomain`  
`resource.networkConfig.dnsConfig.clusterDns`  
`resource.networkConfig.dnsConfig.clusterDnsDomain`  
`resource.networkConfig.dnsConfig.clusterDnsScope`  
`resource.networkConfig.enableCiliumClusterwideNetworkPolicy`  
`resource.networkConfig.enableFqdnNetworkPolicy`  
`resource.networkConfig.enableIntraNodeVisibility`  
`resource.networkConfig.enableL4ilbSubsetting`  
`resource.networkConfig.enableMultiNetworking`  
`resource.networkConfig.gatewayApiConfig.channel`  
`resource.networkConfig.inTransitEncryptionConfig`  
`resource.networkConfig.networkPerformanceConfig.totalEgressBandwidthTier`  
`resource.networkConfig.privateIpv6GoogleAccess`  
`resource.networkConfig.serviceExternalIpsConfig.enabled`  
`resource.networkPolicy.enabled`  
`resource.networkPolicy.provider`  
`resource.nodeConfig.accelerators.acceleratorCount`  
`resource.nodeConfig.accelerators.acceleratorType`  
`resource.nodeConfig.accelerators.gpuDriverInstallationConfig.gpuDriverVersion`  
`resource.nodeConfig.accelerators.gpuPartitionSize`  
`resource.nodeConfig.accelerators.gpuSharingConfig.gpuSharingStrategy`  
`resource.nodeConfig.accelerators.gpuSharingConfig.maxSharedClientsPerGpu`  
`resource.nodeConfig.advancedMachineFeatures.enableNestedVirtualization`  
`resource.nodeConfig.advancedMachineFeatures.performanceMonitoringUnit`  
`resource.nodeConfig.advancedMachineFeatures.threadsPerCore`  
`resource.nodeConfig.bootDiskKmsKey`  
`resource.nodeConfig.confidentialNodes.confidentialInstanceType`  
`resource.nodeConfig.confidentialNodes.enabled`  
`resource.nodeConfig.diskSizeGb`  
`resource.nodeConfig.diskType`  
`resource.nodeConfig.ephemeralStorageLocalSsdConfig.dataCacheCount`  
`resource.nodeConfig.ephemeralStorageLocalSsdConfig.localSsdCount`  
`resource.nodeConfig.fastSocket.enabled`  
`resource.nodeConfig.flexStart`  
`resource.nodeConfig.gcfsConfig.enabled`  
`resource.nodeConfig.gvnic.enabled`  
`resource.nodeConfig.imageType`  
`resource.nodeConfig.kubeletConfig.allowedUnsafeSysctls`  
`resource.nodeConfig.kubeletConfig.containerLogMaxFiles`  
`resource.nodeConfig.kubeletConfig.containerLogMaxSize`  
`resource.nodeConfig.kubeletConfig.cpuCfsQuota`  
`resource.nodeConfig.kubeletConfig.cpuCfsQuotaPeriod`  
`resource.nodeConfig.kubeletConfig.cpuManagerPolicy`  
`resource.nodeConfig.kubeletConfig.imageGcHighThresholdPercent`  
`resource.nodeConfig.kubeletConfig.imageGcLowThresholdPercent`  
`resource.nodeConfig.kubeletConfig.imageMaximumGcAge`  
`resource.nodeConfig.kubeletConfig.imageMinimumGcAge`  
`resource.nodeConfig.kubeletConfig.insecureKubeletReadonlyPortEnabled`  
`resource.nodeConfig.kubeletConfig.memoryManager.policy`  
`resource.nodeConfig.kubeletConfig.podPidsLimit`  
`resource.nodeConfig.kubeletConfig.topologyManager.policy`  
`resource.nodeConfig.kubeletConfig.topologyManager.scope`  
`resource.nodeConfig.labels`  
`resource.nodeConfig.linuxNodeConfig.cgroupMode`  
`resource.nodeConfig.linuxNodeConfig.hugepages.hugepageSize1g`  
`resource.nodeConfig.linuxNodeConfig.hugepages.hugepageSize2m`  
`resource.nodeConfig.linuxNodeConfig.sysctls`  
`resource.nodeConfig.localNvmeSsdBlockConfig.localSsdCount`  
`resource.nodeConfig.localSsdCount`  
`resource.nodeConfig.localSsdEncryptionMode`  
`resource.nodeConfig.loggingConfig.variantConfig.variant`  
`resource.nodeConfig.machineType`  
`resource.nodeConfig.maxRunDuration`  
`resource.nodeConfig.metadata`  
`resource.nodeConfig.minCpuPlatform`  
`resource.nodeConfig.nodeGroup`  
`resource.nodeConfig.oauthScopes`  
`resource.nodeConfig.preemptible`  
`resource.nodeConfig.reservationAffinity.consumeReservationType`  
`resource.nodeConfig.reservationAffinity.key`  
`resource.nodeConfig.reservationAffinity.values`  
`resource.nodeConfig.resourceLabels`  
`resource.nodeConfig.resourceManagerTags.tags`  
`resource.nodeConfig.sandboxConfig.type`  
`resource.nodeConfig.secondaryBootDisks.diskImage`  
`resource.nodeConfig.secondaryBootDisks.mode`  
`resource.nodeConfig.serviceAccount`  
`resource.nodeConfig.shieldedInstanceConfig.enableIntegrityMonitoring`  
`resource.nodeConfig.shieldedInstanceConfig.enableSecureBoot`  
`resource.nodeConfig.soleTenantConfig.nodeAffinities.key`  
`resource.nodeConfig.soleTenantConfig.nodeAffinities.operator`  
`resource.nodeConfig.soleTenantConfig.nodeAffinities.values`  
`resource.nodeConfig.spot`  
`resource.nodeConfig.storagePools`  
`resource.nodeConfig.tags`  
`resource.nodeConfig.taints.effect`  
`resource.nodeConfig.taints.key`  
`resource.nodeConfig.taints.value`  
`resource.nodeConfig.windowsNodeConfig.osVersion`  
`resource.nodeConfig.workloadMetadataConfig.mode`  
`resource.nodePoolAutoConfig.networkTags.tags`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.allowedUnsafeSysctls`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.containerLogMaxFiles`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.containerLogMaxSize`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.cpuCfsQuota`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.cpuCfsQuotaPeriod`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.cpuManagerPolicy`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.imageGcHighThresholdPercent`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.imageGcLowThresholdPercent`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.imageMaximumGcAge`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.imageMinimumGcAge`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.insecureKubeletReadonlyPortEnabled`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.memoryManager.policy`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.podPidsLimit`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.topologyManager.policy`  
`resource.nodePoolAutoConfig.nodeKubeletConfig.topologyManager.scope`  
`resource.nodePoolDefaults.nodeConfigDefaults.gcfsConfig.enabled`  
`resource.nodePoolDefaults.nodeConfigDefaults.loggingConfig.variantConfig.variant`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.allowedUnsafeSysctls`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.containerLogMaxFiles`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.containerLogMaxSize`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.cpuCfsQuota`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.cpuCfsQuotaPeriod`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.cpuManagerPolicy`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.imageGcHighThresholdPercent`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.imageGcLowThresholdPercent`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.imageMaximumGcAge`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.imageMinimumGcAge`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.insecureKubeletReadonlyPortEnabled`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.memoryManager.policy`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.podPidsLimit`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.topologyManager.policy`  
`resource.nodePoolDefaults.nodeConfigDefaults.nodeKubeletConfig.topologyManager.scope`  
`resource.notificationConfig.pubsub.enabled`  
`resource.notificationConfig.pubsub.filter.eventType`  
`resource.notificationConfig.pubsub.topic`  
`resource.podAutoscaling.hpaProfile`  
`resource.privateClusterConfig.enablePrivateEndpoint`  
`resource.privateClusterConfig.enablePrivateNodes`  
`resource.privateClusterConfig.masterGlobalAccessConfig.enabled`  
`resource.privateClusterConfig.masterIpv4CidrBlock`  
`resource.privateClusterConfig.privateEndpointSubnetwork`  
`resource.rbacBindingConfig.enableInsecureBindingSystemAuthenticated`  
`resource.rbacBindingConfig.enableInsecureBindingSystemUnauthenticated`  
`resource.releaseChannel.channel`  
`resource.resourceLabels`  
`resource.resourceUsageExportConfig.bigqueryDestination.datasetId`  
`resource.resourceUsageExportConfig.consumptionMeteringConfig.enabled`  
`resource.resourceUsageExportConfig.enableNetworkEgressMetering`  
`resource.secretManagerConfig.enabled`  
`resource.securityPostureConfig.mode`  
`resource.securityPostureConfig.vulnerabilityMode`  
`resource.shieldedNodes.enabled`  
`resource.subnetwork`  
`resource.userManagedKeysConfig.aggregationCa`  
`resource.userManagedKeysConfig.clusterCa`  
`resource.userManagedKeysConfig.controlPlaneDiskEncryptionKey`  
`resource.userManagedKeysConfig.etcdApiCa`  
`resource.userManagedKeysConfig.etcdPeerCa`  
`resource.userManagedKeysConfig.gkeopsEtcdBackupEncryptionKey`  
`resource.userManagedKeysConfig.serviceAccountSigningKeys`  
`resource.userManagedKeysConfig.serviceAccountVerificationKeys`  
`resource.verticalPodAutoscaling.enabled`  
`resource.workloadIdentityConfig.workloadPool`  
`resource.zone`  
container.googleapis.com/NodePool |  `resource.autopilotConfig.enabled`  
`resource.autoscaling.autoprovisioned`  
`resource.autoscaling.enabled`  
`resource.autoscaling.locationPolicy`  
`resource.autoscaling.maxNodeCount`  
`resource.autoscaling.minNodeCount`  
`resource.autoscaling.totalMaxNodeCount`  
`resource.autoscaling.totalMinNodeCount`  
`resource.bestEffortProvisioning.enabled`  
`resource.bestEffortProvisioning.minProvisionNodes`  
`resource.conditions.code`  
`resource.conditions.message`  
`resource.config.accelerators.acceleratorCount`  
`resource.config.accelerators.acceleratorType`  
`resource.config.accelerators.gpuDriverInstallationConfig.gpuDriverVersion`  
`resource.config.accelerators.gpuPartitionSize`  
`resource.config.accelerators.gpuSharingConfig.gpuSharingStrategy`  
`resource.config.accelerators.gpuSharingConfig.maxSharedClientsPerGpu`  
`resource.config.advancedMachineFeatures.enableNestedVirtualization`  
`resource.config.advancedMachineFeatures.performanceMonitoringUnit`  
`resource.config.advancedMachineFeatures.threadsPerCore`  
`resource.config.bootDiskKmsKey`  
`resource.config.confidentialNodes.confidentialInstanceType`  
`resource.config.confidentialNodes.enabled`  
`resource.config.diskSizeGb`  
`resource.config.diskType`  
`resource.config.ephemeralStorageLocalSsdConfig.dataCacheCount`  
`resource.config.ephemeralStorageLocalSsdConfig.localSsdCount`  
`resource.config.fastSocket.enabled`  
`resource.config.flexStart`  
`resource.config.gcfsConfig.enabled`  
`resource.config.gvnic.enabled`  
`resource.config.imageType`  
`resource.config.kubeletConfig.allowedUnsafeSysctls`  
`resource.config.kubeletConfig.containerLogMaxFiles`  
`resource.config.kubeletConfig.containerLogMaxSize`  
`resource.config.kubeletConfig.cpuCfsQuota`  
`resource.config.kubeletConfig.cpuCfsQuotaPeriod`  
`resource.config.kubeletConfig.cpuManagerPolicy`  
`resource.config.kubeletConfig.imageGcHighThresholdPercent`  
`resource.config.kubeletConfig.imageGcLowThresholdPercent`  
`resource.config.kubeletConfig.imageMaximumGcAge`  
`resource.config.kubeletConfig.imageMinimumGcAge`  
`resource.config.kubeletConfig.insecureKubeletReadonlyPortEnabled`  
`resource.config.kubeletConfig.memoryManager.policy`  
`resource.config.kubeletConfig.podPidsLimit`  
`resource.config.kubeletConfig.topologyManager.policy`  
`resource.config.kubeletConfig.topologyManager.scope`  
`resource.config.labels`  
`resource.config.linuxNodeConfig.cgroupMode`  
`resource.config.linuxNodeConfig.hugepages.hugepageSize1g`  
`resource.config.linuxNodeConfig.hugepages.hugepageSize2m`  
`resource.config.linuxNodeConfig.sysctls`  
`resource.config.localNvmeSsdBlockConfig.localSsdCount`  
`resource.config.localSsdCount`  
`resource.config.localSsdEncryptionMode`  
`resource.config.loggingConfig.variantConfig.variant`  
`resource.config.machineType`  
`resource.config.maxRunDuration`  
`resource.config.metadata`  
`resource.config.minCpuPlatform`  
`resource.config.nodeGroup`  
`resource.config.oauthScopes`  
`resource.config.preemptible`  
`resource.config.reservationAffinity.consumeReservationType`  
`resource.config.reservationAffinity.key`  
`resource.config.reservationAffinity.values`  
`resource.config.resourceLabels`  
`resource.config.resourceManagerTags.tags`  
`resource.config.sandboxConfig.type`  
`resource.config.secondaryBootDisks.diskImage`  
`resource.config.secondaryBootDisks.mode`  
`resource.config.serviceAccount`  
`resource.config.shieldedInstanceConfig.enableIntegrityMonitoring`  
`resource.config.shieldedInstanceConfig.enableSecureBoot`  
`resource.config.soleTenantConfig.nodeAffinities.key`  
`resource.config.soleTenantConfig.nodeAffinities.operator`  
`resource.config.soleTenantConfig.nodeAffinities.values`  
`resource.config.spot`  
`resource.config.storagePools`  
`resource.config.tags`  
`resource.config.taints.effect`  
`resource.config.taints.key`  
`resource.config.taints.value`  
`resource.config.windowsNodeConfig.osVersion`  
`resource.config.workloadMetadataConfig.mode`  
`resource.initialNodeCount`  
`resource.locations`  
`resource.management.autoRepair`  
`resource.management.autoUpgrade`  
`resource.maxPodsConstraint.maxPodsPerNode`  
`resource.name`  
`resource.networkConfig.additionalNodeNetworkConfigs.network`  
`resource.networkConfig.additionalNodeNetworkConfigs.subnetwork`  
`resource.networkConfig.additionalPodNetworkConfigs.networkAttachment`  
`resource.networkConfig.createPodRange`  
`resource.networkConfig.enablePrivateNodes`  
`resource.networkConfig.networkPerformanceConfig.totalEgressBandwidthTier`  
`resource.networkConfig.podIpv4CidrBlock`  
`resource.networkConfig.podRange`  
`resource.placementPolicy.policyName`  
`resource.placementPolicy.tpuTopology`  
`resource.placementPolicy.type`  
`resource.queuedProvisioning.enabled`  
`resource.upgradeSettings.blueGreenSettings.nodePoolSoakDuration`  
`resource.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchNodeCount`  
`resource.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchPercentage`  
`resource.upgradeSettings.blueGreenSettings.standardRolloutPolicy.batchSoakDuration`  
`resource.upgradeSettings.maxSurge`  
`resource.upgradeSettings.maxUnavailable`  
`resource.upgradeSettings.strategy`  
`resource.version`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.enableGkeAutopilot`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

  9. To define a condition, click edit **Edit condition**. 
     1. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false`. This field can contain up to 1000 characters. For details about CEL usage, see [ Common Expression Language](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language). For more information about the service resources you can use in your custom constraints, see [ Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services). 
     2. Click **Save**. 
  10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

  11. Click **Create constraint**. 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 




### gcloud

  1. To create a custom constraint, create a YAML file using the following format: 
    
    name: organizations/ORGANIZATION_ID/customConstraints/CONSTRAINT_NAME
    resourceTypes: RESOURCE_NAME
    methodTypes:
      - CREATE  
      - UPDATE 
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.enableGkeAutopilot`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `container.googleapis.com/Cluster`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can be `CREATE` or both `CREATE` and `UPDATE`. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `"resource.autopilot.enabled == false"`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Possible values are `ALLOW` and `DENY`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

The deny action means that if the condition evaluates to true, the operation to create or update the resource is blocked. 

     * `DISPLAY_NAME`: a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use PII or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
     * `DESCRIPTION`: a human-friendly description of the constraint to display as an error message when the policy is violated. This field can contain up to 2000 characters. 
  2. After you have created the YAML file for a new custom constraint, you must set it up to make it available for organization policies in your organization. To set up a custom constraint, use the [ `gcloud org-policies set-custom-constraint`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/set-custom-constraint) command: 
    
    gcloud org-policies set-custom-constraint CONSTRAINT_PATH

Replace `CONSTRAINT_PATH` with the full path to your custom constraint file. For example, `/home/user/customconstraint.yaml`. 

After this operation is complete, your custom constraints are available as organization policies in your list of Google Cloud organization policies. 

  3. To verify that the custom constraint exists, use the [ `gcloud org-policies list-custom-constraints`](https://docs.cloud.google.com/sdk/gcloud/reference/org-policies/list-custom-constraints) command: 
    
    gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID

Replace `ORGANIZATION_ID` with the ID of your organization resource. 

For more information, see [ Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies). 




## Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

### Console

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 
  4. To configure the organization policy for this resource, click **Manage policy**. 
  5. On the **Edit policy** page, select **Override parent's policy**. 
  6. Click **Add a rule**. 
  7. In the **Enforcement** section, select whether this organization policy is enforced or not. 
  8. Optional: To make the organization policy conditional on a tag, click **Add condition**. Note that if you add a conditional rule to an organization policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see [ Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies). 
  9. Click **Test changes** to simulate the effect of the organization policy. For more information, see [ Test organization policy changes with Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/test-organization-policies). 
  10. To enforce the organization policy in dry-run mode, click **Set dry run policy**. For more information, see [ Test organization policies](https://docs.cloud.google.com/organization-policy/test-policies). 
  11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy**. 



### gcloud

  1. To create an organization policy with boolean rules, create a policy YAML file that references the constraint: 
    
    name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
    spec:
      rules:
      - enforce: true
    
    dryRunSpec:
      rules:
      - enforce: true

Replace the following: 

     * `PROJECT_ID`: the project that you want to enforce your constraint on. 
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.enableGkeAutopilot`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example creates a custom constraint and policy that requires all new clusters in a project to be Autopilot clusters.

### Create the constraint

  1. Save the following file as `constraint-enable-autopilot.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.enableGkeAutopilot
         resourceTypes:
         - container.googleapis.com/Cluster
         methodTypes:
         - CREATE
         condition: "resource.autopilot.enabled == false"
         actionType: DENY
         displayName: Enable GKE Autopilot
         description: All new clusters must be Autopilot clusters.
         

Replace `ORGANIZATION_ID` with your organization ID.

This file defines a constraint where for every new cluster, if the cluster mode is not Autopilot, the operation is denied.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-enable-autopilot.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT                       ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                     DISPLAY_NAME
         custom.enableGkeAutopilot               DENY         CREATE         container.googleapis.com/Cluster   Enable GKE Autopilot
         ...
         




### Create the policy

  1. Save the following file as `policy-enable-autopilot.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.enableGkeAutopilot
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-enable-autopilot.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT                  LIST_POLICY    BOOLEAN_POLICY    ETAG
         custom.enableGkeAutopilot   -              SET               COCsm5QGENiXi2E=
         




After you apply the policy, wait for about two minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try to create a GKE Standard cluster in the project:
    
    
    gcloud container clusters create org-policy-test \
        --project=PROJECT_ID \
        --location=CONTROL_PLANE_LOCATION \
        --num-nodes=1
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project of the policy.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



The output is the following:
    
    
    Operation denied by custom org policies: ["customConstraints/custom.enableGkeAutopilot": "All new clusters must be Autopilot clusters."]
    

## Example custom organization policies for common use cases

The following samples provide the syntax of some custom constraints that you might find useful:

Description | Constraint syntax  
---|---  
Do not disable node auto-upgrade for new node pools | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.enableAutoUpgrade
    resourceTypes:
    - container.googleapis.com/NodePool
    methodTypes:
    - CREATE
    condition: "resource.management.autoUpgrade == true"
    actionType: ALLOW
    displayName: Enable node auto-upgrade
    description: All node pools must have node auto-upgrade enabled.  
  
Restrict anonymous access to cluster endpoints in new and existing clusters | 
    
    
    name: organizations/ORGANIZATION_ID/customConstraints/custom.gkeAnonymousAccessLimited
    resourceTypes:
    - container.googleapis.com/Cluster
    methodTypes:
    - CREATE
    - UPDATE
    condition: "resource.anonymousAuthenticationConfig.mode == LIMITED"
    actionType: ALLOW
    displayName: "Restrict anonymous access to cluster endpoints."
    description: "All new and updated clusters must restrict anonymous access to cluster endpoints."  
  
## What's next

  * See best practices to [harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).
  * Learn how to [require that VM Manager is enabled on all GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enforce-vm-agents).
  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
