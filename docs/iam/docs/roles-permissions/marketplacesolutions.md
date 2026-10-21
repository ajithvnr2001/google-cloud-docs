---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions/
title: Marketplace Solutions API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:48:11.054661+00:00
---

# Marketplace Solutions API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Marketplace Solutions API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Marketplace Solutions API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Marketplace Solutions API roles

Role | Permissions  
---|---  
  
#### Marketplace Solutions Admin Beta

(`roles/marketplacesolutions.admin`) Full access to Marketplace Solutions resources.  |  `marketplacesolutions.*`

  * `marketplacesolutions.locations.get`
  * `marketplacesolutions.locations.list`
  * `marketplacesolutions.operations.cancel`
  * `marketplacesolutions.operations.delete`
  * `marketplacesolutions.operations.get`
  * `marketplacesolutions.operations.list`
  * `marketplacesolutions.powerImages.get`
  * `marketplacesolutions.powerImages.list`
  * `marketplacesolutions.powerInstances.applyPowerAction`
  * `marketplacesolutions.powerInstances.create`
  * `marketplacesolutions.powerInstances.delete`
  * `marketplacesolutions.powerInstances.get`
  * `marketplacesolutions.powerInstances.list`
  * `marketplacesolutions.powerInstances.reset`
  * `marketplacesolutions.powerInstances.update`
  * `marketplacesolutions.powerNetworks.get`
  * `marketplacesolutions.powerNetworks.list`
  * `marketplacesolutions.powerSshKeys.get`
  * `marketplacesolutions.powerSshKeys.list`
  * `marketplacesolutions.powerVolumes.get`
  * `marketplacesolutions.powerVolumes.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Marketplace Solutions Editor Beta

(`roles/marketplacesolutions.editor`) Edit access to Marketplace Solutions resources.  |  `marketplacesolutions.locations.*`

  * `marketplacesolutions.locations.get`
  * `marketplacesolutions.locations.list`

`marketplacesolutions.operations.get` `marketplacesolutions.operations.list` `marketplacesolutions.powerImages.*`

  * `marketplacesolutions.powerImages.get`
  * `marketplacesolutions.powerImages.list`

`marketplacesolutions.powerInstances.get` `marketplacesolutions.powerInstances.list` `marketplacesolutions.powerInstances.update` `marketplacesolutions.powerNetworks.*`

  * `marketplacesolutions.powerNetworks.get`
  * `marketplacesolutions.powerNetworks.list`

`marketplacesolutions.powerSshKeys.*`

  * `marketplacesolutions.powerSshKeys.get`
  * `marketplacesolutions.powerSshKeys.list`

`marketplacesolutions.powerVolumes.*`

  * `marketplacesolutions.powerVolumes.get`
  * `marketplacesolutions.powerVolumes.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Marketplace Solutions Viewer Beta

(`roles/marketplacesolutions.viewer`) Readonly access to Marketplace Solutions resources.  |  `marketplacesolutions.locations.*`

  * `marketplacesolutions.locations.get`
  * `marketplacesolutions.locations.list`

`marketplacesolutions.operations.get` `marketplacesolutions.operations.list` `marketplacesolutions.powerImages.*`

  * `marketplacesolutions.powerImages.get`
  * `marketplacesolutions.powerImages.list`

`marketplacesolutions.powerInstances.get` `marketplacesolutions.powerInstances.list` `marketplacesolutions.powerNetworks.*`

  * `marketplacesolutions.powerNetworks.get`
  * `marketplacesolutions.powerNetworks.list`

`marketplacesolutions.powerSshKeys.*`

  * `marketplacesolutions.powerSshKeys.get`
  * `marketplacesolutions.powerSshKeys.list`

`marketplacesolutions.powerVolumes.*`

  * `marketplacesolutions.powerVolumes.get`
  * `marketplacesolutions.powerVolumes.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Marketplace Solutions API permissions

Permission | Included in roles  
---|---  
  
#### `marketplacesolutions.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerImages.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerImages.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerInstances.applyPowerAction`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.powerInstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.powerInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.powerInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerInstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerInstances.reset`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)   
  
#### `marketplacesolutions.powerInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)   
  
#### `marketplacesolutions.powerNetworks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerNetworks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerSshKeys.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerSshKeys.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerVolumes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `marketplacesolutions.powerVolumes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Marketplace Solutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.admin) (`roles/marketplacesolutions.admin`)  [Marketplace Solutions Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.editor) (`roles/marketplacesolutions.editor`)  [Marketplace Solutions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/marketplacesolutions#marketplacesolutions.viewer) (`roles/marketplacesolutions.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
