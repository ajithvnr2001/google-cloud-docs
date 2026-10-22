---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/comparison_functions/
title: Comparison Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:06.313505+00:00
---

# Comparison Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/comparison_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Comparison Functions Reference

## **Comparison Functions**

Name  | Description   
---|---  
`EQUAL` | Equality comparison   
`GREATER_THAN` | Greater than comparison   
`GREATER_THAN_OR_EQUAL` | Greater than or equal comparison   
`LESS_THAN` | Less than comparison   
`LESS_THAN_OR_EQUAL` | Less than or equal comparison   
`NOT_EQUAL` | Not equals comparison   
`CMP` | General comparison   
  
### EQUAL

**Syntax:**
    
    
    equal(x: ANY, y: ANY) -> BOOLEAN
    

**Examples:**

`x` | `y` | `equal(x, y)`  
---|---|---  
1L | 1L | `TRUE`  
1.0 | 1L | `TRUE`  
-1.0 | 1L | `FALSE`  
NaN | NaN | `TRUE`  
`NULL` | `NULL` | `TRUE`  
`NULL` | `ABSENT` | `FALSE`  
  
**Description:**

Returns `TRUE` if `x` and `y` are equal, and `FALSE` otherwise.

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").equal(5).as("hasPerfectRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1598-L1601)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").equal(5).as("hasPerfectRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2875-L2878)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").equal(5).as("hasPerfectRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L803-L806)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").equal(5).alias("hasPerfectRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2141-L2144)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").equal(5).alias("hasPerfectRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2387-L2390)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").equal(5).as_("hasPerfectRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1032-L1039)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(equal(field("rating"), 5).as("hasPerfectRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L942-L948)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Equal(firestore.FieldOf("rating"), 5).As("hasPerfectRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L28-L33)

### GREATER_THAN

**Syntax:**
    
    
    greater_than(x: ANY, y: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `x` is greater than `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

`x` | `y` | `greater_than(x, y)`  
---|---|---  
1L | 0.0 | `TRUE`  
1L | 1L | `FALSE`  
1L | 2L | `FALSE`  
"foo" | 0L | `FALSE`  
0L | "foo" | `FALSE`  
NaN | 0L | `FALSE`  
0L | NaN | `FALSE`  
`NULL` | `NULL` | `FALSE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").greaterThan(4).as("hasHighRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1608-L1611)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").greaterThan(4).as("hasHighRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2885-L2888)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").greaterThan(4).as("hasHighRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L814-L817)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").greaterThan(4).alias("hasHighRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2152-L2155)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").greaterThan(4).alias("hasHighRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2398-L2401)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").greater_than(4).as_("hasHighRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1047-L1054)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(greaterThan(field("rating"), 4).as("hasHighRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L955-L961)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.GreaterThan(firestore.FieldOf("rating"), 4).As("hasHighRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L47-L52)

### GREATER_THAN_OR_EQUAL

**Syntax:**
    
    
    greater_than_or_equal(x: ANY, y: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `x` is greater than or equal to `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

`x` | `y` | `greater_than_or_equal(x, y)`  
---|---|---  
1L | 0.0 | `TRUE`  
1L | 1L | `TRUE`  
1L | 2L | `FALSE`  
"foo" | 0L | `FALSE`  
0L | "foo" | `FALSE`  
NaN | 0L | `FALSE`  
0L | NaN | `FALSE`  
`NULL` | `NULL` | `TRUE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1618-L1621)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2895-L2898)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("published").greaterThanOrEqual(1900).as("publishedIn20thCentury")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L825-L828)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("published").greaterThanOrEqual(1900).alias("publishedIn20thCentury"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2163-L2166)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("published").greaterThanOrEqual(1900).alias("publishedIn20thCentury"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2409-L2412)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("published")
            .greater_than_or_equal(1900)
            .as_("publishedIn20thCentury")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1062-L1073)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(greaterThanOrEqual(field("published"), 1900).as("publishedIn20thCentury"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L968-L974)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.GreaterThanOrEqual(firestore.FieldOf("published"), 1900).As("publishedIn20thCentury"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L66-L71)

### LESS_THAN

**Syntax:**
    
    
    less_than(x: ANY, y: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `x` is less than `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

`x` | `y` | `less_than(x, y)`  
---|---|---  
1L | 0.0 | `FALSE`  
1L | 1L | `FALSE`  
1L | 2L | `TRUE`  
"foo" | 0L | `FALSE`  
0L | "foo" | `FALSE`  
NaN | 0L | `FALSE`  
0L | NaN | `FALSE`  
`NULL` | `NULL` | `FALSE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("published").lessThan(1923).as("isPublicDomainProbably"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1628-L1631)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("published").lessThan(1923).as("isPublicDomainProbably"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2905-L2908)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("published").lessThan(1923).as("isPublicDomainProbably")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L836-L839)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("published").lessThan(1923).alias("isPublicDomainProbably"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2174-L2177)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("published").lessThan(1923).alias("isPublicDomainProbably"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2420-L2423)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("published").less_than(1923).as_("isPublicDomainProbably"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1081-L1088)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(lessThan(field("published"), 1923).as("isPublicDomainProbably"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L981-L987)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.LessThan(firestore.FieldOf("published"), 1923).As("isPublicDomainProbably"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L85-L90)

### LESS_THAN_OR_EQUAL

**Syntax:**
    
    
    less_than_or_equal(x: ANY, y: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `x` is less than or equal to `y`, and `FALSE` otherwise.

If `x` and `y` are not comparable, returns `FALSE`.

**Examples:**

`x` | `y` | `less_than(x, y)`  
---|---|---  
1L | 0.0 | `FALSE`  
1L | 1L | `TRUE`  
1L | 2L | `TRUE`  
"foo" | 0L | `FALSE`  
0L | "foo" | `FALSE`  
NaN | 0L | `FALSE`  
0L | NaN | `FALSE`  
`NULL` | `NULL` | `TRUE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").lessThanOrEqual(2).as("hasBadRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1638-L1641)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").lessThanOrEqual(2).as("hasBadRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2915-L2918)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").lessThanOrEqual(2).as("hasBadRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L847-L850)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").lessThanOrEqual(2).alias("hasBadRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2185-L2188)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").lessThanOrEqual(2).alias("hasBadRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2431-L2434)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").less_than_or_equal(2).as_("hasBadRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1096-L1103)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(lessThanOrEqual(field("rating"), 2).as("hasBadRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L994-L1000)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.LessThanOrEqual(firestore.FieldOf("rating"), 2).As("hasBadRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_comparison.go#L104-L109)

### NOT_EQUAL

**Syntax:**
    
    
    not_equal(x: ANY, y: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `x` is not equal to `y`, and `FALSE` otherwise.

**Examples:**

`x` | `y` | `not_equal(x, y)`  
---|---|---  
1L | 1L | `FALSE`  
1.0 | 1L | `FALSE`  
-1.0 | 1L | `TRUE`  
NaN | 0L | `TRUE`  
NaN | NaN | `FALSE`  
`NULL` | `NULL` | `FALSE`  
`NULL` | `ABSENT` | `TRUE`  
  
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

### CMP

**Syntax:**
    
    
    cmp(x: ANY, y: ANY) -> Int64
    

**Description:**

Compares `x` & `y`, returning:

  * `1L` if `x` is greater than `y`.
  * `-1L` if `x` is less than `y`.
  * `0L` otherwise.



Unlike other comparison functions, the `cmp(...)` function works across types, following the same ordering used in the `sort(...)` stage. See [value type order](https://docs.cloud.google.com/firestore/native/docs/concepts/data-types) for how values are ordered across types.

**Examples:**

`x` | `y` | `cmp(x, y)`  
---|---|---  
1L | 1L | 0L  
1.0 | 1L | 0L  
-1.0 | 1L | -1L  
42.5D | "foo" | -1L  
`NULL` | `NULL` | 0L  
`NULL` | `ABSENT` | 0L  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
