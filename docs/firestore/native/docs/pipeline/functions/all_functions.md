---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/all_functions/
title: All Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:25.431751+00:00
---

# All Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/all_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# All Functions Reference

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
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_accumulators_aggregation.go#L28-L45)

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
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_accumulators_aggregation.go#L54-L59)

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
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_accumulators_aggregation.go#L73-L78)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L28-L33)

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
    
    [pipeline_snippets_accumulators_aggregation.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_accumulators_aggregation.go#L92-L97)

### MINIMUM

**Syntax:**
    
    
    minimum(expression: ANY) -> ANY
    

**Description:**

Returns the minimum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L47-L52)

### MAXIMUM

**Syntax:**
    
    
    maximum(expression: ANY) -> ANY
    

**Description:**

Returns the maximum non-`NULL`, non-absent value of the `expression` when evaluated on each document.

If there are no non-`NULL`, non-absent values, `NULL` is returned. This includes when no documents are considered.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L66-L71)

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

## **Arithmetic Functions**

All arithmetic functions in Firestore have the following behaviors:

  * Evaluates to `NULL` if any of the input parameters is `NULL`.
  * Evaluates to `NaN` if any of the arguments is `NaN`.
  * Generates an error if an overflow or underflow occurs.



Firestore performs **numeric type widening** based on the following hierarchy: `INT32` < `INT64` < `FLOAT64` < `DECIMAL128`. When an arithmetic function takes multiple numeric arguments of different types (for example, `add(5.0D, 6L)`), narrower types are implicitly converted to the widest type present among the operands. In the previous example, the `6L` is widened to `6.0D` resulting in the expression returning a `FLOAT64` type.

An implicit coercion from `INT64` -> `FLOAT64` can result in a loss of precision as the coerced value can lose of its least significant bits. The resulting value will be rounded version of the original integer value using IEEE 754 round-to-nearest mode.

Name  | Description   
---|---  
`ABS` | Returns the absolute value of a `number`  
`ADD` | Returns the value of `x + y`  
`SUBTRACT` | Returns the value of `x - y`  
`MULTIPLY` | Returns the value of `x * y`  
`DIVIDE` | Returns the value of `x / y`  
`MOD` | Returns the remainder of the division of `x / y`  
`CEIL` | Returns the ceiling of a `number`  
`FLOOR` | Returns the floor of a `number`  
`ROUND` | Rounds a `number` to `places` decimal places   
`TRUNC` | Truncates a `number` to `places` decimal places   
`POW` | Returns the value of `base^exponent`  
`SQRT` | Returns the square root of a `number`  
`EXP` | Returns Euler's number raised to the power of `exponent`  
`LN` | Returns the natural logarithm of a `number`  
`LOG` | Returns the logarithm of a `number`  
`LOG10` | Returns the logarithm of a `number` to base `10`  
`RAND` | Returns a pseudo-random floating point number   
  
### ABS

**Syntax:**
    
    
    abs[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N) -> N
    

**Description:**

Returns the absolute value of a `number`.

  * Throws an error when the function would overflow an `INT32` or `INT64` value.



**Examples:**

number | `abs(number)`  
---|---  
10 | 10  
-10 | 10  
10L | 10L  
-0.0 | 0.0  
10.5 | 10.5  
-10.5 | 10.5  
-231 | `[error]`  
-263 | `[error]`  
  
### ADD

**Syntax:**
    
    
    add[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](x: N, y: N) -> N
    

**Description:**

Returns the value of `x + y`.

**Examples:**

x | y | `add(x, y)`  
---|---|---  
20 | 3 | 23  
10.0 | 1 | 11.0  
22.5 | 2.0 | 24.5  
INT64.MAX | 1 | `[error]`  
INT64.MIN | -1 | `[error]`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("soldBooks").add(field("unsoldBooks")).as("totalBooks"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1366-L1369)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("soldBooks").add(field("unsoldBooks")).as("totalBooks"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2643-L2646)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("soldBooks").add(Field("unsoldBooks")).as("totalBooks")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L552-L555)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1890-L1893)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.add(field("soldBooks"), field("unsoldBooks")).alias("totalBooks"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2136-L2139)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("soldBooks").add(Field.of("unsoldBooks")).as_("totalBooks"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L683-L690)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(add(field("soldBooks"), field("unsoldBooks")).as("totalBooks"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L667-L673)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Add(firestore.FieldOf("soldBooks"), firestore.FieldOf("unsoldBooks")).As("totalBooks"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L28-L33)

### SUBTRACT

**Syntax:**
    
    
    subtract[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](x: N, y: N) -> N
    

**Description:**

Returns the value of `x - y`.

**Examples:**

x | y | `subtract(x, y)`  
---|---|---  
20 | 3 | 17  
10.0 | 1 | 9.0  
22.5 | 2.0 | 20.5  
INT64.MAX | -1 | `[error]`  
INT64.MIN | 1 | `[error]`  
  
##### Node.js
    
    
    const storeCredit = 7;
    const result = await db.pipeline()
      .collection("books")
      .select(field("price").subtract(constant(storeCredit)).as("totalCost"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1376-L1380)

### Web
    
    
    const storeCredit = 7;
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("price").subtract(constant(storeCredit)).as("totalCost"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2653-L2657)

##### Swift
    
    
    let storeCredit = 7
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("price").subtract(Constant(storeCredit)).as("totalCost")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L563-L567)

##### Kotlin  
Android
    
    
    val storeCredit = 7
    val result = db.pipeline()
        .collection("books")
        .select(Expression.subtract(field("price"), storeCredit).alias("totalCost"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1901-L1905)

##### Java  
Android
    
    
    int storeCredit = 7;
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.subtract(field("price"), storeCredit).alias("totalCost"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2147-L2151)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    store_credit = 7
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("price").subtract(store_credit).as_("totalCost"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L698-L706)

##### Java
    
    
    int storeCredit = 7;
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(subtract(field("price"), storeCredit).as("totalCost"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L680-L687)

##### Go
    
    
    storeCredit := 7
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Subtract(firestore.FieldOf("price"), storeCredit).As("totalCost"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L47-L53)

### MULTIPLY

**Syntax:**
    
    
    multiply[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](x: N, y: N) -> N
    

**Description:**

Returns the value of `x * y`.

**Examples:**

x | y | `multiply(x, y)`  
---|---|---  
20 | 3 | 60  
10.0 | 1 | 10.0  
22.5 | 2.0 | 45.0  
INT64.MAX | 2 | `[error]`  
INT64.MIN | 2 | `[error]`  
FLOAT64.MAX | FLOAT64.MAX | `+inf`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("price").multiply(field("soldBooks")).as("revenue"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1387-L1390)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("price").multiply(field("soldBooks")).as("revenue"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2664-L2667)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("price").multiply(Field("soldBooks")).as("revenue")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L575-L578)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(Expression.multiply(field("price"), field("soldBooks")).alias("revenue"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1913-L1916)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.multiply(field("price"), field("soldBooks")).alias("revenue"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2159-L2162)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("price").multiply(Field.of("soldBooks")).as_("revenue"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L714-L721)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(multiply(field("price"), field("soldBooks")).as("revenue"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L694-L700)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Multiply(firestore.FieldOf("price"), firestore.FieldOf("soldBooks")).As("revenue"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L67-L72)

### DIVIDE

**Syntax:**
    
    
    divide[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](x: N, y: N) -> N
    

**Description:**

Returns the value of `x / y`. Integer division is truncated.

**Examples:**

x | y | `divide(x, y)`  
---|---|---  
20 | 3 | 6  
10.0 | 3 | 3.333...  
22.5 | 2 | 11.25  
10 | 0 | `[error]`  
1.0 | 0.0 | `+inf`  
-1.0 | 0.0 | `-inf`  
0.0 | 0.0 | `NaN`  
`+inf` | `+inf` | `NaN`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("ratings").divide(field("soldBooks")).as("reviewRate"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1397-L1400)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("ratings").divide(field("soldBooks")).as("reviewRate"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2674-L2677)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("ratings").divide(Field("soldBooks")).as("reviewRate")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L586-L589)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(Expression.divide(field("ratings"), field("soldBooks")).alias("reviewRate"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1924-L1927)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.divide(field("ratings"), field("soldBooks")).alias("reviewRate"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2170-L2173)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("ratings").divide(Field.of("soldBooks")).as_("reviewRate"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L729-L736)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(divide(field("ratings"), field("soldBooks")).as("reviewRate"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L707-L713)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Divide(firestore.FieldOf("ratings"), firestore.FieldOf("soldBooks")).As("reviewRate"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L86-L91)

### MOD

**Syntax:**
    
    
    mod[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](x: N, y: N) -> N
    

**Description:**

Returns the remainder of `x / y`.

  * Throws an `error` when `y` is zero for integer types (`INT64`).
  * Returns `NaN` when `y` is zero for float types (`FLOAT64`).



**Examples:**

x | y | `mod(x, y)`  
---|---|---  
20 | 3 | 2  
-10 | 3 | -1  
10 | -3 | 1  
-10 | -3 | -1  
10 | 1 | 0  
22.5 | 2 | 0.5  
22.5 | 0.0 | `NaN`  
25 | 0 | `[error]`  
  
##### Node.js
    
    
    const displayCapacity = 1000;
    const result = await db.pipeline()
      .collection("books")
      .select(field("unsoldBooks").mod(constant(displayCapacity)).as("warehousedBooks"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1407-L1411)

### Web
    
    
    const displayCapacity = 1000;
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("unsoldBooks").mod(constant(displayCapacity)).as("warehousedBooks"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2684-L2688)

##### Swift
    
    
    let displayCapacity = 1000
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("unsoldBooks").mod(Constant(displayCapacity)).as("warehousedBooks")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L597-L601)

##### Kotlin  
Android
    
    
    val displayCapacity = 1000
    val result = db.pipeline()
        .collection("books")
        .select(Expression.mod(field("unsoldBooks"), displayCapacity).alias("warehousedBooks"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1935-L1939)

##### Java  
Android
    
    
    int displayCapacity = 1000;
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.mod(field("unsoldBooks"), displayCapacity).alias("warehousedBooks"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2181-L2185)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    display_capacity = 1000
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("unsoldBooks").mod(display_capacity).as_("warehousedBooks"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L744-L752)

##### Java
    
    
    int displayCapacity = 1000;
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(mod(field("unsoldBooks"), displayCapacity).as("warehousedBooks"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L720-L727)

##### Go
    
    
    displayCapacity := 1000
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Mod(firestore.FieldOf("unsoldBooks"), displayCapacity).As("warehousedBooks"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L105-L111)

### CEIL

**Syntax:**
    
    
    ceil[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N) -> N
    

**Description:**

Returns the smallest integer value that isn't less than `number`.

**Examples:**

number | `ceil(number)`  
---|---  
20 | 20  
10 | 10  
0 | 0  
24L | 24L  
-0.4 | -0.0  
0.4 | 1.0  
22.5 | 23.0  
`NaN` | `NaN`  
`+inf` | `+inf`  
`-inf` | `-inf`  
  
##### Node.js
    
    
    const booksPerShelf = 100;
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("unsoldBooks").divide(constant(booksPerShelf)).ceil().as("requiredShelves")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1418-L1424)

### Web
    
    
    const booksPerShelf = 100;
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("unsoldBooks").divide(constant(booksPerShelf)).ceil().as("requiredShelves")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2695-L2701)

##### Swift
    
    
    let booksPerShelf = 100
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("unsoldBooks").divide(Constant(booksPerShelf)).ceil().as("requiredShelves")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L609-L615)

##### Kotlin  
Android
    
    
    val booksPerShelf = 100
    val result = db.pipeline()
        .collection("books")
        .select(
            Expression.divide(field("unsoldBooks"), booksPerShelf).ceil().alias("requiredShelves")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1947-L1953)

##### Java  
Android
    
    
    int booksPerShelf = 100;
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            Expression.divide(field("unsoldBooks"), booksPerShelf).ceil().alias("requiredShelves")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2193-L2199)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    books_per_shelf = 100
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("unsoldBooks")
            .divide(books_per_shelf)
            .ceil()
            .as_("requiredShelves")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L760-L773)

##### Java
    
    
    int booksPerShelf = 100;
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(ceil(divide(field("unsoldBooks"), booksPerShelf)).as("requiredShelves"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L734-L741)

##### Go
    
    
    booksPerShelf := 100
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Ceil(firestore.Divide(firestore.FieldOf("unsoldBooks"), booksPerShelf)).As("requiredShelves"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L125-L131)

### FLOOR

**Syntax:**
    
    
    floor[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N) -> N
    

**Description:**

Returns the largest integer value that isn't greater than `number`.

**Examples:**

number | `floor(number)`  
---|---  
20 | 20  
10 | 10  
0 | 0  
2147483648 | 2147483648  
-0.4 | -1.0  
0.4 | 0.0  
22.5 | 22.0  
`NaN` | `NaN`  
`+inf` | `+inf`  
`-inf` | `-inf`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .addFields(
        field("wordCount").divide(field("pages")).floor().as("wordsPerPage")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1431-L1436)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .addFields(
        field("wordCount").divide(field("pages")).floor().as("wordsPerPage")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2708-L2713)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .addFields([
        Field("wordCount").divide(Field("pages")).floor().as("wordsPerPage")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L623-L628)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .addFields(
            Expression.divide(field("wordCount"), field("pages")).floor().alias("wordsPerPage")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1961-L1966)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .addFields(
            Expression.divide(field("wordCount"), field("pages")).floor().alias("wordsPerPage")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2207-L2212)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .add_fields(
            Field.of("wordCount").divide(Field.of("pages")).floor().as_("wordsPerPage")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L781-L790)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .addFields(floor(divide(field("wordCount"), field("pages"))).as("wordsPerPage"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L748-L754)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	AddFields(firestore.Selectables(
    		firestore.Floor(firestore.Divide(firestore.FieldOf("wordCount"), firestore.FieldOf("pages"))).As("wordsPerPage"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L145-L150)

### ROUND

**Syntax:**
    
    
    round[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N) -> N
    round[N <: INT32 | INT64 | FLOAT64 | DECIMAL128](number: N, places: INT64) -> N
    

**Description:**

Rounds `places` digits off a `number`. Rounds digits from the right of the decimal point if `places` is positive, and to the left of the decimal point if it is negative.

  * If only `number` is provided, rounds to the nearest whole value.
  * Rounds away from zero in halfway cases.
  * An `error` is thrown if rounding with a negative `places` value results in overflow.



**Examples:**

number | places | `round(number, places)`  
---|---|---  
15.5 | 0 | 16.0  
-15.5 | 0 | -16.0  
15 | 1 | 15  
15 | 0 | 15  
15 | -1 | 20  
15 | -2 | 0  
15.48924 | 1 | 15.5  
231-1 | -1 | `[error]`  
263-1L | -1 | `[error]`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("soldBooks").multiply(field("price")).round().as("partialRevenue"))
      .aggregate(field("partialRevenue").sum().as("totalRevenue"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1443-L1447)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("soldBooks").multiply(field("price")).round().as("partialRevenue"))
      .aggregate(field("partialRevenue").sum().as("totalRevenue"))
      );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2720-L2724)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("soldBooks").multiply(Field("price")).round().as("partialRevenue")])
      .aggregate([Field("partialRevenue").sum().as("totalRevenue")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L636-L640)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
        .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1974-L1978)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(Expression.multiply(field("soldBooks"), field("price")).round().alias("partialRevenue"))
        .aggregate(AggregateFunction.sum("partialRevenue").alias("totalRevenue"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2220-L2224)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("soldBooks")
            .multiply(Field.of("price"))
            .round()
            .as_("partialRevenue")
        )
        .aggregate(Field.of("partialRevenue").sum().as_("totalRevenue"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L798-L811)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(round(multiply(field("soldBooks"), field("price"))).as("partialRevenue"))
            .aggregate(sum("partialRevenue").as("totalRevenue"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L761-L768)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Round(firestore.Multiply(firestore.FieldOf("soldBooks"), firestore.FieldOf("price"))).As("partialRevenue"),
    	)).
    	Aggregate(firestore.Accumulators(
    		firestore.Sum("partialRevenue").As("totalRevenue"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L164-L172)

### TRUNC

**Syntax:**
    
    
    trunc[N <: Number](number: N) -> N
    trunc[N <: Number](number:  N, places: INT64) -> N
    

**Description:**

Truncates a `number` to a specified number of `places` decimal places. Truncates digits from the right of the decimal point if `places` is positive, and to the left of the decimal point if it is negative.

  * If only `number` is provided, truncates to the nearest whole value towards zero.
  * An `error` is thrown if truncating results in overflow.



**Examples:**

number | places | `trunc(number, places)`  
---|---|---  
15.5 | 0 | 15.0  
-15.5 | 0 | -15.0  
15 | 1 | 15  
15 | 0 | 15  
15 | -1 | 10  
15 | -2 | 0  
15.48924 | 1 | 15.4  
-15.48924 | 2 | -15.48  
  
### POW

**Syntax:**
    
    
    pow(base: FLOAT64, exponent: FLOAT64) -> FLOAT64
    

**Description:**

Returns the value `base` raised to the power of `exponent`.

  * Throws an error if `base <= 0` and `exponent` is negative.

  * For any `exponent` (including `NaN`), `pow(1, exponent)` is 1.

  * For any `base` (including `NaN`), `pow(base, 0)` is 1.




**Examples:**

base | exponent | `pow(base, exponent)`  
---|---|---  
2 | 3 | 8.0  
2 | -3 | 0.125  
`+inf` | 0 | 1.0  
1 | `+inf` | 1.0  
`NaN` | 0 | 1.0  
1 | `NaN` | 1.0  
`NaN` | `Numeric` | `NaN`  
`Numeric` | `NaN` | `NaN`  
-1 | 0.5 | `[error]`  
0 | -1 | `[error]`  
  
##### Node.js
    
    
    const googleplex = { latitude: 37.4221, longitude: 122.0853 };
    const result = await db.pipeline()
      .collection("cities")
      .addFields(
        field("lat").subtract(constant(googleplex.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        field("lng").subtract(constant(googleplex.longitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      )
      .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1454-L1472)

### Web
    
    
    const googleplex = { latitude: 37.4221, longitude: 122.0853 };
    const result = await execute(db.pipeline()
      .collection("cities")
      .addFields(
        field("lat").subtract(constant(googleplex.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        field("lng").subtract(constant(googleplex.longitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      )
      .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2731-L2749)

##### Swift
    
    
    let googleplex = CLLocation(latitude: 37.4221, longitude: 122.0853)
    let result = try await db.pipeline()
      .collection("cities")
      .addFields([
        Field("lat").subtract(Constant(googleplex.coordinate.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        Field("lng").subtract(Constant(googleplex.coordinate.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      ])
      .select([
        Field("latitudeDifference").add(Field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L648-L666)

##### Kotlin  
Android
    
    
    val googleplex = GeoPoint(37.4221, -122.0853)
    val result = db.pipeline()
        .collection("cities")
        .addFields(
            field("lat").subtract(googleplex.latitude)
                .multiply(111) // km per degree
                .pow(2)
                .alias("latitudeDifference"),
            field("lng").subtract(googleplex.longitude)
                .multiply(111) // km per degree
                .pow(2)
                .alias("longitudeDifference")
        )
        .select(
            field("latitudeDifference").add(field("longitudeDifference")).sqrt()
                // Inaccurate for large distances or close to poles
                .alias("approximateDistanceToGoogle")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1986-L2004)

##### Java  
Android
    
    
    GeoPoint googleplex = new GeoPoint(37.4221, -122.0853);
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("cities")
        .addFields(
            field("lat").subtract(googleplex.getLatitude())
                .multiply(111 /* km per degree */)
                .pow(2)
                .alias("latitudeDifference"),
            field("lng").subtract(googleplex.getLongitude())
                .multiply(111 /* km per degree */)
                .pow(2)
                .alias("longitudeDifference")
        )
        .select(
            field("latitudeDifference").add(field("longitudeDifference")).sqrt()
                // Inaccurate for large distances or close to poles
                .alias("approximateDistanceToGoogle")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2232-L2250)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    googleplexLat = 37.4221
    googleplexLng = -122.0853
    result = (
        client.pipeline()
        .collection("cities")
        .add_fields(
            Field.of("lat")
            .subtract(googleplexLat)
            .multiply(111)  # km per degree
            .pow(2)
            .as_("latitudeDifference"),
            Field.of("lng")
            .subtract(googleplexLng)
            .multiply(111)  # km per degree
            .pow(2)
            .as_("longitudeDifference"),
        )
        .select(
            Field.of("latitudeDifference")
            .add(Field.of("longitudeDifference"))
            .sqrt()
            # Inaccurate for large distances or close to poles
            .as_("approximateDistanceToGoogle")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L819-L846)

##### Java
    
    
    double googleplexLat = 37.4221;
    double googleplexLng = -122.0853;
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("cities")
            .addFields(
                pow(multiply(subtract(field("lat"), googleplexLat), 111), 2)
                    .as("latitudeDifference"),
                pow(multiply(subtract(field("lng"), googleplexLng), 111), 2)
                    .as("longitudeDifference"))
            .select(
                sqrt(add(field("latitudeDifference"), field("longitudeDifference")))
                    // Inaccurate for large distances or close to poles
                    .as("approximateDistanceToGoogle"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L775-L791)

##### Go
    
    
    googleplexLat := 37.4221
    googleplexLng := -122.0853
    snapshot := client.Pipeline().
    	Collection("cities").
    	AddFields(firestore.Selectables(
    		firestore.Pow(firestore.Multiply(firestore.Subtract(firestore.FieldOf("lat"), googleplexLat), 111), 2).As("latitudeDifference"),
    		firestore.Pow(firestore.Multiply(firestore.Subtract(firestore.FieldOf("lng"), googleplexLng), 111), 2).As("longitudeDifference"),
    	)).
    	Select(firestore.Fields(
    		firestore.Sqrt(firestore.Add(firestore.FieldOf("latitudeDifference"), firestore.FieldOf("longitudeDifference"))).
    			// Inaccurate for large distances or close to poles
    			As("approximateDistanceToGoogle"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L186-L199)

### SQRT

**Syntax:**
    
    
    sqrt[N <: FLOAT64 | DECIMAL128](number: N) -> N
    

**Description:**

Returns the square root of a `number`.

  * Throws an `error` if `number` is negative.



**Examples:**

number | `sqrt(number)`  
---|---  
25 | 5.0  
12.002 | 3.464...  
0.0 | 0.0  
`NaN` | `NaN`  
`+inf` | `+inf`  
`-inf` | `[error]`  
`x < 0` | `[error]`  
  
##### Node.js
    
    
    const googleplex = { latitude: 37.4221, longitude: 122.0853 };
    const result = await db.pipeline()
      .collection("cities")
      .addFields(
        field("lat").subtract(constant(googleplex.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        field("lng").subtract(constant(googleplex.longitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      )
      .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1479-L1497)

### Web
    
    
    const googleplex = { latitude: 37.4221, longitude: 122.0853 };
    const result = await execute(db.pipeline()
      .collection("cities")
      .addFields(
        field("lat").subtract(constant(googleplex.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        field("lng").subtract(constant(googleplex.longitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      )
      .select(
        field("latitudeDifference").add(field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2756-L2774)

##### Swift
    
    
    let googleplex = CLLocation(latitude: 37.4221, longitude: 122.0853)
    let result = try await db.pipeline()
      .collection("cities")
      .addFields([
        Field("lat").subtract(Constant(googleplex.coordinate.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("latitudeDifference"),
        Field("lng").subtract(Constant(googleplex.coordinate.latitude))
          .multiply(111 /* km per degree */)
          .pow(2)
          .as("longitudeDifference")
      ])
      .select([
        Field("latitudeDifference").add(Field("longitudeDifference")).sqrt()
          // Inaccurate for large distances or close to poles
          .as("approximateDistanceToGoogle")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L674-L692)

##### Kotlin  
Android
    
    
    val googleplex = GeoPoint(37.4221, -122.0853)
    val result = db.pipeline()
        .collection("cities")
        .addFields(
            field("lat").subtract(googleplex.latitude)
                .multiply(111) // km per degree
                .pow(2)
                .alias("latitudeDifference"),
            field("lng").subtract(googleplex.longitude)
                .multiply(111) // km per degree
                .pow(2)
                .alias("longitudeDifference")
        )
        .select(
            field("latitudeDifference").add(field("longitudeDifference")).sqrt()
                // Inaccurate for large distances or close to poles
                .alias("approximateDistanceToGoogle")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2012-L2030)

##### Java  
Android
    
    
    GeoPoint googleplex = new GeoPoint(37.4221, -122.0853);
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("cities")
        .addFields(
            field("lat").subtract(googleplex.getLatitude())
                .multiply(111 /* km per degree */)
                .pow(2)
                .alias("latitudeDifference"),
            field("lng").subtract(googleplex.getLongitude())
                .multiply(111 /* km per degree */)
                .pow(2)
                .alias("longitudeDifference")
        )
        .select(
            field("latitudeDifference").add(field("longitudeDifference")).sqrt()
                // Inaccurate for large distances or close to poles
                .alias("approximateDistanceToGoogle")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2258-L2276)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    googleplexLat = 37.4221
    googleplexLng = -122.0853
    result = (
        client.pipeline()
        .collection("cities")
        .add_fields(
            Field.of("lat")
            .subtract(googleplexLat)
            .multiply(111)  # km per degree
            .pow(2)
            .as_("latitudeDifference"),
            Field.of("lng")
            .subtract(googleplexLng)
            .multiply(111)  # km per degree
            .pow(2)
            .as_("longitudeDifference"),
        )
        .select(
            Field.of("latitudeDifference")
            .add(Field.of("longitudeDifference"))
            .sqrt()
            # Inaccurate for large distances or close to poles
            .as_("approximateDistanceToGoogle")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L854-L881)

##### Java
    
    
    double googleplexLat = 37.4221;
    double googleplexLng = -122.0853;
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("cities")
            .addFields(
                pow(multiply(subtract(field("lat"), googleplexLat), 111), 2)
                    .as("latitudeDifference"),
                pow(multiply(subtract(field("lng"), googleplexLng), 111), 2)
                    .as("longitudeDifference"))
            .select(
                sqrt(add(field("latitudeDifference"), field("longitudeDifference")))
                    // Inaccurate for large distances or close to poles
                    .as("approximateDistanceToGoogle"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L798-L814)

##### Go
    
    
    googleplexLat := 37.4221
    googleplexLng := -122.0853
    snapshot := client.Pipeline().
    	Collection("cities").
    	AddFields(firestore.Selectables(
    		firestore.Pow(firestore.Multiply(firestore.Subtract(firestore.FieldOf("lat"), googleplexLat), 111), 2).As("latitudeDifference"),
    		firestore.Pow(firestore.Multiply(firestore.Subtract(firestore.FieldOf("lng"), googleplexLng), 111), 2).As("longitudeDifference"),
    	)).
    	Select(firestore.Fields(
    		firestore.Sqrt(firestore.Add(firestore.FieldOf("latitudeDifference"), firestore.FieldOf("longitudeDifference"))).
    			// Inaccurate for large distances or close to poles
    			As("approximateDistanceToGoogle"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L213-L226)

### EXP

**Syntax:**
    
    
    exp(exponent: FLOAT64) -> FLOAT64
    

**Description:**

Returns the value of Euler's number raised to the power of `exponent`, also called the natural exponential function.

**Examples:**

exponent | `exp(exponent)`  
---|---  
0.0 | 1.0  
10 | `e^10` (`FLOAT64`)  
`NaN` | `NaN`  
`+inf` | `+inf`  
`-inf` | 0  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").exp().as("expRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1504-L1507)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").exp().as("expRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2781-L2784)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").exp().as("expRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L700-L703)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").exp().alias("expRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2038-L2041)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").exp().alias("expRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2284-L2287)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").exp().as_("expRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L889-L896)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(exp(field("rating")).as("expRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L821-L827)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Exp(firestore.FieldOf("rating")).As("expRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L240-L245)

### LN

**Syntax:**
    
    
    ln(number: FLOAT64) -> FLOAT64
    

**Description:**

Returns the natural logarithm of `number`. This function is equivalent to `log(number)`.

**Examples:**

number | `ln(number)`  
---|---  
1 | 0.0  
2L | 0.693...  
1.0 | 0.0  
`e` (`FLOAT64`) | 1.0  
`NaN` | `NaN`  
`-inf` | `NaN`  
`+inf` | `+inf`  
`x <= 0` | `[error]`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").ln().as("lnRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1514-L1517)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").ln().as("lnRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2791-L2794)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").ln().as("lnRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L711-L714)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").ln().alias("lnRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2049-L2052)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").ln().alias("lnRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2295-L2298)
    
    
        

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").ln().as_("lnRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L904-L911)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(ln(field("rating")).as("lnRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L834-L840)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.Ln(firestore.FieldOf("rating")).As("lnRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_arithmetic.go#L259-L264)

### LOG

**Syntax:**
    
    
    log(number: FLOAT64, base: FLOAT64) -> FLOAT64
    log(number: FLOAT64) -> FLOAT64
    

**Description:**

Returns the logarithm of a `number` to `base`.

  * If only `number` is provided, returns the logarithm of `number` to `base` (synonymous to `ln(number)`).



**Examples:**

number | base | `log(number, base)`  
---|---|---  
100 | 10 | 2.0  
`NaN` | `Numeric` | `NaN`  
`Numeric` | `NaN` | `NaN`  
`-inf` | `Numeric` | `NaN`  
`Numeric`. | `+inf` | `NaN`  
`number <= 0` | `Numeric` | `[error]`  
`Numeric` | `base <= 0` | `[error]`  
`Numeric` | 1.0 | `[error]`  
  
### LOG10

**Syntax:**
    
    
    log10(x: FLOAT64) -> FLOAT64
    

**Description:**

Returns the logarithm of a `number` to base `10`.

**Examples:**

number | `log10(number)`  
---|---  
100 | 2.0  
`NaN` | `NaN`  
`-inf` | `NaN`  
`+inf` | `+inf`  
`x <= 0` | `[error]`  
  
### RAND

**Syntax:**
    
    
    rand() -> FLOAT64
    

**Description:**

Return a pseudo-random floating point number, chosen uniformly between `0.0` (inclusive) and `1.0` (exclusive).

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L85-L90)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L104-L109)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L123-L128)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L142-L147)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L161-L166)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L180-L185)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L28-L33)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L47-L52)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L66-L71)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L85-L90)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L104-L109)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L123-L128)

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
  
## **Debugging Functions**

Name  | Description   
---|---  
`EXISTS` | Returns `TRUE` if the value is not an absent value   
`IS_ABSENT` | Returns `TRUE` if the value is an absent value   
`IF_ABSENT` | Replaces the value with an expression if it is absent   
`IS_ERROR` | Catches and checks if an error has been thrown by the underlying expression   
`IF_ERROR` | Replaces the value with an expression if it has thrown an error   
`ERROR` | Terminates evaluation and returns an error with the specified message   
  
### EXISTS

**Syntax:**
    
    
    exists(value: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is not the absent value.

**Examples:**

`value` | `exists(value)`  
---|---  
0L | `TRUE`  
"foo" | `TRUE`  
`NULL` | `TRUE`  
`ABSENT` | `FALSE`  
  
##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(field("rating").exists().as("hasRating"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L1658-L1661)

### Web

**Example:**
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(field("rating").exists().as("hasRating"))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2935-L2938)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([Field("rating").exists().as("hasRating")])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L869-L872)

##### Kotlin  
Android

**Example:**
    
    
    val result = db.pipeline()
        .collection("books")
        .select(field("rating").exists().alias("hasRating"))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2207-L2210)

##### Java  
Android

**Example:**
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(field("rating").exists().alias("hasRating"))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2453-L2456)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("rating").exists().as_("hasRating"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1126-L1133)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(exists(field("rating")).as("hasRating"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1020-L1026)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.FieldExists(firestore.FieldOf("rating")).As("hasRating"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L28-L33)

### IS_ABSENT

**Syntax:**
    
    
    is_absent(value: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if `value` is the absent value, and `FALSE` otherwise. Absent values are values that are missing from the input, such as a missing document field.

**Examples:**

`value` | `is_absent(value)`  
---|---  
0L | `FALSE`  
"foo" | `FALSE`  
`NULL` | `FALSE`  
`ABSENT` | `TRUE`  
  
### IF_ABSENT

**Syntax:**
    
    
    if_absent(value: ANY, replacement: ANY) -> ANY
    

**Description:**

If `value` is an absent value, evaluates and returns `replacement`. Otherwise returns `value`.

**Examples:**

`value` | `replacement` | `if_absent(value, replacement)`  
---|---|---  
5L | 0L | 5L  
`NULL` | 0L | `NULL`  
`ABSENT` | 0L | 0L  
  
### IS_ERROR

**Syntax:**
    
    
    is_error(try: ANY) -> BOOLEAN
    

**Description:**

Returns `TRUE` if an error is thrown during the evaluation of `try`. Returns `FALSE` otherwise.

### IF_ERROR

**Syntax:**
    
    
    if_error(try: ANY, catch: ANY) -> ANY
    

**Description:**

If an error is thrown during the evaluation of `try`, evaluates and returns `replacement`. Otherwise returns the resolved value of `try`.

### ERROR

**Syntax:**
    
    
    error(message: STRING) -> ANY
    

**Description:**

Evaluation of the `error` function results in the evaluation of the pipeline to terminate with an error. The given `message` is included in the error.

**Examples:**

`cond` | `res` | `switch_on(cond, res, error("no condition matched"))`  
---|---|---  
`TRUE` | 1L | 1L  
`FALSE` | 1L | `ERROR ("no condition matched")`  
  
## **Reference Functions**

The `REFERENCE` type acts as a "pointer" to other documents in the database (or even other databases). The following functions allow manipulating this type during query execution.

Name  | Description   
---|---  
`COLLECTION_ID` | Returns the ID of the leaf collection in the given reference   
`DOCUMENT_ID` | Returns the ID of the document in the given reference   
`PARENT` | Returns the parent reference   
`REFERENCE_SLICE` | Returns a subset of segments from the given reference   
  
### COLLECTION_ID

**Syntax:**
    
    
    collection_id(ref: REFERENCE) -> STRING
    

**Description:**

Returns the leaf collection ID of the given `REFERENCE`.

**Examples:**

`ref` | `collection_id(ref)`  
---|---  
`users/user1` | `"users"`  
`users/user1/posts/post1` | `"posts"`  
  
### DOCUMENT_ID

**Syntax:**
    
    
    document_id(ref: REFERENCE) -> ANY
    

**Description:**

Returns the document ID of the given `REFERENCE`.

**Examples:**

`ref` | `document_id(ref)`  
---|---  
`users/user1` | `"user1"`  
`users/user1/posts/post1` | `"post1"`  
  
### PARENT

**Syntax:**
    
    
    parent(ref: REFERENCE) -> REFERENCE
    

**Description:**

Returns the parent `REFERENCE` of the given reference, or `NULL` if the ref is a root reference already.

**Examples:**

`ref` | `parent(ref)`  
---|---  
`/` | `NULL`  
`users/user1` | `/`  
`users/user1/posts/post1` | `users/user1`  
  
### REFERENCE_SLICE

**Syntax:**
    
    
    reference_slice(ref: REFERENCE, offset: INT, length: INT) -> REFERENCE
    

**Description:**

A `REFERENCE` is a list of `(collection_id, document_id)` tuples and this allows getting a view of that list, just like `array_slice(...)`.

Returns a new `REFERENCE` that is a subset of the segments of the given `ref`.

  * `offset`: The starting index (0-based) of the slice. If negative, it is an offset from the end of the reference.
  * `length`: The number of segments to include in the slice.



**Examples:**

`ref` | `offset` | `length` | `reference_slice(ref, offset, length)`  
---|---|---|---  
`a/1/b/2/c/3` | 1L | 2L | `b/2/c/3`  
`a/1/b/2/c/3` | 0L | 2L | `a/1/b/2`  
`a/1/b/2/c/3` | -2L | 2L | `c/3`  
  
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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L47-L55)

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L69-L77)

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L91-L99)

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L113-L118)

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L132-L144)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L199-L204)

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
    
    [pipeline_snippets_array.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_array.go#L218-L223)

### MAXIMUM

**Syntax:**
    
    
    maximum(x: ANY...) -> ANY
    maximum(x: ARRAY) -> ANY
    

**Description:**

Returns the maximum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple maximum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L158-L163)

### MINIMUM

**Syntax:**
    
    
    minimum(x: ANY...) -> ANY
    minimum(x: ARRAY) -> ANY
    

**Description:**

Returns the minimum non-`NULL`, non-`ABSENT` value in a series of values `x`.

If there are no non-`NULL`, non-`ABSENT` values, `NULL` is returned.

If there are multiple minimum equivalent values, any one of those values can be returned. Value type ordering follows [documented ordering](https://docs.cloud.google.com/docs/firestore/manage-data/data-types#value_type_ordering).

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
    
    [pipeline_snippets_logical.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_logical.go#L177-L182)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L28-L33)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L47-L52)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L66-L71)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L85-L90)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L104-L109)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L123-L128)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L180-L185)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L199-L204)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L218-L223)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L237-L242)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L256-L261)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L275-L281)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L295-L300)

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
    
    [pipeline_snippets_string.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_string.go#L314-L319)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L28-L33)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L47-L52)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L66-L71)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L85-L90)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L104-L109)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L123-L128)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L142-L147)

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
    
    [pipeline_snippets_date_timestamp.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_date_timestamp.go#L161-L166)

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
    
    [pipeline_snippets_comparison.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_comparison.go#L123-L128)

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
  
## **Vector Functions**

Name  | Description   
---|---  
`COSINE_DISTANCE` | Returns the cosine distance between two vectors   
`DOT_PRODUCT` | Returns the dot product between two vectors   
`EUCLIDEAN_DISTANCE` | Returns the euclidean distance between two vectors   
`MANHATTAN_DISTANCE` | Returns the manhattan distance between two vectors   
`VECTOR_LENGTH` | Returns the number of elements in a vector   
  
### COSINE_DISTANCE

**Syntax:**
    
    
    cosine_distance(x: VECTOR, y: VECTOR) -> FLOAT64
    

**Description:**

Returns the cosine distance between `x` and `y`.

##### Node.js
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("embedding").cosineDistance(sampleVector).as("cosineDistance")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2082-L2088)

### Web
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("embedding").cosineDistance(sampleVector).as("cosineDistance")));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3356-L3360)

##### Swift
    
    
    let sampleVector = [0.0, 1, 2, 3, 4, 5]
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("embedding").cosineDistance(sampleVector).as("cosineDistance")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1329-L1335)

##### Kotlin  
Android
    
    
    val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
    val result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2691-L2697)

##### Java  
Android
    
    
    double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").cosineDistance(sampleVector).alias("cosineDistance")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2936-L2942)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    from google.cloud.firestore_v1.vector import Vector
    
    sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("embedding").cosine_distance(sample_vector).as_("cosineDistance")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1700-L1711)

##### Java
    
    
    double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(cosineDistance(field("embedding"), sampleVector).as("cosineDistance"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1631-L1638)

##### Go
    
    
    sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.CosineDistance(firestore.FieldOf("embedding"), sampleVector).As("cosineDistance"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_vector.go#L28-L34)

### DOT_PRODUCT

**Syntax:**
    
    
    dot_product(x: VECTOR, y: VECTOR) -> FLOAT64
    

**Description:**

Returns the dot product of `x` and `y`.

##### Node.js
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("embedding").dotProduct(sampleVector).as("dotProduct")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2095-L2101)

### Web
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("embedding").dotProduct(sampleVector).as("dotProduct")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3367-L3373)

##### Swift
    
    
    let sampleVector = [0.0, 1, 2, 3, 4, 5]
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("embedding").dotProduct(sampleVector).as("dotProduct")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1343-L1349)

##### Kotlin  
Android
    
    
    val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
    val result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").dotProduct(sampleVector).alias("dotProduct")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2705-L2711)

##### Java  
Android
    
    
    double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").dotProduct(sampleVector).alias("dotProduct")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2950-L2956)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    from google.cloud.firestore_v1.vector import Vector
    
    sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("embedding").dot_product(sample_vector).as_("dotProduct"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1719-L1728)

##### Java
    
    
    double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(dotProduct(field("embedding"), sampleVector).as("dotProduct"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1645-L1652)

##### Go
    
    
    sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.DotProduct(firestore.FieldOf("embedding"), sampleVector).As("dotProduct"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_vector.go#L48-L54)

### EUCLIDEAN_DISTANCE

**Syntax:**
    
    
    euclidean_distance(x: VECTOR, y: VECTOR) -> FLOAT64
    

**Description:**

Computes the euclidean distance between `x` and `y`.

##### Node.js
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2108-L2114)

### Web
    
    
    const sampleVector = [0.0, 1, 2, 3, 4, 5];
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3380-L3386)

##### Swift
    
    
    let sampleVector = [0.0, 1, 2, 3, 4, 5]
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("embedding").euclideanDistance(sampleVector).as("euclideanDistance")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1357-L1363)

##### Kotlin  
Android
    
    
    val sampleVector = doubleArrayOf(0.0, 1.0, 2.0, 3.0, 4.0, 5.0)
    val result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2719-L2725)

##### Java  
Android
    
    
    double[] sampleVector = {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").euclideanDistance(sampleVector).alias("euclideanDistance")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2964-L2970)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    from google.cloud.firestore_v1.vector import Vector
    
    sample_vector = Vector([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    result = (
        client.pipeline()
        .collection("books")
        .select(
            Field.of("embedding")
            .euclidean_distance(sample_vector)
            .as_("euclideanDistance")
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1736-L1749)

##### Java
    
    
    double[] sampleVector = new double[] {0.0, 1.0, 2.0, 3.0, 4.0, 5.0};
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(euclideanDistance(field("embedding"), sampleVector).as("euclideanDistance"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1659-L1666)

##### Go
    
    
    sampleVector := []float64{0.0, 1.0, 2.0, 3.0, 4.0, 5.0}
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.EuclideanDistance(firestore.FieldOf("embedding"), sampleVector).As("euclideanDistance"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_vector.go#L68-L74)

### MANHATTAN_DISTANCE

**Syntax:**
    
    
    manhattan_distance(x: VECTOR, y: VECTOR) -> FLOAT64
    

**Description:**

Computes the manhattan distance between `x` and `y`.

### VECTOR_LENGTH

**Syntax:**
    
    
    vector_length(vector: VECTOR) -> INT64
    

**Description:**

Returns the number of elements in a `VECTOR`.

##### Node.js
    
    
    const result = await db.pipeline()
      .collection("books")
      .select(
        field("embedding").vectorLength().as("vectorLength")
      )
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2121-L2126)

### Web
    
    
    const result = await execute(db.pipeline()
      .collection("books")
      .select(
        field("embedding").vectorLength().as("vectorLength")
      )
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3393-L3398)

##### Swift
    
    
    let result = try await db.pipeline()
      .collection("books")
      .select([
        Field("embedding").vectorLength().as("vectorLength")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1371-L1376)

##### Kotlin  
Android
    
    
    val result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").vectorLength().alias("vectorLength")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L2733-L2738)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> result = db.pipeline()
        .collection("books")
        .select(
            field("embedding").vectorLength().alias("vectorLength")
        )
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L2978-L2983)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    result = (
        client.pipeline()
        .collection("books")
        .select(Field.of("embedding").vector_length().as_("vectorLength"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L1757-L1764)

##### Java
    
    
    Pipeline.Snapshot result =
        firestore
            .pipeline()
            .collection("books")
            .select(vectorLength(field("embedding")).as("vectorLength"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L1673-L1679)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("books").
    	Select(firestore.Fields(
    		firestore.VectorLength(firestore.FieldOf("embedding")).As("vectorLength"),
    	)).
    	Execute(ctx)
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/pipeline_snippets_vector.go#L88-L93)

## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
