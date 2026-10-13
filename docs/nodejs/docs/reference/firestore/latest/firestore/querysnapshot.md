---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot/
title: Class QuerySnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:37.214184+00:00
---

# Class QuerySnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class QuerySnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A QuerySnapshot contains zero or more [QueryDocumentSnapshot][QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) objects representing the results of a query. The documents can be accessed as an array via the [documents] property or enumerated using the [forEach] method. The number of documents can be determined via the [empty] and [size] properties.

QuerySnapshot

## Implements

FirebaseFirestore.QuerySnapshot<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(_query, _readTime, _size, docs, changes)
    
    
    constructor(_query: Query<AppModelType, DbModelType>, _readTime: Timestamp, _size: number, docs: () => Array<QueryDocumentSnapshot<AppModelType, DbModelType>>, changes: () => Array<DocumentChange<AppModelType, DbModelType>>);

Constructs a new instance of the `QuerySnapshot` class

**Parameters**  
---  
**Name** | **Description**  
`_query` |  `[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType>`   
The originating query.  
`_readTime` |  `[Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp)`   
The time when this query snapshot was obtained.  
`_size` |  `number`   
The number of documents in the result set.  
`docs` |  `() => Array<[QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot)<AppModelType, DbModelType>>`   
A callback returning a sorted array of documents matching this query  
`changes` |  `() => Array<[DocumentChange](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange)<AppModelType, DbModelType>>`   
A callback returning a sorted array of document change events for this snapshot.  
  
## Properties 

### docs
    
    
    get docs(): Array<QueryDocumentSnapshot<AppModelType, DbModelType>>;

An array of all the documents in this QuerySnapshot.

{Array.

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then(querySnapshot => {
      let docs = querySnapshot.docs;
      for (let doc of docs) {
        console.log(`Document found at path: ${doc.ref.path}`);
      }
    });
    

### empty
    
    
    get empty(): boolean;

True if there are no documents in the QuerySnapshot.

{boolean} QuerySnapshot#empty

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then(querySnapshot => {
      if (querySnapshot.empty) {
        console.log('No documents found.');
      }
    });
    

### query
    
    
    get query(): Query<AppModelType, DbModelType>;

The query on which you called get() or onSnapshot() in order to get this QuerySnapshot.

{Query} QuerySnapshot#query

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.limit(10).get().then(querySnapshot => {
      console.log(`Returned first batch of results`);
      let query = querySnapshot.query;
      return query.offset(10).get();
    }).then(() => {
      console.log(`Returned second batch of results`);
    });
    

### readTime
    
    
    get readTime(): Timestamp;

The time this query snapshot was obtained.

{Timestamp} QuerySnapshot#readTime

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then((querySnapshot) => {
      let readTime = querySnapshot.readTime;
      console.log(`Query results returned at '${readTime.toDate()}'`);
    });
    

### size
    
    
    get size(): number;

The number of documents in the QuerySnapshot.

{number} QuerySnapshot#size

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then(querySnapshot => {
      console.log(`Found ${querySnapshot.size} documents.`);
    });
    

## Methods 

### docChanges()
    
    
    docChanges(): Array<DocumentChange<AppModelType, DbModelType>>;

Returns an array of the documents changes since the last snapshot. If this is the first snapshot, all documents will be in the list as added changes.

**Returns**  
---  
**Type** | **Description**  
`Array<[DocumentChange](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange)<AppModelType, DbModelType>>` | {Array.  
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.onSnapshot(querySnapshot => {
      let changes = querySnapshot.docChanges();
      for (let change of changes) {
        console.log(`A document was ${change.type}.`);
      }
    });
    

### forEach(callback, thisArg)
    
    
    forEach(callback: (result: firestore.QueryDocumentSnapshot<AppModelType, DbModelType>) => void, thisArg?: unknown): void;

Enumerates all of the documents in the QuerySnapshot. This is a convenience method for running the same callback on each [QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) that is returned.

**Parameters**  
---  
**Name** | **Description**  
`callback` |  `(result: FirebaseFirestore.QueryDocumentSnapshot<AppModelType, DbModelType>) => void`   
A callback to be called with a [QueryDocumentSnapshot][QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) for each document in the snapshot.  
`thisArg` |  `unknown`   
The `this` binding for the callback..  
**Returns**  
---  
**Type** | **Description**  
`void` |   
**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Document found at path: ${documentSnapshot.ref.path}`);
      });
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.QuerySnapshot<AppModelType, DbModelType>): boolean;

Returns true if the document data in this `QuerySnapshot` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.QuerySnapshot<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `QuerySnapshot` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
