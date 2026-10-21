---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/timestamp_functions/
title: Timestamp Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:21.717376+00:00
---

# Timestamp Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/timestamp_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Timestamp Functions Reference

## **Timestamp Functions**

Name  | Description   
---|---  
`CURRENT_TIMESTAMP` | Generates a `TIMESTAMP` corresponding to the request time.   
`TIMESTAMP_TRUNC` | Truncates a `TIMESTAMP` to a given granularity.   
`UNIX_MICROS_TO_TIMESTAMP` | Converts the number of microseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP`  
`UNIX_MILLIS_TO_TIMESTAMP` | Converts the number of milliseconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP`  
`UNIX_SECONDS_TO_TIMESTAMP` | Converts the number of seconds since `1970-01-01 00:00:00 UTC` to a `TIMESTAMP`  
`TIMESTAMP_ADD` | Adds a time interval to a `TIMESTAMP`  
`TIMESTAMP_SUB` | Subtracts a time interval to a `TIMESTAMP`  
`TIMESTAMP_TO_UNIX_MICROS` | Converts a `TIMESTAMP` to the number of microseconds since `1970-01-01 00:00:00 UTC`  
`TIMESTAMP_TO_UNIX_MILLIS` | Converts a `TIMESTAMP` to the number of milliseconds since `1970-01-01 00:00:00 UTC`  
`TIMESTAMP_TO_UNIX_SECONDS` | Converts a `TIMESTAMP` to the number of seconds since `1970-01-01 00:00:00 UTC`  
`TIMESTAMP_DIFF` | Returns the whole number of specified `unit` intervals between two `TIMESTAMP`s.   
`TIMESTAMP_EXTRACT` | Extracts a specific `part` (e.g. year, month, day) from a `TIMESTAMP`.   
  
### CURRENT_TIMESTAMP

**Syntax:**
    
    
    current_timestamp() -> TIMESTAMP
    

**Description:**

Gets the timestamp at the beginning of request time `input` (interpreted as the number of microseconds since `1970-01-01 00:00:00 UTC`).

This is stable within a query, and will always resolve to the same value if called multiple times.

### TIMESTAMP_TRUNC

**Syntax:**
    
    
    timestamp_trunc(timestamp: TIMESTAMP | BSON_TIMESTAMP, granularity: STRING[, timezone: STRING]) -> TIMESTAMP
    

**Description:**

Truncates a timestamp down to a given granularity.

The `granularity` argument must be a string and one of the following:

  * `microsecond`
  * `millisecond`
  * `second`
  * `minute`
  * `hour`
  * `day`
  * `week`
  * `week([weekday])`
  * `month`
  * `quarter`
  * `year`
  * `isoyear`



If the `timezone` argument is provided, truncation will be based on the given timezone's calendar boundaries (e.g. day truncation will truncate to midnight in the given timezone). The truncation will respect daylight savings time.

If `timezone` is not provided, truncation will be based on `UTC` calendar boundaries.

The `timezone` argument should be a string representation of a timezone from the tz database, for example `America/New_York`. A custom time offset can also be used by specifying an offset from `GMT`.

**Examples:**

`timestamp` | `granularity` | `timezone` | `timestamp_trunc(timestamp, granularity, timezone)`  
---|---|---|---  
2000-01-01 10:20:30:123456 UTC | "second" | Not provided | 2001-01-01 10:20:30 UTC  
1997-05-31 04:30:30 UTC | "day" | Not provided | 1997-05-31 00:00:00 UTC  
1997-05-31 04:30:30 UTC | "day" | "America/Los_Angeles" | 1997-05-30 07:00:00 UTC  
2001-03-16 04:00:00 UTC | "week(friday) | Not provided | 2001-03-16 00:00:00 UTC  
2001-03-23 04:00:00 UTC | "week(friday) | "America/Los_Angeles" | 2001-03-23 17:00:00 UTC  
2026-01-24 20:00:00 UTC | "month" | "GMT+06:32:43" | 2026-01-01T06:32:43 UTC  
  
### UNIX_MICROS_TO_TIMESTAMP

**Syntax:**
    
    
    unix_micros_to_timestamp(input: INT64) -> TIMESTAMP
    

**Description:**

Converts `input` (interpreted as the number of microseconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

`input` | `unix_micros_to_timestamp(input)`  
---|---  
0L | 1970-01-01 00:00:00 UTC  
400123456L | 1970-01-01 00:06:40.123456 UTC  
-1000000L | 1969-12-31 23:59:59 UTC  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1986-L1991)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3260-L3265)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("createdAtMicros").unixMicrosToTimestamp().as("createdAtString")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1225-L1230)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtMicros").unixMicrosToTimestamp().alias("createdAtString")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2583-L2588)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtMicros").unixMicrosToTimestamp().alias("createdAtString")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2832-L2837)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("createdAtMicros")
            .unix_micros_to_timestamp()
            .as_("createdAtString")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1564-L1575)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(unixMicrosToTimestamp(field("createdAtMicros")).as("createdAtString"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1527-L1533)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.UnixMicrosToTimestamp(firestore.FieldOf("createdAtMicros")).As("createdAtString"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L28-L33)

### UNIX_MILLIS_TO_TIMESTAMP

**Syntax:**
    
    
    unix_millis_to_timestamp(input: INT64) -> TIMESTAMP
    

**Description:**

Converts `input` (interpreted as the number of milliseconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

`input` | `unix_millis_to_timestamp(input)`  
---|---  
0L | 1970-01-01 00:00:00 UTC  
4000123L | 1970-01-01 01:06:40.123 UTC  
-1000000L | 1969-12-31 23:43:20 UTC  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1998-L2003)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3272-L3277)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("createdAtMillis").unixMillisToTimestamp().as("createdAtString")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1238-L1243)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtMillis").unixMillisToTimestamp().alias("createdAtString")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2596-L2601)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtMillis").unixMillisToTimestamp().alias("createdAtString")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2845-L2850)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("createdAtMillis")
            .unix_millis_to_timestamp()
            .as_("createdAtString")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1583-L1594)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(unixMillisToTimestamp(field("createdAtMillis")).as("createdAtString"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1540-L1546)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.UnixMillisToTimestamp(firestore.FieldOf("createdAtMillis")).As("createdAtString"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L47-L52)

### UNIX_SECONDS_TO_TIMESTAMP

**Syntax:**
    
    
    unix_seconds_to_timestamp(input: INT64) -> TIMESTAMP
    

**Description:**

Converts `input` (interpreted as the number of seconds since `1970-01-01 00:00:00 UTC`) to a `TIMESTAMP`. Throws an `error` if `input` cannot be converted to a valid `TIMESTAMP`.

**Examples:**

`input` | `unix_seconds_to_timestamp(input)`  
---|---  
0L | 1970-01-01 00:00:00 UTC  
60L | 1970-01-01 00:01:00 UTC  
-300L | 1969-12-31 23:55:00 UTC  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2010-L2015)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3284-L3289)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("createdAtSeconds").unixSecondsToTimestamp().as("createdAtString")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1251-L1256)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtSeconds").unixSecondsToTimestamp().alias("createdAtString")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2609-L2614)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAtSeconds").unixSecondsToTimestamp().alias("createdAtString")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2858-L2863)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("createdAtSeconds")
            .unix_seconds_to_timestamp()
            .as_("createdAtString")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1602-L1613)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(unixSecondsToTimestamp(field("createdAtSeconds")).as("createdAtString"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1553-L1559)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.UnixSecondsToTimestamp(firestore.FieldOf("createdAtSeconds")).As("createdAtString"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L66-L71)

### TIMESTAMP_ADD

**Syntax:**
    
    
    timestamp_add(timestamp: TIMESTAMP | BSON_TIMESTAMP, unit: STRING, amount: INT64) -> TIMESTAMP
    

**Description:**

Adds an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to TIMESTAMP_SUB.

The `unit` argument must be a string and one of the following:

  * `microsecond`
  * `millisecond`
  * `second`
  * `minute`
  * `hour`
  * `day`



Throws an error if the resulting timestamp does not fit within the `TIMESTAMP` range.

**Examples:**

`timestamp` | `unit` | `amount` | `timestamp_add(timestamp, unit, amount)`  
---|---|---|---  
2025-02-20 00:00:00 UTC | "minute" | 2L | 2025-02-20 00:02:00 UTC  
2025-02-20 00:00:00 UTC | "hour" | -4L | 2025-02-19 20:00:00 UTC  
2025-02-20 00:00:00 UTC | "day" | 5L | 2025-02-25 00:00:00 UTC  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("createdAt").timestampAdd("day", 3653).as("expiresAt")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2022-L2027)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("createdAt").timestampAdd("day", 3653).as("expiresAt")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3296-L3301)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("createdAt").timestampAdd(3653, .day).as("expiresAt")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1264-L1269)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAt")
              .timestampAdd("day", 3653)
              .alias("expiresAt")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2622-L2629)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("createdAt").timestampAdd("day", 3653).alias("expiresAt")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2871-L2876)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(Field.of("createdAt").timestamp_add("day", 3653).as_("expiresAt"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1621-L1628)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(timestampAdd(field("createdAt"), "day", 3653).as("expiresAt"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1566-L1572)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.TimestampAdd(firestore.FieldOf("createdAt"), "day", 3653).As("expiresAt"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L85-L90)

### TIMESTAMP_SUB

**Syntax:**
    
    
    timestamp_sub(timestamp: TIMESTAMP | BSON_TIMESTAMP, unit: STRING, amount: INT64) -> TIMESTAMP
    

**Description:**

Subtracts an `amount` of `unit` from `timestamp`. The `amount` argument can be negative, in that case it is equivalent to TIMESTAMP_ADD.

The `unit` argument must be a string and one of the following:

  * `microsecond`
  * `millisecond`
  * `second`
  * `minute`
  * `hour`
  * `day`



Throws an error if the resulting timestamp does not fit within the `TIMESTAMP` range.

**Examples:**

`timestamp` | `unit` | `amount` | `timestamp_sub(timestamp, unit, amount)`  
---|---|---|---  
2026-07-04 00:00:00 UTC | "minute" | 40L | 2026-07-03 23:20:00 UTC  
2026-07-04 00:00:00 UTC | "hour" | -24L | 2026-07-05 00:00:00 UTC  
2026-07-04 00:00:00 UTC | "day" | 3L | 2026-07-01 00:00:00 UTC  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("expiresAt").timestampSubtract("day", 14).as("sendWarningTimestamp")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2034-L2039)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("expiresAt").timestampSubtract("day", 14).as("sendWarningTimestamp")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3308-L3313)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("expiresAt").timestampSubtract(14, .day).as("sendWarningTimestamp")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1277-L1282)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("expiresAt")
              .timestampSubtract("day", 14)
              .alias("sendWarningTimestamp")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2637-L2644)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("expiresAt").timestampSubtract("day", 14).alias("sendWarningTimestamp")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2884-L2889)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(
            Field.of("expiresAt")
            .timestamp_subtract("day", 14)
            .as_("sendWarningTimestamp")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1636-L1647)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(timestampSubtract(field("expiresAt"), "day", 14).as("sendWarningTimestamp"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1579-L1585)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.TimestampSubtract(firestore.FieldOf("expiresAt"), "day", 14).As("sendWarningTimestamp"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L104-L109)

### TIMESTAMP_TO_UNIX_MICROS

**Syntax:**
    
    
    timestamp_to_unix_micros(input: TIMESTAMP | BSON_TIMESTAMP) -> INT64
    

**Description:**

Converts `input` to the number of microseconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the microsecond.

**Examples:**

`input` | `timestamp_to_unix_micros(input)`  
---|---  
1970-01-01 00:00:00 UTC | 0L  
1970-01-01 00:06:40.123456 UTC | 400123456L  
1969-12-31 23:59:59 UTC | -1000000L  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixMicros().as("unixMicros")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2046-L2051)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixMicros().as("unixMicros")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3320-L3325)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("dateString").timestampToUnixMicros().as("unixMicros")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1290-L1295)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixMicros().alias("unixMicros")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2652-L2657)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixMicros().alias("unixMicros")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2897-L2902)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(Field.of("dateString").timestamp_to_unix_micros().as_("unixMicros"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1655-L1662)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(timestampToUnixMicros(field("dateString")).as("unixMicros"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1592-L1598)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.TimestampToUnixMicros(firestore.FieldOf("dateString")).As("unixMicros"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L123-L128)

### TIMESTAMP_TO_UNIX_MILLIS

**Syntax:**
    
    
    timestamp_to_unix_millis(input: TIMESTAMP | BSON_TIMESTAMP) -> INT64
    

**Description:**

Converts `input` to the number of milliseconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the millisecond.

**Examples:**

`input` | `timestamp_to_unix_millis(input)`  
---|---  
1970-01-01 00:00:00 UTC | 0L  
1970-01-01 01:06:40.123 UTC | 4000123L  
1969-12-31 23:43:20 | -1000000L  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixMillis().as("unixMillis")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2058-L2063)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixMillis().as("unixMillis")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3332-L3337)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("dateString").timestampToUnixMillis().as("unixMillis")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1303-L1308)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixMillis().alias("unixMillis")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2665-L2670)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixMillis().alias("unixMillis")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2910-L2915)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(Field.of("dateString").timestamp_to_unix_millis().as_("unixMillis"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1670-L1677)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(timestampToUnixMillis(field("dateString")).as("unixMillis"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1605-L1611)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.TimestampToUnixMillis(firestore.FieldOf("dateString")).As("unixMillis"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L142-L147)

### TIMESTAMP_TO_UNIX_SECONDS

**Syntax:**
    
    
    timestamp_to_unix_seconds(input: TIMESTAMP | BSON_TIMESTAMP) -> INT64
    

**Description:**

Converts `input` to the number of seconds since `1970-01-01 00:00:00 UTC`. Truncates higher levels of precision by rounding down to the beginning of the second.

**Examples:**

`input` | `timestamp_to_unix_seconds(input)`  
---|---  
1970-01-01 00:00:00 UTC | 0L  
1970-01-01 00:01:00 UTC | 60L  
1969-12-31 23:55:00 UTC | -300L  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixSeconds().as("unixSeconds")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2070-L2075)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("documents")
      .select(
        field("dateString").timestampToUnixSeconds().as("unixSeconds")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3344-L3349)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("documents")
      .select([
        Field("dateString").timestampToUnixSeconds().as("unixSeconds")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1316-L1321)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixSeconds().alias("unixSeconds")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2678-L2683)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("documents")
        .select(
            field("dateString").timestampToUnixSeconds().alias("unixSeconds")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2923-L2928)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("documents")
        .select(Field.of("dateString").timestamp_to_unix_seconds().as_("unixSeconds"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1685-L1692)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("documents")
            .select(timestampToUnixSeconds(field("dateString")).as("unixSeconds"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1618-L1624)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("documents").
    	Select(firestore.Fields(
    		firestore.TimestampToUnixSeconds(firestore.FieldOf("dateString")).As("unixSeconds"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_date_timestamp.go#L161-L166)

### TIMESTAMP_DIFF

**Syntax:**
    
    
    timestamp_diff(end: TIMESTAMP | BSON_TIMESTAMP, start: TIMESTAMP | BSON_TIMESTAMP, unit: STRING) -> INT64
    

**Description:**

Returns the whole number of specified `unit` intervals between two `TIMESTAMP`s.

  * Returns a negative value if `end` is before `start`.
  * Truncates any fractional unit. For example, `timestamp_diff("2021-01-01 00:00:01", "2021-01-01 00:00:00", "minute")` returns `0`.



The `unit` argument must be a string and one of the following:

  * `microsecond`
  * `millisecond`
  * `second`
  * `minute`
  * `hour`
  * `day`



**Examples:**

`end` | `start` | `unit` | `timestamp_diff(end, start, unit)`  
---|---|---|---  
2026-07-04 00:01:00 UTC | 2026-07-04 00:00:00 UTC | "second" | 60L  
2026-07-04 00:00:00 UTC | 2026-07-05 00:00:00 UTC | "day" | -1L  
2026-07-04 00:00:59 UTC | 2026-07-04 00:00:00 UTC | "minute" | 0L  
  
### TIMESTAMP_EXTRACT

**Syntax:**
    
    
    timestamp_extract(timestamp: TIMESTAMP | BSON_TIMESTAMP, part: STRING[, timezone: STRING]) -> INT64
    

**Description:**

Extracts a specific `part` (e.g. year, month, day) from `timestamp`.

The `part` argument must be a string and one of the following:

  * `microsecond`
  * `millisecond`
  * `second`
  * `minute`
  * `hour`
  * `day`
  * `dayofweek`: Returns a value between 1 (Sunday) and 7 (Saturday).
  * `dayofyear`
  * `week`: Returns the week number of the year, starting at 1 for the first Sunday of the year.
  * `week([weekday])`: Returns the week number of the year, starting on the specified `weekday`.
  * `month`
  * `quarter`
  * `year`
  * `isoweek`: Returns the ISO 8601 week number.
  * `isoyear`: Returns the ISO 8601 week-numbering year.



If the `timezone` argument is provided, the extraction will be based on the given timezone's calendar. The extraction will respect daylight savings time.

If `timezone` is not provided, extraction will be based on `UTC`.

The `timezone` argument should be a string representation of a timezone from the timezone database, for example `America/New_York`. A custom time offset can also be used by specifying an offset from `GMT`.

**Examples:**

`timestamp` | `part` | `timezone` | `timestamp_extract(timestamp, part, timezone)`  
---|---|---|---  
2025-02-20 10:20:30 UTC | "year" | Not provided | 2025  
2025-02-20 10:20:30 UTC | "day" | Not provided | 20  
2025-12-31 23:59:59 UTC | "year" | "Asia/Tokyo" | 2026  
  
## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
