---
url: https://docs.cloud.google.com/apigee/docs/apihub/iam-roles/
title: Predefined IAM roles \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:21:37.042461+00:00
---

# Predefined IAM roles  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/iam-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Predefined IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

Predefined roles give granular access to specific Google Cloud resources. These roles are created and maintained by Google. Google automatically updates their permissions as necessary, such as when Google Cloud adds new features or services. 

The following table lists all the predefined IAM roles for API hub: 

API hubIAM role | Granted permissions  
---|---  
  
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
  
For more information about predefined roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview). For help choosing the most appropriate predefined roles, see [Choose predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
