---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeedbackContext/
title: FeedbackContext \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:34:39.148404+00:00
---

# FeedbackContext  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeedbackContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  FeedbackContext Stay organized with collections  Save and categorize content based on your preferences. 

Feedback context is a resource that represents additional information about the conversation where the feedback was given, such as the conversation history, system instructions, etc. If provided, feedback context allows to correlate the feedback with the conversation, even if the original session is deleted or not available.

Fields  
  
`name` `string` Identifier. The resource name. Assigned by the server on create.Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}/feedbackEntries/{feedbackEntry}/feedbackContext` | `contextEvents[]` `object (`[SessionEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SessionEvent)`)` Optional. The session events from the originating session. | JSON representation  
---  
      
    
    {
      "name": string,
      "contextEvents": [
        {
          object ([SessionEvent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SessionEvent))
        }
      ]
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
