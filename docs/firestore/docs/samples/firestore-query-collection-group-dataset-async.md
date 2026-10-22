---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset-async/
title: Create a collection of Firestore documents (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:09.251331+00:00
---

# Create a collection of Firestore documents (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-query-collection-group-dataset-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Create a collection of Firestore documents (async) Stay organized with collections  Save and categorize content based on your preferences. 

Create a collection of Firestore documents (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Query and filter data](https://docs.cloud.google.com/firestore/native/docs/query-data/queries)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    cities = db.collection("cities")
    
    sf_landmarks = cities.document("SF").collection("landmarks")
    await sf_landmarks.document().set({"name": "Golden Gate Bridge", "type": "bridge"})
    await sf_landmarks.document().set({"name": "Legion of Honor", "type": "museum"})
    la_landmarks = cities.document("LA").collection("landmarks")
    await la_landmarks.document().set({"name": "Griffith Park", "type": "park"})
    await la_landmarks.document().set({"name": "The Getty", "type": "museum"})
    dc_landmarks = cities.document("DC").collection("landmarks")
    await dc_landmarks.document().set({"name": "Lincoln Memorial", "type": "memorial"})
    await dc_landmarks.document().set(
        {"name": "National Air and Space Museum", "type": "museum"}
    )
    tok_landmarks = cities.document("TOK").collection("landmarks")
    await tok_landmarks.document().set({"name": "Ueno Park", "type": "park"})
    await tok_landmarks.document().set(
        {"name": "National Museum of Nature and Science", "type": "museum"}
    )
    bj_landmarks = cities.document("BJ").collection("landmarks")
    await bj_landmarks.document().set({"name": "Jingshan Park", "type": "park"})
    await bj_landmarks.document().set(
        {"name": "Beijing Ancient Observatory", "type": "museum"}
    )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
