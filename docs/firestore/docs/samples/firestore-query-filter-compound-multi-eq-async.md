---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-compound-multi-eq-async/
title: Query a Firestore collection with multiple eq filters (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:31.375830+00:00
---

# Query a Firestore collection with multiple eq filters (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-filter-compound-multi-eq-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Query a Firestore collection with multiple eq filters (async) Stay organized with collections  Save and categorize content based on your preferences. 

Query a Firestore collection with multiple eq filters (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = db.collection("cities")
    
    denver_query = cities_ref.where(filter=FieldFilter("state", "==", "CO")).where(
        filter=FieldFilter("name", "==", "Denver")
    )
    large_us_cities_query = cities_ref.where(
        filter=FieldFilter("state", "==", "CA")
    ).where(filter=FieldFilter("population", ">", 1000000))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
