---
url: https://docs.cloud.google.com/firestore/native/docs/text-search/
title: Use text search \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:15.010561+00:00
---

# Use text search  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/text-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use text search

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use text search features in Firestore to search for specific strings within documents.

## Edition requirements

Text search requires a Firestore Enterprise edition database.

## Before you begin

To perform a text search, you must first [create text indexes](https://docs.cloud.google.com/firestore/native/docs/enterprise-indexing#create-text-index) for the fields you need to search through.

## Run a text search

To perform a text search, use the `documentMatches` expression within the `query` parameter of the `search(...)` stage.

The operation searches only in the fields indexed with a text index. If multiple indexes are available, Firestore selects one index to use for the operation.

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles')
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3518-L3521)

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(query: DocumentMatches("waffles"))
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/db5996f330622c22ee6a4b97bb25b7be56bacda5/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1521-L1523)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage.withQuery(documentMatches("waffles")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3732-L3733)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline().collection("restaurants")
            .search(SearchStage.withQuery(documentMatches("waffles")));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L4116-L4117)

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles')
      })
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2178-L2182)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import DocumentMatches
    
    results = (
        client.pipeline()
        .collection("restaurants")
        .search(DocumentMatches("waffles"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2883-L2890)

##### Java
    
    
    Pipeline.Snapshot results1 =
        firestore.pipeline().collection("restaurants")
            .search(Search.withQuery(documentMatches("waffles")))
            .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3170-L3173)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("restaurants").
    	Search(firestore.WithSearchQuery(firestore.DocumentMatches("waffles"))).
    	Execute(ctx)
    
    [pipeline_snippets_search.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/f7119fc3feaee03d96513265ea64c504e7e6f8b9/firestore/pipeline_snippets_search.go#L28-L31)

### Search for an exact term

To search for an exact term, enclose the term in quotes (`"`):

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('"belgian waffles"')
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3537-L3540)

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(query: DocumentMatches("\"belgian waffles\""))
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/db5996f330622c22ee6a4b97bb25b7be56bacda5/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1539-L1541)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage.withQuery(documentMatches("\"belgian waffles\"")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3750-L3751)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline().collection("restaurants")
            .search(SearchStage.withQuery(documentMatches("\"belgian waffles\"")));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L4133-L4134)

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('"belgian waffles"')
      })
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2186-L2190)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import DocumentMatches
    
    results = (
        client.pipeline()
        .collection("restaurants")
        .search(DocumentMatches('"belgian waffles"'))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2906-L2913)

##### Java
    
    
    Pipeline.Snapshot results2 =
        firestore.pipeline().collection("restaurants")
            .search(Search.withQuery(documentMatches("\"belgian waffles\"")))
            .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3178-L3181)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("restaurants").
    	Search(firestore.WithSearchQuery(firestore.DocumentMatches("\"belgian waffles\""))).
    	Execute(ctx)
    
    [pipeline_snippets_search.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/f7119fc3feaee03d96513265ea64c504e7e6f8b9/firestore/pipeline_snippets_search.go#L45-L48)

### Search for a term combination

To search for combination for terms (logical `AND`), separate the terms with spaces:

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles eggs')
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3556-L3559)

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(query: DocumentMatches("waffles eggs"))
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/db5996f330622c22ee6a4b97bb25b7be56bacda5/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1557-L1559)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage.withQuery(documentMatches("waffles eggs")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3768-L3769)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline().collection("restaurants")
            .search(SearchStage.withQuery(documentMatches("waffles eggs")));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L4150-L4151)

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles eggs')
      })
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2194-L2198)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import DocumentMatches
    
    results = (
        client.pipeline()
        .collection("restaurants")
        .search(DocumentMatches("waffles eggs"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2932-L2939)

##### Java
    
    
    firestore.collection("restaurants").add(new HashMap<String, Object>() {{
      put("name", "Morning Diner");
      put("description", "Start your day with waffles and eggs.");
    }});
    Pipeline.Snapshot results3 =
        firestore.pipeline().collection("restaurants")
            .search(Search.withQuery(documentMatches("waffles eggs")))
            .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3186-L3189)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("restaurants").
    	Search(firestore.WithSearchQuery(firestore.DocumentMatches("waffles eggs"))).
    	Execute(ctx)
    
    [pipeline_snippets_search.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/f7119fc3feaee03d96513265ea64c504e7e6f8b9/firestore/pipeline_snippets_search.go#L62-L65)

### Exclude a term

To exclude a term, prefix the term with a hyphen (`-`):

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('coffee -waffles')
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3575-L3578)

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(query: DocumentMatches("coffee -waffles"))
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/db5996f330622c22ee6a4b97bb25b7be56bacda5/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1575-L1577)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage.withQuery(documentMatches("waffles eggs")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3768-L3769)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline().collection("restaurants")
            .search(SearchStage.withQuery(documentMatches("coffee -waffles")));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L4167-L4168)

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('-waffles')
      })
      .execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2202-L2206)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import DocumentMatches
    
    results = (
        client.pipeline()
        .collection("restaurants")
        .search(DocumentMatches("-waffles"))
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2955-L2962)

##### Java
    
    
    firestore.collection("restaurants").add(new HashMap<String, Object>() {{
      put("name", "City Coffee");
      put("description", "Premium coffee and pastries.");
    }});
    Pipeline.Snapshot results4 =
        firestore.pipeline().collection("restaurants")
            .search(Search.withQuery(documentMatches("-waffles")))
            .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3194-L3197)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("restaurants").
    	Search(firestore.WithSearchQuery(firestore.DocumentMatches("-waffles"))).
    	Execute(ctx)
    
    [pipeline_snippets_search.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/f7119fc3feaee03d96513265ea64c504e7e6f8b9/firestore/pipeline_snippets_search.go#L79-L82)

You can also exclude a phrase, for example, `pizza -"New York"`.

### Sort results

By default, Firestore **sorts results by document creation time** , newest to oldest. You can sort by search score instead, but this requires more computation to calculate and compare the exact score of each document:

To sort results by search score:

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles'),
        sort: score().descending()
      }));

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(
          query: DocumentMatches("waffles"),
          sort: [Score().descending()]
          )
      .execute()

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage
                  .withQuery(documentMatches("waffles"))
                  .withSort(score().descending())
                  )

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: documentMatches('waffles'),
        sort: score().descending()
      })
      .execute();

### Add fields to documents returned by the search stage

You can use `addFields` to add fields to the documents returned by the search stage. Expressions returning values computed by the search stage, like `score()`, can be used within `addFields` in the search stage to write those `values to the output documents.

The following example adds the score field to the documents returned by the search stage:

### Web version 9
    
    
    const result = await execute(db.pipeline().collection('restaurants')
      .search({
        query: 'menu:waffles',
        addFields: [
            score().as('score'),
        ]
      }));
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-next/test.firestore.js#L3594-L3600)

##### iOS
    
    
    let snapshot = try await db.pipeline().collection("restaurants")
      .search(
        query: DocumentMatches("waffles"),
        addFields: [
          Score().as("score")
        ]
      )
      .execute()
    
    [PipelineSnippets.swift](https://github.com/firebase/snippets-ios/blob/db5996f330622c22ee6a4b97bb25b7be56bacda5/firestore/swift/firestore-smoketest/PipelineSnippets.swift#L1593-L1600)

##### Kotlin  
Android
    
    
    val pipeline = db.pipeline().collection("restaurants")
        .search(SearchStage.withQuery(documentMatches("waffles eggs")))
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L3768-L3769)

##### Java  
Android
    
    
    Pipeline pipeline = db.pipeline().collection("restaurants")
            .search(
                    SearchStage.withQuery(documentMatches("menu:waffles"))
                            .withAddFields(score().alias("score")));
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/bb5b419494a9d94466a5422d49f758f8ef5d81fa/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L4184-L4187)

##### Node.js
    
    
    await db.pipeline().collection('restaurants')
      .search({
        query: field('menu').matches('waffles'),
        addFields: [
            score().as('score'),
        ]
      }).execute();
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/3999dead1c222ee0870d5f3e011194fa519e9553/firestore-temp/test.firestore.js#L2210-L2216)

##### Python
    
    
    from google.cloud.firestore_v1.pipeline_expressions import DocumentMatches, Score
    from google.cloud.firestore_v1.pipeline_stages import SearchOptions
    
    results = (
        client.pipeline()
        .collection("restaurants")
        .search(
            SearchOptions(
                query=DocumentMatches("menu:waffles"),
                add_fields=[Score().as_("score")],
            )
        )
        .execute()
    )
    
    [firestore_pipelines.py](https://github.com/firebase/firebase-admin-python/blob/c4ba7c06bb0f7082908f16fee6df5d266483101d/snippets/firestore/firestore_pipelines.py#L2978-L2991)

##### Java
    
    
    Pipeline.Snapshot results5 =
        firestore.pipeline().collection("restaurants")
            .search(Search.withQuery(field("menu").regexMatch("waffles"))
                .withAddFields(score().as("score")))
            .execute().get();
    
    [PipelineSnippets.java](https://github.com/googleapis/java-firestore/blob/8edd723bfd9e683eb3b29c069de8ccc91bc1d847/samples/preview-snippets/src/main/java/com/example/firestore/PipelineSnippets.java#L3202-L3206)

##### Go
    
    
    snapshot := client.Pipeline().
    	Collection("restaurants").
    	Search(
    		firestore.WithSearchQuery(firestore.FieldOf("menu").RegexMatch("waffles")),
    		firestore.WithSearchAddFields(firestore.Score().As("score")),
    	).
    	Execute(ctx)
    
    [pipeline_snippets_search.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/f7119fc3feaee03d96513265ea64c504e7e6f8b9/firestore/pipeline_snippets_search.go#L96-L102)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
