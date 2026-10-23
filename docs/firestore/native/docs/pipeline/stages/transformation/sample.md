---
url: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sample/
title: Sample (Transformation Stage) \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:27.020248+00:00
---

# Sample (Transformation Stage)  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sample (Transformation Stage)

## Description

Returns a non-deterministic sample from the results of the previous stage.

There are two supported modes:

  * `documents`: pick `n` documents randomly.
  * `percent`: pick `n` percent of documents randomly.



## Examples

### Web
    
    
    let results;
    
    // Get a sample of 100 documents in a database
    results = await execute(db.pipeline()
      .database()
      .sample(100)
    );
    
    // Randomly shuffle a list of 3 documents
    results = await execute(db.pipeline()
      .documents([
        doc(db, "cities", "SF"),
        doc(db, "cities", "NY"),
        doc(db, "cities", "DC"),
      ])
      .sample(3)
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2484-L2500)

##### Swift
    
    
    var results: Pipeline.Snapshot
    
    // Get a sample of 100 documents in a database
    results = try await db.pipeline()
      .database()
      .sample(count: 100)
      .execute()
    
    // Randomly shuffle a list of 3 documents
    results = try await db.pipeline()
      .documents([
        db.collection("cities").document("SF"),
        db.collection("cities").document("NY"),
        db.collection("cities").document("DC"),
      ])
      .sample(count: 3)
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L381-L397)

##### Kotlin  
Android
    
    
    var results: Task<Pipeline.Snapshot>
    
    // Get a sample of 100 documents in a database
    results = db.pipeline()
        .database()
        .sample(100)
        .execute()
    
    // Randomly shuffle a list of 3 documents
    results = db.pipeline()
        .documents(
            db.collection("cities").document("SF"),
            db.collection("cities").document("NY"),
            db.collection("cities").document("DC")
        )
        .sample(3)
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1703-L1719)

##### Java  
Android
    
    
    Task<Pipeline.Snapshot> results;
    
    // Get a sample of 100 documents in a database
    results = db.pipeline()
        .database()
        .sample(100)
        .execute();
    
    // Randomly shuffle a list of 3 documents
    results = db.pipeline()
        .documents(
            db.collection("cities").document("SF"),
            db.collection("cities").document("NY"),
            db.collection("cities").document("DC")
        )
        .sample(3)
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1949-L1965)

##### Python
    
    
    # Get a sample of 100 documents in a database
    results = client.pipeline().database().sample(100).execute()
    
    # Randomly shuffle a list of 3 documents
    results = (
        client.pipeline()
        .documents(
            client.collection("cities").document("SF"),
            client.collection("cities").document("NY"),
            client.collection("cities").document("DC"),
        )
        .sample(3)
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L442-L455)

##### Java
    
    
    // Get a sample of 100 documents in a database
    Pipeline.Snapshot results1 = firestore.pipeline().database().sample(100).execute().get();
    
    // Randomly shuffle a list of 3 documents
    Pipeline.Snapshot results2 =
        firestore
            .pipeline()
            .documents(
                firestore.collection("cities").document("SF"),
                firestore.collection("cities").document("NY"),
                firestore.collection("cities").document("DC"))
            .sample(3)
            .execute()
            .get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L462-L475)

##### Go
    
    
    // Get a sample of 100 documents in a database
    results1, err := client.Pipeline().Database().Sample(firestore.WithDocLimit(100)).Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    // Randomly shuffle a list of 3 documents
    results2, err := client.Pipeline().
    	Documents([]*firestore.DocumentRef{
    		client.Collection("cities").Doc("SF"),
    		client.Collection("cities").Doc("NY"),
    		client.Collection("cities").Doc("DC"),
    	}).
    	Sample(firestore.WithDocLimit(3)).
    	Execute(ctx).Results().GetAll()
    if err != nil {
    	fmt.Fprintf(w, "GetAll failed: %v", err)
    	return err
    }
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1001-L1020)

## Modes

### Documents Mode

The `documents` mode picks up to `n` documents randomly from its input, where each document (along with the order of documents) is equally as likely to be chosen. To achieve this, Firestore needs to still scan and process all documents so this can still end up being an expensive operation.

For example, for the following collection:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francsico", state: "California"});
    await db.collection("cities").doc("NYC").set({name: "New York City", state: "New York"});
    await db.collection("cities").doc("CHI").set({name: "Chicago", state: "Illinois"});
    

The sample stage in document mode can be used to retrieve a non-deterministic subset of results from this collection.

### Node.js
    
    
    const sampled = await db.pipeline()
        .collection("/cities")
        .sample(1)
        .execute();
    

In this example, only 1 document at random would be returned at random.
    
    
      { name: "New York City", state: "New York" }
    

If the supplied number is greater than the total number of documents returned, all documents are returned in a random order.

### Node.js
    
    
    const sampled = await db.pipeline()
        .collection("/cities")
        .sample(5)
        .execute();
    

This will result in the following documents:
    
    
      { name: "New York City", state: "New York" }
      { name: "Chicago", state: "Illinois" }
      { name: "San Francisco", state: "California" }
    

### Percent Mode

The `percent` mode attempts to pick `n` percent of all documents from its input. This results in the stage producing approximately `# documents * percent / 100` documents. Just like in `documents` mode, Firestore ensures that each document is equally as likely to be returned. This does require that Firestore needs to scan and process all documents so this can still end up being an expensive operation, even when the result set is small.

Unlike `documents` mode, the order here is not random and instead preserves the pre-existing document order. This percent input must be a double value between `0.0` and `1.0`.

For example, for the following collection:

### Node.js
    
    
    await db.collection("cities").doc("SF").set({name: "San Francsico", state: "California"});
    await db.collection("cities").doc("NYC").set({name: "New York City", state: "New York"});
    await db.collection("cities").doc("CHI").set({name: "Chicago", state: "Illinois"});
    await db.collection("cities").doc("ATL").set({name: "Atlanta", state: "Georgia"});
    

The sample stage in percent mode can be used to retrieve (on average) 50% of the documents from the [`collection(...)`](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/input/collection) stage.

### Node.js
    
    
      const sampled = await db.pipeline()
        .collection("/cities")
        .sample({ percent: 0.5 })
        .execute();
    

This will result in a non-deterministic sample of (on average) 50% of documents from the `cities` collection. The following is one possible output.
    
    
      { name: "New York City", state: "New York" }
      { name: "Chicago", state: "Illinois" }
    

In percent mode, because each document has the same probability of being selected, it is possible for no documents or all documents to be returned.

#### Client examples

### Web
    
    
    // Get a sample of on average 50% of the documents in the database
    const results = await execute(db.pipeline()
      .database()
      .sample({ percentage: 0.5 })
    );
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L2507-L2511)

##### Swift
    
    
    // Get a sample of on average 50% of the documents in the database
    let results = try await db.pipeline()
      .database()
      .sample(percentage: 0.5)
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L405-L409)

##### Kotlin  
Android
    
    
    // Get a sample of on average 50% of the documents in the database
    val results = db.pipeline()
        .database()
        .sample(SampleStage.withPercentage(0.5))
        .execute()
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L1727-L1731)

##### Java  
Android
    
    
    // Get a sample of on average 50% of the documents in the database
    Task<Pipeline.Snapshot> results = db.pipeline()
        .database()
        .sample(SampleStage.withPercentage(0.5))
        .execute();
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1973-L1977)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_stages import SampleOptions
    
    # Get a sample of on average 50% of the documents in the database
    results = (
        client.pipeline().database().sample(SampleOptions.percentage(0.5)).execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L463-L468)

##### Java
    
    
    // Get a sample of on average 50% of the documents in the database
    Pipeline.Snapshot results =
        firestore.pipeline().database().sample(Sample.withPercentage(0.5)).execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L483-L485)

##### Go
    
    
    // Get a sample of on average 50% of the documents in the database
    snapshot := client.Pipeline().
    	Database().
    	Sample(firestore.WithPercentage(0.5)).
    	Execute(ctx)
    
    [pipeline_snippets_general.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/5a88b95e85a07cb132bd437f5940aea3afe8ab54/firestore/pipeline_snippets_general.go#L1030-L1034)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
