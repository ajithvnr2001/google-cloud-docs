---
url: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/reference/roles-permissions/
title: Config Controller roles and permissions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:03.775492+00:00
---

# Config Controller roles and permissions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/reference/roles-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Controller ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/config-controller/docs/reference/roles-permissions)



Send feedback 

#  Config Controller roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles and permissions for Config Controller. To help you control access, Config Controller uses IAM roles and permissions. IAM lets you grant granular access to specific Google Cloud resources and helps prevent access to other resources.

## Roles

Config Controller has predefined roles. The following table lists these roles and the permissions that the roles include:

Role | Permissions  
---|---  
  
#### Config Controller Admin 

(`roles/krmapihosting.admin`) Full access to all Config Controller resources.  |  `krmapihosting.*`

  * `krmapihosting.krmApiHosts.create`
  * `krmapihosting.krmApiHosts.createTagBinding`
  * `krmapihosting.krmApiHosts.delete`
  * `krmapihosting.krmApiHosts.deleteTagBinding`
  * `krmapihosting.krmApiHosts.get`
  * `krmapihosting.krmApiHosts.getIamPolicy`
  * `krmapihosting.krmApiHosts.list`
  * `krmapihosting.krmApiHosts.listEffectiveTags`
  * `krmapihosting.krmApiHosts.listTagBindings`
  * `krmapihosting.krmApiHosts.setIamPolicy`
  * `krmapihosting.krmApiHosts.update`
  * `krmapihosting.locations.get`
  * `krmapihosting.locations.list`
  * `krmapihosting.operations.cancel`
  * `krmapihosting.operations.delete`
  * `krmapihosting.operations.get`
  * `krmapihosting.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Config Controller Editor 

(`roles/krmapihosting.editor`) Editor role for Config Controller  |  `krmapihosting.krmApiHosts.create` `krmapihosting.krmApiHosts.delete` `krmapihosting.krmApiHosts.get` `krmapihosting.krmApiHosts.getIamPolicy` `krmapihosting.krmApiHosts.list` `krmapihosting.krmApiHosts.listEffectiveTags` `krmapihosting.krmApiHosts.listTagBindings` `krmapihosting.krmApiHosts.update` `krmapihosting.locations.*`

  * `krmapihosting.locations.get`
  * `krmapihosting.locations.list`

`krmapihosting.operations.*`

  * `krmapihosting.operations.cancel`
  * `krmapihosting.operations.delete`
  * `krmapihosting.operations.get`
  * `krmapihosting.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Config Controller Viewer 

(`roles/krmapihosting.viewer`) Read-only access to all Config Controller resources.  |  `krmapihosting.krmApiHosts.get` `krmapihosting.krmApiHosts.getIamPolicy` `krmapihosting.krmApiHosts.list` `krmapihosting.krmApiHosts.listEffectiveTags` `krmapihosting.krmApiHosts.listTagBindings` `krmapihosting.locations.*`

  * `krmapihosting.locations.get`
  * `krmapihosting.locations.list`

`krmapihosting.operations.get` `krmapihosting.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### KRM API Hosting AnthosApiEndpoint Service Agent 

(`roles/krmapihosting.anthosApiEndpointServiceAgent`) Grants permissions to resources managed by AnthosApiEndpoint.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.instanceGroupManagers.get` `container.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`
  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`
  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`
  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`
  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`
  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`
  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`
  * `container.clusters.connect`
  * `container.clusters.create`
  * `container.clusters.createTagBinding`
  * `container.clusters.delete`
  * `container.clusters.deleteTagBinding`
  * `container.clusters.get`
  * `container.clusters.getCredentials`
  * `container.clusters.impersonate`
  * `container.clusters.list`
  * `container.clusters.listEffectiveTags`
  * `container.clusters.listTagBindings`
  * `container.clusters.update`
  * `container.componentStatuses.get`
  * `container.componentStatuses.list`
  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`
  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`
  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`
  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`
  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`
  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`
  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`
  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`
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
  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`
  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`
  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`
  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`
  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`
  * `container.hostServiceAgent.use`
  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`
  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`
  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`
  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`
  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`
  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`
  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`
  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`
  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`
  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`
  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`
  * `container.operations.get`
  * `container.operations.list`
  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`
  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`
  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`
  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`
  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`
  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`
  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`
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
  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`
  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`
  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`
  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`
  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`
  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`
  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`
  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`
  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`
  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`
  * `container.selfSubjectRulesReviews.create`
  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`
  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`
  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`
  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`
  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`
  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`
  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`
  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`
  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`
  * `container.tokenReviews.create`
  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`
  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`
  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`
  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`
  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`
  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`gkehub.endpoints.connect` `gkehub.features.*`

  * `gkehub.features.create`
  * `gkehub.features.delete`
  * `gkehub.features.get`
  * `gkehub.features.getIamPolicy`
  * `gkehub.features.list`
  * `gkehub.features.setIamPolicy`
  * `gkehub.features.update`

`gkehub.fleet.*`

  * `gkehub.fleet.create`
  * `gkehub.fleet.createFreeTrial`
  * `gkehub.fleet.delete`
  * `gkehub.fleet.get`
  * `gkehub.fleet.getFreeTrial`
  * `gkehub.fleet.update`
  * `gkehub.fleet.updateFreeTrial`

`gkehub.gateway.*`

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

`gkehub.membershipbindings.*`

  * `gkehub.membershipbindings.create`
  * `gkehub.membershipbindings.delete`
  * `gkehub.membershipbindings.get`
  * `gkehub.membershipbindings.list`
  * `gkehub.membershipbindings.update`

`gkehub.membershipfeatures.*`

  * `gkehub.membershipfeatures.create`
  * `gkehub.membershipfeatures.delete`
  * `gkehub.membershipfeatures.get`
  * `gkehub.membershipfeatures.list`
  * `gkehub.membershipfeatures.update`

`gkehub.memberships.*`

  * `gkehub.memberships.create`
  * `gkehub.memberships.delete`
  * `gkehub.memberships.generateConnectManifest`
  * `gkehub.memberships.get`
  * `gkehub.memberships.getIamPolicy`
  * `gkehub.memberships.list`
  * `gkehub.memberships.setIamPolicy`
  * `gkehub.memberships.update`

`gkehub.namespaces.*`

  * `gkehub.namespaces.create`
  * `gkehub.namespaces.delete`
  * `gkehub.namespaces.get`
  * `gkehub.namespaces.list`
  * `gkehub.namespaces.update`

`gkehub.operations.*`

  * `gkehub.operations.cancel`
  * `gkehub.operations.delete`
  * `gkehub.operations.get`
  * `gkehub.operations.list`

`gkehub.rbacrolebindings.*`

  * `gkehub.rbacrolebindings.create`
  * `gkehub.rbacrolebindings.delete`
  * `gkehub.rbacrolebindings.get`
  * `gkehub.rbacrolebindings.list`
  * `gkehub.rbacrolebindings.update`

`gkehub.scopes.create` `gkehub.scopes.delete` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.list` `gkehub.scopes.listBoundMemberships` `gkehub.scopes.update` `iam.serviceAccounts.actAs` `meshconfig.projects.init` `recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.projects.setIamPolicy` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.use` `serviceusage.values.test`  
  
#### KRM API Hosting Service Agent 

(`roles/krmapihosting.serviceAgent`) Gives KRM API Hosting service account access to managed resource.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.instanceGroupManagers.get` `compute.regions.get` `container.*`

  * `container.apiServices.create`
  * `container.apiServices.delete`
  * `container.apiServices.get`
  * `container.apiServices.getStatus`
  * `container.apiServices.list`
  * `container.apiServices.update`
  * `container.apiServices.updateStatus`
  * `container.auditSinks.create`
  * `container.auditSinks.delete`
  * `container.auditSinks.get`
  * `container.auditSinks.list`
  * `container.auditSinks.update`
  * `container.backendConfigs.create`
  * `container.backendConfigs.delete`
  * `container.backendConfigs.get`
  * `container.backendConfigs.list`
  * `container.backendConfigs.update`
  * `container.bindings.create`
  * `container.bindings.delete`
  * `container.bindings.get`
  * `container.bindings.list`
  * `container.bindings.update`
  * `container.certificateSigningRequests.approve`
  * `container.certificateSigningRequests.create`
  * `container.certificateSigningRequests.delete`
  * `container.certificateSigningRequests.get`
  * `container.certificateSigningRequests.getStatus`
  * `container.certificateSigningRequests.list`
  * `container.certificateSigningRequests.update`
  * `container.certificateSigningRequests.updateStatus`
  * `container.clusterRoleBindings.create`
  * `container.clusterRoleBindings.delete`
  * `container.clusterRoleBindings.get`
  * `container.clusterRoleBindings.list`
  * `container.clusterRoleBindings.update`
  * `container.clusterRoles.bind`
  * `container.clusterRoles.create`
  * `container.clusterRoles.delete`
  * `container.clusterRoles.escalate`
  * `container.clusterRoles.get`
  * `container.clusterRoles.list`
  * `container.clusterRoles.update`
  * `container.clusters.connect`
  * `container.clusters.create`
  * `container.clusters.createTagBinding`
  * `container.clusters.delete`
  * `container.clusters.deleteTagBinding`
  * `container.clusters.get`
  * `container.clusters.getCredentials`
  * `container.clusters.impersonate`
  * `container.clusters.list`
  * `container.clusters.listEffectiveTags`
  * `container.clusters.listTagBindings`
  * `container.clusters.update`
  * `container.componentStatuses.get`
  * `container.componentStatuses.list`
  * `container.configMaps.create`
  * `container.configMaps.delete`
  * `container.configMaps.get`
  * `container.configMaps.list`
  * `container.configMaps.update`
  * `container.controllerRevisions.create`
  * `container.controllerRevisions.delete`
  * `container.controllerRevisions.get`
  * `container.controllerRevisions.list`
  * `container.controllerRevisions.update`
  * `container.cronJobs.create`
  * `container.cronJobs.delete`
  * `container.cronJobs.get`
  * `container.cronJobs.getStatus`
  * `container.cronJobs.list`
  * `container.cronJobs.update`
  * `container.cronJobs.updateStatus`
  * `container.csiDrivers.create`
  * `container.csiDrivers.delete`
  * `container.csiDrivers.get`
  * `container.csiDrivers.list`
  * `container.csiDrivers.update`
  * `container.csiNodeInfos.create`
  * `container.csiNodeInfos.delete`
  * `container.csiNodeInfos.get`
  * `container.csiNodeInfos.list`
  * `container.csiNodeInfos.update`
  * `container.csiNodes.create`
  * `container.csiNodes.delete`
  * `container.csiNodes.get`
  * `container.csiNodes.list`
  * `container.csiNodes.update`
  * `container.customResourceDefinitions.create`
  * `container.customResourceDefinitions.delete`
  * `container.customResourceDefinitions.get`
  * `container.customResourceDefinitions.getStatus`
  * `container.customResourceDefinitions.list`
  * `container.customResourceDefinitions.update`
  * `container.customResourceDefinitions.updateStatus`
  * `container.daemonSets.create`
  * `container.daemonSets.delete`
  * `container.daemonSets.get`
  * `container.daemonSets.getStatus`
  * `container.daemonSets.list`
  * `container.daemonSets.update`
  * `container.daemonSets.updateStatus`
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
  * `container.endpointSlices.create`
  * `container.endpointSlices.delete`
  * `container.endpointSlices.get`
  * `container.endpointSlices.list`
  * `container.endpointSlices.update`
  * `container.endpoints.create`
  * `container.endpoints.delete`
  * `container.endpoints.get`
  * `container.endpoints.list`
  * `container.endpoints.update`
  * `container.events.create`
  * `container.events.delete`
  * `container.events.get`
  * `container.events.list`
  * `container.events.update`
  * `container.frontendConfigs.create`
  * `container.frontendConfigs.delete`
  * `container.frontendConfigs.get`
  * `container.frontendConfigs.list`
  * `container.frontendConfigs.update`
  * `container.horizontalPodAutoscalers.create`
  * `container.horizontalPodAutoscalers.delete`
  * `container.horizontalPodAutoscalers.get`
  * `container.horizontalPodAutoscalers.getStatus`
  * `container.horizontalPodAutoscalers.list`
  * `container.horizontalPodAutoscalers.update`
  * `container.horizontalPodAutoscalers.updateStatus`
  * `container.hostServiceAgent.use`
  * `container.ingresses.create`
  * `container.ingresses.delete`
  * `container.ingresses.get`
  * `container.ingresses.getStatus`
  * `container.ingresses.list`
  * `container.ingresses.update`
  * `container.ingresses.updateStatus`
  * `container.initializerConfigurations.create`
  * `container.initializerConfigurations.delete`
  * `container.initializerConfigurations.get`
  * `container.initializerConfigurations.list`
  * `container.initializerConfigurations.update`
  * `container.jobs.create`
  * `container.jobs.delete`
  * `container.jobs.get`
  * `container.jobs.getStatus`
  * `container.jobs.list`
  * `container.jobs.update`
  * `container.jobs.updateStatus`
  * `container.leases.create`
  * `container.leases.delete`
  * `container.leases.get`
  * `container.leases.list`
  * `container.leases.update`
  * `container.limitRanges.create`
  * `container.limitRanges.delete`
  * `container.limitRanges.get`
  * `container.limitRanges.list`
  * `container.limitRanges.update`
  * `container.localSubjectAccessReviews.create`
  * `container.localSubjectAccessReviews.list`
  * `container.managedCertificates.create`
  * `container.managedCertificates.delete`
  * `container.managedCertificates.get`
  * `container.managedCertificates.list`
  * `container.managedCertificates.update`
  * `container.mutatingWebhookConfigurations.create`
  * `container.mutatingWebhookConfigurations.delete`
  * `container.mutatingWebhookConfigurations.get`
  * `container.mutatingWebhookConfigurations.list`
  * `container.mutatingWebhookConfigurations.update`
  * `container.namespaces.create`
  * `container.namespaces.delete`
  * `container.namespaces.finalize`
  * `container.namespaces.get`
  * `container.namespaces.getStatus`
  * `container.namespaces.list`
  * `container.namespaces.update`
  * `container.namespaces.updateStatus`
  * `container.networkPolicies.create`
  * `container.networkPolicies.delete`
  * `container.networkPolicies.get`
  * `container.networkPolicies.list`
  * `container.networkPolicies.update`
  * `container.nodes.create`
  * `container.nodes.delete`
  * `container.nodes.get`
  * `container.nodes.getStatus`
  * `container.nodes.list`
  * `container.nodes.proxy`
  * `container.nodes.update`
  * `container.nodes.updateStatus`
  * `container.operations.get`
  * `container.operations.list`
  * `container.persistentVolumeClaims.create`
  * `container.persistentVolumeClaims.delete`
  * `container.persistentVolumeClaims.get`
  * `container.persistentVolumeClaims.getStatus`
  * `container.persistentVolumeClaims.list`
  * `container.persistentVolumeClaims.update`
  * `container.persistentVolumeClaims.updateStatus`
  * `container.persistentVolumes.create`
  * `container.persistentVolumes.delete`
  * `container.persistentVolumes.get`
  * `container.persistentVolumes.getStatus`
  * `container.persistentVolumes.list`
  * `container.persistentVolumes.update`
  * `container.persistentVolumes.updateStatus`
  * `container.petSets.create`
  * `container.petSets.delete`
  * `container.petSets.get`
  * `container.petSets.list`
  * `container.petSets.update`
  * `container.petSets.updateStatus`
  * `container.podDisruptionBudgets.create`
  * `container.podDisruptionBudgets.delete`
  * `container.podDisruptionBudgets.get`
  * `container.podDisruptionBudgets.getStatus`
  * `container.podDisruptionBudgets.list`
  * `container.podDisruptionBudgets.update`
  * `container.podDisruptionBudgets.updateStatus`
  * `container.podPresets.create`
  * `container.podPresets.delete`
  * `container.podPresets.get`
  * `container.podPresets.list`
  * `container.podPresets.update`
  * `container.podSecurityPolicies.create`
  * `container.podSecurityPolicies.delete`
  * `container.podSecurityPolicies.get`
  * `container.podSecurityPolicies.list`
  * `container.podSecurityPolicies.update`
  * `container.podSecurityPolicies.use`
  * `container.podTemplates.create`
  * `container.podTemplates.delete`
  * `container.podTemplates.get`
  * `container.podTemplates.list`
  * `container.podTemplates.update`
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
  * `container.priorityClasses.create`
  * `container.priorityClasses.delete`
  * `container.priorityClasses.get`
  * `container.priorityClasses.list`
  * `container.priorityClasses.update`
  * `container.replicaSets.create`
  * `container.replicaSets.delete`
  * `container.replicaSets.get`
  * `container.replicaSets.getScale`
  * `container.replicaSets.getStatus`
  * `container.replicaSets.list`
  * `container.replicaSets.update`
  * `container.replicaSets.updateScale`
  * `container.replicaSets.updateStatus`
  * `container.replicationControllers.create`
  * `container.replicationControllers.delete`
  * `container.replicationControllers.get`
  * `container.replicationControllers.getScale`
  * `container.replicationControllers.getStatus`
  * `container.replicationControllers.list`
  * `container.replicationControllers.update`
  * `container.replicationControllers.updateScale`
  * `container.replicationControllers.updateStatus`
  * `container.resourceQuotas.create`
  * `container.resourceQuotas.delete`
  * `container.resourceQuotas.get`
  * `container.resourceQuotas.getStatus`
  * `container.resourceQuotas.list`
  * `container.resourceQuotas.update`
  * `container.resourceQuotas.updateStatus`
  * `container.roleBindings.create`
  * `container.roleBindings.delete`
  * `container.roleBindings.get`
  * `container.roleBindings.list`
  * `container.roleBindings.update`
  * `container.roles.bind`
  * `container.roles.create`
  * `container.roles.delete`
  * `container.roles.escalate`
  * `container.roles.get`
  * `container.roles.list`
  * `container.roles.update`
  * `container.runtimeClasses.create`
  * `container.runtimeClasses.delete`
  * `container.runtimeClasses.get`
  * `container.runtimeClasses.list`
  * `container.runtimeClasses.update`
  * `container.scheduledJobs.create`
  * `container.scheduledJobs.delete`
  * `container.scheduledJobs.get`
  * `container.scheduledJobs.list`
  * `container.scheduledJobs.update`
  * `container.scheduledJobs.updateStatus`
  * `container.secrets.create`
  * `container.secrets.delete`
  * `container.secrets.get`
  * `container.secrets.list`
  * `container.secrets.update`
  * `container.selfSubjectAccessReviews.create`
  * `container.selfSubjectAccessReviews.list`
  * `container.selfSubjectRulesReviews.create`
  * `container.serviceAccounts.create`
  * `container.serviceAccounts.createToken`
  * `container.serviceAccounts.delete`
  * `container.serviceAccounts.get`
  * `container.serviceAccounts.list`
  * `container.serviceAccounts.update`
  * `container.services.create`
  * `container.services.delete`
  * `container.services.get`
  * `container.services.getStatus`
  * `container.services.list`
  * `container.services.proxy`
  * `container.services.update`
  * `container.services.updateStatus`
  * `container.statefulSets.create`
  * `container.statefulSets.delete`
  * `container.statefulSets.get`
  * `container.statefulSets.getScale`
  * `container.statefulSets.getStatus`
  * `container.statefulSets.list`
  * `container.statefulSets.update`
  * `container.statefulSets.updateScale`
  * `container.statefulSets.updateStatus`
  * `container.storageClasses.create`
  * `container.storageClasses.delete`
  * `container.storageClasses.get`
  * `container.storageClasses.list`
  * `container.storageClasses.update`
  * `container.storageStates.create`
  * `container.storageStates.delete`
  * `container.storageStates.get`
  * `container.storageStates.getStatus`
  * `container.storageStates.list`
  * `container.storageStates.update`
  * `container.storageStates.updateStatus`
  * `container.storageVersionMigrations.create`
  * `container.storageVersionMigrations.delete`
  * `container.storageVersionMigrations.get`
  * `container.storageVersionMigrations.getStatus`
  * `container.storageVersionMigrations.list`
  * `container.storageVersionMigrations.update`
  * `container.storageVersionMigrations.updateStatus`
  * `container.subjectAccessReviews.create`
  * `container.subjectAccessReviews.list`
  * `container.thirdPartyObjects.create`
  * `container.thirdPartyObjects.delete`
  * `container.thirdPartyObjects.get`
  * `container.thirdPartyObjects.list`
  * `container.thirdPartyObjects.update`
  * `container.thirdPartyResources.create`
  * `container.thirdPartyResources.delete`
  * `container.thirdPartyResources.get`
  * `container.thirdPartyResources.list`
  * `container.thirdPartyResources.update`
  * `container.tokenReviews.create`
  * `container.updateInfos.create`
  * `container.updateInfos.delete`
  * `container.updateInfos.get`
  * `container.updateInfos.list`
  * `container.updateInfos.update`
  * `container.validatingWebhookConfigurations.create`
  * `container.validatingWebhookConfigurations.delete`
  * `container.validatingWebhookConfigurations.get`
  * `container.validatingWebhookConfigurations.list`
  * `container.validatingWebhookConfigurations.update`
  * `container.volumeAttachments.create`
  * `container.volumeAttachments.delete`
  * `container.volumeAttachments.get`
  * `container.volumeAttachments.getStatus`
  * `container.volumeAttachments.list`
  * `container.volumeAttachments.update`
  * `container.volumeAttachments.updateStatus`
  * `container.volumeSnapshotClasses.create`
  * `container.volumeSnapshotClasses.delete`
  * `container.volumeSnapshotClasses.get`
  * `container.volumeSnapshotClasses.list`
  * `container.volumeSnapshotClasses.update`
  * `container.volumeSnapshotContents.create`
  * `container.volumeSnapshotContents.delete`
  * `container.volumeSnapshotContents.get`
  * `container.volumeSnapshotContents.getStatus`
  * `container.volumeSnapshotContents.list`
  * `container.volumeSnapshotContents.update`
  * `container.volumeSnapshotContents.updateStatus`
  * `container.volumeSnapshots.create`
  * `container.volumeSnapshots.delete`
  * `container.volumeSnapshots.get`
  * `container.volumeSnapshots.getStatus`
  * `container.volumeSnapshots.list`
  * `container.volumeSnapshots.update`
  * `container.volumeSnapshots.updateStatus`

`iam.serviceAccounts.actAs` `recommender.containerDiagnosisInsights.*`

  * `recommender.containerDiagnosisInsights.get`
  * `recommender.containerDiagnosisInsights.list`
  * `recommender.containerDiagnosisInsights.update`

`recommender.containerDiagnosisRecommendations.*`

  * `recommender.containerDiagnosisRecommendations.get`
  * `recommender.containerDiagnosisRecommendations.list`
  * `recommender.containerDiagnosisRecommendations.update`

`recommender.locations.*`

  * `recommender.locations.get`
  * `recommender.locations.list`

`recommender.networkAnalyzerGkeConnectivityInsights.*`

  * `recommender.networkAnalyzerGkeConnectivityInsights.get`
  * `recommender.networkAnalyzerGkeConnectivityInsights.list`
  * `recommender.networkAnalyzerGkeConnectivityInsights.update`

`recommender.networkAnalyzerGkeIpAddressInsights.*`

  * `recommender.networkAnalyzerGkeIpAddressInsights.get`
  * `recommender.networkAnalyzerGkeIpAddressInsights.list`
  * `recommender.networkAnalyzerGkeIpAddressInsights.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.services.use`  
  
For more information on how you should assign roles, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles). Or you can [create your own custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that contain exactly the permissions that you specify.

## Permissions

### Permissions granted by roles

The following table lists the permissions that the caller must have to call each Config Controller method and which roles grant the permissions:

Permission | Granted by roles  
---|---  
`krmapihosting.krmApiHosts.create` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.krmApiHosts.delete` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.krmApiHosts.get` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.krmApiHosts.getIamPolicy` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Security Reviewer (`roles/iam.securityReviewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.krmApiHosts.list` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Security Reviewer (`roles/iam.securityReviewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.krmApiHosts.setIamPolicy` | 

  * Owner (`roles/owner`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.krmApiHosts.update` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.locations.get` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Viewer (`roles/viewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.locations.list` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Viewer (`roles/viewer`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Security Reviewer (`roles/iam.securityReviewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.operations.cancel` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.operations.delete` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Config Controller Admin (`roles/krmapihosting.admin`)

  
`krmapihosting.operations.get` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Viewer (`roles/viewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
`krmapihosting.operations.list` | 

  * Owner (`roles/owner`)
  * Editor (`roles/editor`)
  * Viewer (`roles/viewer`)
  * Security Admin (`roles/iam.securityAdmin`)
  * Security Reviewer (`roles/iam.securityReviewer`)
  * Config Controller Admin (`roles/krmapihosting.admin`)
  * Config Controller Viewer (`roles/krmapihosting.viewer`)

  
  
### Permissions needed for actions

The following table lists which permission you need to perform specific actions.

Required permission | Method  
---|---  
`krmapihosting.krmApiHosts.create` | `projects.locations.krmApiHosts.create`  
`krmapihosting.krmApiHosts.delete` | `projects.locations.krmApiHosts.delete`  
`krmapihosting.krmApiHosts.get` | `projects.locations.krmApiHosts.get`  
`krmapihosting.krmApiHosts.list` | `projects.locations.krmApiHosts.list`  
`krmapihosting.krmApiHosts.update` | `projects.locations.krmApiHosts.update`  
`krmapihosting.operations.get` | `projects.locations.operations.get`  
`krmapihosting.operations.list` | `projects.locations.operations.list`  
  
## What's next

  * Learn about [IAM](https://docs.cloud.google.com/iam/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
