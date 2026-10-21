---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit/
title: Identity Toolkit roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:01:47.751941+00:00
---

# Identity Toolkit roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Identity Toolkit roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Identity Toolkit. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Identity Toolkit roles

Role | Permissions  
---|---  
  
#### Identity Toolkit Admin 

(`roles/identitytoolkit.admin`) Full access to Identity Toolkit resources.  |  `firebaseauth.*`

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

`identitytoolkit.*`

  * `identitytoolkit.tenants.create`
  * `identitytoolkit.tenants.delete`
  * `identitytoolkit.tenants.get`
  * `identitytoolkit.tenants.getIamPolicy`
  * `identitytoolkit.tenants.list`
  * `identitytoolkit.tenants.setIamPolicy`
  * `identitytoolkit.tenants.update`

  
  
#### Identity Toolkit editor 

(`roles/identitytoolkit.editor`) Write access to Identity Toolkit resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseauth.*`

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

`identitytoolkit.tenants.create` `identitytoolkit.tenants.delete` `identitytoolkit.tenants.get` `identitytoolkit.tenants.getIamPolicy` `identitytoolkit.tenants.list` `identitytoolkit.tenants.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Identity Toolkit Viewer 

(`roles/identitytoolkit.viewer`) Read access to Identity Toolkit resources.  |  `firebaseauth.configs.get` `firebaseauth.users.get` `identitytoolkit.tenants.get` `identitytoolkit.tenants.getIamPolicy` `identitytoolkit.tenants.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Identity Platform Service Agent 

(`roles/identitytoolkit.serviceAgent`) Gives Identity Platform service account access to customer project resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `cloudfunctions.functions.invoke` `recaptchaenterprise.assessments.create` `recaptchaenterprise.keys.create` `recaptchaenterprise.keys.delete` `recaptchaenterprise.keys.get`  
  
## Identity Toolkit permissions

Permission | Included in roles  
---|---  
  
#### `identitytoolkit.tenants.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.viewer) (`roles/identityplatform.viewer`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Identity Toolkit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.viewer) (`roles/identitytoolkit.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.viewer) (`roles/identityplatform.viewer`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Identity Toolkit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.viewer) (`roles/identitytoolkit.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Platform Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.viewer) (`roles/identityplatform.viewer`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  [Identity Toolkit Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.viewer) (`roles/identitytoolkit.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
#### `identitytoolkit.tenants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Identity Platform Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`)  [Identity Toolkit Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.admin) (`roles/identitytoolkit.admin`)  [Identity Toolkit editor](https://docs.cloud.google.com/iam/docs/roles-permissions/identitytoolkit#identitytoolkit.editor) (`roles/identitytoolkit.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Admin SDK Administrator Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.sdkAdminServiceAgent) (`roles/firebase.sdkAdminServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
