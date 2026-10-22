---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai/
title: Document AI roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:32.712799+00:00
---

# Document AI roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Document AI roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Document AI. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Document AI roles

Role | Permissions  
---|---  
  
#### Document AI Administrator Beta

(`roles/documentai.admin`) Grants full access to all resources in Document AI  |  `documentai.*`

  * `documentai.dataLabelingJobs.cancel`
  * `documentai.dataLabelingJobs.create`
  * `documentai.dataLabelingJobs.list`
  * `documentai.datasetSchemas.get`
  * `documentai.datasetSchemas.update`
  * `documentai.datasets.createDocuments`
  * `documentai.datasets.deleteDocuments`
  * `documentai.datasets.get`
  * `documentai.datasets.getDocuments`
  * `documentai.datasets.listDocuments`
  * `documentai.datasets.update`
  * `documentai.datasets.updateDocuments`
  * `documentai.evaluationDocuments.get`
  * `documentai.evaluations.create`
  * `documentai.evaluations.get`
  * `documentai.evaluations.list`
  * `documentai.humanReviewConfigs.get`
  * `documentai.humanReviewConfigs.review`
  * `documentai.humanReviewConfigs.update`
  * `documentai.labelerPools.create`
  * `documentai.labelerPools.delete`
  * `documentai.labelerPools.get`
  * `documentai.labelerPools.list`
  * `documentai.locations.get`
  * `documentai.locations.list`
  * `documentai.operations.getLegacy`
  * `documentai.processedDocumentsSets.get`
  * `documentai.processedDocumentsSets.getDocuments`
  * `documentai.processedDocumentsSets.listDocuments`
  * `documentai.processorTypes.get`
  * `documentai.processorTypes.list`
  * `documentai.processorVersions.create`
  * `documentai.processorVersions.delete`
  * `documentai.processorVersions.get`
  * `documentai.processorVersions.list`
  * `documentai.processorVersions.processBatch`
  * `documentai.processorVersions.processOnline`
  * `documentai.processorVersions.update`
  * `documentai.processors.create`
  * `documentai.processors.delete`
  * `documentai.processors.fetchHumanReviewDetails`
  * `documentai.processors.get`
  * `documentai.processors.list`
  * `documentai.processors.processBatch`
  * `documentai.processors.processOnline`
  * `documentai.processors.update`
  * `documentai.rules.create`
  * `documentai.rules.delete`
  * `documentai.rules.generate`
  * `documentai.rules.get`
  * `documentai.rules.list`
  * `documentai.rules.update`
  * `documentai.schemaVersions.create`
  * `documentai.schemaVersions.delete`
  * `documentai.schemaVersions.get`
  * `documentai.schemaVersions.list`
  * `documentai.schemaVersions.update`
  * `documentai.schemas.create`
  * `documentai.schemas.delete`
  * `documentai.schemas.get`
  * `documentai.schemas.list`
  * `documentai.schemas.update`
  * `documentai.validators.create`
  * `documentai.validators.delete`
  * `documentai.validators.get`
  * `documentai.validators.list`
  * `documentai.validators.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Document AI Editor Beta

(`roles/documentai.editor`) Grants access to use all resources in Document AI  |  `documentai.*`

  * `documentai.dataLabelingJobs.cancel`
  * `documentai.dataLabelingJobs.create`
  * `documentai.dataLabelingJobs.list`
  * `documentai.datasetSchemas.get`
  * `documentai.datasetSchemas.update`
  * `documentai.datasets.createDocuments`
  * `documentai.datasets.deleteDocuments`
  * `documentai.datasets.get`
  * `documentai.datasets.getDocuments`
  * `documentai.datasets.listDocuments`
  * `documentai.datasets.update`
  * `documentai.datasets.updateDocuments`
  * `documentai.evaluationDocuments.get`
  * `documentai.evaluations.create`
  * `documentai.evaluations.get`
  * `documentai.evaluations.list`
  * `documentai.humanReviewConfigs.get`
  * `documentai.humanReviewConfigs.review`
  * `documentai.humanReviewConfigs.update`
  * `documentai.labelerPools.create`
  * `documentai.labelerPools.delete`
  * `documentai.labelerPools.get`
  * `documentai.labelerPools.list`
  * `documentai.locations.get`
  * `documentai.locations.list`
  * `documentai.operations.getLegacy`
  * `documentai.processedDocumentsSets.get`
  * `documentai.processedDocumentsSets.getDocuments`
  * `documentai.processedDocumentsSets.listDocuments`
  * `documentai.processorTypes.get`
  * `documentai.processorTypes.list`
  * `documentai.processorVersions.create`
  * `documentai.processorVersions.delete`
  * `documentai.processorVersions.get`
  * `documentai.processorVersions.list`
  * `documentai.processorVersions.processBatch`
  * `documentai.processorVersions.processOnline`
  * `documentai.processorVersions.update`
  * `documentai.processors.create`
  * `documentai.processors.delete`
  * `documentai.processors.fetchHumanReviewDetails`
  * `documentai.processors.get`
  * `documentai.processors.list`
  * `documentai.processors.processBatch`
  * `documentai.processors.processOnline`
  * `documentai.processors.update`
  * `documentai.rules.create`
  * `documentai.rules.delete`
  * `documentai.rules.generate`
  * `documentai.rules.get`
  * `documentai.rules.list`
  * `documentai.rules.update`
  * `documentai.schemaVersions.create`
  * `documentai.schemaVersions.delete`
  * `documentai.schemaVersions.get`
  * `documentai.schemaVersions.list`
  * `documentai.schemaVersions.update`
  * `documentai.schemas.create`
  * `documentai.schemas.delete`
  * `documentai.schemas.get`
  * `documentai.schemas.list`
  * `documentai.schemas.update`
  * `documentai.validators.create`
  * `documentai.validators.delete`
  * `documentai.validators.get`
  * `documentai.validators.list`
  * `documentai.validators.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Document AI Viewer Beta

(`roles/documentai.viewer`) Grants access to view all resources and process documents in Document AI  |  `documentai.dataLabelingJobs.list` `documentai.datasetSchemas.get` `documentai.datasets.get` `documentai.datasets.getDocuments` `documentai.datasets.listDocuments` `documentai.evaluationDocuments.get` `documentai.evaluations.get` `documentai.evaluations.list` `documentai.humanReviewConfigs.get` `documentai.humanReviewConfigs.review` `documentai.labelerPools.get` `documentai.labelerPools.list` `documentai.locations.*`

  * `documentai.locations.get`
  * `documentai.locations.list`

`documentai.operations.getLegacy` `documentai.processedDocumentsSets.*`

  * `documentai.processedDocumentsSets.get`
  * `documentai.processedDocumentsSets.getDocuments`
  * `documentai.processedDocumentsSets.listDocuments`

`documentai.processorTypes.*`

  * `documentai.processorTypes.get`
  * `documentai.processorTypes.list`

`documentai.processorVersions.get` `documentai.processorVersions.list` `documentai.processorVersions.processBatch` `documentai.processorVersions.processOnline` `documentai.processors.fetchHumanReviewDetails` `documentai.processors.get` `documentai.processors.list` `documentai.processors.processBatch` `documentai.processors.processOnline` `documentai.rules.get` `documentai.rules.list` `documentai.schemaVersions.get` `documentai.schemaVersions.list` `documentai.schemas.get` `documentai.schemas.list` `documentai.validators.get` `documentai.validators.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Document AI API User Beta

(`roles/documentai.apiUser`) Grants access to process documents in Document AI  |  `documentai.humanReviewConfigs.review` `documentai.operations.getLegacy` `documentai.processorVersions.processBatch` `documentai.processorVersions.processOnline` `documentai.processors.processBatch` `documentai.processors.processOnline`  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### DocumentAI Core Service Agent 

(`roles/documentaicore.serviceAgent`) Gives DocumentAI Core Service Account access to consumer resources.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `automl.models.predict` `documentai.humanReviewConfigs.review` `storage.buckets.get` `storage.objects.create` `storage.objects.delete` `storage.objects.get` `storage.objects.list` `storage.objects.update`  
  
## Document AI permissions

Permission | Included in roles  
---|---  
  
#### `documentai.dataLabelingJobs.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.dataLabelingJobs.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.dataLabelingJobs.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.datasetSchemas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.datasetSchemas.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.datasets.createDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 

  
  
#### `documentai.datasets.deleteDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.datasets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.datasets.getDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.datasets.listDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.datasets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.datasets.updateDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.evaluationDocuments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.evaluations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.evaluations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.evaluations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.humanReviewConfigs.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.humanReviewConfigs.review`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [DocumentAI Core Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentaicore.serviceAgent) (`roles/documentaicore.serviceAgent`) 

  
  
#### `documentai.humanReviewConfigs.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.labelerPools.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.labelerPools.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.labelerPools.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.labelerPools.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.operations.getLegacy`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processedDocumentsSets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processedDocumentsSets.getDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processedDocumentsSets.listDocuments`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorTypes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.processorVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.processorVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorVersions.processBatch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processorVersions.processOnline`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `documentai.processorVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.processors.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.processors.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.processors.fetchHumanReviewDetails`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processors.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 

  
  
#### `documentai.processors.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.processors.processBatch`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Content Warehouse Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/contentwarehouse#contentwarehouse.serviceAgent) (`roles/contentwarehouse.serviceAgent`) 

  
  
#### `documentai.processors.processOnline`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Document AI API User](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.apiUser) (`roles/documentai.apiUser`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `documentai.processors.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.rules.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.rules.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.rules.generate`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.rules.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.rules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.rules.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemaVersions.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemaVersions.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemaVersions.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.schemaVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.schemaVersions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemas.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemas.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.schemas.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.schemas.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.schemas.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.validators.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.validators.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
#### `documentai.validators.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.validators.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)  [Document AI Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.viewer) (`roles/documentai.viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `documentai.validators.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Document AI Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.admin) (`roles/documentai.admin`)  [Document AI Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/clouddocumentai#documentai.editor) (`roles/documentai.editor`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
