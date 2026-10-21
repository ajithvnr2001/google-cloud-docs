---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer/
title: Storage Transfer Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:58:45.265180+00:00
---

# Storage Transfer Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Storage Transfer Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Storage Transfer Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Storage Transfer Service roles

Role | Permissions  
---|---  
  
#### Storage Transfer Admin 

(`roles/storagetransfer.admin`) Create, update and manage transfer jobs and operations.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storagetransfer.*`

  * `storagetransfer.agentpools.create`
  * `storagetransfer.agentpools.delete`
  * `storagetransfer.agentpools.get`
  * `storagetransfer.agentpools.list`
  * `storagetransfer.agentpools.report`
  * `storagetransfer.agentpools.update`
  * `storagetransfer.jobs.create`
  * `storagetransfer.jobs.delete`
  * `storagetransfer.jobs.get`
  * `storagetransfer.jobs.list`
  * `storagetransfer.jobs.run`
  * `storagetransfer.jobs.update`
  * `storagetransfer.operations.assign`
  * `storagetransfer.operations.cancel`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.list`
  * `storagetransfer.operations.pause`
  * `storagetransfer.operations.report`
  * `storagetransfer.operations.resume`
  * `storagetransfer.projects.getServiceAccount`

  
  
#### Storage Transfer Viewer 

(`roles/storagetransfer.viewer`) Read access to storage transfer jobs and operations.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storagetransfer.agentpools.get` `storagetransfer.agentpools.list` `storagetransfer.jobs.get` `storagetransfer.jobs.list` `storagetransfer.operations.get` `storagetransfer.operations.list` `storagetransfer.projects.getServiceAccount`  
  
#### Storage Transfer Agent 

(`roles/storagetransfer.transferAgent`) Perform transfers from an agent.  |  `logging.logEntries.create` `monitoring.timeSeries.create` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.get` `pubsub.topics.list` `pubsub.topics.publish` `storagetransfer.agentpools.report` `storagetransfer.operations.assign` `storagetransfer.operations.get` `storagetransfer.operations.report`  
  
#### Storage Transfer User 

(`roles/storagetransfer.user`) Create and update storage transfer jobs and operations.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storagetransfer.agentpools.create` `storagetransfer.agentpools.get` `storagetransfer.agentpools.list` `storagetransfer.agentpools.report` `storagetransfer.agentpools.update` `storagetransfer.jobs.create` `storagetransfer.jobs.get` `storagetransfer.jobs.list` `storagetransfer.jobs.run` `storagetransfer.jobs.update` `storagetransfer.operations.*`

  * `storagetransfer.operations.assign`
  * `storagetransfer.operations.cancel`
  * `storagetransfer.operations.get`
  * `storagetransfer.operations.list`
  * `storagetransfer.operations.pause`
  * `storagetransfer.operations.report`
  * `storagetransfer.operations.resume`

`storagetransfer.projects.getServiceAccount`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Storage Transfer Service Agent 

(`roles/storagetransfer.serviceAgent`) Grants Storage Transfer Service Agent permissions required to run transfers  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.subscriptions.get` `pubsub.subscriptions.update` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.get` `pubsub.topics.publish` `pubsub.topics.update`  
  
## Storage Transfer Service permissions

Permission | Included in roles  
---|---  
  
#### `storagetransfer.agentpools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.agentpools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)   
  
#### `storagetransfer.agentpools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.agentpools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `storagetransfer.agentpools.report`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.agentpools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)   
  
#### `storagetransfer.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `storagetransfer.jobs.run`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.jobs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.assign`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.pause`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.report`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.transferAgent) (`roles/storagetransfer.transferAgent`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.operations.resume`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
#### `storagetransfer.projects.getServiceAccount`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Storage Transfer Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.admin) (`roles/storagetransfer.admin`)  [Storage Transfer Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.viewer) (`roles/storagetransfer.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Storage Transfer User](https://docs.cloud.google.com/iam/docs/roles-permissions/storagetransfer#storagetransfer.user) (`roles/storagetransfer.user`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
