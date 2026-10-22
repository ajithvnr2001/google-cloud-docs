---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/aggregate_functions/
title: Aggregate Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:07.442853+00:00
---

# Aggregate Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/aggregate_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Aggregate Functions Reference

## **Aggregate**

All aggregate functions can be used as top-level expressions in the `aggregate(...)` stage.

Name  | Description   
---|---  
`COUNT` | Returns the number of documents.   
`COUNT_IF` | Returns the count of documents where an expression evaluates to `TRUE`  
`COUNT_DISTINCT` | Returns the count of unique, non `NULL` values   
`SUM` | Returns the sum of all `NUMERIC` values   
`AVERAGE` | Returns the average of all `NUMERIC` values   
`MINIMUM` | Returns the minimum non `NULL` value   
`MAXIMUM` | Returns the maximum non `NULL` value   
`FIRST` | Returns the `expression` value for the first document.   
`LAST` | Returns the `expression` value for the last document.   
`ARRAY_AGG` | Returns an array of all input values.   
`ARRAY_AGG_DISTINCT` | Returns an array of all distinct input values.   
  
### COUNT

**Syntax:**
    
    
    count() -> INT64
    count(expression: ANY) -> INT64
    

**Description:**

Returns the count of documents from the previous stage where `expression` evaluates to any non-`NULL` value. If no `expression` is provided, returns the total count of documents from the previous stage.

##### Node.js
    
    
    // Total number of books in the collection
    const countOfAll = await db.pipeline()
      .collection("books")
      .aggregate(countAll().as("count"))
      .execute();
    
    // Number of books with nonnull `ratings` field
    const countField = await db.pipeline()
      .collection("books")
      .aggregate(field("ratings").count().as("count"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1286-L1296)

### Web
    
    
    // Total number of books in the collection
    const countOfAll = await execute(db.pipeline()
      .collection("books")
      .aggregate(countAll().as("count"))
    );
    
    // Number of books with nonnull `ratings` field
    const countField = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("ratings").count().as("count"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2563-L2573)

##### Swift
    
    
    // Total number of books in the collection
    let countAll = try await db.pipeline()
      .collection("books")
      .aggregate([CountAll().as("count")])
      .execute()
    
    // Number of books with nonnull `ratings` field
    let countField = try await db.pipeline()
      .collection("books")
      .aggregate([Field("ratings").count().as("count")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L465-L475)

##### Kotlin  
Android
    
    
    // Total number of books in the collection
    val countAll = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.countAll().alias("count"))
        .execute()
    
    // Number of books with nonnull `ratings` field
    val countField = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.count("ratings").alias("count"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1803-L1813)

##### Java  
Android
    
    
    // Total number of books in the collection
    Task<Pipeline.Snapshot> countAll = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.countAll().alias("count"))
        .execute();
    
    // Number of books with nonnull `ratings` field
    Task<Pipeline.Snapshot> countField = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.count("ratings").alias("count"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2049-L2059)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Count
    
    # Total number of books in the collection
    count_all = (
        client.pipeline().collection("books").aggregate(Count().as_("count")).execute()
    )
    
    # Number of books with nonnull `ratings` field
    count_field = (
        client.pipeline()
        .collection("books")
        .aggregate(Count("ratings").as_("count"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L570-L583)

##### Java
    
    
    // Total number of books in the collection
    Pipeline.Snapshot countAll =
        firestore.pipeline().collection("books").aggregate(countAll().as("count")).execute().get();
    
    // Number of books with nonnull `ratings` field
    Pipeline.Snapshot countField =
        firestore
            .pipeline()
            .collection("books")
            .aggregate(count("ratings").as("count"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L570-L581)

##### Go
    
    
    // Total number of books in the collection
    countAll, err := client.Pipeline().Collection("books").
    	Aggregate(firestore.Accumulators(firestore.CountAll().As("count"))).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    // Number of books with nonnull `ratings` field
    countField, err := client.Pipeline().
    	Collection("books").
    	Aggregate(firestore.Accumulators(firestore.Count("ratings").As("count"))).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_accumulators_aggregation.go#L28-L45)

### COUNT_IF

**Syntax:**
    
    
    count_if(expression: BOOLEAN) -> INT64
    

**Description:**

Returns the number of documents from the previous stage where `expression` evaluates to `TRUE`.

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .aggregate(
        field("rating").greaterThan(4).countIf().as("filteredCount")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1304-L1309)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(
        field("rating").greaterThan(4).countIf().as("filteredCount")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2581-L2586)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .aggregate([
        AggregateFunction("count_if", [Field("rating").greaterThan(4)]).as("filteredCount")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L484-L489)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .aggregate(
            AggregateFunction.countIf(field("rating").greaterThan(4)).alias("filteredCount")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1822-L1827)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .aggregate(
            AggregateFunction.countIf(field("rating").greaterThan(4)).alias("filteredCount")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2068-L2073)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .aggregate(Field.of("rating").greater_than(4).count_if().as_("filteredCount"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L593-L600)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .aggregate(countIf(field("rating").greaterThan(4)).as("filteredCount"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L589-L595)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Aggregate(firestore.Accumulators(
    		firestore.CountIf(firestore.FieldOf("rating").GreaterThan(4)).As("filteredCount"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_accumulators_aggregation.go#L54-L59)

### COUNT_DISTINCT

**Syntax:**
    
    
    count_distinct(expression: ANY) -> INT64
    

**Description:**

Returns the number of unique non-`NULL`, non-`ABSENT` values of `expression`.

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .aggregate(field("author").countDistinct().as("unique_authors"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1316-L1319)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("author").countDistinct().as("unique_authors"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2593-L2596)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .aggregate([AggregateFunction("count_distinct", [Field("author")]).as("unique_authors")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L497-L500)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.countDistinct("author").alias("unique_authors"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1835-L1838)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.countDistinct("author").alias("unique_authors"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2081-L2084)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .aggregate(Field.of("author").count_distinct().as_("unique_authors"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L608-L615)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .aggregate(countDistinct("author").as("unique_authors"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L602-L608)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Aggregate(firestore.Accumulators(
    		firestore.CountDistinct("author").As("unique_authors"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_accumulators_aggregation.go#L73-L78)

### SUM

**Syntax:**
    
    
    sum(expression: ANY) -> NUMBER
    

**Description:**

Returns the sum for all numerical values, ignoring non-numeric values. Returns `NaN` if any values are `NaN`.

The output will have the same type as the widest input type except in these cases:

  * An `INTEGER` will be converted to a `DOUBLE` if it cannot be represented as an `INTEGER`.



##### Node.js
    
    
    const result = await db.pipeline()
      .collection("cities")
      .aggregate(field("population").sum().as("totalPopulation"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1326-L1329)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("cities")
      .aggregate(field("population").sum().as("totalPopulation"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2603-L2606)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("cities")
      .aggregate([Field("population").sum().as("totalPopulation")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L508-L511)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("cities")
        .aggregate(AggregateFunction.sum("population").alias("totalPopulation"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1846-L1849)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("cities")
        .aggregate(AggregateFunction.sum("population").alias("totalPopulation"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2092-L2095)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("cities")
        .aggregate(Field.of("population").sum().as_("totalPopulation"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L623-L630)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("cities")
            .aggregate(sum("population").as("totalPopulation"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L615-L621)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("cities").
    	Aggregate(firestore.Accumulators(
    		firestore.Sum("population").As("totalPopulation"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_array.go#L28-L33)

### AVERAGE

**Syntax:**
    
    
    average(expression: ANY) -> FLOAT64
    

**Description:**

Returns the average for all numerical values, ignoring non-numeric values. Evaluates to `NaN` if any values are `NaN`, or `NULL` if no numerical values are aggregated.

The output will have the same type as the input type except in these cases:

  * An `INTEGER` will be converted to a `DOUBLE` if it cannot be represented as an `INTEGER`.



##### Node.js
    
    
    const result = await db.pipeline()
      .collection("cities")
      .aggregate(field("population").average().as("averagePopulation"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1336-L1339)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("cities")
      .aggregate(field("population").average().as("averagePopulation"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2613-L2616)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("cities")
      .aggregate([Field("population").average().as("averagePopulation")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L519-L522)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("cities")
        .aggregate(AggregateFunction.average("population").alias("averagePopulation"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1857-L1860)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("cities")
        .aggregate(AggregateFunction.average("population").alias("averagePopulation"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2103-L2106)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("cities")
        .aggregate(Field.of("population").average().as_("averagePopulation"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L638-L645)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("cities")
            .aggregate(average("population").as("averagePopulation"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L628-L634)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("cities").
    	Aggregate(firestore.Accumulators(
    		firestore.Average("population").As("averagePopulation"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_accumulators_aggregation.go#L92-L97)

### MINIMUM

**Syntax:**
    
    
    minimum(expression: ANY) -> ANY
    

**Description:**

Returns the minimum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering).

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .aggregate(field("price").minimum().as("minimumPrice"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1346-L1349)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").minimum().as("minimumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2623-L2626)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .aggregate([Field("price").minimum().as("minimumPrice")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L530-L533)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.minimum("price").alias("minimumPrice"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1868-L1871)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.minimum("price").alias("minimumPrice"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2114-L2117)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .aggregate(Field.of("price").minimum().as_("minimumPrice"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L653-L660)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .aggregate(minimum("price").as("minimumPrice"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L641-L647)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Aggregate(firestore.Accumulators(
    		firestore.Minimum("price").As("minimumPrice"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_array.go#L47-L52)

### MAXIMUM

**Syntax:**
    
    
    maximum(expression: ANY) -> ANY
    

**Description:**

Returns the maximum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/firestore/docs/concepts/data-types#value_type_ordering).

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .aggregate(field("price").maximum().as("maximumPrice"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1356-L1359)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .aggregate(field("price").maximum().as("maximumPrice"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2633-L2636)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .aggregate([Field("price").maximum().as("maximumPrice")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L541-L544)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.maximum("price").alias("maximumPrice"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1879-L1882)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .aggregate(AggregateFunction.maximum("price").alias("maximumPrice"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2125-L2128)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .aggregate(Field.of("price").maximum().as_("maximumPrice"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L668-L675)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .aggregate(maximum("price").as("maximumPrice"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L654-L660)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Aggregate(firestore.Accumulators(
    		firestore.Maximum("price").As("maximumPrice"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_array.go#L66-L71)

### FIRST

**Syntax:**
    
    
    first(expression: ANY) -> ANY
    

**Description:**

Returns the value of `expression` for the first returned document.

### LAST

**Syntax:**
    
    
    last(expression: ANY) -> ANY
    

**Description:**

Returns the value of `expression` for the last returned document.

### ARRAY_AGG

**Syntax:**
    
    
    array_agg(expression: ANY) -> ARRAY<ANY>
    

**Description:**

Returns an array containing all values of `expression` when evaluated on each document.

If the expression resolves to an absent value, it is converted to `NULL`.

The order of elements in the output array is not stable and shouldn't be relied upon.

### ARRAY_AGG_DISTINCT

**Syntax:**
    
    
    array_agg_distinct(expression: ANY) -> ARRAY<ANY>
    

**Description:**

Returns an array containing all distinct values of `expression` when evaluated on each document.

If the expression resolves to an absent value, it is converted to `NULL`.

The order of elements in the output array is not stable and shouldn't be relied upon.

## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
