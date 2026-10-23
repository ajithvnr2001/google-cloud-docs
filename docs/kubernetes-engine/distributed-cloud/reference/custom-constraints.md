---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints/
title: Create and manage custom constraints \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:04.135926+00:00
---

# Create and manage custom constraints  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/custom-constraints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  Create and manage custom constraints Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources:

  * `gkeonprem.googleapis.com/BareMetalAdminCluster`
  * `gkeonprem.googleapis.com/BareMetalCluster`
  * `gkeonprem.googleapis.com/BareMetalNodePool`
  * `gkeonprem.googleapis.com/VmwareAdminCluster`
  * `gkeonprem.googleapis.com/VmwareCluster`
  * `gkeonprem.googleapis.com/VmwareNodePool`



To learn more about Organization Policy, see [Custom organization policies](https://docs.cloud.google.com/organization-policy/overview#custom-organization-policies).

## About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the [organization policy administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level.

Organization Policy provides built-in [managed constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy.

### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about this behavior and how to change it, refer to [Hierarchy evaluation rules](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation#disallow_inheritance).

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

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization resource. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## GKE On-Prem API supported resources

The following table lists the GKE On-Prem API resources that you can reference in custom constraints. 

Resource | Field  
---|---  
gkeonprem.googleapis.com/BareMetalAdminCluster |  `resource.annotations`  
`resource.bareMetalVersion`  
`resource.binaryAuthorization.evaluationMode`  
`resource.clusterOperations.enableApplicationLogs`  
`resource.controlPlane.apiServerArgs.argument`  
`resource.controlPlane.apiServerArgs.value`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.registryBurst`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.registryPullQps`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.serializeImagePullsDisabled`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.nodeConfigs.nodeIp`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.operatingSystem`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.effect`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.key`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.value`  
`resource.description`  
`resource.loadBalancer.manualLbConfig.enabled`  
`resource.loadBalancer.portConfig.controlPlaneLoadBalancerPort`  
`resource.loadBalancer.vipConfig.controlPlaneVip`  
`resource.maintenanceConfig.maintenanceAddressCidrBlocks`  
`resource.name`  
`resource.networkConfig.islandModeCidr.podAddressCidrBlocks`  
`resource.networkConfig.islandModeCidr.serviceAddressCidrBlocks`  
`resource.nodeAccessConfig.loginUser`  
`resource.nodeConfig.maxPodsPerNode`  
`resource.osEnvironmentConfig.packageRepoExcluded`  
`resource.proxy.noProxy`  
`resource.proxy.uri`  
`resource.securityConfig.authorization.adminUsers.username`  
`resource.storage.lvpNodeMountsConfig.path`  
`resource.storage.lvpNodeMountsConfig.storageClass`  
`resource.storage.lvpShareConfig.lvpConfig.path`  
`resource.storage.lvpShareConfig.lvpConfig.storageClass`  
`resource.storage.lvpShareConfig.sharedPathPvCount`  
gkeonprem.googleapis.com/BareMetalCluster |  `resource.adminClusterMembership`  
`resource.annotations`  
`resource.bareMetalVersion`  
`resource.binaryAuthorization.evaluationMode`  
`resource.clusterOperations.enableApplicationLogs`  
`resource.controlPlane.apiServerArgs.argument`  
`resource.controlPlane.apiServerArgs.value`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.registryBurst`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.registryPullQps`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.kubeletConfig.serializeImagePullsDisabled`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.nodeConfigs.nodeIp`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.operatingSystem`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.effect`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.key`  
`resource.controlPlane.controlPlaneNodePoolConfig.nodePoolConfig.taints.value`  
`resource.description`  
`resource.loadBalancer.bgpLbConfig.addressPools.addresses`  
`resource.loadBalancer.bgpLbConfig.addressPools.avoidBuggyIps`  
`resource.loadBalancer.bgpLbConfig.addressPools.manualAssign`  
`resource.loadBalancer.bgpLbConfig.addressPools.pool`  
`resource.loadBalancer.bgpLbConfig.asn`  
`resource.loadBalancer.bgpLbConfig.bgpPeerConfigs.asn`  
`resource.loadBalancer.bgpLbConfig.bgpPeerConfigs.controlPlaneNodes`  
`resource.loadBalancer.bgpLbConfig.bgpPeerConfigs.ipAddress`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.registryBurst`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.registryPullQps`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.serializeImagePullsDisabled`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.nodeConfigs.nodeIp`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.operatingSystem`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.effect`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.key`  
`resource.loadBalancer.bgpLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.value`  
`resource.loadBalancer.manualLbConfig.enabled`  
`resource.loadBalancer.metalLbConfig.addressPools.addresses`  
`resource.loadBalancer.metalLbConfig.addressPools.avoidBuggyIps`  
`resource.loadBalancer.metalLbConfig.addressPools.manualAssign`  
`resource.loadBalancer.metalLbConfig.addressPools.pool`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.registryBurst`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.registryPullQps`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.kubeletConfig.serializeImagePullsDisabled`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.nodeConfigs.nodeIp`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.operatingSystem`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.effect`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.key`  
`resource.loadBalancer.metalLbConfig.loadBalancerNodePoolConfig.nodePoolConfig.taints.value`  
`resource.loadBalancer.portConfig.controlPlaneLoadBalancerPort`  
`resource.loadBalancer.vipConfig.controlPlaneVip`  
`resource.loadBalancer.vipConfig.ingressVip`  
`resource.maintenanceConfig.maintenanceAddressCidrBlocks`  
`resource.name`  
`resource.networkConfig.advancedNetworking`  
`resource.networkConfig.islandModeCidr.podAddressCidrBlocks`  
`resource.networkConfig.islandModeCidr.serviceAddressCidrBlocks`  
`resource.networkConfig.multipleNetworkInterfacesConfig.enabled`  
`resource.networkConfig.srIovConfig.enabled`  
`resource.nodeAccessConfig.loginUser`  
`resource.nodeConfig.containerRuntime`  
`resource.nodeConfig.maxPodsPerNode`  
`resource.osEnvironmentConfig.packageRepoExcluded`  
`resource.proxy.noProxy`  
`resource.proxy.uri`  
`resource.securityConfig.authorization.adminUsers.username`  
`resource.storage.lvpNodeMountsConfig.path`  
`resource.storage.lvpNodeMountsConfig.storageClass`  
`resource.storage.lvpShareConfig.lvpConfig.path`  
`resource.storage.lvpShareConfig.lvpConfig.storageClass`  
`resource.storage.lvpShareConfig.sharedPathPvCount`  
`resource.upgradePolicy.policy`  
gkeonprem.googleapis.com/BareMetalNodePool |  `resource.annotations`  
`resource.displayName`  
`resource.name`  
`resource.nodePoolConfig.kubeletConfig.registryBurst`  
`resource.nodePoolConfig.kubeletConfig.registryPullQps`  
`resource.nodePoolConfig.kubeletConfig.serializeImagePullsDisabled`  
`resource.nodePoolConfig.nodeConfigs.nodeIp`  
`resource.nodePoolConfig.operatingSystem`  
`resource.nodePoolConfig.taints.effect`  
`resource.nodePoolConfig.taints.key`  
`resource.nodePoolConfig.taints.value`  
`resource.upgradePolicy.parallelUpgradeConfig.concurrentNodes`  
`resource.upgradePolicy.parallelUpgradeConfig.minimumAvailableNodes`  
gkeonprem.googleapis.com/VmwareAdminCluster |  `resource.addonNode.autoResizeConfig.enabled`  
`resource.annotations`  
`resource.antiAffinityGroups.aagConfigDisabled`  
`resource.authorization.viewerUsers.username`  
`resource.autoRepairConfig.enabled`  
`resource.bootstrapClusterMembership`  
`resource.controlPlaneNode.cpus`  
`resource.controlPlaneNode.memory`  
`resource.controlPlaneNode.replicas`  
`resource.description`  
`resource.enableAdvancedCluster`  
`resource.imageType`  
`resource.loadBalancer.f5Config.address`  
`resource.loadBalancer.f5Config.partition`  
`resource.loadBalancer.f5Config.snatPool`  
`resource.loadBalancer.manualLbConfig.addonsNodePort`  
`resource.loadBalancer.manualLbConfig.controlPlaneNodePort`  
`resource.loadBalancer.manualLbConfig.ingressHttpNodePort`  
`resource.loadBalancer.manualLbConfig.ingressHttpsNodePort`  
`resource.loadBalancer.manualLbConfig.konnectivityServerNodePort`  
`resource.loadBalancer.metalLbConfig.enabled`  
`resource.loadBalancer.vipConfig.addonsVip`  
`resource.loadBalancer.vipConfig.controlPlaneVip`  
`resource.name`  
`resource.networkConfig.dhcpIpConfig.enabled`  
`resource.networkConfig.haControlPlaneConfig.controlPlaneIpBlock.gateway`  
`resource.networkConfig.haControlPlaneConfig.controlPlaneIpBlock.ips.hostname`  
`resource.networkConfig.haControlPlaneConfig.controlPlaneIpBlock.ips.ip`  
`resource.networkConfig.haControlPlaneConfig.controlPlaneIpBlock.netmask`  
`resource.networkConfig.hostConfig.dnsSearchDomains`  
`resource.networkConfig.hostConfig.dnsServers`  
`resource.networkConfig.hostConfig.ntpServers`  
`resource.networkConfig.podAddressCidrBlocks`  
`resource.networkConfig.serviceAddressCidrBlocks`  
`resource.networkConfig.staticIpConfig.ipBlocks.gateway`  
`resource.networkConfig.staticIpConfig.ipBlocks.ips.hostname`  
`resource.networkConfig.staticIpConfig.ipBlocks.ips.ip`  
`resource.networkConfig.staticIpConfig.ipBlocks.netmask`  
`resource.networkConfig.vcenterNetwork`  
`resource.onPremVersion`  
`resource.platformConfig.requiredPlatformVersion`  
`resource.vcenter.address`  
`resource.vcenter.caCertData`  
`resource.vcenter.cluster`  
`resource.vcenter.datacenter`  
`resource.vcenter.dataDisk`  
`resource.vcenter.datastore`  
`resource.vcenter.folder`  
`resource.vcenter.resourcePool`  
`resource.vcenter.storagePolicyName`  
gkeonprem.googleapis.com/VmwareCluster |  `resource.adminClusterMembership`  
`resource.annotations`  
`resource.antiAffinityGroups.aagConfigDisabled`  
`resource.authorization.adminUsers.username`  
`resource.autoRepairConfig.enabled`  
`resource.binaryAuthorization.evaluationMode`  
`resource.controlPlaneNode.autoResizeConfig.enabled`  
`resource.controlPlaneNode.cpus`  
`resource.controlPlaneNode.memory`  
`resource.controlPlaneNode.replicas`  
`resource.controlPlaneNode.vsphereConfig.datastore`  
`resource.controlPlaneNode.vsphereConfig.storagePolicyName`  
`resource.dataplaneV2.advancedNetworking`  
`resource.dataplaneV2.dataplaneV2Enabled`  
`resource.dataplaneV2.forwardMode`  
`resource.dataplaneV2.windowsDataplaneV2Enabled`  
`resource.description`  
`resource.disableBundledIngress`  
`resource.enableAdvancedCluster`  
`resource.enableControlPlaneV2`  
`resource.loadBalancer.f5Config.address`  
`resource.loadBalancer.f5Config.partition`  
`resource.loadBalancer.f5Config.snatPool`  
`resource.loadBalancer.manualLbConfig.controlPlaneNodePort`  
`resource.loadBalancer.manualLbConfig.ingressHttpNodePort`  
`resource.loadBalancer.manualLbConfig.ingressHttpsNodePort`  
`resource.loadBalancer.manualLbConfig.konnectivityServerNodePort`  
`resource.loadBalancer.metalLbConfig.addressPools.addresses`  
`resource.loadBalancer.metalLbConfig.addressPools.avoidBuggyIps`  
`resource.loadBalancer.metalLbConfig.addressPools.manualAssign`  
`resource.loadBalancer.metalLbConfig.addressPools.pool`  
`resource.loadBalancer.vipConfig.controlPlaneVip`  
`resource.loadBalancer.vipConfig.ingressVip`  
`resource.name`  
`resource.networkConfig.controlPlaneV2Config.controlPlaneIpBlock.gateway`  
`resource.networkConfig.controlPlaneV2Config.controlPlaneIpBlock.ips.hostname`  
`resource.networkConfig.controlPlaneV2Config.controlPlaneIpBlock.ips.ip`  
`resource.networkConfig.controlPlaneV2Config.controlPlaneIpBlock.netmask`  
`resource.networkConfig.dhcpIpConfig.enabled`  
`resource.networkConfig.hostConfig.dnsSearchDomains`  
`resource.networkConfig.hostConfig.dnsServers`  
`resource.networkConfig.hostConfig.ntpServers`  
`resource.networkConfig.podAddressCidrBlocks`  
`resource.networkConfig.serviceAddressCidrBlocks`  
`resource.networkConfig.staticIpConfig.ipBlocks.gateway`  
`resource.networkConfig.staticIpConfig.ipBlocks.ips.hostname`  
`resource.networkConfig.staticIpConfig.ipBlocks.ips.ip`  
`resource.networkConfig.staticIpConfig.ipBlocks.netmask`  
`resource.networkConfig.vcenterNetwork`  
`resource.onPremVersion`  
`resource.storage.vsphereCsiDisabled`  
`resource.upgradePolicy.controlPlaneOnly`  
`resource.vcenter.caCertData`  
`resource.vcenter.cluster`  
`resource.vcenter.datacenter`  
`resource.vcenter.datastore`  
`resource.vcenter.folder`  
`resource.vcenter.resourcePool`  
`resource.vcenter.storagePolicyName`  
`resource.vmTrackingEnabled`  
gkeonprem.googleapis.com/VmwareNodePool |  `resource.annotations`  
`resource.config.bootDiskSizeGb`  
`resource.config.cpus`  
`resource.config.enableLoadBalancer`  
`resource.config.image`  
`resource.config.imageType`  
`resource.config.memoryMb`  
`resource.config.replicas`  
`resource.config.taints.effect`  
`resource.config.taints.key`  
`resource.config.taints.value`  
`resource.config.vsphereConfig.datastore`  
`resource.config.vsphereConfig.hostGroups`  
`resource.config.vsphereConfig.tags.category`  
`resource.config.vsphereConfig.tags.tag`  
`resource.displayName`  
`resource.name`  
`resource.nodePoolAutoscaling.maxReplicas`  
`resource.nodePoolAutoscaling.minReplicas`  
`resource.onPremVersion`  
  
## Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using [Common Expression Language (CEL)](https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of [Creating and managing custom constraints](https://docs.cloud.google.com/organization-policy/create-custom-constraints#common_expression_language).

### Console

To create a custom constraint, do the following: 

  1. In the Google Cloud console, go to the **Organization policies** page. 

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project that you want to set the organization policy for. 
  3. Click add **Custom constraint**. 
  4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 
  5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.denyHighNumvCPUs`. This field can contain up to 70 characters, not counting the prefix (`custom.`), for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
  6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 
  7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
  8. This constraint can only be enforced on the REST `CREATE` method. 

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
    condition: "CONDITION"
    actionType: ACTION
    displayName: DISPLAY_NAME
    description: DESCRIPTION

Replace the following: 

     * `ORGANIZATION_ID`: your organization ID, such as `123456789`. 
     * `CONSTRAINT_NAME`: the name that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example, `custom.denyHighNumvCPUs`. This field can contain up to 70 characters, not counting the prefix (`custom.`)— for example, `organizations/123456789/customConstraints/custom`. Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 
     * `RESOURCE_NAME`: the fully qualified name of the Google Cloud resource containing the object and field that you want to restrict. For example, `gkeonprem.googleapis.com/VmwareNodePool`. Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 
     * `methodTypes`: the REST methods that the constraint is enforced on. Can only be `CREATE`. 

To see the supported methods for each service, find the service in [ Services that support custom constraints](https://docs.cloud.google.com/organization-policy/reference/custom-constraint-supported-services). 

     * `CONDITION`: a [ CEL condition](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-custom-constraints#common_expression_language) that is written against a representation of a supported service resource. This field can contain up to 1000 characters. For example, `resource.config.cpus > 4`. 

For more information about the resources available to write conditions against, see Supported resources. 

     * `ACTION`: the action to take if the `condition` is met. Can only be `ALLOW`. 

The allow action means that if the condition evaluates to true, the operation to create or update the resource is permitted. This also means that every other case except the one explicitly listed in the condition is blocked. 

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
     * `CONSTRAINT_NAME`: the name you defined for your custom constraint. For example, `custom.denyHighNumvCPUs`. 
  2. To enforce the organization policy in [dry-run mode](https://docs.cloud.google.com/organization-policy/test-policies), run the following command with the `dryRunSpec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=dryRunSpec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 

  3. After you verify that the organization policy in dry-run mode works as intended, set the live policy with the `org-policies set-policy` command and the `spec` flag: 
    
    gcloud org-policies set-policy POLICY_PATH --update-mask=spec

Replace `POLICY_PATH` with the full path to your organization policy YAML file. The policy requires up to 15 minutes to take effect. 




## Test the custom organization policy

The following example shows how to deny updating a node pool with more than four vCPUs in a Google Distributed Cloud (software only) VMware user cluster.

Before you begin, you must know the following:

  * Your organization ID
  * A project ID



### Create the constraint

  1. Save the following file as `constraint-node-pool-vcpus.yaml`:
         
         name: organizations/ORGANIZATION_ID/customConstraints/custom.denyHighNumvCPUs
         resourceTypes:
         - gkeonprem.googleapis.com/VmwareNodePool
         methodTypes:
         - CREATE
         - UPDATE
         condition: resource.config.cpus > 4
         actionType: DENY
         displayName: Node pool vCPU constraint
         description: Node pools must have 4 or fewer vCPUs.
         

This defines a constraint that restricts the number of vCPUs in a node pool to 4 or fewer. If the number of vCPUs is greater than 4 on node pool create or update, the operation is denied.

  2. Apply the constraint:
         
         gcloud org-policies set-custom-constraint ~/constraint-node-pool-vcpus.yaml
         

  3. Verify that the constraint exists:
         
         gcloud org-policies list-custom-constraints --organization=ORGANIZATION_ID
         

The output is similar to the following:
         
         CUSTOM_CONSTRAINT         ACTION_TYPE  METHOD_TYPES   RESOURCE_TYPES                            DISPLAY_NAME
         custom.denyHighNumvCPUs   DENY         CREATE         gkeonprem.googleapis.com/VmwareNodePool   Node pool vCPU constraint
         ...
         




### Create the policy

  1. Save the following file as `policy-deny-node-pool-high-vcpus.yaml`:
         
         name: projects/PROJECT_ID/policies/custom.denyHighNumvCPUs
         spec:
           rules:
           - enforce: true
         

Replace `PROJECT_ID` with your project ID.

  2. Apply the policy:
         
         gcloud org-policies set-policy ~/policy-deny-node-pool-high-vcpus.yaml
         

  3. Verify that the policy exists:
         
         gcloud org-policies list --project=PROJECT_ID
         

The output is similar to the following:
         
         CONSTRAINT               LIST_POLICY    BOOLEAN_POLICY    ETAG
         custom.denyHighNumvCPUs  -              SET               COCsm5QGENiXi2E=
         




After you apply the policy, wait for about 15 minutes for Google Cloud to start enforcing the policy.

### Test the policy

Try to update a node pool that violates the policy.

  1. Optionally, list the user clusters to get the cluster name and region:
         
         gcloud container vmware clusters list \
             --project=PROJECT_ID\
             --location=-
         

When you set `--location=-`, that means to list all user clusters in all regions. If you need to scope down the list, set `--location` to the region you specified when you created the cluster or enrolled the cluster in the GKE On-Prem API.

  2. Optionally, list the node pools to get the name of the node pool that you want to update:
         
         gcloud container vmware node-pools list \
             --cluster=USER_CLUSTER_NAME \
             --project=PROJECT_ID \
             --location=REGION
         

Replace the following:

     * `USER_CLUSTER_NAME`: The name of the user cluster that contains the node pool.

     * `REGION`: The Google Cloud region associated with the user cluster.

  3. Run the following command to attempt to update the number of vCPUs to 6:
         
         gcloud container vmware node-pools update NODE_POOL_NAME \
             --cluster=USER_CLUSTER_NAME  \
             --project=PROJECT_ID \
             --location=REGION \
             --cpus=6
          

Replace `NODE_POOL_NAME`: the name of the node pool.




The operation is denied. The output is the following:
    
    
    Operation denied by custom org policy on resource 'projects/PROJECT_ID/locations/REGION/entryGroups/org-policy-test': ["customConstraints/custom.denyHighNumvCPUs"]
    

## Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints.

Description | Constraint syntax  
---|---  
Deny a version | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.VersionDeny
        resourceTypes:
        - gkeonprem.googleapis.com/BareMetalCluster
        methodTypes:
        - CREATE
        - UPDATE
        condition: resource.bareMetalVersion.startsWith("1.29")
        actionType: DENY
        displayName: Bare metal user cluster version denied
        description: The bare metal user cluster version is no longer supported
          
  
Only allow if a key is present | 
    
    
        name: organizations/ORGANIZATION_ID/customConstraints/custom.AllowAnnotation
        resourceTypes:
        - gkeonprem.googleapis.com/BareMetalAdminCluster
        methodTypes:
        - CREATE
        - UPDATE
        condition: '"allowKey" in resource.annotations'
        actionType: ALLOW
        displayName: Bare metal admin cluster annotation keys allowed
        description: Annotation keys are allowed on bare metal admin clusters
          
  
## What's next

  * Learn more about [Organization Policy Service](https://docs.cloud.google.com/organization-policy/overview).
  * Learn more about how to [create and manage organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies).
  * See the full list of managed [organization policy constraints](https://docs.cloud.google.com/organization-policy/reference/org-policy-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
