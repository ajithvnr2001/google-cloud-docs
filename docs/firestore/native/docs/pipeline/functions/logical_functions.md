---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/logical_functions/
title: Logical Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:30.391042+00:00
---

# Logical Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/logical_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Logical Functions Reference

## **Logical Functions**

Name  | Description   
---|---  
`AND` | Performs a logical AND   
`OR` | Performs a logical OR   
`XOR` | Performs a logical XOR   
`NOT` | Performs a logical NOT   
`NOR` | Performs a logical NOR   
`CONDITIONAL` | Branches evaluation based on a conditional expression.   
`IF_NULL` | Returns the first non-null value   
`SWITCH_ON` | Branches evaluation based on a series of conditions   
`EQUAL_ANY` | Checks if a value is equal to any elements in an array   
`NOT_EQUAL_ANY` | Checks if a value is not equal to any elements in an array   
`MAXIMUM` | Returns the maximum value in a set of values   
`MINIMUM` | Returns the minimum value in a set of values   
  
### AND

**Syntax:**
    
    
    and(x: BOOLEAN...) -> BOOLEAN
    

**Description:**

Returns the logical AND of two or more boolean values.

Returns `NULL` if the result can't be derived due to any of the given values being `ABSENT` or `NULL`.

**Examples:**

`x` | `y` | `and(x, y)`  
---|---|---  
`TRUE` | `TRUE` | `TRUE`  
`FALSE` | `TRUE` | `FALSE`  
`NULL` | `TRUE` | `NULL`  
`ABSENT` | `TRUE` | `NULL`  
`NULL` | `FALSE` | `FALSE`  
`FALSE` | `ABSENT` | `FALSE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        and(field("rating").greaterThan(4), field("price").lessThan(10))
          .as("under10Recommendation")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1668-L1674)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        and(field("rating").greaterThan(4), field("price").lessThan(10))
          .as("under10Recommendation")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2945-L2951)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        (Field("rating").greaterThan(4) && Field("price").lessThan(10))
          .as("under10Recommendation")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L880-L886)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            Expression.and(field("rating").greaterThan(4),
              field("price").lessThan(10))
                .alias("under10Recommendation")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2218-L2225)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            Expression.and(
                field("rating").greaterThan(4),
                field("price").lessThan(10)
            ).alias("under10Recommendation")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2464-L2472)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field, And
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            And(
                Field.of("rating").greater_than(4), Field.of("price").less_than(10)
            ).as_("under10Recommendation")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1141-L1152)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                and(greaterThan(field("rating"), 4), lessThan(field("price"), 10))
                    .as("under10Recommendation"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1033-L1041)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.And(
    			firestore.GreaterThan(firestore.FieldOf("rating"), 4),
    			firestore.LessThan(firestore.FieldOf("price"), 10),
    		).As("under10Recommendation"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L47-L55)

### OR

**Syntax:**
    
    
    or(x: BOOLEAN...) -> BOOLEAN
    

**Description:**

Returns the logical OR of two or more boolean values.

Returns `NULL` if the result can't be derived due to any of the given values being `ABSENT` or `NULL`.

**Examples:**

`x` | `y` | `or(x, y)`  
---|---|---  
`TRUE` | `TRUE` | `TRUE`  
`FALSE` | `TRUE` | `TRUE`  
`NULL` | `TRUE` | `TRUE`  
`ABSENT` | `TRUE` | `TRUE`  
`NULL` | `FALSE` | `NULL`  
`FALSE` | `ABSENT` | `NULL`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        or(field("genre").equal("Fantasy"), field("tags").arrayContains("adventure"))
          .as("matchesSearchFilters")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1681-L1687)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        or(field("genre").equal("Fantasy"), field("tags").arrayContains("adventure"))
          .as("matchesSearchFilters")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2958-L2964)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        (Field("genre").equal("Fantasy") || Field("tags").arrayContains("adventure"))
          .as("matchesSearchFilters")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L894-L900)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            Expression.or(field("genre").equal("Fantasy"),
              field("tags").arrayContains("adventure"))
                .alias("matchesSearchFilters")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2233-L2240)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            Expression.or(
                field("genre").equal("Fantasy"),
                field("tags").arrayContains("adventure")
            ).alias("matchesSearchFilters")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2480-L2488)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field, And, Or
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Or(
                Field.of("genre").equal("Fantasy"),
                Field.of("tags").array_contains("adventure"),
            ).as_("matchesSearchFilters")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1160-L1172)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                or(equal(field("genre"), "Fantasy"), arrayContains(field("tags"), "adventure"))
                    .as("matchesSearchFilters"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1048-L1056)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Or(
    			firestore.Equal(firestore.FieldOf("genre"), "Fantasy"),
    			firestore.ArrayContains(firestore.FieldOf("tags"), "adventure"),
    		).As("matchesSearchFilters"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L69-L77)

### XOR

**Syntax:**
    
    
    xor(x: BOOLEAN...) -> BOOLEAN
    

**Description:**

Returns the logical XOR of two or more boolean values.

Returns `NULL` if any of the given values are `ABSENT` or `NULL`.

**Examples:**

`x` | `y` | `xor(x, y)`  
---|---|---  
`TRUE` | `TRUE` | `FALSE`  
`FALSE` | `FALSE` | `FALSE`  
`FALSE` | `TRUE` | `TRUE`  
`NULL` | `TRUE` | `NULL`  
`ABSENT` | `TRUE` | `NULL`  
`NULL` | `FALSE` | `NULL`  
`FALSE` | `ABSENT` | `NULL`  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        xor(field("tags").arrayContains("magic"), field("tags").arrayContains("nonfiction"))
          .as("matchesSearchFilters")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2971-L2977)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        xor(field("tags").arrayContains("magic"), field("tags").arrayContains("nonfiction"))
          .as("matchesSearchFilters")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2971-L2977)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        (Field("tags").arrayContains("magic") ^ Field("tags").arrayContains("nonfiction"))
          .as("matchesSearchFilters")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L908-L914)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            Expression.xor(field("tags").arrayContains("magic"),
              field("tags").arrayContains("nonfiction"))
                .alias("matchesSearchFilters")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2248-L2255)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            Expression.xor(
                field("tags").arrayContains("magic"),
                field("tags").arrayContains("nonfiction")
            ).alias("matchesSearchFilters")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2496-L2504)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field, Xor
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Xor(
                [
                    Field.of("tags").array_contains("magic"),
                    Field.of("tags").array_contains("nonfiction"),
                ]
            ).as_("matchesSearchFilters")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1180-L1194)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                xor(
                        arrayContains(field("tags"), "magic"),
                        arrayContains(field("tags"), "nonfiction"))
                    .as("matchesSearchFilters"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1063-L1073)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Xor(
    			firestore.ArrayContains(firestore.FieldOf("tags"), "magic"),
    			firestore.ArrayContains(firestore.FieldOf("tags"), "nonfiction"),
    		).As("matchesSearchFilters"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L91-L99)

### NOR

**Syntax:**
    
    
    nor(x: BOOLEAN...) -> BOOLEAN
    

**Description:**

Returns the logical NOR of two or more boolean values.

Returns `NULL` if the result can't be derived due to any of the given values being `ABSENT` or `NULL`.

**Examples:**

`x` | `y` | `nor(x, y)`  
---|---|---  
`TRUE` | `TRUE` | `FALSE`  
`FALSE` | `TRUE` | `FALSE`  
`FALSE` | `FALSE` | `TRUE`  
`NULL` | `TRUE` | `FALSE`  
`ABSENT` | `TRUE` | `FALSE`  
`NULL` | `FALSE` | `NULL`  
`FALSE` | `ABSENT` | `NULL`  
  
### NOT

**Syntax:**
    
    
    not(x: BOOLEAN) -> BOOLEAN
    

**Description:**

Returns the logical NOT of a boolean value.

##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("tags").arrayContains("nonfiction").not()
          .as("isFiction")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2984-L2990)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("tags").arrayContains("nonfiction").not()
          .as("isFiction")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2984-L2990)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        (!Field("tags").arrayContains("nonfiction"))
          .as("isFiction")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L922-L928)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            Expression.not(
                field("tags").arrayContains("nonfiction")
            ).alias("isFiction")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2263-L2270)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            Expression.not(
                field("tags").arrayContains("nonfiction")
            ).alias("isFiction")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2512-L2519)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field, Not
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Not(Field.of("tags").array_contains("nonfiction")).as_("isFiction"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1202-L1209)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(not(arrayContains(field("tags"), "nonfiction")).as("isFiction"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1080-L1086)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Not(firestore.ArrayContains(firestore.FieldOf("tags"), "nonfiction")).As("isFiction"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L113-L118)

### CONDITIONAL

**Syntax:**
    
    
    conditional(condition: BOOLEAN, true_case: ANY, false_case: ANY) -> ANY
    

**Description:**

Evaluates and returns the `true_case` if the `condition` evaluates to `TRUE`.

Evaluates and returns the `false_case` if the condition resolves to `FALSE`, `NULL`, or an `ABSENT` value.

**Examples:**

`condition` | `true_case` | `false_case` | `conditional(condition, true_case, false_case)`  
---|---|---|---  
`TRUE` | 1L | 0L | 1L  
`FALSE` | 1L | 0L | 0L  
`NULL` | 1L | 0L | 0L  
`ABSENT` | 1L | 0L | 0L  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("tags").arrayConcat([
          field("pages").greaterThan(100)
            .conditional(constant("longRead"), constant("shortRead"))
        ]).as("extendedTags")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2997-L3005)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("tags").arrayConcat([
          field("pages").greaterThan(100)
            .conditional(constant("longRead"), constant("shortRead"))
        ]).as("extendedTags")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2997-L3005)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("tags").arrayConcat([
          ConditionalExpression(
            Field("pages").greaterThan(100),
            then: Constant("longRead"),
            else: Constant("shortRead")
          )
        ]).as("extendedTags")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L936-L947)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("tags").arrayConcat(
                Expression.conditional(
                    field("pages").greaterThan(100),
                    constant("longRead"),
                    constant("shortRead")
                )
            ).alias("extendedTags")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2278-L2289)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("tags").arrayConcat(
                Expression.conditional(
                    field("pages").greaterThan(100),
                    constant("longRead"),
                    constant("shortRead")
                )
            ).alias("extendedTags")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2527-L2538)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import (
        Field,
        Constant,
        Conditional,
    )
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("tags")
            .array_concat(
                Conditional(
                    Field.of("pages").greater_than(100),
                    Constant.of("longRead"),
                    Constant.of("shortRead"),
                )
            )
            .as_("extendedTags")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1217-L1238)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                arrayConcat(
                        field("tags"),
                        conditional(
                            greaterThan(field("pages"), 100),
                            constant("longRead"),
                            constant("shortRead")))
                    .as("extendedTags"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1093-L1106)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayConcat(
    			firestore.FieldOf("tags"),
    			firestore.Conditional(
    				firestore.GreaterThan(firestore.FieldOf("pages"), 100),
    				firestore.ConstantOf("longRead"),
    				firestore.ConstantOf("shortRead"),
    			),
    		).As("extendedTags"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L132-L144)

### IF_NULL

**Syntax:**
    
    
    if_null(expr: ANY, replacement: ANY) -> ANY
    

**Description:**

Returns `expr` if it is not `NULL`, otherwise evaluates and returns `replacement`. The `replacement` expression is not evaluated if `expr` is used.

**Examples:**

`expr` | `replacement` | `if_null(expr, replacement)`  
---|---|---  
1L | 2L | 1L  
`NULL` | 2L | 2L  
`ABSENT` | 2L | `ABSENT`  
  
### SWITCH_ON

**Syntax:**
    
    
    switch_on(cond1: BOOLEAN, res1: ANY, cond2: BOOLEAN, res2: ANY, ..., [default: ANY]) -> ANY
    

**Description:**

Evaluates a series of conditions and returns the result associated with the first `TRUE` condition. If no conditions evaluate to `TRUE`, the `default` value is returned if provided. If no `default` value is provided, an error is thrown if no other conditions evaluated to `TRUE`.

To provide a `default` value, pass it as the final argument such that there is an odd number of arguments.

**Examples:**

`x` | `switch_on(eq(x, 1L), "one", eq(x, 2L), "two", "other")`  
---|---  
1L | "one"  
2L | "two"  
3L | "other"  
  
### EQUAL_ANY

**Syntax:**
    
    
    equal_any(value: ANY, search_space: ARRAY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is in the `search_space` array.

**Examples:**

`value` | `search_space` | `equal_any(value, search_space)`  
---|---|---  
0L | [1L, 2L, 3L] | `FALSE`  
2L | [1L, 2L, 3L] | `TRUE`  
`NULL` | [1L, 2L, 3L] | `FALSE`  
`NULL` | [1L, `NULL`] | `TRUE`  
`ABSENT` | [1L, `NULL`] | `FALSE`  
NaN | [1L, NaN, 3L] | `TRUE`  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
          .as("matchesGenreFilters")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3012-L3018)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
          .as("matchesGenreFilters")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3012-L3018)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("genre").equalAny(["Science Fiction", "Psychological Thriller"])
          .as("matchesGenreFilters")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L955-L961)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("genre").equalAny(listOf("Science Fiction", "Psychological Thriller"))
                .alias("matchesGenreFilters")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2297-L2303)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("genre").equalAny(Arrays.asList("Science Fiction", "Psychological Thriller"))
                .alias("matchesGenreFilters")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2546-L2552)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("genre")
            .equal_any(["Science Fiction", "Psychological Thriller"])
            .as_("matchesGenreFilters")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1246-L1257)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                equalAny(field("genre"), Arrays.asList("Science Fiction", "Psychological Thriller"))
                    .as("matchesGenreFilters"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1113-L1121)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.EqualAny(firestore.FieldOf("genre"), []string{"Science Fiction", "Psychological Thriller"}).As("matchesGenreFilters"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L199-L204)

### NOT_EQUAL_ANY

**Syntax:**
    
    
    not_equal_any(value: ANY, search_space: ARRAY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is not in the `search_space` array.

**Examples:**

`value` | `search_space` | `not_equal_any(value, search_space)`  
---|---|---  
0L | [1L, 2L, 3L] | `TRUE`  
2L | [1L, 2L, 3L] | `FALSE`  
`NULL` | [1L, 2L, 3L] | `TRUE`  
`NULL` | [1L, `NULL`] | `FALSE`  
`ABSENT` | [1L, `NULL`] | `TRUE`  
NaN | [1L, NaN, 3L] | `FALSE`  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
          .as("byExcludedAuthors")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3025-L3031)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
          .as("byExcludedAuthors")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3025-L3031)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("author").notEqualAny(["George Orwell", "F. Scott Fitzgerald"])
          .as("byExcludedAuthors")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L969-L975)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("author").notEqualAny(listOf("George Orwell", "F. Scott Fitzgerald"))
                .alias("byExcludedAuthors")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2311-L2317)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("author").notEqualAny(Arrays.asList("George Orwell", "F. Scott Fitzgerald"))
                .alias("byExcludedAuthors")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2560-L2566)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("author")
            .not_equal_any(["George Orwell", "F. Scott Fitzgerald"])
            .as_("byExcludedAuthors")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1265-L1276)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                notEqualAny(field("author"), Arrays.asList("George Orwell", "F. Scott Fitzgerald"))
                    .as("byExcludedAuthors"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1128-L1136)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.NotEqualAny(firestore.FieldOf("author"), []string{"George Orwell", "F. Scott Fitzgerald"}).As("byExcludedAuthors"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L218-L223)

### MAXIMUM

**Syntax:**
    
    
    maximum(x: ANY...) -> ANY
    maximum(x: ARRAY) -> ANY
    

**Description:**

Returns the maximum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering).

**Examples:**

`x` | `y` | `maximum(x, y)`  
---|---|---  
`FALSE` | `TRUE` | `TRUE`  
`FALSE` | -10L | -10L  
0.0 | -5L | 0.0  
"foo" | "bar" | "foo"  
"foo" | ["foo"] | ["foo"]  
`ABSENT` | `ABSENT` | `NULL`  
`NULL` | `NULL` | `NULL`  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").maximum().as("maximumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2633-L2636)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").maximum().as("maximumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2633-L2636)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("rating").logicalMaximum([1]).as("flooredRating")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L983-L988)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("rating").logicalMaximum(1).alias("flooredRating")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2339-L2344)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("rating").logicalMaximum(1).alias("flooredRating")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2588-L2593)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").logical_maximum(1).as_("flooredRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1284-L1291)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(logicalMaximum(field("rating"), 1).as("flooredRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1143-L1149)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.LogicalMaximum(firestore.FieldOf("rating"), 1).As("flooredRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L158-L163)

### MINIMUM

**Syntax:**
    
    
    minimum(x: ANY...) -> ANY
    minimum(x: ARRAY) -> ANY
    

**Description:**

Returns the minimum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering).

**Examples:**

`x` | `y` | `minimum(x, y)`  
---|---|---  
`FALSE` | `TRUE` | `FALSE`  
`FALSE` | -10L | `FALSE`  
0.0 | -5L | -5L  
"foo" | "bar" | "bar"  
"foo" | ["foo"] | "foo"  
`ABSENT` | `ABSENT` | `NULL`  
`NULL` | `NULL` | `NULL`  
  
##### Node.js
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").minimum().as("minimumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2623-L2626)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").minimum().as("minimumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2623-L2626)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("rating").logicalMinimum([5]).as("cappedRating")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L996-L1001)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("rating").logicalMinimum(5).alias("cappedRating")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2352-L2357)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("rating").logicalMinimum(5).alias("cappedRating")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2601-L2606)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").logical_minimum(5).as_("cappedRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1299-L1306)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(logicalMinimum(field("rating"), 5).as("cappedRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1156-L1162)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.LogicalMinimum(firestore.FieldOf("rating"), 5).As("cappedRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_logical.go#L177-L182)

## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
