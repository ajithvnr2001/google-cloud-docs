---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig/
title: Firebase Remote Config roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:34.323545+00:00
---

# Firebase Remote Config roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Remote Config roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Remote Config. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Remote Config roles

Role | Permissions  
---|---  
  
#### Firebase Remote Config Admin 

(`roles/cloudconfig.admin`) Full access to Firebase Remote Config resources.  |  `cloudconfig.*`

  * `cloudconfig.configs.get`
  * `cloudconfig.configs.update`

`firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Remote Config Viewer 

(`roles/cloudconfig.viewer`) Read access to Firebase Remote Config resources.  |  `cloudconfig.configs.get` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Infrastructure Manager Service Agent 

(`roles/cloudconfig.serviceAgent`) Gives Infrastructure Manager service agent access to managed resources  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudbuild.builds.create` `cloudbuild.builds.get` `cloudbuild.builds.list` `cloudbuild.builds.update` `cloudbuild.workerpools.use` `iam.serviceAccounts.actAs` `iam.serviceAccounts.getAccessToken` `logging.logEntries.create` `logging.logEntries.route` `serviceusage.services.use` `storage.buckets.create` `storage.buckets.delete` `storage.buckets.get` `storage.buckets.list` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Firebase Remote Config permissions

Permission | Included in roles  
---|---  
  
#### `cloudconfig.configs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Remote Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.admin) (`roles/cloudconfig.admin`)  [Firebase Remote Config Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.viewer) (`roles/cloudconfig.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `cloudconfig.configs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Remote Config Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudconfig#cloudconfig.admin) (`roles/cloudconfig.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
