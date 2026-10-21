---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem/
title: Google Distributed Cloud roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:52:42.146440+00:00
---

# Google Distributed Cloud roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Google Distributed Cloud roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Google Distributed Cloud. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Google Distributed Cloud roles

Role | Permissions  
---|---  
  
#### GKE on-prem Admin 

(`roles/gkeonprem.admin`) Full access to GKE on-prem all resources.  |  `gkeonprem.*`

  * `gkeonprem.bareMetalAdminClusters.connect`
  * `gkeonprem.bareMetalAdminClusters.create`
  * `gkeonprem.bareMetalAdminClusters.createTagBinding`
  * `gkeonprem.bareMetalAdminClusters.deleteTagBinding`
  * `gkeonprem.bareMetalAdminClusters.enroll`
  * `gkeonprem.bareMetalAdminClusters.get`
  * `gkeonprem.bareMetalAdminClusters.getIamPolicy`
  * `gkeonprem.bareMetalAdminClusters.list`
  * `gkeonprem.bareMetalAdminClusters.listEffectiveTags`
  * `gkeonprem.bareMetalAdminClusters.listTagBindings`
  * `gkeonprem.bareMetalAdminClusters.queryVersionConfig`
  * `gkeonprem.bareMetalAdminClusters.setIamPolicy`
  * `gkeonprem.bareMetalAdminClusters.unenroll`
  * `gkeonprem.bareMetalAdminClusters.update`
  * `gkeonprem.bareMetalClusters.create`
  * `gkeonprem.bareMetalClusters.createTagBinding`
  * `gkeonprem.bareMetalClusters.delete`
  * `gkeonprem.bareMetalClusters.deleteTagBinding`
  * `gkeonprem.bareMetalClusters.enroll`
  * `gkeonprem.bareMetalClusters.get`
  * `gkeonprem.bareMetalClusters.getIamPolicy`
  * `gkeonprem.bareMetalClusters.list`
  * `gkeonprem.bareMetalClusters.listEffectiveTags`
  * `gkeonprem.bareMetalClusters.listTagBindings`
  * `gkeonprem.bareMetalClusters.queryVersionConfig`
  * `gkeonprem.bareMetalClusters.setIamPolicy`
  * `gkeonprem.bareMetalClusters.unenroll`
  * `gkeonprem.bareMetalClusters.update`
  * `gkeonprem.bareMetalNodePools.create`
  * `gkeonprem.bareMetalNodePools.delete`
  * `gkeonprem.bareMetalNodePools.enroll`
  * `gkeonprem.bareMetalNodePools.get`
  * `gkeonprem.bareMetalNodePools.getIamPolicy`
  * `gkeonprem.bareMetalNodePools.list`
  * `gkeonprem.bareMetalNodePools.setIamPolicy`
  * `gkeonprem.bareMetalNodePools.unenroll`
  * `gkeonprem.bareMetalNodePools.update`
  * `gkeonprem.locations.get`
  * `gkeonprem.locations.list`
  * `gkeonprem.operations.cancel`
  * `gkeonprem.operations.delete`
  * `gkeonprem.operations.get`
  * `gkeonprem.operations.list`
  * `gkeonprem.vmwareAdminClusters.connect`
  * `gkeonprem.vmwareAdminClusters.createTagBinding`
  * `gkeonprem.vmwareAdminClusters.deleteTagBinding`
  * `gkeonprem.vmwareAdminClusters.enroll`
  * `gkeonprem.vmwareAdminClusters.get`
  * `gkeonprem.vmwareAdminClusters.getIamPolicy`
  * `gkeonprem.vmwareAdminClusters.list`
  * `gkeonprem.vmwareAdminClusters.listEffectiveTags`
  * `gkeonprem.vmwareAdminClusters.listTagBindings`
  * `gkeonprem.vmwareAdminClusters.setIamPolicy`
  * `gkeonprem.vmwareAdminClusters.unenroll`
  * `gkeonprem.vmwareAdminClusters.update`
  * `gkeonprem.vmwareClusters.create`
  * `gkeonprem.vmwareClusters.createTagBinding`
  * `gkeonprem.vmwareClusters.delete`
  * `gkeonprem.vmwareClusters.deleteTagBinding`
  * `gkeonprem.vmwareClusters.enroll`
  * `gkeonprem.vmwareClusters.get`
  * `gkeonprem.vmwareClusters.getIamPolicy`
  * `gkeonprem.vmwareClusters.list`
  * `gkeonprem.vmwareClusters.listEffectiveTags`
  * `gkeonprem.vmwareClusters.listTagBindings`
  * `gkeonprem.vmwareClusters.queryVersionConfig`
  * `gkeonprem.vmwareClusters.setIamPolicy`
  * `gkeonprem.vmwareClusters.unenroll`
  * `gkeonprem.vmwareClusters.update`
  * `gkeonprem.vmwareNodePools.create`
  * `gkeonprem.vmwareNodePools.delete`
  * `gkeonprem.vmwareNodePools.enroll`
  * `gkeonprem.vmwareNodePools.get`
  * `gkeonprem.vmwareNodePools.getIamPolicy`
  * `gkeonprem.vmwareNodePools.list`
  * `gkeonprem.vmwareNodePools.setIamPolicy`
  * `gkeonprem.vmwareNodePools.unenroll`
  * `gkeonprem.vmwareNodePools.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GKE on-prem Editor 

(`roles/gkeonprem.editor`) Editor role for GKE on-prem  |  `gkeonprem.bareMetalAdminClusters.connect` `gkeonprem.bareMetalAdminClusters.create` `gkeonprem.bareMetalAdminClusters.enroll` `gkeonprem.bareMetalAdminClusters.get` `gkeonprem.bareMetalAdminClusters.getIamPolicy` `gkeonprem.bareMetalAdminClusters.list` `gkeonprem.bareMetalAdminClusters.listEffectiveTags` `gkeonprem.bareMetalAdminClusters.listTagBindings` `gkeonprem.bareMetalAdminClusters.queryVersionConfig` `gkeonprem.bareMetalAdminClusters.unenroll` `gkeonprem.bareMetalAdminClusters.update` `gkeonprem.bareMetalClusters.create` `gkeonprem.bareMetalClusters.delete` `gkeonprem.bareMetalClusters.enroll` `gkeonprem.bareMetalClusters.get` `gkeonprem.bareMetalClusters.getIamPolicy` `gkeonprem.bareMetalClusters.list` `gkeonprem.bareMetalClusters.listEffectiveTags` `gkeonprem.bareMetalClusters.listTagBindings` `gkeonprem.bareMetalClusters.queryVersionConfig` `gkeonprem.bareMetalClusters.unenroll` `gkeonprem.bareMetalClusters.update` `gkeonprem.bareMetalNodePools.create` `gkeonprem.bareMetalNodePools.delete` `gkeonprem.bareMetalNodePools.enroll` `gkeonprem.bareMetalNodePools.get` `gkeonprem.bareMetalNodePools.getIamPolicy` `gkeonprem.bareMetalNodePools.list` `gkeonprem.bareMetalNodePools.unenroll` `gkeonprem.bareMetalNodePools.update` `gkeonprem.locations.*`

  * `gkeonprem.locations.get`
  * `gkeonprem.locations.list`

`gkeonprem.operations.*`

  * `gkeonprem.operations.cancel`
  * `gkeonprem.operations.delete`
  * `gkeonprem.operations.get`
  * `gkeonprem.operations.list`

`gkeonprem.vmwareAdminClusters.connect` `gkeonprem.vmwareAdminClusters.enroll` `gkeonprem.vmwareAdminClusters.get` `gkeonprem.vmwareAdminClusters.getIamPolicy` `gkeonprem.vmwareAdminClusters.list` `gkeonprem.vmwareAdminClusters.listEffectiveTags` `gkeonprem.vmwareAdminClusters.listTagBindings` `gkeonprem.vmwareAdminClusters.unenroll` `gkeonprem.vmwareAdminClusters.update` `gkeonprem.vmwareClusters.create` `gkeonprem.vmwareClusters.delete` `gkeonprem.vmwareClusters.enroll` `gkeonprem.vmwareClusters.get` `gkeonprem.vmwareClusters.getIamPolicy` `gkeonprem.vmwareClusters.list` `gkeonprem.vmwareClusters.listEffectiveTags` `gkeonprem.vmwareClusters.listTagBindings` `gkeonprem.vmwareClusters.queryVersionConfig` `gkeonprem.vmwareClusters.unenroll` `gkeonprem.vmwareClusters.update` `gkeonprem.vmwareNodePools.create` `gkeonprem.vmwareNodePools.delete` `gkeonprem.vmwareNodePools.enroll` `gkeonprem.vmwareNodePools.get` `gkeonprem.vmwareNodePools.getIamPolicy` `gkeonprem.vmwareNodePools.list` `gkeonprem.vmwareNodePools.unenroll` `gkeonprem.vmwareNodePools.update` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### GKE on-prem Viewer 

(`roles/gkeonprem.viewer`) Read-only access to GKE on-prem all resources.  |  `gkeonprem.bareMetalAdminClusters.connect` `gkeonprem.bareMetalAdminClusters.get` `gkeonprem.bareMetalAdminClusters.getIamPolicy` `gkeonprem.bareMetalAdminClusters.list` `gkeonprem.bareMetalAdminClusters.listEffectiveTags` `gkeonprem.bareMetalAdminClusters.listTagBindings` `gkeonprem.bareMetalAdminClusters.queryVersionConfig` `gkeonprem.bareMetalClusters.get` `gkeonprem.bareMetalClusters.getIamPolicy` `gkeonprem.bareMetalClusters.list` `gkeonprem.bareMetalClusters.listEffectiveTags` `gkeonprem.bareMetalClusters.listTagBindings` `gkeonprem.bareMetalClusters.queryVersionConfig` `gkeonprem.bareMetalNodePools.get` `gkeonprem.bareMetalNodePools.getIamPolicy` `gkeonprem.bareMetalNodePools.list` `gkeonprem.locations.*`

  * `gkeonprem.locations.get`
  * `gkeonprem.locations.list`

`gkeonprem.operations.get` `gkeonprem.operations.list` `gkeonprem.vmwareAdminClusters.connect` `gkeonprem.vmwareAdminClusters.get` `gkeonprem.vmwareAdminClusters.getIamPolicy` `gkeonprem.vmwareAdminClusters.list` `gkeonprem.vmwareAdminClusters.listEffectiveTags` `gkeonprem.vmwareAdminClusters.listTagBindings` `gkeonprem.vmwareClusters.get` `gkeonprem.vmwareClusters.getIamPolicy` `gkeonprem.vmwareClusters.list` `gkeonprem.vmwareClusters.listEffectiveTags` `gkeonprem.vmwareClusters.listTagBindings` `gkeonprem.vmwareClusters.queryVersionConfig` `gkeonprem.vmwareNodePools.get` `gkeonprem.vmwareNodePools.getIamPolicy` `gkeonprem.vmwareNodePools.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### GKE On-Prem Service Agent 

(`roles/gkeonprem.serviceAgent`) Gives the GKE On-Prem service agent access to Cloud Platform resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `gkehub.memberships.delete` `gkehub.memberships.get` `gkehub.memberships.update` `gkeonprem.bareMetalAdminClusters.connect` `gkeonprem.bareMetalAdminClusters.enroll` `gkeonprem.bareMetalAdminClusters.get` `gkeonprem.bareMetalAdminClusters.unenroll` `gkeonprem.bareMetalClusters.enroll` `gkeonprem.bareMetalClusters.get` `gkeonprem.bareMetalClusters.unenroll` `gkeonprem.bareMetalNodePools.enroll` `gkeonprem.bareMetalNodePools.get` `gkeonprem.bareMetalNodePools.unenroll` `gkeonprem.operations.get` `gkeonprem.operations.list` `gkeonprem.vmwareAdminClusters.connect` `gkeonprem.vmwareAdminClusters.enroll` `gkeonprem.vmwareAdminClusters.get` `gkeonprem.vmwareAdminClusters.unenroll` `gkeonprem.vmwareClusters.enroll` `gkeonprem.vmwareClusters.get` `gkeonprem.vmwareClusters.unenroll` `gkeonprem.vmwareNodePools.enroll` `gkeonprem.vmwareNodePools.get` `gkeonprem.vmwareNodePools.unenroll`  
  
## Google Distributed Cloud permissions

Permission | Included in roles  
---|---  
  
#### `gkeonprem.bareMetalAdminClusters.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalAdminClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalAdminClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.bareMetalAdminClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.bareMetalAdminClusters.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalAdminClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalAdminClusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalAdminClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalAdminClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalAdminClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalAdminClusters.queryVersionConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalAdminClusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.bareMetalAdminClusters.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalAdminClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.bareMetalClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.bareMetalClusters.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalClusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalClusters.queryVersionConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalClusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.bareMetalClusters.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalNodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalNodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.bareMetalNodePools.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalNodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalNodePools.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalNodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.bareMetalNodePools.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.bareMetalNodePools.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.bareMetalNodePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareAdminClusters.connect`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareAdminClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.vmwareAdminClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.vmwareAdminClusters.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareAdminClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareAdminClusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareAdminClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareAdminClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareAdminClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareAdminClusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.vmwareAdminClusters.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareAdminClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareClusters.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.vmwareClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareClusters.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `gkeonprem.vmwareClusters.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE Hub Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.serviceAgent) (`roles/gkehub.serviceAgent`) 
  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareClusters.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareClusters.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareClusters.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareClusters.queryVersionConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareClusters.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.vmwareClusters.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareNodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareNodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
#### `gkeonprem.vmwareNodePools.enroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareNodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareNodePools.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareNodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  [GKE on-prem Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.viewer) (`roles/gkeonprem.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `gkeonprem.vmwareNodePools.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)   
  
#### `gkeonprem.vmwareNodePools.unenroll`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [GKE On-Prem Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.serviceAgent) (`roles/gkeonprem.serviceAgent`) 

  
  
#### `gkeonprem.vmwareNodePools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [GKE on-prem Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.admin) (`roles/gkeonprem.admin`)  [GKE on-prem Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/gkeonprem#gkeonprem.editor) (`roles/gkeonprem.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
