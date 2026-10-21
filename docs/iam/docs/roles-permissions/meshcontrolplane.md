---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane/
title: Cloud Service Mesh control plane roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:06.040119+00:00
---

# Cloud Service Mesh control plane roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/meshcontrolplane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Service Mesh control plane roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Service Mesh control plane. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Service Mesh control plane roles

Cloud Service Mesh control plane offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Mesh Managed Control Plane Service Agent 

(`roles/meshcontrolplane.serviceAgent`) Anthos Service Mesh Managed Control Plane Agent  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `container.apiServices.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`

`container.auditSinks.*`

  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`

`container.backendConfigs.*`

  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`

`container.bindings.*`

  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`

`container.certificateSigningRequests.*`

  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`

`container.clusterRoleBindings.*`

  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`

`container.clusterRoles.*`

  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`

`container.clusters.get` `container.clusters.getCredentials` `container.clusters.list` `container.clusters.update` `container.componentStatuses.*`

  * `container.componentStatuses.get`
  * `container.componentStatuses.list`

`container.configMaps.*`

  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`

`container.controllerRevisions.*`

  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`

`container.cronJobs.*`

  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`

`container.csiDrivers.*`

  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`

`container.csiNodeInfos.*`

  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`

`container.csiNodes.*`

  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`

`container.customResourceDefinitions.*`

  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`

`container.daemonSets.*`

  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`

`container.deployments.*`

  * `container.deployments.create`
  * `container.deployments.delete`
  * `container.deployments.get`
  * `container.deployments.getScale`
  * `container.deployments.getStatus`
  * `container.deployments.list`
  * `container.deployments.rollback`
  * `container.deployments.update`
  * `container.deployments.updateScale`
  * `container.deployments.updateStatus`

`container.endpointSlices.*`

  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`

`container.endpoints.*`

  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`

`container.events.*`

  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`

`container.frontendConfigs.*`

  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`

`container.horizontalPodAutoscalers.*`

  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`

`container.hostServiceAgent.use` `container.ingresses.*`

  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`

`container.initializerConfigurations.*`

  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`

`container.jobs.*`

  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`

`container.leases.*`

  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`

`container.limitRanges.*`

  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`

`container.localSubjectAccessReviews.*`

  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`

`container.managedCertificates.*`

  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`

`container.mutatingWebhookConfigurations.*`

  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`

`container.namespaces.*`

  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`

`container.networkPolicies.*`

  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`

`container.nodes.*`

  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`

`container.operations.*`

  * `container.operations.get`
  * `container.operations.list`

`container.persistentVolumeClaims.*`

  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`

`container.persistentVolumes.*`

  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`

`container.petSets.*`

  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`

`container.podDisruptionBudgets.*`

  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`

`container.podPresets.*`

  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`

`container.podSecurityPolicies.*`

  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`

`container.podTemplates.*`

  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`

`container.pods.*`

  * `container.pods.attach`
  * `container.pods.create`
  * `container.pods.delete`
  * `container.pods.evict`
  * `container.pods.exec`
  * `container.pods.get`
  * `container.pods.getLogs`
  * `container.pods.getStatus`
  * `container.pods.initialize`
  * `container.pods.list`
  * `container.pods.portForward`
  * `container.pods.proxy`
  * `container.pods.update`
  * `container.pods.updateStatus`

`container.priorityClasses.*`

  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`

`container.replicaSets.*`

  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`

`container.replicationControllers.*`

  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`

`container.resourceQuotas.*`

  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`

`container.roleBindings.*`

  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`

`container.roles.*`

  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`

`container.runtimeClasses.*`

  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`

`container.scheduledJobs.*`

  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`

`container.secrets.*`

  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`

`container.selfSubjectAccessReviews.*`

  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`

`container.selfSubjectRulesReviews.create` `container.serviceAccounts.*`

  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`

`container.services.*`

  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`

`container.statefulSets.*`

  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`

`container.storageClasses.*`

  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`

`container.storageStates.*`

  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`

`container.storageVersionMigrations.*`

  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`

`container.subjectAccessReviews.*`

  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`

`container.thirdPartyObjects.*`

  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`

`container.thirdPartyResources.*`

  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`

`container.tokenReviews.create` `container.updateInfos.*`

  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`

`container.validatingWebhookConfigurations.*`

  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`

`container.volumeAttachments.*`

  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`

`container.volumeSnapshotClasses.*`

  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`

`container.volumeSnapshotContents.*`

  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`

`container.volumeSnapshots.*`

  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`gkehub.features.get` `gkehub.features.getIamPolicy` `gkehub.features.list` `gkehub.fleet.get` `gkehub.fleet.getFreeTrial` `gkehub.gateway.*`

  * `gkehub.gateway.delete`
  * `gkehub.gateway.generateCredentials`
  * `gkehub.gateway.get`
  * `gkehub.gateway.patch`
  * `gkehub.gateway.post`
  * `gkehub.gateway.put`
  * `gkehub.gateway.stream`

`gkehub.locations.*`

  * `gkehub.locations.get`
  * `gkehub.locations.list`

`gkehub.membershipbindings.get` `gkehub.membershipbindings.list` `gkehub.membershipfeatures.get` `gkehub.membershipfeatures.list` `gkehub.memberships.generateConnectManifest` `gkehub.memberships.get` `gkehub.memberships.getIamPolicy` `gkehub.memberships.list` `gkehub.namespaces.get` `gkehub.namespaces.list` `gkehub.operations.get` `gkehub.operations.list` `gkehub.rbacrolebindings.get` `gkehub.rbacrolebindings.list` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.list` `gkehub.scopes.listBoundMemberships` `logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test` `trafficdirector.*`

  * `trafficdirector.networks.getConfigs`
  * `trafficdirector.networks.reportMetrics`

  
  
## Cloud Service Mesh control plane permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
