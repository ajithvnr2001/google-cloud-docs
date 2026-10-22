---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions/
title: Service Extensions roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:54.547125+00:00
---

# Service Extensions roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Service Extensions roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Service Extensions. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Service Extensions roles

Role | Permissions  
---|---  
  
#### Service Extensions Admin Beta

(`roles/serviceextensions.admin`) Grants full access to Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.*`

  * `serviceextensions.callouts.invoke`
  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
#### Service Extensions Editor Beta

(`roles/serviceextensions.editor`) Grants access to edit Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.*`

  * `serviceextensions.callouts.invoke`
  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
#### Service Extensions Viewer Beta

(`roles/serviceextensions.viewer`) Grants read access to Service Extensions resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceextensions.locations.*`

  * `serviceextensions.locations.get`
  * `serviceextensions.locations.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Network Actions Service Agent 

(`roles/networkactions.serviceAgent`) Gives Network Actions service account access to read required resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `artifactregistry.files.download` `artifactregistry.repositories.downloadArtifacts`  
  
## Service Extensions permissions

Permission | Included in roles  
---|---  
  
#### `serviceextensions.callouts.invoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Service Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.admin) (`roles/serviceextensions.admin`)  [Service Extensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.editor) (`roles/serviceextensions.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Discovery Engine Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.serviceAgent) (`roles/discoveryengine.serviceAgent`) 

  
  
#### `serviceextensions.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Service Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.admin) (`roles/serviceextensions.admin`)  [Service Extensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.editor) (`roles/serviceextensions.editor`)  [Service Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.viewer) (`roles/serviceextensions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `serviceextensions.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Service Extensions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.admin) (`roles/serviceextensions.admin`)  [Service Extensions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.editor) (`roles/serviceextensions.editor`)  [Service Extensions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceextensions#serviceextensions.viewer) (`roles/serviceextensions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
