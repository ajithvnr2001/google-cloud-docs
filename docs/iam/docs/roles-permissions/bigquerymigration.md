---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration/
title: BigQuery Migration API roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:37.161868+00:00
---

# BigQuery Migration API roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  BigQuery Migration API roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for BigQuery Migration API. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## BigQuery Migration API roles

Role | Permissions  
---|---  
  
#### Bigquerymigration Admin 

(`roles/bigquerymigration.admin`) Admin role for bigquerymigration  |  `bigquerymigration.*`

  * `bigquerymigration.subtasks.get`
  * `bigquerymigration.subtasks.list`
  * `bigquerymigration.translation.translate`
  * `bigquerymigration.workflows.create`
  * `bigquerymigration.workflows.delete`
  * `bigquerymigration.workflows.enableAiOutputTypes`
  * `bigquerymigration.workflows.enableLineageOutputTypes`
  * `bigquerymigration.workflows.enableOutputTypePermissions`
  * `bigquerymigration.workflows.get`
  * `bigquerymigration.workflows.list`
  * `bigquerymigration.workflows.orchestrateTask`
  * `bigquerymigration.workflows.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### MigrationWorkflow Editor 

(`roles/bigquerymigration.editor`) Editor of EDW migration workflows.  |  `bigquerymigration.subtasks.*`

  * `bigquerymigration.subtasks.get`
  * `bigquerymigration.subtasks.list`

`bigquerymigration.workflows.create` `bigquerymigration.workflows.delete` `bigquerymigration.workflows.enableAiOutputTypes` `bigquerymigration.workflows.enableLineageOutputTypes` `bigquerymigration.workflows.enableOutputTypePermissions` `bigquerymigration.workflows.get` `bigquerymigration.workflows.list` `bigquerymigration.workflows.update`  
  
#### MigrationWorkflow Viewer 

(`roles/bigquerymigration.viewer`) Viewer of EDW migration MigrationWorkflow.  |  `bigquerymigration.subtasks.*`

  * `bigquerymigration.subtasks.get`
  * `bigquerymigration.subtasks.list`

`bigquerymigration.workflows.get` `bigquerymigration.workflows.list`  
  
#### Migration Management Editor Beta

(`roles/bigquerymigration.migrationEditor`) Admin of EDW migrations.  |   
  
#### Migration Management Viewer Beta

(`roles/bigquerymigration.migrationViewer`) Viewer of EDW migrations.  |   
  
#### Task Orchestrator 

(`roles/bigquerymigration.orchestrator`) Orchestrator of EDW migration tasks.  |  `bigquerymigration.workflows.orchestrateTask` `storage.objects.list`  
  
#### Migration Translation User 

(`roles/bigquerymigration.translationUser`) User of EDW migration interactive SQL translation service.  |  `bigquerymigration.translation.translate`  
  
#### Task Worker 

(`roles/bigquerymigration.worker`) Worker that executes EDW migration subtasks.  |  `storage.objects.create` `storage.objects.get` `storage.objects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### BigQuery Migration Service Agent 

(`roles/bigquerymigration.serviceAgent`) Access required for the BigQuery Migration Service to perform data discovery, metadata registration, and manage data transfers.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `resourcemanager.projects.get`  
  
## BigQuery Migration API permissions

Permission | Included in roles  
---|---  
  
#### `bigquerymigration.subtasks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)  [MigrationWorkflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.viewer) (`roles/bigquerymigration.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `bigquerymigration.subtasks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)  [MigrationWorkflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.viewer) (`roles/bigquerymigration.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `bigquerymigration.translation.translate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [Migration Translation User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.translationUser) (`roles/bigquerymigration.translationUser`)  [DLP Organization Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.orgdriver) (`roles/dlp.orgdriver`)  [DLP Project Data Profiles Driver](https://docs.cloud.google.com/iam/docs/roles-permissions/dlp#dlp.projectdriver) (`roles/dlp.projectdriver`)  [Databases Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.databasesAdmin) (`roles/iam.databasesAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Dataflow Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataflow#dataflow.serviceAgent) (`roles/dataflow.serviceAgent`) 
  * [Cloud Dataplex Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.serviceAgent) (`roles/dataplex.serviceAgent`) 
  * [Dataprep Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprep#dataprep.serviceAgent) (`roles/dataprep.serviceAgent`) 

  
  
#### `bigquerymigration.workflows.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
#### `bigquerymigration.workflows.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
#### `bigquerymigration.workflows.enableAiOutputTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
#### `bigquerymigration.workflows.enableLineageOutputTypes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
#### `bigquerymigration.workflows.enableOutputTypePermissions`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
#### `bigquerymigration.workflows.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)  [MigrationWorkflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.viewer) (`roles/bigquerymigration.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `bigquerymigration.workflows.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)  [MigrationWorkflow Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.viewer) (`roles/bigquerymigration.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `bigquerymigration.workflows.orchestrateTask`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [Task Orchestrator](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.orchestrator) (`roles/bigquerymigration.orchestrator`)   
  
#### `bigquerymigration.workflows.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Bigquerymigration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.admin) (`roles/bigquerymigration.admin`)  [MigrationWorkflow Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquerymigration#bigquerymigration.editor) (`roles/bigquerymigration.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
