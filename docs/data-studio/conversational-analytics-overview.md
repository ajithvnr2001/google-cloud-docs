---
url: https://docs.cloud.google.com/data-studio/conversational-analytics-overview/
title: Conversational Analytics in Data Studio overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:18.376245+00:00
---

# Conversational Analytics in Data Studio overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/conversational-analytics-overview/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Conversational Analytics in Data Studio overview Stay organized with collections  Save and categorize content based on your preferences. 

Conversational Analytics is a chat with your data feature powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview). Conversational Analytics empowers users with no expertise in business intelligence to ask data-related questions in regular, natural (conversational) language, and go beyond static dashboards.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Key features

Conversational Analytics includes the following key features:

  * [**Talk to your data**](https://docs.cloud.google.com/data-studio/conversational-analytics-data): Converse in natural language with [supported data sources](https://docs.cloud.google.com/data-studio/conversational-analytics-setup#supported-data-sources) or with a custom data agent that was [created in BigQuery](https://docs.cloud.google.com/bigquery/docs/create-data-agents).
  * [**Create and manage data agents**](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents): With data agents, you can customize the AI-powered data querying agent by providing context and instructions that are specific to your data, which helps Conversational Analytics generate more accurate and contextually relevant responses. You can also share your data agents with other users so that they can ask questions with the same context.
  * [**Enable advanced analytics with the Code Interpreter**](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter): The Code Interpreter within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the Code Interpreter's use of Python enables more complex analysis and visualizations. Use of the Code Interpreter requires that [Gemini in Data Studio is enabled](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio) for a Data Studio Pro subscription.



## Legacy experience versus new experience

Conversational Analytics has a new experience that makes conversing with data agents and BigQuery data sources available to more users across Data Studio. For a time you can switch between the "new" and "legacy" experiences to maintain access to the conversations and data agents that you used with legacy Conversational Analytics, but you won't be able to migrate your legacy conversations or data agents to the new Conversational Analytics experience.

The following table summarizes the key differences between the two experiences:

Category | Legacy Conversational Analytics | New Conversational Analytics  
---|---|---  
Supported data sources | CSV, Sheets, Looker, BigQuery data sources or agents | BigQuery data agents  
Availability | Available only to users of a Data Studio Pro (née Looker Studio Pro) subscription, with Gemini in Data Studio (née Gemini in Looker) enabled | Available to all Data Studio users (use of the Code Interpreter still requires Gemini in Data Studio and a Data Studio Pro subscription)  
Agents | Chat with the agents that you created in Data Studio (née Looker Studio) based on CSV, Sheets, Looker, or BigQuery data sources. You won't be able to migrate these agents or conversations to the new experience. | Chat with the agents that you or other users create in BigQuery and share to Data Studio. You cannot create data agents within Data Studio.  
  
## List of documentation

  * [Set up Conversational Analytics in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-setup)
  * [Converse with Data Studio data](https://docs.cloud.google.com/data-studio/conversational-analytics-data)
  * [Data agents in Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-data-agents)
  * [Enable and use the Code Interpreter](https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter)



## Provide feedback

You can provide feedback to Google about individual responses in Conversational Analytics by selecting one of the following options:

  * thumb_up **Good response** : Indicate that the response was helpful.
  * thumb_down **Bad response** : Indicate that the response was not helpful.

**Note:** Gemini in Data Studio features are in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [data-studio-ca AT google.com](mailto:data-studio-ca@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
