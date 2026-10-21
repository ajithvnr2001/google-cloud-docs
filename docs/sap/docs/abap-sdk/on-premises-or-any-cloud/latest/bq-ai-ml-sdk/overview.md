---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview/
title: BigQuery AI and ML SDK for ABAP overview \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:08.206159+00:00
---

# BigQuery AI and ML SDK for ABAP overview  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  BigQuery AI and ML SDK for ABAP overview Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/overview)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/overview)



The BigQuery AI and ML SDK for ABAP streamlines the integration of AI and ML capabilities on BigQuery from ABAP applications and ABAP based AI Agents.

The BigQuery AI and ML SDK for ABAP is built on top of the ABAP SDK for Google Cloud. The SDK is available only with the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

## Why use the BigQuery AI and ML SDK for ABAP

The BigQuery AI and ML SDK for ABAP provides dedicated toolsets to support your generative AI-based ABAP agents or applications with the BigQuery AI and ML capabilities.

With the BigQuery AI and ML SDK for ABAP, you can use the following capabilities from your ABAP environment:

  * Use Gemini to analyze your enterprise data in BigQuery.
  * Generate and manage embeddings for enterprise data in BigQuery to make BigQuery as your low-cost vector database.
  * Perform vector search on your enterprise data in BigQuery for similarity search or to RAG your model.



The following diagram shows how to use the BigQuery AI and ML capabilities through the BigQuery AI and ML SDK for ABAP:

![BigQuery AI and ML SDK for ABAP overview](https://docs.cloud.google.com/static/sap/docs/images/abap-sdk-sap-bq-ai-ml-overview.svg)

As shown in the preceding diagram, the user flow with the BigQuery AI and ML SDK for ABAP is as follows:

  1. The user invokes an ABAP AI application or an AI agent with an input prompt.
  2. The AI agent uses the BigQuery AI and ML SDK for ABAP to use the AI and ML capabilities on source data in BigQuery.
  3. The BigQuery AI and ML SDK for ABAP performs the following for the AI agent:

     * Generates Gemini-driven insight on enterprise data stored in BigQuery.
     * Delivers ML model-driven predictions on enterprise data stored in BigQuery.
     * Generates and manages embeddings in BigQuery.
     * Performs vector similarity search in BigQuery.
  4. The BigQuery AI and ML SDK for ABAP responds to the AI agent with the AI and ML insights based on the invoked BigQuery module and the user prompt.




## Get started with the BigQuery AI and ML SDK for ABAP

###  [ Store and manage enterprise queries ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/store-manage-enterprise-queries)

Store, manage, and share frequently used enterprise queries centrally within BigQuery. 

###  [ Get Gemini insights on BigQuery data ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights)

Use Gemini to analyze your enterprise data stored in BigQuery. 

###  [ Generate and manage embeddings ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/generate-manage-embeddings)

Generate and manage embeddings for your enterprise data stored in BigQuery. 

###  [ Perform vector similarity search ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/perform-vector-search)

Perform vector similarity search on your enterprise data stored in BigQuery. 

## Pricing

The BigQuery AI and ML SDK for ABAP is offered at no cost. However, you are responsible for the charges for the compute resources that you use to train models and to run queries against models.

The type of model that you create affects where the model is trained and the pricing that applies to that operation. Queries against models always run in BigQuery and use [BigQuery compute pricing](https://cloud.google.com/bigquery/pricing#analysis_pricing_models). Because remote models make calls to Agent Platform models, queries against remote models also incur charges from Agent Platform.

You are charged for the storage used by trained models, using [BigQuery storage pricing](https://cloud.google.com/bigquery/pricing#storage). For more information, see [BigQuery ML pricing](https://cloud.google.com/bigquery/pricing#bqml).

## What's next

  * Learn how to [install and configure the BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap).
  * Ask your questions and discuss the BigQuery AI and ML SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
