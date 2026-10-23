---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk-overview/
title: Overview of the Agent Platform SDK for ABAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:50.666137+00:00
---

# Overview of the Agent Platform SDK for ABAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Overview of the Agent Platform SDK for ABAP Stay organized with collections  Save and categorize content based on your preferences. 

The **Agent Platform SDK for ABAP** (formerly **Vertex AI SDK for ABAP**) lets you interact with the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform) programmatically by using [ABAP](https://training.sap.com/content/abap-programming-training). With ready-to-use ABAP classes and AI-centric data types, you can build AI-powered enterprise applications in your SAP environment without having to write custom API integration logic. 

The Agent Platform SDK for ABAP is built on the ABAP SDK for Google Cloud. The Agent Platform SDK for ABAP is available with both the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config) and the [SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config).

## Supported models

The models you can access depend on the SDK edition you use:

Edition | Supported models and services  
---|---  
On-premises or any cloud edition | 

  * [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#gemini-models), [Embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings), [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview), and [Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).
  * [Anthropic Claude models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude), which are offered on Agent Platform as [Model as a Service (MaaS)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-partner-models).
  * [Gemma models](https://ai.google.dev/gemma/docs).

  
SAP BTP edition | 

  * [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#gemini-models), [Embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings), [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview), and [Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).

  
  
## Why use the Agent Platform SDK for ABAP

The Agent Platform SDK for ABAP offers the following capabilities:

  * **Use ABAP classes and methods** : Call the Agent Platform APIs by using built-in ABAP classes and methods.
  * **Use AI-centric ABAP types** : With AI-centric ABAP types for the input and output parameters, you can prepare inputs and parse outputs from the methods.
  * **Receive formatted responses** : Receive formatted responses from the Agent Platform API in an ABAP-friendly format that you can directly incorporate into your SAP business logic.
  * **Configure parameters centrally** : Configure the Agent Platform parameters once against a client key and large language model (LLM), and reuse these configurations for Agent Platform API calls. This approach reduces the amount of repetitive configuration code you need to write for subsequent API calls.



## Get started with the Agent Platform SDK for ABAP

To get started with the Agent Platform SDK for ABAP in your SAP environment, choose your edition:

### SAP BTP edition

###  [ Quick prototyping with Gemini ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/quick-prototyping-with-gemini)

Prototype and test generative AI features in SAP. 

###  [ Generative AI on Agent Platform for SAP ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/vertex-ai-for-sap-overview)

Learn about generative AI on Agent Platform and build scalable applications for SAP. 

### On-premises or any cloud edition

###  [ Quick prototyping with Gemini ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/quick-prototyping-with-gemini)

Prototype and test generative AI features in SAP. 

###  [ Generative AI demos for SAP ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/demos/demos-overview)

Run the built-in demo programs to explore how generative AI can assist you in creating solutions in your SAP environment. 

###  [ Generative AI on Agent Platform for SAP ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/vertex-ai-for-sap-overview)

Learn about generative AI on Agent Platform and build scalable applications for SAP. 

## Pricing

The Agent Platform SDK for ABAP is offered at no cost. However, you are responsible for the charges that result from your use of Google Cloud services, such as the Gemini API or the Agent Platform API.

For [quick prototyping with Gemini](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/quick-prototyping-with-gemini), you use the Gemini API and Google AI Studio. When you access the Gemini API through Google AI Studio, the Gemini API has both free and paid pricing tiers. However, the free tier of the Gemini API is not available in all regions. For information about the regions where you can access the free and paid tiers of the Gemini API, see [Available regions for Google AI Studio and Gemini API](https://ai.google.dev/gemini-api/docs/available-regions). For information about other restrictions, see [Use restrictions](https://ai.google.dev/gemini-api/terms#use-restrictions). For information about pricing and rate limits, see [Pricing models](https://ai.google.dev/pricing).

Agent Platform pricing follows a pay-as-you-go model, which means you're charged based on the resources you consume. For information about pricing, see [Agent Platform pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

For information about pricing for partner models, see [Anthropic Claude pricing on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing#partner-models-on-agent-platform).

For information about how Gemini with Agent Platform is different from Gemini with Google AI Studio, see [Google AI versus Agent Platform differences](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/migrate/migrate-google-ai#google-ai).

## Additional resources

Explore additional resources for generative AI:

### Get started with generative AI on Agent Platform

  * Learn about [generative AI on Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/overview).
  * Learn about [responsible AI best practices and Agent Platform safety filters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai).
  * Read the [Gemini API FAQ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/resources/faq).



### Design and manage your prompts

  * Learn about [prompt design](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * Learn about [common prompting strategies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies) that you can use to affect the model's responses.
  * View [sample prompts in Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agent-studio/quickstart#about-prompts).



## Community resources for building AI-powered ABAP applications

To help you get the most out of the Agent Platform SDK for ABAP, you can explore the following community resources:

### Build your RAG application with Agent Platform and Gemini

Accelerate your [retrieval-augmented generation (RAG)](https://cloud.google.com/use-cases/retrieval-augmented-generation) application development with this [handbook available on GitHub](https://github.com/google-cloud-abap/demo-hpro/blob/main/hpro-guide/%5BGuide%5D%20Vertex%20AI%20SDK%20for%20ABAP.pdf). With an end-to-end sample enterprise use case of warehouse operations, this handbook illustrates how to build your own RAG application by using the Agent Platform SDK for ABAP and prebuilt components from the [GitHub repository](https://github.com/google-cloud-abap/demo-hpro/tree/main).

### Learn how to use generative AI in SAP business applications with Gemini

The following video shows how you can use Gemini to transform your SAP business applications with generative AI.

### Integrate AI features into your ABAP editor

You can use a community-driven sample solution available on GitHub that offers features such as code explanation, code review, and ABAP unit test generation. This solution lets you integrate Gemini's advanced AI capabilities into your ABAP editor by using the Agent Platform SDK for ABAP. For more information, see the [Genie for SAP](https://github.com/google/genie-for-sap-abap-ai-assistant-sample/tree/main) GitHub page.

This solution is for reference only and isn't intended for direct use in a production environment.

Because this solution is a community resource, Google Cloud does not offer support for it. For assistance from the community, raise an issue on the [Issues](https://github.com/google/genie-for-sap-abap-ai-assistant-sample/issues) GitHub page.

## What's next

  * SAP BTP edition of ABAP SDK for Google Cloud: Learn how to [install and configure the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap).
  * On-premises or any cloud edition of ABAP SDK for Google Cloud: Learn how to [install and configure the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap).
  * Explore the built-in [Generative AI demo programs for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/demos/demos-overview).
  * Learn about [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/vertex-ai-for-sap-overview).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
