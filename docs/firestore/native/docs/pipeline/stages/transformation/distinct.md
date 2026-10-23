---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/distinct/
title: Distinct (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:50.644058+00:00
---

# Distinct (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/distinct/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Distinct (Transformation Stage)

## Description

Find all the distinct combination of values for a series of expressions.

The `distinct(...)` stage has similar syntax as [`select(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/select) as it takes one or more selectable expressions. Strings can be used when the expression is just a field reference:

## Examples

##### Node.js
    
    
    let cities = await db.pipeline()
      .collection("cities")
      .distinct("country")
      .execute();
    
    cities = await db.pipeline()
      .collection("cities")
      .distinct(
        field("state").toLower().as("normalizedState"),
        field("country"))
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L822-L832)

### Web
    
    
    let cities = await execute(db.pipeline()
      .collection("cities")
      .distinct("country"));
    
    cities = await execute(db.pipeline()
      .collection("cities")
      .distinct(
        field("state").toLower().as("normalizedState"),
        field("country")));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2100-L2108)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("books")
      .distinct([
        Field("author").toUpper().as("author"),
        Field("genre")
      ])
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L159-L165)

##### Kotlin  
Android
    
    
    var cities = db.pipeline()
        .collection("cities")
        .distinct("country")
        .execute()
    
    cities = db.pipeline()
        .collection("cities")
        .distinct(
            field("state").toLower().alias("normalizedState"),
            field("country")
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3555-L3566)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> cities;
    cities = db.pipeline()
            .collection("cities")
            .distinct("country")
            .execute();
    
    cities = db.pipeline()
            .collection("cities")
            .distinct(
                    field("state").toLower().alias("normalizedState"),
                    field("country"))
            .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L3928-L3939)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import Field
    
    cities = client.pipeline().collection("cities").distinct("country").execute()
    
    cities = (
        client.pipeline()
        .collection("cities")
        .distinct(Field.of("state").to_lower().as_("normalizedState"), "country")
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2814-L2823)

##### Java
    
    
    Pipeline.Snapshot cities1 =
        firestore.pipeline().collection("cities").distinct("country").execute().get();
    
    Pipeline.Snapshot cities2 =
        firestore
            .pipeline()
            .collection("cities")
            .distinct(toLower(field("state")).as("normalizedState"), field("country"))
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3023-L3032)

##### Go
    
    
    cities1, err := client.Pipeline().Collection("cities").Distinct(firestore.Fields("country")).Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    cities2, err := client.Pipeline().Collection("cities").
    	Distinct(firestore.Fields(
    		firestore.ToLower(firestore.FieldOf("state")).As("normalizedState"),
    		firestore.FieldOf("country"),
    	)).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L383-L398)

## Behavior

The `distinct(...)` stage works similarly to an [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate) stage without groups. See also [`aggregate(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/aggregate) and [`select(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/select).

### Find Distinct Field Values

For example, to get a list of every country in the following `cities` collection:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francisco", state: "CA", country: "USA"});
    await db.collection("cities").doc("LA").set({name: "Los Angeles", state: "CA", country: "USA"});
    await db.collection("cities").doc("NY").set({name: "New York", state: "NY", country: "USA"});
    await db.collection("cities").doc("TOR").set({name: "Toronto", state: null, country: "Canada"});
    await db.collection("cities").doc("MEX").set({name: "Mexico City", state: null, country: "Mexico"});
    

Distinct countries can be found using:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .distinct("country")
      .execute();
    

which generates the following result:
    
    
    { country: "USA" }
    { country: "Canada" }
    { country: "Mexico" }
    

### Distinct Output of Expressions

You can also find the distinct combinations of multiple fields, or more complicated expressions. For example:

### Node.js
    
    
    const cities = await db.pipeline()
      .collection("/cities")
      .distinct(
        field("state").toLower().as("normalized_state"),
        field("country"))
      .execute();
    

to get:
    
    
    { country: "USA", normalized_state: "ca" }
    { country: "USA", normalized_state: "ny" }
    { country: "Canada", normalized_state: null }
    { country: "Mexico", normalized_state: null }
    

### Equivalence Behaviors

The equivalence behavior on distinct values follows the same semantics as equalities.

This means that equivalent values, for example mathmatically equivalent numeric values, regardless of original types (32-bit integer, 64-bit integer, floating point numbers, decimal numbers, etc), are considered the same distinct value.

As an example, in a collection `numerics` with different documents containing `foo` values of 32-bit integer `1`, 64-bit integer `1L` and floating point `1.0` respectively, `distinct(...)` will only return 1 result.

In such cases of having different equivalent values present in the dataset, the output value of the group can be **any** of these equivalent values. In this example, this value of `foo` could be returned as `1`, `1L`, or `1.0`.

Even if it appears to be deterministic, you should **not** attempt to rely on the behavior of one specific value getting selected.

### Memory Usage

How the `distinct(...)` stage is executed depends on the available indexes. When there is not an appropriate index chosen by the query optimizer, `distinct(...)` requires buffering all distinct values in the memory.

In the event of having a very large number of distinct values, or values being very large (e.g. distinct on huge values), this stage may run out of memory.

In such cases, you should apply filters to limit the dataset to perform `distinct(...)` on, or create indexes as recommended to avoid large memory usages.

Query Explain will provide information on the actual query execution plan and profiling data to help with the debugging.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
