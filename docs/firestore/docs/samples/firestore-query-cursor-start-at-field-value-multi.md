---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-start-at-field-value-multi/
title: Query a Firestore collection with a cursor start at field (multiple) filter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:48.872420+00:00
---

# Query a Firestore collection with a cursor start at field (multiple) filter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-start-at-field-value-multi/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a Firestore collection with a cursor start at field (multiple) filter Stay organized with collections  Save and categorize content based on your preferences. 

Query a Firestore collection with a cursor start at field (multiple) filter

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Paginate data with query cursors](https://docs.cloud.google.com/firestore/native/docs/query-data/query-cursors)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Query query1 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield");
    Query query2 = db.Collection("cities").OrderBy("Name").OrderBy("State").StartAt("Springfield", "Missouri");

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Will return all Springfields.
    client.Collection("cities").
    	OrderBy("name", firestore.Asc).
    	OrderBy("state", firestore.Asc).
    	StartAt("Springfield")
    
    // Will return Springfields where state comes after Wisconsin.
    client.Collection("cities").
    	OrderBy("name", firestore.Asc).
    	OrderBy("state", firestore.Asc).
    	StartAt("Springfield", "Wisconsin")

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Will return all Springfields
    Query query1 = db.collection("cities").orderBy("name").orderBy("state").startAt("Springfield");
    
    // Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    Query query2 =
        db.collection("cities").orderBy("name").orderBy("state").startAt("Springfield", "Missouri");

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Will return all Springfields
    const startAtNameRes = await db.collection('cities')
      .orderBy('name')
      .orderBy('state')
      .startAt('Springfield')
      .get();
    
    // Will return 'Springfield, Missouri' and 'Springfield, Wisconsin'
    const startAtNameAndStateRes = await db.collection('cities')
      .orderBy('name')
      .orderBy('state')
      .startAt('Springfield', 'Missouri')
      .get();

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Will return all Springfields
    $query1 = $db
        ->collection('samples/php/cities')
        ->orderBy('name')
        ->orderBy('state')
        ->startAt(['Springfield']);
    
    // Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    $query2 = $db
        ->collection('samples/php/cities')
        ->orderBy('name')
        ->orderBy('state')
        ->startAt(['Springfield', 'Missouri']);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    start_at_name = (
        db.collection("cities").order_by("name").start_at({"name": "Springfield"})
    )
    
    start_at_name_and_state = (
        db.collection("cities")
        .order_by("name")
        .order_by("state")
        .start_at({"name": "Springfield", "state": "Missouri"})
    )

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Will return all Springfields
    query1 = firestore.col(collection_path).order("name").order("state").start_at("Springfield")
    
    # Will return "Springfield, Missouri" and "Springfield, Wisconsin"
    query2 = firestore.col(collection_path).order("name").order("state").start_at(["Springfield", "Missouri"])

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
