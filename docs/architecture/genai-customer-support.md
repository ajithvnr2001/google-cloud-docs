---
url: https://docs.cloud.google.com/architecture/genai-customer-support/
title: Generative AI use case: Generate solutions for customer-support questions \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:09.744860+00:00
---

# Generative AI use case: Generate solutions for customer-support questions  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/genai-customer-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Generative AI use case: Generate solutions for customer-support questions Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-12-16 UTC

This document provides a high-level architecture for an application that uses AI to generate solutions for support questions from customers.

The intended audience for this document includes architects, developers, and administrators who build and manage generative AI applications in the cloud. The document assumes that you have a foundational understanding of [generative AI](https://docs.cloud.google.com/docs/generative-ai/glossary#generative-ai).

The Deployment section of this document provides code samples for AI-assisted customer support use cases.

## Architecture

The following diagram shows an architecture for an AI-assisted support desk application in Google Cloud. The application receives questions from customers, retrieves relevant resources from a knowledge base, and then it generates solutions for the questions. The architecture is an implementation of the [retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary/#retrieval-augmented_generation) approach.

![Architecture for an application that uses AI to generate responses to support requests from customers.](https://docs.cloud.google.com/static/architecture/images/genai-customer-support-architecture.png)![Architecture for an application that uses AI to generate responses to support requests from customers.](https://docs.cloud.google.com/static/architecture/images/genai-customer-support-architecture.png)

The application in this architecture consists of containerized services that are deployed in a Google Kubernetes Engine (GKE) cluster. The architecture shows the following flow:

  1. A customer submits a question to the support desk application.
  2. The support desk application passes the customer's question to the knowledge retriever service.
  3. The knowledge retriever service constructs and sends a prompt to Gemini API to retrieve resources that are relevant to the customer's question.
  4. Gemini identifies relevant resources from a support knowledge base that's stored in Cloud Storage.
  5. Gemini returns the IDs of the relevant resources to the knowledge retriever service.
  6. The knowledge retriever service retrieves the relevant resources from Cloud Storage.
  7. The knowledge retriever service sends the customer's question and relevant resources to the solution generator service.
  8. The solution generator service sends the resources to Gemini API, with a prompt to generate a detailed solution for the customer's question.
  9. Gemini generates a solution, such as step-by-step instructions or a video walkthrough.
  10. The solution generator service provides the solution to the customer through the support desk application.



## Products used

This example architecture uses the following Google Cloud products:

  * [ Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Deployment

To experiment with AI-assisted customer support applications in Google Cloud, use the following code samples:

  * [Build a customer support application that uses generative AI](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/customer-support/customer_support_gemini_genai_sdk.ipynb).
  * [Sample prompt for AI-assisted customer service use cases](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/prompt-gallery/samples/answer_question_customer_service_assistance).



## What's next

  * [Build a customer support agent using Gemini](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/gemini/multimodal-live-api/native-audio-websocket-demo-apps/customer-support-demo-app).
  * Build AI agents for customer support use cases by using [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook), [flows](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow), and [data stores](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) in Dialogflow CX.
  * Explore more [generative AI architecture guides](https://docs.cloud.google.com/architecture/ai-ml#generative_ai).
  * For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer

Other contributors: 

  * [Amina Mansour](https://www.linkedin.com/in/aminamansour/) | Tech Lead, Global Developer Relations & Strategic Content
  * [Megan O'Keefe](https://www.linkedin.com/in/askmeegs) | Developer Advocate
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer
  * [Shir Meir Lador](https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
