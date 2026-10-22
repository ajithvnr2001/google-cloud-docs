---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization/
title: Route Optimization roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:04.801397+00:00
---

# Route Optimization roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Route Optimization roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Route Optimization. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Route Optimization roles

Role | Permissions  
---|---  
  
#### Routeoptimization Admin 

(`roles/routeoptimization.admin`) Admin role for routeoptimization  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `routeoptimization.*`

  * `routeoptimization.locations.use`
  * `routeoptimization.operations.create`
  * `routeoptimization.operations.get`

  
  
#### Route Optimization Editor 

(`roles/routeoptimization.editor`) This role can create long-running operations via BatchOptimizeTours.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `routeoptimization.*`

  * `routeoptimization.locations.use`
  * `routeoptimization.operations.create`
  * `routeoptimization.operations.get`

  
  
#### Route Optimization Viewer 

(`roles/routeoptimization.viewer`) This role can view any long-running Operations.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `routeoptimization.locations.use` `routeoptimization.operations.get`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Route Optimization Service Agent 

(`roles/routeoptimization.serviceAgent`) Grants Route Optimization Service Account access to read and write GCS objects in the host project.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `storage.buckets.get` `storage.objects.create` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Route Optimization permissions

Permission | Included in roles  
---|---  
  
#### `routeoptimization.locations.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Routeoptimization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.admin) (`roles/routeoptimization.admin`)  [Route Optimization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.editor) (`roles/routeoptimization.editor`)  [Route Optimization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.viewer) (`roles/routeoptimization.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `routeoptimization.operations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Routeoptimization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.admin) (`roles/routeoptimization.admin`)  [Route Optimization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.editor) (`roles/routeoptimization.editor`)   
  
#### `routeoptimization.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Routeoptimization Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.admin) (`roles/routeoptimization.admin`)  [Route Optimization Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.editor) (`roles/routeoptimization.editor`)  [Route Optimization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/routeoptimization#routeoptimization.viewer) (`roles/routeoptimization.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
