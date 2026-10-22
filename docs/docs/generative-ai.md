---
url: https://docs.cloud.google.com/docs/generative-ai/
title: Generative AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:44.379170+00:00
---

# Generative AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/generative-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Generative AI ](https://docs.cloud.google.com/docs/generative-ai)



![](https://docs.cloud.google.com/_static/clouddocs/images/icons/categories/ai-and-machine-learning-color.svg)

# Generative AI

Documentation and resources for building and implementing generative AI applications with Google Cloud tools and products.

[Get started for free](https://console.cloud.google.com/freetrial)

#### Start your proof of concept with $300 in free credit

  * Develop with our latest Generative AI models and tools. 
  * Get free usage of 20+ popular products, including Compute Engine and AI APIs. 
  * No automatic charges, no commitment. 



[ View free product offers ](https://docs.cloud.google.com/free/docs/free-cloud-features#free-tier)

#### Keep exploring with 20+ always-free products.

Access 20+ free products for common use cases, including AI APIs, VMs, data warehouses, and more. 

##  Learn about building generative AI applications 

###  [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview)

Access Google's large generative AI models so you can test, tune, and deploy them for use in your AI-powered applications. 

###  [ Gemini Quickstart ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart-multimodal)

See what it's like to send requests to the Gemini API through Google Cloud's AI-ML platform, Vertex AI. 

###  [ AI/ML orchestration on GKE ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)

Leverage the power of GKE as a customizable AI/ML platform featuring high performance, cost effective serving and training with industry-leading scale and flexible infrastructure options. 

###  [ When to use generative AI ](https://docs.cloud.google.com/docs/ai-ml/generative-ai/generative-ai-or-traditional-ai)

Identify whether generative AI, traditional AI, or a combination of both might suit your business use case. 

###  [ Develop a generative AI application ](https://docs.cloud.google.com/docs/ai-ml/generative-ai/develop-generative-ai-application)

Learn how to address the challenges in each stage of developing a generative AI application. 

###  [ Code samples and sample applications ](https://docs.cloud.google.com/docs/generative-ai/code-samples)

View code samples for popular use cases and deploy examples of generative AI applications that are secure, efficient, resilient, high-performing, and cost-effective. 

###  [ Generative AI glossary ](https://docs.cloud.google.com/docs/generative-ai/glossary)

Learn about specific terms that are associated with generative AI. 

## Gen AI tools

![List of generative AI tools including Vertex AI Studio, Colab Enterprise/Notebooks, and Workbench listed under Cloud Console, and SDK/APIs listed as a separate item.](https://docs.cloud.google.com/static/docs/generative-ai/images/gen-ai-tools.svg)

## Gen AI development flow

![Diagram of the generative AI development flow with six stages: model selection \(including Model Garden\), prompt engineering \(including prompt gallery, Vertex AI Studio, compare prompts, and optimize prompt\), tuning \(including training and tuning\), optimization \(including distillation\), deployment \(including Model Registry, online prediction, and batch prediction\), and monitoring. The model selection, prompt engineering, tuning, and optimization stages are part of a looping subcycle labeled Evaluation.](https://docs.cloud.google.com/static/docs/generative-ai/images/gen-ai-dev-flow.svg)

##  Model exploration and hosting 

Google Cloud provides a set of state-of-the-art foundation models through Vertex AI, including Gemini. You can also deploy a third-party model to either Vertex AI Model Garden or self-host on GKE or Compute Engine.

###  [ Google Models on Vertex AI (Gemini, Imagen) ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/models)

Discover test, customize, and deploy Google models and assets from an ML model library. 

###  [ Other models in the Vertex AI Model Garden ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)

Discover, test, customize, and deploy select OSS models and assets from an ML model library. 

###  [ Text generation models via HuggingFace ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-hugging-face-models)

Learn how to deploy HuggingFace text generation models to Vertex AI or Google Kubernetes Engine (GKE). 

###  [ GPUs on Compute Engine ](https://docs.cloud.google.com/compute/docs/gpus/about-gpus)

Attach GPUs to VM instances to accelerate generative AI workloads on Compute Engine. 

##  Prompt design and engineering 

Prompt design is the process of authoring prompt and response pairs to give language models additional context and instructions. After you author prompts, you feed them to the model as a prompt dataset for pretraining. When a model serves predictions, it responds with your instructions built in.

###  [ Vertex AI Studio ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart)

Design, test, and customize your prompts sent to Google's Gemini and PaLM 2 large language models (LLM). 

###  [ Overview of Prompting Strategies ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)

Learn the prompt-engineering workflow and common strategies that you can use to affect model responses. 

###  [ Prompt Gallery ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery)

View example prompts and responses for specific use cases. 

##  Grounding and RAG 

_Grounding_ connects AI models to data sources to improve the accuracy of responses and reduce hallucinations. _RAG_ , a common grounding technique, searches for relevant information and adds it to the model's prompt, ensuring output is based on facts and up-to-date information.

###  [ Vertex AI grounding ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)

You can ground Vertex AI models with Google Search or with your own data stored in Agent Search. 

###  [ Ground with Google Search ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/ground-gemini#web-ground-gemini)

Use Grounding with Google Search to connect the model to the up-to-date knowledge available on the internet. 

###  [ Vector embeddings in AlloyDB ](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings)

Use AlloyDB to generate and store vector embeddings, then index and query the embeddings using the pgvector extension. 

###  [ Cloud SQL and pgvector ](https://github.com/pgvector/pgvector?tab=readme-ov-file#pgvector)

Store vector embeddings in Postgres SQL, then index and query the embeddings using the pgvector extension. 

###  [ Integrating BigQuery data into your LangChain application ](https://cloud.google.com/blog/products/ai-machine-learning/open-source-framework-for-connecting-llms-to-your-data)

Use LangChain to extract data from BigQuery and enrich and ground your model's responses. 

[ description  ](https://docs.cloud.google.com/firestore/docs/vector-search)

###  [ Vector embeddings in Firestore ](https://docs.cloud.google.com/firestore/docs/vector-search)

Create vector embeddings from your Firestore data, then index and query the embeddings. 

###  [ Vector embeddings in Memorystore (Redis) ](https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search)

Use LangChain to extract data from Memorystore and enrich and ground your model's responses. 

##  Agents and function calling 

Agents make it easy to design and integrate a conversational user interface into your mobile app, while function calling extends the capabilities of a model.

###  [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction)

Leverage Google's foundation models, search expertise, and conversational AI technologies for enterprise-grade generative AI applications. 

###  [ Vertex AI Function calling ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling)

Add function calling to your model to enable actions like booking a reservation based on extracted calendar information. 

##  Model customization and training 

Specialized tasks, such as training a language model on specific terminology, might require more training than you can do with prompt design or grounding alone. In that scenario, you can use model tuning to improve performance, or train your own model.

###  [ Evaluate models in Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)

Evaluate the performance of foundation models and your tuned generative AI models on Vertex AI. 

###  [ Tune Vertex AI models ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)

General purpose foundation models can benefit from tuning to improve their performance on specific tasks. 

###  [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)

TPUs are Google's custom-developed ASICs used to accelerate machine learning workloads, such as training an LLM. 

##  Related guides and sites 

[ description  ](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search)

Intermediate

###  [ Infrastructure for a RAG-capable generative AI application using Vertex AI and Vector Search ](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search)

Reference architecture for a RAG-capable generative AI application using Vertex AI and Vector Search. 

[ description  ](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai)

Intermediate

###  [ Infrastructure for a RAG-capable generative AI application using Vertex AI and AlloyDB for PostgreSQL ](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai)

Reference architecture for a RAG-capable generative AI application using Vertex AI and AlloyDB for PostgreSQL. 

[ description  ](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke)

Intermediate

###  [ Infrastructure for a RAG-capable generative AI application using GKE and Cloud SQL ](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-gke)

Reference architecture for a RAG-capable generative AI application using GKE, Cloud SQL, and open source tools like Ray, Hugging Face, and LangChain. 

## Start building

### Set up your development environment for Google Cloud

  * [C# and .NET](https://docs.cloud.google.com/dotnet/docs/setup)
  * [C++](https://docs.cloud.google.com/cpp/docs/setup)
  * [Go](https://docs.cloud.google.com/go/docs/setup)
  * [Java](https://docs.cloud.google.com/java/docs/setup)
  * [JavaScript and Node.js](https://docs.cloud.google.com/nodejs/docs/setup)
  * [Python](https://docs.cloud.google.com/python/docs/setup)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/setup)



### Set up LangChain

LangChain is an open source framework for generative AI apps that allows you to build context into your prompts, and take action based on the model's response. 

  * [Python (LangChain)](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm)
  * [JavaScript (LangChain.js)](https://js.langchain.com/docs/integrations/platforms/google)
  * [Java (LangChain4j)](https://docs.langchain4j.dev/integrations/language-models/google-palm/)
  * [Go (LangChainGo)](https://tmc.github.io/langchaingo/docs/)



### View code samples and deploy sample applications

View [code samples for popular use cases and deploy examples of generative AI applications](https://docs.cloud.google.com/docs/generative-ai/code-samples) that are secure, efficient, resilient, high-performing, and cost-effective. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
