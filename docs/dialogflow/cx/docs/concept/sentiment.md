---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment/
title: Sentiment analysis \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:55.984054+00:00
---

# Sentiment analysis  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Sentiment analysis Stay organized with collections  Save and categorize content based on your preferences. 

Sentiment analysis inspects end-user input and identifies the prevailing subjective opinion, especially to determine an end-user's attitude as positive, negative, or neutral. When making a detect intent request, you can specify that sentiment analysis be performed, and the response will contain sentiment analysis values.

## Supported languages

For a list of supported languages, see the **sentiment** column on the [language reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language). If you request sentiment analysis for an unsupported language, your detect intent request does not fail, but the `QueryResult.diagnostic_info` field contains error information.

## Detect intent

Using the API, you can request sentiment analysis for each `detectIntent` or `streamingDetectIntent` call by setting the `analyzeQueryTextSentiment` field to true. The response contains a `sentimentAnalysisResult` field with `score` and `magnitude` values.

## Using sentiment in conditions

You can use sentiment analysis results via the request-scoped parameters when defining a condition.

For more information, see the [sentiment analysis parameters descriptions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#request-scoped-sentiment), and [Conditions reference](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#request-scoped) for how the parameters can be used in conditions.

## Using sentiment in the simulator

You can enable sentiment analysis when using the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator-settings).

[ Previous arrow_back  Git export/restore  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github)

[ Next Using multiple projects  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/multi-project)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
