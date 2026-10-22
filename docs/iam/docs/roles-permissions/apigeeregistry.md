---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry/
title: Apigee Registry roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:00.919285+00:00
---

# Apigee Registry roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Apigee Registry roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Apigee Registry. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Apigee Registry roles

Role | Permissions  
---|---  
  
#### Cloud Apigee Registry Admin Beta

(`roles/apigeeregistry.admin`) Full access to Cloud Apigee Registry Registry and Runtime resources.  |  `apigeeregistry.*`

  * `apigeeregistry.apis.create`
  * `apigeeregistry.apis.delete`
  * `apigeeregistry.apis.get`
  * `apigeeregistry.apis.getIamPolicy`
  * `apigeeregistry.apis.list`
  * `apigeeregistry.apis.setIamPolicy`
  * `apigeeregistry.apis.update`
  * `apigeeregistry.artifacts.create`
  * `apigeeregistry.artifacts.delete`
  * `apigeeregistry.artifacts.get`
  * `apigeeregistry.artifacts.getIamPolicy`
  * `apigeeregistry.artifacts.list`
  * `apigeeregistry.artifacts.setIamPolicy`
  * `apigeeregistry.artifacts.update`
  * `apigeeregistry.deployments.create`
  * `apigeeregistry.deployments.delete`
  * `apigeeregistry.deployments.get`
  * `apigeeregistry.deployments.list`
  * `apigeeregistry.deployments.update`
  * `apigeeregistry.instances.get`
  * `apigeeregistry.instances.update`
  * `apigeeregistry.locations.get`
  * `apigeeregistry.locations.list`
  * `apigeeregistry.operations.cancel`
  * `apigeeregistry.operations.delete`
  * `apigeeregistry.operations.get`
  * `apigeeregistry.operations.list`
  * `apigeeregistry.specs.create`
  * `apigeeregistry.specs.delete`
  * `apigeeregistry.specs.get`
  * `apigeeregistry.specs.getIamPolicy`
  * `apigeeregistry.specs.list`
  * `apigeeregistry.specs.setIamPolicy`
  * `apigeeregistry.specs.update`
  * `apigeeregistry.versions.create`
  * `apigeeregistry.versions.delete`
  * `apigeeregistry.versions.get`
  * `apigeeregistry.versions.getIamPolicy`
  * `apigeeregistry.versions.list`
  * `apigeeregistry.versions.setIamPolicy`
  * `apigeeregistry.versions.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Apigee Registry Editor Beta

(`roles/apigeeregistry.editor`) Edit access to Cloud Apigee Registry Registry resources.  |  `apigeeregistry.apis.create` `apigeeregistry.apis.delete` `apigeeregistry.apis.get` `apigeeregistry.apis.getIamPolicy` `apigeeregistry.apis.list` `apigeeregistry.apis.update` `apigeeregistry.artifacts.create` `apigeeregistry.artifacts.delete` `apigeeregistry.artifacts.get` `apigeeregistry.artifacts.getIamPolicy` `apigeeregistry.artifacts.list` `apigeeregistry.artifacts.update` `apigeeregistry.deployments.*`

  * `apigeeregistry.deployments.create`
  * `apigeeregistry.deployments.delete`
  * `apigeeregistry.deployments.get`
  * `apigeeregistry.deployments.list`
  * `apigeeregistry.deployments.update`

`apigeeregistry.specs.create` `apigeeregistry.specs.delete` `apigeeregistry.specs.get` `apigeeregistry.specs.getIamPolicy` `apigeeregistry.specs.list` `apigeeregistry.specs.update` `apigeeregistry.versions.create` `apigeeregistry.versions.delete` `apigeeregistry.versions.get` `apigeeregistry.versions.getIamPolicy` `apigeeregistry.versions.list` `apigeeregistry.versions.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Apigee Registry Viewer Beta

(`roles/apigeeregistry.viewer`) Read-only access to Cloud Apigee Registry Registry resources.  |  `apigeeregistry.apis.get` `apigeeregistry.apis.list` `apigeeregistry.artifacts.get` `apigeeregistry.artifacts.list` `apigeeregistry.deployments.get` `apigeeregistry.deployments.list` `apigeeregistry.specs.get` `apigeeregistry.specs.list` `apigeeregistry.versions.get` `apigeeregistry.versions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Apigee Registry Worker Beta

(`roles/apigeeregistry.worker`) The role used by Apigee Registry application workers to read and update Apigee Registry Artifacts.  |  `apigeeregistry.apis.get` `apigeeregistry.apis.list` `apigeeregistry.apis.update` `apigeeregistry.artifacts.create` `apigeeregistry.artifacts.delete` `apigeeregistry.artifacts.get` `apigeeregistry.artifacts.list` `apigeeregistry.artifacts.update` `apigeeregistry.deployments.get` `apigeeregistry.deployments.list` `apigeeregistry.deployments.update` `apigeeregistry.specs.get` `apigeeregistry.specs.list` `apigeeregistry.specs.update` `apigeeregistry.versions.get` `apigeeregistry.versions.list` `apigeeregistry.versions.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Apigee Registry permissions

Permission | Included in roles  
---|---  
  
#### `apigeeregistry.apis.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.apis.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.apis.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.apis.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.apis.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.apis.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigeeregistry.apis.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.artifacts.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.artifacts.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.artifacts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.artifacts.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.artifacts.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.artifacts.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigeeregistry.artifacts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.deployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.deployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.deployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.deployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.deployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.instances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.instances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)   
  
#### `apigeeregistry.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)   
  
#### `apigeeregistry.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)   
  
#### `apigeeregistry.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.specs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.specs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.specs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.specs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.specs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.specs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigeeregistry.specs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
#### `apigeeregistry.versions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.versions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)   
  
#### `apigeeregistry.versions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.versions.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.versions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.viewer) (`roles/apigeeregistry.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `apigeeregistry.versions.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `apigeeregistry.versions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Apigee Registry Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.admin) (`roles/apigeeregistry.admin`)  [Cloud Apigee Registry Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.editor) (`roles/apigeeregistry.editor`)  [Cloud Apigee Registry Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/apigeeregistry#apigeeregistry.worker) (`roles/apigeeregistry.worker`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
