---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/database/
title: Database (Input Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:13.238822+00:00
---

# Database (Input Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/database/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Database (Input Stage)

## Description

Returns all the documents within a database across different collections and nested levels.

## Examples

### Web
    
    
    // Count all documents in the database
    const results = await execute(db.pipeline()
      .database()
      .aggregate(countAll().as("total"))
      );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2416-L2420)

##### Swift
    
    
    // Count all documents in the database
    let results = try await db.pipeline()
      .database()
      .aggregate([CountAll().as("total")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L312-L316)

##### Kotlin  
Android
    
    
    // Count all documents in the database
    val results = db.pipeline()
        .database()
        .aggregate(AggregateFunction.countAll().alias("total"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1634-L1638)

##### Java  
Android
    
    
          // Count all documents in the database
    Task<Pipeline.Snapshot> results = db.pipeline()
        .database()
        .aggregate(AggregateFunction.countAll().alias("total"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1880-L1884)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Count
    
    # Count all documents in the database
    results = client.pipeline().database().aggregate(Count().as_("total")).execute()
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L366-L369)

##### Java
    
    
    // Count all documents in the database
    Pipeline.Snapshot results =
        firestore.pipeline().database().aggregate(countAll().as("total")).execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L359-L361)

##### Go
    
    
    // Count all documents in the database
    snapshot := client.Pipeline().
    	Database().
    	Aggregate(firestore.Accumulators(firestore.CountAll().As("total"))).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_general.go#L911-L915)

## Behavior

In order to use the `database(...)` stage, it must appear as the first stage in the pipeline.

The order of documents returned from the `database(...)` stage is unstable and cannot be relied upon. A subsequent [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage can be used to obtain a deterministic ordering.

For example, for the following documents:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francsico", state: "California", population: 800000});
    await db.collection("states").doc("CA").set({name: "California", population: 39000000});
    await db.collection("countries").doc("USA").set({name: "United States of America", population: 340000000});
    

The `database(...)` stage can be used to retrieve all the documents in the database.

### Node.js
    
    
    const results = await db.pipeline()
      .database()
      .sort(field("population").ascending())
      .execute();
    

This query produces the following documents:
    
    
      { name: "San Francsico", state: "California", population: 800000 }
      { name: "California", population: 39000000 }
      { name: "United States of America", population: 340000000 }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
