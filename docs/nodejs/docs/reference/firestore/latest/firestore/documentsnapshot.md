---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot/
title: Class DocumentSnapshot (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:34.451066+00:00
---

# Class DocumentSnapshot (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class DocumentSnapshot (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A DocumentSnapshot is an immutable representation for a document in a Firestore database. The data can be extracted with [data()] or [get(fieldPath)] to get a specific field.

For a DocumentSnapshot that points to a non-existing document, any data access will return 'undefined'. You can use the [exists] property to explicitly verify a document's existence.

DocumentSnapshot

## Implements

FirebaseFirestore.DocumentSnapshot<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DocumentSnapshot` class.

## Properties 

### createTime
    
    
    get createTime(): Timestamp | undefined;

The time the document was created. Undefined for documents that don't exist.

{Timestamp|undefined} DocumentSnapshot#createTime

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(documentSnapshot => {
      if (documentSnapshot.exists) {
        let createTime = documentSnapshot.createTime;
        console.log(`Document created at '${createTime.toDate()}'`);
      }
    });
    

### exists
    
    
    get exists(): boolean;

True if the document exists.

{boolean} DocumentSnapshot#exists

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then((documentSnapshot) => {
      if (documentSnapshot.exists) {
        console.log(`Data: ${JSON.stringify(documentSnapshot.data())}`);
      }
    });
    

### id
    
    
    get id(): string;

The ID of the document for which this DocumentSnapshot contains data.

{string} DocumentSnapshot#id

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then((documentSnapshot) => {
      if (documentSnapshot.exists) {
        console.log(`Document found with name '${documentSnapshot.id}'`);
      }
    });
    

### readTime
    
    
    get readTime(): Timestamp;

The time this snapshot was read.

{Timestamp} DocumentSnapshot#readTime

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(documentSnapshot => {
      let readTime = documentSnapshot.readTime;
      console.log(`Document read at '${readTime.toDate()}'`);
    });
    

### ref
    
    
    get ref(): DocumentReference<AppModelType, DbModelType>;

A [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference) for the document stored in this snapshot.

{DocumentReference} DocumentSnapshot#ref

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then((documentSnapshot) => {
      if (documentSnapshot.exists) {
        console.log(`Found document at '${documentSnapshot.ref.path}'`);
      }
    });
    

### updateTime
    
    
    get updateTime(): Timestamp | undefined;

The time the document was last updated (at the time the snapshot was generated). Undefined for documents that don't exist.

{Timestamp|undefined} DocumentSnapshot#updateTime

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(documentSnapshot => {
      if (documentSnapshot.exists) {
        let updateTime = documentSnapshot.updateTime;
        console.log(`Document updated at '${updateTime.toDate()}'`);
      }
    });
    

## Methods 

### data()
    
    
    data(): AppModelType | undefined;

Retrieves all fields in the document as an object. Returns 'undefined' if the document doesn't exist.

**Returns**  
---  
**Type** | **Description**  
`AppModelType | undefined` | {T|undefined} An object containing all fields in the document or 'undefined' if the document doesn't exist.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(documentSnapshot => {
      let data = documentSnapshot.data();
      console.log(`Retrieved data: ${JSON.stringify(data)}`);
    });
    

### get(field)
    
    
    get(field: string | FieldPath): any;

Retrieves the field specified by `field`.

**Parameter**  
---  
**Name** | **Description**  
`field` |  `string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
The field path (e.g. 'foo' or 'foo.bar') to a specific field.  
**Returns**  
---  
**Type** | **Description**  
`any` | {*} The data at the specified field location or undefined if no such field exists.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.set({ a: { b: 'c' }}).then(() => {
      return documentRef.get();
    }).then(documentSnapshot => {
      let field = documentSnapshot.get('a.b');
      console.log(`Retrieved field value: ${field}`);
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.DocumentSnapshot<AppModelType, DbModelType>): boolean;

Returns true if the document's data and path in this `DocumentSnapshot` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.DocumentSnapshot<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `DocumentSnapshot` is equal to the provided value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
