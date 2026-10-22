---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/source/
title: Cloud Source Repositories roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:54.182690+00:00
---

# Cloud Source Repositories roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/source/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Cloud Source Repositories roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Cloud Source Repositories. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Cloud Source Repositories roles

Role | Permissions  
---|---  
  
#### Source Repository Administrator 

(`roles/source.admin`) Provides permissions to create, update, delete, list, clone, fetch, and browse repositories. Also provides permissions to read and change IAM policies.  Lowest-level resources where you can grant this role:

  * Repository 

|  `source.*`

  * `source.repos.create`
  * `source.repos.delete`
  * `source.repos.get`
  * `source.repos.getIamPolicy`
  * `source.repos.getProjectConfig`
  * `source.repos.list`
  * `source.repos.setIamPolicy`
  * `source.repos.update`
  * `source.repos.updateProjectConfig`
  * `source.repos.updateRepoConfig`

  
  
#### Source Repository Editor 

(`roles/source.editor`) Editor role for Source Repository  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `source.repos.get` `source.repos.getIamPolicy` `source.repos.list` `source.repos.update`  
  
#### Source Repository Viewer 

(`roles/source.viewer`) Viewer role for Source Repository  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `source.repos.get` `source.repos.getIamPolicy` `source.repos.list`  
  
#### Source Repository Reader 

(`roles/source.reader`) Provides permissions to list, clone, fetch, and browse repositories.  Lowest-level resources where you can grant this role:

  * Repository 

|  `source.repos.get` `source.repos.list`  
  
#### Source Repository Writer 

(`roles/source.writer`) Provides permissions to list, clone, fetch, browse, and update repositories.  Lowest-level resources where you can grant this role:

  * Repository 

|  `source.repos.get` `source.repos.list` `source.repos.update`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Cloud Source Repositories Service Agent 

(`roles/sourcerepo.serviceAgent`) Allow Cloud Source Repositories to integrate with other Cloud services.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `iam.serviceAccounts.getAccessToken` `pubsub.topics.publish`  
  
## Cloud Source Repositories permissions

Permission | Included in roles  
---|---  
  
#### `source.repos.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Deployment Manager Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/deploymentmanager#clouddeploymentmanager.serviceAgent) (`roles/clouddeploymentmanager.serviceAgent`) 

  
  
#### `source.repos.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `source.repos.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Source Repository Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.editor) (`roles/source.editor`)  [Source Repository Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.viewer) (`roles/source.viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Source Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.reader) (`roles/source.reader`)  [Source Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.writer) (`roles/source.writer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 
  * [Endpoints Portal Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/endpointsportal#endpointsportal.serviceAgent) (`roles/endpointsportal.serviceAgent`) 

  
  
#### `source.repos.getIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Source Repository Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.editor) (`roles/source.editor`)  [Source Repository Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.viewer) (`roles/source.viewer`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `source.repos.getProjectConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `source.repos.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Source Repository Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.editor) (`roles/source.editor`)  [Source Repository Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.viewer) (`roles/source.viewer`)  [Telco Automation Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/telcoautomation#telcoautomation.admin) (`roles/telcoautomation.admin`)  [Composer Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/composer#composer.worker) (`roles/composer.worker`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Source Repository Reader](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.reader) (`roles/source.reader`)  [Source Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.writer) (`roles/source.writer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Build Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.serviceAgent) (`roles/cloudbuild.serviceAgent`) 
  * [(Deprecated) Cloud Functions Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.serviceAgent) (`roles/cloudfunctions.serviceAgent`) 

  
  
#### `source.repos.setIamPolicy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `source.repos.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Source Repository Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.editor) (`roles/source.editor`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)  [Source Repository Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.writer) (`roles/source.writer`)   
  
#### `source.repos.updateProjectConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
#### `source.repos.updateRepoConfig`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Source Repository Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/source#source.admin) (`roles/source.admin`)  [Dev Ops](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.devOps) (`roles/iam.devOps`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
