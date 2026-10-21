---
url: https://docs.cloud.google.com/managed-spark/docs/managed-spark-regulatory-compliance/
title: Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:53.839417+00:00
---

# Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/managed-spark-regulatory-compliance/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Resources ](https://docs.cloud.google.com/managed-spark/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Managed Service for Apache Spark that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Managed Service for Apache Spark APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
dataproc.googleapis.com | v1 |  SUPPORTED   
dataproc.googleapis.com | v1beta2 |  SUPPORTED   
  
### Compliance supported regions

Managed Service for Apache Spark is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-central2
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: dataproc.googleapis.com/Batch

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/batches` RPC methods:

  * `google.cloud.dataproc.v1.BatchController.CreateBatch`

| 

  * `batch.pysparkBatch.args`
  * `batch.rayBatch.args`
  * `batch.sparkBatch.args`
  * `batch.sparkRBatch.args`
  * `batch.sparkSqlBatch.queryVariables.key`
  * `batch.sparkSqlBatch.queryVariables.value`

  
  
#### Resource: dataproc.googleapis.com/Job

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `dataproc.googleapis.com` REST API: `PATCH` `/v1/projects/{project_id}/regions/{region}/jobs/{job_id}` RPC methods:

  * `google.cloud.dataproc.v1.JobController.UpdateJob`

| 

  * `job.flinkJob.args`
  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pyflinkJob.args`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`
  * `job.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `PATCH` `/v1beta2/projects/{project_id}/regions/{region}/jobs/{job_id}` RPC methods:

  * `google.cloud.dataproc.v1beta2.JobController.UpdateJob`

| 

  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/projects/{project_id}/regions/{region}/jobs:submit` RPC methods:

  * `google.cloud.dataproc.v1.JobController.SubmitJob`

| 

  * `job.flinkJob.args`
  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pyflinkJob.args`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`
  * `job.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/projects/{project_id}/regions/{region}/jobs:submitAsOperation` RPC methods:

  * `google.cloud.dataproc.v1.JobController.SubmitJobAsOperation`

| 

  * `job.flinkJob.args`
  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pyflinkJob.args`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`
  * `job.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/projects/{project_id}/regions/{region}/jobs:submit` RPC methods:

  * `google.cloud.dataproc.v1beta2.JobController.SubmitJob`

| 

  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/projects/{project_id}/regions/{region}/jobs:submitAsOperation` RPC methods:

  * `google.cloud.dataproc.v1beta2.JobController.SubmitJobAsOperation`

| 

  * `job.hadoopJob.args`
  * `job.hiveJob.queryList.queries`
  * `job.hiveJob.scriptVariables.key`
  * `job.hiveJob.scriptVariables.value`
  * `job.pigJob.queryList.queries`
  * `job.pigJob.scriptVariables.key`
  * `job.pigJob.scriptVariables.value`
  * `job.prestoJob.queryList.queries`
  * `job.pysparkJob.args`
  * `job.sparkJob.args`
  * `job.sparkRJob.args`
  * `job.sparkSqlJob.queryList.queries`
  * `job.sparkSqlJob.scriptVariables.key`
  * `job.sparkSqlJob.scriptVariables.value`

  
  
#### Resource: dataproc.googleapis.com/WorkflowTemplate

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/workflowTemplates` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/locations/*}/workflowTemplates:instantiateInline` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/regions/*}/workflowTemplates` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.CreateWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/regions/*}/workflowTemplates:instantiateInline` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/{parent=projects/*/locations/*}/workflowTemplates` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.CreateWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/{parent=projects/*/locations/*}/workflowTemplates:instantiateInline` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/{parent=projects/*/regions/*}/workflowTemplates` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.CreateWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `POST` `/v1beta2/{parent=projects/*/regions/*}/workflowTemplates:instantiateInline` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.InstantiateInlineWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `PUT` `/v1/{template.name=projects/*/locations/*/workflowTemplates/*}` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.UpdateWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `PUT` `/v1/{template.name=projects/*/regions/*/workflowTemplates/*}` RPC methods:

  * `google.cloud.dataproc.v1.WorkflowTemplateService.UpdateWorkflowTemplate`

| 

  * `template.jobs.flinkJob.args`
  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pyflinkJob.args`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`
  * `template.jobs.trinoJob.queryList.queries`

  
Service: `dataproc.googleapis.com` REST API: `PUT` `/v1beta2/{template.name=projects/*/locations/*/workflowTemplates/*}` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.UpdateWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
Service: `dataproc.googleapis.com` REST API: `PUT` `/v1beta2/{template.name=projects/*/regions/*/workflowTemplates/*}` RPC methods:

  * `google.cloud.dataproc.v1beta2.WorkflowTemplateService.UpdateWorkflowTemplate`

| 

  * `template.jobs.hadoopJob.args`
  * `template.jobs.hiveJob.queryList.queries`
  * `template.jobs.hiveJob.scriptVariables.key`
  * `template.jobs.hiveJob.scriptVariables.value`
  * `template.jobs.pigJob.queryList.queries`
  * `template.jobs.pigJob.scriptVariables.key`
  * `template.jobs.pigJob.scriptVariables.value`
  * `template.jobs.prestoJob.queryList.queries`
  * `template.jobs.pysparkJob.args`
  * `template.jobs.sparkJob.args`
  * `template.jobs.sparkRJob.args`
  * `template.jobs.sparkSqlJob.queryList.queries`
  * `template.jobs.sparkSqlJob.scriptVariables.key`
  * `template.jobs.sparkSqlJob.scriptVariables.value`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Cluster identification | 

  * `cluster`
  * `clusterName`
  * `clusterUuid`

  
Job identification | 

  * `job`
  * `jobId`
  * `yarnApplicationId`
  * `yarnApplicationIds`

  
Job specific configurations | 

  * `job.flinkJob.jarFileUris`
  * `job.hadoopJob.fileUris`
  * `job.pigJob.queryFileUri`
  * `job.pyflinkJob.pythonFileUris`
  * `job.pysparkJob.fileUris`
  * `job.sparkSqlJob.queryFileUri`

  
Location identification | 

  * `region`

  
Network and connectivity | 

  * `cluster.config.gceClusterConfig.networkUri`
  * `cluster.config.gceClusterConfig.nodeGroupAffinity.nodeGroupUri`
  * `cluster.config.gceClusterConfig.subnetworkUri`

  
Project identification | 

  * `project`
  * `projectId`

  
Resource configuration - compute | 

  * `cluster.config.auxiliaryNodeGroups.nodeGroup.nodeGroupConfig.machineTypeUri`
  * `cluster.config.masterConfig.machineTypeUri`
  * `cluster.config.masterConfig.minCpuPlatform`
  * `cluster.config.secondaryWorkerConfig.machineTypeUri`
  * `cluster.config.workerConfig.machineTypeUri`
  * `cluster.config.workerConfig.minCpuPlatform`

  
Resource configuration - storage | 

  * `cluster.config.auxiliaryNodeGroups.nodeGroup.nodeGroupConfig.diskConfig.bootDiskType`
  * `cluster.config.masterConfig.diskConfig.bootDiskType`
  * `cluster.config.masterConfig.diskConfig.localSsdInterface`
  * `cluster.config.secondaryWorkerConfig.diskConfig.bootDiskType`
  * `cluster.config.workerConfig.diskConfig.bootDiskType`
  * `cluster.config.workerConfig.diskConfig.localSsdInterface`

  
Security configuration - encryption | 

  * `cluster.config.encryptionConfig.gcePdKmsKeyName`
  * `cluster.config.encryptionConfig.kmsKey`

  
Security configuration - kerberos | 

  * `cluster.config.securityConfig.kerberosConfig.kdcDbKeyUri`
  * `cluster.config.securityConfig.kerberosConfig.keyPasswordUri`
  * `cluster.config.securityConfig.kerberosConfig.keystoreUri`
  * `cluster.config.securityConfig.kerberosConfig.kmsKeyUri`
  * `cluster.config.securityConfig.kerberosConfig.rootPrincipalPasswordUri`
  * `cluster.config.securityConfig.kerberosConfig.truststoreUri`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
