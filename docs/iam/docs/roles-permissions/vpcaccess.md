---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess/
title: Serverless VPC Access roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:13.339031+00:00
---

# Serverless VPC Access roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Serverless VPC Access roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Serverless VPC Access. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Serverless VPC Access roles

Role | Permissions  
---|---  
  
#### Serverless VPC Access Admin 

(`roles/vpcaccess.admin`) Full access to all Serverless VPC Access resources  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vpcaccess.*`

  * `vpcaccess.connectors.create`
  * `vpcaccess.connectors.delete`
  * `vpcaccess.connectors.get`
  * `vpcaccess.connectors.list`
  * `vpcaccess.connectors.update`
  * `vpcaccess.locations.list`
  * `vpcaccess.operations.get`
  * `vpcaccess.operations.list`

  
  
#### Serverless VPC Access User 

(`roles/vpcaccess.user`) User of Serverless VPC Access connectors  |  `compute.networks.access` `resourcemanager.projects.get` `resourcemanager.projects.list` `vpcaccess.connectors.get` `vpcaccess.connectors.list` `vpcaccess.locations.list` `vpcaccess.operations.*`

  * `vpcaccess.operations.get`
  * `vpcaccess.operations.list`

  
  
#### Serverless VPC Access Viewer 

(`roles/vpcaccess.viewer`) Viewer of all Serverless VPC Access resources  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vpcaccess.connectors.get` `vpcaccess.connectors.list` `vpcaccess.locations.list` `vpcaccess.operations.*`

  * `vpcaccess.operations.get`
  * `vpcaccess.operations.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Serverless VPC Access Service Agent 

(`roles/vpcaccess.serviceAgent`) Can create and manage resources to support serverless application to connect to virtual private cloud.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `billing.accounts.get` `compute.addresses.createInternal` `compute.addresses.deleteInternal` `compute.addresses.get` `compute.addresses.list` `compute.autoscalers.*`

  * `compute.autoscalers.create`
  * `compute.autoscalers.delete`
  * `compute.autoscalers.get`
  * `compute.autoscalers.list`
  * `compute.autoscalers.update`

`compute.disks.create` `compute.firewalls.create` `compute.firewalls.delete` `compute.firewalls.get` `compute.firewalls.list` `compute.firewalls.update` `compute.healthChecks.create` `compute.healthChecks.delete` `compute.healthChecks.get` `compute.healthChecks.list` `compute.healthChecks.update` `compute.healthChecks.use` `compute.healthChecks.useReadOnly` `compute.httpHealthChecks.create` `compute.httpHealthChecks.delete` `compute.httpHealthChecks.get` `compute.httpHealthChecks.list` `compute.httpHealthChecks.use` `compute.httpHealthChecks.useReadOnly` `compute.httpsHealthChecks.create` `compute.httpsHealthChecks.delete` `compute.httpsHealthChecks.get` `compute.httpsHealthChecks.update` `compute.httpsHealthChecks.use` `compute.httpsHealthChecks.useReadOnly` `compute.images.get` `compute.images.useReadOnly` `compute.instanceGroupManagers.create` `compute.instanceGroupManagers.delete` `compute.instanceGroupManagers.get` `compute.instanceGroupManagers.update` `compute.instanceGroupManagers.use` `compute.instanceGroups.create` `compute.instanceGroups.delete` `compute.instanceGroups.get` `compute.instanceGroups.update` `compute.instanceTemplates.create` `compute.instanceTemplates.delete` `compute.instanceTemplates.get` `compute.instanceTemplates.useReadOnly` `compute.instances.create` `compute.instances.delete` `compute.instances.get` `compute.instances.getGuestAttributes` `compute.instances.list` `compute.instances.reset` `compute.instances.setLabels` `compute.instances.setMetadata` `compute.instances.setTags` `compute.instances.start` `compute.instances.stop` `compute.instances.use` `compute.machineTypes.get` `compute.networks.get` `compute.networks.updatePolicy` `compute.networks.use` `compute.projects.get` `compute.projects.setCommonInstanceMetadata` `compute.regionOperations.get` `compute.regionOperations.list` `compute.regions.*`

  * `compute.regions.get`
  * `compute.regions.list`

`compute.subnetworks.create` `compute.subnetworks.delete` `compute.subnetworks.get` `compute.subnetworks.list` `compute.subnetworks.use` `compute.zoneOperations.get` `compute.zoneOperations.list` `compute.zones.*`

  * `compute.zones.get`
  * `compute.zones.list`

`deploymentmanager.compositeTypes.get` `deploymentmanager.deployments.create` `deploymentmanager.deployments.delete` `deploymentmanager.deployments.get` `deploymentmanager.deployments.list` `deploymentmanager.deployments.update` `deploymentmanager.manifests.*`

  * `deploymentmanager.manifests.get`
  * `deploymentmanager.manifests.list`

`deploymentmanager.operations.*`

  * `deploymentmanager.operations.get`
  * `deploymentmanager.operations.list`

`deploymentmanager.typeProviders.create` `deploymentmanager.typeProviders.get` `logging.logEntries.create` `logging.logMetrics.create` `logging.logMetrics.delete` `logging.logMetrics.get` `logging.logMetrics.update` `resourcemanager.projects.get`  
  
## Serverless VPC Access permissions

Permission | Included in roles  
---|---  
  
#### `vpcaccess.connectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `vpcaccess.connectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `vpcaccess.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  [Serverless VPC Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.user) (`roles/vpcaccess.user`)  [Serverless VPC Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer) (`roles/vpcaccess.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Data Connectors Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.serviceAgent) (`roles/dataconnectors.serviceAgent`) 
  * [Cloud Run Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) (`roles/run.serviceAgent`) 
  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 

  
  
#### `vpcaccess.connectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  [Serverless VPC Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.user) (`roles/vpcaccess.user`)  [Serverless VPC Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer) (`roles/vpcaccess.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Serverless Integrations Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/runapps#runapps.serviceAgent) (`roles/runapps.serviceAgent`) 

  
  
#### `vpcaccess.connectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)   
  
#### `vpcaccess.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  [Serverless VPC Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.user) (`roles/vpcaccess.user`)  [Serverless VPC Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer) (`roles/vpcaccess.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `vpcaccess.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  [Serverless VPC Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.user) (`roles/vpcaccess.user`)  [Serverless VPC Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer) (`roles/vpcaccess.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `vpcaccess.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Serverless VPC Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.admin) (`roles/vpcaccess.admin`)  [Serverless VPC Access User](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.user) (`roles/vpcaccess.user`)  [Serverless VPC Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vpcaccess#vpcaccess.viewer) (`roles/vpcaccess.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
