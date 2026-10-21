---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-pagination-async/
title: Use start cursors and limits to paginate Firestore collections (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:25:33.778847+00:00
---

# Use start cursors and limits to paginate Firestore collections (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-cursor-pagination-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Use start cursors and limits to paginate Firestore collections (async) Stay organized with collections  Save and categorize content based on your preferences. 

Use start cursors and limits to paginate Firestore collections (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Paginate data with query cursors](https://docs.cloud.google.com/firestore/native/docs/query-data/query-cursors)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities_ref = db.collection("cities")
    first_query = cities_ref.order_by("population").limit(3)
    
    # Get the last document from the results
    docs = [d async for d in first_query.stream()]
    last_doc = list(docs)[-1]
    
    # Construct a new query starting at this document
    # Note: this will not have the desired effect if
    # multiple cities have the exact same population value
    last_pop = last_doc.to_dict()["population"]
    
    next_query = (
        cities_ref.order_by("population").start_after({"population": last_pop}).limit(3)
    )
    # Use the query for pagination
    # ...

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
