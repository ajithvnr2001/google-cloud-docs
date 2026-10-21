---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/find_nearest/
title: Find Nearest (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:57.259199+00:00
---

# Find Nearest (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/find_nearest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Find Nearest (Transformation Stage)

## Description

Performs a nearest neighbor vector search on the given `embedding` field using the requested distance_measure.

## Examples

##### Node.js
    
    
    const results = await db.pipeline()
      .collection("cities")
      .findNearest({
          field: "embedding",
          vectorValue: [1.5, 2.345],
          distanceMeasure: "euclidean"
      })
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L503-L510)

### Web
    
    
    const results = await execute(db.pipeline()
      .collection("cities")
      .findNearest({
          field: "embedding",
          vectorValue: [1.5, 2.345],
          distanceMeasure: "euclidean"
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L1797-L1803)

##### Swift
    
    
    let results = try await db.pipeline()
      .collection("cities")
      .findNearest(
        field: Field("embedding"),
        vectorValue: VectorValue([1.5, 2.345]),
        distanceMeasure: .euclidean
      )
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a9512e6e882ad3f5aa32d9d929b77893bc1f1d1e/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1787-L1794)

##### Kotlin  
Android
    
    
    val results = db.pipeline()
        .collection("cities")
        .findNearest(
            "embedding",
            doubleArrayOf(1.5, 2.345),
            FindNearestStage.DistanceMeasure.EUCLIDEAN
        )
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3222-L3229)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results = db.pipeline()
            .collection("cities")
            .findNearest(
                "embedding",
                new double[] {1.5, 2.345},
                FindNearestStage.DistanceMeasure.EUCLIDEAN
            )
            .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L3515-L3522)

##### Python
    
    
    from google.cloud.firestore_v1.vector import Vector
    from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
    
    results = (
        client.pipeline()
        .collection("cities")
        .find_nearest(
            field="embedding",
            vector_value=Vector([1.5, 2.345]),
            distance_measure=DistanceMeasure.EUCLIDEAN,
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2351-L2363)

##### Java
    
    
    Pipeline.Snapshot results =
        firestore
            .pipeline()
            .collection("cities")
            .findNearest(
                "embedding",
                new double[] {1.5, 2.345},
                FindNearest.DistanceMeasure.EUCLIDEAN,
                new FindNearestOptions())
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L2431-L2441)

##### Go
    
    
    snapshot := client.Pipeline().Collection("cities").
    	FindNearest("embedding", []float64{1.5, 2.345}, firestore.PipelineDistanceMeasureEuclidean).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/edbc7e6338c19c4a6e788ce685473e8cf2f397e4/firestore/pipeline_snippets_general.go#L2039-L2041)

## Behavior

### Distance Measure

The `find_nearest(...)` stage supports the following options for vector distance:

  * `euclidean`: Measures the `euclidean` distance between the vectors. To learn more, see [Euclidean](https://en.wikipedia.org/wiki/Euclidean_distance).
  * `cosine`: Compares vectors based on the angle between them which lets you measure similarity that isn't based on the vectors magnitude. We recommend using `dot_product` with unit normalized vectors instead of COSINE distance, which is mathematically equivalent with better performance. To learn more see [Cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity).
  * `dot_product`: Similar to `cosine` but is affected by the magnitude of the vectors. To learn more, see [Dot product](https://en.wikipedia.org/wiki/Dot_product).



### Choose the distance measure

Depending on whether or not all your vector embeddings are normalized, you can determine which distance measure to use to find the distance measure. A normalized vector embedding has a magnitude (length) of exactly 1.0.

In addition, if you know which distance measure your model was trained with, use that distance measure to compute the distance between your vector embeddings.

**Normalized data**

If you have a dataset where all vector embeddings are normalized, then all three distance measures provide the same semantic search results. In essence, although each distance measure returns a different value, those values sort the same way. When embeddings are normalized, `dot_product` is usually the most computationally efficient, but the difference is negligible in most cases. However, if your application is highly performance sensitive, `dot_product` might help with performance tuning.

**Non-normalized data**

If you have a dataset where vector embeddings aren't normalized, then it's not mathematically correct to use `dot_product` as a distance measure because dot product doesn't measure distance. Depending on how the embeddings were generated and what type of search is preferred, either the `cosine` or `euclidean` distance measure produces search results that are subjectively better than the other distance measures. Experimentation with either `cosine` or `euclidean` might be necessary to determine which is best for your use case.

**Unsure if data is normalized or non-normalized**

If you're unsure whether or not your data is normalized and you want to use `dot_product`, we recommend that you use `cosine` instead. `cosine` is like `dot_product` with normalization built in. Distance measured using `cosine` ranges from `0` to `2`. A result that is close to `0` indicates the vectors are very similar.

### Limit the results

You can limit the number of documents returned by the query by setting the limit field.

### Node.js
    
    
    const results = await db.pipeline()
      .collection("cities")
      .findNearest({
          field: "embedding",
          vectorValue: vector([1.5, 2.345]),
          distanceMeasure: "euclidean",
          limit: 10,
      })
      .execute();
    

### Retrieving the Calculated Vector Distance

You can retrieve the calculated vector distance by assigning a distance_field output property name on the `find_nearest(...)` stage, as shown in the following example:

As an example, for the following collection:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francisco", embedding: vector([1.0, -1.0])});
    await db.collection("cities").doc("TO").set({name: "Toronto", embedding: vector([5.0, -10.0])});
    await db.collection("cities").doc("AT").set({name: "Atlantis", embedding: vector([2.0, -4.0])});
    

Perform a vector search with a requested output distance_field:

### Node.js
    
    
    const results = await db.pipeline()
      .collection("cities")
      .findNearest({
          field: "embedding",
          vectorValue: vector([1.3, 2.345]),
          distanceMeasure: "euclidean",
          distanceField: "computedDistance",
      })
      .execute();
    

Which produces the following documents:
    
    
    {name: "San Francisco", embedding: vector([1.0, -1.0]), computedDistance: 3.3584259705999178},
    {name: "Atlantis", embedding: vector([2.0, -4.0]), computedDistance: 6.383496299051172},
    {name: "Toronto", embedding: vector([5.0, -10.0]), computedDistance: 12.887553103673328}
    

## Limitations

As you work with vector embeddings, note the following limitation:

  * The maximum supported embedding dimension is 2048. To store larger indexes, use [dimensionality reduction](https://en.wikipedia.org/wiki/Dimensionality_reduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
