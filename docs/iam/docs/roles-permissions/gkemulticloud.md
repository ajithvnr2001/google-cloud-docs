---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud/
title: GKE Multi-Cloud roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:34.675969+00:00
---

# GKE Multi-Cloud roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  GKE Multi-Cloud roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for GKE Multi-Cloud. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## GKE Multi-Cloud roles

Role | Permissions  
---|---  
  
#### Anthos Multi-cloud Admin 

(`roles/gkemulticloud.admin`) Admin access to Anthos Multi-cloud resources.  |  `gkemulticloud.*`

  * `gkemulticloud.attachedClusters.create`
  * `gkemulticloud.attachedClusters.createTagBinding`
  * `gkemulticloud.attachedClusters.delete`
  * `gkemulticloud.attachedClusters.deleteTagBinding`
  * `gkemulticloud.attachedClusters.generateInstallManifest`
  * `gkemulticloud.attachedClusters.get`
  * `gkemulticloud.attachedClusters.import`
  * `gkemulticloud.attachedClusters.list`
  * `gkemulticloud.attachedClusters.listEffectiveTags`
  * `gkemulticloud.attachedClusters.listTagBindings`
  * `gkemulticloud.attachedClusters.update`
  * `gkemulticloud.attachedServerConfigs.get`
  * `gkemulticloud.awsClusters.create`
  * `gkemulticloud.awsClusters.delete`
  * `gkemulticloud.awsClusters.generateAccessToken`
  * `gkemulticloud.awsClusters.get`
  * `gkemulticloud.awsClusters.getAdminKubeconfig`
  * `gkemulticloud.awsClusters.list`
  * `gkemulticloud.awsClusters.update`
  * `gkemulticloud.awsNodePools.create`
  * `gkemulticloud.awsNodePools.delete`
  * `gkemulticloud.awsNodePools.get`
  * `gkemulticloud.awsNodePools.list`
  * `gkemulticloud.awsNodePools.update`
  * `gkemulticloud.awsServerConfigs.get`
  * `gkemulticloud.azureClients.create`
  * `gkemulticloud.azureClients.delete`
  * `gkemulticloud.azureClients.get`
  * `gkemulticloud.azureClients.list`
  * `gkemulticloud.azureClusters.create`
  * `gkemulticloud.azureClusters.delete`
  * `gkemulticloud.azureClusters.generateAccessToken`
  * `gkemulticloud.azureClusters.get`
  * `gkemulticloud.azureClusters.getAdminKubeconfig`
  * `gkemulticloud.azureClusters.list`
  * `gkemulticloud.azureClusters.update`
  * `gkemulticloud.azureNodePools.create`
  * `gkemulticloud.azureNodePools.delete`
  * `gkemulticloud.azureNodePools.get`
  * `gkemulticloud.azureNodePools.list`
  * `gkemulticloud.azureNodePools.update`
  * `gkemulticloud.azureServerConfigs.get`
  * `gkemulticloud.operations.cancel`
  * `gkemulticloud.operations.delete`
  * `gkemulticloud.operations.get`
  * `gkemulticloud.operations.list`
  * `gkemulticloud.operations.wait`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Anthos Multi-cloud Editor 

(`roles/gkemulticloud.editor`) Editor role for Anthos Multi-cloud  |  `gkemulticloud.attachedClusters.create` `gkemulticloud.attachedClusters.delete` `gkemulticloud.attachedClusters.generateInstallManifest` `gkemulticloud.attachedClusters.get` `gkemulticloud.attachedClusters.import` `gkemulticloud.attachedClusters.list` `gkemulticloud.attachedClusters.listEffectiveTags` `gkemulticloud.attachedClusters.listTagBindings` `gkemulticloud.attachedClusters.update` `gkemulticloud.attachedServerConfigs.get` `gkemulticloud.awsClusters.create` `gkemulticloud.awsClusters.delete` `gkemulticloud.awsClusters.generateAccessToken` `gkemulticloud.awsClusters.get` `gkemulticloud.awsClusters.list` `gkemulticloud.awsClusters.update` `gkemulticloud.awsNodePools.*`

  * `gkemulticloud.awsNodePools.create`
  * `gkemulticloud.awsNodePools.delete`
  * `gkemulticloud.awsNodePools.get`
  * `gkemulticloud.awsNodePools.list`
  * `gkemulticloud.awsNodePools.update`

`gkemulticloud.awsServerConfigs.get` `gkemulticloud.azureClients.*`

  * `gkemulticloud.azureClients.create`
  * `gkemulticloud.azureClients.delete`
  * `gkemulticloud.azureClients.get`
  * `gkemulticloud.azureClients.list`

`gkemulticloud.azureClusters.create` `gkemulticloud.azureClusters.delete` `gkemulticloud.azureClusters.generateAccessToken` `gkemulticloud.azureClusters.get` `gkemulticloud.azureClusters.list` `gkemulticloud.azureClusters.update` `gkemulticloud.azureNodePools.*`

  * `gkemulticloud.azureNodePools.create`
  * `gkemulticloud.azureNodePools.delete`
  * `gkemulticloud.azureNodePools.get`
  * `gkemulticloud.azureNodePools.list`
  * `gkemulticloud.azureNodePools.update`

`gkemulticloud.azureServerConfigs.get` `gkemulticloud.operations.*`

  * `gkemulticloud.operations.cancel`
  * `gkemulticloud.operations.delete`
  * `gkemulticloud.operations.get`
  * `gkemulticloud.operations.list`
  * `gkemulticloud.operations.wait`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Anthos Multi-cloud Viewer 

(`roles/gkemulticloud.viewer`) Viewer access to Anthos Multi-cloud resources.  |  `gkemulticloud.attachedClusters.generateInstallManifest` `gkemulticloud.attachedClusters.get` `gkemulticloud.attachedClusters.list` `gkemulticloud.attachedClusters.listEffectiveTags` `gkemulticloud.attachedClusters.listTagBindings` `gkemulticloud.attachedServerConfigs.get` `gkemulticloud.awsClusters.generateAccessToken` `gkemulticloud.awsClusters.get` `gkemulticloud.awsClusters.list` `gkemulticloud.awsNodePools.get` `gkemulticloud.awsNodePools.list` `gkemulticloud.awsServerConfigs.get` `gkemulticloud.azureClients.get` `gkemulticloud.azureClients.list` `gkemulticloud.azureClusters.generateAccessToken` `gkemulticloud.azureClusters.get` `gkemulticloud.azureClusters.list` `gkemulticloud.azureNodePools.get` `gkemulticloud.azureNodePools.list` `gkemulticloud.azureServerConfigs.get` `gkemulticloud.operations.get` `gkemulticloud.operations.list` `gkemulticloud.operations.wait` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Anthos Multi-cloud Telemetry Writer 

(`roles/gkemulticloud.telemetryWriter`) Grant access to write cluster telemetry data such as logs, metrics, and resource metadata.  |  `kubernetesmetadata.*`

  * `kubernetesmetadata.metadata.config`
  * `kubernetesmetadata.metadata.publish`
  * `kubernetesmetadata.metadata.snapshot`

`logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `opsconfigmonitoring.resourceMetadata.write`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Anthos Multi-Cloud Container Service Agent 

(`roles/gkemulticloud.containerServiceAgent`) Grants the Anthos Multi-Cloud Container Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `binaryauthorization.platformPolicies.evaluatePolicy` `binaryauthorization.platformPolicies.get` `binaryauthorization.platformPolicies.list` `binaryauthorization.policy.evaluatePolicy` `binaryauthorization.policy.get` `cloudnotifications.activities.list` `kubernetesmetadata.*`

  * `kubernetesmetadata.metadata.config`
  * `kubernetesmetadata.metadata.publish`
  * `kubernetesmetadata.metadata.snapshot`

`logging.logEntries.create` `logging.logEntries.route` `monitoring.alertPolicies.get` `monitoring.alertPolicies.list` `monitoring.alertPolicies.listEffectiveTags` `monitoring.alertPolicies.listTagBindings` `monitoring.alerts.*`

  * `monitoring.alerts.get`
  * `monitoring.alerts.list`

`monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.dashboards.listEffectiveTags` `monitoring.dashboards.listTagBindings` `monitoring.groups.get` `monitoring.groups.list` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.notificationChannelDescriptors.*`

  * `monitoring.notificationChannelDescriptors.get`
  * `monitoring.notificationChannelDescriptors.list`

`monitoring.notificationChannels.get` `monitoring.notificationChannels.list` `monitoring.services.get` `monitoring.services.list` `monitoring.slos.get` `monitoring.slos.list` `monitoring.snoozes.get` `monitoring.snoozes.list` `monitoring.timeSeries.*`

  * `monitoring.timeSeries.create`
  * `monitoring.timeSeries.list`

`monitoring.uptimeCheckConfigs.get` `monitoring.uptimeCheckConfigs.list` `opsconfigmonitoring.*`

  * `opsconfigmonitoring.resourceMetadata.list`
  * `opsconfigmonitoring.resourceMetadata.write`

`resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.services.use` `stackdriver.projects.get` `stackdriver.resourceMetadata.list`  
  
#### Anthos Multi-Cloud Control Plane Machine Service Agent 

(`roles/gkemulticloud.controlPlaneMachineServiceAgent`) Grants the Anthos Multi-Cloud Control Plane Machine Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.dockerimages.get` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `serviceusage.services.use`  
  
#### Anthos Multi-Cloud Node Pool Machine Service Agent 

(`roles/gkemulticloud.nodePoolMachineServiceAgent`) Grants the Anthos Multi-Cloud Node Pool Machine Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.dockerimages.get` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `serviceusage.services.use`  
  
#### Anthos Multi-Cloud Service Agent 

(`roles/gkemulticloud.serviceAgent`) Grants the Anthos Multi-Cloud Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `gkehub.endpoints.connect` `gkehub.features.*`

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

`gkehub.scopes.create` `gkehub.scopes.delete` `gkehub.scopes.get` `gkehub.scopes.getIamPolicy` `gkehub.scopes.list` `gkehub.scopes.listBoundMemberships` `gkehub.scopes.update` `gkemulticloud.awsClusters.delete` `gkemulticloud.awsNodePools.delete` `gkemulticloud.azureClients.delete` `gkemulticloud.azureClusters.delete` `gkemulticloud.azureNodePools.delete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## GKE Multi-Cloud permissions

Permission | Included in roles  
---|---  
  
#### `gkemulticloud.attachedClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.attachedClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkemulticloud.attachedClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.attachedClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkemulticloud.attachedClusters.generateInstallManifest`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.attachedClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.attachedClusters.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.attachedClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.attachedClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.attachedClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.attachedClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.attachedServerConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.awsClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.awsClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 

  
  
#### `gkemulticloud.awsClusters.generateAccessToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.awsClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 

  
  
#### `gkemulticloud.awsClusters.getAdminKubeconfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)   
  
#### `gkemulticloud.awsClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.awsClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.awsNodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.awsNodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 

  
  
#### `gkemulticloud.awsNodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.awsNodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.awsNodePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.awsServerConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureClients.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.azureClients.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 

  
  
#### `gkemulticloud.azureClients.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureClients.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.azureClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 

  
  
#### `gkemulticloud.azureClusters.generateAccessToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 

  
  
#### `gkemulticloud.azureClusters.getAdminKubeconfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)   
  
#### `gkemulticloud.azureClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.azureNodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.azureNodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Anthos Multi-Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.serviceAgent) (`roles/gkemulticloud.serviceAgent`) 

  
  
#### `gkemulticloud.azureNodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureNodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.azureNodePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.azureServerConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)   
  
#### `gkemulticloud.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkemulticloud.operations.wait`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Anthos Multi-cloud Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.admin) (`roles/gkemulticloud.admin`)  [Anthos Multi-cloud Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.editor) (`roles/gkemulticloud.editor`)  [Anthos Multi-cloud Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkemulticloud#gkemulticloud.viewer) (`roles/gkemulticloud.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
