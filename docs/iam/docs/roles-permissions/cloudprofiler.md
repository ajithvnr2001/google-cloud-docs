---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler/
title: Cloud Profiler roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:27.449559+00:00
---

# Cloud Profiler roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Profiler roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Profiler. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Profiler roles

Role | Permissions  
---|---  
  
#### Cloud Profiler Admin 

(`roles/cloudprofiler.admin`) Admin role for Cloud Profiler  |  `cloudprofiler.*`

  * `cloudprofiler.profiles.create`
  * `cloudprofiler.profiles.list`
  * `cloudprofiler.profiles.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Profiler Viewer 

(`roles/cloudprofiler.viewer`) Viewer role for Cloud Profiler  |  `cloudprofiler.profiles.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Cloud Profiler Agent 

(`roles/cloudprofiler.agent`) Cloud Profiler agents are allowed to register and provide the profiling data.  |  `cloudprofiler.profiles.create` `cloudprofiler.profiles.update`  
  
#### Cloud Profiler User 

(`roles/cloudprofiler.user`) Cloud Profiler users are allowed to query and view the profiling data.  |  `cloudprofiler.profiles.list` `resourcemanager.projects.get` `resourcemanager.projects.list` `serviceusage.catalogs.listMembers` `serviceusage.consumerpolicy.analyze` `serviceusage.consumerpolicy.get` `serviceusage.effectivepolicy.get` `serviceusage.groups.*`

  * `serviceusage.groups.list`
  * `serviceusage.groups.listExpandedMembers`
  * `serviceusage.groups.listMembers`

`serviceusage.quotas.get` `serviceusage.services.get` `serviceusage.services.list` `serviceusage.services.listApis` `serviceusage.services.listDependentServices` `serviceusage.values.test`  
  
## Cloud Profiler permissions

Permission | Included in roles  
---|---  
  
#### `cloudprofiler.profiles.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Profiler Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.admin) (`roles/cloudprofiler.admin`)  [Cloud Profiler Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.agent) (`roles/cloudprofiler.agent`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)   
  
#### `cloudprofiler.profiles.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Profiler Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.admin) (`roles/cloudprofiler.admin`)  [Cloud Profiler Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.viewer) (`roles/cloudprofiler.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Cloud Profiler User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.user) (`roles/cloudprofiler.user`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `cloudprofiler.profiles.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Cloud Profiler Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.admin) (`roles/cloudprofiler.admin`)  [Cloud Profiler Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudprofiler#cloudprofiler.agent) (`roles/cloudprofiler.agent`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
