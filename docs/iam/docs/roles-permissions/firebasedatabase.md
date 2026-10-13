---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase/
title: Firebase Realtime Database roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:24.895920+00:00
---

# Firebase Realtime Database roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Realtime Database roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Realtime Database. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Realtime Database roles

Role | Permissions  
---|---  
  
#### Firebase Realtime Database Admin 

(`roles/firebasedatabase.admin`) Full read/write access to Firebase Realtime Database resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasedatabase.*`

  * `firebasedatabase.instances.create`
  * `firebasedatabase.instances.delete`
  * `firebasedatabase.instances.disable`
  * `firebasedatabase.instances.get`
  * `firebasedatabase.instances.list`
  * `firebasedatabase.instances.reenable`
  * `firebasedatabase.instances.undelete`
  * `firebasedatabase.instances.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Realtime Database Viewer 

(`roles/firebasedatabase.viewer`) Read-only access to Firebase Realtime Database resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasedatabase.instances.get` `firebasedatabase.instances.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Firebase Realtime Database Service Agent 

(`roles/firebasedatabase.serviceAgent`) Access to publish triggers  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `pubsub.topics.publish` `serviceusage.services.use`  
  
## Firebase Realtime Database permissions

Permission | Included in roles  
---|---  
  
#### `firebasedatabase.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Realtime Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.viewer) (`roles/firebasedatabase.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Realtime Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.viewer) (`roles/firebasedatabase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.reenable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.undelete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasedatabase.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Realtime Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasedatabase#firebasedatabase.admin) (`roles/firebasedatabase.admin`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
