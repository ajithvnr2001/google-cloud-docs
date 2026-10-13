---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest
title: Class GenerateStatelessSummaryRequest (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:01.123860+00:00
---

# Class GenerateStatelessSummaryRequest (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerateStatelessSummaryRequest (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    GenerateStatelessSummaryRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The request message for Conversations.GenerateStatelessSummary.

## Attributes  
  
---  
**Name** | **Description**  
`stateless_conversation` |  `[google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest.MinimalConversation](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest.MinimalConversation)`   
Required. The conversation to suggest a summary for.   
`conversation_profile` |  `[google.cloud.dialogflow_v2beta1.types.ConversationProfile](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.ConversationProfile)`   
Required. A ConversationProfile containing information required for Summary generation. Required fields: {language_code, security_settings} Optional fields: {agent_assistant_config}   
`latest_message` |  `str`   
Optional. The name of the latest conversation message used as context for generating a Summary. If empty, the latest message of the conversation will be used. The format is specific to the user and the names of the messages provided.   
`max_context_size` |  `int`   
Optional. Max number of messages prior to and including [latest_message] to use as context when compiling the suggestion. By default 500 and at most 1000.   
  
## Classes 

### MinimalConversation
    
    
    MinimalConversation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The minimum amount of information required to generate a Summary without having a Conversation resource created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
