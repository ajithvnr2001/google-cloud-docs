---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore/
title: Class Firestore (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:35.434642+00:00
---

# Class Firestore (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Firestore (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

The Firestore client represents a Firestore Database and is the entry point for all Firestore operations.

## Implements

firestore.Firestore

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Examples

Install the client library with [npm](https://www.npmjs.com/):
    
    
    npm install --save @google-cloud/firestore
    
    

Import the client library
    
    
    var Firestore = require('[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)');
    
    

Create a client that uses [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/production#providing_credentials_to_your_application):
    
    
    var firestore = new Firestore();
    
    

Create a client with [explicit credentials](https://cloud.google.com/docs/authentication/production#obtaining_and_providing_service_account_credentials_manually):
    
    
    var firestore = new Firestore({ projectId:
    'your-project-id', keyFilename: '/path/to/keyfile.json'
    });
    
    

Full quickstart example: Placeholder: the quickstart sample (samples/quickstart.js, region tag firestore_quickstart) is not currently available.

## Constructors 

### (constructor)(settings)
    
    
    constructor(settings?: firestore.Settings);

Constructs a new instance of the `Firestore` class

**Parameter**  
---  
**Name** | **Description**  
`settings` |  `firestore.Settings`   
[Configuration object](#/docs).  
  
## Properties 

### databaseId
    
    
    get databaseId(): string;

Returns the Database ID for this Firestore instance.

## Methods 

### batch()
    
    
    batch(): WriteBatch;

Creates a [WriteBatch][WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch), used for performing multiple writes as a single atomic operation.

**Returns**  
---  
**Type** | **Description**  
`[WriteBatch](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writebatch)` | {WriteBatch} A WriteBatch that operates on this Firestore client.  
**Example**
    
    
    let writeBatch = firestore.batch();
    
    // Add two documents in an atomic batch.
    let data = { foo: 'bar' };
    writeBatch.set(firestore.doc('col/doc1'), data);
    writeBatch.set(firestore.doc('col/doc2'), data);
    
    writeBatch.commit().then(res => {
      console.log('Successfully executed batch.');
    });
    

### bulkWriter(options)
    
    
    bulkWriter(options?: firestore.BulkWriterOptions): BulkWriter;

Creates a [BulkWriter][BulkWriter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter), used for performing multiple writes in parallel. Gradually ramps up writes as specified by the 500/50/5 rule.

If you pass `BulkWriterOptions`, you can configure the throttling rates for the created BulkWriter.

**Parameter**  
---  
**Name** | **Description**  
`options` |  `firestore.BulkWriterOptions`   
BulkWriter options.  
**Returns**  
---  
**Type** | **Description**  
`[BulkWriter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter)` | {BulkWriter} A BulkWriter that operates on this Firestore client.  
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    
    bulkWriter.create(firestore.doc('col/doc1'), {foo: 'bar'})
      .then(res => {
        console.log(`Added document at ${res.writeTime}`);
      });
    bulkWriter.update(firestore.doc('col/doc2'), {foo: 'bar'})
      .then(res => {
        console.log(`Updated document at ${res.writeTime}`);
      });
    bulkWriter.delete(firestore.doc('col/doc3'))
      .then(res => {
        console.log(`Deleted document at ${res.writeTime}`);
      });
    await bulkWriter.close().then(() => {
      console.log('Executed all writes');
    });
    

### bundle(name)
    
    
    bundle(name?: string): BundleBuilder;

Creates a new `BundleBuilder` instance to package selected Firestore data into a bundle.

**Parameter**  
---  
**Name** | **Description**  
`name` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`[BundleBuilder](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bundlebuilder)` |   
  
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
`[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)` | {CollectionReference} The [CollectionReference][CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference) instance.  
**Example**
    
    
    let collectionRef = firestore.collection('collection');
    
    // Add a document with an auto-generated ID.
    collectionRef.add({foo: 'bar'}).then((documentRef) => {
      console.log(`Added document at ${documentRef.path})`);
    });
    

### collectionGroup(collectionId)
    
    
    collectionGroup(collectionId: string): CollectionGroup;

Creates and returns a new Query that includes all documents in the database that are contained in a collection or subcollection with the given collectionId.

**Parameter**  
---  
**Name** | **Description**  
`collectionId` |  `string`   
Identifies the collections to query over. Every collection or subcollection with this ID as the last segment of its path will be included. Cannot contain a slash.  
**Returns**  
---  
**Type** | **Description**  
`[CollectionGroup](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectiongroup)` | {CollectionGroup} The created CollectionGroup.  
**Example**
    
    
    let docA = firestore.doc('mygroup/docA').set({foo: 'bar'});
    let docB = firestore.doc('abc/def/mygroup/docB').set({foo: 'bar'});
    
    Promise.all([docA, docB]).then(() => {
       let query = firestore.collectionGroup('mygroup');
       query = query.where('foo', '==', 'bar');
       return query.get().then(snapshot => {
          console.log(`Found ${snapshot.size} documents.`);
       });
    });
    

### doc(documentPath)
    
    
    doc(documentPath: string): DocumentReference;

Gets a [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference) instance that refers to the document at the specified path.

**Parameter**  
---  
**Name** | **Description**  
`documentPath` |  `string`   
A slash-separated path to a document.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)` | {DocumentReference} The [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference) instance.  
**Example**
    
    
    let documentRef = firestore.doc('collection/document');
    console.log(`Path of document is ${documentRef.path}`);
    

### getAll(documentRefsOrReadOptions)
    
    
    getAll<AppModelType, DbModelType extends firestore.DocumentData>(...documentRefsOrReadOptions: Array<firestore.DocumentReference<AppModelType, DbModelType> | firestore.ReadOptions>): Promise<Array<DocumentSnapshot<AppModelType, DbModelType>>>;

Retrieves multiple documents from Firestore.

The first argument is required and must be of type `DocumentReference` followed by any additional `DocumentReference` documents. If used, the optional `ReadOptions` must be the last argument.

**Parameter**  
---  
**Name** | **Description**  
`documentRefsOrReadOptions` |  `Array<FirebaseFirestore.DocumentReference<AppModelType, DbModelType> | FirebaseFirestore.ReadOptions>`   
The `DocumentReferences` to receive, followed by an optional field mask.  
**Returns**  
---  
**Type** | **Description**  
`Promise<Array<[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)<AppModelType, DbModelType>>>` | {Promise<Array.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let docRef1 = firestore.doc('col/doc1');
    let docRef2 = firestore.doc('col/doc2');
    
    firestore.getAll(docRef1, docRef2, { fieldMask: ['user'] }).then(docs => {
      console.log(`First document: ${JSON.stringify(docs[0])}`);
      console.log(`Second document: ${JSON.stringify(docs[1])}`);
    });
    

### listCollections()
    
    
    listCollections(): Promise<CollectionReference[]>;

Fetches the root collections that are associated with this Firestore database.

**Returns**  
---  
**Type** | **Description**  
`Promise<[CollectionReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/collectionreference)[]>` | {Promise.<Array.  
**Example**
    
    
    firestore.listCollections().then(collections => {
      for (let collection of collections) {
        console.log(`Found collection with id: ${collection.id}`);
      }
    });
    

### pipeline()
    
    
    pipeline(): PipelineSource;

Creates and returns a new PipelineSource, which allows specifying the source stage of a `Pipeline`.

**Returns**  
---  
**Type** | **Description**  
`[PipelineSource](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesource)` |   
**Example**
    
    
    let myPipeline: Pipeline = firestore.pipeline().collection('books');
    

### recursiveDelete(ref, bulkWriter)
    
    
    recursiveDelete(ref: firestore.CollectionReference<any, any> | firestore.DocumentReference<any, any>, bulkWriter?: BulkWriter): Promise<void>;

Recursively deletes all documents and subcollections at and under the specified level.

If any delete fails, the promise is rejected with an error message containing the number of failed deletes and the stack trace of the last failed delete. The provided reference is deleted regardless of whether all deletes succeeded.

`recursiveDelete()` uses a BulkWriter instance with default settings to perform the deletes. To customize throttling rates or add success/error callbacks, pass in a custom BulkWriter instance.

**Parameters**  
---  
**Name** | **Description**  
`ref` |  `FirebaseFirestore.CollectionReference<any, any> | FirebaseFirestore.DocumentReference<any, any>`   
The reference of a document or collection to delete.  
`bulkWriter` |  `[BulkWriter](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter)`   
A custom BulkWriter instance used to perform the deletes.  
**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | A promise that resolves when all deletes have been performed. The promise is rejected if any of the deletes fail.  
**Example**
    
    
    // Recursively delete a reference and log the references of failures.
    const bulkWriter = firestore.bulkWriter();
    bulkWriter
      .onWriteError((error) => {
        if (
          error.failedAttempts < max_retry_attempts="" )="" {="" return="" true;="" }="" else="" {="" console.log('failed="" write="" at="" document:="" ',="" error.documentref.path);="" return="" false;="" }="" });="" await="" firestore.recursivedelete(docref,="" bulkwriter);="">

### runTransaction(updateFunction, transactionOptions)
    
    
    runTransaction<T>(updateFunction: (transaction: Transaction) => Promise<T>, transactionOptions?: firestore.ReadWriteTransactionOptions | firestore.ReadOnlyTransactionOptions): Promise<T>;

Executes the given updateFunction and commits the changes applied within the transaction.

You can use the transaction object passed to 'updateFunction' to read and modify Firestore documents under lock. You have to perform all reads before before you perform any write.

Transactions can be performed as read-only or read-write transactions. By default, transactions are executed in read-write mode.

A read-write transaction obtains a pessimistic lock on all documents that are read during the transaction. These locks block other transactions, batched writes, and other non-transactional writes from changing that document. Any writes in a read-write transactions are committed once 'updateFunction' resolves, which also releases all locks.

If a read-write transaction fails with contention, the transaction is retried up to five times. The `updateFunction` is invoked once for each attempt.

Read-only transactions do not lock documents. They can be used to read documents at a consistent snapshot in time, which may be up to 60 seconds in the past. Read-only transactions are not retried.

Transactions time out after 60 seconds if no documents are read. Transactions that are not committed within than 270 seconds are also aborted. Any remaining locks are released when a transaction times out.

T

**Parameters**  
---  
**Name** | **Description**  
`updateFunction` |  `(transaction: [Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)) => Promise<T>`   
The user function to execute within the transaction context.  
`transactionOptions` |  `FirebaseFirestore.ReadWriteTransactionOptions | FirebaseFirestore.ReadOnlyTransactionOptions`   
Transaction options.  
**Returns**  
---  
**Type** | **Description**  
`Promise<T>` | {Promise  
**Type Parameter**  
---  
**Name** | **Description**  
`T` |   
**Example**
    
    
    let counterTransaction = firestore.runTransaction(transaction => {
      let documentRef = firestore.doc('col/doc');
      return transaction.get(documentRef).then(doc => {
        if (doc.exists) {
          let count =  doc.get('count') || 0;
          if (count > 10) {
            return Promise.reject('Reached maximum count');
          }
          transaction.update(documentRef, { count: ++count });
          return Promise.resolve(count);
        }
    
        transaction.create(documentRef, { count: 1 });
        return Promise.resolve(1);
      });
    });
    
    counterTransaction.then(res => {
      console.log(`Count updated to ${res}`);
    });
    

### settings(settings)
    
    
    settings(settings: firestore.Settings): void;

Specifies custom settings to be used to configure the `Firestore` instance. Can only be invoked once and before any other Firestore method.

If settings are provided via both `settings()` and the `Firestore` constructor, both settings objects are merged and any settings provided via `settings()` take precedence.

**Parameter**  
---  
**Name** | **Description**  
`settings` |  `firestore.Settings`   
The settings to use for all Firestore operations.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### snapshot_(documentName, readTime, encoding)
    
    
    snapshot_(documentName: string, readTime?: google.protobuf.ITimestamp, encoding?: 'protobufJS'): DocumentSnapshot;

Creates a [DocumentSnapshot][DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot) or a [QueryDocumentSnapshot][QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot) from a `firestore.v1.Document` proto (or from a resource name for missing documents).

This API is used by Google Cloud Functions and can be called with both 'Proto3 JSON' and 'Protobuf JS' encoded data.

**Parameters**  
---  
**Name** | **Description**  
`documentName` |  `string`   
  
`readTime` |  `google.protobuf.ITimestamp`   
A 'Timestamp' proto indicating the time this document was read.  
`encoding` |  `'protobufJS'`   
One of 'json' or 'protobufJS'. Applies to both the 'document' Proto and 'readTime'. Defaults to 'protobufJS'.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)` | A QueryDocumentSnapshot for existing documents, otherwise a DocumentSnapshot.  
  
### snapshot_(documentName, readTime, encoding)
    
    
    snapshot_(documentName: string, readTime: string, encoding: 'json'): DocumentSnapshot;

**Parameters**  
---  
**Name** | **Description**  
`documentName` |  `string`   
  
`readTime` |  `string`   
  
`encoding` |  `'json'`   
  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)` |   
  
### snapshot_(document, readTime, encoding)
    
    
    snapshot_(document: api.IDocument, readTime: google.protobuf.ITimestamp, encoding?: 'protobufJS'): QueryDocumentSnapshot;

**Parameters**  
---  
**Name** | **Description**  
`document` |  `api.IDocument`   
  
`readTime` |  `google.protobuf.ITimestamp`   
  
`encoding` |  `'protobufJS'`   
  
**Returns**  
---  
**Type** | **Description**  
`[QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot)` |   
  
### snapshot_(document, readTime, encoding)
    
    
    snapshot_(document: {
            [k: string]: unknown;
        }, readTime: string, encoding: 'json'): QueryDocumentSnapshot;

**Parameters**  
---  
**Name** | **Description**  
`document` |  `{ [k: string]: unknown; }`   
  
`readTime` |  `string`   
  
`encoding` |  `'json'`   
  
**Returns**  
---  
**Type** | **Description**  
`[QueryDocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querydocumentsnapshot)` |   
  
### terminate()
    
    
    terminate(): Promise<void>;

Terminates the Firestore client and closes all open streams.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | A Promise that resolves when the client is terminated.  
  
### toJSON()
    
    
    toJSON(): object;

Returns the Project ID to serve as the JSON representation of this Firestore instance.

**Returns**  
---  
**Type** | **Description**  
`object` | An object that contains the project ID (or `undefined` if not yet available).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
