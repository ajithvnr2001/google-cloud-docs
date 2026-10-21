---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging/
title: Firebase Cloud Messaging roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:26:05.464444+00:00
---

# Firebase Cloud Messaging roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Cloud Messaging roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Cloud Messaging. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Cloud Messaging roles

Role | Permissions  
---|---  
  
#### Firebase Cloud Messaging Service Editor 

(`roles/cloudmessaging.editor`) Editor of Firebase Cloud Messaging resources  |  `cloudmessaging.*`

  * `cloudmessaging.messages.create`
  * `cloudmessaging.topicSubscriptions.create`
  * `cloudmessaging.topicSubscriptions.delete`
  * `cloudmessaging.topicSubscriptions.get`
  * `cloudmessaging.topicSubscriptions.list`
  * `cloudmessaging.topicSubscriptions.update`

`fcmdata.deliverydata.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Cloud Messaging API Admin 

(`roles/firebasecloudmessaging.admin`) Full read/write access to Firebase Cloud Messaging API resources.  |  `cloudmessaging.*`

  * `cloudmessaging.messages.create`
  * `cloudmessaging.topicSubscriptions.create`
  * `cloudmessaging.topicSubscriptions.delete`
  * `cloudmessaging.topicSubscriptions.get`
  * `cloudmessaging.topicSubscriptions.list`
  * `cloudmessaging.topicSubscriptions.update`

`fcmdata.deliverydata.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Cloud Messaging API Viewer 

(`roles/firebasecloudmessaging.viewer`) Read-only access to Firebase Cloud Messaging API resources.  |  `cloudmessaging.topicSubscriptions.get` `cloudmessaging.topicSubscriptions.list` `fcmdata.deliverydata.list` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasenotifications.messages.get` `firebasenotifications.messages.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Cloud Messaging Admin 

(`roles/firebasenotifications.admin`) Full read/write access to Firebase Cloud Messaging resources.  |  `fcmdata.deliverydata.list` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasenotifications.*`

  * `firebasenotifications.messages.create`
  * `firebasenotifications.messages.delete`
  * `firebasenotifications.messages.get`
  * `firebasenotifications.messages.list`
  * `firebasenotifications.messages.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Cloud Messaging Viewer 

(`roles/firebasenotifications.viewer`) Read-only access to Firebase Cloud Messaging resources.  |  `fcmdata.deliverydata.list` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasenotifications.messages.get` `firebasenotifications.messages.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Firebase Cloud Messaging permissions

Permission | Included in roles  
---|---  
  
#### `cloudmessaging.messages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 
  * [Firebase SDK Provisioning Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkProvisioningServiceAgent) (`roles/firebase.sdkProvisioningServiceAgent`) 

  
  
#### `cloudmessaging.topicSubscriptions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)   
  
#### `cloudmessaging.topicSubscriptions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)   
  
#### `cloudmessaging.topicSubscriptions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudmessaging.topicSubscriptions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudmessaging.topicSubscriptions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Cloud Messaging Service Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#cloudmessaging.editor) (`roles/cloudmessaging.editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Cloud Messaging API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.admin) (`roles/firebasecloudmessaging.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)   
  
#### `firebasenotifications.messages.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasenotifications.messages.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasenotifications.messages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Cloud Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.viewer) (`roles/firebasenotifications.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasenotifications.messages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Cloud Messaging API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasecloudmessaging.viewer) (`roles/firebasecloudmessaging.viewer`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Cloud Messaging Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.viewer) (`roles/firebasenotifications.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebasenotifications.messages.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Cloud Messaging Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin) (`roles/firebasenotifications.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
