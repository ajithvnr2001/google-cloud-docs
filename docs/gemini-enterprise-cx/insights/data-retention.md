---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/data-retention/
title: Data retention in Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:14.981761+00:00
---

# Data retention in Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/data-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Data retention in Customer Experience Insights Stay organized with collections  Save and categorize content based on your preferences. 

For general data deletion information, see the [Google Cloud data deletion policy](https://docs.cloud.google.com/docs/security/deletion).

Customer Experience Insights deletes data processed through the [console](https://ccai.cloud.google.com/insights/projects/global/locations/global/highlights) after the following amounts of time, depending on the data type.

CX Insights also uses generative AI models for some of its features, which have their own [data governance policies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/data-governance).

CX Insights abides by the following logical deletion policies for each data type:

  * **Conversations** : When you delete a conversation from either the **Conversation Hub** or the **Conversations** tab in Quality AI, you also remove it from the CX Insights databases. Your deletion immediately removes all analysis results related to the conversation, such as highlights, sentiment, topic annotations, and Quality AI scores.
  * **Topic models** : When you create a topic model,CX Insights keeps the topic model until you request to delete it. CX Insights removes topic models and topics only when you request their deletion.
  * **Quality AI scorecards** : When you create a Quality AI scorecard, CX Insights keeps the scorecard until you request to delete it. CX Insights removes Quality AI scorecards and questions only when you request their deletion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
