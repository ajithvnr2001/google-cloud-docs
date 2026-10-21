---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/
title: Query a Firestore collection with an array_contains_any filter \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:35.418055+00:00
---

# Query a Firestore collection with an array_contains_any filter  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-array-contains-any/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a Firestore collection with an array_contains_any filter Stay organized with collections  Save and categorize content based on your preferences. 

Query a Firestore collection with an array_contains_any filter

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query query = citiesRef.WhereArrayContainsAny("Regions", new[] { "west_coast", "east_coast" });

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities := client.Collection("cities")
    query := cities.Where("regions", "array-contains-any", []string{"west_coast", "east_coast"}).Documents(ctx)

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference citiesRef = db.collection("cities");
    
    Query query =
        citiesRef.whereArrayContainsAny("regions", Arrays.asList("west_coast", "east_coast"));

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const coastalCities = await citiesRef.where('regions', 'array-contains-any',
        ['west_coast', 'east_coast']).get();

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $containsQuery = $citiesRef->where('regions', 'array-contains-any', ['west_coast', 'east_coast']);

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = db.collection("cities")
    
    query = cities_ref.where(
        filter=FieldFilter(
            "regions", "array_contains_any", ["west_coast", "east_coast"]
        )
    )
    return query

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = firestore.col collection_path
    costal_cities = cities_ref.where "regions", "array-contains-any", ["west_coast", "east_coast"]

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
