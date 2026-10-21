---
url: https://docs.cloud.google.com/run/docs/ai/overview/
title: Run AI solutions on Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:29.527478+00:00
---

# Run AI solutions on Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Run AI solutions on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides an overview of using Cloud Run to host apps, run inference, and build AI workflows.

## Cloud Run for hosting AI applications, agents, and scalable API endpoints

Cloud Run provides a fully managed platform that scales your AI apps and workloads.

When you host AI apps on Cloud Run, you typically have the following architectural components:

  * **Serving and orchestration** : You deploy your application code or container to Cloud Run.
  * **AI models** : You use Google's AI models, open-source models, or custom models with your app.
  * **Integrations** : You can connect to Google Cloud services or third-party services for memory, databases, storage, security, and more.
  * **Tools** : You can connect to tools for other tasks and operations.



The following diagram shows a high-level overview of using Cloud Run as a hosting platform for AI apps:

![The four components of an AI app hosted on Cloud Run:
    1. Serving and orchestration, 2. AI models, 3. Integrations, 4. Tools.](https://docs.cloud.google.com/static/run/docs/images/components-of-cloud-run-ai-app.svg)**Figure 1.** Components of an AI app hosted on Cloud Run.

As shown in the diagram:

  1. Within the **serving and orchestration layer** , a Cloud Run service acts as a scalable API endpoint for your application's core logic. It efficiently manages multiple concurrent users through automatic, on-demand, and rapid scaling of instances.

You bring your container to deploy to Cloud Run. You can either package your application and its dependency into a container, or provide your source code and let Cloud Run automatically build your code into a container for deployment. For source code deployments, you can use any language, open frameworks, or SDKs to build your AI apps.

  2. Your AI app acts as a scalable API endpoint that handles incoming requests and sends data to a pre-trained **AI model** for processing, then returns the results.

Cloud Run is integrated with Google's models, such as the Gemini and Vertex AI models, and can integrate with open-source models, like Llama and Gemma. If you have a custom model that you've trained yourself, you can also use that model with your Cloud Run resource.

  3. Google Cloud offers a wide variety of solutions to support your AI application's infrastructure. Some **Google Cloud integrations** that work well with your AI app include:

     * Memory and databases 
       * Short-term 
         * [Memorystore](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run) is a caching and temporary, high-access data management service that provides a fast and external cache for short-term data storage.
       * Long-term 
         * [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run) is a PostgreSQL-compatible database designed for demanding transactional and analytical workloads. It offers built-in vector embedding generation and a high-speed vector index, making it fast for semantic search compared to the standard `pgvector` implementation.
         * [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) is a relational database database service for MySQL, PostgreSQL, and SQL Server that can also serve as a vector store with the `pgvector` extension for PostgreSQL.
         * [Firestore](https://docs.cloud.google.com/firestore/native/docs/overview) is a scalable NoSQL document database service that includes built-in vector search capabilities.
     * Storage 
       * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) is an object storage solution for holding large datasets for model training, input/output files for your application, or model artifacts.
     * Security 
       * [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) is a secrets and credential management service that provides a secure and centralized way to store sensitive data like API keys, passwords, and credentials, which are often required for AI applications to interact with external services.

To learn more, see [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services).

  4. **Tools** let your AI apps and models interact with services, APIs, or websites that run externally or on Cloud Run.

For example, if your AI app is an [AI agent](https://docs.cloud.google.com/run/docs/ai-agents), your agent might send a request to an [MCP server](https://docs.cloud.google.com/run/docs/host-mcp-servers) to execute an external tool, or use tools running in your container, like [code execution](https://docs.cloud.google.com/run/docs/code-execution), computer use, information retrieval, and so forth.




## Host models on Cloud Run for AI inference

In addition to building applications and agents that use a large language model (LLM), you can also enable GPUs with Cloud Run to run pre-trained or custom self-deployed models for AI inference.

Cloud Run GPUs make it possible to handle the large number of operations that are needed to run computationally demanding tasks for AI inference workloads. Deploy AI models as container images or from source code and use a variety of methods to deploy your Cloud Run resources.

## What's next

  * [Explore Cloud Run AI resources](https://docs.cloud.google.com/run/docs/ai/resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
