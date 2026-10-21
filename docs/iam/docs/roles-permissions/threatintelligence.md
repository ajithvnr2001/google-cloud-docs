---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence/
title: Google Threat Intelligence roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:12:22.577024+00:00
---

# Google Threat Intelligence roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Threat Intelligence roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Threat Intelligence. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Threat Intelligence roles

Role | Permissions  
---|---  
  
#### GTI Alert Admin Beta

(`roles/threatintelligence.alertAdmin`) This role can view and edit all properties of resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.*`

  * `threatintelligence.alertdocuments.get`
  * `threatintelligence.alerts.get`
  * `threatintelligence.alerts.list`
  * `threatintelligence.alerts.update`
  * `threatintelligence.configurations.get`
  * `threatintelligence.configurations.list`
  * `threatintelligence.configurations.listRevisions`
  * `threatintelligence.configurations.update`
  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
#### GTI Alert User Beta

(`roles/threatintelligence.alertUser`) This role can view and edit properties of resources, except for editing configurations and exporting alerts.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.alertdocuments.get` `threatintelligence.alerts.*`

  * `threatintelligence.alerts.get`
  * `threatintelligence.alerts.list`
  * `threatintelligence.alerts.update`

`threatintelligence.configurations.get` `threatintelligence.configurations.list` `threatintelligence.configurations.listRevisions` `threatintelligence.findings.*`

  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
#### CTEM Admin Beta

(`roles/threatintelligence.ctemAdmin`) This role can view and edit all properties of resources along with the Projects.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.configurations.*`

  * `threatintelligence.configurations.get`
  * `threatintelligence.configurations.list`
  * `threatintelligence.configurations.listRevisions`
  * `threatintelligence.configurations.update`

`threatintelligence.findings.*`

  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
#### CTEM Editor Beta

(`roles/threatintelligence.ctemEditor`) This role can view and edit all properties of resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.configurations.*`

  * `threatintelligence.configurations.get`
  * `threatintelligence.configurations.list`
  * `threatintelligence.configurations.listRevisions`
  * `threatintelligence.configurations.update`

`threatintelligence.findings.*`

  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
#### CTEM Project Admin Beta

(`roles/threatintelligence.ctemProjectAdmin`) CTEM Project Admin  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.configurations.get` `threatintelligence.configurations.list` `threatintelligence.configurations.update` `threatintelligence.findings.*`

  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
#### CTEM Viewer Beta

(`roles/threatintelligence.ctemViewer`) This role can view all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `threatintelligence.configurations.get` `threatintelligence.configurations.list` `threatintelligence.configurations.listRevisions` `threatintelligence.findings.*`

  * `threatintelligence.findings.get`
  * `threatintelligence.findings.list`

  
  
## Google Threat Intelligence permissions

Permission | Included in roles  
---|---  
  
#### `threatintelligence.alertdocuments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)   
  
#### `threatintelligence.alerts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)   
  
#### `threatintelligence.alerts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)   
  
#### `threatintelligence.alerts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)   
  
#### `threatintelligence.configurations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemProjectAdmin) (`roles/threatintelligence.ctemProjectAdmin`)  [CTEM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemViewer) (`roles/threatintelligence.ctemViewer`)   
  
#### `threatintelligence.configurations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemProjectAdmin) (`roles/threatintelligence.ctemProjectAdmin`)  [CTEM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemViewer) (`roles/threatintelligence.ctemViewer`)   
  
#### `threatintelligence.configurations.listRevisions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemViewer) (`roles/threatintelligence.ctemViewer`)   
  
#### `threatintelligence.configurations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemProjectAdmin) (`roles/threatintelligence.ctemProjectAdmin`)   
  
#### `threatintelligence.findings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemProjectAdmin) (`roles/threatintelligence.ctemProjectAdmin`)  [CTEM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemViewer) (`roles/threatintelligence.ctemViewer`)   
  
#### `threatintelligence.findings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [GTI Alert Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertAdmin) (`roles/threatintelligence.alertAdmin`)  [GTI Alert User](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.alertUser) (`roles/threatintelligence.alertUser`)  [CTEM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemAdmin) (`roles/threatintelligence.ctemAdmin`)  [CTEM Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemEditor) (`roles/threatintelligence.ctemEditor`)  [CTEM Project Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemProjectAdmin) (`roles/threatintelligence.ctemProjectAdmin`)  [CTEM Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/threatintelligence#threatintelligence.ctemViewer) (`roles/threatintelligence.ctemViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
