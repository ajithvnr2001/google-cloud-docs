---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/map_functions/
title: Map Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:41.034704+00:00
---

# Map Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/map_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Map Functions Reference

## **Map Functions**

Name  | Description   
---|---  
`MAP` | Constructs a map value from a series of key-value pairs   
`MAP_GET` | Returns the value in a map given a specified key   
`MAP_SET` | Returns a copy of a map with a series of updated keys   
`MAP_REMOVE` | Returns a copy of a map with a series of keys removed   
`MAP_MERGE` | Merges a series of maps together.   
`CURRENT_CONTEXT` | Returns the current context as a map.   
`MAP_KEYS` | Returns an array of all keys in a map.   
`MAP_VALUES` | Returns an array of all values in a map.   
`MAP_ENTRIES` | Returns an array of key-value pairs of a map.   
  
### MAP

**Syntax:**
    
    
    map(key: STRING, value: ANY, ...) -> MAP
    

**Description:**

Constructs a map from a series of key-value pairs.

### MAP_GET

**Syntax:**
    
    
    map_get(map: ANY, key: STRING) -> ANY
    

**Description:**

Returns the value in a map given a specified key. Returns an `ABSENT` value if the `key` does not exist in the map, or if the `map` argument is not a `MAP`.

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("awards").mapGet("pulitzer").as("hasPulitzerAward")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1788-L1793)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("awards").mapGet("pulitzer").as("hasPulitzerAward")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3062-L3067)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("awards").mapGet("pulitzer").as("hasPulitzerAward")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1009-L1014)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("awards").mapGet("pulitzer").alias("hasPulitzerAward")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2365-L2370)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("awards").mapGet("pulitzer").alias("hasPulitzerAward")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2614-L2619)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("awards").map_get("pulitzer").as_("hasPulitzerAward"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1314-L1321)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(mapGet(field("awards"), "pulitzer").as("hasPulitzerAward"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1169-L1175)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.MapGet(firestore.FieldOf("awards"), "pulitzer").As("hasPulitzerAward"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_object.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_object.go#L28-L33)

### MAP_SET

**Syntax:**
    
    
    map_set(map: MAP, key: STRING, value: ANY, ...) -> MAP
    

**Description:**

Returns a copy of the `map` value with its contents updated by a series of key-value pairs.

If the given resolves to an absent value, the associated key is removed from the map.

If the `map` argument is not a `MAP`, returns an absent value.

### MAP_REMOVE

**Syntax:**
    
    
    map_remove(map: MAP, key: STRING...) -> MAP
    

**Description:**

Returns a copy of the `map` value with a series of keys removed.

### MAP_MERGE

**Syntax:**
    
    
    map_merge(maps: MAP...) -> MAP
    

Merges the contents of 2 or more maps. If multiple maps have conflicting values, the last value is used.

### CURRENT_CONTEXT

**Syntax:**
    
    
    current_context() -> MAP
    

Returns a map consisting of all available fields in the current point of execution.

### MAP_KEYS

**Syntax:**
    
    
    map_keys(map: MAP) -> ARRAY<STRING>
    

**Description:**

Returns an array containing all keys of the `map` value.

### MAP_VALUES

**Syntax:**
    
    
    map_values(map: MAP) -> ARRAY<ANY>
    

**Description:**

Returns an array containing all values of the `map` value.

### MAP_ENTRIES

**Syntax:**
    
    
    map_entries(map: MAP) -> ARRAY<MAP>
    

**Description:**

Returns an array containing all key-value pairs in the `map` value.

Each key-value pair will be in the form of a map with two entries, `k` and `v`.

**Examples:**

`map` | `map_entries(map)`  
---|---  
{} | []  
{"foo" : 2L} | [{"k": "foo", "v" : 2L}]  
{"foo" : "bar", "bar" : "foo"} | [{"k": "foo", "v" : "bar" }, {"k" : "bar", "v": "foo"}]  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
