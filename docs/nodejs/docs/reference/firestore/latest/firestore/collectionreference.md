---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference/
title: Class CollectionReference (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:33.997682+00:00
---

# Class CollectionReference (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class CollectionReference (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A CollectionReference object can be used for adding documents, getting document references, and querying for documents (using the methods inherited from [Query][Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)).

CollectionReference Query

## Inheritance

[Query](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/query)<AppModelType, DbModelType> > CollectionReference

## Implements

FirebaseFirestore.CollectionReference<AppModelType, DbModelType>

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(firestore, path, converter)
    
    
    constructor(firestore: Firestore, path: ResourcePath, converter?: firestore.FirestoreDataConverter<AppModelType, DbModelType>);

Constructs a new instance of the `CollectionReference` class

**Parameters**  
---  
**Name** | **Description**  
`firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
The Firestore Database client.  
`path` |  `ResourcePath`   
The Path of this collection.  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<AppModelType, DbModelType>`   
  
  
## Properties 

### id
    
    
    get id(): string;

The last path element of the referenced collection.

{string} CollectionReference#id

**Example**
    
    
    let collectionRef = firestore.collection('col/doc/subcollection');
    console.log(`ID of the subcollection: ${collectionRef.id}`);
    

### parent
    
    
    get parent(): DocumentReference | null;

A reference to the containing Document if this is a subcollection, else null.

{DocumentReference|null} CollectionReference#parent

**Example**
    
    
    let collectionRef = firestore.collection('col/doc/subcollection');
    let documentRef = collectionRef.parent;
    console.log(`Parent name: ${documentRef.path}`);
    

### path
    
    
    get path(): string;

A string representing the path of the referenced collection (relative to the root of the database).

{string} CollectionReference#path

**Example**
    
    
    let collectionRef = firestore.collection('col/doc/subcollection');
    console.log(`Path of the subcollection: ${collectionRef.path}`);
    

## Methods 

### add(data)
    
    
    add(data: firestore.WithFieldValue<AppModelType>): Promise<DocumentReference<AppModelType, DbModelType>>;

Add a new document to this collection with the specified data, assigning it a document ID automatically.

**Parameter**  
---  
**Name** | **Description**  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
An Object containing the data for the new document.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<AppModelType, DbModelType>>` | {Promise.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    collectionRef.add({foo: 'bar'}).then(documentReference => {
      console.log(`Added document with name: ${documentReference.id}`);
    });
    

### doc()
    
    
    doc(): DocumentReference<AppModelType, DbModelType>;

**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<AppModelType, DbModelType>` |   
  
### doc(documentPath)
    
    
    doc(documentPath: string): DocumentReference<AppModelType, DbModelType>;

**Parameter**  
---  
**Name** | **Description**  
`documentPath` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<AppModelType, DbModelType>` |   
  
### isEqual(other)
    
    
    isEqual(other: firestore.CollectionReference<AppModelType, DbModelType>): boolean;

Returns true if this `CollectionReference` is equal to the provided value.

**Parameter**  
---  
**Name** | **Description**  
`other` |  `FirebaseFirestore.CollectionReference<AppModelType, DbModelType>`   
The value to compare against.  
**Returns**  
---  
**Type** | **Description**  
`boolean` | {boolean} true if this `CollectionReference` is equal to the provided value.  
  
### listDocuments()
    
    
    listDocuments(): Promise<Array<DocumentReference<AppModelType, DbModelType>>>;

Retrieves the list of documents in this collection.

The document references returned may include references to "missing documents", i.e. document locations that have no document present but which contain subcollections with documents. Attempting to read such a document reference (e.g. via `.get()` or `.onSnapshot()`) will return a `DocumentSnapshot` whose `.exists` property is false.

**Returns**  
---  
**Type** | **Description**  
`Promise<Array<[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<AppModelType, DbModelType>>>` | {Promise<DocumentReference[]>} The list of documents in this collection.  
**Example**
    
    
    let collectionRef = firestore.collection('col');
    
    return collectionRef.listDocuments().then(documentRefs => {
       return firestore.getAll(...documentRefs);
    }).then(documentSnapshots => {
       for (let documentSnapshot of documentSnapshots) {
          if (documentSnapshot.exists) {
            console.log(`Found document with data: ${documentSnapshot.id}`);
          } else {
            console.log(`Found missing document: ${documentSnapshot.id}`);
          }
       }
    });
    

### withConverter(converter)
    
    
    withConverter<NewAppModelType, NewDbModelType extends firestore.DocumentData = firestore.DocumentData>(converter: firestore.FirestoreDataConverter<NewAppModelType, NewDbModelType>): CollectionReference<NewAppModelType, NewDbModelType>;

**Parameter**  
---  
**Name** | **Description**  
`converter` |  `FirebaseFirestore.FirestoreDataConverter<NewAppModelType, NewDbModelType>`   
  
**Returns**  
---  
**Type** | **Description**  
`[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)<NewAppModelType, NewDbModelType>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`NewAppModelType` |   
`NewDbModelType` |   
  
### withConverter(converter)
    
    
    withConverter(converter: null): CollectionReference<firestore.DocumentData, firestore.DocumentData>;

**Parameter**  
---  
**Name** | **Description**  
`converter` |  `null`   
  
**Returns**  
---  
**Type** | **Description**  
`[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)<FirebaseFirestore.DocumentData, FirebaseFirestore.DocumentData>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
