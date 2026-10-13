---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client
title: Class Client (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:45.231337+00:00
---

# Class Client (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Client (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    Client(
        *,
        api_key: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        debug_config: typing.Optional[google.genai.client.DebugConfig] = None,
        http_options: typing.Optional[
            typing.Union[google.genai.types.HttpOptions, google.genai.types.HttpOptionsDict]
        ] = None
    )

Gen AI Client for the Vertex SDK.

Use this client to interact with Vertex-specific Gemini features.

## Properties 

### agent_engines

API documentation for `agent_engines` property.

### aio

API documentation for `aio` property.

### datasets

API documentation for `datasets` property.

### evals

API documentation for `evals` property.

### prompt_optimizer

API documentation for `prompt_optimizer` property.

### prompts

API documentation for `prompts` property.

### skills

API documentation for `skills` property.

## Methods 

### Client
    
    
    Client(
        *,
        api_key: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        debug_config: typing.Optional[google.genai.client.DebugConfig] = None,
        http_options: typing.Optional[
            typing.Union[google.genai.types.HttpOptions, google.genai.types.HttpOptionsDict]
        ] = None
    )

Initializes the client.

**Parameters**  
---  
**Name** | **Description**  
`api_key` |  `str`   
The `API key  
`credentials` |  `google.auth.credentials.Credentials`   
The credentials to use for authentication when calling the Vertex AI APIs. Credentials can be obtained from environment variables and default credentials. For more information, see `Set up Application Default Credentials <https://cloud.google.com/docs/authentication/provide-credentials-adc>`_.  
`project` |  `str`   
The `Google Cloud project ID <https://cloud.google.com/vertex-ai/docs/start/cloud-environment>`_ to use for quota. Can be obtained from environment variables (for example, `GOOGLE_CLOUD_PROJECT`).  
`location` |  `str`   
The `location <https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations>`_ to send API requests to (for example, `us-central1`). Can be obtained from environment variables.  
`debug_config` |  `DebugConfig`   
Config settings that control network behavior of the client. This is typically used when running test code.  
`http_options` |  `Union[HttpOptions, HttpOptionsDict]`   
Http options to use for the client.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
