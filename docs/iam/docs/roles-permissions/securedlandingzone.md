---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone/
title: Secured Landing Zone roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:58.952452+00:00
---

# Secured Landing Zone roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Secured Landing Zone roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Secured Landing Zone. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Secured Landing Zone roles

Role | Permissions  
---|---  
  
#### Secured Landing Zone Admin Beta

(`roles/securedlandingzone.admin`) Admin role for Secured Landing Zone  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securedlandingzone.*`

  * `securedlandingzone.operations.get`
  * `securedlandingzone.overwatches.activate`
  * `securedlandingzone.overwatches.create`
  * `securedlandingzone.overwatches.delete`
  * `securedlandingzone.overwatches.get`
  * `securedlandingzone.overwatches.list`
  * `securedlandingzone.overwatches.suspend`
  * `securedlandingzone.overwatches.update`

  
  
#### Secured Landing Zone Viewer Beta

(`roles/securedlandingzone.viewer`) Viewer role for Secured Landing Zone  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securedlandingzone.operations.get` `securedlandingzone.overwatches.get` `securedlandingzone.overwatches.list`  
  
#### SLZ BQDW Blueprint Organization Level Remediator Beta

(`roles/securedlandingzone.bqdwOrgRemediator`) Access to modify (remediate) resources in SLZ BQDW Blueprint at Organization.  |  `accesscontextmanager.servicePerimeters.get` `accesscontextmanager.servicePerimeters.list` `accesscontextmanager.servicePerimeters.update`  
  
#### SLZ BQDW Blueprint Project Level Remediator Beta

(`roles/securedlandingzone.bqdwProjectRemediator`) Access to modify (remediate) resources in SLZ BQDW Blueprint at Project.  |  `bigquery.datasets.get` `bigquery.datasets.getIamPolicy` `bigquery.datasets.setIamPolicy` `bigquery.datasets.update` `cloudkms.cryptoKeys.get` `cloudkms.cryptoKeys.getIamPolicy` `cloudkms.cryptoKeys.list` `cloudkms.cryptoKeys.setIamPolicy` `cloudkms.cryptoKeys.update` `cloudkms.keyRings.getIamPolicy` `cloudkms.keyRings.setIamPolicy` `pubsub.topics.get` `pubsub.topics.getIamPolicy` `pubsub.topics.list` `pubsub.topics.setIamPolicy` `pubsub.topics.update` `resourcemanager.projects.update` `serviceusage.services.use` `storage.buckets.get` `storage.buckets.getIamPolicy` `storage.buckets.list` `storage.buckets.setIamPolicy` `storage.buckets.update`  
  
#### Overwatch Activator Beta

(`roles/securedlandingzone.overwatchActivator`) This role can activate or suspend Overwatches  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securedlandingzone.overwatches.activate` `securedlandingzone.overwatches.suspend`  
  
#### Overwatch Admin Beta

(`roles/securedlandingzone.overwatchAdmin`) Full access to Overwatches  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securedlandingzone.*`

  * `securedlandingzone.operations.get`
  * `securedlandingzone.overwatches.activate`
  * `securedlandingzone.overwatches.create`
  * `securedlandingzone.overwatches.delete`
  * `securedlandingzone.overwatches.get`
  * `securedlandingzone.overwatches.list`
  * `securedlandingzone.overwatches.suspend`
  * `securedlandingzone.overwatches.update`

  
  
#### Overwatch Viewer Beta

(`roles/securedlandingzone.overwatchViewer`) This role can view all properties of Overwatches  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `securedlandingzone.operations.get` `securedlandingzone.overwatches.get` `securedlandingzone.overwatches.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Secured Landing Zone Service Agent 

(`roles/securedlandingzone.serviceAgent`) Grants Secured Landing Zone service account permissions to manage resources in the customer project  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudasset.assets.exportOrgPolicy` `cloudasset.assets.exportResource` `cloudasset.feeds.create` `cloudasset.feeds.delete` `cloudasset.feeds.update` `logging.logEntries.list` `pubsub.subscriptions.consume` `pubsub.subscriptions.create` `pubsub.subscriptions.delete` `pubsub.topics.attachSubscription` `pubsub.topics.create` `pubsub.topics.delete` `pubsub.topics.detachSubscription` `pubsub.topics.getIamPolicy` `pubsub.topics.setIamPolicy` `resourcemanager.projects.get` `securitycenter.assetsecuritymarks.update` `securitycenter.findings.list` `securitycenter.findings.update` `securitycenter.sources.list` `securitycenter.sources.update` `serviceusage.services.use`  
  
## Secured Landing Zone permissions

Permission | Included in roles  
---|---  
  
#### `securedlandingzone.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Secured Landing Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.viewer) (`roles/securedlandingzone.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)  [Overwatch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchViewer) (`roles/securedlandingzone.overwatchViewer`)   
  
#### `securedlandingzone.overwatches.activate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Overwatch Activator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchActivator) (`roles/securedlandingzone.overwatchActivator`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)   
  
#### `securedlandingzone.overwatches.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)   
  
#### `securedlandingzone.overwatches.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)   
  
#### `securedlandingzone.overwatches.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Secured Landing Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.viewer) (`roles/securedlandingzone.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)  [Overwatch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchViewer) (`roles/securedlandingzone.overwatchViewer`)   
  
#### `securedlandingzone.overwatches.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Secured Landing Zone Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.viewer) (`roles/securedlandingzone.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)  [Overwatch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchViewer) (`roles/securedlandingzone.overwatchViewer`)   
  
#### `securedlandingzone.overwatches.suspend`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Overwatch Activator](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchActivator) (`roles/securedlandingzone.overwatchActivator`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)   
  
#### `securedlandingzone.overwatches.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secured Landing Zone Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.admin) (`roles/securedlandingzone.admin`)  [Overwatch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/securedlandingzone#securedlandingzone.overwatchAdmin) (`roles/securedlandingzone.overwatchAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
