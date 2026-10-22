---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph/
title: Enterprise Knowledge Graph roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:21.773752+00:00
---

# Enterprise Knowledge Graph roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Enterprise Knowledge Graph roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Enterprise Knowledge Graph. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Enterprise Knowledge Graph roles

Role | Permissions  
---|---  
  
#### Enterprise Knowledge Graph Admin Beta

(`roles/enterpriseknowledgegraph.admin`) Administrator of Enterprise Knowledge Graph resources  |  `enterpriseknowledgegraph.*`

  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.search`
  * `enterpriseknowledgegraph.entityReconciliationJobs.cancel`
  * `enterpriseknowledgegraph.entityReconciliationJobs.create`
  * `enterpriseknowledgegraph.entityReconciliationJobs.delete`
  * `enterpriseknowledgegraph.entityReconciliationJobs.get`
  * `enterpriseknowledgegraph.entityReconciliationJobs.list`
  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.search`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Enterprise Knowledge Graph Editor Beta

(`roles/enterpriseknowledgegraph.editor`) Editor of Enterprise Knowledge Graph resources  |  `enterpriseknowledgegraph.*`

  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.search`
  * `enterpriseknowledgegraph.entityReconciliationJobs.cancel`
  * `enterpriseknowledgegraph.entityReconciliationJobs.create`
  * `enterpriseknowledgegraph.entityReconciliationJobs.delete`
  * `enterpriseknowledgegraph.entityReconciliationJobs.get`
  * `enterpriseknowledgegraph.entityReconciliationJobs.list`
  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.search`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Enterprise Knowledge Graph Viewer Beta

(`roles/enterpriseknowledgegraph.viewer`) Viewer of Enterprise Knowledge Graph resources  |  `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.*`

  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.search`

`enterpriseknowledgegraph.entityReconciliationJobs.get` `enterpriseknowledgegraph.entityReconciliationJobs.list` `enterpriseknowledgegraph.publicKnowledgeGraphEntities.*`

  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.lookup`
  * `enterpriseknowledgegraph.publicKnowledgeGraphEntities.search`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Enterprise Knowledge Graph Service Agent 

(`roles/enterpriseknowledgegraph.serviceAgent`) Gives Enterprise Knowledge Graph Service Account access to consumer resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `bigquery.config.get` `bigquery.datasets.create` `bigquery.datasets.get` `bigquery.jobs.create` `bigquery.readsessions.create` `bigquery.readsessions.getData` `bigquery.tables.create` `bigquery.tables.get` `bigquery.tables.getData` `bigquery.tables.list` `bigquery.tables.update` `bigquery.tables.updateData` `cloudaicompanion.topics.create` `dataform.folders.create` `dataform.locations.*`

  * `dataform.locations.get`
  * `dataform.locations.list`

`dataform.repositories.create` `dataform.repositories.list` `geminidataanalytics.locations.chat` `resourcemanager.projects.get` `resourcemanager.projects.list` `storage.objects.get` `storage.objects.list`  
  
## Enterprise Knowledge Graph permissions

Permission | Included in roles  
---|---  
  
#### `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.lookup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterpriseknowledgegraph.cloudKnowledgeGraphEntities.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterpriseknowledgegraph.entityReconciliationJobs.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)   
  
#### `enterpriseknowledgegraph.entityReconciliationJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)   
  
#### `enterpriseknowledgegraph.entityReconciliationJobs.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)   
  
#### `enterpriseknowledgegraph.entityReconciliationJobs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterpriseknowledgegraph.entityReconciliationJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterpriseknowledgegraph.publicKnowledgeGraphEntities.lookup`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `enterpriseknowledgegraph.publicKnowledgeGraphEntities.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Enterprise Knowledge Graph Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.admin) (`roles/enterpriseknowledgegraph.admin`)  [Enterprise Knowledge Graph Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.editor) (`roles/enterpriseknowledgegraph.editor`)  [Enterprise Knowledge Graph Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/enterpriseknowledgegraph#enterpriseknowledgegraph.viewer) (`roles/enterpriseknowledgegraph.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
