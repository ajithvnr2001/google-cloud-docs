---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/dml/
title: Modify data with Pipeline operations \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:27.622994+00:00
---

# Modify data with Pipeline operations  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/dml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Modify data with Pipeline operations

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the `update(...)` and `delete(...)` Data manipulation language (DML) stages to construct data pipelines that can query for documents and then delete or modify data.

## Edition requirements

The operations described on this page require Firestore Enterprise edition.

## Before you begin

You should be familiar with how to [query a database with Pipeline operations](https://docs.cloud.google.com/firestore/native/docs/pipeline/overview).

## Update documents

Use the [`update(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/dml/update) DML stage to construct data pipelines that can query for documents and then add or modify data.

All DML stages must come at the end of the pipeline. The documents coming into this stage must include the `__name__` field to identify which documents to update. The operation fails if any of the documents you attempt to update don't exist.

For example, the following operation backfills a data model change to all documents in a collection group. The pipeline adds a `preferences.color` field to all all documents in the `users` collection group that are missing that field.

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
    
    [pipeline_snippets_dml.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_dml.go#L28-L36)

## Delete documents

Use the [`delete(...)` stage](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/dml/delete) DML stages to construct data pipelines that can query for documents and then delete data. To prevent accidental bulk deletions, pipelines ending in `delete(...)` should include at least one `where(...)` stage. All DML stages must come at the end of the pipeline.

For example, the following pipeline deletes all `users` documents with `address.users` set to `USA` and with `__create_time__` less than 10 days:

##### Node.js
    
    
    const pipeline = db.pipeline()
      .collectionGroup("users")
      .where(field("address.country").equal("USA"))
      .where(field("__create_time__").timestampAdd("day", 10).lessThan(currentTimestamp()))
      .delete();
    await pipeline.execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2371-L2376)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import CurrentTimestamp, Field
    
    snapshot = (
        client.pipeline()
        .collection_group("users")
        .where(Field.of("address.country").equal("USA"))
        .where(
            Field.of("__create_time__")
            .timestamp_add("day", 10)
            .less_than(CurrentTimestamp())
        )
        .delete()
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L3199-L3212)

##### Java
    
    
    Pipeline.Snapshot deleteResults = firestore.pipeline()
      .collectionGroup("users")
      .where(field("address.country").equal("USA"))
      .where(field("__create_time__").add(constant(10)).lessThan(currentTimestamp()))
      .delete()
      .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/a63ea067b1999ac717b561380fe36d03645484de/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3252-L3257)

##### Go
    
    
    snapshot := client.Pipeline().
    	CollectionGroup("users").
    	Where(firestore.FieldOf("address.country").Equal("USA")).
    	Where(firestore.FieldOf("__create_time__").Add(firestore.ConstantOf(10)).LessThan(firestore.CurrentTimestamp())).
    	Delete().
    	Execute(ctx)
    
    [pipeline_snippets_dml.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_dml.go#L50-L55)

## Consistency

Pipeline operations with `update(...)` and `delete()` stages aren't supported within a transaction. DML stages run outside of a transaction with the following behavior:

  * Each document is updated independently. This means operations are not atomic across documents. The operation fails on first error and partial success is possible.
  * The following stages are supported: 
    * `collection(...)`
    * `collection_group(...)`
    * `where(...)`
    * `select(...)`
    * `add_fields(...)`
    * `remove_fields(...)`
    * `let(...)`
    * `sort(...)`
    * `limit(...)`
    * `offset(...)`
  * The following are stages are not supported: 
    * `aggregate(...)`
    * `distinct(...)`
    * `unnest(...)`
    * `find_nearest(...)`
    * Multi-query stages like `union(...)`, joins, and sub-queries are not allowed before a DML stage.



## Limitations

Note the following limitations for DML stages:

  * DML stages must be the last stages in a pipeline definition before calling `.execute()`.
  * Pipeline operations with `update(...)` and `delete()` stages aren't supported within a transaction.
  * If the stage preceding the DML stage produces multiple documents with the same `__name__`, each instance is processed. For `update(...)`, this means the same target document might be modified multiple times. For `delete(...)`, subsequent attempts after the first will be no-ops.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
