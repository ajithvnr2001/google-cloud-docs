---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting/
title: Error Reporting roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:19.375696+00:00
---

# Error Reporting roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Error Reporting roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Error Reporting. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Error Reporting roles

Role | Permissions  
---|---  
  
#### Error Reporting Admin Beta

(`roles/errorreporting.admin`) Provides full access to Error Reporting data.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.*`

  * `errorreporting.applications.list`
  * `errorreporting.errorEvents.create`
  * `errorreporting.errorEvents.delete`
  * `errorreporting.errorEvents.list`
  * `errorreporting.groupMetadata.get`
  * `errorreporting.groupMetadata.update`
  * `errorreporting.groups.list`

`logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting User Beta

(`roles/errorreporting.user`) Provides the permissions to read and write Error Reporting data, except for sending new error events.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.applications.list` `errorreporting.errorEvents.delete` `errorreporting.errorEvents.list` `errorreporting.groupMetadata.*`

  * `errorreporting.groupMetadata.get`
  * `errorreporting.groupMetadata.update`

`errorreporting.groups.list` `logging.notificationRules.*`

  * `logging.notificationRules.create`
  * `logging.notificationRules.delete`
  * `logging.notificationRules.get`
  * `logging.notificationRules.list`
  * `logging.notificationRules.update`

`resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting Viewer Beta

(`roles/errorreporting.viewer`) Provides read-only access to Error Reporting data.  Lowest-level resources where you can grant this role:

  * Project 

|  `cloudnotifications.activities.list` `errorreporting.applications.list` `errorreporting.errorEvents.list` `errorreporting.groupMetadata.get` `errorreporting.groups.list` `logging.notificationRules.get` `logging.notificationRules.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `stackdriver.projects.get`  
  
#### Error Reporting Writer Beta

(`roles/errorreporting.writer`) Provides the permissions to send error events to Error Reporting.  Lowest-level resources where you can grant this role:

  * Service Account 

|  `errorreporting.errorEvents.create`  
  
## Error Reporting permissions

Permission | Included in roles  
---|---  
  
#### `errorreporting.applications.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)  [Error Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.viewer) (`roles/errorreporting.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `errorreporting.errorEvents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.writer) (`roles/errorreporting.writer`)   
  
#### `errorreporting.errorEvents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)   
  
#### `errorreporting.errorEvents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)  [Error Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.viewer) (`roles/errorreporting.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `errorreporting.groupMetadata.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)  [Error Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.viewer) (`roles/errorreporting.viewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `errorreporting.groupMetadata.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)   
  
#### `errorreporting.groups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Error Reporting Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.admin) (`roles/errorreporting.admin`)  [Error Reporting User](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.user) (`roles/errorreporting.user`)  [Error Reporting Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/errorreporting#errorreporting.viewer) (`roles/errorreporting.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Hub Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudhub#cloudhub.operator) (`roles/cloudhub.operator`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Firebase Develop Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developViewer) (`roles/firebase.developViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Site Reliability Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.siteReliabilityEngineer) (`roles/iam.siteReliabilityEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
