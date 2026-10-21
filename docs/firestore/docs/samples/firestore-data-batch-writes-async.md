---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-batch-writes-async/
title: Performs a batch update on a Firestore document (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:07.265132+00:00
---

# Performs a batch update on a Firestore document (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-data-batch-writes-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Performs a batch update on a Firestore document (async) Stay organized with collections  Save and categorize content based on your preferences. 

Performs a batch update on a Firestore document (async). 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transactions and batched writes](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    batch = db.batch()
    
    # Set the data for NYC
    nyc_ref = db.collection("cities").document("NYC")
    batch.set(nyc_ref, {"name": "New York City"})
    
    # Update the population for SF
    sf_ref = db.collection("cities").document("SF")
    batch.update(sf_ref, {"population": 1000000})
    
    # Delete DEN
    den_ref = db.collection("cities").document("DEN")
    batch.delete(den_ref)
    
    # Commit the batch
    await batch.commit()

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
