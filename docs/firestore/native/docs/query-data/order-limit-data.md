---
url: https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data/
title: Order and limit data \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:24:54.290665+00:00
---

# Order and limit data  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/query-data/order-limit-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Order and limit data

**Tip:** This page applies to the Core operations interface. To order and limit data in the Pipeline operations interface for Enterprise edition, see [Pipeline operation `limit` stage](https://docs.cloud.google.com/firestore/native/docs/pipeline/stages/transformation/limit). 

Firestore provides powerful query functionality for specifying which documents you want to retrieve from a collection. These queries can also be used with either `get()` or `addSnapshotListener()`, as described in [Get Data](https://docs.cloud.google.com/firestore/native/docs/query-data/get-data).

**Note:** While the code samples cover multiple languages, the text explaining the samples refers to the Web method names.

## Order and limit data

By default, a query retrieves all documents that satisfy the query in ascending order by document ID. You can specify the sort order for your data using `orderBy()`, and you can limit the number of documents retrieved using `limit()`. If you specify a `limit()`, the value must be greater than or equal to zero.

**Note:** An `orderBy()` clause also filters for existence of the given field. The result set will not include documents that do not contain the given field.

For example, you could query for the first 3 cities alphabetically with:

### Web version 9
    
    
    import { query, orderBy, limit } from "firebase/firestore";  
    
    const q = query(citiesRef, orderBy("name"), limit(3));
    
    [order_and_limit.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/order_and_limit.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.orderBy("name").limit(3);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L929-L929)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef.order(by: "name").limit(to: 3)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1021-L1021)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[citiesRef queryOrderedByField:@"name"] queryLimitedTo:3];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L933-L933)

##### Kotlin  
Android
    
    
    citiesRef.orderBy("name").limit(3)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L927-L927)

##### Java  
Android
    
    
    citiesRef.orderBy("name").limit(3);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1120-L1120)

### Dart
    
    
    final citiesRef = db.collection("cities");
    citiesRef.orderBy("name").limit(3);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L957-L958)

##### Java
    
    
    Query query = cities.orderBy("name").limit(3);
    Query query = cities.orderBy("name").limitToLast(3);
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L264-L264)

##### Python
    
    
    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = query.get()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-client/snippets.py#L578-L580)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name").limit_to_last(2)
    results = await query.get()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-async-client/snippets.py#L563-L565)

##### C++
    
    
    cities_ref.OrderBy("name").Limit(3);
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1063-L1063)

##### Node.js
    
    
    const firstThreeRes = await citiesRef.orderBy('name').limit(3).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L688-L688)

##### Go
    
    
    query := cities.OrderBy("name", firestore.Asc).Limit(3)
    query := cities.OrderBy("name", firestore.Asc).LimitToLast(3)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/query.go#L155-L155)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $query = $citiesRef->orderBy('name')->limit(3);

##### Unity
    
    
    Query query = citiesRef.OrderBy("Name").Limit(3);

##### C#
    
    
    Query query = citiesRef.OrderBy("Name").Limit(3);
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/55b6f7afd6367b7564f419b3e0d62a3e467522e3/firestore/api/OrderLimitData/Program.cs#L44-L44)

##### Ruby
    
    
    query = cities_ref.order("name").limit(3)
    
    [order_limit_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/96af99eb31443fe6587644b8cd7074947b001a5a/google-cloud-firestore/samples/order_limit_data.rb#L25-L25)

You could also sort in descending order to get the _last_ 3 cities:

### Web version 9
    
    
    import { query, orderBy, limit } from "firebase/firestore";  
    
    const q = query(citiesRef, orderBy("name", "desc"), limit(3));
    
    [order_and_limit_desc.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/order_and_limit_desc.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.orderBy("name", "desc").limit(3);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L936-L936)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef.order(by: "name", descending: true).limit(to: 3)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1029-L1029)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[citiesRef queryOrderedByField:@"name" descending:YES] queryLimitedTo:3];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L940-L940)

##### Kotlin  
Android
    
    
    citiesRef.orderBy("name", Query.Direction.DESCENDING).limit(3)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L931-L931)

##### Java  
Android
    
    
    citiesRef.orderBy("name", Direction.DESCENDING).limit(3);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1124-L1124)

### Dart
    
    
    final citiesRef = db.collection("cities");
    citiesRef.orderBy("name", descending: true).limit(3);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L964-L965)

##### Java
    
    
    Query query = cities.orderBy("name", Direction.DESCENDING).limit(3);
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L290-L290)

##### Python
    
    
    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-client/snippets.py#L539-L541)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    query = cities_ref.order_by("name", direction=firestore.Query.DESCENDING).limit(3)
    results = query.stream()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-async-client/snippets.py#L529-L531)

##### C++
    
    
    cities_ref.OrderBy("name", Query::Direction::kDescending).Limit(3);
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1068-L1068)

##### Node.js
    
    
    const lastThreeRes = await citiesRef.orderBy('name', 'desc').limit(3).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L692-L692)

##### Go
    
    
    query := cities.OrderBy("name", firestore.Desc).Limit(3)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/query.go#L164-L164)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $query = $citiesRef->orderBy('name', 'DESC')->limit(3);

##### Unity
    
    
    Query query = citiesRef.OrderByDescending("Name").Limit(3);

##### C#
    
    
    Query query = citiesRef.OrderByDescending("Name").Limit(3);
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/55b6f7afd6367b7564f419b3e0d62a3e467522e3/firestore/api/OrderLimitData/Program.cs#L58-L58)

##### Ruby
    
    
    query = cities_ref.order("name", "desc").limit(3)
    
    [order_limit_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/96af99eb31443fe6587644b8cd7074947b001a5a/google-cloud-firestore/samples/order_limit_data.rb#L40-L40)

You can also order by multiple fields. For example, if you wanted to order by state, and within each state order by population in descending order:

### Web version 9
    
    
    import { query, orderBy } from "firebase/firestore";  
    
    const q = query(citiesRef, orderBy("state"), orderBy("population", "desc"));
    
    [order_multiple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/order_multiple.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.orderBy("state").orderBy("population", "desc");
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L943-L943)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef
      .order(by: "state")
      .order(by: "population", descending: true)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1037-L1039)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[citiesRef queryOrderedByField:@"state"] queryOrderedByField:@"population" descending:YES];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L947-L947)

##### Kotlin  
Android
    
    
    citiesRef.orderBy("state").orderBy("population", Query.Direction.DESCENDING)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L935-L935)

##### Java  
Android
    
    
    citiesRef.orderBy("state").orderBy("population", Direction.DESCENDING);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1128-L1128)

### Dart
    
    
    final citiesRef = db.collection("cities");
    citiesRef.orderBy("state").orderBy("population", descending: true);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L971-L972)

##### Java
    
    
    Query query = cities.orderBy("state").orderBy("population", Direction.DESCENDING);
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L277-L277)

##### Python
    
    
    cities_ref = db.collection("cities")
    ordered_city_ref = cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-client/snippets.py#L552-L555)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    cities_ref.order_by("state").order_by(
        "population", direction=firestore.Query.DESCENDING
    )
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-async-client/snippets.py#L539-L542)

##### C++
    
    
    cities_ref.OrderBy("state").OrderBy("name", Query::Direction::kDescending);
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1074-L1074)

##### Node.js
    
    
    const byStateByPopRes = await citiesRef.orderBy('state').orderBy('population', 'desc').get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L696-L696)

##### Go
    
    
    query := client.Collection("cities").OrderBy("state", firestore.Asc).OrderBy("population", firestore.Desc)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/query.go#L172-L172)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $query = $citiesRef->orderBy('state')->orderBy('population', 'DESC');

##### Unity
    
    
    Query query = citiesRef.OrderBy("State").OrderByDescending("Population");

##### C#
    
    
    Query query = citiesRef.OrderBy("State").OrderByDescending("Population");
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/55b6f7afd6367b7564f419b3e0d62a3e467522e3/firestore/api/OrderLimitData/Program.cs#L72-L72)

##### Ruby
    
    
    query = cities_ref.order("state").order("population", "desc")
    
    [order_limit_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/96af99eb31443fe6587644b8cd7074947b001a5a/google-cloud-firestore/samples/order_limit_data.rb#L55-L55)

You can combine `where()` filters with `orderBy()` and `limit()`. In the following example, the queries define a population threshold, sort by population in ascending order, and return only the first few results that exceed the threshold:

### Web version 9
    
    
    import { query, where, orderBy, limit } from "firebase/firestore";  
    
    const q = query(citiesRef, where("population", ">", 100000), orderBy("population"), limit(2));
    
    [filter_and_order.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/firestore-next/test-firestore/filter_and_order.js#L8-L10)

### Web version 8

[Learn more](https://firebase.google.com/docs/web/learn-more#modular-version) about the tree-shakeable modular Web API and its advantages over the namespaced API.
    
    
    citiesRef.where("population", ">", 100000).orderBy("population").limit(2);
    
    [test.firestore.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/firestore/test.firestore.js#L950-L950)

##### Swift

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    citiesRef
      .whereField("population", isGreaterThan: 100000)
      .order(by: "population")
      .limit(to: 2)
    
    [ViewController.swift](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/swift/firestore-smoketest/ViewController.swift#L1047-L1050)

##### Objective-C

**Note:** This product is not available on watchOS and App Clip targets. 
    
    
    [[[citiesRef queryWhereField:@"population" isGreaterThan:@100000]
        queryOrderedByField:@"population"]
        queryLimitedTo:2];
    
    [ViewController.m](https://github.com/firebase/snippets-ios/blob/a542286ec4de7ab7e90e838485eaa2f3cd92d153/firestore/objc/firestore-smoketest-objc/ViewController.m#L954-L956)

##### Kotlin  
Android
    
    
    citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2)
    
    [DocSnippets.kt](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/kotlin/DocSnippets.kt#L939-L939)

##### Java  
Android
    
    
    citiesRef.whereGreaterThan("population", 100000).orderBy("population").limit(2);
    
    [DocSnippets.java](https://github.com/firebase/snippets-android/blob/12ec906c9ccba5acf8d47009fd4f00370b186b9b/firestore/app/src/main/java/com/google/example/firestore/DocSnippets.java#L1132-L1132)

### Dart
    
    
    final citiesRef = db.collection("cities");
    citiesRef
        .where("population", isGreaterThan: 100000)
        .orderBy("population")
        .limit(2);
    
    [firestore.dart](https://github.com/firebase/snippets-flutter/blob/f674af111fe63779c39e79699f7d269231f77563/packages/firebase_snippets_app/lib/snippets/firestore.dart#L978-L982)

##### Java
    
    
    Query query = cities.whereGreaterThan("population", 2500000L).orderBy("population").limit(2);
    
    [QueryDataSnippets.java](https://github.com/googleapis/java-firestore/blob/dd16eb077d99ea3c7ddb213b23537ae700c8ea6c/samples/snippets/src/main/java/com/example/firestore/snippets/QueryDataSnippets.java#L303-L303)

##### Python
    
    
    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-client/snippets.py#L563-L569)

##### Python  
(Async)
    
    
    cities_ref = db.collection("cities")
    query = (
        cities_ref.where(filter=FieldFilter("population", ">", 2500000))
        .order_by("population")
        .limit(2)
    )
    results = query.stream()
    
    [snippets.py](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/08e010a5852a3328fe8c1904020e1d8adb48fe85/firestore/cloud-async-client/snippets.py#L549-L555)

##### C++
    
    
    cities_ref.WhereGreaterThan("population", FieldValue::Integer(100000))
        .OrderBy("population")
        .Limit(2);
    
    [snippets.cpp](https://github.com/firebase/snippets-cpp/blob/778b6bcc8e8e8fcabb1c2e3a8d11ab51a26aa77b/firestore/android/FirestoreSnippetsCpp/app/src/main/cpp/snippets.cpp#L1082-L1084)

##### Node.js
    
    
    const biggestRes = await citiesRef.where('population', '>', 2500000)
      .orderBy('population').limit(2).get();
    
    [index.js](https://github.com/firebase/snippets-node/blob/7cb8d0ffc824d22d8d586425659d5860f26cbb28/firestore/main/index.js#L700-L701)

##### Go
    
    
    query := cities.Where("population", ">", 2500000).OrderBy("population", firestore.Desc).Limit(2)
    
    [query.go](https://github.com/GoogleCloudPlatform/golang-samples/blob/d82de36e538a4cb88a7524e135753522415591d6/firestore/query.go#L180-L180)

##### PHP

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $query = $citiesRef
        ->where('population', '>', 2500000)
        ->orderBy('population')
        ->limit(2);

##### Unity
    
    
    Query query = citiesRef
        .WhereGreaterThan("Population", 2500000)
        .OrderBy("Population")
        .Limit(2);

##### C#
    
    
    Query query = citiesRef
        .WhereGreaterThan("Population", 2500000)
        .OrderBy("Population")
        .Limit(2);
    
    [Program.cs](https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/55b6f7afd6367b7564f419b3e0d62a3e467522e3/firestore/api/OrderLimitData/Program.cs#L86-L89)

##### Ruby
    
    
    query = cities_ref.where("population", ">", 2_500_000).order("population").limit(2)
    
    [order_limit_data.rb](https://github.com/googleapis/google-cloud-ruby/blob/96af99eb31443fe6587644b8cd7074947b001a5a/google-cloud-firestore/samples/order_limit_data.rb#L70-L70)

However, if you have a filter with a range comparison (`<`, `<=`, `>`, `>=`), your first ordering must be on the same field, see the list of `orderBy()` limitations below.

## Limitations

Note the following restriction for `orderBy()` clauses:

  * An `orderBy()` clause also filters for existence of the given fields. The result set will not include documents that do not contain the given fields. 



## `orderBy` and existence

When you order a query by a given field, the query can return only the documents where the order-by field exists.

For example, the following query would not return any documents where the `population` field is not set, even if they otherwise meet the query filters.

##### Java
    
    
    db.collection("cities").whereEqualTo("country", “USA”).orderBy(“population”);

A related effect applies to inequalities. A query with an inequality filter on a field also implies ordering by that field. The following query does not return documents without a `population` field even if `country = USA` in that document . As a workaround, you can execute separate queries for each ordering or you can assign a value for all fields that you order by.

##### Java
    
    
    db.collection(“cities”).where(or(“country”, USA”), greaterThan(“population”, 250000));

The query above includes an implied order-by on the inequality and is equivalent to the following:

##### Java
    
    
    db.collection(“cities”).where(or(“country”, USA”), greaterThan(“population”, 250000)).orderBy(“population”);

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
