---
url: https://docs.cloud.google.com/architecture/genai-marketing-campaigns/
title: Generative AI use case: Generate content for personalized marketing campaigns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:32.001046+00:00
---

# Generative AI use case: Generate content for personalized marketing campaigns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/genai-marketing-campaigns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Generative AI use case: Generate content for personalized marketing campaigns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-04 UTC

This document provides a high-level architecture for an application that uses AI to generate content for personalized marketing campaigns.

The intended audience for this document includes architects, developers, and administrators who build and manage generative AI applications in the cloud for the media and marketing industries. The document assumes that you have a foundational understanding of [generative AI](https://docs.cloud.google.com/docs/generative-ai/glossary#generative-ai).

The Deployment section of this document provides links to code samples to help you experiment with deploying generative AI applications for marketing use cases.

## Architecture

The following diagram shows an architecture for an application in Google Cloud that processes user data to generate media assets for personalized marketing campaigns.

![Architecture for a generative AI application that generates personalized marketing campaigns.](https://docs.cloud.google.com/static/architecture/images/genai-marketing-campaigns-architecture.png)![Architecture for an application that uses AI to generate personalized marketing campaigns.](https://docs.cloud.google.com/static/architecture/images/genai-marketing-campaigns-architecture.png)

The architecture shows the following flows:

  * **Ingest and process user data** :

    1. User data from sources within Google Cloud and from external sources is uploaded to BigQuery.
    2. A Dataflow pipeline processes the uploaded data and derives marketing insights, such as demographic profiles, interests, and purchasing patterns.
    3. Eventarc triggers a Cloud Run service.
    4. The Cloud Run service sends the marketing insights to Gemini Enterprise Agent Platform, with a prompt to generate personalized media assets for marketing campaigns.
    5. For each user, the Gemini model on Agent Platform generates audio, video, and text content for online marketing campaigns.
    6. The Cloud Run service uploads the generated content to a content-server bucket in Cloud Storage.
  * **Serve marketing content** :

When users visit the company web portal (hosted on Cloud Run), the portal service does the following:

    1. Retrieves user-specific marketing content from the Cloud Storage content server.
    2. Displays the marketing content on the web pages that users visit.



To improve the quality of the content that's generated, consider the following adjustments to the architecture:

  * Build a feedback loop that enables the model to learn from the impact of the marketing campaigns.
  * Include a human review step before generated content is uploaded to Cloud Storage to verify that the content aligns with safety guidelines and brand standards.



## Products used

This example architecture uses the following Google Cloud products:

  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 
  * [ BigQuery](https://cloud.google.com/bigquery): An enterprise data warehouse that helps you manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence. 
  * [ Dataflow](https://cloud.google.com/dataflow): A service that provides unified stream and batch data processing at scale. 
  * [ Eventarc](https://docs.cloud.google.com/eventarc/docs/overview): A serverless solution to asynchronously route messages triggered by events. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.



## Deployment

The [Generative AI for Marketing](https://github.com/GoogleCloudPlatform/genai-for-marketing) repository in GitHub includes code samples that you can use to experiment with deploying generative AI applications for marketing use cases.

## What's next

  * [Generate visuals and copy for marketing campaigns](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/marketing/creative_content_generation.ipynb).
  * Explore more [generative AI architecture guides](https://docs.cloud.google.com/architecture/genai-overview).
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

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
