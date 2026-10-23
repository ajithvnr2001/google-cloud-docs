---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights/
title: Smart highlights \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:31.499716+00:00
---

# Smart highlights  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Smart highlights Stay organized with collections  Save and categorize content based on your preferences. 

Smart highlights automatically detects highlights in a contact center conversation without requiring any additional configuration. A conversation's highlights are the words or phrases that were important for determining the end user's intent. This feature analyzes each conversation turn and categorizes the user's intention, then labels any highlights present in a conversation.

## How it works

Customer Experience Insights uses [Dialogflow intent](https://docs.cloud.google.com/dialogflow/es/docs/intents-overview) technology to detect conversation highlights at the sentence level. When Customer Experience Insights detects a highlight, it creates a [call annotation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#Analysis.CallAnnotation) and includes that in the analysis with other annotations.

## Supported smart highlights

Intent | Definition | Example highlight  
---|---|---  
`AUTHENTICATION_INFO` | Asking for information that can be used to authenticate a customer. | Can you please help me with your account number?  
`CHECK_ISSUE_RESOLVED` | Checking if the issue is resolved and there are no further questions or problems. | Have I addressed your concern for today?  
`CONFIRM_ISSUE_RESOLVED` | Confirming the issue was resolved. | All my questions were answered.  
  
## View smart highlights

You can view smart highlights labels in the [Customer Experience Insights console](https://ccai.cloud.google.com/insights) along with other labels, such as detected entities. When you export conversations to BigQuery, Customer Experience Insights automatically includes smart highlights labels in your exporter. This lets you perform a custom inspection of the data.

**Note:** [sentences.intentMatchData](https://docs.cloud.google.com/gemini-enterprise-cx/insights/export#bigquery_schema_data_dictionary_) represents smart highlights in the exporter schema.

## Smart highlights feedback

Smart highlights use natural language processing to identify intents within your conversation. This feature can incorrectly identify phrases or not identify an accurate phrase. If you find a scenario in your data where a smart highlight is not working as described, you can provide feedback with one of the following methods:

  * Use the **Send Feedback** option from the **Help** menu in the Customer Experience Insights console.
  * Reach out directly to the [Customer Experience Insights feedback team](https://docs.cloud.google.com/gemini-enterprise-cx/insights/contact-center-insights-feedback@google.com).



In your feedback, provide the name of the smart highlight, the phrase, and whether the phrase was missed or identified incorrectly.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
