---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/where/
title: Where (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:26.579757+00:00
---

# Where (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/where/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Where (Transformation Stage)

## Description

Filters the documents from the previous stage, returning only the documents where the condition evaluates to `true`.

## Examples

### Web
    
    
    let results;
    
    results = await execute(db.pipeline().collection("books")
      .where(field("rating").equal(5))
      .where(field("published").lessThan(1900))
    );
    
    results = await execute(db.pipeline().collection("books")
      .where(and(field("rating").equal(5), field("published").lessThan(1900)))
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2223-L2232)

##### Swift
    
    
    var results: Pipeline.Snapshot
    
    results = try await db.pipeline().collection("books")
      .where(Field("rating").equal(5))
      .where(Field("published").lessThan(1900))
      .execute()
    
    results = try await db.pipeline().collection("books")
      .where(Field("rating").equal(5) && Field("published").lessThan(1900))
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L127-L136)

##### Kotlin  
Android
    
    
    var results: Task<Pipeline.Snapshot>
    
    results = db.pipeline().collection("books")
        .where(field("rating").equal(5))
        .where(field("published").lessThan(1900))
        .execute()
    
    results = db.pipeline().collection("books")
        .where(Expression.and(field("rating").equal(5),
          field("published").lessThan(1900)))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1446-L1456)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results;
    
    results = db.pipeline().collection("books")
        .where(field("rating").equal(5))
        .where(field("published").lessThan(1900))
        .execute();
    
    results = db.pipeline().collection("books")
        .where(Expression.and(
            field("rating").equal(5),
            field("published").lessThan(1900)
        ))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1691-L1703)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import And, Field
    
    results = (
        client.pipeline()
        .collection("books")
        .where(Field.of("rating").equal(5))
        .where(Field.of("published").less_than(1900))
        .execute()
    )
    
    results = (
        client.pipeline()
        .collection("books")
        .where(And(Field.of("rating").equal(5), Field.of("published").less_than(1900)))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L128-L143)

##### Java
    
    
    Pipeline.Snapshot results1 =
        firestore
            .pipeline()
            .collection("books")
            .where(field("rating").equal(5))
            .where(field("published").lessThan(1900))
            .execute()
            .get();
    
    Pipeline.Snapshot results2 =
        firestore
            .pipeline()
            .collection("books")
            .where(and(field("rating").equal(5), field("published").lessThan(1900)))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L151-L166)

##### Go
    
    
    results1, err := client.Pipeline().
    	Collection("books").
    	Where(firestore.FieldOf("rating").Equal(5)).
    	Where(firestore.FieldOf("published").LessThan(1900)).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    results2, err := client.Pipeline().
    	Collection("books").
    	Where(firestore.And(
    		firestore.FieldOf("rating").Equal(5),
    		firestore.FieldOf("published").LessThan(1900),
    	)).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1548-L1568)

## Behavior

### Chained versus Nested Filters

Multiple `where(...)` stages can be chained together, which is logically equivalent to combining the filter conditions within a single `where(...)` stage using an `and(...)` expression. Both approaches produce the same execution plan and have no impact on query execution or performance.

For example, chaining multiple `where(...)` stages:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .where(field("location.country").equals("USA"))
      .where(field("population").greaterThan(500000))
      .execute();
    

is equivalent to using a single `where(...)` stage with a compound `and(...)`:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .where(
        field("location.country").equals("USA")
          .and(field("population").greaterThan(500000)))
      .execute();
    

However, filtering based on a logical `or(...)` of conditions cannot be split across multiple stages and must be done in a single `where(...)` stage:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .where(
        field("location.state").equals("NY")
          .or(field("location.state").equals("CA")))
      .execute();
    

### Complex Expressions

The filter condition can contain complex filter conditions containing deeply nested expressions and logical operators. For example:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .where(
        field("name").like("San%")
        .or(
          field("location.state").charLength().greaterThan(7)
          .and(field("location.country").equals("USA"))))
    

filters `/cities` based on a regular expression, or if the city is in the `USA` with a long enough state name. Any expression can be given as the condition, but will only match those which evaluate to `true`.

### Stage Ordering

The order of stages is important as it can change the query evaluation order. For example the query:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .limit(10)
      .where(field("location.country").equals("USA"))
      .execute();
    

will only filter on `location.country` for a (potentially random) set of 10 documents as the prior [`limit(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit) stage is restricting the documents that are ever provided to the `where(...)` stage. Given this, the rule of thumb is to put the `where(...)` stages as early in the query as possible.

**`HAVING`-Like Functionality:**

The `where(...)` stage can come after any stage that changes the schema of the documents, like [`select(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/select) or [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate) and will refer to the fields produced from those stages. Importantly for [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate), a following `where(...)` clause that refers to the accumulated fields acts like a `HAVING` clause in a typical SQL system. For example:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .aggregate({
        accumulators: [field("population").sum().as("total_population")],
        groups: ["location.state"]
      })
      .where(field("total_population").greaterThan(10000000))
    

allows returning the states which have cities over a total population size.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
