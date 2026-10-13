---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/looker/
title: Looker roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:03.903848+00:00
---

# Looker roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/looker/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Looker roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Looker. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Looker roles

Role | Permissions  
---|---  
  
#### Looker Admin 

(`roles/looker.admin`) Full access to all Looker resources.  |  `looker.*`

  * `looker.backups.create`
  * `looker.backups.delete`
  * `looker.backups.get`
  * `looker.backups.list`
  * `looker.instances.create`
  * `looker.instances.createTagBinding`
  * `looker.instances.delete`
  * `looker.instances.deleteTagBinding`
  * `looker.instances.export`
  * `looker.instances.get`
  * `looker.instances.import`
  * `looker.instances.list`
  * `looker.instances.listEffectiveTags`
  * `looker.instances.listTagBindings`
  * `looker.instances.login`
  * `looker.instances.update`
  * `looker.locations.get`
  * `looker.locations.list`
  * `looker.operations.cancel`
  * `looker.operations.delete`
  * `looker.operations.get`
  * `looker.operations.list`

`monitoring.timeSeries.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.quotas.get`  
  
#### Looker Viewer 

(`roles/looker.viewer`) Read-only access to all Looker resources.  |  `looker.backups.get` `looker.backups.list` `looker.instances.get` `looker.instances.list` `looker.instances.listEffectiveTags` `looker.instances.listTagBindings` `looker.instances.login` `looker.locations.*`

  * `looker.locations.get`
  * `looker.locations.list`

`looker.operations.get` `looker.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Looker Instance User 

(`roles/looker.instanceUser`) Access to log in to a Looker instance.  |  `looker.instances.get` `looker.instances.login` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Looker Service Agent 

(`roles/looker.restrictedServiceAgent`) Gives the Looker service account permission to manage customer resources. Does not include permissions to access BigQuery.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `compute.globalAddresses.get` `looker.backups.create` `looker.instances.get` `resourcemanager.projects.get` `serviceusage.services.use`  
  
#### (Legacy) Looker Service Agent 

(`roles/looker.serviceAgent`) Legacy role that gives the Looker service account permission to manage customer resources, including BigQuery  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.config.get` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.models.export` `bigquery.models.getData` `bigquery.models.getMetadata` `bigquery.models.list` `bigquery.tables.create` `bigquery.tables.createSnapshot` `bigquery.tables.export` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `compute.globalAddresses.get` `looker.backups.create` `looker.instances.get` `resourcemanager.projects.get` `serviceusage.services.use`  
  
## Looker permissions

Permission | Included in roles  
---|---  
  
#### `looker.backups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Looker Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.restrictedServiceAgent) (`roles/looker.restrictedServiceAgent`) 
  * [(Legacy) Looker Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.serviceAgent) (`roles/looker.serviceAgent`) 

  
  
#### `looker.backups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.backups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.backups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.instances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.instances.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `looker.instances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.instances.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `looker.instances.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Instance User](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.instanceUser) (`roles/looker.instanceUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Looker Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.restrictedServiceAgent) (`roles/looker.restrictedServiceAgent`) 
  * [(Legacy) Looker Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.serviceAgent) (`roles/looker.serviceAgent`) 

  
  
#### `looker.instances.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.instances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.instances.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.instances.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.instances.login`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Looker Instance User](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.instanceUser) (`roles/looker.instanceUser`)   
  
#### `looker.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)   
  
#### `looker.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `looker.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`)  [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
