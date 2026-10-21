---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-range-valid/
title: Use two ranges for a Firestore query \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:00.986755+00:00
---

# Use two ranges for a Firestore query  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-range-valid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Use two ranges for a Firestore query Stay organized with collections  Save and categorize content based on your preferences. 

Use two ranges for a Firestore query

## Code sample

### C#

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    CollectionReference citiesRef = db.Collection("cities");
    Query rangeQuery = citiesRef
        .WhereGreaterThanOrEqualTo("State", "CA")
        .WhereLessThanOrEqualTo("State", "IN");

### Go

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    stateQuery := cities.Where("state", ">=", "CA").Where("state", "<", "IN")
    populationQuery := cities.Where("state", "==", "CA").Where("population", ">", 1000000)

### Java

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    Query validQuery1 =
        cities.whereGreaterThanOrEqualTo("state", "CA").whereLessThanOrEqualTo("state", "IN");
    Query validQuery2 = cities.whereEqualTo("state", "CA").whereGreaterThan("population", 1000000);

### Node.js

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    citiesRef.where('state', '>=', 'CA').where('state', '<=', 'IN');
    citiesRef.where('state', '==', 'CA').where('population', '>', 1000000);

### PHP

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    $rangeQuery = $citiesRef
        ->where('state', '>=', 'CA')
        ->where('state', '<=', 'IN');

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = db.collection("cities")
    cities_ref.where(filter=FieldFilter("state", ">=", "CA")).where(
        filter=FieldFilter("state", "<=", "IN")
    )

### Ruby

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    range_query = cities_ref.where("state", ">=", "CA").where("state", "<=", "IN")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
