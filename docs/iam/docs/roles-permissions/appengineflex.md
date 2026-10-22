---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex/
title: App Engine flexible environment roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:57.963003+00:00
---

# App Engine flexible environment roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/appengineflex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  App Engine flexible environment roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for App Engine flexible environment. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## App Engine flexible environment roles

App Engine flexible environment offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### App Engine flexible environment Service Agent 

(`roles/appengineflex.serviceAgent`) Can edit and manage App Engine Flexible Environment apps. Includes access to service accounts.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.projectsettings.get` `artifactregistry.repositories.create` `artifactregistry.repositories.downloadArtifacts` `artifactregistry.repositories.get` `artifactregistry.repositories.uploadArtifacts` `billing.accounts.get` `cloudbuild.builds.create` `cloudbuild.builds.get` `compute.addresses.create` `compute.addresses.delete` `compute.addresses.get` `compute.addresses.list` `compute.addresses.use` `compute.autoscalers.create` `compute.autoscalers.delete` `compute.autoscalers.get` `compute.autoscalers.update` `compute.backendServices.create` `compute.backendServices.delete` `compute.backendServices.get` `compute.backendServices.list` `compute.backendServices.update` `compute.backendServices.use` `compute.disks.create` `compute.disks.list` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.update` `compute.forwardingRules.create` `compute.forwardingRules.delete` `compute.forwardingRules.get` `compute.globalAddresses.create` `compute.globalAddresses.delete` `compute.globalAddresses.get` `compute.globalAddresses.use` `compute.globalForwardingRules.create` `compute.globalForwardingRules.delete` `compute.globalForwardingRules.get` `compute.globalOperations.get` `compute.healthChecks.create` `compute.healthChecks.delete` `compute.healthChecks.get` `compute.healthChecks.update` `compute.healthChecks.useReadOnly` `compute.httpHealthChecks.create` `compute.httpHealthChecks.delete` `compute.httpHealthChecks.get` `compute.httpHealthChecks.use` `compute.httpHealthChecks.useReadOnly` `compute.httpsHealthChecks.create` `compute.httpsHealthChecks.delete` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.update` `compute.httpsHealthChecks.use` `compute.httpsHealthChecks.useReadOnly` `compute.images.get` `compute.images.useReadOnly` `compute.instanceGroupManagers.create` `compute.instanceGroupManagers.delete` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.update` `compute.instanceGroupManagers.use` `compute.instanceGroups.create` `compute.instanceGroups.delete` `compute.instanceGroups.get` `compute.instanceGroups.update` `compute.instanceGroups.use` `compute.instanceTemplates.create` `compute.instanceTemplates.delete` `compute.instanceTemplates.get` `compute.instanceTemplates.useReadOnly` `compute.instances.attachDisk` `compute.instances.create` `compute.instances.delete` `compute.instances.detachDisk` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.getSerialPortOutput` `compute.instances.list` `compute.instances.reset` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.use` `compute.machineTypes.get` `compute.networks.create` `compute.networks.delete` `compute.networks.get` `compute.networks.updatePolicy` `compute.networks.use` `compute.networks.useExternalIp` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.regionBackendServices.create` `compute.regionBackendServices.delete` `compute.regionBackendServices.get` `compute.regionBackendServices.list` `compute.regionBackendServices.update` `compute.regionBackendServices.use` `compute.regionOperations.get` `compute.regions.get` `compute.routes.create` `compute.routes.delete` `compute.routes.get` `compute.routes.list` `compute.subnetworks.delete` `compute.subnetworks.get` `compute.subnetworks.use` `compute.subnetworks.useExternalIp` `compute.targetHttpProxies.create` `compute.targetHttpProxies.delete` `compute.targetHttpProxies.get` `compute.targetHttpProxies.use` `compute.targetHttpsProxies.create` `compute.targetHttpsProxies.delete` `compute.targetHttpsProxies.get` `compute.targetHttpsProxies.setSslCertificates` `compute.targetHttpsProxies.use` `compute.urlMaps.create` `compute.urlMaps.delete` `compute.urlMaps.get` `compute.urlMaps.update` `compute.urlMaps.use` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`deploymentmanager.compositeTypes.get` `deploymentmanager.deployments.create` `deploymentmanager.deployments.delete` `deploymentmanager.deployments.get` `deploymentmanager.deployments.list` `deploymentmanager.deployments.update` `deploymentmanager.manifests.*`

  * `deploymentmanager.manifests.get`
  * `deploymentmanager.manifests.list`

`deploymentmanager.operations.*`

  * `deploymentmanager.operations.get`
  * `deploymentmanager.operations.list`

`deploymentmanager.typeProviders.create` `deploymentmanager.typeProviders.get` `iam.serviceAccounts.actAs` `iam.serviceAccounts.get` `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.signBlob` `iam.serviceAccounts.signJwt` `logging.logEntries.create` `logging.logMetrics.create` `logging.logMetrics.delete` `logging.logMetrics.get` `logging.logMetrics.update` `resourcemanager.organizations.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.setIamPolicy` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.enable` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.setIamPolicy` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.getIamPolicy` `storage.objects.list`  
  
## App Engine flexible environment permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
