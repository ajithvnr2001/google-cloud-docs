---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth/
title: Firebase Authentication roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:15.703138+00:00
---

# Firebase Authentication roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Authentication roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Authentication. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Authentication roles

Role | Permissions  
---|---  
  
#### Firebase Authentication Admin 

(`roles/firebaseauth.admin`) Full read/write access to Firebase Authentication resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Authentication editor 

(`roles/firebaseauth.editor`) Write access to Firebase Authentication resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseauth.*`

  * `firebaseauth.configs.create`
  * `firebaseauth.configs.get`
  * `firebaseauth.configs.getHashConfig`
  * `firebaseauth.configs.getSecret`
  * `firebaseauth.configs.update`
  * `firebaseauth.users.create`
  * `firebaseauth.users.createSession`
  * `firebaseauth.users.delete`
  * `firebaseauth.users.get`
  * `firebaseauth.users.sendEmail`
  * `firebaseauth.users.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Authentication Viewer 

(`roles/firebaseauth.viewer`) Read-only access to Firebase Authentication resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseauth.configs.get` `firebaseauth.users.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Firebase Authentication permissions

Permission | Included in roles  
---|---  
  
#### `firebaseauth.configs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.configs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Firebase Authentication Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.viewer) (`roles/identityplatform.viewer`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Identity Toolkit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.viewer) (`roles/identitytoolkit.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.configs.getHashConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)   
  
#### `firebaseauth.configs.getSecret`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.configs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 
  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.createSession`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Firebase Authentication Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.viewer) (`roles/firebaseauth.viewer`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.viewer) (`roles/identityplatform.viewer`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Identity Toolkit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.viewer) (`roles/identitytoolkit.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.sendEmail`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `firebaseauth.users.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Authentication Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.admin) (`roles/firebaseauth.admin`)  [Firebase Authentication editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseauth#firebaseauth.editor) (`roles/firebaseauth.editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
