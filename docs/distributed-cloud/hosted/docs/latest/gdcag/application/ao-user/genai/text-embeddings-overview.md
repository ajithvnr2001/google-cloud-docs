---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-overview/
title: Text embeddings overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:48:11.172702+00:00
---

# Text embeddings overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/text-embeddings-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Text embeddings overview Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** This content applies to version 1.14.4 and later.

Embeddings are numerical representations of text, images, or videos that capture relationships between inputs. Machine learning models, especially Generative AI models, are suited for creating embeddings by identifying patterns within large datasets. Applications can use embeddings to process and produce language, recognizing complex meanings and semantic relationships specific to your content.

Vertex AI on Google Distributed Cloud (GDC) air-gapped supports Text Embedding APIs for English and multilingual textual input. Text Embedding works by converting text into arrays of floating-point numbers called vectors. These vectors are designed to capture the meaning of the text. The length of the embedding array is called the vector's dimensionality. For example, one passage of text might be represented by a vector containing hundreds of dimensions. Then, by calculating the numerical distance between the vector representations of two pieces of text, an application can determine the similarity between the objects.

**Note:** Only text is supported as an input type for embeddings on GDC.

For a list of supported models, see [Embeddings models](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/genai-models#embeddings-models).

For a list of supported multilingual languages, see [Supported text embedding languages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/supported-text-languages).

## Text embeddings use cases

Some common use cases for text embeddings include:

  * **Semantic search** : Search text ranked by semantic similarity.
  * **Classification** : Return the class of items with attributes similar to the given text.
  * **Clustering** : Cluster items whose text attributes are similar to the given text.
  * **Outlier detection** : Return items where text attributes are least related to the given text.
  * **Conversational interface** : Cluster groups of sentences that can lead to similar responses, like in a conversation-level embedding space.



### Example use case: Develop a book recommendation chatbot

If you want to develop a book recommendation chatbot, the first thing to do is to use a deep neural network (DNN) to convert each book into an embedding vector, where one embedding vector represents one book. You can feed the book title or text content as input to the DNN. Alternatively, you can use both of these inputs together, along with any other metadata describing the book, such as the genre.

The embeddings in this example could include thousands of book titles with summaries and their genre. It might have representations for books like _Wuthering Heights_ by Emily Brontë and _Persuasion_ by Jane Austen that are similar to each other (small distance between numerical representation). In contrast, the numerical representation of the book _The Great Gatsby_ by F. Scott Fitzgerald would be further, as the time period, genre, and summary are less similar.

The inputs are the main influence on the orientation of the embedding space. For example, if we only had book title inputs, then two books with similar titles but very different summaries could be close together. However, if we include the title and summary, then these same books are less similar (further away) in the embedding space.

Working with Generative AI, this book-suggestion chatbot could summarize, suggest, and show you books that you might like (or dislike) based on your query.

## What's next

  * Learn how to [get text embeddings](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/genai/get-text-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
