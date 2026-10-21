---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/string_functions/
title: String Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:28.190523+00:00
---

# String Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/string_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# String Functions Reference

## **String Functions**

Name  | Description   
---|---  
`BYTE_LENGTH` | Returns the number of `BYTES` in a `STRING` or `BYTES` value   
`CHAR_LENGTH` | Returns the number of unicode characters in a `STRING` value   
`STARTS_WITH` | Returns `TRUE` if a `STRING` begins with a given prefix   
`ENDS_WITH` | Returns `TRUE` if a `STRING` ends with a given postfix   
`LIKE` | Returns `TRUE` if a `STRING` matches a pattern   
`REGEX_CONTAINS` | Returns `TRUE` if a value is a partial or full match for a regular expression   
`REGEX_FIND` | Returns the first substring that matches a regular expression, or `NULL` if there is no match.   
`REGEX_FIND_ALL` | Returns an array of all substrings that match a regular expression, or an empty array if there are no matches.   
`REGEX_MATCH` | Returns `TRUE` if any part of a value matches a regular expression   
`STRING_CONCAT` | Concatenates multiple `STRING` into a `STRING`  
`STRING_CONTAINS` | Returns `TRUE` if a value contains a `STRING`  
`STRING_INDEX_OF` | Returns the 0-based index of the first occurrence of a `STRING` or `BYTES` value.   
`TO_UPPER` | Converts a `STRING` or `BYTES` value to uppercase.   
`TO_LOWER` | Converts a `STRING` or `BYTES` value to lowercase.   
`SUBSTRING` | Gets a substring of a `STRING` or `BYTES` value.   
`STRING_REVERSE` | Reverses a `STRING` or `BYTES` value.   
`STRING_REPEAT` | Repeats a `STRING` or `BYTES` value a specified number of times.   
`STRING_REPLACE_ALL` | Replaces all occurrences of a `STRING` or `BYTES` value.   
`STRING_REPLACE_ONE` | Replaces the first occurrence of a `STRING` or `BYTES` value.   
`TRIM` | Trims leading and trailing characters from a `STRING` or `BYTES` value.   
`LTRIM` | Trims leading characters from a `STRING` or `BYTES` value.   
`RTRIM` | Trims trailing characters from a `STRING` or `BYTES` value.   
`SPLIT` | Splits a `STRING` or `BYTES` value into an array.   
  
### BYTE_LENGTH

**Syntax:**
    
    
    byte_length[T <: STRING | BYTES](value: T) -> INT64
    

**Description:**

Returns the number of `BYTES` in a `STRING` or `BYTES` value.

**Examples:**

value | `byte_length(value)`  
---|---  
"abc" | 3  
"xyzabc" | 6  
b"abc" | 3  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("title").byteLength().as("titleByteLength")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1800-L1805)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("title").byteLength().as("titleByteLength")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3074-L3079)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("title").byteLength().as("titleByteLength")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1022-L1027)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("title").byteLength().alias("titleByteLength")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2378-L2383)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("title").byteLength().alias("titleByteLength")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2627-L2632)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("title").byte_length().as_("titleByteLength"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1329-L1336)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(byteLength(field("title")).as("titleByteLength"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1234-L1240)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.ByteLength(firestore.FieldOf("title")).As("titleByteLength"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L28-L33)

### CHAR_LENGTH

**Syntax:**
    
    
    char_length(value: STRING) -> INT64
    

**Description:**

Returns the number of unicode code points in `STRING` value.

**Examples:**

value | `char_length(value)`  
---|---  
"abc" | 3  
"hello" | 5  
"world" | 5  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("title").charLength().as("titleCharLength")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1812-L1817)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("title").charLength().as("titleCharLength")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3086-L3091)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("title").charLength().as("titleCharLength")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1035-L1040)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("title").charLength().alias("titleCharLength")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2391-L2396)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("title").charLength().alias("titleCharLength")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2640-L2645)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("title").char_length().as_("titleCharLength"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1344-L1351)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(charLength(field("title")).as("titleCharLength"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1247-L1253)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.CharLength(firestore.FieldOf("title")).As("titleCharLength"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L47-L52)

### STARTS_WITH

**Syntax:**
    
    
    starts_with(value: STRING, prefix: STRING) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` begins with `prefix`.

**Examples:**

value | prefix | `starts_with(value, prefix)`  
---|---|---  
"abc" | "a" | true  
"abc" | "b" | false  
"abc" | "" | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("title").startsWith("The")
          .as("needsSpecialAlphabeticalSort")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1824-L1830)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("title").startsWith("The")
          .as("needsSpecialAlphabeticalSort")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3098-L3104)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("title").startsWith("The")
          .as("needsSpecialAlphabeticalSort")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1048-L1054)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("title").startsWith("The")
                .alias("needsSpecialAlphabeticalSort")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2404-L2410)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("title").startsWith("The")
                .alias("needsSpecialAlphabeticalSort")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2653-L2659)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("title").starts_with("The").as_("needsSpecialAlphabeticalSort")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1359-L1368)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(startsWith(field("title"), "The").as("needsSpecialAlphabeticalSort"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1260-L1266)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.StartsWith(firestore.FieldOf("title"), "The").As("needsSpecialAlphabeticalSort"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L66-L71)

### ENDS_WITH

**Syntax:**
    
    
    ends_with(value: STRING, postfix: STRING) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` ends with `postfix`.

**Examples:**

value | postfix | `ends_with(value, postfix)`  
---|---|---  
"abc" | "c" | true  
"abc" | "b" | false  
"abc" | "" | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("inventory/devices/laptops")
      .select(
        field("name").endsWith("16 inch")
          .as("16InLaptops")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1837-L1843)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("inventory/devices/laptops")
      .select([
        Field("name").endsWith("16 inch")
          .as("16InLaptops")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1062-L1068)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("inventory/devices/laptops")
        .select(
            field("name").endsWith("16 inch")
                .alias("16InLaptops")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2418-L2424)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("inventory/devices/laptops")
        .select(
            field("name").endsWith("16 inch")
                .alias("16InLaptops")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2667-L2673)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("inventory/devices/laptops")
        .select(Field.of("name").ends_with("16 inch").as_("16InLaptops"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1376-L1383)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("inventory/devices/laptops")
            .select(endsWith(field("name"), "16 inch").as("16InLaptops"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1273-L1279)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("inventory/devices/laptops").
    	Select(firestore.Fields(
    		firestore.EndsWith(firestore.FieldOf("name"), "16 inch").As("`Laptops16in`"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L85-L90)

### LIKE

**Syntax:**
    
    
    like(value: STRING, pattern: STRING) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` matches `pattern`.

**Examples:**

value | pattern | `like(value, pattern)`  
---|---|---  
"Firestore" | "Fire%" | true  
"Firestore" | "%store" | true  
"Datastore" | "Data_tore" | true  
"100%" | "100\%" | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("genre").like("%Fiction")
          .as("anyFiction")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1850-L1856)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("genre").like("%Fiction")
          .as("anyFiction")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3124-L3130)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("genre").like("%Fiction")
          .as("anyFiction")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1076-L1082)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("genre").like("%Fiction")
                .alias("anyFiction")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2432-L2438)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("genre").like("%Fiction")
                .alias("anyFiction")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2681-L2687)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("genre").like("%Fiction").as_("anyFiction"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1391-L1398)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(like(field("genre"), "%Fiction").as("anyFiction"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1286-L1292)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Like(firestore.FieldOf("genre"), "%Fiction").As("anyFiction"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L104-L109)

### REGEX_CONTAINS

**Syntax:**
    
    
    regex_contains(value: STRING, regexp: STRING | REGEX) -> BOOLEAN
    

**Description:**

Returns `TRUE` if some part of `value` matches `regexp`. If `regexp` is not a valid regular expression, this function returns an `error`.

The `regexp` argument can also be a `REGEX` value created using `regex("pattern", "options")`. This format lets you provide regular expression options along with the pattern. The supported options are:

  * `i`: Case-insensitive matching.
  * `m`: Multi-line mode (`^` and `$` match the start or end of lines).
  * `s`: Dotall mode (`.` matches newlines).



If `regexp` is a `STRING`, no options are applied besides those embedded in the pattern itself (e.g., `(?i)`).

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

value | regexp | `regex_contains(value, regexp)`  
---|---|---  
"Firestore" | "Fire" | true  
"Firestore" | "store$" | true  
"Firestore" | "data" | false  
"Firestore" | `regex("fire", "i")` | true  
"Firestore" | `regex("FIRE", "")` | false  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("title").regexContains("Firestore (Enterprise|Standard)")
          .as("isFirestoreRelated")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1863-L1869)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("title").regexContains("Firestore (Enterprise|Standard)")
          .as("isFirestoreRelated")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3137-L3143)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("title").regexContains("Firestore (Enterprise|Standard)")
          .as("isFirestoreRelated")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1090-L1096)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("title").regexContains("Firestore (Enterprise|Standard)")
                .alias("isFirestoreRelated")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2446-L2452)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("title").regexContains("Firestore (Enterprise|Standard)")
                .alias("isFirestoreRelated")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2695-L2701)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("title")
            .regex_contains("Firestore (Enterprise|Standard)")
            .as_("isFirestoreRelated")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1406-L1417)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(
                regexContains(field("title"), "Firestore (Enterprise|Standard)")
                    .as("isFirestoreRelated"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1299-L1307)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.RegexContains(firestore.FieldOf("title"), "Firestore (Enterprise|Standard)").As("isFirestoreRelated"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L123-L128)

### REGEX_FIND

**Syntax:**
    
    
    regex_find(value: STRING, regexp: STRING | REGEX) -> STRING
    

**Description:**

Returns the first substring in `value` that matches `regexp`, or `NULL` if there is no match. If `regexp` is not a valid regular expression, this function returns an `error`.

The `regexp` argument can also be a `REGEX` value created using `regex("pattern", "options")`. This format lets you provide regular expression options along with the pattern. The supported options are:

  * `i`: Case-insensitive matching.
  * `m`: Multi-line mode (`^` and `$` match the start or end of lines).
  * `s`: Dotall mode (`.` matches newlines).



If `regexp` is a `STRING`, no options are applied besides those embedded in the pattern itself (e.g., `(?i)`).

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

value | regexp | `regex_find(value, regexp)`  
---|---|---  
"Sometext MATCH" | "SomeText" | "Sometext"  
"Sometext MATCH" | `regex("match", "i")` | "MATCH"  
"Sometext MATCH" | `regex("(match)", "i")` | "MATCH"  
"Sometext match" | `regex("MATCH", "")` | null  
  
### REGEX_FIND_ALL

**Syntax:**
    
    
    regex_find_all(value: STRING, regexp: STRING | REGEX) -> ARRAY<STRING>
    

**Description:**

Returns an array of all substrings in `value` that match `regexp`, or an empty array if there are no matches. If `regexp` is not a valid regular expression, this function returns an `error`.

The `regexp` argument can also be a `REGEX` value created using `regex("pattern", "options")`. This format lets you provide regular expression options along with the pattern. The supported options are:

  * `i`: Case-insensitive matching.
  * `m`: Multi-line mode (`^` and `$` match the start or end of lines).
  * `s`: Dotall mode (`.` matches newlines).



If `regexp` is a `STRING`, no options are applied besides those embedded in the pattern itself (e.g., `(?i)`).

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

value | regexp | `regex_find_all(value, regexp)`  
---|---|---  
"one two three two" | "one" | ["one"]  
"one TWO three Two" | `regex("two", "i")` | ["TWO", "Two"]  
"one two three two" | `regex("TWO", "")` | []  
  
### REGEX_MATCH

**Syntax:**
    
    
    regex_match(value: STRING, regexp: STRING | REGEX) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` fully matches `regexp`. If `regexp` is not a valid regular expression, this function returns an `error`.

The `regexp` argument can also be a `REGEX` value created using `regex("pattern", "options")`. This format lets you provide regular expression options along with the pattern. The supported options are:

  * `i`: Case-insensitive matching.
  * `m`: Multi-line mode (`^` and `$` match the start or end of lines).
  * `s`: Dotall mode (`.` matches newlines).



If `regexp` is a `STRING`, no options are applied besides those embedded in the pattern itself (e.g., `(?i)`).

Regular expressions follow the syntax of the [re2](https://github.com/google/re2/wiki/Syntax) library.

**Examples:**

value | regexp | `regex_match(value, regexp)`  
---|---|---  
"Firestore" | "F.*store" | true  
"Firestore" | "Fire" | false  
"Firestore" | "^F.*e$" | true  
"FiReStOrE" | `regex("firestore", "i")` | true  
"Firestore" | `regex("firestore", "")` | false  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("title").regexMatch("Firestore (Enterprise|Standard)")
          .as("isFirestoreExactly")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1876-L1882)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("title").regexMatch("Firestore (Enterprise|Standard)")
          .as("isFirestoreExactly")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3150-L3156)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("title").regexMatch("Firestore (Enterprise|Standard)")
          .as("isFirestoreExactly")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1104-L1110)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("title").regexMatch("Firestore (Enterprise|Standard)")
                .alias("isFirestoreExactly")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2460-L2466)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("title").regexMatch("Firestore (Enterprise|Standard)")
                .alias("isFirestoreExactly")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2709-L2715)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("title")
            .regex_match("Firestore (Enterprise|Standard)")
            .as_("isFirestoreExactly")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1425-L1436)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(
                regexMatch(field("title"), "Firestore (Enterprise|Standard)")
                    .as("isFirestoreExactly"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1340-L1348)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.RegexMatch(firestore.FieldOf("title"), "Firestore (Enterprise|Standard)").As("isFirestoreExactly"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L180-L185)

### STRING_CONCAT

**Syntax:**
    
    
    string_concat(values: STRING...) -> STRING
    

**Description:**

Concatenates two or more `STRING` values into a single result.

**Examples:**

arguments | `string_concat(values...)`  
---|---  
`()` | error  
`("a")` | "a"  
`("abc", "def")` | "abcdef"  
`("a", "", "c")` | "ac"  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("title").stringConcat(" by ", field("author"))
          .as("fullyQualifiedTitle")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1889-L1895)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("title").stringConcat(" by ", field("author"))
          .as("fullyQualifiedTitle")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3163-L3169)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("title").concat([" by ", Field("author")])
          .as("fullyQualifiedTitle")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1118-L1124)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("title").concat(" by ", field("author"))
                .alias("fullyQualifiedTitle")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2474-L2480)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("title").concat(" by ", field("author"))
                .alias("fullyQualifiedTitle")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2723-L2729)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("title")
            .concat(" by ", Field.of("author"))
            .as_("fullyQualifiedTitle")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1444-L1455)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(stringConcat(field("title"), " by ", field("author")).as("fullyQualifiedTitle"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1355-L1361)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.StringConcat(firestore.FieldOf("title"), " by ", firestore.FieldOf("author")).As("fullyQualifiedTitle"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L199-L204)

### STRING_CONTAINS

**Syntax:**
    
    
    string_contains(value: STRING, substring: STRING) -> BOOLEAN
    

**Description:**

Checks if `value` contains the literal String `substring`.

**Examples:**

value | substring | `string_contains(value, substring)`  
---|---|---  
"abc" | "b" | true  
"abc" | "d" | false  
"abc" | "" | true  
"a.c" | "." | true  
"☃☃☃" | "☃" | true  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("articles")
      .select(
        field("body").stringContains("Firestore")
          .as("isFirestoreRelated")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1902-L1908)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("articles")
      .select(
        field("body").stringContains("Firestore")
          .as("isFirestoreRelated")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3176-L3182)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("articles")
      .select([
        Field("body").stringContains("Firestore")
          .as("isFirestoreRelated")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1132-L1138)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("articles")
        .select(
            field("body").stringContains("Firestore")
                .alias("isFirestoreRelated")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2488-L2494)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("articles")
        .select(
            field("body").stringContains("Firestore")
                .alias("isFirestoreRelated")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2737-L2743)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("articles")
        .select(Field.of("body").string_contains("Firestore").as_("isFirestoreRelated"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1463-L1470)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("articles")
            .select(stringContains(field("body"), "Firestore").as("isFirestoreRelated"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1368-L1374)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("articles").
    	Select(firestore.Fields(
    		firestore.StringContains(firestore.FieldOf("body"), "Firestore").As("isFirestoreRelated"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L218-L223)

### STRING_INDEX_OF

**Syntax:**
    
    
    string_index_of[T <: STRING | BYTES](value: T, search: T) -> INT64
    

**Description:**

Returns the 0-based index of the first occurrence of `search` in `value`.

  * Returns `-1` if `search` is not found.
  * If `value` is a `STRING` value, the result is measured in unicode code points. If it is a `BYTES` value, it is measured in bytes.
  * If `search` is an empty `STRING` or `BYTES` value, the result is `0`.



**Examples:**

value | search | `string_index_of(value, search)`  
---|---|---  
"hello world" | "o" | 4  
"hello world" | "l" | 2  
"hello world" | "z" | -1  
"banana" | "ana" | 1  
"abc" | "" | 0  
b"abc" | b"b" | 1  
"é" | "é" | 0  
b"é" | b"é" | 0  
  
### TO_UPPER

**Syntax:**
    
    
    to_upper[T <: STRING | BYTES](value: T) -> T
    

**Description:**

Converts a `STRING` or `BYTES` value to uppercase.

If a byte or char does not correspond to a UTF-8 lowercase alphabetic character, it is passed through unchanged.

**Examples:**

value | `to_upper(value)`  
---|---  
"abc" | "ABC"  
"AbC" | "ABC"  
b"abc" | b"ABC"  
b"a1c" | b"A1C"  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("authors")
      .select(
        field("name").toUpper()
          .as("uppercaseName")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1915-L1921)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("authors")
      .select(
        field("name").toUpper()
          .as("uppercaseName")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3189-L3195)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("authors")
      .select([
        Field("name").toUpper()
          .as("uppercaseName")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1146-L1152)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("authors")
        .select(
            field("name").toUpper()
                .alias("uppercaseName")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2502-L2508)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("authors")
        .select(
            field("name").toUpper()
                .alias("uppercaseName")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2751-L2757)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("authors")
        .select(Field.of("name").to_upper().as_("uppercaseName"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1478-L1485)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("authors")
            .select(toUpper(field("name")).as("uppercaseName"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1381-L1387)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("authors").
    	Select(firestore.Fields(
    		firestore.ToUpper(firestore.FieldOf("name")).As("uppercaseName"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L237-L242)

### TO_LOWER

**Syntax:**
    
    
    to_lower[T <: STRING | BYTES](value: T) -> T
    

**Description:**

Converts a `STRING` or `BYTES` value to lowercase.

If a byte or char does not correspond to a UTF-8 uppercase alphabetic character, it is passed through unchanged.

**Examples:**

value | `to_lower(value)`  
---|---  
"ABC" | "abc"  
"AbC" | "abc"  
"A1C" | "a1c"  
b"ABC" | b"abc"  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("authors")
      .select(
        field("genre").toLower().equal("fantasy")
          .as("isFantasy")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1928-L1934)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("authors")
      .select(
        field("genre").toLower().equal("fantasy")
          .as("isFantasy")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3202-L3208)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("authors")
      .select([
        Field("genre").toLower().equal("fantasy")
          .as("isFantasy")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1160-L1166)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("authors")
        .select(
            field("genre").toLower().equal("fantasy")
                .alias("isFantasy")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2516-L2522)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("authors")
        .select(
            field("genre").toLower().equal("fantasy")
                .alias("isFantasy")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2765-L2771)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("authors")
        .select(Field.of("genre").to_lower().equal("fantasy").as_("isFantasy"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1493-L1500)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("authors")
            .select(equal(toLower(field("genre")), "fantasy").as("isFantasy"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1394-L1400)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("authors").
    	Select(firestore.Fields(
    		firestore.Equal(firestore.ToLower(firestore.FieldOf("genre")), "fantasy").As("isFantasy"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L256-L261)

### SUBSTRING

**Syntax:**
    
    
    substring[T <: STRING | BYTES](input: T, position: INT64) -> T
    substring[T <: STRING | BYTES](input: T, position: INT64, length: INT64) -> T
    

**Description:**

Returns a substring of `input` starting at `position` (zero-based index) and including up to `length` entries. If no `length` is provided, returns the substring from `position` to the end of the `input`.

  * If `input` is a `STRING` value, `position` and `length` are measured in unicode code points. If it is a `BYTES` value, they are measured in bytes.

  * If `position` is greater than the length of the `input`, an empty substring is returned. If `position` plus `length` is greater than the length of `input`, the substring is truncated to the end of `input`.

  * If `position` is negative, the position is taken from the end of the input. If the negative `position` is greater than the size of the input, the position is set to zero. `length` must be non-negative.




**Examples:**

When `length` is not provided:

input | position | `substring(input, position)`  
---|---|---  
"abc" | 0 | "abc"  
"abc" | 1 | "bc"  
"abc" | 3 | ""  
"abc" | -1 | "c"  
b"abc" | 1 | b"bc"  
  
When `length` is provided:

input | position | length | `substring(input, position, length)`  
---|---|---|---  
"abc" | 0 | 1 | "a"  
"abc" | 1 | 2 | "bc"  
"abc" | -1 | 1 | "c"  
b"abc" | 0 | 1 | b"a"  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .where(field("title").startsWith("The "))
      .select(
        field("title").substring(4)
          .as("titleWithoutLeadingThe")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1940-L1947)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .where(field("title").startsWith("The "))
      .select(
        field("title").substring(4)
          .as("titleWithoutLeadingThe")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3214-L3221)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .where(Field("title").startsWith("The "))
      .select([
        Field("title").substring(position: 4)
          .as("titleWithoutLeadingThe")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1174-L1181)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .where(field("title").startsWith("The "))
        .select(
            field("title")
              .substring(constant(4),
                field("title").charLength().subtract(4))
                .alias("titleWithoutLeadingThe")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2530-L2539)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .where(field("title").startsWith("The "))
        .select(
            field("title").substring(
              constant(4),
                field("title").charLength().subtract(4))
                .alias("titleWithoutLeadingThe")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2779-L2788)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .where(Field.of("title").starts_with("The "))
        .select(Field.of("title").substring(4).as_("titleWithoutLeadingThe"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1508-L1516)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .where(startsWith(field("title"), "The "))
            .select(
                substring(field("title"), constant(4), field("title").charLength())
                    .as("titleWithoutLeadingThe"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1407-L1416)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Where(firestore.StartsWith(firestore.FieldOf("title"), "The ")).
    	Select(firestore.Fields(
    		firestore.Substring(firestore.FieldOf("title"), firestore.ConstantOf(4), firestore.FieldOf("title").CharLength()).As("titleWithoutLeadingThe"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L275-L281)

### STRING_REVERSE

**Syntax:**
    
    
    string_reverse[T <: STRING | BYTES](input: T) -> T
    

**Description:**

Returns the supplied input in reverse order.

Characters are delineated by Unicode code points when the input is a `STRING`, and bytes when the input is a `BYTES` value.

**Examples:**

input | `string_reverse(input)`  
---|---  
"abc" | "cba"  
"a🌹b" | "b🌹a"  
"hello" | "olleh"  
b"abc" | b"cba"  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("name").reverse().as("reversedName")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1954-L1959)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("name").reverse().as("reversedName")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3228-L3233)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("name").reverse().as("reversedName")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1189-L1194)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("name").reverse().alias("reversedName")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2547-L2552)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("name").reverse().alias("reversedName")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2796-L2801)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("name").string_reverse().as_("reversedName"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1524-L1531)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(reverse(field("name")).as("reversedName"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1423-L1429)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Reverse(firestore.FieldOf("name")).As("reversedName"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L295-L300)

### STRING_REPEAT

**Syntax:**
    
    
    string_repeat[T <: STRING | BYTES](input: T, repetitions: INT64) -> T
    

**Description:**

Returns the `input` repeated `repetitions` times.

  * `repetitions` must be a non-negative integer.
  * If `repetitions` is `0`, returns an empty value of the same type as `input`.
  * If the result exceeds the maximum allowed size (1 MB), an error is returned.



**Examples:**

input | repetitions | `string_repeat(input, repetitions)`  
---|---|---  
"foo" | 3 | "foofoofoo"  
"foo" | 0 | ""  
"a " | 3 | "a a a "  
b"ab" | 2 | b"abab"  
"é🦆" | 2 | "é🦆é🦆"  
  
### STRING_REPLACE_ALL

**Syntax:**
    
    
    string_replace_all[T <: STRING | BYTES](input: T, find: T, replacement: T) -> T
    

**Description:**

Replaces all non-overlapping occurrences of `find` in `input` with `replacement`.

  * Matches are case-sensitive.
  * If `find` is empty, no replacements are made.



**Examples:**

input | find | replacement | `string_replace_all(input, find, replacement)`  
---|---|---|---  
"foobarfoo" | "foo" | "baz" | "bazbarbaz"  
"ababab" | "aba" | "c" | "cbab"  
"foobar" | "o" | "" | "fbar"  
"é🦆🌎🦆" | "🦆" | "a" | "éa🌎a"  
b"abc" | b"b" | b"d" | b"adc"  
  
### STRING_REPLACE_ONE

**Syntax:**
    
    
    string_replace_one[T <: STRING | BYTES](input: T, find: T, replacement: T) -> T
    

**Description:**

Replaces the first occurrence of `find` in `input` with `replacement`.

  * Matches are case-sensitive.
  * If `find` is empty, no replacements are made.



**Examples:**

input | find | replacement | `string_replace_one(input, find, replacement)`  
---|---|---|---  
"foobarfoo" | "foo" | "baz" | "bazbarfoo"  
"é" | "é" | "a" | "a"  
b"foobar" | b"o" | b"z" | b"fzoobar"  
  
### TRIM

**Syntax:**
    
    
    trim[T <: STRING | BYTES](input: T, values_to_trim: T) -> T
    trim[T <: STRING | BYTES](input: T) -> T
    

**Description:**

Trims a specified set of `BYTES` or `CHARS` from the beginning and end of the supplied `input`.

  * If no `values_to_trim` are provided, trims whitespace characters.



**Examples:**

When `values_to_trim` is not provided:

input | `trim(input)`  
---|---  
" foo " | "foo"  
b" foo " | b"foo"  
"foo" | "foo"  
"" | ""  
" " | ""  
"\t foo \n" | "foo"  
b"\t foo \n" | b"foo"  
"\r\f\v foo \r\f\v" | "foo"  
b"\r\f\v foo \r\f\v" | b"foo"  
  
When `values_to_trim` is provided:

input | values_to_trim | `trim(input, values_to_trim)`  
---|---|---  
"abcbfooaacb" | "abc" | "foo"  
"abcdaabadbac" | "abc" | "daabad"  
b"C1C2C3" | b"C1" | b"C2C3"  
b"C1C2" | "foo" | error  
"foo" | b"C1" | error  
  
### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("name").trim().as("whitespaceTrimmedName")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3240-L3245)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("name").trim(" \n\t").as("whitespaceTrimmedName")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1202-L1207)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("name").trim().alias("whitespaceTrimmedName")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2560-L2565)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("name").trim().alias("whitespaceTrimmedName")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2809-L2814)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("name").trim().as_("whitespaceTrimmedName"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1539-L1546)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(trim(field("name")).as("whitespaceTrimmedName"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1436-L1442)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Trim(firestore.FieldOf("name")).As("whitespaceTrimmedName"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_string.go#L314-L319)

### LTRIM

**Syntax:**
    
    
    ltrim[T <: STRING | BYTES](value: T, to_trim: T) -> T
    ltrim[T <: STRING | BYTES](value: T) -> T
    

**Description:**

Trims a specified set of `BYTES` or `CHARS` from the beginning of the supplied `value`.

  * If `to_trim` is not provided, trims leading whitespace characters.



**Examples:**

When `to_trim` is not provided:

value | `ltrim(value)`  
---|---  
" foo " | "foo "  
"foo" | "foo"  
  
When `to_trim` is provided:

value | to_trim | `ltrim(value, to_trim)`  
---|---|---  
"aaabc" | "a" | "bc"  
"abacaba" | "ba" | "caba"  
"é" | "é" | ""  
  
### RTRIM

**Syntax:**
    
    
    rtrim[T <: STRING | BYTES](value: T, to_trim: T) -> T
    rtrim[T <: STRING | BYTES](value: T) -> T
    

**Description:**

Trims a specified set of `BYTES` or `CHARS` from the end of the supplied `value`.

  * If `to_trim` is not provided, trims trailing whitespace characters.



**Examples:**

When `to_trim` is not provided:

value | `rtrim(value)`  
---|---  
" foo " | " foo"  
"foo" | "foo"  
  
When `to_trim` is provided:

value | to_trim | `rtrim(value, to_trim)`  
---|---|---  
"abccc" | "c" | "ab"  
"abacaba" | "ba" | "abac"  
"é" | "é" | ""  
  
### SPLIT

**Syntax:**
    
    
    split(input: STRING) -> ARRAY<STRING>
    split[T <: STRING | BYTES](input: T, delimiter: T) -> ARRAY<T>
    

**Description:**

Splits a `STRING` or `BYTES` value, using a delimiter.

  * For `STRING` the default delimiter is the comma `,`. The delimiter is treated as a single string.

  * For `BYTES`, you must specify a delimiter.

  * Splitting on an empty delimiter produces an array of Unicode codepoints for `STRING` values, and an array of `BYTES` for `BYTES` values.

  * Splitting an empty `STRING` returns an `ARRAY` with a single empty `STRING`.




**Examples:**

When `delimiter` is not provided:

input | `split(input)`  
---|---  
"foo,bar,foo" | ["foo", "bar", "foo"]  
"foo" | ["foo"]  
",foo," | ["", "foo", ""]  
"" | [""]  
b"C120C2C4" | error  
  
When `delimiter` is provided:

input | delimiter | `split(input, delimiter)`  
---|---|---  
"foo bar foo" | " " | ["foo", "bar", "foo"]  
"foo bar foo" | "z" | ["foo bar foo"]  
"abc" | "" | ["a", "b", "c"]  
b"C1,C2,C4" | b"," | [b"C1", b"C2", b"C4"]  
b"ABC" | b"" | [b"A", b"B", b"C"]  
"foo" | b"C1" | error  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
