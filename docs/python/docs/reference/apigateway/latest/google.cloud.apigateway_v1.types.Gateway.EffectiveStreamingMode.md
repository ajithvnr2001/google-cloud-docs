---
url: https://docs.cloud.google.com/python/docs/reference/apigateway/latest/google.cloud.apigateway_v1.types.Gateway.EffectiveStreamingMode
title: Class EffectiveStreamingMode (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:06.733530+00:00
---

# Class EffectiveStreamingMode (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigateway/latest/google.cloud.apigateway_v1.types.Gateway.EffectiveStreamingMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EffectiveStreamingMode (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.2  1.11.0  1.10.1  1.9.5  1.8.0  1.7.3  1.6.1  1.5.1  1.4.0  1.3.3  1.2.2  1.1.1  1.0.4  0.2.0  0.1.0 
    
    
    EffectiveStreamingMode(value)

The streaming mode a Gateway is served with. This enum is frozen. No values are expected to be added in the future.

## Enums  
  
---  
**Name** | **Description**  
`EFFECTIVE_STREAMING_MODE_UNSPECIFIED` | Indicates that the service has not resolved a mode. Every gateway returned by `GetGateway` and `ListGateways` carries a resolved mode, so this value should not be returned under normal circumstances.  
`EFFECTIVE_STREAMING_MODE_DISABLED` | Indicates that the gateway does not support streaming.  
`EFFECTIVE_STREAMING_MODE_ENABLED` | Indicates that the gateway supports streaming.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
