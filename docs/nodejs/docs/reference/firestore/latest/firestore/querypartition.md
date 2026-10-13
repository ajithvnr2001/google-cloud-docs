---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querypartition/
title: Class QueryPartition (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:36.959363+00:00
---

# Class QueryPartition (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querypartition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class QueryPartition (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A split point that can be used in a query as a starting and/or end point for the query results. The cursors returned by and can only be used in a query that matches the constraint of query that produced this partition.

QueryPartition

## Implements

FirebaseFirestore.QueryPartition<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(_firestore, _collectionId, _converter, _startAt, _endBefore)
    
    
    constructor(_firestore: Firestore, _collectionId: string, _converter: firestore.FirestoreDataConverter<AppModelType, DbModelType>, _startAt: api.IValue[] | undefined, _endBefore: api.IValue[] | undefined);

Constructs a new instance of the `QueryPartition` class

**Parameters**  
---  
**Name** | **Description**  
`_firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
  
`_collectionId` |  `string`   
  
`_converter` |  `FirebaseFirestore.FirestoreDataConverter<AppModelType, DbModelType>`   
  
`_startAt` |  `google.firestore.v1.IValue[] | undefined`   
  
`_endBefore` |  `google.firestore.v1.IValue[] | undefined`   
  
  
## Properties 

### endBefore
    
    
    get endBefore(): unknown[] | undefined;

The cursor that defines the first result after this partition or `undefined` if this is the last partition. The cursor value must be destructured when passed to `endBefore()` (for example with `query.endBefore(...queryPartition.endBefore)`).

**Example**
    
    
    const query = firestore.collectionGroup('collectionId');
    for await (const partition of query.getPartitions(42)) {
      let partitionedQuery = query.orderBy(FieldPath.documentId());
      if (partition.startAt) {
        partitionedQuery = partitionedQuery.startAt(...partition.startAt);
      }
      if (partition.endBefore) {
        partitionedQuery = partitionedQuery.endBefore(...partition.endBefore);
      }
      const querySnapshot = await partitionedQuery.get();
      console.log(`Partition contained ${querySnapshot.length} documents`);
    }
    
    

{Array<*>}

### startAt
    
    
    get startAt(): unknown[] | undefined;

The cursor that defines the first result for this partition or `undefined` if this is the first partition. The cursor value must be destructured when passed to `startAt()` (for example with `query.startAt(...queryPartition.startAt)`).

**Example**
    
    
    const query = firestore.collectionGroup('collectionId');
    for await (const partition of query.getPartitions(42)) {
      let partitionedQuery = query.orderBy(FieldPath.documentId());
      if (partition.startAt) {
        partitionedQuery = partitionedQuery.startAt(...partition.startAt);
      }
      if (partition.endBefore) {
        partitionedQuery = partitionedQuery.endBefore(...partition.endBefore);
      }
      const querySnapshot = await partitionedQuery.get();
      console.log(`Partition contained ${querySnapshot.length} documents`);
    }
    
    

{Array<*>}

## Methods 

### toQuery()
    
    
    toQuery(): Query<AppModelType, DbModelType>;

Returns a query that only encapsulates the documents for this partition.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>` | {Query  
**Example**
    
    
    const query = firestore.collectionGroup('collectionId');
    for await (const partition of query.getPartitions(42)) {
      const partitionedQuery = partition.toQuery();
      const querySnapshot = await partitionedQuery.get();
      console.log(`Partition contained ${querySnapshot.length} documents`);
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
