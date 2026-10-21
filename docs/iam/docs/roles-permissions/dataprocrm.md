---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm/
title: Managed Service for Apache Spark Resource Manager roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:02:35.951655+00:00
---

# Managed Service for Apache Spark Resource Manager roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Managed Service for Apache Spark Resource Manager roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Managed Service for Apache Spark Resource Manager. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Managed Service for Apache Spark Resource Manager roles

Role | Permissions  
---|---  
  
#### Dataproc Resource Manager Admin Beta

(`roles/dataprocrm.admin`) Grants full access to all Dataproc Resource Manager resources. Intended for users that need to create and delete any Dataproc Resource Manager resources.  |  `dataprocrm.*`

  * `dataprocrm.locations.get`
  * `dataprocrm.locations.list`
  * `dataprocrm.nodePools.create`
  * `dataprocrm.nodePools.delete`
  * `dataprocrm.nodePools.deleteNodes`
  * `dataprocrm.nodePools.get`
  * `dataprocrm.nodePools.list`
  * `dataprocrm.nodePools.resize`
  * `dataprocrm.nodes.get`
  * `dataprocrm.nodes.heartbeat`
  * `dataprocrm.nodes.list`
  * `dataprocrm.nodes.mintOAuthToken`
  * `dataprocrm.nodes.update`
  * `dataprocrm.operations.cancel`
  * `dataprocrm.operations.delete`
  * `dataprocrm.operations.get`
  * `dataprocrm.operations.list`
  * `dataprocrm.workloads.cancel`
  * `dataprocrm.workloads.create`
  * `dataprocrm.workloads.delete`
  * `dataprocrm.workloads.get`
  * `dataprocrm.workloads.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Dataproc Resource Manager Viewer Beta

(`roles/dataprocrm.viewer`) Grants read access to all Dataproc Resource Manager resources. Intended for users that need read-only access to Dataproc Resource Manager resources.  |  `dataprocrm.locations.*`

  * `dataprocrm.locations.get`
  * `dataprocrm.locations.list`

`dataprocrm.nodePools.get` `dataprocrm.nodePools.list` `dataprocrm.nodes.get` `dataprocrm.nodes.list` `dataprocrm.nodes.mintOAuthToken` `dataprocrm.operations.get` `dataprocrm.operations.list` `dataprocrm.workloads.get` `dataprocrm.workloads.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Dataproc Resource Manager Node Service Agent 

(`roles/dataprocrm.nodeServiceAgent`) Dataproc Resource Manager Node Service Agent used to run managed resources in user project with restricted permissions.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `dataprocrm.nodes.get` `dataprocrm.nodes.heartbeat` `dataprocrm.nodes.mintOAuthToken` `logging.logEntries.create` `logging.logEntries.route` `monitoring.metricDescriptors.create` `monitoring.metricDescriptors.get` `monitoring.metricDescriptors.list` `monitoring.monitoredResourceDescriptors.*`

  * `monitoring.monitoredResourceDescriptors.get`
  * `monitoring.monitoredResourceDescriptors.list`

`monitoring.timeSeries.create` `serviceusage.services.use`  
  
## Managed Service for Apache Spark Resource Manager permissions

Permission | Included in roles  
---|---  
  
#### `dataprocrm.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocrm.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `dataprocrm.nodePools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodePools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodePools.deleteNodes`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodePools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodePools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodePools.resize`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dataproc Resource Manager Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent) (`roles/dataprocrm.nodeServiceAgent`) 

  
  
#### `dataprocrm.nodes.heartbeat`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dataproc Resource Manager Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent) (`roles/dataprocrm.nodeServiceAgent`) 

  
  
#### `dataprocrm.nodes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.nodes.mintOAuthToken`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 
  * [Dataproc Resource Manager Node Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.nodeServiceAgent) (`roles/dataprocrm.nodeServiceAgent`) 

  
  
#### `dataprocrm.nodes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)   
  
#### `dataprocrm.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Dataproc Serverless Node.](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessNode) (`roles/dataproc.serverlessNode`)  [Dataproc Worker](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.worker) (`roles/dataproc.worker`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.workloads.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.workloads.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.workloads.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.workloads.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
#### `dataprocrm.workloads.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [BigQuery Studio Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioAdmin) (`roles/bigquery.studioAdmin`)  [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)  [Dataproc Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.admin) (`roles/dataproc.admin`)  [Dataproc Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.editor) (`roles/dataproc.editor`)  [Dataproc Resource Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.admin) (`roles/dataprocrm.admin`)  [Dataproc Resource Manager Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataprocrm#dataprocrm.viewer) (`roles/dataprocrm.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Dataproc Serverless Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)  [Data Scientist](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.dataScientist) (`roles/iam.dataScientist`)  [ML Engineer](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.mlEngineer) (`roles/iam.mlEngineer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) 
  * [Dataproc Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) (`roles/dataproc.serviceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
