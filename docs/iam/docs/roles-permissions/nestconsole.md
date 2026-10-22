---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole/
title: Nest Console roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:06.949979+00:00
---

# Nest Console roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Nest Console roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Nest Console. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Nest Console roles

Role | Permissions  
---|---  
  
#### Nestconsole Admin 

(`roles/nestconsole.admin`) Admin role for nestconsole  |  `nestconsole.*`

  * `nestconsole.smarthomePreviews.update`
  * `nestconsole.smarthomeProjects.create`
  * `nestconsole.smarthomeProjects.delete`
  * `nestconsole.smarthomeProjects.get`
  * `nestconsole.smarthomeProjects.update`
  * `nestconsole.smarthomeVersions.create`
  * `nestconsole.smarthomeVersions.get`
  * `nestconsole.smarthomeVersions.submit`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Nestconsole Editor 

(`roles/nestconsole.editor`) Editor role for nestconsole  |  `nestconsole.smarthomePreviews.update` `nestconsole.smarthomeProjects.get` `nestconsole.smarthomeProjects.update` `nestconsole.smarthomeVersions.*`

  * `nestconsole.smarthomeVersions.create`
  * `nestconsole.smarthomeVersions.get`
  * `nestconsole.smarthomeVersions.submit`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Nestconsole Viewer 

(`roles/nestconsole.viewer`) Viewer role for nestconsole  |  `nestconsole.smarthomeProjects.get` `nestconsole.smarthomeVersions.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Home Developer Console Admin 

(`roles/nestconsole.homeDeveloperAdmin`) Admin access to Google Home Developer Console resources  |  `nestconsole.*`

  * `nestconsole.smarthomePreviews.update`
  * `nestconsole.smarthomeProjects.create`
  * `nestconsole.smarthomeProjects.delete`
  * `nestconsole.smarthomeProjects.get`
  * `nestconsole.smarthomeProjects.update`
  * `nestconsole.smarthomeVersions.create`
  * `nestconsole.smarthomeVersions.get`
  * `nestconsole.smarthomeVersions.submit`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Home Developer Console Editor 

(`roles/nestconsole.homeDeveloperEditor`) Read-Write access to Google Home Developer Console resources  |  `nestconsole.smarthomePreviews.update` `nestconsole.smarthomeProjects.get` `nestconsole.smarthomeProjects.update` `nestconsole.smarthomeVersions.*`

  * `nestconsole.smarthomeVersions.create`
  * `nestconsole.smarthomeVersions.get`
  * `nestconsole.smarthomeVersions.submit`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Google Home Developer Console Reader 

(`roles/nestconsole.homeDeveloperViewer`) Read-only access to Google Home Developer Console resources  |  `nestconsole.smarthomeProjects.get` `nestconsole.smarthomeVersions.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Nest Console permissions

Permission | Included in roles  
---|---  
  
#### `nestconsole.smarthomePreviews.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)   
  
#### `nestconsole.smarthomeProjects.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)   
  
#### `nestconsole.smarthomeProjects.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)   
  
#### `nestconsole.smarthomeProjects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Nestconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.viewer) (`roles/nestconsole.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)  [Google Home Developer Console Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperViewer) (`roles/nestconsole.homeDeveloperViewer`)   
  
#### `nestconsole.smarthomeProjects.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)   
  
#### `nestconsole.smarthomeVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)   
  
#### `nestconsole.smarthomeVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Nestconsole Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.viewer) (`roles/nestconsole.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)  [Google Home Developer Console Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperViewer) (`roles/nestconsole.homeDeveloperViewer`)   
  
#### `nestconsole.smarthomeVersions.submit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Nestconsole Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.admin) (`roles/nestconsole.admin`)  [Nestconsole Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.editor) (`roles/nestconsole.editor`)  [Google Home Developer Console Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperAdmin) (`roles/nestconsole.homeDeveloperAdmin`)  [Google Home Developer Console Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/nestconsole#nestconsole.homeDeveloperEditor) (`roles/nestconsole.homeDeveloperEditor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
