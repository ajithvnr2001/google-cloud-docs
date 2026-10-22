---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons/
title: Google Workspace add-ons roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:32.458635+00:00
---

# Google Workspace add-ons roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Workspace add-ons roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Workspace add-ons. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Workspace add-ons roles

Role | Permissions  
---|---  
  
#### Google Workspace Add-ons Admin 

(`roles/gsuiteaddons.admin`) Admin role for Google Workspace Add-ons  |  `chat.*`

  * `chat.bots.get`
  * `chat.bots.update`

`gsuiteaddons.*`

  * `gsuiteaddons.authorizations.get`
  * `gsuiteaddons.chatAppConfigs.get`
  * `gsuiteaddons.chatAppConfigs.update`
  * `gsuiteaddons.deployments.create`
  * `gsuiteaddons.deployments.delete`
  * `gsuiteaddons.deployments.execute`
  * `gsuiteaddons.deployments.get`
  * `gsuiteaddons.deployments.install`
  * `gsuiteaddons.deployments.installStatus`
  * `gsuiteaddons.deployments.list`
  * `gsuiteaddons.deployments.uninstall`
  * `gsuiteaddons.deployments.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Workspace Add-ons Viewer 

(`roles/gsuiteaddons.viewer`) Viewer role for Google Workspace Add-ons  |  `chat.bots.get` `gsuiteaddons.authorizations.get` `gsuiteaddons.chatAppConfigs.get` `gsuiteaddons.deployments.get` `gsuiteaddons.deployments.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Workspace Add-ons Developer 

(`roles/gsuiteaddons.developer`) Full access to Google Workspace Add-ons resources  |  `chat.*`

  * `chat.bots.get`
  * `chat.bots.update`

`gsuiteaddons.*`

  * `gsuiteaddons.authorizations.get`
  * `gsuiteaddons.chatAppConfigs.get`
  * `gsuiteaddons.chatAppConfigs.update`
  * `gsuiteaddons.deployments.create`
  * `gsuiteaddons.deployments.delete`
  * `gsuiteaddons.deployments.execute`
  * `gsuiteaddons.deployments.get`
  * `gsuiteaddons.deployments.install`
  * `gsuiteaddons.deployments.installStatus`
  * `gsuiteaddons.deployments.list`
  * `gsuiteaddons.deployments.uninstall`
  * `gsuiteaddons.deployments.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Workspace Add-ons Reader 

(`roles/gsuiteaddons.reader`) Read-only access to Google Workspace Add-ons resources  |  `chat.bots.get` `gsuiteaddons.authorizations.get` `gsuiteaddons.chatAppConfigs.get` `gsuiteaddons.deployments.get` `gsuiteaddons.deployments.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Workspace Add-ons Tester 

(`roles/gsuiteaddons.tester`) Testing execution access to Google Workspace Add-ons resources  |  `gsuiteaddons.deployments.execute` `gsuiteaddons.deployments.install` `gsuiteaddons.deployments.installStatus` `gsuiteaddons.deployments.uninstall` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Google Workspace add-ons permissions

Permission | Included in roles  
---|---  
  
#### `gsuiteaddons.authorizations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.viewer) (`roles/gsuiteaddons.viewer`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.reader) (`roles/gsuiteaddons.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gsuiteaddons.chatAppConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.viewer) (`roles/gsuiteaddons.viewer`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.reader) (`roles/gsuiteaddons.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gsuiteaddons.chatAppConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)   
  
#### `gsuiteaddons.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Workspace Marketplace App Configuration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workspacemarketplace#appmetadata.workspaceMarketplaceAppConfigurationAdmin) (`roles/appmetadata.workspaceMarketplaceAppConfigurationAdmin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)   
  
#### `gsuiteaddons.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Workspace Marketplace App Configuration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workspacemarketplace#appmetadata.workspaceMarketplaceAppConfigurationAdmin) (`roles/appmetadata.workspaceMarketplaceAppConfigurationAdmin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)   
  
#### `gsuiteaddons.deployments.execute`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.tester) (`roles/gsuiteaddons.tester`)   
  
#### `gsuiteaddons.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.viewer) (`roles/gsuiteaddons.viewer`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.reader) (`roles/gsuiteaddons.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gsuiteaddons.deployments.install`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.tester) (`roles/gsuiteaddons.tester`)   
  
#### `gsuiteaddons.deployments.installStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.tester) (`roles/gsuiteaddons.tester`)   
  
#### `gsuiteaddons.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.viewer) (`roles/gsuiteaddons.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Workspace Marketplace App Configuration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workspacemarketplace#appmetadata.workspaceMarketplaceAppConfigurationAdmin) (`roles/appmetadata.workspaceMarketplaceAppConfigurationAdmin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.reader) (`roles/gsuiteaddons.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gsuiteaddons.deployments.uninstall`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Tester](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.tester) (`roles/gsuiteaddons.tester`)   
  
#### `gsuiteaddons.deployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Workspace Marketplace App Configuration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workspacemarketplace#appmetadata.workspaceMarketplaceAppConfigurationAdmin) (`roles/appmetadata.workspaceMarketplaceAppConfigurationAdmin`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
