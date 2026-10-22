---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming/
title: Device Streaming API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:30.488178+00:00
---

# Device Streaming API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Device Streaming API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Device Streaming API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Device Streaming API roles

Role | Permissions  
---|---  
  
#### Device Streaming Admin 

(`roles/devicestreaming.admin`) Administrator owning access to Direct Access  |  `cloudtestservice.environmentcatalog.get` `devicestreaming.*`

  * `devicestreaming.deviceSessions.cancel`
  * `devicestreaming.deviceSessions.create`
  * `devicestreaming.deviceSessions.get`
  * `devicestreaming.deviceSessions.list`
  * `devicestreaming.deviceSessions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Device Streaming Viewer 

(`roles/devicestreaming.viewer`) Viewer, able to see what device streaming sessions exist  |  `cloudtestservice.environmentcatalog.get` `devicestreaming.deviceSessions.get` `devicestreaming.deviceSessions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Device Streaming API permissions

Permission | Included in roles  
---|---  
  
#### `devicestreaming.deviceSessions.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `devicestreaming.deviceSessions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `devicestreaming.deviceSessions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Run Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.viewer) (`roles/devicerun.viewer`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Device Streaming Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.viewer) (`roles/devicestreaming.viewer`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)  [Firebase Test Lab Direct Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessViewer) (`roles/cloudtestservice.directAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `devicestreaming.deviceSessions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Run Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.viewer) (`roles/devicerun.viewer`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Device Streaming Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.viewer) (`roles/devicestreaming.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)  [Firebase Test Lab Direct Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessViewer) (`roles/cloudtestservice.directAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `devicestreaming.deviceSessions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
