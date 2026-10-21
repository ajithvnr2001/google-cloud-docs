---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager/
title: Parameter Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:13:56.131311+00:00
---

# Parameter Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Parameter Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Parameter Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Parameter Manager roles

Role | Permissions  
---|---  
  
#### Parameter Manager Admin 

(`roles/parametermanager.admin`) Grants full access to all Parameter Manager resources. Intended for project admins & owners who need to perform all administrative tasks.  |  `parametermanager.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`
  * `parametermanager.parameterVersions.create`
  * `parametermanager.parameterVersions.delete`
  * `parametermanager.parameterVersions.get`
  * `parametermanager.parameterVersions.list`
  * `parametermanager.parameterVersions.render`
  * `parametermanager.parameterVersions.update`
  * `parametermanager.parameters.create`
  * `parametermanager.parameters.createTagBinding`
  * `parametermanager.parameters.delete`
  * `parametermanager.parameters.deleteTagBinding`
  * `parametermanager.parameters.get`
  * `parametermanager.parameters.list`
  * `parametermanager.parameters.listEffectiveTags`
  * `parametermanager.parameters.listTagBindings`
  * `parametermanager.parameters.update`
  * `parametermanager.templateVersions.create`
  * `parametermanager.templateVersions.delete`
  * `parametermanager.templateVersions.get`
  * `parametermanager.templateVersions.list`
  * `parametermanager.templateVersions.render`
  * `parametermanager.templateVersions.update`
  * `parametermanager.templates.create`
  * `parametermanager.templates.delete`
  * `parametermanager.templates.get`
  * `parametermanager.templates.list`
  * `parametermanager.templates.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Editor 

(`roles/parametermanager.editor`) Editor role for Parameter Manager  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.create` `parametermanager.parameterVersions.delete` `parametermanager.parameterVersions.get` `parametermanager.parameterVersions.list` `parametermanager.parameterVersions.update` `parametermanager.parameters.create` `parametermanager.parameters.delete` `parametermanager.parameters.get` `parametermanager.parameters.list` `parametermanager.parameters.listEffectiveTags` `parametermanager.parameters.listTagBindings` `parametermanager.parameters.update` `parametermanager.templateVersions.create` `parametermanager.templateVersions.delete` `parametermanager.templateVersions.get` `parametermanager.templateVersions.list` `parametermanager.templateVersions.update` `parametermanager.templates.*`

  * `parametermanager.templates.create`
  * `parametermanager.templates.delete`
  * `parametermanager.templates.get`
  * `parametermanager.templates.list`
  * `parametermanager.templates.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Viewer 

(`roles/parametermanager.viewer`) Viewer role for Parameter Manager  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.get` `parametermanager.parameterVersions.list` `parametermanager.parameters.get` `parametermanager.parameters.list` `parametermanager.parameters.listEffectiveTags` `parametermanager.parameters.listTagBindings` `parametermanager.templateVersions.get` `parametermanager.templateVersions.list` `parametermanager.templates.get` `parametermanager.templates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Parameter Accessor 

(`roles/parametermanager.parameterAccessor`) Grants read access to ParameterManager ParameterVersion resources. Intended for users & applications that need to perform read operations on ParameterVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.render` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Parameter Version Adder 

(`roles/parametermanager.parameterVersionAdder`) Grants create access to Parameter Manager ParameterVersion resources. Intended for users & applications that need to perform create operations on ParameterVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.create` `parametermanager.parameters.get` `parametermanager.parameters.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Parameter Version Manager 

(`roles/parametermanager.parameterVersionManager`) Grants read & write access to all Parameter Manager ParameterVersion resources. Intended for users & applications that need to view Parameters and perform create/read/update/delete/list operations on ParameterVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.create` `parametermanager.parameterVersions.delete` `parametermanager.parameterVersions.get` `parametermanager.parameterVersions.list` `parametermanager.parameterVersions.update` `parametermanager.parameters.get` `parametermanager.parameters.list` `parametermanager.parameters.listEffectiveTags` `parametermanager.parameters.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Parameter Viewer 

(`roles/parametermanager.parameterViewer`) Grants read access to Parameter Manager Parameter & ParameterVersion resources. Intended for users & applications that need to perform read/list operations on Parameters and ParameterVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.parameterVersions.get` `parametermanager.parameterVersions.list` `parametermanager.parameters.get` `parametermanager.parameters.list` `parametermanager.parameters.listEffectiveTags` `parametermanager.parameters.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Template Accessor Beta

(`roles/parametermanager.templateAccessor`) Grants read access to ParameterManager TemplateVersion resources. Intended for users & applications that need to perform read operations on TemplateVersions only.  |  `parametermanager.templateVersions.render`  
  
#### Parameter Manager Template Version Manager Beta

(`roles/parametermanager.templateVersionManager`) Grants read & write access to all Parameter Manager TemplateVersion resources. Intended for users & applications that need to view Templates and perform create/read/update/delete/list operations on TemplateVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.templateVersions.create` `parametermanager.templateVersions.delete` `parametermanager.templateVersions.get` `parametermanager.templateVersions.list` `parametermanager.templateVersions.update` `parametermanager.templates.get` `parametermanager.templates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Parameter Manager Template Viewer Beta

(`roles/parametermanager.templateViewer`) Grants read access to Parameter Manager Template & TemplateVersion resources. Intended for users & applications that need to perform read/list operations on Templates and TemplateVersions only.  |  `parametermanager.locations.*`

  * `parametermanager.locations.get`
  * `parametermanager.locations.list`

`parametermanager.templateVersions.get` `parametermanager.templateVersions.list` `parametermanager.templates.get` `parametermanager.templates.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Parameter Manager permissions

Permission | Included in roles  
---|---  
  
#### `parametermanager.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterAccessor) (`roles/parametermanager.parameterAccessor`)  [Parameter Manager Parameter Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterAccessor) (`roles/parametermanager.parameterAccessor`)  [Parameter Manager Parameter Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.parameterVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Parameter Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)   
  
#### `parametermanager.parameterVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)   
  
#### `parametermanager.parameterVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameterVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameterVersions.render`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Parameter Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterAccessor) (`roles/parametermanager.parameterAccessor`)   
  
#### `parametermanager.parameterVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)   
  
#### `parametermanager.parameters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
#### `parametermanager.parameters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `parametermanager.parameters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
#### `parametermanager.parameters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `parametermanager.parameters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Adder](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Parameter Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`)  [Parameter Manager Parameter Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`)   
  
#### `parametermanager.parameters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
#### `parametermanager.templateVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)   
  
#### `parametermanager.templateVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)   
  
#### `parametermanager.templateVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.templateVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.templateVersions.render`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Template Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateAccessor) (`roles/parametermanager.templateAccessor`)   
  
#### `parametermanager.templateVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)   
  
#### `parametermanager.templates.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
#### `parametermanager.templates.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
#### `parametermanager.templates.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.templates.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)  [Parameter Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.viewer) (`roles/parametermanager.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Parameter Manager Template Version Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`)  [Parameter Manager Template Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateViewer) (`roles/parametermanager.templateViewer`)   
  
#### `parametermanager.templates.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`)  [Parameter Manager Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.editor) (`roles/parametermanager.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
