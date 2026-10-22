---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors/
title: Data Connectors roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:06.694189+00:00
---

# Data Connectors roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Connectors roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Connectors. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Connectors roles

Role | Permissions  
---|---  
  
#### Data Connectors Admin Beta

(`roles/dataconnectors.admin`) Admin role for Data Connectors  |  `dataconnectors.*`

  * `dataconnectors.connectors.create`
  * `dataconnectors.connectors.delete`
  * `dataconnectors.connectors.get`
  * `dataconnectors.connectors.getIamPolicy`
  * `dataconnectors.connectors.list`
  * `dataconnectors.connectors.setIamPolicy`
  * `dataconnectors.connectors.update`
  * `dataconnectors.connectors.use`
  * `dataconnectors.locations.get`
  * `dataconnectors.locations.list`
  * `dataconnectors.operations.cancel`
  * `dataconnectors.operations.delete`
  * `dataconnectors.operations.get`
  * `dataconnectors.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Connectors Editor Beta

(`roles/dataconnectors.editor`) Editor role for Data Connectors  |  `dataconnectors.connectors.create` `dataconnectors.connectors.delete` `dataconnectors.connectors.get` `dataconnectors.connectors.getIamPolicy` `dataconnectors.connectors.list` `dataconnectors.connectors.update` `dataconnectors.connectors.use` `dataconnectors.locations.*`

  * `dataconnectors.locations.get`
  * `dataconnectors.locations.list`

`dataconnectors.operations.*`

  * `dataconnectors.operations.cancel`
  * `dataconnectors.operations.delete`
  * `dataconnectors.operations.get`
  * `dataconnectors.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Connectors Viewer Beta

(`roles/dataconnectors.viewer`) Viewer role for Data Connectors  |  `dataconnectors.connectors.get` `dataconnectors.connectors.getIamPolicy` `dataconnectors.connectors.list` `dataconnectors.locations.*`

  * `dataconnectors.locations.get`
  * `dataconnectors.locations.list`

`dataconnectors.operations.get` `dataconnectors.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Connector Admin Beta

(`roles/dataconnectors.connectorAdmin`) Full access to Data Connectors.  |  `dataconnectors.*`

  * `dataconnectors.connectors.create`
  * `dataconnectors.connectors.delete`
  * `dataconnectors.connectors.get`
  * `dataconnectors.connectors.getIamPolicy`
  * `dataconnectors.connectors.list`
  * `dataconnectors.connectors.setIamPolicy`
  * `dataconnectors.connectors.update`
  * `dataconnectors.connectors.use`
  * `dataconnectors.locations.get`
  * `dataconnectors.locations.list`
  * `dataconnectors.operations.cancel`
  * `dataconnectors.operations.delete`
  * `dataconnectors.operations.get`
  * `dataconnectors.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Connector User Beta

(`roles/dataconnectors.connectorUser`) Access to use Data Connectors.  |  `dataconnectors.connectors.get` `dataconnectors.connectors.getIamPolicy` `dataconnectors.connectors.list` `dataconnectors.connectors.use`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Data Connectors Service Agent 

(`roles/dataconnectors.serviceAgent`) Gives Data Connectors service agent permission to access the virtual private cloud  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalOperations.get` `compute.networks.access` `vpcaccess.connectors.get`  
  
## Data Connectors permissions

Permission | Included in roles  
---|---  
  
#### `dataconnectors.connectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.connectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.connectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Data Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorUser) (`roles/dataconnectors.connectorUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.connectors.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Data Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorUser) (`roles/dataconnectors.connectorUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.connectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Data Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorUser) (`roles/dataconnectors.connectorUser`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.connectors.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.connectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.connectors.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Data Connector User](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorUser) (`roles/dataconnectors.connectorUser`)   
  
#### `dataconnectors.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)   
  
#### `dataconnectors.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataconnectors.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Connectors Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.admin) (`roles/dataconnectors.admin`)  [Data Connectors Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.editor) (`roles/dataconnectors.editor`)  [Data Connectors Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.viewer) (`roles/dataconnectors.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataconnectors#dataconnectors.connectorAdmin) (`roles/dataconnectors.connectorAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
