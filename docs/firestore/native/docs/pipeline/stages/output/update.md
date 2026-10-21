---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/output/update/
title: Update (Output Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:44.777073+00:00
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

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `update(...)` stage updates existing documents.

## Examples

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
    
    [pipeline_snippets_dml.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/edbc7e6338c19c4a6e788ce685473e8cf2f397e4/firestore/pipeline_snippets_dml.go#L28-L36)

## Behavior

All data manipulation language (DML) stages must come at the end of the pipeline.

The documents coming into this stage must include the `__name__` field to identify which documents to update. The operation fails if any of the documents don't exist. Most Input stages (like [`collection(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection), [`collection_group(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection_group), [`database(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/database), and [`documents(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/documents)) include the `__name__` field by default.

You can optionally provide `transformations` to apply right before writing the documents. These act identically to adding an [`add_fields(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/add_fields) right before the final output stage and the expressions run in the context of the previous documents.

The response includes a summary of the number of documents modified. For example, the following response confirms that the pipeline modified three documents:
    
    
    {documents_modified: 3L}
    

## Limitations

  * DML stages don't support Firestore Security Rules. DML operation attempts through Firestore Security Rules are denied.

  * During the Preview for this feature, you cannot run DML stages in a transaction. For more information on consistency behavior see [Consistency](https://docs.cloud.google.com/firestore/native/docs/pipeline/dml#consistency).

  * If the stage preceding the DML stage produces multiple documents with the same `__name__`, each instance is processed. For `update(...)`, this means the same target document might be modified multiple times. For `delete(...)`, subsequent attempts after the first will be no-ops.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
