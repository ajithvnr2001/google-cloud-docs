---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder/
title: Transcoder API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:24:46.457275+00:00
---

# Transcoder API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Transcoder API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Transcoder API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Transcoder API roles

Role | Permissions  
---|---  
  
#### Transcoder Admin 

(`roles/transcoder.admin`) Full access to all transcoder resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transcoder.*`

  * `transcoder.jobTemplates.create`
  * `transcoder.jobTemplates.createTagBinding`
  * `transcoder.jobTemplates.delete`
  * `transcoder.jobTemplates.deleteTagBinding`
  * `transcoder.jobTemplates.get`
  * `transcoder.jobTemplates.list`
  * `transcoder.jobTemplates.listEffectiveTags`
  * `transcoder.jobTemplates.listTagBindings`
  * `transcoder.jobs.create`
  * `transcoder.jobs.createTagBinding`
  * `transcoder.jobs.delete`
  * `transcoder.jobs.deleteTagBinding`
  * `transcoder.jobs.get`
  * `transcoder.jobs.list`
  * `transcoder.jobs.listEffectiveTags`
  * `transcoder.jobs.listTagBindings`

  
  
#### Transcoder Editor 

(`roles/transcoder.editor`) Editor role for transcoder  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transcoder.jobTemplates.create` `transcoder.jobTemplates.delete` `transcoder.jobTemplates.get` `transcoder.jobTemplates.list` `transcoder.jobTemplates.listEffectiveTags` `transcoder.jobTemplates.listTagBindings` `transcoder.jobs.create` `transcoder.jobs.delete` `transcoder.jobs.get` `transcoder.jobs.list` `transcoder.jobs.listEffectiveTags` `transcoder.jobs.listTagBindings`  
  
#### Transcoder Viewer 

(`roles/transcoder.viewer`) Viewer of all transcoder resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `transcoder.jobTemplates.get` `transcoder.jobTemplates.list` `transcoder.jobTemplates.listEffectiveTags` `transcoder.jobTemplates.listTagBindings` `transcoder.jobs.get` `transcoder.jobs.list` `transcoder.jobs.listEffectiveTags` `transcoder.jobs.listTagBindings`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Transcoder Service Agent 

(`roles/transcoder.serviceAgent`) Downloads and uploads media files from and to customer Cloud Storage buckets. Publishes status updates to customer Pub/Sub.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `pubsub.topics.publish` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `transcoder.jobs.delete`  
  
## Transcoder API permissions

Permission | Included in roles  
---|---  
  
#### `transcoder.jobTemplates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)   
  
#### `transcoder.jobTemplates.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `transcoder.jobTemplates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)   
  
#### `transcoder.jobTemplates.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `transcoder.jobTemplates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobTemplates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobTemplates.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobTemplates.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 

  
  
#### `transcoder.jobs.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `transcoder.jobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 
  * [Transcoder Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.serviceAgent) (`roles/transcoder.serviceAgent`) 

  
  
#### `transcoder.jobs.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `transcoder.jobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Media Asset Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/mediaasset#mediaasset.serviceAgent) (`roles/mediaasset.serviceAgent`) 

  
  
#### `transcoder.jobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobs.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `transcoder.jobs.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Transcoder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.admin) (`roles/transcoder.admin`)  [Transcoder Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.editor) (`roles/transcoder.editor`)  [Transcoder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/transcoder#transcoder.viewer) (`roles/transcoder.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
