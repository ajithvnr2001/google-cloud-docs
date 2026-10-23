---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/output/update/
title: Update (Output Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:48.457323+00:00
---

# Update (Output Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/output/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Update (Output Stage)

## Description

`update(...)` is a Data manipulation language (DML) stage that updates existing documents in Firestore. This stage can be attached to the end of a query to update fields on all documents referenced by the preceding stage.

## Examples

### Backfill a schema change

For example, the following operation backfills a data model change to all documents in a collection group. The pipeline adds a `preferences.color` field to all documents in the `users` collection group that are missing that field.

##### Node.js
    
    
    const snapshot = await db.pipeline()
       .collectionGroup("users")
       .where(not(exists(field("preferences.color"))))
       .addFields(constant(null).as("preferences.color"))
       .removeFields("color")
       .update()
       .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2360-L2366)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Constant, Field, Not
    
    snapshot = (
        client.pipeline()
        .collection_group("users")
        .where(Not(Field.of("preferences.color").exists()))
        .add_fields(Constant.of(None).as_("preferences.color"))
        .remove_fields("color")
        .update()
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L3166-L3176)

##### Java
    
    
    Pipeline.Snapshot snapshot = firestore.pipeline()
       .collectionGroup("users")
       .where(not(exists(field("preferences.color"))))
       .addFields(constant((String) null).as("preferences.color"))
       .removeFields("color")
       .update()
       .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/a63ea067b1999ac717b561380fe36d03645484de/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3241-L3247)

##### Go
    
    
    snapshot := client.Pipeline().
    	CollectionGroup("users").
    	Where(firestore.Not(firestore.FieldExists(firestore.FieldOf("preferences.color")))).
    	AddFields(firestore.Selectables(
    		firestore.ConstantOfNull().As("preferences.color"),
    	)).
    	RemoveFields(firestore.Fields("color")).
    	Update().
    	Execute(ctx)
    
    [pipeline_snippets_dml.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_dml.go#L28-L36)

## Behavior

The following sections describe the execution behavior, responses, and restrictions for the `update(...)` stage.

### Final Stage

All data manipulation language (DML) stages must come at the end of the pipeline, no further stages can be attached.

### `__name__` Required

The documents coming into this stage must include the `__name__` field to identify which documents to update. The operation fails if any of the documents don't exist. Most Input stages (like [`collection(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection), [`collection_group(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection_group), [`database(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/database), and [`documents(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/documents)) include the `__name__` field by default.

### Optional Field Transformations

You can optionally provide `transformations` to apply right before writing the documents. These act identically to adding an [`add_fields(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields) right before the final output stage and the expressions run in the context of the previous documents.

### Update from Aggregation Subqueries

The `update()` stage can be used with aggregation subqueries and scalar functions to update documents based on dynamically computed values, such as identifying if a user has the top score. This pattern must be executed within a user transaction.

##### Node.js

```js const results = await db.runTransaction(async (transaction) => { return transaction.execute( db.pipeline() .collection("users") .where( field("score").equal( scalar( db.pipeline() .collection("scores") .aggregate({ accumulators: [max(field("points")).as("max_points")] }) .select(field("max_points")) ) ) ) .update([constant(true).as("is_top_scorer")]) ); }); ``` 

##### Java

```java Pipeline pipeline = db.pipeline() .collection("users") .where( eq( field("score"), scalar( db.pipeline() .collection("scores") .aggregate(max(field("points")).as("max_points")) .select(field("max_points"))))) .update(new Update(constant(true).as("is_top_scorer"))); db.runTransaction(transaction -> { transaction.execute(pipeline); return null; }); ``` 

### Response

The response includes a summary of the number of documents modified. For example, the following response confirms that the pipeline modified three documents:
    
    
    {documents_modified: 3L}
    

### Limitations

  * DML stages can now be run within transactions. The `insert()` and `upsert()` stages need to be run within a transaction in most cases.

  * When executing a pipeline with DML stages within a new transaction, you can use the `atomic` option to automatically run within a transaction and commit upon successful execution of the pipeline.

  * When running within a transaction, there are no restrictions on other stages (such as `where`, `addFields`, `union`, `findNearest`, and `aggregate` subqueries). Transactional DML operations are bounded by Firestore Enterprise edition transaction limits. Because transactions don't allow reads after the first write, you cannot call a DML pipeline multiple times within a single transaction or read documents after a DML pipeline executes. Attempting to execute a read after a DML write fails with a `FAILED_PRECONDITION` error: `Cannot have reads after the first write in a Firestore transaction.`

  * When running outside of a transaction:

    * Each document is updated independently of each other, and writes are not atomic across documents. The pipeline halts on the first error, allowing for partial success to occur.
    * Advanced multi-query stages (`aggregate`, `distinct`, `unnest`, `find_nearest`, `union`, joins, and subqueries) are not supported.
  * Under Firebase Security Rules, each batch of documents re-evaluates rules and executes lookups. If rules use `get()` or `exists()`, the global 20-lookup limit is reached after writing approximately 200 documents, and the operation fails with `PERMISSION_DENIED`. Use Custom Claims instead of `get()` / `exists()` lookups to avoid this limit.

  * If the stage preceding the DML stage produces multiple documents with the same `__name__` or evaluates to the same destination document ID, each mutation is processed sequentially:

    * For `upsert(...)` and `update(...)`: Multiple mutations targeting the same document follow "last one wins" semantics, where the last mutation processed determines the final state of the document.
    * For `delete(...)`: The first attempt deletes the document, and subsequent attempts for the same document are no-ops.
    * For `insert(...)`: The first attempt creates the document, and subsequent attempts targeting the same document ID fail with an `ALREADY_EXISTS` error.



### Transactional Execution

DML operations can be executed as part of a read-write transaction by either providing an explicit transaction to the pipeline execution call or by using the `atomic` option.

Firestore transactions require all reads to execute before any writes. Because a DML pipeline executes writes, you cannot perform reads (such as document lookups or query reads) after running a DML pipeline in the same transaction. For example, you cannot call a DML pipeline multiple times in a single transaction. Attempting to read after a DML pipeline executes fails with a `FAILED_PRECONDITION` error: `Cannot have reads after the first write in a Firestore transaction.`

#### Using an explicit transaction

##### Node.js

```js // Execute a pipeline with DML stage within an explicit transaction const pipeline = db.pipeline() .collection("users") .where(field("active").equal(false)) .addFields(constant("inactive").as("status")) .update(); await db.runTransaction(async (transaction) => { return transaction.execute(pipeline); }); ``` 

##### Java

```java // Execute a pipeline with DML stage within an explicit transaction Pipeline pipeline = db.pipeline() .collection("users") .where(field("active").equal(false)) .addFields(constant("inactive").as("status")) .update(); db.runTransaction(transaction -> { transaction.execute(pipeline); return null; }); ``` 

#### Using the `atomic` option

##### Node.js

```js // Execute a pipeline const results = await db.pipeline() .collection("users") .where(field("active").equal(false)) .addFields(constant("inactive").as("status")) .update() .execute({ atomic: true }); ``` 

##### Java

```java // Execute a pipeline passing atomic option to execute() Pipeline pipeline = db.pipeline() .collection("users") .where(field("active").equal(false)) .addFields(constant("inactive").as("status")) .update(); pipeline.execute(new PipelineExecuteOptions().withAtomic(true)); ``` 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
