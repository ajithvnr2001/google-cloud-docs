---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment/
title: Rapid Migration Assessment roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:54.622213+00:00
---

# Rapid Migration Assessment roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Rapid Migration Assessment roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Rapid Migration Assessment. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Rapid Migration Assessment roles

Role | Permissions  
---|---  
  
#### Rapid Migration Assessment Admin 

(`roles/rma.admin`) Full access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.*`

  * `rma.annotations.create`
  * `rma.annotations.get`
  * `rma.collectors.create`
  * `rma.collectors.delete`
  * `rma.collectors.get`
  * `rma.collectors.list`
  * `rma.collectors.update`
  * `rma.locations.get`
  * `rma.locations.list`
  * `rma.operations.cancel`
  * `rma.operations.delete`
  * `rma.operations.get`
  * `rma.operations.list`

  
  
#### Rapid Migration Assessment Viewer 

(`roles/rma.viewer`) Read-only access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list`  
  
#### Rapid Migration Assessment Runner 

(`roles/rma.runner`) Update and Read access to Rapid Migration Assessment all resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `rma.annotations.get` `rma.collectors.get` `rma.collectors.list` `rma.collectors.update` `rma.locations.*`

  * `rma.locations.get`
  * `rma.locations.list`

`rma.operations.get` `rma.operations.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### RMA Service Agent 

(`roles/rapidmigrationassessment.serviceAgent`) Gives RMA service account access to MC resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `autoscaling.sites.writeMetrics` `cloudasset.assets.exportResource` `cloudasset.feeds.create` `logging.logEntries.create` `migrationcenter.assets.list` `migrationcenter.assets.reportFrames` `migrationcenter.importJobs.get` `migrationcenter.importJobs.list` `migrationcenter.sources.*`

  * `migrationcenter.sources.create`
  * `migrationcenter.sources.delete`
  * `migrationcenter.sources.get`
  * `migrationcenter.sources.list`
  * `migrationcenter.sources.update`

`monitoring.metricDescriptors.create` `monitoring.metricDescriptors.list` `monitoring.timeSeries.create` `resourcemanager.projects.get`  
  
## Rapid Migration Assessment permissions

Permission | Included in roles  
---|---  
  
#### `rma.annotations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)   
  
#### `rma.annotations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.collectors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)   
  
#### `rma.collectors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)   
  
#### `rma.collectors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.collectors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.collectors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)   
  
#### `rma.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)   
  
#### `rma.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
#### `rma.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Migration Center Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.admin) (`roles/migrationcenter.admin`)  [Migration Center Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/migrationcenter#migrationcenter.viewer) (`roles/migrationcenter.viewer`)  [Rapid Migration Assessment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.admin) (`roles/rma.admin`)  [Rapid Migration Assessment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.viewer) (`roles/rma.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Rapid Migration Assessment Runner](https://docs.cloud.google.com/iam/docs/roles-permissions/rapidmigrationassessment#rma.runner) (`roles/rma.runner`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
