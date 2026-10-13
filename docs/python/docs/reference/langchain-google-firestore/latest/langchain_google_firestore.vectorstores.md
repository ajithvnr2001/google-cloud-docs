---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/latest/langchain_google_firestore.vectorstores
title: Module vectorstores (0.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:12.228000+00:00
---

# Module vectorstores (0.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/latest/langchain_google_firestore.vectorstores

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module vectorstores (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.5.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/latest/langchain_google_firestore.vectorstores)
  * [ 0.4.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/0.4.0/langchain_google_firestore.vectorstores)
  * [ 0.3.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/0.3.0/langchain_google_firestore.vectorstores)
  * [ 0.2.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/0.2.1/langchain_google_firestore.vectorstores)



API documentation for `vectorstores` module.

## Classes 

### [FirestoreVectorStore](https://docs.cloud.google.com/python/docs/reference/langchain-google-firestore/latest/langchain_google_firestore.vectorstores.FirestoreVectorStore)
    
    
    FirestoreVectorStore(
        collection: google.cloud.firestore_v1.collection.CollectionReference | str,
        embedding_service: langchain_core.embeddings.embeddings.Embeddings,
        client: typing.Optional[google.cloud.firestore_v1.client.Client] = None,
        content_field: str = "content",
        metadata_field: str = "metadata",
        embedding_field: str = "embedding",
        distance_strategy: typing.Optional[
            google.cloud.firestore_v1.base_vector_query.DistanceMeasure
        ] = DistanceMeasure.COSINE,
        filters: typing.Optional[google.cloud.firestore_v1.base_query.BaseFilter] = None,
    )

Interface for vector store.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
