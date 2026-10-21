---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting/
title: KRM API Hosting roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:08.491416+00:00
---

# KRM API Hosting roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  KRM API Hosting roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for KRM API Hosting. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## KRM API Hosting roles

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

`resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.list` `resourcemanager.projects.setIamPolicy` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.services.use` `serviceusage.values.test`  
  
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
  
## KRM API Hosting permissions

Permission | Included in roles  
---|---  
  
#### `krmapihosting.krmApiHosts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)   
  
#### `krmapihosting.krmApiHosts.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `krmapihosting.krmApiHosts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)   
  
#### `krmapihosting.krmApiHosts.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `krmapihosting.krmApiHosts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.krmApiHosts.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.krmApiHosts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.krmApiHosts.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.krmApiHosts.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.krmApiHosts.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)   
  
#### `krmapihosting.krmApiHosts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)   
  
#### `krmapihosting.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)   
  
#### `krmapihosting.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)   
  
#### `krmapihosting.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `krmapihosting.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Config Controller Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.admin) (`roles/krmapihosting.admin`)  [Config Controller Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.editor) (`roles/krmapihosting.editor`)  [Config Controller Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/krmapihosting#krmapihosting.viewer) (`roles/krmapihosting.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
