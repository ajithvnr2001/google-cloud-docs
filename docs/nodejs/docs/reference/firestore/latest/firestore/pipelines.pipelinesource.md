---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesource
title: Class Pipelines.PipelineSource (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.575322+00:00
---

# Class Pipelines.PipelineSource (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Pipelines.PipelineSource (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

Represents the source of a Firestore `Pipeline`.

## Implements

firestore.Pipelines.PipelineSource

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(db)
    
    
    constructor(db: Firestore);

Constructs a new instance of the `PipelineSource` class

**Parameter**  
---  
**Name** | **Description**  
`db` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
  
  
## Methods 

### _validateReference(reference)
    
    
    _validateReference(reference: firestore.CollectionReference | firestore.DocumentReference): reference is CollectionReference | DocumentReference;

**Parameter**  
---  
**Name** | **Description**  
`reference` |  `FirebaseFirestore.CollectionReference | FirebaseFirestore.DocumentReference`   
  
**Returns**  
---  
**Type** | **Description**  
`reference is [CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference) | [DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)` |   
  
### collection(collection)
    
    
    collection(collection: string | firestore.CollectionReference): Pipeline;

Returns all documents from the entire collection. The collection can be nested.

**Parameter**  
---  
**Name** | **Description**  
`collection` |  `string | FirebaseFirestore.CollectionReference`   
Name or reference to the collection that will be used as the Pipeline source.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### collection(options)
    
    
    collection(options: firestore.Pipelines.CollectionStageOptions): Pipeline;

Returns all documents from the entire collection. The collection can be nested.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.CollectionStageOptions`   
Options defining how this CollectionStage is evaluated.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### collectionGroup(collectionId)
    
    
    collectionGroup(collectionId: string): Pipeline;

Returns all documents from a collection ID regardless of the parent.

**Parameter**  
---  
**Name** | **Description**  
`collectionId` |  `string`   
ID of the collection group to use as the Pipeline source.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### collectionGroup(options)
    
    
    collectionGroup(options: firestore.Pipelines.CollectionGroupStageOptions): Pipeline;

Returns all documents from a collection ID regardless of the parent.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.CollectionGroupStageOptions`   
Options defining how this CollectionGroupStage is evaluated.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### createFrom(query)
    
    
    createFrom(query: firestore.VectorQuery): Pipeline;

Convert the given VectorQuery into an equivalent Pipeline.

**Parameter**  
---  
**Name** | **Description**  
`query` |  `firestore.VectorQuery`   
A VectorQuery to be converted into a Pipeline.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### createFrom(query)
    
    
    createFrom(query: firestore.Query): Pipeline;

Convert the given Query into an equivalent Pipeline.

**Parameter**  
---  
**Name** | **Description**  
`query` |  `firestore.Query`   
A Query to be converted into a Pipeline.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### database()
    
    
    database(): Pipeline;

Returns all documents from the entire database.

**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### database(options)
    
    
    database(options: firestore.Pipelines.DatabaseStageOptions): Pipeline;

Returns all documents from the entire database.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.DatabaseStageOptions`   
Options defining how a DatabaseStage is evaluated.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### documents(docs)
    
    
    documents(docs: Array<string | DocumentReference>): Pipeline;

Set the pipeline's source to the documents specified by the given paths and DocumentReferences.

**Parameter**  
---  
**Name** | **Description**  
`docs` |  `Array<string | [DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)>`   
An array of paths and DocumentReferences specifying the individual documents that will be the source of this pipeline. The converters for these DocumentReferences will be ignored and not have an effect on this pipeline.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
### documents(options)
    
    
    documents(options: firestore.Pipelines.DocumentsStageOptions): Pipeline;

Set the pipeline's source to the documents specified by the given paths and DocumentReferences.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.Pipelines.DocumentsStageOptions`   
Options defining how this DocumentsStage is evaluated.  
**Returns**  
---  
**Type** | **Description**  
`[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
