---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Environment
title: Class Environment (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:56.358548+00:00
---

# Class Environment (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Environment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Environment (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    Environment(mapping=None, *, ignore_unknown_fields=False, **kwargs)

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the `versions and environments guide <https://cloud.google.com/dialogflow/docs/agents-versions>`__.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The unique identifier of this agent environment. Supported formats: \- `projects/` \- `projects/`  
`description` |  `str`   
Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected.   
`agent_version` |  `str`   
Optional. The agent version loaded into this environment. Supported formats: \- `projects/` \- `projects/`  
`state` |  `[google.cloud.dialogflow_v2beta1.types.Environment.State](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Environment.State)`   
Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods.   
`text_to_speech_settings` |  `[google.cloud.dialogflow_v2beta1.types.TextToSpeechSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.TextToSpeechSettings)`   
Optional. Text to speech settings for this environment.   
`fulfillment` |  `[google.cloud.dialogflow_v2beta1.types.Fulfillment](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.Fulfillment)`   
Optional. The fulfillment settings to use for this environment.   
  
## Classes 

### State
    
    
    State(value)

Represents an environment state. When an environment is pointed to a new agent version, the environment is temporarily set to the `LOADING` state. During that time, the environment keeps on serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the `RUNNING` state.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
