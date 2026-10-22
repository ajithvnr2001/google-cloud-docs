---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash/
title: Firebase Crashlytics roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:51.450445+00:00
---

# Firebase Crashlytics roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Crashlytics roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Crashlytics. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Crashlytics roles

Role | Permissions  
---|---  
  
#### Firebase Crashlytics Admin 

(`roles/firebasecrashlytics.admin`) Full read/write access to Firebase Crashlytics resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasecrashlytics.*`

  * `firebasecrashlytics.config.get`
  * `firebasecrashlytics.config.update`
  * `firebasecrashlytics.data.get`
  * `firebasecrashlytics.issues.get`
  * `firebasecrashlytics.issues.list`
  * `firebasecrashlytics.issues.update`
  * `firebasecrashlytics.sessions.get`

`logging.logEntries.download` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Crashlytics Viewer 

(`roles/firebasecrashlytics.viewer`) Read-only access to Firebase Crashlytics resources.  |  `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `firebasecrashlytics.config.get` `firebasecrashlytics.data.get` `firebasecrashlytics.issues.get` `firebasecrashlytics.issues.list` `firebasecrashlytics.sessions.get` `logging.logEntries.download` `logging.views.access` `logging.views.listLogs` `logging.views.listResourceKeys` `logging.views.listResourceValues` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Crash Symbol Uploader 

(`roles/firebasecrash.symbolMappingsAdmin`) Full read/write access to symbol mapping file resources for Firebase Crash Reporting.  |  `firebase.clients.get` `firebase.clients.list` `resourcemanager.projects.get`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Firebase Crashlytics Service Agent 

(`roles/firebasecrashlytics.serviceAgent`) Access to BigQuery export for Crashlytics  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.update` `bigquery.tables.updateData` `serviceusage.services.use`  
  
## Firebase Crashlytics permissions

Permission | Included in roles  
---|---  
  
#### `firebasecrash.issues.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)   
  
#### `firebasecrash.reports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebasecrashlytics.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebasecrashlytics.config.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)   
  
#### `firebasecrashlytics.data.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebasecrashlytics.issues.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebasecrashlytics.issues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `firebasecrashlytics.issues.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)   
  
#### `firebasecrashlytics.sessions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Crashlytics Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.admin) (`roles/firebasecrashlytics.admin`)  [Firebase Crashlytics Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecrash#firebasecrashlytics.viewer) (`roles/firebasecrashlytics.viewer`)  [Firebase Quality Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityAdmin) (`roles/firebase.qualityAdmin`)  [Firebase Quality Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.qualityViewer) (`roles/firebase.qualityViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
