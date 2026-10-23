---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/
title: Vector Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:24.314492+00:00
---

# Vector Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/vector_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Vector Functions Reference

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
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_vector.go#L28-L34)

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
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_vector.go#L48-L54)

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
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_vector.go#L68-L74)

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
    
    [pipeline_snippets_vector.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_vector.go#L88-L93)

## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
