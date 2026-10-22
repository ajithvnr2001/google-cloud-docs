---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager/
title: Secret Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:14.868218+00:00
---

# Secret Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Secret Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Secret Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Secret Manager roles

Role | Permissions  
---|---  
  
#### Secret Manager Admin 

(`roles/secretmanager.admin`) Full access to administer Secret Manager resources.  Lowest-level resources where you can grant this role:

  * Secret 

|  `cloudkms.keyHandles.*`

  * `cloudkms.keyHandles.create`
  * `cloudkms.keyHandles.get`
  * `cloudkms.keyHandles.list`

`cloudkms.operations.get` `cloudkms.projects.showEffectiveAutokeyConfig` `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.*`

  * `secretmanager.locations.get`
  * `secretmanager.locations.list`
  * `secretmanager.secrets.create`
  * `secretmanager.secrets.createTagBinding`
  * `secretmanager.secrets.delete`
  * `secretmanager.secrets.deleteTagBinding`
  * `secretmanager.secrets.enableManagedRotation`
  * `secretmanager.secrets.get`
  * `secretmanager.secrets.getIamPolicy`
  * `secretmanager.secrets.list`
  * `secretmanager.secrets.listEffectiveTags`
  * `secretmanager.secrets.listTagBindings`
  * `secretmanager.secrets.rotate`
  * `secretmanager.secrets.setIamPolicy`
  * `secretmanager.secrets.update`
  * `secretmanager.versions.access`
  * `secretmanager.versions.add`
  * `secretmanager.versions.destroy`
  * `secretmanager.versions.disable`
  * `secretmanager.versions.enable`
  * `secretmanager.versions.get`
  * `secretmanager.versions.list`

  
  
#### Secret Manager Editor 

(`roles/secretmanager.editor`) Editor role for Secret Manager  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.locations.*`

  * `secretmanager.locations.get`
  * `secretmanager.locations.list`

`secretmanager.secrets.create` `secretmanager.secrets.delete` `secretmanager.secrets.enableManagedRotation` `secretmanager.secrets.get` `secretmanager.secrets.getIamPolicy` `secretmanager.secrets.list` `secretmanager.secrets.listEffectiveTags` `secretmanager.secrets.listTagBindings` `secretmanager.secrets.rotate` `secretmanager.secrets.update` `secretmanager.versions.add` `secretmanager.versions.destroy` `secretmanager.versions.disable` `secretmanager.versions.enable` `secretmanager.versions.get` `secretmanager.versions.list`  
  
#### Secret Manager Secret Accessor 

(`roles/secretmanager.secretAccessor`) Allows accessing the payload of secrets.  Lowest-level resources where you can grant this role:

  * Secret 

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.versions.access`  
  
#### Secret Manager Viewer 

(`roles/secretmanager.viewer`) Allows viewing metadata of all Secret Manager resources  Lowest-level resources where you can grant this role:

  * Secret 

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.locations.*`

  * `secretmanager.locations.get`
  * `secretmanager.locations.list`

`secretmanager.secrets.get` `secretmanager.secrets.getIamPolicy` `secretmanager.secrets.list` `secretmanager.secrets.listEffectiveTags` `secretmanager.secrets.listTagBindings` `secretmanager.versions.get` `secretmanager.versions.list`  
  
#### Secret Manager Secret Version Adder 

(`roles/secretmanager.secretVersionAdder`) Allows adding versions to existing secrets.  Lowest-level resources where you can grant this role:

  * Secret 

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.secrets.rotate` `secretmanager.versions.add`  
  
#### Secret Manager Secret Version Manager 

(`roles/secretmanager.secretVersionManager`) Allows creating and managing versions of existing secrets.  Lowest-level resources where you can grant this role:

  * Secret 

|  `resourcemanager.projects.get` `resourcemanager.projects.list` `secretmanager.secrets.rotate` `secretmanager.versions.add` `secretmanager.versions.destroy` `secretmanager.versions.disable` `secretmanager.versions.enable` `secretmanager.versions.get` `secretmanager.versions.list`  
  
## Secret Manager permissions

Permission | Included in roles  
---|---  
  
#### `secretmanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `secretmanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `secretmanager.secrets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)   
  
#### `secretmanager.secrets.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `secretmanager.secrets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)   
  
#### `secretmanager.secrets.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `secretmanager.secrets.enableManagedRotation`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)   
  
#### `secretmanager.secrets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `secretmanager.secrets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Connector Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/connectors#connectors.admin) (`roles/connectors.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `secretmanager.secrets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Audit Manager Auditing Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.serviceAgent) (`roles/auditmanager.serviceAgent`) 

  
  
#### `secretmanager.secrets.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `secretmanager.secrets.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `secretmanager.secrets.rotate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Secret Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionAdder) (`roles/secretmanager.secretVersionAdder`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.secrets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)   
  
#### `secretmanager.secrets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)   
  
#### `secretmanager.versions.access`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`)   
  
#### `secretmanager.versions.add`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Secret Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionAdder) (`roles/secretmanager.secretVersionAdder`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.versions.destroy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.versions.disable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.versions.enable`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)   
  
#### `secretmanager.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Secret Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.admin) (`roles/secretmanager.admin`)  [Secret Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.editor) (`roles/secretmanager.editor`)  [Secret Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Secret Manager Secret Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
