---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/create-examplestore/
title: Create or reuse an Example Store instance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:14.543637+00:00
---

# Create or reuse an Example Store instance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/create-examplestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Agents ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents)



Send feedback 

#  Create or reuse an Example Store instance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page shows you how to create a new Example Store instance or reuse an existing Example Store instance. You can store your examples in an Example Store when developing your LLM application and dynamically retrieve them to use in your LLM prompts.

To teach an LLM or an agent using few-shot examples, you must first create or reuse an Example Store instance for your project and location, and then upload examples to it.

For each project and location, you can have a maximum of 50 Example Store instances. After you create an Example Store instance, you can share it across multiple LLM applications and agents.

There are two ways to provision an Example Store instance:

  * **Create a new Example Store instance** : When you create a new Example Store instance, you need to specify the embedding model, which Example Store uses to determine which examples are relevant to users' queries. Example Store supports the following embedding models:

    * `text-embedding-005`

    * `text-multilingual-embedding-002`

You can't change an embedding model after you create the Example Store instance. If you want to use a different embedding model, you must create another example store. For more information about text embeddings, see [Get text embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-text-embeddings).

  * **Reuse an existing Example Store instance** : Example Store instances are designed to be used by multiple agents, so you can access the stored examples across LLM applications. You can't change the embedding model when you reuse an existing Example Store instance.




## Prerequisites

Before you use the Python samples on this page, install and initialize the Agent Platform SDK in your local Python environment.

  1. Run the following command to install the Agent Platform SDK for Example Store.
         
         pip install --upgrade google-cloud-aiplatform>=1.87.0

  2. Use the following code sample to import and initialize the SDK for Example Store.
         
         import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
         from vertexai.preview import example_stores
         
         [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
           project="PROJECT_ID",
           location="LOCATION"
         )
         

Replace the following:

     * PROJECT_ID: Your project ID.

     * LOCATION: Your region. Only `us-central1` is supported.




## Create an Example Store instance

Use the following samples to create an Example Store instance for a specified project and location. Note that creating an Example Store instance takes a few minutes.

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import example_stores
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
        project="PROJECT_ID",
        location="LOCATION"
    )
    
    my_example_store = example_stores.ExampleStore.create(
        example_store_config=example_stores.ExampleStoreConfig(
            vertex_embedding_model="EMBEDDING_MODEL"
        )
    )
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: The region where you want to create the example store. The only region supported is `us-central1`.
  * EMBEDDING_MODEL: Embedding model that the Example Store instance uses to determine which examples are relevant to users' queries. Example Store supports the following embedding models: 
    * `text-embedding-005`
    * `text-multilingual-embedding-002`



### REST

To create an [`ExampleStore`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores) resource, send a `POST` request by using the [`exampleStores.create`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/create) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your project ID.
  * LOCATION: The region where you want to create the Example Store instance. The only region supported is `us-central1`.
  * DISPLAY_NAME: The name of the Example Store instance.
  * EMBEDDING_MODEL: Embedding model that the Example Store instance uses to determine which examples are relevant to users' queries. Example Store supports the following embedding models: 
    * `textembedding-gecko@003`
    * `text-embedding-004`
    * `text-multilingual-embedding-002`



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/exampleStores

Request JSON body: 
    
    
    {
      "display_name": "DISPLAY_NAME",
      "example_store_config": {"vertex_embedding_model": EMBEDDING_MODEL}
    }
    
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/exampleStores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/exampleStores" | Select-Object -Expand Content

You should receive a JSON response similar to the following, where EXAMPLE_STORE_ID represents the ID of the Example Store instance. 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/exampleStores/EXAMPLE_STORE_ID/operations/",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.aiplatform.v1beta1.CreateExampleStoreOperationMetadata",
        "genericMetadata": {
          "createTime": "2024-10-10T02:06:10.417111Z",
          "updateTime": "2024-10-10T02:06:10.417111Z"
        }
      }
    }
    

## Reuse an existing Example Store instance

Use the following sample to reuse an existing Example Store instance for a specified project and location.

### Python

Before trying this sample, follow the Python setup instructions in the [Agent Platform quickstart using client libraries](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries). 

To authenticate to Agent Platform, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import example_stores
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
        project="PROJECT_ID",
        location="LOCATION"
    )
    
    example_store = example_stores.ExampleStore(
        "EXAMPLE_STORE_NAME")
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: The region where you want to create the example store. The only region supported is `us-central1`.
  * EXAMPLE_STORE_NAME: Name of the Example Store instance you want to reuse. 



## What's next

  * [Upload examples to the Example Store instance.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/example-store/upload-examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
