---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/apihub/
title: API Hub roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:31.524428+00:00
---

# API Hub roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/apihub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  API Hub roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for API Hub. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## API Hub roles

Role | Permissions  
---|---  
  
#### Cloud API Hub Admin 

(`roles/apihub.admin`) Full access to all API hub resources.  |  `apigee.projectorganizations.get` `apihub.*`

  * `apihub.addons.get`
  * `apihub.addons.list`
  * `apihub.addons.manage`
  * `apihub.apiHubInstances.create`
  * `apihub.apiHubInstances.delete`
  * `apihub.apiHubInstances.get`
  * `apihub.apiHubInstances.list`
  * `apihub.apiHubInstances.update`
  * `apihub.apiOperations.create`
  * `apihub.apiOperations.delete`
  * `apihub.apiOperations.get`
  * `apihub.apiOperations.list`
  * `apihub.apiOperations.listAll`
  * `apihub.apiOperations.update`
  * `apihub.apis.create`
  * `apihub.apis.createTagBinding`
  * `apihub.apis.delete`
  * `apihub.apis.deleteTagBinding`
  * `apihub.apis.get`
  * `apihub.apis.list`
  * `apihub.apis.listEffectiveTags`
  * `apihub.apis.listTagBindings`
  * `apihub.apis.update`
  * `apihub.attributes.create`
  * `apihub.attributes.delete`
  * `apihub.attributes.get`
  * `apihub.attributes.list`
  * `apihub.attributes.update`
  * `apihub.curations.create`
  * `apihub.curations.delete`
  * `apihub.curations.get`
  * `apihub.curations.list`
  * `apihub.curations.update`
  * `apihub.definitions.get`
  * `apihub.definitions.list`
  * `apihub.definitions.update`
  * `apihub.dependencies.create`
  * `apihub.dependencies.delete`
  * `apihub.dependencies.get`
  * `apihub.dependencies.list`
  * `apihub.dependencies.update`
  * `apihub.deployments.create`
  * `apihub.deployments.createTagBinding`
  * `apihub.deployments.delete`
  * `apihub.deployments.deleteTagBinding`
  * `apihub.deployments.get`
  * `apihub.deployments.list`
  * `apihub.deployments.listEffectiveTags`
  * `apihub.deployments.listTagBindings`
  * `apihub.deployments.update`
  * `apihub.discoveredApiObservations.get`
  * `apihub.discoveredApiObservations.list`
  * `apihub.discoveredApiOperations.get`
  * `apihub.discoveredApiOperations.list`
  * `apihub.externalApis.create`
  * `apihub.externalApis.delete`
  * `apihub.externalApis.get`
  * `apihub.externalApis.list`
  * `apihub.externalApis.update`
  * `apihub.hostProjectRegistrations.create`
  * `apihub.hostProjectRegistrations.delete`
  * `apihub.hostProjectRegistrations.get`
  * `apihub.hostProjectRegistrations.list`
  * `apihub.hostProjectRegistrations.register`
  * `apihub.llmEnablements.deregister`
  * `apihub.llmEnablements.get`
  * `apihub.llmEnablements.list`
  * `apihub.llmEnablements.register`
  * `apihub.locations.collectApiData`
  * `apihub.locations.getApiInsights`
  * `apihub.locations.searchResources`
  * `apihub.locations2.searchResources`
  * `apihub.operations.cancel`
  * `apihub.operations.delete`
  * `apihub.operations.get`
  * `apihub.operations.list`
  * `apihub.plugininstances.applyConfig`
  * `apihub.plugininstances.create`
  * `apihub.plugininstances.delete`
  * `apihub.plugininstances.disable`
  * `apihub.plugininstances.enable`
  * `apihub.plugininstances.execute`
  * `apihub.plugininstances.get`
  * `apihub.plugininstances.list`
  * `apihub.plugininstances.managePluginInstanceSourceData`
  * `apihub.plugininstances.update`
  * `apihub.plugins.create`
  * `apihub.plugins.delete`
  * `apihub.plugins.disable`
  * `apihub.plugins.enable`
  * `apihub.plugins.get`
  * `apihub.plugins.list`
  * `apihub.runTimeProjectAttachments.attach`
  * `apihub.runTimeProjectAttachments.create`
  * `apihub.runTimeProjectAttachments.delete`
  * `apihub.runTimeProjectAttachments.get`
  * `apihub.runTimeProjectAttachments.list`
  * `apihub.runTimeProjectAttachments.lookup`
  * `apihub.specs.create`
  * `apihub.specs.delete`
  * `apihub.specs.get`
  * `apihub.specs.lint`
  * `apihub.specs.list`
  * `apihub.specs.listAll`
  * `apihub.specs.update`
  * `apihub.styleGuides.get`
  * `apihub.styleGuides.update`
  * `apihub.versions.create`
  * `apihub.versions.delete`
  * `apihub.versions.get`
  * `apihub.versions.list`
  * `apihub.versions.listAll`
  * `apihub.versions.update`

`cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API Hub Editor 

(`roles/apihub.editor`) Edit access to most of Cloud API Hub resources.  |  `apihub.addons.get` `apihub.addons.list` `apihub.apiHubInstances.get` `apihub.apiHubInstances.list` `apihub.apiOperations.*`

  * `apihub.apiOperations.create`
  * `apihub.apiOperations.delete`
  * `apihub.apiOperations.get`
  * `apihub.apiOperations.list`
  * `apihub.apiOperations.listAll`
  * `apihub.apiOperations.update`

`apihub.apis.*`

  * `apihub.apis.create`
  * `apihub.apis.createTagBinding`
  * `apihub.apis.delete`
  * `apihub.apis.deleteTagBinding`
  * `apihub.apis.get`
  * `apihub.apis.list`
  * `apihub.apis.listEffectiveTags`
  * `apihub.apis.listTagBindings`
  * `apihub.apis.update`

`apihub.attributes.get` `apihub.attributes.list` `apihub.curations.get` `apihub.curations.list` `apihub.definitions.*`

  * `apihub.definitions.get`
  * `apihub.definitions.list`
  * `apihub.definitions.update`

`apihub.dependencies.*`

  * `apihub.dependencies.create`
  * `apihub.dependencies.delete`
  * `apihub.dependencies.get`
  * `apihub.dependencies.list`
  * `apihub.dependencies.update`

`apihub.deployments.*`

  * `apihub.deployments.create`
  * `apihub.deployments.createTagBinding`
  * `apihub.deployments.delete`
  * `apihub.deployments.deleteTagBinding`
  * `apihub.deployments.get`
  * `apihub.deployments.list`
  * `apihub.deployments.listEffectiveTags`
  * `apihub.deployments.listTagBindings`
  * `apihub.deployments.update`

`apihub.discoveredApiObservations.*`

  * `apihub.discoveredApiObservations.get`
  * `apihub.discoveredApiObservations.list`

`apihub.discoveredApiOperations.*`

  * `apihub.discoveredApiOperations.get`
  * `apihub.discoveredApiOperations.list`

`apihub.externalApis.*`

  * `apihub.externalApis.create`
  * `apihub.externalApis.delete`
  * `apihub.externalApis.get`
  * `apihub.externalApis.list`
  * `apihub.externalApis.update`

`apihub.hostProjectRegistrations.get` `apihub.hostProjectRegistrations.list` `apihub.llmEnablements.*`

  * `apihub.llmEnablements.deregister`
  * `apihub.llmEnablements.get`
  * `apihub.llmEnablements.list`
  * `apihub.llmEnablements.register`

`apihub.locations.collectApiData` `apihub.locations.searchResources` `apihub.operations.get` `apihub.operations.list` `apihub.plugininstances.get` `apihub.plugininstances.list` `apihub.plugins.get` `apihub.plugins.list` `apihub.runTimeProjectAttachments.get` `apihub.runTimeProjectAttachments.list` `apihub.specs.*`

  * `apihub.specs.create`
  * `apihub.specs.delete`
  * `apihub.specs.get`
  * `apihub.specs.lint`
  * `apihub.specs.list`
  * `apihub.specs.listAll`
  * `apihub.specs.update`

`apihub.styleGuides.get` `apihub.versions.*`

  * `apihub.versions.create`
  * `apihub.versions.delete`
  * `apihub.versions.get`
  * `apihub.versions.list`
  * `apihub.versions.listAll`
  * `apihub.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API Hub Viewer 

(`roles/apihub.viewer`) View access to all Cloud API hub resources.  |  `apihub.addons.get` `apihub.addons.list` `apihub.apiHubInstances.get` `apihub.apiHubInstances.list` `apihub.apiOperations.get` `apihub.apiOperations.list` `apihub.apiOperations.listAll` `apihub.apis.get` `apihub.apis.list` `apihub.apis.listEffectiveTags` `apihub.apis.listTagBindings` `apihub.attributes.get` `apihub.attributes.list` `apihub.curations.get` `apihub.curations.list` `apihub.definitions.get` `apihub.definitions.list` `apihub.dependencies.get` `apihub.dependencies.list` `apihub.deployments.get` `apihub.deployments.list` `apihub.deployments.listEffectiveTags` `apihub.deployments.listTagBindings` `apihub.discoveredApiObservations.*`

  * `apihub.discoveredApiObservations.get`
  * `apihub.discoveredApiObservations.list`

`apihub.discoveredApiOperations.*`

  * `apihub.discoveredApiOperations.get`
  * `apihub.discoveredApiOperations.list`

`apihub.externalApis.get` `apihub.externalApis.list` `apihub.hostProjectRegistrations.get` `apihub.hostProjectRegistrations.list` `apihub.llmEnablements.get` `apihub.llmEnablements.list` `apihub.locations.searchResources` `apihub.operations.get` `apihub.operations.list` `apihub.plugininstances.get` `apihub.plugininstances.list` `apihub.plugins.get` `apihub.plugins.list` `apihub.runTimeProjectAttachments.get` `apihub.runTimeProjectAttachments.list` `apihub.specs.get` `apihub.specs.list` `apihub.specs.listAll` `apihub.styleGuides.get` `apihub.versions.get` `apihub.versions.list` `apihub.versions.listAll` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API hub Addons Admin 

(`roles/apihub.addonsAdmin`) Full access to all Cloud API hub addon resources.  |  `apihub.addons.*`

  * `apihub.addons.get`
  * `apihub.addons.list`
  * `apihub.addons.manage`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API hub Insights Viewer 

(`roles/apihub.apiInsightsViewer`) View API hub insights dashboards.  |  `apigee.projectorganizations.get` `apihub.apiHubInstances.get` `apihub.apiHubInstances.list` `apihub.apis.get` `apihub.apis.list` `apihub.deployments.get` `apihub.deployments.list` `apihub.locations.getApiInsights` `apihub.plugininstances.get` `apihub.plugininstances.list` `monitoring.dashboards.get` `monitoring.dashboards.list` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

  
  
#### Cloud API hub Attributes Admin 

(`roles/apihub.attributeAdmin`) Full access to all Cloud API hub attribute's resources.  |  `apihub.attributes.*`

  * `apihub.attributes.create`
  * `apihub.attributes.delete`
  * `apihub.attributes.get`
  * `apihub.attributes.list`
  * `apihub.attributes.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API hub Plugins Admin 

(`roles/apihub.pluginAdmin`) Full access to all Cloud API hub plugin's resources.  |  `apihub.curations.*`

  * `apihub.curations.create`
  * `apihub.curations.delete`
  * `apihub.curations.get`
  * `apihub.curations.list`
  * `apihub.curations.update`

`apihub.locations.collectApiData` `apihub.operations.*`

  * `apihub.operations.cancel`
  * `apihub.operations.delete`
  * `apihub.operations.get`
  * `apihub.operations.list`

`apihub.plugininstances.*`

  * `apihub.plugininstances.applyConfig`
  * `apihub.plugininstances.create`
  * `apihub.plugininstances.delete`
  * `apihub.plugininstances.disable`
  * `apihub.plugininstances.enable`
  * `apihub.plugininstances.execute`
  * `apihub.plugininstances.get`
  * `apihub.plugininstances.list`
  * `apihub.plugininstances.managePluginInstanceSourceData`
  * `apihub.plugininstances.update`

`apihub.plugins.*`

  * `apihub.plugins.create`
  * `apihub.plugins.delete`
  * `apihub.plugins.disable`
  * `apihub.plugins.enable`
  * `apihub.plugins.get`
  * `apihub.plugins.list`

`apihub.specs.lint` `apihub.styleGuides.*`

  * `apihub.styleGuides.get`
  * `apihub.styleGuides.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API hub Provisioning Admin 

(`roles/apihub.provisioningAdmin`) Full access to Cloud API hub provisioning related resources.  |  `apihub.apiHubInstances.*`

  * `apihub.apiHubInstances.create`
  * `apihub.apiHubInstances.delete`
  * `apihub.apiHubInstances.get`
  * `apihub.apiHubInstances.list`
  * `apihub.apiHubInstances.update`

`apihub.hostProjectRegistrations.*`

  * `apihub.hostProjectRegistrations.create`
  * `apihub.hostProjectRegistrations.delete`
  * `apihub.hostProjectRegistrations.get`
  * `apihub.hostProjectRegistrations.list`
  * `apihub.hostProjectRegistrations.register`

`apihub.operations.*`

  * `apihub.operations.cancel`
  * `apihub.operations.delete`
  * `apihub.operations.get`
  * `apihub.operations.list`

`apihub.runTimeProjectAttachments.*`

  * `apihub.runTimeProjectAttachments.attach`
  * `apihub.runTimeProjectAttachments.create`
  * `apihub.runTimeProjectAttachments.delete`
  * `apihub.runTimeProjectAttachments.get`
  * `apihub.runTimeProjectAttachments.list`
  * `apihub.runTimeProjectAttachments.lookup`

`cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud API hub Runtime Project Attachment Editor 

(`roles/apihub.runTimeProjectAttachmentsEditor`) Access to add/delete project as a runtime project attachment to API hub host project.  |  `apihub.runTimeProjectAttachments.attach`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### API-Hub Runtime Project Service Agent 

(`roles/apihub.runtimeProjectServiceAgent`) Gives API-Hub Service Account access to runtime project resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `apigee.deployments.list` `apigee.envgroupattachments.list` `apigee.envgroups.list` `apigee.environments.get` `apigee.organizations.create` `apigee.organizations.delete` `apigee.organizations.get` `apigee.organizations.update` `apigee.proxies.get` `apigee.proxyrevisions.get` `apihub.addons.get` `apihub.addons.list` `apihub.apiOperations.delete` `apihub.apiOperations.list` `apihub.apis.create` `apihub.apis.delete` `apihub.apis.list` `apihub.apis.update` `apihub.attributes.create` `apihub.attributes.list` `apihub.attributes.update` `apihub.curations.list` `apihub.definitions.list` `apihub.dependencies.delete` `apihub.dependencies.list` `apihub.deployments.create` `apihub.deployments.delete` `apihub.deployments.list` `apihub.deployments.update` `apihub.externalApis.list` `apihub.hostProjectRegistrations.list` `apihub.operations.get` `apihub.operations.list` `apihub.plugininstances.create` `apihub.plugininstances.delete` `apihub.plugininstances.list` `apihub.plugininstances.update` `apihub.plugins.create` `apihub.plugins.delete` `apihub.plugins.list` `apihub.runTimeProjectAttachments.list` `apihub.specs.create` `apihub.specs.delete` `apihub.specs.list` `apihub.specs.update` `apihub.versions.create` `apihub.versions.delete` `apihub.versions.list` `apihub.versions.update`  
  
## API Hub permissions

Permission | Included in roles  
---|---  
  
#### `apihub.addons.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Addons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.addonsAdmin) (`roles/apihub.addonsAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.addons.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Addons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.addonsAdmin) (`roles/apihub.addonsAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.addons.manage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Addons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.addonsAdmin) (`roles/apihub.addonsAdmin`)   
  
#### `apihub.apiHubInstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.apiHubInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.apiHubInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.apiHubInstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.apiHubInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)   
  
#### `apihub.apiOperations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.apiOperations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.apiOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.apiOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.apiOperations.listAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.apiOperations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.apis.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.apis.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apihub.apis.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.apis.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apihub.apis.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Apigee Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  [Apigee Security Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.apis.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.apis.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.apis.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.apis.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.attributes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Attributes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.attributeAdmin) (`roles/apihub.attributeAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.attributes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Attributes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.attributeAdmin) (`roles/apihub.attributeAdmin`)   
  
#### `apihub.attributes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Attributes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.attributeAdmin) (`roles/apihub.attributeAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.attributes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Attributes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.attributeAdmin) (`roles/apihub.attributeAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.attributes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Attributes Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.attributeAdmin) (`roles/apihub.attributeAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.curations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.curations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.curations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.curations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.curations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.definitions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.definitions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.definitions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.dependencies.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.dependencies.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.dependencies.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.dependencies.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.dependencies.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.deployments.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apihub.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.deployments.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `apihub.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Apigee Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityAdmin) (`roles/apigee.securityAdmin`)  [Apigee Security Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.securityViewer) (`roles/apigee.securityViewer`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.deployments.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.deployments.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.deployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.discoveredApiObservations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.discoveredApiObservations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.discoveredApiOperations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.discoveredApiOperations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.externalApis.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.externalApis.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.externalApis.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.externalApis.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.externalApis.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.hostProjectRegistrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.hostProjectRegistrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.hostProjectRegistrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.hostProjectRegistrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.hostProjectRegistrations.register`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.llmEnablements.deregister`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.llmEnablements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.llmEnablements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.llmEnablements.register`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)   
  
#### `apihub.locations.collectApiData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.locations.getApiInsights`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.locations.searchResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.locations2.searchResources`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugininstances.applyConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugininstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugininstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugininstances.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugininstances.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugininstances.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugininstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugininstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Insights Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.apiInsightsViewer) (`roles/apihub.apiInsightsViewer`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugininstances.managePluginInstanceSourceData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.plugininstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugins.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugins.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.plugins.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugins.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugins.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.plugins.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.attach`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Cloud API hub Runtime Project Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runTimeProjectAttachmentsEditor) (`roles/apihub.runTimeProjectAttachmentsEditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [ApiGateway Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.admin) (`roles/apigateway.admin`)  [ApiGateway Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.editor) (`roles/apigateway.editor`)  [ApiGateway Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigateway#apigateway.viewer) (`roles/apigateway.viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.runTimeProjectAttachments.lookup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Provisioning Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.provisioningAdmin) (`roles/apihub.provisioningAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.specs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.specs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.specs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.specs.lint`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.specs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 
  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.specs.listAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.specs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.styleGuides.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.styleGuides.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API hub Plugins Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.pluginAdmin) (`roles/apihub.pluginAdmin`)   
  
#### `apihub.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Apigee Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.coreServiceAgent) (`roles/apigee.coreServiceAgent`) 
  * [Apigee Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.serviceAgent) (`roles/apigee.serviceAgent`) 

  
  
#### `apihub.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
#### `apihub.versions.listAll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Apigee API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiAdminV2) (`roles/apigee.apiAdminV2`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  [Cloud API Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.viewer) (`roles/apihub.viewer`)  [Apigee API Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.apiReaderV2) (`roles/apigee.apiReaderV2`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apihub.versions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Organization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigee#apigee.admin) (`roles/apigee.admin`)  [Cloud API Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.admin) (`roles/apihub.admin`)  [Cloud API Hub Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.editor) (`roles/apihub.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [API-Hub Runtime Project Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apihub#apihub.runtimeProjectServiceAgent) (`roles/apihub.runtimeProjectServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
