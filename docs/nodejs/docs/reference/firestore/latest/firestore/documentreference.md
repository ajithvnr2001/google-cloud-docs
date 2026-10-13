---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference/
title: Class DocumentReference (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:34.141493+00:00
---

# Class DocumentReference (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class DocumentReference (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A DocumentReference refers to a document location in a Firestore database and can be used to write, read, or listen to the location. The document at the referenced location may or may not exist. A DocumentReference can also be used to create a [CollectionReference][CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference) to a subcollection.

DocumentReference

## Implements

Serializable

FirebaseFirestore.DocumentReference<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Remarks

The constructor for this class is marked as internal. Third-party code should not call the constructor directly or create subclasses that extend the `DocumentReference` class.

## Properties 

### firestore
    
    
    get firestore(): Firestore;

The [Firestore][Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore) instance for the Firestore database (useful for performing transactions, etc.).

{Firestore} DocumentReference#firestore

**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.add({foo: 'bar'}).then(documentReference => {
      let firestore = documentReference.firestore;
      console.log(`Root location for document is ${firestore.formattedName}`);
    });
    

### id
    
    
    get id(): string;

The last path element of the referenced document.

{string} DocumentReference#id

**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.add({foo: 'bar'}).then(documentReference => {
      console.log(`Added document with name '${documentReference.id}'`);
    });
    

### parent
    
    
    get parent(): CollectionReference<AppModelType, DbModelType>;

A reference to the collection to which this DocumentReference belongs.

DocumentReference#parent {CollectionReference}

**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    let collectionRef = documentRef.parent;
    
    collectionRef.where('foo', '==', 'bar').get().then(results => {
      console.log(`Found ${results.size} matches in parent collection`);
    }):
    

### path
    
    
    get path(): string;

A string representing the path of the referenced document (relative to the root of the database).

{string} DocumentReference#path

**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    collectionRef.add({foo: 'bar'}).then(documentReference => {
      console.log(`Added document at '${documentReference.path}'`);
    });
    

## Methods 

### collection(collectionPath)
    
    
    collection(collectionPath: string): CollectionReference;

Gets a [CollectionReference][CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference) instance that refers to the collection at the specified path.

**Parameter**  
---  
**Name** | **Description**  
`collectionPath` |  `string`   
A slash-separated path to a collection.  
**Returns**  
---  
**Type** | **Description**  
`[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)` | {CollectionReference} A reference to the new subcollection.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    let subcollection = documentRef.collection('subcollection');
    console.log(`Path to subcollection: ${subcollection.path}`);
    

### create(data)
    
    
    create(data: firestore.WithFieldValue<AppModelType>): Promise<WriteResult>;

Create a document with the provided object values. This will fail the write if a document exists at its location.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
An object that contains the fields and data to serialize as the document.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise.  
**Example**
    
    
    let documentRef = firestore.collection('col').doc();
    
    documentRef.create({foo: 'bar'}).then((res) => {
      console.log(`Document created at ${res.updateTime}`);
    }).catch((err) => {
      console.log(`Failed to create document: ${err}`);
    });
    

### delete(precondition)
    
    
    delete(precondition?: firestore.Precondition): Promise<WriteResult>;

Deletes the document referred to by this `DocumentReference`.

A delete for a non-existing document is treated as a success (unless lastUptimeTime is provided).

**Parameter**  
---  
**Name** | **Description**  
`precondition` |  `firestore.Precondition`   
A precondition to enforce for this delete.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.delete().then(() => {
      console.log('Document successfully deleted.');
    });
    

### get()
    
    
    get(): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

Reads the document referred to by this DocumentReference.

**Returns**  
---  
**Type** | **Description**  
`Promise<[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)<AppModelType, DbModelType>>` | {Promise.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.get().then(documentSnapshot => {
      if (documentSnapshot.exists) {
        console.log('Document retrieved successfully.');
      }
    });
    

### isEqual(other)
    
    
    isEqual(other: firestore.DocumentReference<AppModelType, DbModelType>): boolean;

Returns true if this `DocumentReference` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `DocumentReference` is equal to the provided value.  
  
### listCollections()
    
    
    listCollections(): Promise<Array<CollectionReference>>;

Fetches the subcollections that are direct children of this document.

**Returns**  
---  
**Type** | **Description**  
`Promise<Array<[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)>>` | {Promise.<Array.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.listCollections().then(collections => {
      for (let collection of collections) {
        console.log(`Found subcollection with id: ${collection.id}`);
      }
    });
    

### onSnapshot(onNext, onError)
    
    
    onSnapshot(onNext: (snapshot: firestore.DocumentSnapshot<AppModelType, DbModelType>) => void, onError?: (error: Error) => void): () => void;

Attaches a listener for DocumentSnapshot events.

**Parameters**  
---  
**Name** | **Description**  
`onNext` |  `(snapshot: FirebaseFirestore.DocumentSnapshot<AppModelType, DbModelType>) => void`   
A callback to be called every time a new `DocumentSnapshot` is available.  
`onError` |  `(error: Error) => void`   
A callback to be called if the listen fails or is cancelled. No further callbacks will occur. If unset, errors will be logged to the console.  
**Returns**  
---  
**Type** | **Description**  
`() => void` | {function()} An unsubscribe function that can be called to cancel the snapshot listener.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    let unsubscribe = documentRef.onSnapshot(documentSnapshot => {
      if (documentSnapshot.exists) {
        console.log(documentSnapshot.data());
      }
    }, err => {
      console.log(`Encountered error: ${err}`);
    });
    
    // Remove this listener.
    unsubscribe();
    

### set(data, options)
    
    
    set(data: firestore.PartialWithFieldValue<AppModelType>, options: firestore.SetOptions): Promise<WriteResult>;

**Parameters**  
---  
**Name** | **Description**  
`data` |  `FirebaseFirestore.PartialWithFieldValue<AppModelType>`   
  
`options` |  `firestore.SetOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` |   
  
### set(data)
    
    
    set(data: firestore.WithFieldValue<AppModelType>): Promise<WriteResult>;

**Parameter**  
---  
**Name** | **Description**  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` |   
  
### update(dataOrField, preconditionOrValues)
    
    
    update(dataOrField: firestore.UpdateData<DbModelType> | string | firestore.FieldPath, ...preconditionOrValues: Array<unknown | string | firestore.FieldPath | firestore.Precondition>): Promise<WriteResult>;

Updates fields in the document referred to by this DocumentReference. If the document doesn't yet exist, the update fails and the returned Promise will be rejected.

The update() method accepts either an object with field paths encoded as keys and field values encoded as values, or a variable number of arguments that alternate between field paths and field values.

A Precondition restricting this update can be specified as the last argument.

**Parameters**  
---  
**Name** | **Description**  
`dataOrField` |  `FirebaseFirestore.UpdateData<DbModelType> | string | FirebaseFirestore.FieldPath`   
An object containing the fields and values with which to update the document or the path of the first field to update.  
`preconditionOrValues` |  `Array<unknown | string | FirebaseFirestore.FieldPath | FirebaseFirestore.Precondition>`   
An alternating list of field paths and values to update or a Precondition to restrict this update.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise.  
**Example**
    
    
    let documentRef = firestore.doc('col/doc');
    
    documentRef.update({foo: 'bar'}).then(res => {
      console.log(`Document updated at ${res.updateTime}`);
    });
    

### withConverter(converter)
    
    
    withConverter<NewAppModelType, NewDbModelType extends firestore.DocumentData = firestore.DocumentData>(converter: firestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null): DocumentReference<NewAppModelType, NewDbModelType>;

**Parameter**  
---  
**Name** | **Description**  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<NewAppModelType, NewDbModelType> | null`   
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<NewAppModelType, NewDbModelType>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`NewAppModelType` |   
`NewDbModelType` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
