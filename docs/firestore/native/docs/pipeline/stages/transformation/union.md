---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/union/
title: Union (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:37.485317+00:00
---

# Union (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/union/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Union (Transformation Stage)

## Description

Merges the documents from another pipeline with those in the current pipeline.

## Examples

##### Node.js
    
    
      const results = await db.pipeline()
        .collection("cities/SF/restaurants")
        .where(eq("type", "chinese"))
        .union(db.pipeline()
          .collection("cities/NYC/restaurants")
          .where(eq("type", "italian")))
        .where(gte("rating", 4.5))
        .execute();
        

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("cities/SF/restaurants")
      .where(field("type").equal("Chinese"))
      .union(db.pipeline()
        .collection("cities/NY/restaurants")
        .where(field("type").equal("Italian")))
      .where(field("rating").greaterThanOrEqual(4.5))
      .sort(field("__name__").descending())
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2518-L2526)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("cities/SF/restaurants")
      .where(Field("type").equal("Chinese"))
      .union(with: db.pipeline()
        .collection("cities/NY/restaurants")
        .where(Field("type").equal("Italian")))
      .where(Field("rating").greaterThanOrEqual(4.5))
      .sort([Field("__name__").descending()])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L417-L425)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(db.pipeline()
            .collection("cities/NY/restaurants")
            .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(field("__name__").descending())
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1739-L1747)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(db.pipeline()
            .collection("cities/NY/restaurants")
            .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(field("__name__").descending())
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1985-L1993)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    results = (
        client.pipeline()
        .collection("cities/SF/restaurants")
        .where(Field.of("type").equal("Chinese"))
        .union(
            client.pipeline()
            .collection("cities/NY/restaurants")
            .where(Field.of("type").equal("Italian"))
        )
        .where(Field.of("rating").greater_than_or_equal(4.5))
        .sort(Field.of("__name__").descending())
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L476-L490)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("cities/SF/restaurants")
            .where(field("type").equal("Chinese"))
            .union(
                firestore
                    .pipeline()
                    .collection("cities/NY/restaurants")
                    .where(field("type").equal("Italian")))
            .where(field("rating").greaterThanOrEqual(4.5))
            .sort(descending(field("__name__")))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L492-L505)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("cities/SF/restaurants").
    	Where(firestore.FieldOf("type").Equal("Chinese")).
    	Union(
    		client.Pipeline().
    			Collection("cities/NY/restaurants").
    			Where(firestore.FieldOf("type").Equal("Italian")),
    	).
    	Where(firestore.FieldOf("rating").GreaterThanOrEqual(4.5)).
    	Sort(firestore.Orders(firestore.Descending(firestore.FieldOf("__name__")))).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1152-L1162)

## Behavior

This stage runs multiple pipelines in parallel and concatenates the results together.

### Non-Deterministic Order of Results

The order in which results are combined between the two pipelines is non-deterministic. Any perceived order is unstable and shouldn't be relied upon. A following [`sort(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort) stage can be added if a stable order is required.

##### Node.js
    
    
      const results = await db.pipeline()
        .collection("cities/SF/restaurants")
        .where(eq("type", "chinese"))
        .union(db.pipeline()
          .collection("cities/NYC/restaurants")
          .where(eq("type", "italian")))
        .where(gte("rating", 4.5))
        .sort(Field.of("__name__"))
        .execute();
        

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(db.pipeline()
            .collection("cities/NY/restaurants")
            .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(field("__name__").descending())
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1755-L1763)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
        .collection("cities/SF/restaurants")
        .where(field("type").equal("Chinese"))
        .union(db.pipeline()
            .collection("cities/NY/restaurants")
            .where(field("type").equal("Italian")))
        .where(field("rating").greaterThanOrEqual(4.5))
        .sort(field("__name__").descending())
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2001-L2009)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    results = (
        client.pipeline()
        .collection("cities/SF/restaurants")
        .where(Field.of("type").equal("Chinese"))
        .union(
            client.pipeline()
            .collection("cities/NY/restaurants")
            .where(Field.of("type").equal("Italian"))
        )
        .where(Field.of("rating").greater_than_or_equal(4.5))
        .sort(Field.of("__name__").descending())
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L498-L512)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("cities/SF/restaurants")
            .where(field("type").equal("Chinese"))
            .union(
                firestore
                    .pipeline()
                    .collection("cities/NY/restaurants")
                    .where(field("type").equal("Italian")))
            .where(field("rating").greaterThanOrEqual(4.5))
            .sort(descending(field("__name__")))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L512-L525)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("cities/SF/restaurants").
    	Where(firestore.FieldOf("type").Equal("Chinese")).
    	Union(
    		client.Pipeline().
    			Collection("cities/NY/restaurants").
    			Where(firestore.FieldOf("type").Equal("Italian")),
    	).
    	Where(firestore.FieldOf("rating").GreaterThanOrEqual(4.5)).
    	Sort(firestore.Orders(firestore.Descending(firestore.FieldOf("__name__")))).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1176-L1186)

### Duplicate Results

The `union(...)` stage does not deduplicate results. A following [`distinct(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/distinct) or [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate) stage can be added if duplicate results need to be removed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
