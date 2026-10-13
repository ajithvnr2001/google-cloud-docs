---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquerysnapshot/
title: Class VectorQuerySnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:37.664751+00:00
---

# Class VectorQuerySnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/vectorquerysnapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class VectorQuerySnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A `VectorQuerySnapshot` contains zero or more `QueryDocumentSnapshot` objects representing the results of a query. The documents can be accessed as an array via the `docs` property or enumerated using the `forEach` method. The number of documents can be determined via the `empty` and `size` properties.

## Implements

FirebaseFirestore.VectorQuerySnapshot<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `VectorQuerySnapshot` class.

## Properties 

### docs
    
    
    get docs(): Array<QueryDocumentSnapshot<AppModelType, DbModelType>>;

An array of all the documents in this `VectorQuerySnapshot`.

**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
    query.get().then(querySnapshot => {
      let docs = querySnapshot.docs;
      for (let doc of docs) {
        console.log(`Document found at path: ${doc.ref.path}`);
      }
    });
    

### empty
    
    
    get empty(): boolean;

`true` if there are no documents in the `VectorQuerySnapshot`.

**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
    query.get().then(querySnapshot => {
      if (querySnapshot.empty) {
        console.log('No documents found.');
      }
    });
    

### query
    
    
    get query(): VectorQuery<AppModelType, DbModelType>;

The `VectorQuery` on which you called get() in order to get this `VectorQuerySnapshot`.

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    query.findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"})
      .get().then(querySnapshot => {
        console.log(`Returned first batch of results`);
        let query = querySnapshot.query;
        return query.offset(10).get();
      }).then(() => {
      console.log(`Returned second batch of results`);
      });
    

### readTime
    
    
    get readTime(): Timestamp;

The time this `VectorQuerySnapshot` was obtained.

**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
    query.get().then((querySnapshot) => {
      let readTime = querySnapshot.readTime;
      console.log(`Query results returned at '${readTime.toDate()}'`);
    });
    

### size
    
    
    get size(): number;

The number of documents in the `VectorQuerySnapshot`.

**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
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
`Array<[DocumentChange](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange)<AppModelType, DbModelType>>` | An array of the documents changes since the last snapshot.  
**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
    query.get().then(querySnapshot => {
      let changes = querySnapshot.docChanges();
      for (let change of changes) {
        console.log(`A document was ${change.type}.`);
      }
    });
    

### forEach(callback, thisArg)
    
    
    forEach(callback: (result: firestore.QueryDocumentSnapshot<AppModelType, DbModelType>) => void, thisArg?: unknown): void;

Enumerates all of the documents in the `VectorQuerySnapshot`. This is a convenience method for running the same callback on each [QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) that is returned.

**Parameters**  
---  
**Name** | **Description**  
`callback` |  `(result: FirebaseFirestore.QueryDocumentSnapshot<AppModelType, DbModelType>) => void`   
A callback to be called with a [QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) for each document in the snapshot.  
`thisArg` |  `unknown`   
The `this` binding for the callback..  
**Returns**  
---  
**Type** | **Description**  
`void` |   
**Example**
    
    
    let query = firestore.collection('col')
      .findNearest("embedding", [0, 0], {limit: 10, distanceMeasure: "EUCLIDEAN"});
    
    query.get().then(querySnapshot => {
      querySnapshot.forEach(documentSnapshot => {
        console.log(`Document found at path: ${documentSnapshot.ref.path}`);
      });
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.VectorQuerySnapshot<AppModelType, DbModelType>): boolean;

Returns true if the document data in this `VectorQuerySnapshot` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.VectorQuerySnapshot<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | true if this `VectorQuerySnapshot` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
