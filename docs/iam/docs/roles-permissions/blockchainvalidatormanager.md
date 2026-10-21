---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager/
title: Blockchain Validator Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:06:20.467824+00:00
---

# Blockchain Validator Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Blockchain Validator Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Blockchain Validator Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Blockchain Validator Manager roles

Role | Permissions  
---|---  
  
#### Blockchain Validator Manager Admin Beta

(`roles/blockchainvalidatormanager.admin`) Full access to Blockchain Validator Manager resources.  |  `blockchainvalidatormanager.*`

  * `blockchainvalidatormanager.blockchainValidatorConfigs.create`
  * `blockchainvalidatormanager.blockchainValidatorConfigs.delete`
  * `blockchainvalidatormanager.blockchainValidatorConfigs.get`
  * `blockchainvalidatormanager.blockchainValidatorConfigs.list`
  * `blockchainvalidatormanager.blockchainValidatorConfigs.update`
  * `blockchainvalidatormanager.locations.get`
  * `blockchainvalidatormanager.locations.list`
  * `blockchainvalidatormanager.operations.cancel`
  * `blockchainvalidatormanager.operations.delete`
  * `blockchainvalidatormanager.operations.get`
  * `blockchainvalidatormanager.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Blockchain Validator Viewer Beta

(`roles/blockchainvalidatormanager.viewer`) Readonly access to Blockchain Validator Manager resources.  |  `blockchainvalidatormanager.blockchainValidatorConfigs.get` `blockchainvalidatormanager.blockchainValidatorConfigs.list` `blockchainvalidatormanager.locations.*`

  * `blockchainvalidatormanager.locations.get`
  * `blockchainvalidatormanager.locations.list`

`blockchainvalidatormanager.operations.get` `blockchainvalidatormanager.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Blockchain Validator Manager permissions

Permission | Included in roles  
---|---  
  
#### `blockchainvalidatormanager.blockchainValidatorConfigs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)   
  
#### `blockchainvalidatormanager.blockchainValidatorConfigs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)   
  
#### `blockchainvalidatormanager.blockchainValidatorConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `blockchainvalidatormanager.blockchainValidatorConfigs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `blockchainvalidatormanager.blockchainValidatorConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)   
  
#### `blockchainvalidatormanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `blockchainvalidatormanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `blockchainvalidatormanager.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)   
  
#### `blockchainvalidatormanager.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)   
  
#### `blockchainvalidatormanager.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `blockchainvalidatormanager.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Blockchain Validator Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.admin) (`roles/blockchainvalidatormanager.admin`)  [Blockchain Validator Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/blockchainvalidatormanager#blockchainvalidatormanager.viewer) (`roles/blockchainvalidatormanager.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
