---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval/
title: Access Approval roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:29:16.012375+00:00
---

# Access Approval roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Access Approval roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Access Approval. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Access Approval roles

Role | Permissions  
---|---  
  
#### Access Approval Admin 

(`roles/accessapproval.admin`) Admin role for Access Approval  |  `accessapproval.*`

  * `accessapproval.requests.approve`
  * `accessapproval.requests.dismiss`
  * `accessapproval.requests.get`
  * `accessapproval.requests.invalidate`
  * `accessapproval.requests.list`
  * `accessapproval.serviceAccounts.get`
  * `accessapproval.settings.delete`
  * `accessapproval.settings.get`
  * `accessapproval.settings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Approval Editor 

(`roles/accessapproval.editor`) Editor role for Access Approval  |  `accessapproval.requests.get` `accessapproval.requests.list` `accessapproval.serviceAccounts.get` `accessapproval.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Approval Viewer 

(`roles/accessapproval.viewer`) Ability to view access approval requests and configuration  |  `accessapproval.requests.get` `accessapproval.requests.list` `accessapproval.serviceAccounts.get` `accessapproval.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Approval Approver 

(`roles/accessapproval.approver`) Ability to view or act on access approval requests and view configuration.  |  `accessapproval.requests.*`

  * `accessapproval.requests.approve`
  * `accessapproval.requests.dismiss`
  * `accessapproval.requests.get`
  * `accessapproval.requests.invalidate`
  * `accessapproval.requests.list`

`accessapproval.serviceAccounts.get` `accessapproval.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Approval Config Editor 

(`roles/accessapproval.configEditor`) Ability to update the Access Approval configuration  |  `accessapproval.serviceAccounts.get` `accessapproval.settings.*`

  * `accessapproval.settings.delete`
  * `accessapproval.settings.get`
  * `accessapproval.settings.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Access Approval Invalidator 

(`roles/accessapproval.invalidator`) Ability to invalidate existing approved approval requests  |  `accessapproval.requests.invalidate` `accessapproval.serviceAccounts.get` `accessapproval.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Access Approval permissions

Permission | Included in roles  
---|---  
  
#### `accessapproval.requests.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)   
  
#### `accessapproval.requests.dismiss`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)   
  
#### `accessapproval.requests.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.editor) (`roles/accessapproval.editor`)  [Access Approval Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Controls Partner Access Approval Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.accessApprovalServiceAgent) (`roles/cloudcontrolspartner.accessApprovalServiceAgent`) 

  
  
#### `accessapproval.requests.invalidate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)  [Access Approval Invalidator](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.invalidator) (`roles/accessapproval.invalidator`)   
  
#### `accessapproval.requests.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.editor) (`roles/accessapproval.editor`)  [Access Approval Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Controls Partner Access Approval Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudcontrolspartner#cloudcontrolspartner.accessApprovalServiceAgent) (`roles/cloudcontrolspartner.accessApprovalServiceAgent`) 

  
  
#### `accessapproval.serviceAccounts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.editor) (`roles/accessapproval.editor`)  [Access Approval Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)  [Access Approval Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.configEditor) (`roles/accessapproval.configEditor`)  [Access Approval Invalidator](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.invalidator) (`roles/accessapproval.invalidator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `accessapproval.settings.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.configEditor) (`roles/accessapproval.configEditor`)   
  
#### `accessapproval.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.editor) (`roles/accessapproval.editor`)  [Access Approval Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.viewer) (`roles/accessapproval.viewer`)  [Access Approval Approver](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.approver) (`roles/accessapproval.approver`)  [Access Approval Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.configEditor) (`roles/accessapproval.configEditor`)  [Access Approval Invalidator](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.invalidator) (`roles/accessapproval.invalidator`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 
  * [Cloud Security Compliance Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsecuritycompliance#cloudsecuritycompliance.serviceAgent) (`roles/cloudsecuritycompliance.serviceAgent`) 

  
  
#### `accessapproval.settings.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Access Approval Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.admin) (`roles/accessapproval.admin`)  [Access Approval Config Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/accessapproval#accessapproval.configEditor) (`roles/accessapproval.configEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
