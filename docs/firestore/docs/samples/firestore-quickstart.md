---
url: https://docs.cloud.google.com/firestore/docs/samples/firestore-quickstart/
title: Getting started with Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:47.161482+00:00
---

# Getting started with Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/samples/firestore-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Samples ](https://docs.cloud.google.com/firestore/docs/samples)



#  Getting started with Firestore Stay organized with collections  Save and categorize content based on your preferences. 

Getting started with Firestore

## Code sample

### Kotlin
    
    
    // Create the client.
    val db = FirestoreOptions.newBuilder()
        .build()
        .service
    
    // Fetch the document reference and data object.
    val docRef = db.collection(collectionName).document(documentName)
    val data = docRef
        .get() // future
        .get() // snapshot
        .data ?: error("Document $collectionName:$documentName not found") // MutableMap
    
    // Print the retrieved data.
    data.forEach { (key, value) -> println("$key: $value") }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=firestore). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
