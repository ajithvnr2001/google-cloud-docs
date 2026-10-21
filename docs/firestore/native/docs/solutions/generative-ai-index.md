---
url: https://docs.cloud.google.com/firestore/native/docs/solutions/generative-ai-index/
title: Get started with generative AI \u00a0|\u00a0 Firestore in Native mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:58:44.948184+00:00
---

# Get started with generative AI  |  Firestore in Native mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/native/docs/solutions/generative-ai-index/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Native mode ](https://docs.cloud.google.com/firestore/native/docs)
  * [ Guides ](https://docs.cloud.google.com/firestore/native/docs/create-database-server-client-library)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Get started with generative AI 

This page helps you get started with implementing generative AI features in your app. It describes the features and integrations for Firestore that involve generative AI.

## Quickstart for vector search with Firestore

Creating innovative AI-powered solutions for use cases such as product recommendations and chatbots often requires vector similarity search, or vector search for short. You can perform vector search on Firestore data without the hassle of copying data to another vector search solution, maintaining operational simplicity and efficiency.

The core workflow for vector search in Firestore consists of 4 steps.

[Understand vector search fully in our blog post](https://cloud.google.com/blog/products/databases/get-started-with-firestore-vector-similarity-search)

### looks_oneGenerate vector embeddings

The first step in utilizing vector search is to generate vector embeddings. Embeddings are representations of different kinds of data like text, images, and video that capture semantic or syntactic similarities between the entities they represent. Embeddings can be calculated using a service, such as the Vertex AI text-embeddings API. 

### looks_twoStore embeddings in Firestore

Once the embeddings are generated you can store them in Firestore using one of the supported SDKs. Here is what that operation looks like in the NodeJS SDK:
    
    
    const db = new Firestore();
    let collectionRef = db.collection("beans");
    await collectionRef.add({
      name: "Kahawa coffee beans",
      type: "arabica",
      description: "Information about the Kahawa coffee beans.",
      embedding_field: FieldValue.vector([0.1, 0.3, ..., 0.2]), // a vector with 768 dimensions
    });
    

### looks_3Create a vector index

The next step is to create a Firestore KNN vector index where the vector embeddings are stored. During the preview release, you will need to create the index using the `gcloud` command line tool.

### looks_4Perform the vector search

Once you have added all the vector embeddings and created the vector index, you are ready to run the search. You will then utilize the `find_nearest` call on a collection reference to pass the query vector embedding with which to compare the stored embeddings and to specify the distance function you want to utilize.

Once again, explore the workflow and more use cases in our [blog post](https://cloud.google.com/blog/products/databases/get-started-with-firestore-vector-similarity-search).

## Solution: vector search

**Summary:** Store and query vector embeddings.

**Use case:** This feature is used by the other tools and features.

[See the guide for vector search](https://cloud.google.com/firestore/docs/vector-search)

## Solution: LangChain integrations

**Summary:** Use Firestore as a vector store, document loader, or chat message history source for LangChain.

**Use case:** Build generative AI applications or retrieval-augmented generation (RAG) workflows.

[See the guide for LangChain](https://cloud.google.com/firestore/docs/langchain)

## Solution: Genkit

**Summary:** Genkit is an open source framework that helps you build, deploy, and monitor production-ready AI-powered apps.

**Use case:** Use Genkit and Firestore to create apps that generate custom content, use semantic search, handle unstructured inputs, answer questions with your business data, and much more!

[See the Genkit documentation](https://genkit.dev)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
