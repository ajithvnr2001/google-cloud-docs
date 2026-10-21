---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/arithmetic_functions/
title: Arithmetic Functions Reference \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:28.881399+00:00
---

# Arithmetic Functions Reference  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/functions/arithmetic_functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Arithmetic Functions Reference

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L28-L33)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L47-L53)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L67-L72)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L86-L91)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L105-L111)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L125-L131)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L145-L150)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L164-L172)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L186-L199)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L213-L226)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L240-L245)

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
    
    [pipeline_snippets_arithmetic.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/6d3321b0e6be6f8f6a370c08bf5593f7f0558f6e/firestore/pipeline_snippets_arithmetic.go#L259-L264)

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

## What's next

  * See the [Pipeline Queries overview](https://docs.cloud.google.com/firestore/docs/pipeline/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
