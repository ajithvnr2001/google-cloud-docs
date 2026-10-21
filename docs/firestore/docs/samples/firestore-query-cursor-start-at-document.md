---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-start-at-document/
title: Query a Firestore collection with a cursor start at document filter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:33.701393+00:00
---

# Query a Firestore collection with a cursor start at document filter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-start-at-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a Firestore collection with a cursor start at document filter Stay organized with collections  Save and categorize content based on your preferences. 

Query a Firestore collection with a cursor start at document filter

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Paginate data with query cursors](https://docs.cloud.google.com/firestore/native/docs/query-data/query-cursors)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference citiesRef = db.Collection("cities");
    DocumentReference docRef = citiesRef.Document("SF");
    DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
    Query query = citiesRef.OrderBy("Population").StartAt(snapshot);

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities := client.Collection("cities")
    dsnap, err := cities.Doc("SF").Get(ctx)
    if err != nil {
    	fmt.Println(err)
    }
    query := cities.OrderBy("population", firestore.Asc).StartAt(dsnap.Data()["population"]).Documents(ctx)

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Fetch the snapshot with an API call, waiting for a maximum of 30 seconds for a result.
    ApiFuture<DocumentSnapshot> future = db.collection("cities").document("SF").get();
    DocumentSnapshot snapshot = future.get(30, TimeUnit.SECONDS);
    
    // Construct the query
    Query query = db.collection("cities").orderBy("population").startAt(snapshot);

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const docRef = db.collection('cities').doc('SF');
    const snapshot = await docRef.get();
    const startAtSnapshot = db.collection('cities')
      .orderBy('population')
      .startAt(snapshot);
    
    await startAtSnapshot.limit(10).get();

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $citiesRef = $db->collection('samples/php/cities');
    $docRef = $citiesRef->document('SF');
    $snapshot = $docRef->snapshot();
    
    $query = $citiesRef
        ->orderBy('population')
        ->startAt($snapshot);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    doc_ref = db.collection("cities").document("SF")
    
    snapshot = doc_ref.get()
    start_at_snapshot = (
        db.collection("cities").order_by("population").start_at(snapshot)
    )

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    doc_ref = firestore.doc "#{collection_path}/SF"
    snapshot = doc_ref.get
    query = cities_ref.order("population").start_at(snapshot)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
