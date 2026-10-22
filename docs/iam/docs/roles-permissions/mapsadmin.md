---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin/
title: Maps Admin roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:20.047619+00:00
---

# Maps Admin roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Maps Admin roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Maps Admin. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Maps Admin roles

Role | Permissions  
---|---  
  
#### Maps API Admin 

(`roles/mapsadmin.admin`) Read and Write all Maps Management and Maps Styles Resources.  |  `mapsadmin.*`

  * `mapsadmin.clientMaps.create`
  * `mapsadmin.clientMaps.delete`
  * `mapsadmin.clientMaps.get`
  * `mapsadmin.clientMaps.list`
  * `mapsadmin.clientMaps.update`
  * `mapsadmin.clientStyleActivationRules.update`
  * `mapsadmin.clientStyleSheetSnapshots.list`
  * `mapsadmin.clientStyleSheetSnapshots.update`
  * `mapsadmin.clientStyles.create`
  * `mapsadmin.clientStyles.delete`
  * `mapsadmin.clientStyles.get`
  * `mapsadmin.clientStyles.list`
  * `mapsadmin.clientStyles.update`
  * `mapsadmin.mapViews.create`
  * `mapsadmin.mapViews.delete`
  * `mapsadmin.mapViews.get`
  * `mapsadmin.mapViews.list`
  * `mapsadmin.mapViews.update`
  * `mapsadmin.styleEditorConfigs.get`
  * `mapsadmin.styleSnapshots.list`
  * `mapsadmin.styleSnapshots.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Maps API Viewer 

(`roles/mapsadmin.viewer`) Read all Maps Management and Maps Styles Resources.  |  `mapsadmin.clientMaps.get` `mapsadmin.clientMaps.list` `mapsadmin.clientStyleSheetSnapshots.list` `mapsadmin.clientStyles.get` `mapsadmin.clientStyles.list` `mapsadmin.mapViews.get` `mapsadmin.mapViews.list` `mapsadmin.styleEditorConfigs.get` `mapsadmin.styleSnapshots.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Maps Admin permissions

Permission | Included in roles  
---|---  
  
#### `mapsadmin.clientMaps.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.clientMaps.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.clientMaps.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.clientMaps.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.clientMaps.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.clientStyleActivationRules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.clientStyleSheetSnapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.clientStyleSheetSnapshots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.clientStyles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps Platform Datasets Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.admin) (`roles/mapsplatformdatasets.admin`)   
  
#### `mapsadmin.clientStyles.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps Platform Datasets Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.admin) (`roles/mapsplatformdatasets.admin`)   
  
#### `mapsadmin.clientStyles.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Maps Platform Datasets Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.admin) (`roles/mapsplatformdatasets.admin`)  [Maps Platform Datasets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.viewer) (`roles/mapsplatformdatasets.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.clientStyles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Maps Platform Datasets Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.admin) (`roles/mapsplatformdatasets.admin`)  [Maps Platform Datasets Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.viewer) (`roles/mapsplatformdatasets.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.clientStyles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps Platform Datasets Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsplatformdatasets#mapsplatformdatasets.admin) (`roles/mapsplatformdatasets.admin`)   
  
#### `mapsadmin.mapViews.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.mapViews.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.mapViews.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.mapViews.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.mapViews.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
#### `mapsadmin.styleEditorConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.styleSnapshots.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)  [Maps API Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.viewer) (`roles/mapsadmin.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `mapsadmin.styleSnapshots.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Maps API Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/mapsadmin#mapsadmin.admin) (`roles/mapsadmin.admin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
