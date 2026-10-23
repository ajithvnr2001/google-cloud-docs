---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/export-conversations/
title: Export conversation data \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:23.937196+00:00
---

# Export conversation data  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/export-conversations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Export conversation data Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can export conversation messages to a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket. Each conversation is exported as a separate JSON file in the [standard conversation data format](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-data-format#conversation_transcript_data). A maximum of 10,000 conversations can be exported at a time, and each conversation can have at most 1000 messages.

## Authentication and access control

When you send a request to export conversations, use your [end-user credentials for authentication](https://docs.cloud.google.com/docs/authentication/end-user). Your user account must be granted at least a **read** role for the Dialogflow API and an **edit** role (with the ability to overwrite objects) for the Cloud Storage bucket you want to export data to. For more details on user account roles see the [Cloud Storage access control](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) and [Dialogflow access control](https://docs.cloud.google.com/dialogflow/docs/access-control) documentation.

When executing REST requests at the command-line:

  * Use [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) to authenticate `gcloud` with your user account.
  * Use [`gcloud auth print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/print-access-token) to create a token for request authentication.



## Conversations available for export

Only conversations that have been [completed](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/pgka#complete_the_conversation) are available for export. Old conversations are deleted by the system periodically, so if you try to reference an older conversation it may no longer be available.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
