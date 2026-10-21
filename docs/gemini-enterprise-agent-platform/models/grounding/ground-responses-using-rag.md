---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/ground-responses-using-rag/
title: Ground responses using RAG \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:00.681684+00:00
---

# Ground responses using RAG  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/ground-responses-using-rag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Ground responses using RAG Stay organized with collections  Save and categorize content based on your preferences. 

Grounding is a technique that you can use to help produce model responses that are more trustworthy, helpful, and factual. When you ground generative AI model responses, you connect them to verifiable sources of information. To implement grounding, you must retrieve relevant source data. The recommended best practice is to use the retrieval-augmented generation (RAG) technique. Retrieval is usually done using a search engine, which uses an index that's embedded with the semantic meanings of the source text.

There are also services and component APIs that implement the RAG lifecycle, such as the Agent Search Builder API, which allows for mix-and-match building. With mix-and-match building, you can implement a RAG solution using any of the following services or APIs:

  * **Grounding generation API** : You can use it to implement grounding, or link to a retrieval provider for the complete RAG lifecycle.
  * **Document layout parser** : This parser represents the best of Document AI and Gemini for document understanding. For more information about the layout parser, see [Use the layout parser](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/layout-parser-integration).
  * **Gemini Enterprise Agent Platform Vector Search** : This search service is highly performant and uses a high-quality vector database.
  * **Check grounding API** : This API compares RAG output with the retrieved facts and helps to ensure that all statements are grounded before returning the response to the user.



## Ground responses using RAG Engine on Gemini Enterprise Agent Platform

To ground responses using RAG Engine, you must create a prompt. Do the following:

  1. In the Google Cloud console, go to the **Agent Studio** page.

[Go to Agent Studio](https://console.cloud.google.com/agent-platform/studio/multimodal;mode=prompt)

  2. In the side panel, under **Model settings** , go to the **Grounding** section, and turn on the **Your data** toggle.

  3. In the configuration pane, select **RAG Engine** as the grounding source.

  4. From the **Corpus** list, select your corpus name.

  5. In the **Top-K Similarity** field, select **20** , which is the default.

  6. Click **Save**.




## What's next

  * To learn more about responsible AI and safety filters, see [responsible AI best practices and Gemini Enterprise Agent Platform's safety filters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai).
  * To learn more about how RAG is implemented by RAG Engine, see [RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
