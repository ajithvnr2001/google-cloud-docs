---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch/
title: Vector Search roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:47.441087+00:00
---

# Vector Search roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Vector Search roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Vector Search. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Vector Search roles

Role | Permissions  
---|---  
  
#### Vector Search Admin 

(`roles/vectorsearch.admin`) Grants full access to all vectorsearch resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vectorsearch.*`

  * `vectorsearch.collections.create`
  * `vectorsearch.collections.delete`
  * `vectorsearch.collections.get`
  * `vectorsearch.collections.list`
  * `vectorsearch.collections.update`
  * `vectorsearch.dataObjects.create`
  * `vectorsearch.dataObjects.delete`
  * `vectorsearch.dataObjects.export`
  * `vectorsearch.dataObjects.get`
  * `vectorsearch.dataObjects.import`
  * `vectorsearch.dataObjects.query`
  * `vectorsearch.dataObjects.search`
  * `vectorsearch.dataObjects.update`
  * `vectorsearch.indexes.create`
  * `vectorsearch.indexes.delete`
  * `vectorsearch.indexes.get`
  * `vectorsearch.indexes.list`
  * `vectorsearch.indexes.update`
  * `vectorsearch.locations.get`
  * `vectorsearch.locations.list`
  * `vectorsearch.operations.cancel`
  * `vectorsearch.operations.delete`
  * `vectorsearch.operations.get`
  * `vectorsearch.operations.list`

  
  
#### Vector Search Viewer 

(`roles/vectorsearch.viewer`) Grants read access to all vectorsearch resources.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vectorsearch.collections.get` `vectorsearch.collections.list` `vectorsearch.dataObjects.export` `vectorsearch.dataObjects.get` `vectorsearch.dataObjects.query` `vectorsearch.dataObjects.search` `vectorsearch.indexes.get` `vectorsearch.indexes.list` `vectorsearch.locations.*`

  * `vectorsearch.locations.get`
  * `vectorsearch.locations.list`

`vectorsearch.operations.get` `vectorsearch.operations.list`  
  
#### Vector Search Collection Writer 

(`roles/vectorsearch.collectionWriter`) Grants read-write access to Collections.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vectorsearch.collections.*`

  * `vectorsearch.collections.create`
  * `vectorsearch.collections.delete`
  * `vectorsearch.collections.get`
  * `vectorsearch.collections.list`
  * `vectorsearch.collections.update`

`vectorsearch.locations.*`

  * `vectorsearch.locations.get`
  * `vectorsearch.locations.list`

`vectorsearch.operations.*`

  * `vectorsearch.operations.cancel`
  * `vectorsearch.operations.delete`
  * `vectorsearch.operations.get`
  * `vectorsearch.operations.list`

  
  
#### Vector Search DataObject Writer 

(`roles/vectorsearch.dataObjectWriter`) Grants read-write access to DataObjects and read access to parent Collections.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vectorsearch.collections.get` `vectorsearch.collections.list` `vectorsearch.dataObjects.*`

  * `vectorsearch.dataObjects.create`
  * `vectorsearch.dataObjects.delete`
  * `vectorsearch.dataObjects.export`
  * `vectorsearch.dataObjects.get`
  * `vectorsearch.dataObjects.import`
  * `vectorsearch.dataObjects.query`
  * `vectorsearch.dataObjects.search`
  * `vectorsearch.dataObjects.update`

`vectorsearch.locations.*`

  * `vectorsearch.locations.get`
  * `vectorsearch.locations.list`

  
  
#### Vector Search Index Writer 

(`roles/vectorsearch.indexWriter`) Grants read-write access to Indexes and read access to parent Collections.  |  `resourcemanager.projects.get` `resourcemanager.projects.list` `vectorsearch.collections.get` `vectorsearch.collections.list` `vectorsearch.indexes.*`

  * `vectorsearch.indexes.create`
  * `vectorsearch.indexes.delete`
  * `vectorsearch.indexes.get`
  * `vectorsearch.indexes.list`
  * `vectorsearch.indexes.update`

`vectorsearch.locations.*`

  * `vectorsearch.locations.get`
  * `vectorsearch.locations.list`

`vectorsearch.operations.*`

  * `vectorsearch.operations.cancel`
  * `vectorsearch.operations.delete`
  * `vectorsearch.operations.get`
  * `vectorsearch.operations.list`

  
  
### Service agent roles

Service agent roles should only be granted to [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

Role | Permissions  
---|---  
  
#### Vector Search Service Agent 

(`roles/vectorsearch.serviceAgent`) Gives Vector Search access to read Cloud Storage buckets, read/create objects, use Vertex Models, and call Discovery Engine RankService.  **Warning:** Do not grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents).  |  `aiplatform.batchPredictionJobs.create` `aiplatform.batchPredictionJobs.get` `aiplatform.endpoints.predict` `discoveryengine.rankingConfigs.rank` `storage.buckets.get` `storage.objects.create` `storage.objects.get` `storage.objects.list` `vectorsearch.collections.create` `vectorsearch.collections.delete` `vectorsearch.dataObjects.create` `vectorsearch.dataObjects.delete` `vectorsearch.dataObjects.import` `vectorsearch.dataObjects.update` `vectorsearch.indexes.delete`  
  
## Vector Search permissions

Permission | Included in roles  
---|---  
  
#### `vectorsearch.collections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.collections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.collections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.collections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.collections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.dataObjects.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.dataObjects.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.dataObjects.export`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)   
  
#### `vectorsearch.dataObjects.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.dataObjects.import`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.dataObjects.query`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.dataObjects.search`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.dataObjects.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.indexes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.indexes.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 
  * [Vector Search Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.serviceAgent) (`roles/vectorsearch.serviceAgent`) 

  
  
#### `vectorsearch.indexes.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.indexes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.indexes.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)   
  
#### `vectorsearch.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)   
  
#### `vectorsearch.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search DataObject Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.dataObjectWriter) (`roles/vectorsearch.dataObjectWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  [Wiz Cloud Inventory Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/wiz#wiz.cloudInventoryViewer) (`roles/wiz.cloudInventoryViewer`)   
  
#### `vectorsearch.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)   
  
#### `vectorsearch.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)   
  
#### `vectorsearch.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
#### `vectorsearch.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Vector Search Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.admin) (`roles/vectorsearch.admin`)  [Vector Search Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.viewer) (`roles/vectorsearch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Vector Search Collection Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.collectionWriter) (`roles/vectorsearch.collectionWriter`)  [Vector Search Index Writer](https://docs.cloud.google.com/iam/docs/roles-permissions/vectorsearch#vectorsearch.indexWriter) (`roles/vectorsearch.indexWriter`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Vertex AI RAG Data Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.ragServiceAgent) (`roles/aiplatform.ragServiceAgent`) 

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
