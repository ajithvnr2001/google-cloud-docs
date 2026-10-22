---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager/
title: Privileged Access Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:55.211001+00:00
---

# Privileged Access Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Privileged Access Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Privileged Access Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Privileged Access Manager roles

Role | Permissions  
---|---  
  
#### Privileged Access Manager Admin 

(`roles/privilegedaccessmanager.admin`) Full access to Privileged Access Manager resources.  |  `privilegedaccessmanager.entitlements.*`

  * `privilegedaccessmanager.entitlements.create`
  * `privilegedaccessmanager.entitlements.delete`
  * `privilegedaccessmanager.entitlements.get`
  * `privilegedaccessmanager.entitlements.list`
  * `privilegedaccessmanager.entitlements.setIamPolicy`
  * `privilegedaccessmanager.entitlements.update`

`privilegedaccessmanager.grants.*`

  * `privilegedaccessmanager.grants.get`
  * `privilegedaccessmanager.grants.list`
  * `privilegedaccessmanager.grants.revoke`

`privilegedaccessmanager.locations.*`

  * `privilegedaccessmanager.locations.checkOnboardingStatus`
  * `privilegedaccessmanager.locations.get`
  * `privilegedaccessmanager.locations.list`

`privilegedaccessmanager.operations.*`

  * `privilegedaccessmanager.operations.delete`
  * `privilegedaccessmanager.operations.get`
  * `privilegedaccessmanager.operations.list`

`privilegedaccessmanager.settings.fetchEffective` `privilegedaccessmanager.settings.get` `resourcemanager.projects.get`  
  
#### Privilegedaccessmanager Editor 

(`roles/privilegedaccessmanager.editor`) Editor role for privilegedaccessmanager  |  `privilegedaccessmanager.entitlements.get` `privilegedaccessmanager.entitlements.list` `privilegedaccessmanager.grants.get` `privilegedaccessmanager.grants.list` `privilegedaccessmanager.locations.get` `privilegedaccessmanager.locations.list` `privilegedaccessmanager.operations.get` `privilegedaccessmanager.operations.list` `privilegedaccessmanager.settings.fetchEffective` `privilegedaccessmanager.settings.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Privileged Access Manager Viewer 

(`roles/privilegedaccessmanager.viewer`) Readonly access to Privileged Access Manager resources.  |  `privilegedaccessmanager.entitlements.get` `privilegedaccessmanager.entitlements.list` `privilegedaccessmanager.grants.get` `privilegedaccessmanager.grants.list` `privilegedaccessmanager.locations.get` `privilegedaccessmanager.locations.list` `privilegedaccessmanager.operations.get` `privilegedaccessmanager.operations.list` `privilegedaccessmanager.settings.fetchEffective` `privilegedaccessmanager.settings.get` `resourcemanager.projects.get`  
  
#### Privileged Access Manager Settings Admin Beta

(`roles/privilegedaccessmanager.settingsAdmin`) Administrator of Privileged Access Manager Settings.  |  `privilegedaccessmanager.operations.get` `privilegedaccessmanager.settings.*`

  * `privilegedaccessmanager.settings.fetchEffective`
  * `privilegedaccessmanager.settings.get`
  * `privilegedaccessmanager.settings.update`

  
  
#### Privileged Access Manager Settings Viewer Beta

(`roles/privilegedaccessmanager.settingsViewer`) Readonly access to Privileged Access Manager Settings & Effective Settings.  |  `privilegedaccessmanager.settings.fetchEffective` `privilegedaccessmanager.settings.get`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Privileged Access Manager Folder Service Agent 

(`roles/privilegedaccessmanager.folderServiceAgent`) Gives privileged access manager service account access to modify IAM policies on GCP folders  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.setIamPolicy`  
  
#### Privileged Access Manager Organization Service Agent 

(`roles/privilegedaccessmanager.organizationServiceAgent`) Gives privileged access manager service account access to modify IAM policies on GCP organizations  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.roles.get` `resourcemanager.organizations.get` `resourcemanager.organizations.getIamPolicy` `resourcemanager.organizations.setIamPolicy`  
  
#### Privileged Access Manager Project Service Agent 

(`roles/privilegedaccessmanager.projectServiceAgent`) Gives privileged access manager service account access to modify IAM policies on GCP projects  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.roles.get` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.setIamPolicy`  
  
#### Privileged Access Manager Service Agent 

(`roles/privilegedaccessmanager.serviceAgent`) Gives privileged access manager service account access to modify IAM policies on GCP resources  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.roles.get` `resourcemanager.folders.get` `resourcemanager.folders.getIamPolicy` `resourcemanager.folders.setIamPolicy` `resourcemanager.organizations.get` `resourcemanager.organizations.getIamPolicy` `resourcemanager.organizations.setIamPolicy` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy` `resourcemanager.projects.setIamPolicy`  
  
## Privileged Access Manager permissions

Permission | Included in roles  
---|---  
  
#### `privilegedaccessmanager.entitlements.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.entitlements.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.entitlements.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.entitlements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.entitlements.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.entitlements.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.grants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.grants.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.grants.revoke`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.locations.checkOnboardingStatus`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)   
  
#### `privilegedaccessmanager.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Privileged Access Manager Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsAdmin) (`roles/privilegedaccessmanager.settingsAdmin`)   
  
#### `privilegedaccessmanager.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `privilegedaccessmanager.settings.fetchEffective`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Privileged Access Manager Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsAdmin) (`roles/privilegedaccessmanager.settingsAdmin`)  [Privileged Access Manager Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsViewer) (`roles/privilegedaccessmanager.settingsViewer`)   
  
#### `privilegedaccessmanager.settings.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Privileged Access Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)  [Privilegedaccessmanager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.editor) (`roles/privilegedaccessmanager.editor`)  [Privileged Access Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.viewer) (`roles/privilegedaccessmanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Privileged Access Manager Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsAdmin) (`roles/privilegedaccessmanager.settingsAdmin`)  [Privileged Access Manager Settings Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsViewer) (`roles/privilegedaccessmanager.settingsViewer`)   
  
#### `privilegedaccessmanager.settings.update`

|  [Privileged Access Manager Settings Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.settingsAdmin) (`roles/privilegedaccessmanager.settingsAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
