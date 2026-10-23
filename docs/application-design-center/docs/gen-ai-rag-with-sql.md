---
url: https://docs.cloud.google.com/application-design-center/docs/gen-ai-rag-with-sql/
title: Generative AI RAG with Cloud SQL \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:19.092760+00:00
---

# Generative AI RAG with Cloud SQL  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/gen-ai-rag-with-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Generative AI RAG with Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

Build a generative AI chat application that uses retrieval-augmented generation (RAG) to provide grounded and accurate responses based on your organization's data. This guide describes the _Generative AI RAG with Cloud SQL_ application template, which you can customize to fit your unique needs and deploy as an application.

For example, you might implement this template to address the following business needs:

Example | Business need | Implementation  
---|---|---  
Customer support chatbot | Companies need to provide instant customer support. | Host the chat interface on Cloud Run. Vertex AI processes embeddings and generates responses based on technical documentation stored as vectors in Cloud SQL.  
Internal HR assistant | Employees need to find information about benefits, company policies, and internal procedures. | Host the HR assistant on Cloud Run. When employees query the tool, Vertex AI retrieves relevant policy information from Cloud SQL to generate accurate, source-grounded answers.  
Legal document researcher | Legal teams need to quickly find relevant case law or contract clauses across large document repositories. | Host the research portal on Cloud Run. Vertex AI summarizes relevant precedents and identifies specific language in contracts using legal documents stored as vectors in Cloud SQL.  
Semantic product search | Ecommerce companies want to facilitate product searches using natural language descriptions rather than exact keywords. | Host the search interface on Cloud Run. Vertex AI processes user descriptions to return the most semantically relevant products from product catalogs stored as vectors in Cloud SQL.  
  
## Architecture

The following image shows the components and connections in the application:

![A generative AI RAG application in the design canvas. The application includes frontend, retrieval, AI, secret management, and database components.](https://docs.cloud.google.com/static/application-design-center/images/google-generative-ai-rag.png)

The following is the request processing flow of the application:

  1. Load data to a PostgreSQL database in [Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/introduction).
  2. [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) creates embeddings of text fields and stores them as vectors in the database.
  3. A [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) frontend receives external requests and distributes traffic to the Cloud Load Balancing backend.
  4. The Cloud Load Balancing backend distributes traffic to the [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) frontend service.
  5. The frontend service communicates with a retrieval service for a generative AI call.
  6. The retrieval service uses [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to securely access API keys and credentials that are required to access Vertex AI and Cloud SQL.
  7. The retrieval service converts the request to an embedding and searches for similar vectors in the Cloud SQL database.
  8. The retrieval service sends results from the search, along with the original prompt, to Vertex AI to create a response.



## What's next

  * To learn how to duplicate and customize this template, see [Quickstart: Customize and deploy a Google template](https://docs.cloud.google.com/application-design-center/docs/quickstart-deploy-google-template).
  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Identify general architectural best practices with the [Google Cloud Architecture Framework](https://docs.cloud.google.com/architecture/framework).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
