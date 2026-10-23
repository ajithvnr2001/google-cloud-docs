---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-rag-generate-content/
title: Generate responses using the RAG file \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:09.229132+00:00
---

# Generate responses using the RAG file  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-rag-generate-content/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Generate responses using the RAG file Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to generate the content using a RAG file.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [RAG Engine API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/rag-api-v1)
  * [Use a Weaviate database with RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-weaviate-db)
  * [Use Agent Platform Vector Search with RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-vertexai-vector-search)
  * [Use Agent Search as a retrieval backend using RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-vertexai-search)
  * [Use Vertex AI Feature Store in RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/use-feature-store-with-rag)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google import genai
    from google.genai import types as genai_types
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # corpus_name = "projects/{PROJECT_ID}/locations/us-central1/ragCorpora/{rag_corpus_id}"
    
    rag_retrieval_tool = genai_types.Tool(
        retrieval=genai_types.Retrieval(
            vertex_rag_store=genai_types.VertexRagStore(
                rag_resources=[
                    genai_types.VertexRagStoreRagResource(
                        rag_corpus=corpus_name
                    )
                ],
                rag_retrieval_config=genai_types.RagRetrievalConfig(
                    top_k=10,
                    filter=genai_types.RagRetrievalConfigFilter(
                        vector_distance_threshold=0.5
                    ),
                ),
            ),
        )
    )
    
    # Create a GenAI SDK client to make a generate_content request
    genai_client = genai.Client(enterprise=True, project=PROJECT_ID, location="us-central1")
    
    response = genai_client.models.generate_content(
        model="gemini-2.5-pro",
        contents="Why is the sky blue?",
        config=genai_types.GenerateContentConfig(
            tools=[rag_retrieval_tool]
        )
    )
    print(response.text)
    # Example response:
    #   The sky appears blue due to a phenomenon called Rayleigh scattering.
    #   Sunlight, which contains all colors of the rainbow, is scattered
    #   by the tiny particles in the Earth's atmosphere....
    #   ...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
