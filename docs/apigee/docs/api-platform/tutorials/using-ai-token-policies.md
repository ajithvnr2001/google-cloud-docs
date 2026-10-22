---
url: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies/
title: Get started with LLM token policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:58.341811+00:00
---

# Get started with LLM token policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/tutorials/using-ai-token-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Get started with LLM token policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Overview

Apigee's LLM token policies are crucial for cost control, performance optimization, and platform stability, leveraging LLM token usage and user prompt token metrics to enforce limits and provide real-time monitoring.

This document describes how to get started with the following LLM token policies:

  * **[PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy)** : Protects targets from token abuse by throttling tokens based on the user prompt message. The PromptTokenLimit policy is like a spike arrest for your AI prompts. It helps you control the rate of token usage from user prompts to prevent abuse and ensure your backend services are not overwhelmed. 
  * **[LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy)** : Controls LLM expenditures and applies granular quota management based on API products. The LLMTokenQuota policy allows you to enforce token consumption limits for your LLM APIs over a specific time period (e.g., per minute, hour, day, or month). This is crucial for managing costs and ensuring fair usage of your AI services. 



## PromptTokenLimit policy

Use the [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) when you want to protect your backend services from sudden spikes in token usage from user prompts. For example, you can limit the number of tokens per minute to a reasonable number to prevent a single user from overwhelming your service. 

Add this policy to the request flow of your API proxy.

The following PromptTokenLimit policy example limits the token rate to 1,000 tokens per minute: 
    
    
    <PromptTokenLimit continueOnError="false" enabled="true" name="PTL-limitTokens-1">
      <DisplayName>Limit Prompt Tokens</DisplayName>
      <!-- The rate at which to limit tokens. Here, 1,000 per minute -->
      <Rate>1000pm</Rate>
      <!-- Specifies where to get the user's prompt from the request -->
      <UserPromptSource>{jsonPath('$.contents[-1].parts[-1].text',request.content,true)}</UserPromptSource>
    </PromptTokenLimit>

Where:

  * [`<Rate>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy#rate): The rate at which to limit tokens.
  * [`<UserPromptSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy#userpromptsource): Specifies where to get the user's prompt from the request.



See the [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy) reference page for:

  * [Examples](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy#samples)
  * [Flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy#variables)
  * [Error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy#errors)



Configure the PromptTokenLimit policy in the Apigee UI when performing the following tasks:

  * [Create an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add)
  * [Creating an API proxy using the UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#creatinganapiproxyintheedgemanagementui)
  * [ Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui)



## LLMTokenQuota policy

Use the [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) when you want to set and enforce token consumption quotas for different API products, developers, or apps. For example, you can offer different token quotas for different subscription tiers. 

The policy can be used in two main ways:

  * **Counting Tokens** : Use the `CountOnly` setting to track token usage without enforcing a hard limit. This is useful for monitoring and reporting. 
  * **Enforcing Quotas** : Use the `EnforceOnly` setting to reject API calls once the token quota has been exceeded. 



Add an `EnforceOnly` policy to the request flow to check if the quota has been exceeded. Add a `CountOnly` policy to the response flow to count the tokens used in the LLM response.

The following LLMTokenQuota policy example enforces a quota of 10,000 tokens per hour, with the settings dynamically sourced from an API product: 
    
    
    <LLMTokenQuota name="Quota-Enforce-Only" type="rollingwindow">
      <EnforceOnly>true</EnforceOnly>
      <!-- The interval and time unit for the quota -->
      <Interval ref="verifyapikey.verify-api-key.apiproduct.developer.llmQuota.interval">1</Interval>
      <TimeUnit ref="verifyapikey.verify-api-key.apiproduct.developer.llmQuota.timeunit">hour</TimeUnit>
      <!-- The number of tokens allowed in the interval -->
      <Allow count="10000" countRef="verifyapikey.verify-api-key.apiproduct.developer.llmQuota.limit"/>
      <!-- Specifies where to get the token usage from the LLM's response -->
      <LLMTokenUsageSource>{jsonPath('$.usageMetadata.candidatesTokenCount',response.content,true)}</LLMTokenUsageSource>
      <!-- Specifies where to get the model name from the LLM's response -->
      <LLMModelSource>{jsonPath('$.model',response.content,true)}</LLMModelSource>
    </LLMTokenQuota>

Where:

  * [`<EnforceOnly>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#enforceonly): When set to `true`, this element is used to reject API calls once the token quota has been exceeded. This empowers API providers to set strict limits on the number of tokens consumed by applications over a defined interval.
  * [`<Interval>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#interval): This element specifies the time interval over which the number of tokens from LLM responses is calculated. It is used in conjunction with `<TimeUnit>` and `<Allow>` to define the token quota.
  * [`<TimeUnit>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#timeunit): This element defines the time unit for the `<Interval>`. Valid values include `minute`, `hour`, `day`, or `month`.
  * [`<Allow>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#allow): This element defines the number of tokens allowed in the `<Interval>`.
  * [`<LLMTokenUsageSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#llmtokenusagesource): This element provides the source of the token usage from the LLM response. It should be a message template that provides a single value of the token usage.
  * [`<LLMModelSource>`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#llmmodelsource): This element provides the source of the model from the LLM response or request. It should be a message template that provides a single value of the model name.



See the [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) reference page for:

  * [Examples](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#samples)
  * [Flow variables](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#variables)
  * [Error reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy#errors)



Configure the LLMTokenQuota policy in the Apigee UI as described in the following sections:

  * [Create an API product](https://docs.cloud.google.com/apigee/docs/api-platform/publish/create-api-products#add)
  * [ Creating an API proxy using the UI](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy#creatinganapiproxyintheedgemanagementui)
  * [ Attaching and configuring policies in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-management-ui)



## Limitations

The LLM token policies have the following limitations:

  * **LLMTokenQuota policy limitations**
    * The policy currently only supports text-based tokens.
    * The last allowed request may consume more tokens than the remaining quota.
    * The policy requires the exact JSON path for the LLM tokens consumed in the response payload and cannot detect it automatically. 
  * **PromptTokenLimit policy limitations**
    * The policy currently only supports text-based tokens.
    * The policy uses a standard library to count the tokens, which may differ from how some LLM providers count tokens. 
    * The policy requires the exact JSON path for the prompt text; it cannot find it dynamically. 



## See also

  * [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy)
  * [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy)
  * [Use an LLMTokenQuota policy to enforce token quotas for streaming server sent events](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events#llm-token-quota)
  * [REST Resource: organizations.apiproducts](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
