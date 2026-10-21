---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/chat/
title: Hangouts Chat roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:58:30.547455+00:00
---

# Hangouts Chat roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Hangouts Chat roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Hangouts Chat. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Hangouts Chat roles

Role | Permissions  
---|---  
  
#### Chat Admin 

(`roles/chat.admin`) Admin role for chat  |  `chat.*`

  * `chat.bots.get`
  * `chat.bots.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chat Viewer 

(`roles/chat.viewer`) Viewer role for chat  |  `chat.bots.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Chat Apps Owner 

(`roles/chat.owner`) Can view and modify app configurations  |  `chat.*`

  * `chat.bots.get`
  * `chat.bots.update`

  
  
#### Chat Apps Viewer 

(`roles/chat.reader`) Can view app configurations  |  `chat.bots.get`  
  
## Hangouts Chat permissions

Permission | Included in roles  
---|---  
  
#### `chat.bots.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Chat Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.admin) (`roles/chat.admin`)  [Chat Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.viewer) (`roles/chat.viewer`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Google Workspace Add-ons Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.viewer) (`roles/gsuiteaddons.viewer`)  [Workspace Marketplace App Configuration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/workspacemarketplace#appmetadata.workspaceMarketplaceAppConfigurationAdmin) (`roles/appmetadata.workspaceMarketplaceAppConfigurationAdmin`)  [Chat Apps Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.owner) (`roles/chat.owner`)  [Chat Apps Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.reader) (`roles/chat.reader`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)  [Google Workspace Add-ons Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.reader) (`roles/gsuiteaddons.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `chat.bots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Chat Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.admin) (`roles/chat.admin`)  [Google Workspace Add-ons Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.admin) (`roles/gsuiteaddons.admin`)  [Chat Apps Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/chat#chat.owner) (`roles/chat.owner`)  [Google Workspace Add-ons Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/gsuiteaddons#gsuiteaddons.developer) (`roles/gsuiteaddons.developer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
