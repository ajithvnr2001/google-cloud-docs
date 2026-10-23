---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/type_functions/
title: Type Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:28.694176+00:00
---

# Type Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/type_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Type Functions Reference

## **Type Functions**

Name  | Description   
---|---  
`TYPE` | Returns the type of the value as a `STRING`.   
`IS_TYPE` | Returns `true` if the value matches the specified type.   
  
### TYPE

**Syntax:**
    
    
    type(input: ANY) -> STRING
    

**Description:**

Returns a string representation of the `input` type.

If given an absent value, returns `NULL`.

**Examples:**

`input` | `type(input)`  
---|---  
NULL | `"null"`  
true | `"boolean"`  
1 | `"int32"`  
-3L | `"int64"`  
3.14 | `"float64"`  
2024-01-01T00:00:00Z UTC | `"timestamp"`  
"foo" | `"string"`  
b"foo" | `"bytes"`  
[1, 2] | `"array"`  
{"a": 1} | `"map"`  
`path("c/d")` | `"reference"`  
`vector([1.0, 2.0])` | `"vector"`  
`object_id "a7f2c9d18b3e4509f67c12d8"` | `"object_id"`  
`1.2e9m` | `"decimal128"`  
`regex "/pattern/i"` | `"regex"`  
`bson_timestamp(1732754912, 500)` | `"bson_timestamp"`  
ABSENT | `NULL`  
  
**Client examples**

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("title").notEqual("1984").as("not1984"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1648-L1651)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("title").notEqual("1984").as("not1984"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2925-L2928)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("title").notEqual("1984").as("not1984")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L858-L861)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("title").notEqual("1984").alias("not1984"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2196-L2199)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("title").notEqual("1984").alias("not1984"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2442-L2445)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("title").not_equal("1984").as_("not1984"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1111-L1118)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(notEqual(field("title"), "1984").as("not1984"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1007-L1013)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.NotEqual(firestore.FieldOf("title"), "1984").As("not1984"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L123-L128)

### IS_TYPE

**Syntax:**
    
    
    is_type(input: ANY, type: STRING) -> BOOLEAN
    

**Description:**

Returns `true` if the `input` matches the specified `type`, otherwise `false`. If given an absent `input`, returns `NULL`.

Supported `type` strings are:

  * `"null"`
  * `"boolean"`
  * `"int32"`
  * `"int64"`
  * `"float64"`
  * `"decimal128"`
  * `"number"`
  * `"timestamp"`
  * `"string"`
  * `"bytes"`
  * `"array"`
  * `"map"`
  * `"reference"`
  * `"vector"`
  * `"geo_point"`
  * `"max_key"`
  * `"min_key"`
  * `"object_id"`
  * `"regex"`
  * `"bson_timestamp"`



**Examples:**

`input` | `type` | `is_type(input, type)`  
---|---|---  
NULL | "null" | true  
true | "boolean" | true  
3.14 | "float64" | true  
"foo" | "string" | true  
b"foo" | "string" | false  
[1, 2] | "array" | true  
{"a": 1} | "map" | true  
`vector([1.0, 2.0])` | "vector" | true  
ABSENT | "string" | NULL  
"bar" | "other" | ERROR  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
