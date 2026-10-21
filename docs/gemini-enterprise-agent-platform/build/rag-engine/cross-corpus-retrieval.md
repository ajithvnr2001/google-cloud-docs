---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval/
title: RAG Engine Cross Corpus Retrieval \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:34.915243+00:00
---

# RAG Engine Cross Corpus Retrieval  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/cross-corpus-retrieval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  RAG Engine Cross Corpus Retrieval Stay organized with collections  Save and categorize content based on your preferences. 

The [VPC-SC security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) and CMEK are supported by Agent Platform RAG Engine. Data residency and AXT security controls aren't supported.

**Important** : Set the corpus `description` when creating a RAG corpus. The `description` is not editable after creation. **High-quality descriptions are crucial for effective cross-corpus retrieval** , as the system relies on them to select the appropriate corpora for your query.

This page describes two APIs, AsyncRetrieveContexts and AskContexts, that support RAG Cross Corpus Retrieval, powered by Agentic Retrieval in the backend.

AsyncRetrieveContexts API: This is an asynchronous API that allows users to retrieve relevant contexts from multiple RAG-managed corpora. This is a long-running API. Users can use the operation ID to get the status of the query and result.

AskContexts API: This is a synchronous API that directly generates the answer to the query by searching across multiple RAG-managed corpora.

**Important** : To use this feature, you must grant the **Vertex AI User** role in your project to the RAG Engine service account: `service-[Your project's automatically generated [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers)]@gcp-sa-vertex-rag.iam.gserviceaccount.com`.

**Important** : This feature is only available in `us-central1`.

## System Architecture and Corpus Selection

This section describes the architecture of the RAG Cross Corpus Retrieval system and how it selects appropriate corpora for retrieval.

### System Architecture

The Cross Corpus Retrieval system uses an agentic approach to orchestrate retrieval across multiple corpora. A high-level overview of the architecture includes the following components:

  * Orchestrator/Router: Receives the user query and coordinates the retrieval process.
  * Planning Agent: Analyzes the query and determines which corpora are most relevant based on their `descriptions`.
  * Retrieval Engine: Performs semantic search on the selected RAG corpora.
  * Reasoning Agent: Evaluates if the retrieved contexts are sufficient to answer the query. If insufficient, it generates feedback to trigger another retrieval loop based on Sufficient Context Awareness (SCA). For more details, see the [SCA blog post](https://research.google/blog/deeper-insights-into-retrieval-augmented-generation-the-role-of-sufficient-context/) and the [research paper](https://openreview.net/forum?id=Jjr2Odj8DJ).
  * LLM Generator (for `AskContexts`): Synthesizes the retrieved contexts to generate a final answer.



![Cross Corpus Retrieval Architecture](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/build/rag-engine/images/cross-corpus-retrieval-architecture.png)

### How Corpora are Selected

When a query is executed across multiple RAG managed corpora, the system must determine which corpus contains the information needed to answer the query. This is achieved through **Agentic Retrieval** :

  1. Corpus Mapping: The system maintains a map of available RAG corpora along with their technical descriptions (specified in the `description` field of the RAG corpus).
  2. Semantic Matching: A strategic planning agent (powered by a Gemini model) evaluates the user's query against the `descriptions` of the available corpora.
  3. Targeted Routing: The planner generates a retrieval plan that maps specific parts of the query to the most relevant corpora, ensuring that retrieval is focused and efficient rather than searching all corpora naively.



## Code Samples

The following code samples demonstrate how to use the RAG Cross Corpus Retrieval APIs.

### AsyncRetrieveContexts API

This code sample demonstrates how to retrieve contexts from multiple RAG corpora asynchronously.

###  Python 
    
    
    from vertexai.preview import rag
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    
    PROJECT_ID = "PROJECT_ID"
    LOCATION = "LOCATION"
    RAG_CORPUS_1_ID = "RAG_CORPUS_1_ID"
    RAG_CORPUS_2_ID = "RAG_CORPUS_2_ID"
    
    # Initialize API once per session
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location=LOCATION)
    
    # Async retrieve contexts from multiple corpora
    # This can be run in an environment like a Colab notebook.
    response = await rag.async_retrieve_contexts(
        text="Why is the sky blue?",
        rag_resources=[
            rag.RagResource(
                rag_corpus=f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{RAG_CORPUS_1_ID}",
            ),
            rag.RagResource(
                rag_corpus=f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{RAG_CORPUS_2_ID}",
            ),
        ],
    )
    print(response)
    

###  REST 
    
    
    PROJECT_ID="PROJECT_ID"
    LOCATION="LOCATION"
    RAG_CORPUS_1_ID="RAG_CORPUS_1_ID"
    RAG_CORPUS_2_ID="RAG_CORPUS_2_ID"
    QUERY="Why is the sky blue?"
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://${LOCATION}-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}:asyncRetrieveContexts" \
      -d '{
        "query": {
          "text": "'"$QUERY"'"
        },
        "tools": {
          "retrieval": {
            "disable_attribution": false,
            "vertex_rag_store": {
              "rag_resources": {
                "rag_corpus": "projects/'"${PROJECT_ID}"'/locations/'"${LOCATION}"'/ragCorpora/'"${RAG_CORPUS_1_ID}"'"
              },
              "rag_resources": {
                "rag_corpus": "projects/'"${PROJECT_ID}"'/locations/'"${LOCATION}"'/ragCorpora/'"${RAG_CORPUS_2_ID}"'"
              }
            }
          }
        }
      }'
    

#### Get Operation Result

Since `AsyncRetrieveContexts` is a long-running operation, you can use the `GetOperations` API to poll for the result using the operation ID.

###  Python 

**Note:** The high-level Python SDK `rag.async_retrieve_contexts` shown in the preceding example automatically waits for the operation to complete. Use the following example if you need to poll the operation manually or fetch the result of a previous operation.
    
    
    from google.cloud import aiplatform_v1beta1
    
    PROJECT_ID = "PROJECT_ID"
    LOCATION = "LOCATION"
    OPERATION_ID = "OPERATION_ID"
    
    client = aiplatform_v1beta1.[VertexRagServiceClient](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.vertex_rag_service.VertexRagServiceClient.html)(
        client_options={"api_endpoint": f"{LOCATION}-aiplatform.googleapis.com"}
    )
    
    operation = client.[get_operation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1beta1.services.vertex_rag_service.VertexRagServiceClient.html#google_cloud_aiplatform_v1beta1_services_vertex_rag_service_VertexRagServiceClient_get_operation)(
        request={"name": f"projects/{PROJECT_ID}/locations/{LOCATION}/operations/{OPERATION_ID}"}
    )
    
    if operation.done:
        print(operation.response)
    else:
        print("Operation is still running")
    

###  REST 
    
    
    PROJECT_ID="PROJECT_ID"
    LOCATION="LOCATION"
    OPERATION_ID="OPERATION_ID"
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://${LOCATION}-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/operations/${OPERATION_ID}"
    

### AskContexts API

This code sample demonstrates how to directly generate an answer by searching across multiple RAG corpora synchronously.

###  Python 
    
    
    from vertexai.preview import rag
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    
    PROJECT_ID = "PROJECT_ID"
    LOCATION = "LOCATION"
    RAG_CORPUS_1_ID = "RAG_CORPUS_1_ID"
    RAG_CORPUS_2_ID = "RAG_CORPUS_2_ID"
    
    # Initialize API once per session
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location=LOCATION)
    
    # Ask contexts from multiple corpora
    response = rag.ask_contexts(
        text="Why is the sky blue?",
        rag_resources=[
            rag.RagResource(
                rag_corpus=f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{RAG_CORPUS_1_ID}",
            ),
            rag.RagResource(
                rag_corpus=f"projects/{PROJECT_ID}/locations/{LOCATION}/ragCorpora/{RAG_CORPUS_2_ID}",
            ),
        ],
    )
    print(response)
    

###  REST 
    
    
    PROJECT_ID="PROJECT_ID"
    LOCATION="LOCATION"
    RAG_CORPUS_1_ID="RAG_CORPUS_1_ID"
    RAG_CORPUS_2_ID="RAG_CORPUS_2_ID"
    QUERY="Why is the sky blue?"
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://${LOCATION}-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}:askContexts" \
      -d '{
        "query": {
          "text": "'"$QUERY"'"
        },
        "tools": {
          "retrieval": {
            "disable_attribution": false,
            "vertex_rag_store": {
              "rag_resources": {
                "rag_corpus": "projects/'"${PROJECT_ID}"'/locations/'"${LOCATION}"'/ragCorpora/'"${RAG_CORPUS_1_ID}"'"
              },
              "rag_resources": {
                "rag_corpus": "projects/'"${PROJECT_ID}"'/locations/'"${LOCATION}"'/ragCorpora/'"${RAG_CORPUS_2_ID}"'"
              }
            }
          }
        }
      }'
    

## What's next

  * To learn more about the RAG API, see [RAG Engine API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/rag-api).
  * To learn more about the responses from RAG, see [Retrieval and Generation Output of RAG Engine](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/rag-output-explained).
  * To learn about the RAG Engine, see the [RAG Engine overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
