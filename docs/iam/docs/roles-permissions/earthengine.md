---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine/
title: Google Earth Engine roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:24.459709+00:00
---

# Google Earth Engine roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Earth Engine roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Earth Engine. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Earth Engine roles

Role | Permissions  
---|---  
  
#### Earth Engine Resource Admin Beta

(`roles/earthengine.admin`) Full access to all Earth Engine resource features  |  `earthengine.*`

  * `earthengine.assets.create`
  * `earthengine.assets.delete`
  * `earthengine.assets.get`
  * `earthengine.assets.getIamPolicy`
  * `earthengine.assets.list`
  * `earthengine.assets.setIamPolicy`
  * `earthengine.assets.update`
  * `earthengine.computations.create`
  * `earthengine.config.get`
  * `earthengine.config.update`
  * `earthengine.exports.create`
  * `earthengine.featureviews.create`
  * `earthengine.filmstripthumbnails.create`
  * `earthengine.filmstripthumbnails.get`
  * `earthengine.imports.create`
  * `earthengine.maps.create`
  * `earthengine.maps.get`
  * `earthengine.operations.delete`
  * `earthengine.operations.get`
  * `earthengine.operations.list`
  * `earthengine.operations.update`
  * `earthengine.tables.create`
  * `earthengine.tables.get`
  * `earthengine.thumbnails.create`
  * `earthengine.thumbnails.get`
  * `earthengine.videothumbnails.create`
  * `earthengine.videothumbnails.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Earth Engine Resource Editor Beta

(`roles/earthengine.editor`) Editor role for Earth Engine  |  `earthengine.assets.create` `earthengine.assets.delete` `earthengine.assets.get` `earthengine.assets.getIamPolicy` `earthengine.assets.list` `earthengine.assets.update` `earthengine.computations.create` `earthengine.config.*`

  * `earthengine.config.get`
  * `earthengine.config.update`

`earthengine.exports.create` `earthengine.featureviews.create` `earthengine.filmstripthumbnails.*`

  * `earthengine.filmstripthumbnails.create`
  * `earthengine.filmstripthumbnails.get`

`earthengine.imports.create` `earthengine.maps.*`

  * `earthengine.maps.create`
  * `earthengine.maps.get`

`earthengine.operations.*`

  * `earthengine.operations.delete`
  * `earthengine.operations.get`
  * `earthengine.operations.list`
  * `earthengine.operations.update`

`earthengine.tables.*`

  * `earthengine.tables.create`
  * `earthengine.tables.get`

`earthengine.thumbnails.*`

  * `earthengine.thumbnails.create`
  * `earthengine.thumbnails.get`

`earthengine.videothumbnails.*`

  * `earthengine.videothumbnails.create`
  * `earthengine.videothumbnails.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Earth Engine Resource Viewer Beta

(`roles/earthengine.viewer`) Viewer of all Earth Engine resources  |  `earthengine.assets.get` `earthengine.assets.getIamPolicy` `earthengine.assets.list` `earthengine.computations.create` `earthengine.config.get` `earthengine.filmstripthumbnails.get` `earthengine.maps.get` `earthengine.operations.get` `earthengine.operations.list` `earthengine.tables.get` `earthengine.thumbnails.get` `earthengine.videothumbnails.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Earth Engine Apps Publisher Beta

(`roles/earthengine.appsPublisher`) Publisher of Earth Engine Apps  |  `iam.serviceAccounts.create` `iam.serviceAccounts.disable` `iam.serviceAccounts.enable` `iam.serviceAccounts.get` `iam.serviceAccounts.getIamPolicy` `iam.serviceAccounts.setIamPolicy` `resourcemanager.projects.get` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.services.get` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
#### Earth Engine Resource Writer Beta

(`roles/earthengine.writer`) Writer of all Earth Engine resources  |  `earthengine.assets.create` `earthengine.assets.delete` `earthengine.assets.get` `earthengine.assets.getIamPolicy` `earthengine.assets.list` `earthengine.assets.update` `earthengine.computations.create` `earthengine.config.*`

  * `earthengine.config.get`
  * `earthengine.config.update`

`earthengine.exports.create` `earthengine.featureviews.create` `earthengine.filmstripthumbnails.*`

  * `earthengine.filmstripthumbnails.create`
  * `earthengine.filmstripthumbnails.get`

`earthengine.imports.create` `earthengine.maps.*`

  * `earthengine.maps.create`
  * `earthengine.maps.get`

`earthengine.operations.*`

  * `earthengine.operations.delete`
  * `earthengine.operations.get`
  * `earthengine.operations.list`
  * `earthengine.operations.update`

`earthengine.tables.*`

  * `earthengine.tables.create`
  * `earthengine.tables.get`

`earthengine.thumbnails.*`

  * `earthengine.thumbnails.create`
  * `earthengine.thumbnails.get`

`earthengine.videothumbnails.*`

  * `earthengine.videothumbnails.create`
  * `earthengine.videothumbnails.get`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Google Earth Engine permissions

Permission | Included in roles  
---|---  
  
#### `earthengine.assets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.assets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.assets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.assets.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.assets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.assets.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `earthengine.assets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.computations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.config.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.config.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.exports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.featureviews.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.filmstripthumbnails.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.filmstripthumbnails.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.imports.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.maps.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.maps.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.operations.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.tables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.tables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.thumbnails.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.thumbnails.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `earthengine.videothumbnails.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)   
  
#### `earthengine.videothumbnails.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Earth Engine Resource Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.admin) (`roles/earthengine.admin`)  [Earth Engine Resource Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.editor) (`roles/earthengine.editor`)  [Earth Engine Resource Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.viewer) (`roles/earthengine.viewer`)  [Earth Engine Resource Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/earthengine#earthengine.writer) (`roles/earthengine.writer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
