---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/stream/
title: Stream roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:46.850852+00:00
---

# Stream roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/stream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Stream roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Stream. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Stream roles

Role | Permissions  
---|---  
  
#### Stream Admin 

(`roles/stream.admin`) Full access to Stream all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `stream.*`

  * `stream.locations.get`
  * `stream.locations.list`
  * `stream.operations.cancel`
  * `stream.operations.delete`
  * `stream.operations.get`
  * `stream.operations.list`
  * `stream.streamContents.build`
  * `stream.streamContents.create`
  * `stream.streamContents.delete`
  * `stream.streamContents.get`
  * `stream.streamContents.list`
  * `stream.streamContents.update`
  * `stream.streamInstances.create`
  * `stream.streamInstances.delete`
  * `stream.streamInstances.get`
  * `stream.streamInstances.list`
  * `stream.streamInstances.rollout`
  * `stream.streamInstances.update`

  
  
#### Stream Viewer 

(`roles/stream.viewer`) Read-only access to Stream all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `stream.locations.*`

  * `stream.locations.get`
  * `stream.locations.list`

`stream.operations.get` `stream.operations.list` `stream.streamContents.get` `stream.streamContents.list` `stream.streamInstances.get` `stream.streamInstances.list`  
  
#### Stream Content Admin 

(`roles/stream.contentAdmin`) Full access to all StreamContent resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `stream.streamContents.*`

  * `stream.streamContents.build`
  * `stream.streamContents.create`
  * `stream.streamContents.delete`
  * `stream.streamContents.get`
  * `stream.streamContents.list`
  * `stream.streamContents.update`

  
  
#### Stream Content Builder 

(`roles/stream.contentBuilder`) Read and build access to StreamContent resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `stream.streamContents.build` `stream.streamContents.get` `stream.streamContents.list`  
  
#### Stream Instance Admin 

(`roles/stream.instanceAdmin`) Full access to all StreamInstance resources and Read access to all StreamContent resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `stream.streamContents.get` `stream.streamContents.list` `stream.streamInstances.*`

  * `stream.streamInstances.create`
  * `stream.streamInstances.delete`
  * `stream.streamInstances.get`
  * `stream.streamInstances.list`
  * `stream.streamInstances.rollout`
  * `stream.streamInstances.update`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Stream Service Agent 

(`roles/stream.serviceAgent`) Gives Immersive Stream for XR access to the required resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.buckets.create` `storage.buckets.get` `storage.objects.create` `storage.objects.get` `storage.objects.list`  
  
## Stream permissions

Permission | Included in roles  
---|---  
  
#### `stream.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `stream.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `stream.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)   
  
#### `stream.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)   
  
#### `stream.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `stream.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `stream.streamContents.build`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)  [Stream Content Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentBuilder) (`roles/stream.contentBuilder`)   
  
#### `stream.streamContents.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)   
  
#### `stream.streamContents.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)   
  
#### `stream.streamContents.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)  [Stream Content Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentBuilder) (`roles/stream.contentBuilder`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamContents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)  [Stream Content Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentBuilder) (`roles/stream.contentBuilder`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamContents.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Content Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.contentAdmin) (`roles/stream.contentAdmin`)   
  
#### `stream.streamInstances.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamInstances.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamInstances.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamInstances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.viewer) (`roles/stream.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamInstances.rollout`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
#### `stream.streamInstances.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Stream Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.admin) (`roles/stream.admin`)  [Stream Instance Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/stream#stream.instanceAdmin) (`roles/stream.instanceAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
