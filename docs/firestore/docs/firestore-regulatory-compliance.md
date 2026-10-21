---
url: https://docs.cloud.google.com/firestore/docs/firestore-regulatory-compliance/
title: Regulatory support in Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:11.528020+00:00
---

# Regulatory support in Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/firestore-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Resources ](https://docs.cloud.google.com/firestore/native/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Regulatory support in Firestore

This document describes the features, configurations and APIs in Firestore that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Firestore APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
datastore.googleapis.com | v1 |  SUPPORTED   
datastore.googleapis.com | v1beta1 |  SUPPORTED   
datastore.googleapis.com | v1beta3 |  SUPPORTED   
firestore.googleapis.com | v1 |  SUPPORTED   
firestore.googleapis.com | v1beta1 |  SUPPORTED   
firestore.googleapis.com | v1beta2 |  SUPPORTED   
  
### Compliance supported regions

Firestore is available for Data Boundary for ITAR in the following Google Cloud regions:

  * us-central1
  * us-east1
  * us-east4
  * us-east5
  * us-south1
  * us-west1
  * us-west2
  * us-west3
  * us-west4



### API fields for sensitive data

#### Resource: firestore.googleapis.com/Document

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `firestore.googleapis.com` REST API: `POST` `/v1/{parent=projects/*/databases/*/documents/**}/{collection_id}` RPC methods:

  * `google.firestore.v1.Firestore.CreateDocument`

| 

  * `document.fields.value`

  
Service: `firestore.googleapis.com` REST API: `POST` `/v1/{database=projects/*/databases/*}/documents:commit` RPC methods:

  * `google.firestore.v1.Firestore.Commit`

| 

  * `writes.update.fields.value`

  
Service: `firestore.googleapis.com` REST API: `POST` `/v1/{database=projects/*/databases/*}/documents:batchWrite` RPC methods:

  * `google.firestore.v1.Firestore.BatchWrite`

| 

  * `writes.update.fields.value`

  
  
#### Resource: datastore.googleapis.com/Entity

The following table specifies the API resources and fields that are designed to handle data that is protected under Data Boundary for ITAR.

API Method | Protected fields  
---|---  
Service: `datastore.googleapis.com` REST API: `POST` `/v1/projects/{project_id}:commit` RPC methods:

  * `google.datastore.v1.Datastore.Commit`

| 

  * `mutations.insert.properties.value`
  * `mutations.update.properties.value`
  * `mutations.upsert.properties.value`

  
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Database configuration | 

  * `database.cmekConfig.kmsKeyName`
  * `database.etag`
  * `database.locationId`
  * `database.storagePlacement`
  * `encryptionConfig.customerManagedEncryption.kmsKeyName`
  * `pitrSnapshot.database`

  
Document and entity specification | 

  * `document.fields.key`
  * `document.fields.value.mapValue.fields.key`
  * `document.name`
  * `entityFilter.namespaceIds`
  * `structuredAggregationQuery.structuredQuery.from.collectionId`
  * `structuredQuery.from.collectionId`

  
Index and field configuration | 

  * `field.indexConfig.indexes.defaultCollation`
  * `field.indexConfig.indexes.fields.fieldPath`
  * `field.indexConfig.indexes.indexName`
  * `field.indexConfig.indexes.searchIndexOptions.textLanguageOverrideFieldPath`
  * `field.name`
  * `indexId`

  
Key and path identification | 

  * `keys.partitionId.databaseId`
  * `keys.partitionId.namespaceId`
  * `keys.partitionId.projectId`
  * `keys.path.kind`
  * `keys.path.name`

  
Mutation operations | 

  * `mutations.delete.path.name`
  * `mutations.insert.properties.key`
  * `mutations.propertyTransforms.increment.keyValue.path.kind`
  * `mutations.propertyTransforms.removeAllFromArray.values.keyValue.path.kind`
  * `mutations.update.key.path.name`
  * `mutations.upsert.key.path.name`

  
Pagination and ordering | 

  * `groupBy`
  * `orderBy`
  * `pageToken`
  * `structuredAggregationQuery.structuredQuery.orderBy.field.fieldPath`
  * `structuredQuery.orderBy.field.fieldPath`

  
Project and database identification | 

  * `collectionId`
  * `database`
  * `databaseId`
  * `name`
  * `parent`
  * `projectId`

  
Query and filter parameters | 

  * `aggregationQuery.nestedQuery.filter.propertyFilter.property.name`
  * `entityFilter.kinds`
  * `field.indexConfig.indexes.partialFilterExpression`
  * `field.indexConfig.indexes.searchIndexOptions.textLanguage`
  * `filter`
  * `gqlQuery.queryString`

  
Request control and metadata | 

  * `allocateIds.requestOptions.requestTags`
  * `commit.requestOptions.isolationKey`
  * `requestExtensions.typeUrl`
  * `requestOptions.isolationKey`
  * `requestOptions.requestTags`
  * `rollback.requestOptions.requestTags`

  
Transformations and properties | 

  * `mutations.propertyMask.paths`
  * `mutations.propertyTransforms.appendMissingElements.values.keyValue.path.kind`
  * `mutations.propertyTransforms.maximum.keyValue.path.kind`
  * `mutations.propertyTransforms.minimum.keyValue.path.kind`
  * `writes.transform.fieldTransforms.fieldPath`
  * `writes.updateTransforms.fieldPath`

  
  
### References

  * [Cloud Firestore documentation](https://cloud.google.com/firestore/docs)
  * [Cloud Firestore API reference](https://cloud.google.com/firestore/docs/reference/rest)
  * [Cloud Firestore RPC reference](https://cloud.google.com/firestore/docs/reference/rpc)
  * [Assured Workloads Monitoring](https://cloud.google.com/assured-workloads/docs/monitor-folder)

  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
