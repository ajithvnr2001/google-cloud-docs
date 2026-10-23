---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/supported-rag-models/
title: RAG Engine on Gemini Enterprise Agent Platform supported models \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:58.446413+00:00
---

# RAG Engine on Gemini Enterprise Agent Platform supported models  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/supported-rag-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  RAG Engine on Gemini Enterprise Agent Platform supported models Stay organized with collections  Save and categorize content based on your preferences. 

The [VPC-SC security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.

This page lists Gemini models, self-deployed models, and models with managed APIs on Agent Platform that support RAG Engine on Gemini Enterprise Agent Platform.

## Gemini models

The following models support RAG Engine:

#### Click to expand supported models

  * [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)
  * [Gemini 3.7 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash)
  * [Gemini 3.6 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash)
  * [Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)
  * [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash)
  * [Gemini 3.1 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) preview
  * [Gemini 3.1 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)
  * [Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) preview
  * [Gemini 2.5 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-pro)
  * [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)
  * [Gemini 2.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)



Fine-tuned Gemini models are unsupported when the Gemini models use RAG Engine on Gemini Enterprise Agent Platform.

## Self-deployed models

RAG Engine on Gemini Enterprise Agent Platform supports all models in [Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models).

Use RAG Engine with your self-deployed open model endpoints.

Replace the variables used in the code sample:

  * **PROJECT_ID** : Your project ID.
  * **LOCATION** : The region to process your request.
  * **ENDPOINT_ID** : Your endpoint ID.
        
        # Create a model instance with your self-deployed open model endpoint
          rag_model = GenerativeModel(
              "projects/PROJECT_ID/locations/LOCATION/endpoints/ENDPOINT_ID",
              tools=[rag_retrieval_tool]
          )
        




## Models with managed APIs on Agent Platform

The models with managed APIs on Agent Platform that support RAG Engine include the following:

  * [Mistral on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/mistral)
  * [Llama 3.1 and 3.2](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/llama)



The following code sample demonstrates how to use the Gemini `GenerateContent` API to create a generative model instance. The model ID, `/publisher/meta/models/llama-3.1-405B-instruct-maas`, is found in the [model card](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models).

Replace the variables used in the code sample:

  * **PROJECT_ID** : Your project ID.
  * **LOCATION** : The region to process your request.
  * **RAG_RETRIEVAL_TOOL** : Your RAG retrieval tool.
        
        # Create a model instance with Llama 3.1 MaaS endpoint
          rag_model = GenerativeModel(
              "projects/PROJECT_ID/locations/LOCATION/publisher/meta/models/llama-3.1-405B-instruct-maas",
              tools=RAG_RETRIEVAL_TOOL
          )
        




The following code sample demonstrates how to use the OpenAI compatible `ChatCompletions` API to generate a model response.

Replace the variables used in the code sample:

  * **PROJECT_ID** : Your project ID.
  * **LOCATION** : The region to process your request.
  * **MODEL_ID** : LLM model for content generation. For example, `meta/llama-3.1-405b-instruct-maas`.
  * **INPUT_PROMPT** : The text sent to the LLM for content generation. Use a prompt relevant to the documents in Agent Search.
  * **RAG_CORPUS_ID** : The ID of the RAG corpus resource.
  * **ROLE** : Your role.
  * **USER** : Your username.
  * **CONTENT** : Your content.
        
        # Generate a response with Llama 3.1 MaaS endpoint
          response = client.chat.completions.create(
              model="MODEL_ID",
              messages=[{"ROLE": "USER", "content": "CONTENT"}],
              extra_body={
                  "extra_body": {
                      "google": {
                          "vertex_rag_store": {
                              "rag_resources": {
                                  "rag_corpus": "RAG_CORPUS_ID"
                              },
                              "similarity_top_k": 10
                          }
                      }
                  }
              },
          )
        




## What's next

  * [Use Embedding models with RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-embedding-models).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
