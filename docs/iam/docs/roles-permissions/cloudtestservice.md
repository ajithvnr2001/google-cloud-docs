---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice/
title: Firebase Test Lab roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:44.922791+00:00
---

# Firebase Test Lab roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Firebase Test Lab roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Firebase Test Lab. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Firebase Test Lab roles

Role | Permissions  
---|---  
  
#### Cloud Test Service Admin 

(`roles/cloudtestservice.admin`) Admin role for cloudtestservice  |  `cloudtestservice.*`

  * `cloudtestservice.devicesession.cancel`
  * `cloudtestservice.devicesession.create`
  * `cloudtestservice.devicesession.get`
  * `cloudtestservice.devicesession.list`
  * `cloudtestservice.devicesession.update`
  * `cloudtestservice.devicesession.use`
  * `cloudtestservice.environmentcatalog.get`
  * `cloudtestservice.matrices.create`
  * `cloudtestservice.matrices.get`
  * `cloudtestservice.matrices.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Test Service Viewer 

(`roles/cloudtestservice.viewer`) Viewer role for cloudtestservice  |  `cloudtestservice.devicesession.get` `cloudtestservice.devicesession.list` `cloudtestservice.environmentcatalog.get` `cloudtestservice.matrices.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Test Lab Direct Access Admin Beta

(`roles/cloudtestservice.directAccessAdmin`) Administrator owning access to Direct Access  |  `cloudtestservice.devicesession.*`

  * `cloudtestservice.devicesession.cancel`
  * `cloudtestservice.devicesession.create`
  * `cloudtestservice.devicesession.get`
  * `cloudtestservice.devicesession.list`
  * `cloudtestservice.devicesession.update`
  * `cloudtestservice.devicesession.use`

`cloudtestservice.environmentcatalog.get` `devicestreaming.*`

  * `devicestreaming.deviceSessions.cancel`
  * `devicestreaming.deviceSessions.create`
  * `devicestreaming.deviceSessions.get`
  * `devicestreaming.deviceSessions.list`
  * `devicestreaming.deviceSessions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Test Lab Direct Access Viewer Beta

(`roles/cloudtestservice.directAccessViewer`) Viewer, able to see what direct access sessions exist  |  `cloudtestservice.devicesession.get` `cloudtestservice.devicesession.list` `cloudtestservice.environmentcatalog.get` `devicestreaming.deviceSessions.get` `devicestreaming.deviceSessions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Firebase Test Lab Admin 

(`roles/cloudtestservice.testAdmin`) Full access to all Test Lab features  |  `cloudtestservice.environmentcatalog.get` `cloudtestservice.matrices.*`

  * `cloudtestservice.matrices.create`
  * `cloudtestservice.matrices.get`
  * `cloudtestservice.matrices.update`

`cloudtoolresults.*`

  * `cloudtoolresults.executions.create`
  * `cloudtoolresults.executions.get`
  * `cloudtoolresults.executions.list`
  * `cloudtoolresults.executions.update`
  * `cloudtoolresults.histories.create`
  * `cloudtoolresults.histories.get`
  * `cloudtoolresults.histories.list`
  * `cloudtoolresults.settings.create`
  * `cloudtoolresults.settings.get`
  * `cloudtoolresults.settings.update`
  * `cloudtoolresults.steps.create`
  * `cloudtoolresults.steps.get`
  * `cloudtoolresults.steps.list`
  * `cloudtoolresults.steps.update`

`firebase.billingPlans.get` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.create` `storage.buckets.get` `storage.buckets.update` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Firebase Test Lab Viewer 

(`roles/cloudtestservice.testViewer`) Read access to Test Lab features  |  `cloudtestservice.environmentcatalog.get` `cloudtestservice.matrices.get` `cloudtoolresults.executions.get` `cloudtoolresults.executions.list` `cloudtoolresults.histories.get` `cloudtoolresults.histories.list` `cloudtoolresults.settings.get` `cloudtoolresults.steps.get` `cloudtoolresults.steps.list` `firebase.clients.get` `firebase.clients.list` `firebase.projects.get` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.objects.get` `storage.objects.list`  
  
## Firebase Test Lab permissions

Permission | Included in roles  
---|---  
  
#### `cloudtestservice.devicesession.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `cloudtestservice.devicesession.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `cloudtestservice.devicesession.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Cloud Test Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.viewer) (`roles/cloudtestservice.viewer`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)  [Firebase Test Lab Direct Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessViewer) (`roles/cloudtestservice.directAccessViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtestservice.devicesession.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Cloud Test Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.viewer) (`roles/cloudtestservice.viewer`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)  [Firebase Test Lab Direct Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessViewer) (`roles/cloudtestservice.directAccessViewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtestservice.devicesession.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `cloudtestservice.devicesession.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)   
  
#### `cloudtestservice.environmentcatalog.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Cloud Test Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.viewer) (`roles/cloudtestservice.viewer`)  [Device Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.admin) (`roles/devicerun.admin`)  [Device Run Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicerun#devicerun.viewer) (`roles/devicerun.viewer`)  [Device Streaming Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.admin) (`roles/devicestreaming.admin`)  [Device Streaming Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/devicestreaming#devicestreaming.viewer) (`roles/devicestreaming.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Test Lab Direct Access Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessAdmin) (`roles/cloudtestservice.directAccessAdmin`)  [Firebase Test Lab Direct Access Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.directAccessViewer) (`roles/cloudtestservice.directAccessViewer`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtestservice.matrices.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)   
  
#### `cloudtestservice.matrices.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Cloud Test Service Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.viewer) (`roles/cloudtestservice.viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.viewer) (`roles/firebase.viewer`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)  [Firebase Test Lab Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testViewer) (`roles/cloudtestservice.testViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudtestservice.matrices.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Test Service Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.admin) (`roles/cloudtestservice.admin`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Firebase Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.editor) (`roles/firebase.editor`)  [Firebase Test Lab Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtestservice#cloudtestservice.testAdmin) (`roles/cloudtestservice.testAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
