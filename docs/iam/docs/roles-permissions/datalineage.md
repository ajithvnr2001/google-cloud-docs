---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage/
title: Data Lineage API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:04.703172+00:00
---

# Data Lineage API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Data Lineage API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Data Lineage API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Data Lineage API roles

Role | Permissions  
---|---  
  
#### Data Lineage Administrator 

(`roles/datalineage.admin`) Grants full access to all resources in Data Lineage API  |  `datalineage.*`

  * `datalineage.configs.get`
  * `datalineage.configs.update`
  * `datalineage.events.create`
  * `datalineage.events.delete`
  * `datalineage.events.get`
  * `datalineage.events.getFields`
  * `datalineage.events.list`
  * `datalineage.locations.processOpenLineageMessage`
  * `datalineage.locations.searchLinks`
  * `datalineage.operations.get`
  * `datalineage.processRevisions.delete`
  * `datalineage.processRevisions.get`
  * `datalineage.processRevisions.insert`
  * `datalineage.processRevisions.list`
  * `datalineage.processes.create`
  * `datalineage.processes.delete`
  * `datalineage.processes.get`
  * `datalineage.processes.list`
  * `datalineage.processes.markAsDeleted`
  * `datalineage.processes.update`
  * `datalineage.runs.create`
  * `datalineage.runs.delete`
  * `datalineage.runs.get`
  * `datalineage.runs.list`
  * `datalineage.runs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Editor 

(`roles/datalineage.editor`) Grants edit access to all resources in Data Lineage API  |  `datalineage.events.*`

  * `datalineage.events.create`
  * `datalineage.events.delete`
  * `datalineage.events.get`
  * `datalineage.events.getFields`
  * `datalineage.events.list`

`datalineage.locations.*`

  * `datalineage.locations.processOpenLineageMessage`
  * `datalineage.locations.searchLinks`

`datalineage.operations.get` `datalineage.processRevisions.*`

  * `datalineage.processRevisions.delete`
  * `datalineage.processRevisions.get`
  * `datalineage.processRevisions.insert`
  * `datalineage.processRevisions.list`

`datalineage.processes.*`

  * `datalineage.processes.create`
  * `datalineage.processes.delete`
  * `datalineage.processes.get`
  * `datalineage.processes.list`
  * `datalineage.processes.markAsDeleted`
  * `datalineage.processes.update`

`datalineage.runs.*`

  * `datalineage.runs.create`
  * `datalineage.runs.delete`
  * `datalineage.runs.get`
  * `datalineage.runs.list`
  * `datalineage.runs.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Viewer 

(`roles/datalineage.viewer`) Grants read access to all resources in Data Lineage API  |  `datalineage.events.get` `datalineage.events.getFields` `datalineage.events.list` `datalineage.locations.searchLinks` `datalineage.processRevisions.get` `datalineage.processRevisions.list` `datalineage.processes.get` `datalineage.processes.list` `datalineage.runs.get` `datalineage.runs.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Data Lineage Events Producer 

(`roles/datalineage.producer`) Grants access to creating all resources in Data Lineage API  |  `datalineage.events.create` `datalineage.locations.processOpenLineageMessage` `datalineage.processRevisions.insert` `datalineage.processes.create` `datalineage.processes.get` `datalineage.processes.markAsDeleted` `datalineage.processes.update` `datalineage.runs.create` `datalineage.runs.get` `datalineage.runs.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Data Lineage API permissions

Permission | Included in roles  
---|---  
  
#### `datalineage.configs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.configs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)   
  
#### `datalineage.events.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.events.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)   
  
#### `datalineage.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.events.getFields`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.events.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.locations.processOpenLineageMessage`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)   
  
#### `datalineage.locations.searchLinks`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.processRevisions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)   
  
#### `datalineage.processRevisions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.processRevisions.insert`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.processRevisions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.processes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.processes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)   
  
#### `datalineage.processes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.processes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.processes.markAsDeleted`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.processes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.runs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
#### `datalineage.runs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)   
  
#### `datalineage.runs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.runs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Data Lineage Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.viewer) (`roles/datalineage.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `datalineage.runs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Data Lineage Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.admin) (`roles/datalineage.admin`)  [Data Lineage Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.editor) (`roles/datalineage.editor`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Data Lineage Events Producer](https://docs.cloud.google.com/iam/docs/roles-permissions/datalineage#datalineage.producer) (`roles/datalineage.producer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
