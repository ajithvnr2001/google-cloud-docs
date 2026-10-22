---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs/
title: Dell EMC Cloud OneFS roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:41.217564+00:00
---

# Dell EMC Cloud OneFS roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Dell EMC Cloud OneFS roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Dell EMC Cloud OneFS. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Dell EMC Cloud OneFS roles

Role | Permissions  
---|---  
  
#### Dell EMC Cloud OneFS Admin Beta

(`roles/dellemccloudonefs.admin`) This role is managed by Dell EMC, not Google.  |  `cloudonefs.isiloncloud.com/*`

  * `cloudonefs.isiloncloud.com/clusters.create`
  * `cloudonefs.isiloncloud.com/clusters.delete`
  * `cloudonefs.isiloncloud.com/clusters.get`
  * `cloudonefs.isiloncloud.com/clusters.list`
  * `cloudonefs.isiloncloud.com/clusters.update`
  * `cloudonefs.isiloncloud.com/clusters.updateAdvancedSettings`
  * `cloudonefs.isiloncloud.com/fileshares.create`
  * `cloudonefs.isiloncloud.com/fileshares.delete`
  * `cloudonefs.isiloncloud.com/fileshares.get`
  * `cloudonefs.isiloncloud.com/fileshares.list`
  * `cloudonefs.isiloncloud.com/fileshares.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dell EMC Cloud OneFS Viewer Beta

(`roles/dellemccloudonefs.viewer`) This role is managed by Dell EMC, not Google.  |  `cloudonefs.isiloncloud.com/clusters.get` `cloudonefs.isiloncloud.com/clusters.list` `cloudonefs.isiloncloud.com/fileshares.get` `cloudonefs.isiloncloud.com/fileshares.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dell EMC Cloud OneFS User Beta

(`roles/dellemccloudonefs.user`) This role is managed by Dell EMC, not Google.  |  `cloudonefs.isiloncloud.com/clusters.create` `cloudonefs.isiloncloud.com/clusters.delete` `cloudonefs.isiloncloud.com/clusters.get` `cloudonefs.isiloncloud.com/clusters.list` `cloudonefs.isiloncloud.com/clusters.update` `cloudonefs.isiloncloud.com/fileshares.*`

  * `cloudonefs.isiloncloud.com/fileshares.create`
  * `cloudonefs.isiloncloud.com/fileshares.delete`
  * `cloudonefs.isiloncloud.com/fileshares.get`
  * `cloudonefs.isiloncloud.com/fileshares.list`
  * `cloudonefs.isiloncloud.com/fileshares.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Dell EMC Cloud OneFS permissions

Permission | Included in roles  
---|---  
  
#### `cloudonefs.isiloncloud.com/clusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
#### `cloudonefs.isiloncloud.com/clusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
#### `cloudonefs.isiloncloud.com/clusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.viewer) (`roles/dellemccloudonefs.viewer`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudonefs.isiloncloud.com/clusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.viewer) (`roles/dellemccloudonefs.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudonefs.isiloncloud.com/clusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
#### `cloudonefs.isiloncloud.com/clusters.updateAdvancedSettings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)   
  
#### `cloudonefs.isiloncloud.com/fileshares.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
#### `cloudonefs.isiloncloud.com/fileshares.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
#### `cloudonefs.isiloncloud.com/fileshares.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.viewer) (`roles/dellemccloudonefs.viewer`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudonefs.isiloncloud.com/fileshares.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.viewer) (`roles/dellemccloudonefs.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudonefs.isiloncloud.com/fileshares.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dell EMC Cloud OneFS Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.admin) (`roles/dellemccloudonefs.admin`)  [Dell EMC Cloud OneFS User](https://docs.cloud.google.com/iam/docs/roles-permissions/dellemccloudonefs#dellemccloudonefs.user) (`roles/dellemccloudonefs.user`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
