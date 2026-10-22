---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder/
title: Cloud Location Finder roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:00.874278+00:00
---

# Cloud Location Finder roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Location Finder roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Location Finder. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Location Finder roles

Role | Permissions  
---|---  
  
#### Cloud Location Finder Admin Beta

(`roles/cloudlocationfinder.admin`) Full access to Cloud Location Finder resources.  |  `cloudlocationfinder.*`

  * `cloudlocationfinder.cloudLocations.create`
  * `cloudlocationfinder.cloudLocations.delete`
  * `cloudlocationfinder.cloudLocations.get`
  * `cloudlocationfinder.cloudLocations.list`
  * `cloudlocationfinder.cloudLocations.search`
  * `cloudlocationfinder.cloudLocations.update`
  * `cloudlocationfinder.locations.get`
  * `cloudlocationfinder.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Location Finder Viewer Beta

(`roles/cloudlocationfinder.viewer`) Readonly access to Cloud Location Finder resources.  |  `cloudlocationfinder.cloudLocations.get` `cloudlocationfinder.cloudLocations.list` `cloudlocationfinder.cloudLocations.search` `cloudlocationfinder.locations.*`

  * `cloudlocationfinder.locations.get`
  * `cloudlocationfinder.locations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Cloud Location Finder permissions

Permission | Included in roles  
---|---  
  
#### `cloudlocationfinder.cloudLocations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)   
  
#### `cloudlocationfinder.cloudLocations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)   
  
#### `cloudlocationfinder.cloudLocations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)  [Cloud Location Finder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.viewer) (`roles/cloudlocationfinder.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudlocationfinder.cloudLocations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)  [Cloud Location Finder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.viewer) (`roles/cloudlocationfinder.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudlocationfinder.cloudLocations.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)  [Cloud Location Finder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.viewer) (`roles/cloudlocationfinder.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudlocationfinder.cloudLocations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)   
  
#### `cloudlocationfinder.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)  [Cloud Location Finder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.viewer) (`roles/cloudlocationfinder.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudlocationfinder.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Location Finder Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.admin) (`roles/cloudlocationfinder.admin`)  [Cloud Location Finder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudlocationfinder#cloudlocationfinder.viewer) (`roles/cloudlocationfinder.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
