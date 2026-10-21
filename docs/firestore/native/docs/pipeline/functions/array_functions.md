---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/array_functions/
title: Array Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:38.236701+00:00
---

# Array Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/array_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Array Functions Reference

## **Array Functions**

Name  | Description   
---|---  
`ARRAY` | Returns an `ARRAY` containing one element for each input argument   
`ARRAY_CONCAT` | Concatenates multiple arrays into a single `ARRAY`  
`ARRAY_CONTAINS` | Returns `TRUE` if a given `ARRAY` contains a particular value   
`ARRAY_CONTAINS_ALL` | Returns `TRUE` if all values are present in the `ARRAY`  
`ARRAY_CONTAINS_ANY` | Returns `TRUE` if any of the values are present in the `ARRAY`  
`ARRAY_FILTER` | Filters out elements from an `ARRAY` that don't satisfy a predicate   
`ARRAY_FIRST` | Returns the first element in an `ARRAY`  
`ARRAY_FIRST_N` | Returns the first `n` elements in an `ARRAY`  
`ARRAY_GET` | Returns the element at a given index in an `ARRAY`  
`ARRAY_INDEX_OF` | Returns the index of the first occurrence of a value in an `ARRAY`  
`ARRAY_INDEX_OF_ALL` | Returns all indexes of a value in an `ARRAY`  
`ARRAY_LENGTH` | Returns the number of elements in an `ARRAY`  
`ARRAY_LAST` | Returns the last element in an `ARRAY`  
`ARRAY_LAST_N` | Returns the last `n` elements in an `ARRAY`  
`ARRAY_REVERSE` | Reverses the order of elements in an `ARRAY`  
`ARRAY_SLICE` | Returns a slice of an `ARRAY`  
`ARRAY_TRANSFORM` | Transforms elements in an `ARRAY` by applying expression to each element   
`MAXIMUM` | Returns the maximum value in an `ARRAY`  
`MAXIMUM_N` | Returns the `n` largest values in an `ARRAY`  
`MINIMUM` | Returns the minimum value in an `ARRAY`  
`MINIMUM_N` | Returns the `n` smallest values in an `ARRAY`  
`SUM` | Returns the sum of all `NUMERIC` values in an `ARRAY`.   
`JOIN` | Produces a concatenation of the elements in an `ARRAY` as a `STRING` value.   
  
### ARRAY

**Syntax:**
    
    
    array(values: ANY...) -> ARRAY
    

**Description:**

Constructs an array from the given elements.

  * If an argument does not exist, it is replaced with `NULL` in the resulting array.



**Examples:**

values | `array(values)`  
---|---  
() | []  
(1, 2, 3) | [1, 2, 3]  
("a", 1, true) | ["a", 1, true]  
(1, null) | [1, null]  
(1, [2, 3]) | [1, [2, 3]]  
  
### ARRAY_CONCAT

**Syntax:**
    
    
    array_concat(arrays: ARRAY...) -> ARRAY
    

**Description:**

Concatenates two or more arrays into a single `ARRAY`.

**Examples:**

arrays | `array_concat(arrays)`  
---|---  
([1, 2], [3, 4]) | [1, 2, 3, 4]  
(["a", "b"], ["c"]) | ["a", "b", "c"]  
([1], [2], [3]) | [1, 2, 3]  
([], [1, 2]) | [1, 2]  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("genre").arrayConcat([field("subGenre")]).as("allGenres"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1530-L1533)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("genre").arrayConcat([Field("subGenre")]).as("allGenres")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L729-L732)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayConcat(field("subGenre")).alias("allGenres"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2067-L2070)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayConcat(field("subGenre")).alias("allGenres"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2313-L2316)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("genre").array_concat(Field.of("subGenre")).as_("allGenres"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L934-L941)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(arrayConcat(field("genre"), field("subGenre")).as("allGenres"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L860-L866)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayConcat(firestore.FieldOf("genre"), firestore.FieldOf("subGenre")).As("allGenres"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L85-L90)

### ARRAY_CONTAINS

**Syntax:**
    
    
    array_contains(array: ARRAY, value: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is found in the `array`, and `FALSE` otherwise.

**Examples:**

array | value | `array_contains(array, value)`  
---|---|---  
[1, 2, 3] | 2 | true  
[[1, 2], [3]] | [1, 2] | true  
[1, null] | null | true  
"abc" | ANY | error  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("genre").arrayContains(constant("mystery")).as("isMystery"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1540-L1543)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("genre").arrayContains(constant("mystery")).as("isMystery"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2817-L2820)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("genre").arrayContains(Constant("mystery")).as("isMystery")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L740-L743)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayContains("mystery").alias("isMystery"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2078-L2081)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayContains("mystery").alias("isMystery"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2324-L2327)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("genre").array_contains("mystery").as_("isMystery"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L949-L956)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(arrayContains(field("genre"), "mystery").as("isMystery"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L873-L879)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayContains(firestore.FieldOf("genre"), "mystery").As("isMystery"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L104-L109)

### ARRAY_CONTAINS_ALL

**Syntax:**
    
    
    array_contains_all(array: ARRAY, search_values: ARRAY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if all `search_values` are found in the `array`, and `FALSE` otherwise.

**Examples:**

array | search_values | `array_contains_all(array, search_values)`  
---|---|---  
[1, 2, 3] | [1, 2] | true  
[1, 2, 3] | [1, 4] | false  
[1, null] | [null] | true  
[NaN] | [NaN] | true  
[] | [] | true  
[1, 2, 3] | [] | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("genre")
          .arrayContainsAll([constant("fantasy"), constant("adventure")])
          .as("isFantasyAdventure")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1550-L1557)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("genre")
          .arrayContainsAll([constant("fantasy"), constant("adventure")])
          .as("isFantasyAdventure")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2827-L2834)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("genre")
          .arrayContainsAll([Constant("fantasy"), Constant("adventure")])
          .as("isFantasyAdventure")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L751-L758)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("genre")
                .arrayContainsAll(listOf("fantasy", "adventure"))
                .alias("isFantasyAdventure")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2089-L2096)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("genre")
                .arrayContainsAll(Arrays.asList("fantasy", "adventure"))
                .alias("isFantasyAdventure")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2335-L2342)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("genre")
            .array_contains_all(["fantasy", "adventure"])
            .as_("isFantasyAdventure")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L964-L975)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                arrayContainsAll(field("genre"), Arrays.asList("fantasy", "adventure"))
                    .as("isFantasyAdventure"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L886-L894)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayContainsAll(firestore.FieldOf("genre"), []string{"fantasy", "adventure"}).As("isFantasyAdventure"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L123-L128)

### ARRAY_CONTAINS_ANY

**Syntax:**
    
    
    array_contains_any(array: ARRAY, search_values: ARRAY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if any of the `search_values` are found in the `array`, and `FALSE` otherwise.

**Examples:**

array | search_values | `array_contains_any(array, search_values)`  
---|---|---  
[1, 2, 3] | [4, 1] | true  
[1, 2, 3] | [4, 5] | false  
[1, 2, null] | [null] | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("genre")
          .arrayContainsAny([constant("fantasy"), constant("nonfiction")])
          .as("isMysteryOrFantasy")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1564-L1571)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("genre")
          .arrayContainsAny([constant("fantasy"), constant("nonfiction")])
          .as("isMysteryOrFantasy")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2841-L2848)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("genre")
          .arrayContainsAny([Constant("fantasy"), Constant("nonfiction")])
          .as("isMysteryOrFantasy")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L766-L773)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("genre")
                .arrayContainsAny(listOf("fantasy", "nonfiction"))
                .alias("isMysteryOrFantasy")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2104-L2111)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("genre")
                .arrayContainsAny(Arrays.asList("fantasy", "nonfiction"))
                .alias("isMysteryOrFantasy")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2350-L2357)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("genre")
            .array_contains_any(["fantasy", "nonfiction"])
            .as_("isMysteryOrFantasy")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L983-L994)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(
                arrayContainsAny(field("genre"), Arrays.asList("fantasy", "nonfiction"))
                    .as("isMysteryOrFantasy"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L901-L909)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayContainsAny(firestore.FieldOf("genre"), []string{"fantasy", "nonfiction"}).As("isMysteryOrFantasy"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L142-L147)

### ARRAY_FILTER

**Syntax:**
    
    
    array_filter(array: ARRAY, predicate: (ANY) -> BOOLEAN) -> ARRAY
    

**Description:**

Filters `array` using a `predicate` expression, returning a new array with only elements that satisfy the predicate.

  * For each element in `array`, `predicate` is evaluated. If it returns `true`, the element is included in the result; otherwise (if it returns `false` or `null`), it is omitted.
  * If `predicate` evaluates to a non-boolean or non-null value, the function returns an error.



**Examples:**

array | predicate | `array_filter(array, predicate)`  
---|---|---  
[1, 2, 3] | x -> x > 1 | [2, 3]  
[1, null, 3] | x -> x > 1 | [3]  
["a", "b", "c"] | x -> x != "b" | ["a", "c"]  
[] | x -> true | []  
  
### ARRAY_GET

**Syntax:**
    
    
    array_get(array: ARRAY, index: INT64) -> ANY
    

**Description:**

Returns the element at the 0-based `index` in `array`.

  * If `index` is negative, elements are accessed from the end of array, where `-1` is the last element.
  * If `array` is not of type `ARRAY` and not `null`, returns an error.
  * If `index` is out of bounds, the function returns an absent value.
  * If `index` is not of type `INT64`, the function returns an error.



**Examples:**

array | index | `array_get(array, index)`  
---|---|---  
[1, 2, 3] | 0 | 1  
[1, 2, 3] | -1 | 3  
[1, 2, 3] | 3 | absent  
[1, 2, 3] | -4 | absent  
"abc" | 0 | error  
null | 0 | null  
`Array` | "a" | error  
`Array` | 2.0 | error  
  
### ARRAY_LENGTH

**Syntax:**
    
    
    array_length(array: ARRAY) -> INT64
    

**Description:**

Returns the number of elements in `array`.

**Examples:**

array | `array_length(array)`  
---|---  
[1, 2, 3] | 3  
[] | 0  
[1, 1, 1] | 3  
[1, null] | 2  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("genre").arrayLength().as("genreCount"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1578-L1581)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("genre").arrayLength().as("genreCount"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2855-L2858)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("genre").arrayLength().as("genreCount")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L781-L784)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayLength().alias("genreCount"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2119-L2122)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayLength().alias("genreCount"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2365-L2368)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("genre").array_length().as_("genreCount"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1002-L1009)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(arrayLength(field("genre")).as("genreCount"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L916-L922)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayLength(firestore.FieldOf("genre")).As("genreCount"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L161-L166)

### ARRAY_REVERSE

**Syntax:**
    
    
    array_reverse(array: ARRAY) -> ARRAY
    

**Description:**

Reverses the given `array`.

**Examples:**

array | `array_reverse(array)`  
---|---  
[1, 2, 3] | [3, 2, 1]  
["a", "b"] | ["b", "a"]  
[1, 2, 2, 3] | [3, 2, 2, 1]  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(arrayReverse(field("genre")).as("reversedGenres"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1588-L1591)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("genre").arrayReverse().as("reversedGenres"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2865-L2868)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("genre").arrayReverse().as("reversedGenres")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L792-L795)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayReverse().alias("reversedGenres"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2130-L2133)
    
    
        
    
    ##### Java  
    Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("genre").arrayReverse().alias("reversedGenres"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2376-L2379)
    
    
      

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("genre").array_reverse().as_("reversedGenres"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1017-L1024)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(arrayReverse(field("genre")).as("reversedGenres"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L929-L935)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ArrayReverse(firestore.FieldOf("genre")).As("reversedGenres"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_array.go#L180-L185)

### ARRAY_FIRST

**Syntax:**
    
    
    array_first(array: ARRAY) -> ANY
    

**Description:**

Returns the first element in `array`. This is equivalent to `array_get(array, 0)`.

  * If `array` is empty, returns an absent value.



**Examples:**

array | `array_first(array)`  
---|---  
[1, 2, 3] | 1  
[] | absent  
  
### ARRAY_FIRST_N

**Syntax:**
    
    
    array_first_n(array: ARRAY, n: INT64) -> ARRAY
    

**Description:**

Returns the first `n` elements of `array`. This is equivalent to `array_slice(array, 0, n)`.

  * If `n` is negative, returns an error.



**Examples:**

array | n | `array_first_n(array, n)`  
---|---|---  
[1, 2, 3, 4, 5] | 3 | [1, 2, 3]  
[1, 2] | 3 | [1, 2]  
[1, 2, 3] | 0 | []  
  
### ARRAY_INDEX_OF

**Syntax:**
    
    
    array_index_of(array: ARRAY, value: ANY) -> INT64
    

**Description:**

Returns the 0-based index of the first occurrence of `value` in `array`. Returns -1 if `value` is not found.

**Examples:**

array | value | `array_index_of(array, value)`  
---|---|---  
[1, 2, 3, 2] | 2 | 1  
[1, 2, 3] | 4 | -1  
[1, null, 3] | null | 1  
  
### ARRAY_INDEX_OF_ALL

**Syntax:**
    
    
    array_index_of_all(array: ARRAY, value: ANY) -> ARRAY<INT64>
    

**Description:**

Returns an array containing the 0-based indexes of all occurrences of `value` in `array`. Returns `[]` if `value` is not found.

**Examples:**

array | value | `array_index_of_all(array, value)`  
---|---|---  
[1, 2, 3, 2] | 2 | [1, 3]  
[1, 2, 3] | 4 | []  
[1, null, 3, null] | null | [1, 3]  
  
### ARRAY_LAST

**Syntax:**
    
    
    array_last(array: ARRAY) -> ANY
    

**Description:**

Returns the last element in `array`. This is equivalent to `array_get(array, -1)`.

  * If `array` is empty, returns an absent value.



**Examples:**

array | `array_last(array)`  
---|---  
[1, 2, 3] | 3  
[] | absent  
  
### ARRAY_LAST_N

**Syntax:**
    
    
    array_last_n(array: ARRAY, n: INT64) -> ARRAY
    

**Description:**

Returns the last `n` elements of `array`.

  * If `n` is negative, returns an error.



**Examples:**

array | n | `array_last_n(array, n)`  
---|---|---  
[1, 2, 3, 4, 5] | 3 | [3, 4, 5]  
[1, 2] | 3 | [1, 2]  
[1, 2, 3] | 0 | []  
  
### ARRAY_SLICE

**Syntax:**
    
    
    array_slice(array: ARRAY, offset: INT64, length: INT64) -> ARRAY
    

**Description:**

Returns a subset of `array` starting from 0-based index `offset`, and including `length` elements.

  * If `offset` is negative, it indicates the start position from the end of the array, with `-1` being the last element.
  * If `length` is greater than the number of elements remaining in the array after `offset`, the result extends to the end of the array.
  * `length` must be non-negative, otherwise returns an error.



**Examples:**

array | offset | length | `array_slice(array, offset, length)`  
---|---|---|---  
[1, 2, 3, 4, 5] | 1 | 3 | [2, 3, 4]  
[1, 2, 3, 4, 5] | -2 | 2 | [4, 5]  
[1, 2, 3] | 1 | 5 | [2, 3]  
[1, 2, 3] | 3 | 2 | []  
  
### ARRAY_TRANSFORM

**Syntax:**
    
    
    array_transform(array: ARRAY, expression: (ANY) -> ANY) -> ARRAY
    array_transform(array: ARRAY, expression: (ANY, INT64) -> ANY) -> ARRAY
    

**Description:**

Transforms `array` by applying `expression` to each element, returning a new array with transformed elements. The output array will always have same size as input array.

  * `expression` can be a unary function `element -> result`, or a binary function `(element, index) -> result`.
  * If `expression` is unary, it is called with each element of `array`.
  * If `expression` is binary, it is called with each element of `array` and its corresponding 0-based index.



**Examples:**

array | expression | `array_transform(array, expression)`  
---|---|---  
[1, 2, 3] | x -> x * 2 | [2, 4, 6]  
[1, 2, 3] | x -> x + 1 | [2, 3, 4]  
[10, 20] | (x, i) -> x + i | [10, 21]  
[] | x -> 1 | []  
  
### MAXIMUM

**Syntax:**
    
    
    maximum(array: ARRAY) -> ANY
    

**Description:**

Returns the maximum value in `array`.

  * `NULL` values are ignored during comparison.
  * If `array` is empty or only contains `NULL` values, returns `NULL`.



**Examples:**

array | `maximum(array)`  
---|---  
[1, 5, 2] | 5  
[1, null, 5] | 5  
["a", "c", "b"] | "c"  
[null, null] | null  
[] | null  
  
### MAXIMUM_N

**Syntax:**
    
    
    maximum_n(array: ARRAY, n: INT64) -> ARRAY
    

**Description:**

Returns an array of the `n` largest values in `array` in descending order.

  * `NULL` values are ignored.
  * If `n` is negative, returns an error.



**Examples:**

array | n | `maximum_n(array, n)`  
---|---|---  
[1, 5, 2, 4, 3] | 3 | [5, 4, 3]  
[1, null, 5] | 3 | [5, 1]  
  
### MINIMUM

**Syntax:**
    
    
    minimum(array: ARRAY) -> ANY
    

**Description:**

Returns the minimum value in `array`.

  * `NULL` values are ignored during comparison.
  * If `array` is empty or only contains `NULL` values, returns `NULL`.



**Examples:**

array | `minimum(array)`  
---|---  
[1, 5, 2] | 1  
[5, null, 1] | 1  
["a", "c", "b"] | "a"  
[null, null] | null  
[] | null  
  
### MINIMUM_N

**Syntax:**
    
    
    minimum_n(array: ARRAY, n: INT64) -> ARRAY
    

**Description:**

Returns an array of the `n` smallest values in `array` in ascending order.

  * `NULL` values are ignored.
  * If `n` is negative, returns an error.



**Examples:**

array | n | `minimum_n(array, n)`  
---|---|---  
[1, 5, 2, 4, 3] | 3 | [1, 2, 3]  
[5, null, 1] | 3 | [1, 5]  
  
### SUM

**Syntax:**
    
    
    sum(array: ARRAY) -> INT64 | FLOAT64
    

**Description:**

Returns the sum of all `NUMERIC` values in an `ARRAY`.

  * Non-numeric values in the array are ignored.
  * If any numeric value in the array is `NaN`, the function returns `NaN`.
  * The return type is determined by the widest numeric type in the array: `INT64` < `FLOAT64`.
  * If 64-bit integer overflow occurs before any floating point value is summed, an error is returned. If floating point values are summed, overflow will result in +/- infinity.
  * If the array contains no numeric values at all, the function returns `NULL`.



**Examples:**

array | `sum(array)`  
---|---  
[1, 2, 3] | 6L  
[1L, 2L, 3L] | 6L  
[2000000000, 2000000000] | 4000000000L  
[10, 20.5] | 30.5  
[1, "a", 2] | 3L  
[INT64.MAX_VALUE, 1] | error  
[INT64.MAX_VALUE, 1, -1.0] | error  
[INT64.MAX_VALUE, 1.0] | 9.223372036854776e+18  
  
### JOIN

**Syntax:**
    
    
    join[T <: STRING | BYTES](array: ARRAY<T>, delimiter: T) -> STRING
    join[T <: STRING | BYTES](array: ARRAY<T>, delimiter: T, null_text: T) -> STRING
    

**Description:**

Returns a concatenation of the elements in `array` as a `STRING`. The `array` can be of `STRING` or `BYTES` data types.

  * All elements in `array`, `delimiter`, and `null_text` must be of the same type; they must all be `STRING`s or all be `BYTES`.
  * If `null_text` is provided, any `NULL` values in `array` are replaced with `null_text`.
  * If `null_text` is not provided, `NULL` values in `array` are omitted from the result.



**Examples:**

When `null_text` is not provided:

array | delimiter | `join(array, delimiter)`  
---|---|---  
["a", "b", "c"] | "," | "a,b,c"  
["a", null, "c"] | "," | "a,c"  
[b'a', b'b', b'c'] | b',' | b'a,b,c'  
["a", b'c'] | "," | error  
["a", "c"] | b',' | error  
[b'a', b'c'] | "," | error  
  
When `null_text` is provided:

array | delimiter | null_text | `join(array, delimiter, null_text)`  
---|---|---|---  
["a", null, "c"] | "," | "MISSING" | "a,MISSING,c"  
[b'a', null, b'c'] | b',' | b'NULL' | b'a,NULL,c'  
[null, "b", null] | "," | "MISSING" | "MISSING,b,MISSING"  
[b'a', null, null] | b',' | b'NULL' | b'a,NULL,NULL'  
["a", null] | "," | b'N' | error  
[b'a', null] | b',' | "N" | error  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
