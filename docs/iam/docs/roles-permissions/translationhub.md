---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub/
title: Translation Hub roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:46.176005+00:00
---

# Translation Hub roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Translation Hub roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Translation Hub. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Translation Hub roles

Role | Permissions  
---|---  
  
#### Translation Hub Admin Beta

(`roles/translationhub.admin`) Admin of Translation Hub  |  `automl.models.get` `automl.models.list` `automl.models.predict` `cloudtranslate.customModels.get` `cloudtranslate.customModels.list` `cloudtranslate.customModels.predict` `cloudtranslate.glossaries.create` `cloudtranslate.glossaries.delete` `cloudtranslate.glossaries.get` `cloudtranslate.glossaries.list` `cloudtranslate.glossaries.predict` `resourcemanager.projects.get` `resourcemanager.projects.list` `translationhub.*`

  * `translationhub.portals.create`
  * `translationhub.portals.delete`
  * `translationhub.portals.get`
  * `translationhub.portals.list`
  * `translationhub.portals.update`

  
  
#### Translation Hub Viewer Beta

(`roles/translationhub.viewer`) Viewer role for Translation Hub  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `translationhub.portals.get` `translationhub.portals.list`  
  
#### Translation Hub Portal User Beta

(`roles/translationhub.portalUser`) Portal user of Translation Hub  |  `automl.models.get` `automl.models.list` `automl.models.predict` `cloudtranslate.customModels.get` `cloudtranslate.customModels.list` `cloudtranslate.customModels.predict` `cloudtranslate.glossaries.get` `cloudtranslate.glossaries.list` `cloudtranslate.glossaries.predict` `resourcemanager.projects.get` `resourcemanager.projects.list` `translationhub.portals.get` `translationhub.portals.list`  
  
## Translation Hub permissions

Permission | Included in roles  
---|---  
  
#### `translationhub.portals.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)   
  
#### `translationhub.portals.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)   
  
#### `translationhub.portals.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)  [Translation Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.viewer) (`roles/translationhub.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Translation Hub Portal User](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.portalUser) (`roles/translationhub.portalUser`)   
  
#### `translationhub.portals.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)  [Translation Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.viewer) (`roles/translationhub.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Translation Hub Portal User](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.portalUser) (`roles/translationhub.portalUser`)   
  
#### `translationhub.portals.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Translation Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/translationhub#translationhub.admin) (`roles/translationhub.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
