---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter/
title: Class BulkWriter (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:33.336227+00:00
---

# Class BulkWriter (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwriter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class BulkWriter (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A Firestore BulkWriter that can be used to perform a large number of writes in parallel.

BulkWriter

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(firestore, options)
    
    
    constructor(firestore: Firestore, options?: firestore.BulkWriterOptions);

Constructs a new instance of the `BulkWriter` class

**Parameters**  
---  
**Name** | **Description**  
`firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
  
`options` |  `firestore.BulkWriterOptions`   
  
  
## Methods 

### close()
    
    
    close(): Promise<void>;

Commits all enqueued writes and marks the BulkWriter instance as closed.

After calling `close()`, calling any method will throw an error. Any retries scheduled as part of an `onWriteError()` handler will be run before the `close()` promise resolves.

Returns a Promise that resolves when there are no more pending writes. The Promise will never be rejected. Calling this method will send all requests. The promise resolves immediately if there are no pending writes.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise  
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    
    bulkWriter.create(documentRef, {foo: 'bar'});
    bulkWriter.update(documentRef2, {foo: 'bar'});
    bulkWriter.delete(documentRef3);
    await close().then(() => {
      console.log('Executed all writes');
    });
    

### create(documentRef, data)
    
    
    create<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.WithFieldValue<AppModelType>): Promise<WriteResult>;

Create a document with the provided data. This single operation will fail if a document exists at its location.

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
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    let documentRef = firestore.collection('col').doc();
    
    bulkWriter
     .create(documentRef, {foo: 'bar'})
     .then(result => {
       console.log('Successfully executed write at: ', result);
     })
     .catch(err => {
       console.log('Write failed with: ', err);
     });
    });
    

### delete(documentRef, precondition)
    
    
    delete<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, precondition?: firestore.Precondition): Promise<WriteResult>;

Delete a document from the database.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be deleted.  
`precondition` |  `firestore.Precondition`   
A precondition to enforce for this delete.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    let documentRef = firestore.doc('col/doc');
    
    bulkWriter
     .delete(documentRef)
     .then(result => {
       console.log('Successfully deleted document');
     })
     .catch(err => {
       console.log('Delete failed with: ', err);
     });
    });
    

### flush()
    
    
    flush(): Promise<void>;

Commits all writes that have been enqueued up to this point in parallel.

Returns a Promise that resolves when all currently queued operations have been committed. The Promise will never be rejected since the results for each individual operation are conveyed via their individual Promises.

The Promise resolves immediately if there are no pending writes. Otherwise, the Promise waits for all previously issued writes, but it does not wait for writes that were added after the method is called. If you want to wait for additional writes, call `flush()` again.

**Returns**  
---  
**Type** | **Description**  
`Promise<void>` | {Promise  
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    
    bulkWriter.create(documentRef, {foo: 'bar'});
    bulkWriter.update(documentRef2, {foo: 'bar'});
    bulkWriter.delete(documentRef3);
    await flush().then(() => {
      console.log('Executed all writes');
    });
    

### onWriteError(shouldRetryCallback)
    
    
    onWriteError(shouldRetryCallback: (error: BulkWriterError) => boolean): void;

Attaches an error handler listener that is run every time a BulkWriter operation fails.

BulkWriter has a default error handler that retries UNAVAILABLE and ABORTED errors up to a maximum of 10 failed attempts. When an error handler is specified, the default error handler will be overwritten.

**Parameter**  
---  
**Name** | **Description**  
`shouldRetryCallback` |  `(error: [BulkWriterError](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/bulkwritererror)) => boolean`   
A callback to be called every time a BulkWriter operation fails. Returning `true` will retry the operation. Returning `false` will stop the retry loop.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    
    bulkWriter
      .onWriteError((error) => {
        if (
          error.code === GrpcStatus.UNAVAILABLE &&
          error.failedAttempts < max_retry_attempts="" )="" {="" return="" true;="" }="" else="" {="" console.log('failed="" write="" at="" document:="" ',="" error.documentref);="" return="" false;="" }="" });="">

### onWriteResult(successCallback)
    
    
    onWriteResult(successCallback: (documentRef: firestore.DocumentReference<any, any>, result: WriteResult) => void): void;

Attaches a listener that is run every time a BulkWriter operation successfully completes.

**Parameter**  
---  
**Name** | **Description**  
`successCallback` |  `(documentRef: FirebaseFirestore.DocumentReference<any, any>, result: [WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)) => void`   
A callback to be called every time a BulkWriter operation successfully completes.  
**Returns**  
---  
**Type** | **Description**  
`void` |   
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    
    bulkWriter
      .onWriteResult((documentRef, result) => {
        console.log(
          'Successfully executed write on document: ',
          documentRef,
          ' at: ',
          result
        );
      });
    

### set(documentRef, data, options)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: Partial<AppModelType>, options: firestore.SetOptions): Promise<WriteResult>;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `Partial<AppModelType>`   
  
`options` |  `firestore.SetOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### set(documentRef, data)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: AppModelType): Promise<WriteResult>;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `AppModelType`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### update(documentRef, dataOrField, preconditionOrValues)
    
    
    update<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, dataOrField: firestore.UpdateData<DbModelType> | string | FieldPath, ...preconditionOrValues: Array<{
            lastUpdateTime?: Timestamp;
        } | unknown | string | FieldPath>): Promise<WriteResult>;

Update fields of the document referred to by the provided [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference). If the document doesn't yet exist, the update fails and the entire batch will be rejected.

The update() method accepts either an object with field paths encoded as keys and field values encoded as values, or a variable number of arguments that alternate between field paths and field values. Nested fields can be updated by providing dot-separated field path strings or by providing FieldPath objects.

A Precondition restricting this update can be specified as the last argument.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be updated.  
`dataOrField` |  `FirebaseFirestore.UpdateData<DbModelType> | string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)`   
An object containing the fields and values with which to update the document or the path of the first field to update.  
`preconditionOrValues` |  `Array<{ lastUpdateTime?: [Timestamp](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/timestamp); } | unknown | string | [FieldPath](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/fieldpath)>`   
An alternating list of field paths and values to update or a Precondition to restrict this update  
**Returns**  
---  
**Type** | **Description**  
`Promise<[WriteResult](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/writeresult)>` | {Promise  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    let bulkWriter = firestore.bulkWriter();
    let documentRef = firestore.doc('col/doc');
    
    bulkWriter
     .update(documentRef, {foo: 'bar'})
     .then(result => {
       console.log('Successfully executed write at: ', result);
     })
     .catch(err => {
       console.log('Write failed with: ', err);
     });
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
