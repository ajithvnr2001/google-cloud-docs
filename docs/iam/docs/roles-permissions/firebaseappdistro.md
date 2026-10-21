---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro/
title: Firebase App Distribution roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:59:37.923220+00:00
---

# Firebase App Distribution roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase App Distribution roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase App Distribution. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase App Distribution roles

Role | Permissions  
---|---  
  
#### Firebase App Distribution Admin 

(`roles/firebaseappdistro.admin`) Full read/write access to Firebase App Distribution resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseappdistro.*`

  * `firebaseappdistro.groups.list`
  * `firebaseappdistro.groups.update`
  * `firebaseappdistro.releases.list`
  * `firebaseappdistro.releases.update`
  * `firebaseappdistro.testers.list`
  * `firebaseappdistro.testers.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase App Distribution Viewer 

(`roles/firebaseappdistro.viewer`) Read-only access to Firebase App Distribution resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseappdistro.groups.list` `firebaseappdistro.releases.list` `firebaseappdistro.testers.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Firebase App Distribution permissions

Permission | Included in roles  
---|---  
  
#### `firebaseappdistro.groups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
#### `firebaseappdistro.groups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
#### `firebaseappdistro.releases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
#### `firebaseappdistro.releases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
#### `firebaseappdistro.testers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase App Distribution Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.viewer) (`roles/firebaseappdistro.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
#### `firebaseappdistro.testers.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase App Distribution Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseappdistro#firebaseappdistro.admin) (`roles/firebaseappdistro.admin`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase App Distribution Admin SDK Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.appDistributionSdkServiceAgent) (`roles/firebase.appDistributionSdkServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
