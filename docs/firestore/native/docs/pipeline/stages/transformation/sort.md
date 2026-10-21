---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort/
title: Sort (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:10.330372+00:00
---

# Sort (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sort/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sort (Transformation Stage)

## Description

Sorts the input documents based on one or more specified sort orderings.

## Examples

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("books")
      .sort(
        field("release_date").descending(), field("author").ascending()
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2265-L2270)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("books")
      .sort([
        Field("release_date").descending(), Field("author").ascending()
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L173-L178)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("books")
        .sort(
            field("release_date").descending(),
            field("author").ascending()
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1493-L1499)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
        .collection("books")
        .sort(
            field("release_date").descending(),
            field("author").ascending()
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1739-L1745)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    results = (
        client.pipeline()
        .collection("books")
        .sort(Field.of("release_date").descending(), Field.of("author").ascending())
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L183-L190)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("books")
            .sort(descending(field("release_date")), ascending(field("author")))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L201-L207)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Sort(firestore.Orders(
    		firestore.Descending(firestore.FieldOf("release_date")),
    		firestore.Ascending(firestore.FieldOf("author")),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_general.go#L117-L123)

## Behavior

### Sort order

Sort order follows [Firestore's value type order](https://docs.cloud.google.com/firestore/native/docs/concepts/data-types#value_type_ordering)

### Deterministic Order of Results

If there is no `sort` stage in the query, the ordering of the returned results is non-deterministic and may vary between executions. If a `sort` stage is present but the ordering expressions fail to produce a unique ordering among the returned results, the ordering of the returned results may still vary between executions.

For example, sorting cities by the country of the cities, in ascending order against the following dataset:
    
    
    { name: "Los Angeles", state: "CA", country: "USA", population: 3970000 },
    { name: "New York", state: "NY", country: "USA", population: 8530000 }
    { name: "San Francisco", state: "CA", country: "USA", population: 870000 },
    

can produce any permutation of the 3 documents in the dataset because they all have the same country attribute. To produce a deterministic ordering of the results, you can append a sort order on **name** to the order:

### Node.js
    
    
    const results = await db.pipeline()
      .collection("/cities")
      .sort(field("country").ascending(), fieldd("__name__").ascending())
      .execute();
    

This will use the unique document name as the tiebreaker when multiple documents have the same country value. Note that any other fields which together with the country field form a unique key of the document within the collection can be used to produce a deterministic order of results.

### Sorting Equivalent Values

Equivalent values are sorted together but the order of results within the equivalent class are not deterministic according to the Deterministic Order of Results discussion. For example, sorting cities by size, in ascending order against the following dataset:
    
    
    { name: "Los Angeles", state: "CA", country: "USA", size: 3970000 },
    { name: "Mexico City", state: null, country: "Mexico", size: 3970000.0 },
    

can produce any permutation of the 2 documents in the dataset because both documents have the equivalent size value `3970000`.

### Multiple Sort Stages

When the query contains multiple consecutive sort stages, only the last sort stage has an impact on the query results. Note that this is different from the behavior of the `orderBy` clause in the Core API.

### Top-N Sort Optimization

When a [`limit(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit) is used after a `sort`, a top-n sort may be used. This optimization bounds the memory use of the sort stage by allowing it to only store `N` documents at a time—as defined by [`limit(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit)—making the sort more memory-efficient.

### Null and Absent values

If a field specified in an ordering does not exist in a document, its value is sorted as if the value is `null`. For example, sorting cities by the state of the cities, in ascending order against the following dataset:
    
    
    { name: "Los Angeles", state: "CA", country: "USA", population: 3970000 },
    { name: "Mexico City", state: null, country: "Mexico", population: 9200000 },
    { name: "New York", state: "NY", country: "USA", population: 8530000 }
    { name: "San Francisco", state: "CA", country: "USA", population: 870000 },
    { name: "Toronto", country: "Canada", population: 2930000 },
    

produces the following results where the "Toronto" document and the "Mexico City" document are sorted as `null` and before other documents.
    
    
    { name: "Toronto", country: "Canada", population: 2930000 },
    { name: "Mexico City", state: null, country: "Mexico", population: 9200000 },
    { name: "Los Angeles", state: "CA", country: "USA", population: 3970000 },
    { name: "San Francisco", state: "CA", country: "USA", population: 870000 },
    { name: "New York", state: "NY", country: "USA", population: 8530000 }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
