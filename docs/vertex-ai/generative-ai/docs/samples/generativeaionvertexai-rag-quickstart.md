---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-rag-quickstart/
title: Use the quickstart to get familiar with RAG \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:12.581261+00:00
---

# Use the quickstart to get familiar with RAG  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-rag-quickstart/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Use the quickstart to get familiar with RAG Stay organized with collections  Save and categorize content based on your preferences. 

This quickstart demonstrates how to use the RAG API.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [RAG quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-quickstart)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import agentplatform
    
    from agentplatform import types
    from google import genai
    from google.genai import types as genai_types
    
    
    # Create a RAG Corpus, Import Files, and Generate a response
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # MODEL_ID = "gemini-3.5-flash"
    # display_name = "test_corpus"
    # gcs_path = "gs://my_bucket/my_files_dir/*"
    # google_drive_path ="https://drive.google.com/file/d/123"
    
    # Initialize Agent Platform client once per session
    client = agentplatform.Client(project=PROJECT_ID, location="us-east4")
    
    # Configure embedding model, for example "text-embedding-005".
    embedding_model_config = types.RagEmbeddingModelConfig(
        vertex_prediction_endpoint=types.RagEmbeddingModelConfigVertexPredictionEndpoint(
            endpoint="publishers/google/models/text-embedding-005"
        ),
    )
    
    # Create RagCorpus
    rag_corpus = client.rag.create_corpus(
        rag_corpus=types.RagCorpus(
            display_name=display_name,
            rag_vector_db_config=types.RagVectorDbConfig(
                rag_embedding_model_config=embedding_model_config
            )
        )
    )
    
    # Import Files to the RagCorpus
    client.rag.import_files(
        name=rag_corpus.name,
        import_config=types.ImportRagFilesConfig(
            gcs_source=genai_types.GcsSource(uris=[gcs_path]),
            rag_file_transformation_config=types.RagFileTransformationConfig(
                rag_file_chunking_config=types.RagFileChunkingConfig(
                    chunk_size=512,
                    chunk_overlap=100,
                )
            ), # optional
            max_embedding_requests_per_min=1000, # optional
        )
    )
    
    # Direct context retrieval
    rag_retrieval_config = genai_types.RagRetrievalConfig(
        top_k=3,  # Optional
        filter=genai_types.RagRetrievalConfigFilter(
            vector_distance_threshold=0.5
        ),  # Optional
    )
    response = client.rag.retrieve_contexts(
        vertex_rag_store=genai_types.VertexRagStore(
            rag_resources=[
                genai_types.VertexRagStoreRagResource(
                    rag_corpus=rag_corpus.name,
                )
            ],
        ),
        query=types.RagQuery(
            text="What is RAG and why it is helpful?",
            rag_retrieval_config=rag_retrieval_config,   
        )
    )
    print(response)
    
    # Enhance generation
    # Create a RAG retrieval tool
    rag_retrieval_tool = genai_types.Tool(
        retrieval=genai_types.Retrieval(
            vertex_rag_store=genai_types.VertexRagStore(
                rag_resources=[
                    genai_types.VertexRagStoreRagResource(
                        rag_corpus=rag_corpus.name,
                        # Optional: supply IDs from `rag.list_files()`.
                        # rag_file_ids=["rag-file-1", "rag-file-2", ...],
                    )
                ],
                rag_retrieval_config=rag_retrieval_config,
            ),
        )
    )
    
    # Call generate_content with the tool using the GenAI SDK
    
    # Create a GenAI SDK client
    genai_client = genai.Client(enterprise=True, project=PROJECT_ID, location="us-east4")
    
    
    response = genai_client.models.generate_content(
        model=MODEL_ID,
        contents="What is RAG and why it is helpful?",
        config=genai_types.GenerateContentConfig(
            tools=[rag_retrieval_tool]
        )
    )
    print(response.text)
    # Example response:
    #   RAG stands for Retrieval-Augmented Generation.
    #   It's a technique used in AI to enhance the quality of responses
    # ...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
