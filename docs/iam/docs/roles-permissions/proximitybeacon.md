---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon/
title: Proximity Beacon roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:34.054005+00:00
---

# Proximity Beacon roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Proximity Beacon roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Proximity Beacon. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Proximity Beacon roles

Role | Permissions  
---|---  
  
#### Beacon Admin 

(`roles/proximitybeacon.admin`) Admin role for Proximity Beacon  |  `proximitybeacon.*`

  * `proximitybeacon.attachments.create`
  * `proximitybeacon.attachments.delete`
  * `proximitybeacon.attachments.get`
  * `proximitybeacon.attachments.list`
  * `proximitybeacon.beacons.attach`
  * `proximitybeacon.beacons.create`
  * `proximitybeacon.beacons.get`
  * `proximitybeacon.beacons.getIamPolicy`
  * `proximitybeacon.beacons.list`
  * `proximitybeacon.beacons.setIamPolicy`
  * `proximitybeacon.beacons.update`
  * `proximitybeacon.namespaces.create`
  * `proximitybeacon.namespaces.delete`
  * `proximitybeacon.namespaces.get`
  * `proximitybeacon.namespaces.getIamPolicy`
  * `proximitybeacon.namespaces.list`
  * `proximitybeacon.namespaces.setIamPolicy`
  * `proximitybeacon.namespaces.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Editor 

(`roles/proximitybeacon.editor`) Editor role for Proximity Beacon  |  `proximitybeacon.attachments.*`

  * `proximitybeacon.attachments.create`
  * `proximitybeacon.attachments.delete`
  * `proximitybeacon.attachments.get`
  * `proximitybeacon.attachments.list`

`proximitybeacon.beacons.attach` `proximitybeacon.beacons.create` `proximitybeacon.beacons.get` `proximitybeacon.beacons.list` `proximitybeacon.beacons.update` `proximitybeacon.namespaces.create` `proximitybeacon.namespaces.delete` `proximitybeacon.namespaces.get` `proximitybeacon.namespaces.list` `proximitybeacon.namespaces.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Viewer 

(`roles/proximitybeacon.viewer`) Viewer role for Proximity Beacon  |  `proximitybeacon.attachments.get` `proximitybeacon.attachments.list` `proximitybeacon.beacons.get` `proximitybeacon.beacons.list` `proximitybeacon.namespaces.get` `proximitybeacon.namespaces.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Attachment Editor 

(`roles/proximitybeacon.attachmentEditor`) Can create and delete attachments; can list and get a project's beacons; can list a project's namespaces.  |  `proximitybeacon.attachments.*`

  * `proximitybeacon.attachments.create`
  * `proximitybeacon.attachments.delete`
  * `proximitybeacon.attachments.get`
  * `proximitybeacon.attachments.list`

`proximitybeacon.beacons.get` `proximitybeacon.beacons.list` `proximitybeacon.namespaces.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Attachment Publisher 

(`roles/proximitybeacon.attachmentPublisher`) Grants necessary permissions to use beacons to create attachments in namespaces not owned by this project.  |  `proximitybeacon.beacons.attach` `proximitybeacon.beacons.get` `proximitybeacon.beacons.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Attachment Viewer 

(`roles/proximitybeacon.attachmentViewer`) Can view all attachments under a namespace; no beacon or namespace permissions.  |  `proximitybeacon.attachments.get` `proximitybeacon.attachments.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Beacon Editor 

(`roles/proximitybeacon.beaconEditor`) Necessary access to register, modify, and view beacons; no attachment or namespace permissions.  |  `proximitybeacon.beacons.create` `proximitybeacon.beacons.get` `proximitybeacon.beacons.list` `proximitybeacon.beacons.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Proximity Beacon permissions

Permission | Included in roles  
---|---  
  
#### `proximitybeacon.attachments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)   
  
#### `proximitybeacon.attachments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)   
  
#### `proximitybeacon.attachments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)  [Beacon Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentViewer) (`roles/proximitybeacon.attachmentViewer`)   
  
#### `proximitybeacon.attachments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)  [Beacon Attachment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentViewer) (`roles/proximitybeacon.attachmentViewer`)   
  
#### `proximitybeacon.beacons.attach`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Attachment Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentPublisher) (`roles/proximitybeacon.attachmentPublisher`)   
  
#### `proximitybeacon.beacons.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.beaconEditor) (`roles/proximitybeacon.beaconEditor`)   
  
#### `proximitybeacon.beacons.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)  [Beacon Attachment Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentPublisher) (`roles/proximitybeacon.attachmentPublisher`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.beaconEditor) (`roles/proximitybeacon.beaconEditor`)   
  
#### `proximitybeacon.beacons.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `proximitybeacon.beacons.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)  [Beacon Attachment Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentPublisher) (`roles/proximitybeacon.attachmentPublisher`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.beaconEditor) (`roles/proximitybeacon.beaconEditor`)   
  
#### `proximitybeacon.beacons.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)   
  
#### `proximitybeacon.beacons.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.beaconEditor) (`roles/proximitybeacon.beaconEditor`)   
  
#### `proximitybeacon.namespaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)   
  
#### `proximitybeacon.namespaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)   
  
#### `proximitybeacon.namespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `proximitybeacon.namespaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `proximitybeacon.namespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)  [Beacon Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.viewer) (`roles/proximitybeacon.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Beacon Attachment Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.attachmentEditor) (`roles/proximitybeacon.attachmentEditor`)   
  
#### `proximitybeacon.namespaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)   
  
#### `proximitybeacon.namespaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Beacon Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.admin) (`roles/proximitybeacon.admin`)  [Beacon Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/proximitybeacon#proximitybeacon.editor) (`roles/proximitybeacon.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
