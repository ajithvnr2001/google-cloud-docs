---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation/
title: Appliance Activation Service roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:57.438861+00:00
---

# Appliance Activation Service roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Appliance Activation Service roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Appliance Activation Service. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Appliance Activation Service roles

Role | Permissions  
---|---  
  
#### Appliance Admin Beta

(`roles/applianceactivation.admin`) Admin role for Appliance  |  `applianceactivation.*`

  * `applianceactivation.rttCommands.approve`
  * `applianceactivation.rttCommands.create`
  * `applianceactivation.rttCommands.get`
  * `applianceactivation.rttCommands.list`
  * `applianceactivation.rttCommands.sendResult`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Appliance Viewer Beta

(`roles/applianceactivation.viewer`) Viewer role for Appliance  |  `applianceactivation.rttCommands.get` `applianceactivation.rttCommands.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Appliance troubleshooting commands approver Beta

(`roles/applianceactivation.approver`) Grants access to approve commands to run on appliances  |  `applianceactivation.rttCommands.approve` `applianceactivation.rttCommands.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### On-appliance troubleshooting client Beta

(`roles/applianceactivation.client`) Grants access to read commands for an appliance and send its result.  |  `applianceactivation.rttCommands.get` `applianceactivation.rttCommands.sendResult`  
  
#### Appliance troubleshooter Beta

(`roles/applianceactivation.troubleshooter`) Grants access to send new commands to run on appliances and view the outputs  |  `applianceactivation.rttCommands.create` `applianceactivation.rttCommands.get` `applianceactivation.rttCommands.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Appliance Activation Service permissions

Permission | Included in roles  
---|---  
  
#### `applianceactivation.rttCommands.approve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.admin) (`roles/applianceactivation.admin`)  [Appliance troubleshooting commands approver](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.approver) (`roles/applianceactivation.approver`)   
  
#### `applianceactivation.rttCommands.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.admin) (`roles/applianceactivation.admin`)  [Appliance troubleshooter](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.troubleshooter) (`roles/applianceactivation.troubleshooter`)   
  
#### `applianceactivation.rttCommands.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.admin) (`roles/applianceactivation.admin`)  [Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.viewer) (`roles/applianceactivation.viewer`)  [Appliance troubleshooting commands approver](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.approver) (`roles/applianceactivation.approver`)  [On-appliance troubleshooting client](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.client) (`roles/applianceactivation.client`)  [Appliance troubleshooter](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.troubleshooter) (`roles/applianceactivation.troubleshooter`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `applianceactivation.rttCommands.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.admin) (`roles/applianceactivation.admin`)  [Appliance Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.viewer) (`roles/applianceactivation.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Appliance troubleshooter](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.troubleshooter) (`roles/applianceactivation.troubleshooter`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `applianceactivation.rttCommands.sendResult`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Appliance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.admin) (`roles/applianceactivation.admin`)  [On-appliance troubleshooting client](https://docs.cloud.google.com/iam/docs/roles-permissions/applianceactivation#applianceactivation.client) (`roles/applianceactivation.client`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
