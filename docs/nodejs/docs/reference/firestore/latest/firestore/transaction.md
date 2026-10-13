---
url: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction/
title: Class Transaction (9.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:47:37.378542+00:00
---

# Class Transaction (9.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class Transaction (9.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

9.3.1 (latest)  7.11.0  7.9.0  7.7.0  7.6.0  7.5.0  7.4.0  7.3.1  7.2.0  7.1.0  6.4.1  6.3.0  6.0.0  5.0.2  4.15.1  4.14.2  4.9.8 

A reference to a transaction.

The Transaction object passed to a transaction's updateFunction provides the methods to read and write data within the transaction context. See [runTransaction()].

Transaction

## Implements

firestore.Transaction

## Package

[@google-cloud/firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/overview.html)

## Constructors 

### (constructor)(firestore, requestTag, transactionOptions)
    
    
    constructor(firestore: Firestore, requestTag: string, transactionOptions?: firestore.ReadWriteTransactionOptions | firestore.ReadOnlyTransactionOptions);

Constructs a new instance of the `Transaction` class

**Parameters**  
---  
**Name** | **Description**  
`firestore` |  `[Firestore](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/firestore)`   
The Firestore Database client.  
`requestTag` |  `string`   
A unique client-assigned identifier for the scope of this transaction.  
`transactionOptions` |  `FirebaseFirestore.ReadWriteTransactionOptions | FirebaseFirestore.ReadOnlyTransactionOptions`   
The user-defined options for this transaction.  
  
## Methods 

### create(documentRef, data)
    
    
    create<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.WithFieldValue<AppModelType>): Transaction;

Create the document referred to by the provided [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference). The operation will fail the transaction if a document exists at the specified location.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be created.  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
The object data to serialize as the document.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)` | {Transaction} This Transaction instance. Used for chaining method calls.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    firestore.runTransaction(transaction => {
      let documentRef = firestore.doc('col/doc');
      return transaction.get(documentRef).then(doc => {
        if (!doc.exists) {
          transaction.create(documentRef, { foo: 'bar' });
        }
      });
    });
    

### delete(documentRef, precondition)
    
    
    delete(documentRef: DocumentReference<any, any>, precondition?: firestore.Precondition): this;

Deletes the document referred to by the provided [DocumentReference] [DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference).

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `[DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference)<any, any>`   
A reference to the document to be deleted.  
`precondition` |  `firestore.Precondition`   
A precondition to enforce for this delete.  
**Returns**  
---  
**Type** | **Description**  
`this` | {Transaction} This Transaction instance. Used for chaining method calls.  
**Example**
    
    
    firestore.runTransaction(transaction => {
      let documentRef = firestore.doc('col/doc');
      transaction.delete(documentRef);
      return Promise.resolve();
    });
    

### execute(pipeline)
    
    
    execute(pipeline: Pipeline): Promise<PipelineSnapshot>;

Executes this pipeline and returns a Promise to represent the asynchronous operation.

The returned Promise can be used to track the progress of the pipeline execution and retrieve the results (or handle any errors) asynchronously.

The pipeline results are returned in a `PipelineSnapshot` object, which contains a list of `PipelineResult` objects. Each `PipelineResult` typically represents a single key/value map that has passed through all the stages of the pipeline, however this might differ depending on the stages involved in the pipeline. For example:

  * If there are no stages or only transformation stages, each `PipelineResult` represents a single document.
  * If there is an aggregation, only a single `PipelineResult` is returned, representing the aggregated results over the entire dataset .
  * If there is an aggregation stage with grouping, each `PipelineResult` represents a distinct group and its associated aggregated values.



**Parameter**  
---  
**Name** | **Description**  
`pipeline` |  `[Pipeline](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipeline)`   
  
**Returns**  
---  
**Type** | **Description**  
`Promise<[PipelineSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/pipelines.pipelinesnapshot)>` | A Promise representing the asynchronous pipeline execution.  
**Example**
    
    
    typescript
    const futureResults = await transaction
      .execute(
        firestore.pipeline().collection("books")
          .where(greaterThan(field("rating"), 4.5))
          .select("title", "author", "rating"));
    

### get(query)
    
    
    get<AppModelType, DbModelType extends firestore.DocumentData>(query: firestore.Query<AppModelType, DbModelType>): Promise<QuerySnapshot<AppModelType, DbModelType>>;

Retrieves a query result. Holds a pessimistic lock on all returned documents.

**Parameter**  
---  
**Name** | **Description**  
`query` |  `FirebaseFirestore.Query<AppModelType, DbModelType>`   
A query to execute.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[QuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/querysnapshot)<AppModelType, DbModelType>>` | {Promise  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### get(documentRef)
    
    
    get<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>): Promise<DocumentSnapshot<AppModelType, DbModelType>>;

Reads the document referenced by the provided `DocumentReference.` Holds a pessimistic lock on the returned document.

**Parameter**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be read.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[DocumentSnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentsnapshot)<AppModelType, DbModelType>>` | {Promise  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### get(aggregateQuery)
    
    
    get<AppModelType, DbModelType extends firestore.DocumentData, AggregateSpecType extends firestore.AggregateSpec>(aggregateQuery: firestore.AggregateQuery<AggregateSpecType, AppModelType, DbModelType>): Promise<AggregateQuerySnapshot<AggregateSpecType, AppModelType, DbModelType>>;

Retrieves an aggregate query result. Holds a pessimistic lock on all documents that were matched by the underlying query.

**Parameter**  
---  
**Name** | **Description**  
`aggregateQuery` |  `FirebaseFirestore.AggregateQuery<AggregateSpecType, AppModelType, DbModelType>`   
An aggregate query to execute.  
**Returns**  
---  
**Type** | **Description**  
`Promise<[AggregateQuerySnapshot](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/aggregatequerysnapshot)<AggregateSpecType, AppModelType, DbModelType>>` | An AggregateQuerySnapshot for the retrieved data.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
`AggregateSpecType` |   
  
### getAll(documentRefsOrReadOptions)
    
    
    getAll<AppModelType, DbModelType extends firestore.DocumentData>(...documentRefsOrReadOptions: Array<firestore.DocumentReference<AppModelType, DbModelType> | firestore.ReadOptions>): Promise<Array<DocumentSnapshot<AppModelType, DbModelType>>>;

Retrieves multiple documents from Firestore. Holds a pessimistic lock on all returned documents.

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
    
    
    let firstDoc = firestore.doc('col/doc1');
    let secondDoc = firestore.doc('col/doc2');
    let resultDoc = firestore.doc('col/doc3');
    
    firestore.runTransaction(transaction => {
      return transaction.getAll(firstDoc, secondDoc).then(docs => {
        transaction.set(resultDoc, {
          sum: docs[0].get('count') + docs[1].get('count')
        });
      });
    });
    

### set(documentRef, data, options)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.PartialWithFieldValue<AppModelType>, options: firestore.SetOptions): Transaction;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `FirebaseFirestore.PartialWithFieldValue<AppModelType>`   
  
`options` |  `firestore.SetOptions`   
  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### set(documentRef, data)
    
    
    set<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, data: firestore.WithFieldValue<AppModelType>): Transaction;

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
  
`data` |  `FirebaseFirestore.WithFieldValue<AppModelType>`   
  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)` |   
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
  
### update(documentRef, dataOrField, preconditionOrValues)
    
    
    update<AppModelType, DbModelType extends firestore.DocumentData>(documentRef: firestore.DocumentReference<AppModelType, DbModelType>, dataOrField: firestore.UpdateData<DbModelType> | string | firestore.FieldPath, ...preconditionOrValues: Array<firestore.Precondition | unknown | string | firestore.FieldPath>): Transaction;

Updates fields in the document referred to by the provided [DocumentReference][DocumentReference](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/documentreference). The update will fail if applied to a document that does not exist.

The update() method accepts either an object with field paths encoded as keys and field values encoded as values, or a variable number of arguments that alternate between field paths and field values. Nested fields can be updated by providing dot-separated field path strings or by providing FieldPath objects.

A Precondition restricting this update can be specified as the last argument.

**Parameters**  
---  
**Name** | **Description**  
`documentRef` |  `FirebaseFirestore.DocumentReference<AppModelType, DbModelType>`   
A reference to the document to be updated.  
`dataOrField` |  `FirebaseFirestore.UpdateData<DbModelType> | string | FirebaseFirestore.FieldPath`   
An object containing the fields and values with which to update the document or the path of the first field to update.  
`preconditionOrValues` |  `Array<FirebaseFirestore.Precondition | unknown | string | FirebaseFirestore.FieldPath>`   
An alternating list of field paths and values to update or a Precondition to to enforce on this update.  
**Returns**  
---  
**Type** | **Description**  
`[Transaction](https://docs.cloud.google.com/nodejs/docs/reference/firestore/latest/firestore/transaction)` | {Transaction} This Transaction instance. Used for chaining method calls.  
**Type Parameters**  
---  
**Name** | **Description**  
`AppModelType` |   
`DbModelType` |   
**Example**
    
    
    firestore.runTransaction(transaction => {
      let documentRef = firestore.doc('col/doc');
      return transaction.get(documentRef).then(doc => {
        if (doc.exists) {
          transaction.update(documentRef, { count: doc.get('count') + 1 });
        } else {
          transaction.create(documentRef, { count: 1 });
        }
      });
    });
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
