---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods/
title: Firebase Mods roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:19.198303+00:00
---

# Firebase Mods roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Mods roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Mods. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Mods roles

Firebase Mods offers the following service agent roles. Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Firebase Extensions API Service Agent 

(`roles/firebasemods.serviceAgent`) Grants Firebase Extensions API Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `appengine.applications.get` `artifactregistry.packages.delete` `cloudfunctions.functions.getIamPolicy` `cloudfunctions.functions.setIamPolicy` `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.queues.*`

  * `cloudtasks.queues.create`
  * `cloudtasks.queues.delete`
  * `cloudtasks.queues.get`
  * `cloudtasks.queues.getIamPolicy`
  * `cloudtasks.queues.list`
  * `cloudtasks.queues.pause`
  * `cloudtasks.queues.purge`
  * `cloudtasks.queues.resume`
  * `cloudtasks.queues.setIamPolicy`
  * `cloudtasks.queues.update`

`cloudtasks.tasks.create` `cloudtasks.tasks.fullView` `deploymentmanager.compositeTypes.*`

  * `deploymentmanager.compositeTypes.create`
  * `deploymentmanager.compositeTypes.delete`
  * `deploymentmanager.compositeTypes.get`
  * `deploymentmanager.compositeTypes.list`
  * `deploymentmanager.compositeTypes.update`

`deploymentmanager.deployments.cancelPreview` `deploymentmanager.deployments.create` `deploymentmanager.deployments.delete` `deploymentmanager.deployments.get` `deploymentmanager.deployments.list` `deploymentmanager.deployments.stop` `deploymentmanager.deployments.update` `deploymentmanager.manifests.*`

  * `deploymentmanager.manifests.get`
  * `deploymentmanager.manifests.list`

`deploymentmanager.operations.*`

  * `deploymentmanager.operations.get`
  * `deploymentmanager.operations.list`

`deploymentmanager.resources.*`

  * `deploymentmanager.resources.get`
  * `deploymentmanager.resources.list`

`deploymentmanager.typeProviders.*`

  * `deploymentmanager.typeProviders.create`
  * `deploymentmanager.typeProviders.delete`
  * `deploymentmanager.typeProviders.get`
  * `deploymentmanager.typeProviders.getType`
  * `deploymentmanager.typeProviders.list`
  * `deploymentmanager.typeProviders.listTypes`
  * `deploymentmanager.typeProviders.update`

`deploymentmanager.types.*`

  * `deploymentmanager.types.create`
  * `deploymentmanager.types.delete`
  * `deploymentmanager.types.get`
  * `deploymentmanager.types.list`
  * `deploymentmanager.types.update`

`eventarc.channels.create` `eventarc.channels.delete` `eventarc.channels.get` `eventarc.channels.setIamPolicy` `iam.serviceAccounts.actAs` `iam.serviceAccounts.create` `iam.serviceAccounts.get` `iam.serviceAccounts.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.projects.updateLiens` `run.services.getIamPolicy` `run.services.setIamPolicy` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.*`

  * `serviceusage.consumerpolicy.analyze`
  * `serviceusage.consumerpolicy.get`
  * `serviceusage.consumerpolicy.update`

`serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.enable` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Firebase Mods permissions

There are no IAM permissions for this service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
