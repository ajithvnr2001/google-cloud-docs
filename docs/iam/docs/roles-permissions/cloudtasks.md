---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks/
title: Cloud Tasks roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:39:49.996490+00:00
---

# Cloud Tasks roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Tasks roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Tasks. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Tasks roles

Role | Permissions  
---|---  
  
#### Cloud Tasks Admin 

(`roles/cloudtasks.admin`) Full access to queues and tasks.  |  `cloudtasks.*`

  * `cloudtasks.cmekConfig.get`
  * `cloudtasks.cmekConfig.update`
  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`
  * `cloudtasks.operations.get`
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
  * `cloudtasks.tasks.create`
  * `cloudtasks.tasks.delete`
  * `cloudtasks.tasks.fullView`
  * `cloudtasks.tasks.get`
  * `cloudtasks.tasks.list`
  * `cloudtasks.tasks.run`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Editor 

(`roles/cloudtasks.editor`) Editor role for cloudtasks  |  `cloudtasks.cmekConfig.get` `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.operations.get` `cloudtasks.queues.create` `cloudtasks.queues.delete` `cloudtasks.queues.get` `cloudtasks.queues.list` `cloudtasks.queues.pause` `cloudtasks.queues.purge` `cloudtasks.queues.resume` `cloudtasks.queues.update` `cloudtasks.tasks.*`

  * `cloudtasks.tasks.create`
  * `cloudtasks.tasks.delete`
  * `cloudtasks.tasks.fullView`
  * `cloudtasks.tasks.get`
  * `cloudtasks.tasks.list`
  * `cloudtasks.tasks.run`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Viewer 

(`roles/cloudtasks.viewer`) Get and list access to tasks, queues, and locations.  |  `cloudtasks.cmekConfig.get` `cloudtasks.locations.*`

  * `cloudtasks.locations.get`
  * `cloudtasks.locations.list`

`cloudtasks.operations.get` `cloudtasks.queues.get` `cloudtasks.queues.list` `cloudtasks.tasks.fullView` `cloudtasks.tasks.get` `cloudtasks.tasks.list` `monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Enqueuer Beta

(`roles/cloudtasks.enqueuer`) Access to create tasks.  |  `cloudtasks.operations.get` `cloudtasks.tasks.create` `cloudtasks.tasks.fullView` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Queue Admin 

(`roles/cloudtasks.queueAdmin`) Admin access to queues.  |  `cloudtasks.locations.*`

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

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Task Deleter 

(`roles/cloudtasks.taskDeleter`) Access to delete tasks.  |  `cloudtasks.tasks.delete` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Tasks Task Runner Beta

(`roles/cloudtasks.taskRunner`) Access to run tasks.  |  `cloudtasks.tasks.fullView` `cloudtasks.tasks.run` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Tasks Service Agent 

(`roles/cloudtasks.serviceAgent`) Grants Cloud Tasks Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.getAccessToken` `iam.serviceAccounts.getOpenIdToken` `logging.logEntries.create`  
  
## Cloud Tasks permissions

Permission | Included in roles  
---|---  
  
#### `cloudtasks.cmekConfig.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtasks.cmekConfig.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)   
  
#### `cloudtasks.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Cloud Tasks Enqueuer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.enqueuer) (`roles/cloudtasks.enqueuer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtasks.queues.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 
  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.purge`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.queues.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Queue Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.queueAdmin) (`roles/cloudtasks.queueAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.tasks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Enqueuer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.enqueuer) (`roles/cloudtasks.enqueuer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.tasks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Task Deleter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.taskDeleter) (`roles/cloudtasks.taskDeleter`)   
  
#### `cloudtasks.tasks.fullView`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Cloud Tasks Enqueuer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.enqueuer) (`roles/cloudtasks.enqueuer`)  [Cloud Tasks Task Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.taskRunner) (`roles/cloudtasks.taskRunner`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Extensions API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasemods#firebasemods.serviceAgent) (`roles/firebasemods.serviceAgent`) 

  
  
#### `cloudtasks.tasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtasks.tasks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.viewer) (`roles/cloudtasks.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtasks.tasks.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Tasks Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.admin) (`roles/cloudtasks.admin`)  [Cloud Tasks Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.editor) (`roles/cloudtasks.editor`)  [Cloud Tasks Task Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtasks#cloudtasks.taskRunner) (`roles/cloudtasks.taskRunner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
