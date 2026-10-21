---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm/
title: Google Security Operations Service Management roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:12:53.588406+00:00
---

# Google Security Operations Service Management roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Security Operations Service Management roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Security Operations Service Management. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Security Operations Service Management roles

Role | Permissions  
---|---  
  
#### Chronicle Service Admin 

(`roles/chroniclesm.admin`) Admins can view and modify Chronicle service details.  |  `chroniclesm.*`

  * `chroniclesm.contracts.get`
  * `chroniclesm.contracts.update`
  * `chroniclesm.gcpAssociations.create`
  * `chroniclesm.gcpAssociations.delete`
  * `chroniclesm.gcpAssociations.get`
  * `chroniclesm.gcpAssociations.list`
  * `chroniclesm.gcpLogFlowFilters.get`
  * `chroniclesm.gcpLogFlowFilters.update`
  * `chroniclesm.gcpSettings.get`
  * `chroniclesm.gcpSettings.update`
  * `chroniclesm.soarRoleScripts.list`

  
  
#### Chroniclesm Editor 

(`roles/chroniclesm.editor`) Editor role for chroniclesm  |  `chroniclesm.contracts.*`

  * `chroniclesm.contracts.get`
  * `chroniclesm.contracts.update`

`chroniclesm.gcpAssociations.get` `chroniclesm.gcpAssociations.list` `chroniclesm.gcpLogFlowFilters.*`

  * `chroniclesm.gcpLogFlowFilters.get`
  * `chroniclesm.gcpLogFlowFilters.update`

`chroniclesm.gcpSettings.*`

  * `chroniclesm.gcpSettings.get`
  * `chroniclesm.gcpSettings.update`

`chroniclesm.soarRoleScripts.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chronicle Service Viewer 

(`roles/chroniclesm.viewer`) Viewers can see Chronicle service details but not change them.  |  `chroniclesm.contracts.get` `chroniclesm.gcpAssociations.get` `chroniclesm.gcpAssociations.list` `chroniclesm.gcpLogFlowFilters.get` `chroniclesm.gcpSettings.get` `chroniclesm.soarRoleScripts.list`  
  
## Google Security Operations Service Management permissions

Permission | Included in roles  
---|---  
  
#### `chroniclesm.contracts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chroniclesm.contracts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)   
  
#### `chroniclesm.gcpAssociations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)   
  
#### `chroniclesm.gcpAssociations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)   
  
#### `chroniclesm.gcpAssociations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chroniclesm.gcpAssociations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chroniclesm.gcpLogFlowFilters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chroniclesm.gcpLogFlowFilters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)   
  
#### `chroniclesm.gcpSettings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chroniclesm.gcpSettings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)   
  
#### `chroniclesm.soarRoleScripts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chronicle Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.admin) (`roles/chroniclesm.admin`)  [Chroniclesm Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.editor) (`roles/chroniclesm.editor`)  [Chronicle Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chroniclesm#chroniclesm.viewer) (`roles/chroniclesm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
