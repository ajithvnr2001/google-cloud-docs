---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig/
title: Cloud Runtime Configuration API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:51:14.630846+00:00
---

# Cloud Runtime Configuration API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Runtime Configuration API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Runtime Configuration API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Runtime Configuration API roles

Role | Permissions  
---|---  
  
#### Cloud RuntimeConfig Admin 

(`roles/runtimeconfig.admin`) Full access to RuntimeConfig resources.  |  `runtimeconfig.*`

  * `runtimeconfig.configs.create`
  * `runtimeconfig.configs.delete`
  * `runtimeconfig.configs.get`
  * `runtimeconfig.configs.getIamPolicy`
  * `runtimeconfig.configs.list`
  * `runtimeconfig.configs.setIamPolicy`
  * `runtimeconfig.configs.update`
  * `runtimeconfig.operations.get`
  * `runtimeconfig.operations.list`
  * `runtimeconfig.variables.create`
  * `runtimeconfig.variables.delete`
  * `runtimeconfig.variables.get`
  * `runtimeconfig.variables.getIamPolicy`
  * `runtimeconfig.variables.list`
  * `runtimeconfig.variables.setIamPolicy`
  * `runtimeconfig.variables.update`
  * `runtimeconfig.variables.watch`
  * `runtimeconfig.waiters.create`
  * `runtimeconfig.waiters.delete`
  * `runtimeconfig.waiters.get`
  * `runtimeconfig.waiters.getIamPolicy`
  * `runtimeconfig.waiters.list`
  * `runtimeconfig.waiters.setIamPolicy`
  * `runtimeconfig.waiters.update`

  
  
#### Runtimeconfig Editor 

(`roles/runtimeconfig.editor`) Editor role for runtimeconfig  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `runtimeconfig.configs.create` `runtimeconfig.configs.delete` `runtimeconfig.configs.get` `runtimeconfig.configs.list` `runtimeconfig.configs.update` `runtimeconfig.operations.*`

  * `runtimeconfig.operations.get`
  * `runtimeconfig.operations.list`

`runtimeconfig.variables.create` `runtimeconfig.variables.delete` `runtimeconfig.variables.get` `runtimeconfig.variables.list` `runtimeconfig.variables.update` `runtimeconfig.variables.watch` `runtimeconfig.waiters.create` `runtimeconfig.waiters.delete` `runtimeconfig.waiters.get` `runtimeconfig.waiters.list` `runtimeconfig.waiters.update`  
  
#### Runtimeconfig Viewer 

(`roles/runtimeconfig.viewer`) Viewer role for runtimeconfig  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `runtimeconfig.configs.get` `runtimeconfig.configs.list` `runtimeconfig.operations.*`

  * `runtimeconfig.operations.get`
  * `runtimeconfig.operations.list`

`runtimeconfig.variables.get` `runtimeconfig.variables.list` `runtimeconfig.variables.watch` `runtimeconfig.waiters.get` `runtimeconfig.waiters.list`  
  
## Cloud Runtime Configuration API permissions

Permission | Included in roles  
---|---  
  
#### `runtimeconfig.configs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.configs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.configs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.configs.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `runtimeconfig.configs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.configs.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)   
  
#### `runtimeconfig.configs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `runtimeconfig.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `runtimeconfig.variables.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.variables.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.variables.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.variables.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `runtimeconfig.variables.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.variables.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)   
  
#### `runtimeconfig.variables.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.variables.watch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `runtimeconfig.waiters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.waiters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.waiters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.waiters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)   
  
#### `runtimeconfig.waiters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Runtimeconfig Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.viewer) (`roles/runtimeconfig.viewer`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `runtimeconfig.waiters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)   
  
#### `runtimeconfig.waiters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Firebase Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.admin) (`roles/firebase.admin`)  [Cloud RuntimeConfig Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.admin) (`roles/runtimeconfig.admin`)  [Runtimeconfig Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/runtimeconfig#runtimeconfig.editor) (`roles/runtimeconfig.editor`)  [Firebase Develop Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/firebase#firebase.developAdmin) (`roles/firebase.developAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
