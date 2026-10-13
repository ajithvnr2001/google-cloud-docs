---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettingsOrBuilder
title: Interface ErrorHandlingSettingsOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:37.957101+00:00
---

# Interface ErrorHandlingSettingsOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ErrorHandlingSettingsOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ErrorHandlingSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEndSessionConfig()
    
    
    public abstract ErrorHandlingSettings.EndSessionConfig getEndSessionConfig()

Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).

` .google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig end_session_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig)` | The endSessionConfig.  
  
### getEndSessionConfigOrBuilder()
    
    
    public abstract ErrorHandlingSettings.EndSessionConfigOrBuilder getEndSessionConfigOrBuilder()

Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).

` .google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig end_session_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings.EndSessionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfigOrBuilder)` |   
  
### getErrorHandlingStrategy()
    
    
    public abstract ErrorHandlingSettings.ErrorHandlingStrategy getErrorHandlingStrategy()

Optional. The strategy to use for error handling.

` .google.cloud.ces.v1.ErrorHandlingSettings.ErrorHandlingStrategy error_handling_strategy = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettings.ErrorHandlingStrategy)` | The errorHandlingStrategy.  
  
### getErrorHandlingStrategyValue()
    
    
    public abstract int getErrorHandlingStrategyValue()

Optional. The strategy to use for error handling.

` .google.cloud.ces.v1.ErrorHandlingSettings.ErrorHandlingStrategy error_handling_strategy = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for errorHandlingStrategy.  
  
### getFallbackResponseConfig()
    
    
    public abstract ErrorHandlingSettings.FallbackResponseConfig getFallbackResponseConfig()

Optional. Configuration for handling fallback responses.

` .google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig fallback_response_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig)` | The fallbackResponseConfig.  
  
### getFallbackResponseConfigOrBuilder()
    
    
    public abstract ErrorHandlingSettings.FallbackResponseConfigOrBuilder getFallbackResponseConfigOrBuilder()

Optional. Configuration for handling fallback responses.

` .google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig fallback_response_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings.FallbackResponseConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfigOrBuilder)` |   
  
### hasEndSessionConfig()
    
    
    public abstract boolean hasEndSessionConfig()

Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).

` .google.cloud.ces.v1.ErrorHandlingSettings.EndSessionConfig end_session_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endSessionConfig field is set.  
  
### hasFallbackResponseConfig()
    
    
    public abstract boolean hasFallbackResponseConfig()

Optional. Configuration for handling fallback responses.

` .google.cloud.ces.v1.ErrorHandlingSettings.FallbackResponseConfig fallback_response_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fallbackResponseConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
