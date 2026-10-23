---
url: https://docs.cloud.google.com/profiler/docs/iam/
title: Control access with IAM \u00a0|\u00a0 Cloud Profiler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:25.681691+00:00
---

# Control access with IAM  |  Cloud Profiler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/profiler/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Profiler ](https://docs.cloud.google.com/profiler/docs)
  * [ Guides ](https://docs.cloud.google.com/profiler/docs/measure-app-performance)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Control access with IAM

Cloud Profiler controls access to profiling activities in Google Cloud projects by using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) roles and permissions.

**Note:** Cloud Profiler doesn't support [Workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation). You can't use Cloud Profiler in an environment that relies exclusively on Workload identity federation for authentication.

## Overview

To use Cloud Profiler for a Google Cloud project, you must have the appropriate IAM permissions on that project.

Permissions are not granted directly to users; permissions are instead granted indirectly through roles, which group permissions. For more information on these concepts, see the IAM documentation on [roles, permissions, and related concepts](https://docs.cloud.google.com/iam/docs/overview#concepts_related_to_access_management).

## Permissions and roles

This section summarizes the permissions and roles that apply to Profiler.

### Permissions

The following table lists the permissions required for profiling activities:

Activity | Required permissions  
---|---  
Create profiles | `cloudprofiler.profiles.create`  
List profiles | `cloudprofiler.profiles.list`  
Modify profiles | `cloudprofiler.profiles.update`  
  
### Roles

IAM roles include permissions and can be assigned to users, groups, and service accounts. The following table lists the roles for Profiler:

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
  
To learn how to assign Identity and Access Management roles to a user or service account, see [Managing Policies](https://docs.cloud.google.com/iam/docs/managing-policies).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
