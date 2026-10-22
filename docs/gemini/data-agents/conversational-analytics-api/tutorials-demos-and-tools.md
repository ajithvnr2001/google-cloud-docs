---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/tutorials-demos-and-tools/
title: Conversational Analytics API tutorials, demos, and tools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:20.180041+00:00
---

# Conversational Analytics API tutorials, demos, and tools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/tutorials-demos-and-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API tutorials, demos, and tools Stay organized with collections  Save and categorize content based on your preferences. 

To help you build and evaluate data agents with the Conversational Analytics API, this page provides links to guided tutorials, interactive demos, sample applications, and development tools.

## Interactive tutorials

This section links to codelabs, interactive Colaboratory notebooks, and blog posts that provide step-by-step guidance to help you learn core API concepts.

Resource | Description | Format  
---|---|---  
[Introduction to the Conversational Analytics API](https://codelabs.developers.google.com/ca-api-bigquery) | Follow a step-by-step tutorial to learn how to use the Python SDK with a BigQuery data source, how to create a new agent by using the Conversational Analytics API, how to create and manage conversations, and how to send and stream responses from the API. | Codelab  
[Build a chat app with the Conversational Analytics API for Looker and BigQuery](https://codelabs.developers.google.com/codelabs/looker-ca-api) | Learn how to use the Conversational Analytics API with Looker and BigQuery to build a chat application, including how to set up the Streamlit Quickstart app, and learn about the benefits of Looker for semantic modeling. | Codelab  
[HTTP Colaboratory notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_http.ipynb) | Explore an interactive, step-by-step guide to setting up your environment, building a data agent, and making API calls by using HTTP requests. | Notebook  
[Python SDK Colaboratory notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb) | Explore an interactive, step-by-step guide to setting up your environment, building a data agent, and making API calls by using the Python SDK. | Notebook  
[Blog: Building a conversational agent in BigQuery using the Conversational Analytics API](https://cloud.google.com/blog/products/data-analytics/build-data-agents-with-conversational-analytics-api) | Learn to build a BigQuery conversational agent by using the Python SDK, with guidance on setup, stateful conversations, and streaming responses. | Blog  
  
## Sample applications and demos

This section links to sample applications and video demonstrations that showcase the API's capabilities.

### Sample apps and videos

The following resources demonstrate how to integrate the Conversational Analytics API in various environments and provide overviews of API features:

  * [Streamlit Quickstart app](https://github.com/looker-open-source/ca-api-quickstarts): Learn how to integrate with the Conversational Analytics API in a local test environment.
  * [Conversational Analytics demos and tools](https://github.com/looker-open-source/ca-demos-and-tools): Review demos and tools that showcase Conversational Analytics API capabilities and provide practical integration patterns.
  * [YouTube: Conversational Analytics API](https://www.youtube.com/watch?v=c3WSg0Bpmt4): Learn about the Conversational Analytics API, including how the API processes natural language questions, connects to data sources such as BigQuery and Looker, and returns results as text or visualizations.
  * [YouTube: Embed analytics experiences in your applications using the Conversational Analytics API](https://www.youtube.com/watch?v=p-MguQf84Tg): Learn about the Conversational Analytics API and how to build a Conversational Analytics API agent by using the Agent Development Kit (ADK).



## SDKs and development tools

This section provides links to client libraries, the Agent Development Kit (ADK), the MCP Toolbox, and other tools for building, managing, and evaluating data agents.

### Client libraries

Installation instructions and reference documentation are available for the following Conversational Analytics API client libraries:

  * [.NET (v1beta)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest)
  * [Go (v1beta)](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/geminidataanalytics/latest/apiv1beta)
  * [Node.js](https://www.npmjs.com/package/@google-cloud/geminidataanalytics)
  * [PHP (v1beta)](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest)
  * [Python (v1beta)](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest)
  * [Ruby (v1beta)](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/overview)



### Agent Development Kit (ADK)

The [Agent Development Kit (ADK)](https://adk.dev/) includes tools for building and managing Conversational Analytics API data agents:

  * [`ask_data_agent`](https://adk.dev/integrations/data-agent/): Ask natural language questions of a pre-configured data agent by referencing the agent's ID.
  * [`ask_data_insights`](https://adk.dev/integrations/bigquery/): Generate natural language data insights from sources such as BigQuery with a stateless API call that doesn't require a data agent.



### MCP Toolbox for Databases

The [MCP Toolbox for Databases](https://mcp-toolbox.dev/documentation/introduction/) is an open-source MCP server that connects AI agents, IDEs, and applications to data sources. It wraps the Conversational Analytics API as MCP-compatible tools that enable interaction with services such as BigQuery and Looker.

The toolbox includes MCP-compatible tools for the following services:

  * [BigQuery Conversational Analytics tool](https://mcp-toolbox.dev/integrations/bigquery/tools/bigquery-conversational-analytics/) (`bigquery-conversational-analytics`)
  * [Looker Conversational Analytics tool](https://mcp-toolbox.dev/integrations/looker/tools/looker-conversational-analytics/) (`looker-conversational-analytics`)



### Other development tools

The following tool can assist with other development tasks, such as agent evaluation:

  * [Prism](https://github.com/looker-open-source/ca-demos-and-tools/blob/main/ca-agent-ops-prism/README.md): Use this open-source application to monitor and evaluate AI agent performance, run test suites, and capture traces.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
