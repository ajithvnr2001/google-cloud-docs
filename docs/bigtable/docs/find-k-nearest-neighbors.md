---
url: https://docs.cloud.google.com/bigtable/docs/find-k-nearest-neighbors/
title: Perform similarity vector search in Bigtable by finding the K-nearest neighbors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:53.306298+00:00
---

# Perform similarity vector search in Bigtable by finding the K-nearest neighbors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/find-k-nearest-neighbors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Perform similarity vector search in Bigtable by finding the K-nearest neighbors

Similarity vector search can help you identify similar concepts and contextual meaning in your Bigtable data, which means it can provide more relevant results when filtering for data stored within a specified key range. Example use cases include the following:

  * Semantic matching of messages for a particular user in inbox search.
  * Anomaly detection within a range of sensors.
  * Retrieving the most relevant documents within a set of known keys for retrieval augmented generation (RAG).
  * Personalization of search results to enhance a user's search experience by retrieving and ranking results based on their historical prompts and preferences that Bigtable stores.
  * Retrieval of similar conversation threads to find and display past conversations that are contextually similar to a user's current chat for a more personalized experience.
  * Prompt deduplication to identify identical or semantically similar prompts submitted by the same user and avoid redundant AI processing.

**Note:** This page describes how to perform similarity vector search in Bigtable by using the cosine distance and Euclidean distance vector functions in [GoogleSQL for Bigtable](https://docs.cloud.google.com/bigtable/docs/googlesql-overview) to find K-nearest neighbors. This approach requires that you set up the required Bigtable components manually. We recommend that you try the [Bigtable vector store for LangChain](https://docs.cloud.google.com/bigtable/docs/langchain#vector-store) instead. The `BigtableVectorStore` class provides readymade methods for running vector K-nearest neighbors searches, enriched with metadata filtering features. 

Before you read this page, it's important that you understand the following concepts:

  * [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance): measures the shortest distance between two vectors.
  * [Cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance): measures the cosine of the angle between two vectors.
  * [K-nearest neighbors (KNN)](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm): a supervised machine learning algorithm used to solve classification or regression problems.



Bigtable supports the `COSINE_DISTANCE()` and `EUCLIDEAN_DISTANCE()` functions, which operate on vector embeddings, letting you find the KNN of the input embedding.

You can use the Gemini Enterprise Agent Platform text embeddings APIs to generate and store your Bigtable data as vector embeddings. You can then provide these vector embeddings as an input parameter in your query to find the nearest vectors in N-dimensional space to search for semantically similar or related items.

Both distance functions take the arguments `vector1` and `vector2`, which are of the type `array<>` and must consist of the same dimensions and have the same length. For more details about these functions, see the following:

  * [`COSINE_DISTANCE()`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#cosine_distance)
  * [`EUCLIDEAN_DISTANCE()`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#euclidean_distance)



The code on this page demonstrate how to create embeddings, store them in Bigtable, and then perform a KNN search.

The example on this page uses `EUCLIDEAN_DISTANCE()` and the Bigtable client library for Python. However, you can also use `COSINE_DISTANCE()` and any client library that supports GoogleSQL for Bigtable, such as the [ Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview).

## Before you begin

Complete the following before you try the code samples.

### Required roles

To get the permissions that you need to read and write to Bigtable, ask your administrator to grant you the following IAM role:

  * Bigtable User ([`roles/bigtable.user`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.user)) on the Bigtable instance that you want to send requests to



### Set up your environment

  1. Download and install the Bigtable client library for Python. To use GoogleSQL for Bigtable functions, you must use `python-bigtable` version 2.26.0 or later. Instructions, including how to set up authentication, are at [Python hello world](https://docs.cloud.google.com/bigtable/docs/samples-python-hello).

  2. If you don't have a Bigtable instance, follow the steps at [Create an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance).

  3. Identify your resource IDs. When you run the code, replace the following placeholders with the IDs of your Google Cloud project, Bigtable instance, and table:

     * `PROJECT_ID`
     * `INSTANCE_ID`
     * `TABLE_ID`



## Create a table to store the text, embeddings, and search phrase

Create a table with two column families.

###  Python 
    
    
    from google.cloud import [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest)
    from google.cloud.bigtable import column_family
    
    client = [bigtable](https://docs.cloud.google.com/python/docs/reference/bigtable/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html)(project=PROJECT_ID, admin=True)
    instance = [client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.html).[instance](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.client.Client.html#google_cloud_bigtable_client_Client_instance)(INSTANCE_ID)
    table = instance.table(TABLE_ID)
    column_families = {"docs":column_family.[MaxVersionsGCRule](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.column_family.MaxVersionsGCRule.html)(2), "search_phrase":column_family.[MaxVersionsGCRule](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.column_family.MaxVersionsGCRule.html)(2)}
    
    if not table.exists():
      table.create(column_families=column_families)
    else:
      print("Table already exists")
    

## Embed texts with a pre-trained, foundational model from Agent Platform

Generate the text and embeddings to store in Bigtable along with the associated keys. For more information, see [Get text embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings) or [Get multimodal embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings).

###  Python 
    
    
    from typing import List, Optional
    from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
    from vertexai.generative_models import GenerativeModel
    
    #defines which LLM that we should use to generate the text
    model = GenerativeModel("gemini-1.5-pro-001")
    
    #First, use generative AI to create a list of 10 chunks for phrases
    #This can be replaced with a static list of text items or your own data
    
    chunks = []
    for i in range(10):
      response = model.generate_content(
          "Generate a paragraph between 10 and 20 words that is about about either
          Bigtable or Generative AI"
    )
    chunks.append(response.text)
    print(response.text)
    #create embeddings for the chunks of text
    def embed_text(
      texts: List[str] = chunks,
      task: str = "RETRIEVAL_DOCUMENT",
      model_name: str = "text-embedding-004",
      dimensionality: Optional[int] = 128,
    ) -> List[List[float]]:
      """Embeds texts with a pre-trained, foundational model."""
      model = TextEmbeddingModel.from_pretrained(model_name)
      inputs = [TextEmbeddingInput(text, task) for text in texts]
      kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
      embeddings = model.get_embeddings(inputs, **kwargs)
      return [embedding.values for embedding in embeddings]
    
    embeddings = embed_text()
    print("embeddings created for text phrases")
    

## Define functions that let you convert into byte objects

Bigtable is optimized for key-value pairs and generally stores data as byte objects. For more information about designing your data model for Bigtable, see [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design#general-concepts).

You need to convert the embeddings that come back from Agent Platform, which are stored as a list of floating point numbers in Python. You convert each element to big-endian IEEE 754 floating-point formation and then concatenate them together. The following function achieves this.

###  Python 
    
    
    import struct
    def floats_to_bytes(float_list):
      """
      Convert a list of floats to a bytes object, where each float is represented
      by 4 big-endian bytes.
    
      Parameters:
      float_list (list of float): The list of floats to be converted.
    
      Returns:
      bytes: The resulting bytes object with concatenated 4-byte big-endian
      representations of the floats.
      """
      byte_array = bytearray()
    
      for value in float_list:
          packed_value = struct.pack('>f', value)
          byte_array.extend(packed_value)
    
      # Convert bytearray to bytes
      return bytes(byte_array)
    

## Write the embeddings to Bigtable

Convert the embeddings to byte objects, create a mutation, and then write the data to Bigtable.

###  Python 
    
    
    from google.cloud.bigtable.data  import [RowMutationEntry](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.RowMutationEntry.html)
    from google.cloud.bigtable.data  import [SetCell](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.SetCell.html)
    
    mutations = []
    embeddings = embed_text()
    for i, embedding in enumerate(embeddings):
      print(embedding)
    
      #convert each embedding into a byte object
      vector = floats_to_bytes(embedding)
    
      #set the row key which will be used to pull the range of documents (ex. doc type or user id)
      row_key = f"doc_{i}"
    
      row = table.direct_row(row_key)
    
      #set the column for the embedding based on the byte object format of the embedding
      [row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html).set_cell("docs","embedding",vector)
      #store the text associated with vector in the same key
      [row](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.row.html).set_cell("docs","text",chunks[i])
      [mutations](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/google.cloud.bigtable.data.mutations.html).append(row)
    
    #write the rows to Bigtable
    table.mutate_rows(mutations)
    

## Perform a KNN search using GoogleSQL for Bigtable

The vectors are stored as binary-encoded data that can be read from Bigtable using a conversion function from the `BYTES` type to `ARRAY<FLOAT32>`.

Here is the SQL query:
    
    
    SELECT _key, TO_VECTOR32(data['embedding']) AS embedding
    FROM table WHERE _key LIKE 'store123%';
    

You can use the GoogleSQL `COSINE_DISTANCE` function to find the similarity between your text embeddings and the search phrases that you give it. Since this computation can take time to process, use the Python client library's [asynchronous data client](https://docs.cloud.google.com/python/docs/reference/bigtable/latest/async_data_client) to execute the SQL query.

###  Python 
    
    
    from google.cloud.bigtable.data import BigtableDataClientAsync
    
    #first embed the search phrase
    search_embedding = embed_text(texts=["Apache HBase"])
    
    query = """
          select _key, docs['text'] as description
          FROM knn_intro
          ORDER BY COSINE_DISTANCE(TO_VECTOR32(docs['embedding']), {search_embedding})
          LIMIT 1;
          """
    
    async def execute_query():
      async with BigtableDataClientAsync(project=PROJECT_ID) as client:
        local_query = query
        async for row in await client.execute_query(query.format(search_embedding=search_embedding[0]), INSTANCE_ID):
          return(row["_key"],row["description"])
    
    await execute_query()
    

The response that is returned is a generated text description that describes Bigtable.

## What's next

  * [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/bigtable/docs/langchain).
  * [Learn more about using SQL in Bigtable](https://docs.cloud.google.com/bigtable/docs/introduction-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
