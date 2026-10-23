---
url: https://docs.cloud.google.com/vision-ai/docs/overview/
title: Agent Platform Vision overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:15.914842+00:00
---

# Agent Platform Vision overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/overview/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Agent Platform Vision overview Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise Agent Platform Vision (formerly Vertex AI Vision) is an AI-powered platform to ingest, analyze and store video data. Agent Platform Vision lets users build and deploy applications with a simplified user interface.

Using Agent Platform Vision you can build end-to-end computer image solutions by leveraging Agent Platform Vision's integration with other major components, namely Live Video Analytics, data streams, and Vision Warehouse. The Gemini Enterprise Agent Platform Vision API lets you build a high level app from low level APIs, and create and update a high level workflow that combines multiple individual API calls. You can then execute your workflow as a unit by making a single deploy request to the Agent Platform Vision platform server.

Using Agent Platform Vision, you can:

  * Ingest real-time video data
  * Analyze data for insights using general and custom vision AI models
  * Store insights in Vision Warehouse for simplified querying and metadata information



## Agent Platform Vision workflow

The steps you complete to use Agent Platform Vision are as follows:

  1. **Ingest real-time data**

Agent Platform Vision's architecture lets you quickly and conveniently stream real-time video ingestion infrastructure in a public Cloud.

  2. **Analyze data**

After data is ingested, Agent Platform Vision's framework provides you with straightforward access and orchestration of a large and growing portfolio of _general_ , _custom_ , & _specialized_ analysis models.

  3. **Store and query output**

After your app analyzes your data you can send this information to a storage destination (Vision Warehouse or BigQuery), or receive the data live. With Vision Warehouse you can send your app output to a warehouse that generalizes your search work and serves multiple data types and use cases.


![Gemini Enterprise Agent Platform Vision application graph displayed in the Google Cloud console.](https://docs.cloud.google.com/static/vision-ai/docs/images/vision-ai-graph.png)_A graph for a Agent Platform Vision occupancy analytics app in the Google Cloud console_

## A note on Responsible AI

At Google Cloud, we prioritize helping customers safely develop and implement solutions using Gemini Enterprise Agent Platform Vision. For Gemini Enterprise Agent Platform Vision, we've worked to develop fair and equitable performance in accordance with [Google's AI Principles](https://ai.google/principles/).

This work includes testing for bias during development, for example looking at performance across different skin tones, and developing product features to enhance privacy and limit personal identification, like person and face blur. We are committed to iterating and improving, and we will continue to incorporate best practices and lessons learned into our Vertex AI products.

When Gemini Enterprise Agent Platform Vision is integrated into a customer's unique organizational context, there are likely to be additional responsible AI considerations. We encourage customers to leverage fairness, interpretability, privacy and security [best practices](https://ai.google/responsibilities/responsible-ai-practices/?category=general) when implementing Gemini Enterprise Agent Platform Vision, especially when building custom or AutoML trained models. Throughout this technical documentation, we have provided additional guidance and resources to support this work. To learn more, read about Google's recommendations for [Responsible AI practices](https://ai.google/responsibilities/responsible-ai-practices/?category=general).

## What's next

  * Read more in the blog post ["Vertex AI Vision: Easily build and deploy computer vision applications at scale"](https://cloud.google.com/blog/products/ai-machine-learning/computer-vision-for-vertex-ai).
  * Learn details about specific models in the [Occupancy analytics guide](https://docs.cloud.google.com/vision-ai/docs/occupancy-analytics-model), [Person blur guide](https://docs.cloud.google.com/vision-ai/docs/person-blur-model), [Person/vehicle detector guide](https://docs.cloud.google.com/vision-ai/docs/person-vehicle-model), or [Motion filtering guide](https://docs.cloud.google.com/vision-ai/docs/motion-filtering-model).
  * Try Agent Platform Vision in the Google Cloud console by reading the [Build an app in the console](https://docs.cloud.google.com/vision-ai/docs/build-app-console-quickstart) quickstart.
  * [Set up your local environment](https://docs.cloud.google.com/vision-ai/docs/cloud-environment) to use Agent Platform Vision.



[ Next Quickstart: Build an app in the console  arrow_forward  ](https://docs.cloud.google.com/vision-ai/docs/build-app-console-quickstart)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
