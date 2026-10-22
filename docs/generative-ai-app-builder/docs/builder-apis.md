---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis/
title: Vertex AI APIs for building search and RAG experiences \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:16.573202+00:00
---

# Vertex AI APIs for building search and RAG experiences  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/builder-apis/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Vertex AI APIs for building search and RAG experiences Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI offers a suite of APIs to help you build Retrieval-Augmented Generation (RAG) applications or a search engine. This page introduces those APIs.

## Retrieval and generation

RAG is a methodology that enables Large Language Models (LLMs) to generate responses that are grounded to your data source of choice. There are two stages in RAG:

  1. **Retrieval** : Getting the most relevant facts quickly can be a common search problem. With RAG, you can quickly retrieve the facts that are important to generate an answer.
  2. **Generation:** The retrieved facts are used by the LLM to generate a grounded response.



Vertex AI offers options for both stages to match a variety of developer needs.

## Retrieval

Choose the best retrieval method for your needs:

  * **Agent Search:** Agent Search is a Google Search-quality information retrieval engine that can be a component of any generative AI application that uses your enterprise data. Agent Search works as an out-of-the-box semantic & keyword search engine for RAG with the ability to process a variety of document types and with connectors to a variety of source systems including BigQuery and many third party systems.

For more information, see [Agent Search](https://docs.cloud.google.com/enterprise-search).

  * **Build your own retrieval:** If you want to build your semantic search, you can rely on Vertex AI APIs for components of your custom RAG system. This suite of APIs provide high-quality implementations for document parsing, embedding generation, vector search, and semantic ranking. Using these lower-level APIs gives you full flexibility on the design of your retriever while at the same time offering accelerated time to market and high quality by relying on lower-level Vertex AI APIs.

For more information, see Build your own Retrieval Augmented Generation.

  * **Bring an existing retrieval** : You can use your existing search as a retriever for [grounded generation](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen). You can also ground responses using RAG to upgrade your existing search to higher quality. For more information, see [Grounding overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview).

  * **Vertex AI RAG Engine** : Vertex AI RAG Engine provides a fully-managed runtime for RAG orchestration, which lets developers build RAG for use in production and enterprise-ready contexts.

For more information, see [Vertex AI RAG Engine overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-overview) in the Generative AI on Vertex AI documentation.

  * **Google Search** : When you use Grounding with Google Search for your Gemini model, then Gemini uses Google Search and generates output that is grounded to the relevant search results. This retrieval method doesn't require management and you get the world's knowledge available to Gemini.

For more information, see [Grounding with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-gemini) in the Generative AI on Vertex AI documentation.




## Generation

Choose the best generation method for your needs:

  * **Ground with your data** : Generate well-grounded answers to a user's query. The grounded generation API uses specialized, fine-tuned Gemini models and is an effective way to reduce hallucinations and provide responses grounded to your sources or third-party sources including references to grounding support content.

For more information, see [Generate grounded answers with RAG](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

You can also ground responses to your Agent Search data using Generative AI on Vertex AI. For more information, see [Ground with your data](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-with-your-data).

  * **Ground with Google Search:** Gemini is Google's most capable model and offers out-of-the-box grounding with Google Search. You can use it to build your fully-customized grounded generation solution.

For more information, see [Grounding with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-gemini) in the Generative AI on Vertex AI documentation.

  * **Model Garden:** If you want full control and the model of your choice, you can use any of the models in [Vertex AI Model Garden](https://docs.cloud.google.com/model-garden) for generation.




## Build your own Retrieval Augmented Generation

Developing a custom RAG system for grounding offers flexibility and control at every step of the process. Vertex AI offers a suite of APIs to help you create your own search solutions. Using those APIs gives you full flexibility on the design of your RAG application while at the same time offering accelerated time to market and high quality by relying on these lower-level Vertex AI APIs.

  * **The Document AI Layout Parser.** The Document AI Layout Parser transforms documents in various formats into structured representations, making content like paragraphs, tables, lists, and structural elements like headings, page headers, and footers accessible, and creating context-aware chunks that facilitate information retrieval in a range of generative AI and discovery apps.

For more information, see [Document AI Layout Parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk) in the _Document AI_ documentation.

  * **Embeddings API:** The Vertex AI embeddings APIs let you create embeddings for text or multimodal inputs. Embeddings are vectors of floating point numbers that are designed to capture the meaning of their input. You can use the embeddings to power semantic search using Vector search.

For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings) and [Multimodal embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-multimodal-embeddings) in the Generative AI on Vertex AI documentation.

  * **Vector Search.** The retrieval engine is a key part of your RAG or search application. Vertex AI Vector Search is a retrieval engine that can search from billions of semantically similar or semantically related items at scale, with high queries per second (QPS), high recall, low latency, and cost efficiency. It can search over dense embeddings, and supports sparse embedding keyword search and hybrid search in Public preview.

For more information, see: [Overview of Vertex AI Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview) in the Vertex AI documentation.

  * **The ranking API.** The ranking API takes in a list of documents and reranks those documents based on how relevant the documents are to a given query. Compared to embeddings that look purely at the semantic similarity of a document and a query, the ranking API can give you a more precise score for how well a document answers a given query.

For more information, see [Improve search and RAG quality with ranking API](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking).

  * **The grounded generation API.** Use the grounded generation API to generate well-grounded answers to a user's prompt. The grounding sources can be your Agent Search data stores, custom data that you provide, or Google Search.

For more information, see [Generate grounded answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen).

  * **The generate content API.** Use the generate content API to generate well-grounded answers to a user's prompt. The grounding sources can be your Agent Search data stores or Google Search.

For more information, see [Ground with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-with-google-search) or [Ground with your data](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-with-your-data).

  * **The check grounding API.** The check grounding API determines how grounded a given piece of text is in a given set of reference texts. The API can generate supporting citations from the reference text to indicate where the given text is supported by the reference texts. Among other things, the API can be used to assess the grounded-ness of responses from a RAG systems. Additionally, as an experimental feature, the API also generates contradicting citations that show where the given text and reference texts disagree.

For more information, see [Check grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding).




## Workflow: Generate grounded responses from unstructured data

Here's a workflow that outlines how to integrate the Vertex AI RAG APIs to generate grounded responses from unstructured data.

  1. Import your unstructured documents, such as PDF files, HTML files, or images with text, into a Cloud Storage location.
  2. Process the imported documents using the [layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk). The layout parser breaks down the unstructured documents into chunks and transforms the unstructured content into its structured representation. The layout parser also extracts annotations from the chunks.
  3. [Create text embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings) for chunks using Vertex AI text embeddings API.
  4. [Index and retrieve](https://docs.cloud.google.com/vertex-ai/docs/vector-search/create-manage-index) the chunk embeddings using Vector Search.
  5. [Rank the chunks](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking) using the ranking API and determine the top-ranked chunks.
  6. Generate grounded answers based on the top-ranked chunks using the [grounded generation API](https://docs.cloud.google.com/generative-ai-app-builder/docs/grounded-gen) or using the [generate content API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-with-your-data).



If you generated the answers using an answer generation model other than the Google models, you can [check the grounding](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-grounding) of these answers using the check grounding method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
