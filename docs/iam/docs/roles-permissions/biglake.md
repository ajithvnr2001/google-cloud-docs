---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/biglake/
title: BigLake roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:28.244640+00:00
---

# BigLake roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/biglake/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigLake roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigLake. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigLake roles

Role | Permissions  
---|---  
  
#### BigLake Admin 

(`roles/biglake.admin`) Provides full access to all BigLake resources.  |  `biglake.*`

  * `biglake.catalogs.create`
  * `biglake.catalogs.delete`
  * `biglake.catalogs.get`
  * `biglake.catalogs.getIamPolicy`
  * `biglake.catalogs.list`
  * `biglake.catalogs.setIamPolicy`
  * `biglake.catalogs.update`
  * `biglake.databases.create`
  * `biglake.databases.delete`
  * `biglake.databases.get`
  * `biglake.databases.list`
  * `biglake.databases.update`
  * `biglake.locks.check`
  * `biglake.locks.create`
  * `biglake.locks.delete`
  * `biglake.locks.list`
  * `biglake.namespaces.create`
  * `biglake.namespaces.delete`
  * `biglake.namespaces.get`
  * `biglake.namespaces.getIamPolicy`
  * `biglake.namespaces.list`
  * `biglake.namespaces.setIamPolicy`
  * `biglake.namespaces.update`
  * `biglake.tables.create`
  * `biglake.tables.createPartitions`
  * `biglake.tables.delete`
  * `biglake.tables.deletePartitions`
  * `biglake.tables.get`
  * `biglake.tables.getData`
  * `biglake.tables.getIamPolicy`
  * `biglake.tables.list`
  * `biglake.tables.listPartitions`
  * `biglake.tables.lock`
  * `biglake.tables.register`
  * `biglake.tables.setIamPolicy`
  * `biglake.tables.update`
  * `biglake.tables.updateData`
  * `biglake.tables.updatePartitions`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Editor Beta

(`roles/biglake.editor`) Provides read and write access to all BigLake resources.  |  `biglake.catalogs.create` `biglake.catalogs.delete` `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.catalogs.update` `biglake.databases.*`

  * `biglake.databases.create`
  * `biglake.databases.delete`
  * `biglake.databases.get`
  * `biglake.databases.list`
  * `biglake.databases.update`

`biglake.locks.*`

  * `biglake.locks.check`
  * `biglake.locks.create`
  * `biglake.locks.delete`
  * `biglake.locks.list`

`biglake.namespaces.create` `biglake.namespaces.delete` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.namespaces.update` `biglake.tables.create` `biglake.tables.createPartitions` `biglake.tables.delete` `biglake.tables.deletePartitions` `biglake.tables.get` `biglake.tables.getData` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `biglake.tables.lock` `biglake.tables.update` `biglake.tables.updateData` `biglake.tables.updatePartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Viewer 

(`roles/biglake.viewer`) Provides read-only access to all BigLake resources.  |  `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.databases.get` `biglake.databases.list` `biglake.locks.list` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.tables.get` `biglake.tables.getData` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Metadata Viewer Beta

(`roles/biglake.metadataViewer`) Provides read-only metadata access to all BigLake resources.  |  `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.tables.get` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## BigLake permissions

Permission | Included in roles  
---|---  
  
#### `biglake.catalogs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.catalogs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.catalogs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `biglake.catalogs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.catalogs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.catalogs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.catalogs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.databases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.databases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.databases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.databases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.databases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.locks.check`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.locks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.locks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.locks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.namespaces.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.namespaces.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.namespaces.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `biglake.namespaces.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.namespaces.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.namespaces.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.namespaces.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.createPartitions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.deletePartitions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `biglake.tables.getData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `biglake.tables.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.tables.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 

  
  
#### `biglake.tables.listPartitions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [BigLake Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.viewer) (`roles/biglake.viewer`)  [BigLake Metadata Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.metadataViewer) (`roles/biglake.metadataViewer`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `biglake.tables.lock`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.register`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.updateData`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
#### `biglake.tables.updatePartitions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigLake Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)  [BigLake Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.editor) (`roles/biglake.editor`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
