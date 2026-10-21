---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt/
title: Firebase A/B Testing roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:30:24.908643+00:00
---

# Firebase A/B Testing roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase A/B Testing roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase A/B Testing. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase A/B Testing roles

Role | Permissions  
---|---  
  
#### Firebase A/B Testing Admin Beta

(`roles/firebaseabt.admin`) Full read/write access to Firebase A/B Testing resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseabt.*`

  * `firebaseabt.experimentresults.get`
  * `firebaseabt.experiments.create`
  * `firebaseabt.experiments.delete`
  * `firebaseabt.experiments.get`
  * `firebaseabt.experiments.list`
  * `firebaseabt.experiments.update`
  * `firebaseabt.projectmetadata.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase A/B Testing Viewer Beta

(`roles/firebaseabt.viewer`) Read-only access to Firebase A/B Testing resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebaseabt.experimentresults.get` `firebaseabt.experiments.get` `firebaseabt.experiments.list` `firebaseabt.projectmetadata.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Firebase A/B Testing permissions

Permission | Included in roles  
---|---  
  
#### `firebaseabt.experimentresults.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebaseabt.experiments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)   
  
#### `firebaseabt.experiments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Firebase Service Management Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.managementServiceAgent) (`roles/firebase.managementServiceAgent`) 

  
  
#### `firebaseabt.experiments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebaseabt.experiments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebaseabt.experiments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)   
  
#### `firebaseabt.projectmetadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase A/B Testing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.admin) (`roles/firebaseabt.admin`)  [Firebase A/B Testing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebaseabt#firebaseabt.viewer) (`roles/firebaseabt.viewer`)  [Firebase Grow Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthAdmin) (`roles/firebase.growthAdmin`)  [Firebase Grow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.growthViewer) (`roles/firebase.growthViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
