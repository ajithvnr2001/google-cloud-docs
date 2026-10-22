---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect/
title: Apigee Connect roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:31.671568+00:00
---

# Apigee Connect roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Apigee Connect roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Apigee Connect. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Apigee Connect roles

Role | Permissions  
---|---  
  
#### Apigee Connect Admin 

(`roles/apigeeconnect.Admin`) Admin of Apigee Connect  |  `apigeeconnect.*`

  * `apigeeconnect.connections.list`
  * `apigeeconnect.endpoints.connect`

  
  
#### Apigeeconnect Viewer 

(`roles/apigeeconnect.viewer`) Viewer role for apigeeconnect  |  `apigeeconnect.connections.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Apigee Connect Agent 

(`roles/apigeeconnect.Agent`) Ability to set up Apigee Connect agent between external clusters and Google.  |  `apigeeconnect.endpoints.connect`  
  
## Apigee Connect permissions

Permission | Included in roles  
---|---  
  
#### `apigeeconnect.connections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Apigee Connect Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Admin) (`roles/apigeeconnect.Admin`)  [Apigeeconnect Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.viewer) (`roles/apigeeconnect.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeconnect.endpoints.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Apigee Connect Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Admin) (`roles/apigeeconnect.Admin`)  [Apigee Connect Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeconnect#apigeeconnect.Agent) (`roles/apigeeconnect.Agent`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
