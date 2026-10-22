---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement/
title: GDC Hardware Management API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:37.223700+00:00
---

# GDC Hardware Management API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  GDC Hardware Management API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for GDC Hardware Management API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## GDC Hardware Management API roles

Role | Permissions  
---|---  
  
#### GDC Hardware Management Admin Beta

(`roles/gdchardwaremanagement.admin`) Full access to GDC Hardware Management resources.  |  `gdchardwaremanagement.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`
  * `gdchardwaremanagement.comments.create`
  * `gdchardwaremanagement.comments.get`
  * `gdchardwaremanagement.comments.list`
  * `gdchardwaremanagement.hardware.create`
  * `gdchardwaremanagement.hardware.delete`
  * `gdchardwaremanagement.hardware.get`
  * `gdchardwaremanagement.hardware.list`
  * `gdchardwaremanagement.hardware.update`
  * `gdchardwaremanagement.hardwareGroups.create`
  * `gdchardwaremanagement.hardwareGroups.delete`
  * `gdchardwaremanagement.hardwareGroups.get`
  * `gdchardwaremanagement.hardwareGroups.list`
  * `gdchardwaremanagement.hardwareGroups.update`
  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`
  * `gdchardwaremanagement.operations.cancel`
  * `gdchardwaremanagement.operations.delete`
  * `gdchardwaremanagement.operations.get`
  * `gdchardwaremanagement.operations.list`
  * `gdchardwaremanagement.orders.create`
  * `gdchardwaremanagement.orders.delete`
  * `gdchardwaremanagement.orders.get`
  * `gdchardwaremanagement.orders.list`
  * `gdchardwaremanagement.orders.submit`
  * `gdchardwaremanagement.orders.update`
  * `gdchardwaremanagement.sites.create`
  * `gdchardwaremanagement.sites.delete`
  * `gdchardwaremanagement.sites.get`
  * `gdchardwaremanagement.sites.list`
  * `gdchardwaremanagement.sites.update`
  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`
  * `gdchardwaremanagement.zones.create`
  * `gdchardwaremanagement.zones.delete`
  * `gdchardwaremanagement.zones.get`
  * `gdchardwaremanagement.zones.list`
  * `gdchardwaremanagement.zones.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Gdchardwaremanagement Viewer Beta

(`roles/gdchardwaremanagement.viewer`) Viewer role for gdchardwaremanagement  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.get` `gdchardwaremanagement.comments.list` `gdchardwaremanagement.hardware.get` `gdchardwaremanagement.hardware.list` `gdchardwaremanagement.hardwareGroups.get` `gdchardwaremanagement.hardwareGroups.list` `gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.get` `gdchardwaremanagement.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GDC Hardware Management Operator Beta

(`roles/gdchardwaremanagement.operator`) Create, read, and update access to GDC Hardware Management resources that support those operations. Also grants delete access to HardwareGroup resource.  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.*`

  * `gdchardwaremanagement.comments.create`
  * `gdchardwaremanagement.comments.get`
  * `gdchardwaremanagement.comments.list`

`gdchardwaremanagement.hardware.*`

  * `gdchardwaremanagement.hardware.create`
  * `gdchardwaremanagement.hardware.delete`
  * `gdchardwaremanagement.hardware.get`
  * `gdchardwaremanagement.hardware.list`
  * `gdchardwaremanagement.hardware.update`

`gdchardwaremanagement.hardwareGroups.*`

  * `gdchardwaremanagement.hardwareGroups.create`
  * `gdchardwaremanagement.hardwareGroups.delete`
  * `gdchardwaremanagement.hardwareGroups.get`
  * `gdchardwaremanagement.hardwareGroups.list`
  * `gdchardwaremanagement.hardwareGroups.update`

`gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.create` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.orders.update` `gdchardwaremanagement.sites.create` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.sites.update` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.*`

  * `gdchardwaremanagement.zones.create`
  * `gdchardwaremanagement.zones.delete`
  * `gdchardwaremanagement.zones.get`
  * `gdchardwaremanagement.zones.list`
  * `gdchardwaremanagement.zones.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GDC Hardware Management Reader Beta

(`roles/gdchardwaremanagement.reader`) Readonly access to GDC Hardware Management resources.  |  `gdchardwaremanagement.changeLogEntries.*`

  * `gdchardwaremanagement.changeLogEntries.get`
  * `gdchardwaremanagement.changeLogEntries.list`

`gdchardwaremanagement.comments.get` `gdchardwaremanagement.comments.list` `gdchardwaremanagement.hardware.get` `gdchardwaremanagement.hardware.list` `gdchardwaremanagement.hardwareGroups.get` `gdchardwaremanagement.hardwareGroups.list` `gdchardwaremanagement.locations.*`

  * `gdchardwaremanagement.locations.get`
  * `gdchardwaremanagement.locations.list`

`gdchardwaremanagement.operations.get` `gdchardwaremanagement.operations.list` `gdchardwaremanagement.orders.get` `gdchardwaremanagement.orders.list` `gdchardwaremanagement.sites.get` `gdchardwaremanagement.sites.list` `gdchardwaremanagement.skus.*`

  * `gdchardwaremanagement.skus.get`
  * `gdchardwaremanagement.skus.list`

`gdchardwaremanagement.zones.get` `gdchardwaremanagement.zones.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## GDC Hardware Management API permissions

Permission | Included in roles  
---|---  
  
#### `gdchardwaremanagement.changeLogEntries.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.changeLogEntries.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.comments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.comments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.comments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.hardware.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.hardware.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.hardware.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.hardware.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.hardware.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.hardwareGroups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.hardwareGroups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.hardwareGroups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.hardwareGroups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.hardwareGroups.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)   
  
#### `gdchardwaremanagement.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)   
  
#### `gdchardwaremanagement.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.orders.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.orders.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)   
  
#### `gdchardwaremanagement.orders.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.orders.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.orders.submit`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)   
  
#### `gdchardwaremanagement.orders.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.sites.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.sites.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)   
  
#### `gdchardwaremanagement.sites.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.sites.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.sites.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.skus.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.skus.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.zones.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.zones.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
#### `gdchardwaremanagement.zones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.zones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [Gdchardwaremanagement Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.viewer) (`roles/gdchardwaremanagement.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)  [GDC Hardware Management Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.reader) (`roles/gdchardwaremanagement.reader`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gdchardwaremanagement.zones.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GDC Hardware Management Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.admin) (`roles/gdchardwaremanagement.admin`)  [GDC Hardware Management Operator](https://docs.cloud.google.com/iam/docs/roles-permissions/gdchardwaremanagement#gdchardwaremanagement.operator) (`roles/gdchardwaremanagement.operator`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
