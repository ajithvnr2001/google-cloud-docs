---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-transaction-document-update-async/
title: Updating a Firestore document in a transaction (async) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:59.413387+00:00
---

# Updating a Firestore document in a transaction (async)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-transaction-document-update-async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Updating a Firestore document in a transaction (async) Stay organized with collections  Save and categorize content based on your preferences. 

Updating a Firestore document in a transaction (async).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transactions and batched writes](https://docs.cloud.google.com/firestore/native/docs/manage-data/transactions)



## Code sample

### Python

To authenticate to Firestore, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    transaction = db.transaction()
    city_ref = db.collection("cities").document("SF")
    
    @firestore.async_transactional
    async def update_in_transaction(transaction, city_ref):
        snapshot = await city_ref.get(transaction=transaction)
        transaction.update(city_ref, {"population": snapshot.get("population") + 1})
    
    await update_in_transaction(transaction, city_ref)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
