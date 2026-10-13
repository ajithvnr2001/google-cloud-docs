---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange/
title: Class DocumentChange (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:33.777109+00:00
---

# Class DocumentChange (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentchange/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class DocumentChange (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A DocumentChange represents a change to the documents matching a query. It contains the document affected and the type of change that occurred.

DocumentChange

## Implements

FirebaseFirestore.DocumentChange<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(type, document, oldIndex, newIndex)
    
    
    constructor(type: DocumentChangeType, document: QueryDocumentSnapshot<AppModelType, DbModelType>, oldIndex: number, newIndex: number);

Constructs a new instance of the `DocumentChange` class

**Parameters**  
---  
**Name** | **Description**  
`type` |  `[DocumentChangeType](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)`   
'added' | 'removed' | 'modified'.  
`document` |  `[QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot)<AppModelType, DbModelType>`   
The document.  
`oldIndex` |  `number`   
The index in the documents array prior to this change.  
`newIndex` |  `number`   
The index in the documents array after this change.  
  
## Properties 

### doc
    
    
    get doc(): QueryDocumentSnapshot<AppModelType, DbModelType>;

The document affected by this change.

{QueryDocumentSnapshot} DocumentChange#doc

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    
    let unsubscribe = query.onSnapshot(querySnapshot => {
      for (let change of querySnapshot.docChanges) {
        console.log(change.doc.data());
      }
    });
    
    // Remove this listener.
    unsubscribe();
    

### newIndex
    
    
    get newIndex(): number;

The index of the changed document in the result set immediately after this DocumentChange (i.e. supposing that all prior DocumentChange objects and the current DocumentChange object have been applied). Is -1 for 'removed' events.

{number} DocumentChange#newIndex

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    let docsArray = [];
    
    let unsubscribe = query.onSnapshot(querySnapshot => {
      for (let change of querySnapshot.docChanges) {
        if (change.oldIndex !== -1) {
          docsArray.splice(change.oldIndex, 1);
        }
        if (change.newIndex !== -1) {
          docsArray.splice(change.newIndex, 0, change.doc);
        }
      }
    });
    
    // Remove this listener.
    unsubscribe();
    

### oldIndex
    
    
    get oldIndex(): number;

The index of the changed document in the result set immediately prior to this DocumentChange (i.e. supposing that all prior DocumentChange objects have been applied). Is -1 for 'added' events.

{number} DocumentChange#oldIndex

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    let docsArray = [];
    
    let unsubscribe = query.onSnapshot(querySnapshot => {
      for (let change of querySnapshot.docChanges) {
        if (change.oldIndex !== -1) {
          docsArray.splice(change.oldIndex, 1);
        }
        if (change.newIndex !== -1) {
          docsArray.splice(change.newIndex, 0, change.doc);
        }
      }
    });
    
    // Remove this listener.
    unsubscribe();
    

### type
    
    
    get type(): DocumentChangeType;

The type of change ('added', 'modified', or 'removed').

{string} DocumentChange#type

**Example**
    
    
    let query = firestore.collection('col').where('foo', '==', 'bar');
    let docsArray = [];
    
    let unsubscribe = query.onSnapshot(querySnapshot => {
      for (let change of querySnapshot.docChanges) {
        console.log(`Type of change is ${change.type}`);
      }
    });
    
    // Remove this listener.
    unsubscribe();
    

## Methods 

### isEqual(other)
    
    
    isEqual(other: firestore.DocumentChange<AppModelType, DbModelType>): boolean;

Returns true if the data in this `DocumentChange` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.DocumentChange<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | true if this `DocumentChange` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
