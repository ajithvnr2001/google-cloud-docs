---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.LlmPolicyOrBuilder
title: Interface Guardrail.LlmPolicyOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:55.335577+00:00
---

# Interface Guardrail.LlmPolicyOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.LlmPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Guardrail.LlmPolicyOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface Guardrail.LlmPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAllowShortUtterance()
    
    
    public abstract boolean getAllowShortUtterance()

Optional. By default, the LLM policy check is bypassed for short utterances. Enabling this setting applies the policy check to all utterances, including those that would normally be skipped.

`bool allow_short_utterance = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowShortUtterance.  
  
### getFailOpen()
    
    
    public abstract boolean getFailOpen()

Optional. If an error occurs during the policy check, fail open and do not trigger the guardrail.

`bool fail_open = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The failOpen.  
  
### getMaxConversationMessages()
    
    
    public abstract int getMaxConversationMessages()

Optional. When checking this policy, consider the last 'n' messages in the conversation. When not set a default value of 10 will be used.

`int32 max_conversation_messages = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxConversationMessages.  
  
### getModelSettings()
    
    
    public abstract ModelSettings getModelSettings()

Optional. Model settings.

` .google.cloud.ces.v1beta.ModelSettings model_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ModelSettings)` | The modelSettings.  
  
### getModelSettingsOrBuilder()
    
    
    public abstract ModelSettingsOrBuilder getModelSettingsOrBuilder()

Optional. Model settings.

` .google.cloud.ces.v1beta.ModelSettings model_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ModelSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.ModelSettingsOrBuilder)` |   
  
### getPolicyScope()
    
    
    public abstract Guardrail.LlmPolicy.PolicyScope getPolicyScope()

Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.

` .google.cloud.ces.v1beta.Guardrail.LlmPolicy.PolicyScope policy_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.LlmPolicy.PolicyScope)` | The policyScope.  
  
### getPolicyScopeValue()
    
    
    public abstract int getPolicyScopeValue()

Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.

` .google.cloud.ces.v1beta.Guardrail.LlmPolicy.PolicyScope policy_scope = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for policyScope.  
  
### getPrompt()
    
    
    public abstract String getPrompt()

Required. Policy prompt.

`string prompt = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The prompt.  
  
### getPromptBytes()
    
    
    public abstract ByteString getPromptBytes()

Required. Policy prompt.

`string prompt = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for prompt.  
  
### hasModelSettings()
    
    
    public abstract boolean hasModelSettings()

Optional. Model settings.

` .google.cloud.ces.v1beta.ModelSettings model_settings = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelSettings field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
