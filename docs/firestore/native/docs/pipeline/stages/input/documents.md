---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/documents/
title: Documents (Input Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:27.793386+00:00
---

# Documents (Input Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/documents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Documents (Input Stage)

## Description

Returns documents by looking up a fixed set of predefined documents.

The stage must take one or more documents as input and cannot contain documents with duplicate paths. If a referenced document does not exist, no results will be produced for that document path.

This stage behaves similar to Firestore's `batchGet` and allows filtering on the results directly rather than performing post-filtering steps after the batch operation.

## Examples

### Web
    
    
    const results = await execute(db.pipeline()
      .documents([
        doc(db, "cities", "SF"),
        doc(db, "cities", "DC"),
        doc(db, "cities", "NY")
      ])
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2427-L2433)

##### Swift
    
    
    let results = try await db.pipeline()
      .documents([
        db.collection("cities").document("SF"),
        db.collection("cities").document("DC"),
        db.collection("cities").document("NY")
      ]).execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L324-L329)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .documents(
            db.collection("cities").document("SF"),
            db.collection("cities").document("DC"),
            db.collection("cities").document("NY")
        ).execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1646-L1651)

##### Java  
Android
    
    
          Task<Pipeline.Snapshot> results = db.pipeline()
        .documents(
            db.collection("cities").document("SF"),
            db.collection("cities").document("DC"),
            db.collection("cities").document("NY")
        ).execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1892-L1897)
    
    
        

##### Python
    
    
    results = (
        client.pipeline()
        .documents(
            client.collection("cities").document("SF"),
            client.collection("cities").document("DC"),
            client.collection("cities").document("NY"),
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L377-L385)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .documents(
                firestore.collection("cities").document("SF"),
                firestore.collection("cities").document("DC"),
                firestore.collection("cities").document("NY"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L368-L376)

##### Go
    
    
    snapshot := client.Pipeline().
    	Documents([]*firestore.DocumentRef{
    		client.Collection("cities").Doc("SF"),
    		client.Collection("cities").Doc("DC"),
    		client.Collection("cities").Doc("NY"),
    	}).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L929-L935)

## Behavior

In order to use the `documents(...)` stage, it must appear as the first stage in the pipeline.

The order of documents returned from the `documents(...)` stage is unstable and cannot be relied upon. A subsequent [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage can be used to obtain a deterministic ordering.

For example, for the following documents:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francsico", state: "California"});
    await db.collection("cities").doc("NYC").set({name: "New York City", state: "New York"});
    await db.collection("cities").doc("CHI").set({name: "Chicago", state: "Illinois"});
    

The `documents(...)` stage can be used to retrieve only the `SF` and `NYC` documents and then sort them in ascending order of name.

### Node.js
    
    
    const results = await db.pipeline()
      .documents(
        db.collection("cities").doc("SF"),
        db.collection("cities").doc("NYC"))
      .sort(field("name").ascending())
      .execute();
    

This query produces the following documents:
    
    
      { name: "New York City", state: "New York" }
      { name: "San Francsico", state: "California" }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
