---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/domains/
title: Cloud Domains roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:24.244350+00:00
---

# Cloud Domains roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/domains/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Domains roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Domains. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Domains roles

Role | Permissions  
---|---  
  
#### Cloud Domains Admin 

(`roles/domains.admin`) Full access to Cloud Domains Registrations and related resources.  |  `domains.*`

  * `domains.locations.get`
  * `domains.locations.list`
  * `domains.operations.cancel`
  * `domains.operations.get`
  * `domains.operations.list`
  * `domains.registrations.configureContact`
  * `domains.registrations.configureDns`
  * `domains.registrations.configureManagement`
  * `domains.registrations.create`
  * `domains.registrations.createTagBinding`
  * `domains.registrations.delete`
  * `domains.registrations.deleteTagBinding`
  * `domains.registrations.get`
  * `domains.registrations.getIamPolicy`
  * `domains.registrations.list`
  * `domains.registrations.listEffectiveTags`
  * `domains.registrations.listTagBindings`
  * `domains.registrations.setIamPolicy`
  * `domains.registrations.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Domains Editor 

(`roles/domains.editor`) Editor role for Cloud Domains  |  `domains.locations.*`

  * `domains.locations.get`
  * `domains.locations.list`

`domains.operations.*`

  * `domains.operations.cancel`
  * `domains.operations.get`
  * `domains.operations.list`

`domains.registrations.configureContact` `domains.registrations.configureDns` `domains.registrations.configureManagement` `domains.registrations.create` `domains.registrations.delete` `domains.registrations.get` `domains.registrations.getIamPolicy` `domains.registrations.list` `domains.registrations.listEffectiveTags` `domains.registrations.listTagBindings` `domains.registrations.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Domains Viewer 

(`roles/domains.viewer`) Read-only access to Cloud Domains Registrations and related resources.  |  `domains.locations.*`

  * `domains.locations.get`
  * `domains.locations.list`

`domains.operations.get` `domains.operations.list` `domains.registrations.get` `domains.registrations.getIamPolicy` `domains.registrations.list` `domains.registrations.listEffectiveTags` `domains.registrations.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud Domains permissions

Permission | Included in roles  
---|---  
  
#### `domains.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.configureContact`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.registrations.configureDns`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.registrations.configureManagement`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.registrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.registrations.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `domains.registrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
#### `domains.registrations.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `domains.registrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)  [Cloud Domains Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.viewer) (`roles/domains.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `domains.registrations.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `domains.registrations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Domains Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.admin) (`roles/domains.admin`)  [Cloud Domains Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/domains#domains.editor) (`roles/domains.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
