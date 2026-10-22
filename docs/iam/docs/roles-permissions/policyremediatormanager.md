---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager/
title: Policy Remediator Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:57.197881+00:00
---

# Policy Remediator Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Policy Remediator Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Policy Remediator Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Policy Remediator Manager roles

Role | Permissions  
---|---  
  
#### Policyremediatormanager Admin Beta

(`roles/policyremediatormanager.admin`) Admin role for policyremediatormanager  |  `policyremediatormanager.*`

  * `policyremediatormanager.locations.get`
  * `policyremediatormanager.locations.list`
  * `policyremediatormanager.operations.cancel`
  * `policyremediatormanager.operations.delete`
  * `policyremediatormanager.operations.get`
  * `policyremediatormanager.operations.list`
  * `policyremediatormanager.remediatorServices.disable`
  * `policyremediatormanager.remediatorServices.enable`
  * `policyremediatormanager.remediatorServices.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Policyremediatormanager Viewer Beta

(`roles/policyremediatormanager.viewer`) Viewer role for policyremediatormanager  |  `policyremediatormanager.locations.*`

  * `policyremediatormanager.locations.get`
  * `policyremediatormanager.locations.list`

`policyremediatormanager.operations.get` `policyremediatormanager.operations.list` `policyremediatormanager.remediatorServices.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Policy Remediator Admin Beta

(`roles/policyremediatormanager.policyRemediatorAdmin`) Grants the ability to enable and disable the usage of the policy remediator for the organization  |  `policyremediatormanager.*`

  * `policyremediatormanager.locations.get`
  * `policyremediatormanager.locations.list`
  * `policyremediatormanager.operations.cancel`
  * `policyremediatormanager.operations.delete`
  * `policyremediatormanager.operations.get`
  * `policyremediatormanager.operations.list`
  * `policyremediatormanager.remediatorServices.disable`
  * `policyremediatormanager.remediatorServices.enable`
  * `policyremediatormanager.remediatorServices.get`

  
  
#### Policy Remediator Reader Beta

(`roles/policyremediatormanager.policyRemediatorReader`) Grants the ability to read/view the state of the policy remediator for the organization  |  `policyremediatormanager.locations.*`

  * `policyremediatormanager.locations.get`
  * `policyremediatormanager.locations.list`

`policyremediatormanager.operations.get` `policyremediatormanager.operations.list` `policyremediatormanager.remediatorServices.get`  
  
## Policy Remediator Manager permissions

Permission | Included in roles  
---|---  
  
#### `policyremediatormanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policyremediatormanager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.viewer) (`roles/policyremediatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)  [Policy Remediator Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorReader) (`roles/policyremediatormanager.policyRemediatorReader`)   
  
#### `policyremediatormanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policyremediatormanager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.viewer) (`roles/policyremediatormanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)  [Policy Remediator Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorReader) (`roles/policyremediatormanager.policyRemediatorReader`)   
  
#### `policyremediatormanager.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)   
  
#### `policyremediatormanager.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)   
  
#### `policyremediatormanager.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policyremediatormanager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.viewer) (`roles/policyremediatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)  [Policy Remediator Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorReader) (`roles/policyremediatormanager.policyRemediatorReader`)   
  
#### `policyremediatormanager.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policyremediatormanager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.viewer) (`roles/policyremediatormanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)  [Policy Remediator Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorReader) (`roles/policyremediatormanager.policyRemediatorReader`)   
  
#### `policyremediatormanager.remediatorServices.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)   
  
#### `policyremediatormanager.remediatorServices.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)   
  
#### `policyremediatormanager.remediatorServices.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Policyremediatormanager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.admin) (`roles/policyremediatormanager.admin`)  [Policyremediatormanager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.viewer) (`roles/policyremediatormanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Policy Remediator Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorAdmin) (`roles/policyremediatormanager.policyRemediatorAdmin`)  [Policy Remediator Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/policyremediatormanager#policyremediatormanager.policyRemediatorReader) (`roles/policyremediatormanager.policyRemediatorReader`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
