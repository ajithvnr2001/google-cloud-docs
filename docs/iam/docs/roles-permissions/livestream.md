---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/livestream/
title: Live Stream roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:19.778848+00:00
---

# Live Stream roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/livestream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Live Stream roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Live Stream. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Live Stream roles

Role | Permissions  
---|---  
  
#### Live Stream Admin 

(`roles/livestream.admin`) Admin role for livestream  |  `livestream.*`

  * `livestream.assets.create`
  * `livestream.assets.delete`
  * `livestream.assets.get`
  * `livestream.assets.list`
  * `livestream.channels.create`
  * `livestream.channels.createTagBinding`
  * `livestream.channels.delete`
  * `livestream.channels.deleteTagBinding`
  * `livestream.channels.get`
  * `livestream.channels.list`
  * `livestream.channels.listEffectiveTags`
  * `livestream.channels.listTagBindings`
  * `livestream.channels.start`
  * `livestream.channels.stop`
  * `livestream.channels.update`
  * `livestream.clips.create`
  * `livestream.clips.delete`
  * `livestream.clips.get`
  * `livestream.clips.list`
  * `livestream.dvrSessions.create`
  * `livestream.dvrSessions.delete`
  * `livestream.dvrSessions.get`
  * `livestream.dvrSessions.list`
  * `livestream.dvrSessions.update`
  * `livestream.events.create`
  * `livestream.events.delete`
  * `livestream.events.get`
  * `livestream.events.list`
  * `livestream.inputs.create`
  * `livestream.inputs.createTagBinding`
  * `livestream.inputs.delete`
  * `livestream.inputs.deleteTagBinding`
  * `livestream.inputs.get`
  * `livestream.inputs.list`
  * `livestream.inputs.listEffectiveTags`
  * `livestream.inputs.listTagBindings`
  * `livestream.inputs.update`
  * `livestream.locations.get`
  * `livestream.locations.list`
  * `livestream.operations.cancel`
  * `livestream.operations.delete`
  * `livestream.operations.get`
  * `livestream.operations.list`
  * `livestream.pools.createTagBinding`
  * `livestream.pools.deleteTagBinding`
  * `livestream.pools.get`
  * `livestream.pools.listEffectiveTags`
  * `livestream.pools.listTagBindings`
  * `livestream.pools.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Live Stream Editor 

(`roles/livestream.editor`) Full access to Live Stream resources.  |  `livestream.*`

  * `livestream.assets.create`
  * `livestream.assets.delete`
  * `livestream.assets.get`
  * `livestream.assets.list`
  * `livestream.channels.create`
  * `livestream.channels.createTagBinding`
  * `livestream.channels.delete`
  * `livestream.channels.deleteTagBinding`
  * `livestream.channels.get`
  * `livestream.channels.list`
  * `livestream.channels.listEffectiveTags`
  * `livestream.channels.listTagBindings`
  * `livestream.channels.start`
  * `livestream.channels.stop`
  * `livestream.channels.update`
  * `livestream.clips.create`
  * `livestream.clips.delete`
  * `livestream.clips.get`
  * `livestream.clips.list`
  * `livestream.dvrSessions.create`
  * `livestream.dvrSessions.delete`
  * `livestream.dvrSessions.get`
  * `livestream.dvrSessions.list`
  * `livestream.dvrSessions.update`
  * `livestream.events.create`
  * `livestream.events.delete`
  * `livestream.events.get`
  * `livestream.events.list`
  * `livestream.inputs.create`
  * `livestream.inputs.createTagBinding`
  * `livestream.inputs.delete`
  * `livestream.inputs.deleteTagBinding`
  * `livestream.inputs.get`
  * `livestream.inputs.list`
  * `livestream.inputs.listEffectiveTags`
  * `livestream.inputs.listTagBindings`
  * `livestream.inputs.update`
  * `livestream.locations.get`
  * `livestream.locations.list`
  * `livestream.operations.cancel`
  * `livestream.operations.delete`
  * `livestream.operations.get`
  * `livestream.operations.list`
  * `livestream.pools.createTagBinding`
  * `livestream.pools.deleteTagBinding`
  * `livestream.pools.get`
  * `livestream.pools.listEffectiveTags`
  * `livestream.pools.listTagBindings`
  * `livestream.pools.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Live Stream Viewer 

(`roles/livestream.viewer`) Read access to Live Stream resources.  |  `livestream.assets.get` `livestream.assets.list` `livestream.channels.get` `livestream.channels.list` `livestream.channels.listEffectiveTags` `livestream.channels.listTagBindings` `livestream.clips.get` `livestream.clips.list` `livestream.dvrSessions.get` `livestream.dvrSessions.list` `livestream.events.get` `livestream.events.list` `livestream.inputs.get` `livestream.inputs.list` `livestream.inputs.listEffectiveTags` `livestream.inputs.listTagBindings` `livestream.locations.*`

  * `livestream.locations.get`
  * `livestream.locations.list`

`livestream.operations.get` `livestream.operations.list` `livestream.pools.get` `livestream.pools.listEffectiveTags` `livestream.pools.listTagBindings` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Live Stream Service Agent 

(`roles/livestream.serviceAgent`) Uploads media files to customer Cloud Storage buckets.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Live Stream permissions

Permission | Included in roles  
---|---  
  
#### `livestream.assets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.assets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.assets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.assets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.channels.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.channels.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.channels.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.channels.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.channels.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.channels.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.channels.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.channels.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.channels.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.channels.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.channels.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.clips.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.clips.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.clips.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.clips.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.dvrSessions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.dvrSessions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.dvrSessions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.dvrSessions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.dvrSessions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.events.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.events.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.events.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.events.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.inputs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.inputs.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.inputs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.inputs.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.inputs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.inputs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.inputs.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.inputs.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.inputs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
#### `livestream.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.pools.createTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.pools.deleteTagBinding`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)   
  
#### `livestream.pools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.pools.listEffectiveTags`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.pools.listTagBindings`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)  [Live Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.viewer) (`roles/livestream.viewer`)  [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`)  [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `livestream.pools.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Live Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.admin) (`roles/livestream.admin`)  [Live Stream Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/livestream#livestream.editor) (`roles/livestream.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
