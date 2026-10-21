---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing/
title: Enterprise Purchasing API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:07:26.934466+00:00
---

# Enterprise Purchasing API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Enterprise Purchasing API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Enterprise Purchasing API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Enterprise Purchasing API roles

Role | Permissions  
---|---  
  
#### Enterprise Purchasing Admin Beta

(`roles/enterprisepurchasing.admin`) Full access to Enterprise Purchasing resources.  |  `enterprisepurchasing.*`

  * `enterprisepurchasing.gcveCuds.create`
  * `enterprisepurchasing.gcveCuds.get`
  * `enterprisepurchasing.gcveCuds.list`
  * `enterprisepurchasing.gcveNodePricingInfo.list`
  * `enterprisepurchasing.licenseKeys.create`
  * `enterprisepurchasing.licenseKeys.delete`
  * `enterprisepurchasing.licenseKeys.get`
  * `enterprisepurchasing.licenseKeys.list`
  * `enterprisepurchasing.locations.get`
  * `enterprisepurchasing.locations.list`
  * `enterprisepurchasing.operations.cancel`
  * `enterprisepurchasing.operations.delete`
  * `enterprisepurchasing.operations.get`
  * `enterprisepurchasing.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Enterprise Purchasing Editor Beta

(`roles/enterprisepurchasing.editor`) Edit access to Enterprise Purchasing resources.  |  `enterprisepurchasing.gcveCuds.get` `enterprisepurchasing.gcveCuds.list` `enterprisepurchasing.gcveNodePricingInfo.list` `enterprisepurchasing.licenseKeys.get` `enterprisepurchasing.licenseKeys.list` `enterprisepurchasing.locations.*`

  * `enterprisepurchasing.locations.get`
  * `enterprisepurchasing.locations.list`

`enterprisepurchasing.operations.get` `enterprisepurchasing.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Enterprise Purchasing Viewer Beta

(`roles/enterprisepurchasing.viewer`) Readonly access to Enterprise Purchasing resources.  |  `enterprisepurchasing.gcveCuds.get` `enterprisepurchasing.gcveCuds.list` `enterprisepurchasing.gcveNodePricingInfo.list` `enterprisepurchasing.licenseKeys.get` `enterprisepurchasing.licenseKeys.list` `enterprisepurchasing.locations.*`

  * `enterprisepurchasing.locations.get`
  * `enterprisepurchasing.locations.list`

`enterprisepurchasing.operations.get` `enterprisepurchasing.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Enterprise Purchasing API permissions

Permission | Included in roles  
---|---  
  
#### `enterprisepurchasing.gcveCuds.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)   
  
#### `enterprisepurchasing.gcveCuds.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.gcveCuds.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.gcveNodePricingInfo.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.licenseKeys.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)   
  
#### `enterprisepurchasing.licenseKeys.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)   
  
#### `enterprisepurchasing.licenseKeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.licenseKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)   
  
#### `enterprisepurchasing.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)   
  
#### `enterprisepurchasing.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterprisepurchasing.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Purchasing Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.admin) (`roles/enterprisepurchasing.admin`)  [Enterprise Purchasing Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.editor) (`roles/enterprisepurchasing.editor`)  [Enterprise Purchasing Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterprisepurchasing#enterprisepurchasing.viewer) (`roles/enterprisepurchasing.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
