---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch/
title: Class WriteBatch (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:37.962630+00:00
---

# Class WriteBatch (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class WriteBatch (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A Firestore WriteBatch that can be used to atomically commit multiple write operations at once.

WriteBatch

## Implements

firestore.WriteBatch

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(firestore)
    
    
    constructor(firestore: Firestore);

Constructs a new instance of the `WriteBatch` class

**Parameter**  
---  
**Name** | **Description**  
`firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
  
  
## Properties 

### _firestore
    
    
    protected readonly _firestore: Firestore;

## Methods 

### commit()
    
    
    commit(): Promise<WriteResult[]>;

Atomically commits all pending operations to the database and verifies all preconditions. Fails the entire write if any precondition is not met.

**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)[]>` | {Promise.<Array.  
**Example**
    
    
    let writeBatch = firestore.batch();
    let documentRef = firestore.doc('col/doc');
    
    writeBatch.set(documentRef, {foo: 'bar'});
    
    writeBatch.commit().then(() => {
      console.log('Successfully executed batch.');
    });
    

### create(documentRef, data)
    
    
    create<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.WithFieldValue<AppModelType>): WriteBatch;

Create a document with the provided object values. This will fail the batch if a document exists at its location.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be created.  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
The object to serialize as the document.  
**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` | {WriteBatch} This WriteBatch instance. Used for chaining method calls.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let writeBatch = firestore.batch();
    let documentRef = firestore.collection('col').doc();
    
    writeBatch.create(documentRef, {foo: 'bar'});
    
    writeBatch.commit().then(() => {
      console.log('Successfully executed batch.');
    });
    

### delete(documentRef, precondition)
    
    
    delete(documentRef: firestore.DocumentReference<any, any>, precondition?: firestore.Precondition): WriteBatch;

Deletes a document from the database.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<any, any>`   
A reference to the document to be deleted.  
`precondition` |  `firestore.Precondition`   
A precondition to enforce for this delete.  
**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` | {WriteBatch} This WriteBatch instance. Used for chaining method calls.  
**Example**
    
    
    let writeBatch = firestore.batch();
    let documentRef = firestore.doc('col/doc');
    
    writeBatch.delete(documentRef);
    
    writeBatch.commit().then(() => {
      console.log('Successfully executed batch.');
    });
    

### set(documentRef, data, options)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.PartialWithFieldValue<AppModelType>, options: firestore.SetOptions): WriteBatch;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `FirebaseFirestore.PartialWithFieldValue<AppModelType>`   
  
`options` |  `firestore.SetOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### set(documentRef, data)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.WithFieldValue<AppModelType>): WriteBatch;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
  
**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### update(documentRef, dataOrField, preconditionOrValues)
    
    
    update<AppModelType = firestore.DocumentData, DbModelType extends firestore.DocumentData = firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, dataOrField: firestore.UpdateData<DbModelType> | string | firestore.FieldPath, ...preconditionOrValues: Array<{
            lastUpdateTime?: firestore.Timestamp;
        } | unknown | string | firestore.FieldPath>): WriteBatch;

Update fields of the document referred to by the provided [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference). If the document doesn't yet exist, the update fails and the entire batch will be rejected.

The update() method accepts either an object with field paths encoded as keys and field values encoded as values, or a variable number of arguments that alternate between field paths and field values. Nested fields can be updated by providing dot-separated field path strings or by providing FieldPath objects.

A Precondition restricting this update can be specified as the last argument.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be updated.  
`dataOrField` |  `FirebaseFirestore.UpdateData<DbModelType> | string | FirebaseFirestore.FieldPath`   
An object containing the fields and values with which to update the document or the path of the first field to update.  
`preconditionOrValues` |  `Array<{ lastUpdateTime?: FirebaseFirestore.Timestamp; } | unknown | string | FirebaseFirestore.FieldPath>`   
An alternating list of field paths and values to update or a Precondition to restrict this update.  
**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` | {WriteBatch} This WriteBatch instance. Used for chaining method calls.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let writeBatch = firestore.batch();
    let documentRef = firestore.doc('col/doc');
    
    writeBatch.update(documentRef, {foo: 'bar'});
    
    writeBatch.commit().then(() => {
      console.log('Successfully executed batch.');
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
