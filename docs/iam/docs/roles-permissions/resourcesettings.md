---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings/
title: Resource Settings roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:06.038882+00:00
---

# Resource Settings roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Resource Settings roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Resource Settings. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Resource Settings roles

Role | Permissions  
---|---  
  
#### Resource Settings Administrator 

(`roles/resourcesettings.admin`) Provides admin capabilities to set Resource Setting Values on resources.  Lowest-level resources where you can grant this role:

  * Organization

|  `resourcesettings.*`

  * `resourcesettings.settings.get`
  * `resourcesettings.settings.list`
  * `resourcesettings.settings.update`

  
  
#### Resource Settings Viewer 

(`roles/resourcesettings.viewer`) Provides capabilities to view Resource Settings and Resource Setting Values on resources.  |  `resourcesettings.settings.get` `resourcesettings.settings.list`  
  
## Resource Settings permissions

Permission | Included in roles  
---|---  
  
#### `resourcesettings.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Resource Settings Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings#resourcesettings.admin) (`roles/resourcesettings.admin`)  [Resource Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings#resourcesettings.viewer) (`roles/resourcesettings.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `resourcesettings.settings.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Resource Settings Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings#resourcesettings.admin) (`roles/resourcesettings.admin`)  [Resource Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings#resourcesettings.viewer) (`roles/resourcesettings.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `resourcesettings.settings.update`

|  [Resource Settings Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcesettings#resourcesettings.admin) (`roles/resourcesettings.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
