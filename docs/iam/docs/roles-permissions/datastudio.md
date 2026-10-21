---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio/
title: Data Studio roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:36:11.375883+00:00
---

# Data Studio roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Studio roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Studio. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Studio roles

Role | Permissions  
---|---  
  
#### Data Studio Admin Beta

(`roles/datastudio.admin`) Data Studio Admin  |  `datastudio.*`

  * `datastudio.datasources.delete`
  * `datastudio.datasources.get`
  * `datastudio.datasources.getIamPolicy`
  * `datastudio.datasources.move`
  * `datastudio.datasources.restoreTrash`
  * `datastudio.datasources.search`
  * `datastudio.datasources.setIamPolicy`
  * `datastudio.datasources.settingsShare`
  * `datastudio.datasources.share`
  * `datastudio.datasources.trash`
  * `datastudio.datasources.update`
  * `datastudio.reports.delete`
  * `datastudio.reports.get`
  * `datastudio.reports.getIamPolicy`
  * `datastudio.reports.move`
  * `datastudio.reports.restoreTrash`
  * `datastudio.reports.search`
  * `datastudio.reports.setIamPolicy`
  * `datastudio.reports.settingsShare`
  * `datastudio.reports.share`
  * `datastudio.reports.trash`
  * `datastudio.reports.update`
  * `datastudio.workspaces.createUnder`
  * `datastudio.workspaces.delete`
  * `datastudio.workspaces.get`
  * `datastudio.workspaces.getIamPolicy`
  * `datastudio.workspaces.moveIn`
  * `datastudio.workspaces.moveOut`
  * `datastudio.workspaces.restoreTrash`
  * `datastudio.workspaces.search`
  * `datastudio.workspaces.setIamPolicy`
  * `datastudio.workspaces.trash`
  * `datastudio.workspaces.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Studio Asset Editor Beta

(`roles/datastudio.editor`) Editor of a Data Studio resource  |  `datastudio.datasources.get` `datastudio.datasources.getIamPolicy` `datastudio.datasources.search` `datastudio.datasources.update` `datastudio.reports.get` `datastudio.reports.getIamPolicy` `datastudio.reports.search` `datastudio.reports.update` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy`  
  
#### Data Studio Asset Viewer Beta

(`roles/datastudio.viewer`) Viewer of a Data Studio resource  |  `datastudio.datasources.get` `datastudio.datasources.search` `datastudio.reports.get` `datastudio.reports.search` `resourcemanager.projects.get`  
  
#### Data Studio Workspace Content Manager Beta

(`roles/datastudio.contentManager`) Content Manager of a Data Studio resource  |  `datastudio.datasources.get` `datastudio.datasources.getIamPolicy` `datastudio.datasources.move` `datastudio.datasources.restoreTrash` `datastudio.datasources.search` `datastudio.datasources.settingsShare` `datastudio.datasources.share` `datastudio.datasources.trash` `datastudio.datasources.update` `datastudio.reports.get` `datastudio.reports.getIamPolicy` `datastudio.reports.move` `datastudio.reports.restoreTrash` `datastudio.reports.search` `datastudio.reports.settingsShare` `datastudio.reports.share` `datastudio.reports.trash` `datastudio.reports.update` `datastudio.workspaces.createUnder` `datastudio.workspaces.get` `datastudio.workspaces.getIamPolicy` `datastudio.workspaces.moveIn` `datastudio.workspaces.search` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy`  
  
#### Data Studio Workspace Contributor Beta

(`roles/datastudio.contributor`) Contributor of a Data Studio resource  |  `datastudio.datasources.get` `datastudio.datasources.getIamPolicy` `datastudio.datasources.restoreTrash` `datastudio.datasources.search` `datastudio.datasources.settingsShare` `datastudio.datasources.share` `datastudio.datasources.update` `datastudio.reports.get` `datastudio.reports.getIamPolicy` `datastudio.reports.restoreTrash` `datastudio.reports.search` `datastudio.reports.settingsShare` `datastudio.reports.share` `datastudio.reports.update` `datastudio.workspaces.createUnder` `datastudio.workspaces.get` `datastudio.workspaces.getIamPolicy` `datastudio.workspaces.moveIn` `datastudio.workspaces.search` `resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy`  
  
#### Data Studio Workspace Manager Beta

(`roles/datastudio.manager`) Manager of a Data Studio resource  |  `datastudio.*`

  * `datastudio.datasources.delete`
  * `datastudio.datasources.get`
  * `datastudio.datasources.getIamPolicy`
  * `datastudio.datasources.move`
  * `datastudio.datasources.restoreTrash`
  * `datastudio.datasources.search`
  * `datastudio.datasources.setIamPolicy`
  * `datastudio.datasources.settingsShare`
  * `datastudio.datasources.share`
  * `datastudio.datasources.trash`
  * `datastudio.datasources.update`
  * `datastudio.reports.delete`
  * `datastudio.reports.get`
  * `datastudio.reports.getIamPolicy`
  * `datastudio.reports.move`
  * `datastudio.reports.restoreTrash`
  * `datastudio.reports.search`
  * `datastudio.reports.setIamPolicy`
  * `datastudio.reports.settingsShare`
  * `datastudio.reports.share`
  * `datastudio.reports.trash`
  * `datastudio.reports.update`
  * `datastudio.workspaces.createUnder`
  * `datastudio.workspaces.delete`
  * `datastudio.workspaces.get`
  * `datastudio.workspaces.getIamPolicy`
  * `datastudio.workspaces.moveIn`
  * `datastudio.workspaces.moveOut`
  * `datastudio.workspaces.restoreTrash`
  * `datastudio.workspaces.search`
  * `datastudio.workspaces.setIamPolicy`
  * `datastudio.workspaces.trash`
  * `datastudio.workspaces.update`

`resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy`  
  
#### Data Studio Workspace Viewer Beta

(`roles/datastudio.workspaceViewer`) Viewer of a Data Studio Workspace  |  `datastudio.datasources.get` `datastudio.datasources.search` `datastudio.reports.get` `datastudio.reports.search` `datastudio.workspaces.get` `datastudio.workspaces.search` `resourcemanager.projects.get`  
  
#### Looker Admin Beta

(`roles/lookerstudio.lookerAdmin`) Admin of Looker instance mapping to a Studio subscription  |  `datastudio.*`

  * `datastudio.datasources.delete`
  * `datastudio.datasources.get`
  * `datastudio.datasources.getIamPolicy`
  * `datastudio.datasources.move`
  * `datastudio.datasources.restoreTrash`
  * `datastudio.datasources.search`
  * `datastudio.datasources.setIamPolicy`
  * `datastudio.datasources.settingsShare`
  * `datastudio.datasources.share`
  * `datastudio.datasources.trash`
  * `datastudio.datasources.update`
  * `datastudio.reports.delete`
  * `datastudio.reports.get`
  * `datastudio.reports.getIamPolicy`
  * `datastudio.reports.move`
  * `datastudio.reports.restoreTrash`
  * `datastudio.reports.search`
  * `datastudio.reports.setIamPolicy`
  * `datastudio.reports.settingsShare`
  * `datastudio.reports.share`
  * `datastudio.reports.trash`
  * `datastudio.reports.update`
  * `datastudio.workspaces.createUnder`
  * `datastudio.workspaces.delete`
  * `datastudio.workspaces.get`
  * `datastudio.workspaces.getIamPolicy`
  * `datastudio.workspaces.moveIn`
  * `datastudio.workspaces.moveOut`
  * `datastudio.workspaces.restoreTrash`
  * `datastudio.workspaces.search`
  * `datastudio.workspaces.setIamPolicy`
  * `datastudio.workspaces.trash`
  * `datastudio.workspaces.update`

`resourcemanager.projects.get` `resourcemanager.projects.getIamPolicy`  
  
#### Looker Studio Pro Manager Beta

(`roles/lookerstudio.proManager`) Looker Studio Pro Manager  |  `lookerstudio.pro.manage` `resourcemanager.projects.get` `resourcemanager.projects.list` `resourcemanager.projects.updateLiens`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Data Studio Managed Storage Service Agent 

(`roles/datastudio.managedStorageServiceAgent`) Grants Data Studio Service Account access to manage resources in the user project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.datasets.get` `bigquery.tables.create` `bigquery.tables.delete` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list`  
  
#### Data Studio Service Agent 

(`roles/datastudio.serviceAgent`) Grants Data Studio Service Account access to manage resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.jobs.create` `serviceusage.services.use`  
  
## Data Studio permissions

Permission | Included in roles  
---|---  
  
#### `datastudio.datasources.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Asset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.viewer) (`roles/datastudio.viewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.move`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.restoreTrash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Asset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.viewer) (`roles/datastudio.viewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.settingsShare`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.share`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.trash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.datasources.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Asset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.viewer) (`roles/datastudio.viewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.move`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.restoreTrash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Asset Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.viewer) (`roles/datastudio.viewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.settingsShare`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.share`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.trash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.reports.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Asset Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.editor) (`roles/datastudio.editor`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.createUnder`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.moveIn`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.moveOut`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.restoreTrash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Content Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contentManager) (`roles/datastudio.contentManager`)  [Data Studio Workspace Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.contributor) (`roles/datastudio.contributor`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Data Studio Workspace Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.workspaceViewer) (`roles/datastudio.workspaceViewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.trash`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `datastudio.workspaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.admin) (`roles/datastudio.admin`)  [Data Studio Workspace Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#datastudio.manager) (`roles/datastudio.manager`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.lookerAdmin) (`roles/lookerstudio.lookerAdmin`)   
  
#### `lookerstudio.pro.manage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Looker Studio Pro Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
