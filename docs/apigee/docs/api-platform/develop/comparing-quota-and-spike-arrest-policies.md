---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies/
title: Comparing rate-limiting policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:37.055238+00:00
---

# Comparing rate-limiting policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/comparing-quota-and-spike-arrest-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Comparing rate-limiting policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Key Point:**

The [ Quota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy), [ SpikeArrest](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy), [ PromptTokenLimit](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy), and [ LLMTokenQuota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) policies are all used for rate limiting, but they serve different purposes and operate on different metrics. While Quota and SpikeArrest focus on request counts, the PromptTokenLimit and LLMTokenQuota policies manage and control consumption based on tokens, which is crucial for AI and Large Language Model (LLM) workloads. 

While SpikeArrest and PromptTokenLimit maintain counts with high reliability, they are designed to use a [ Redis best-effort cache](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/other_protocols/redis) to store their counts. Because the cache is not replicated, there are cases where counts may be lost, such as a restart of the cache servers, or other rare cases. 

For these reasons, we recommend against using SpikeArrest or PromptTokenLimit for use cases that require accurate counting. Only the synchronous Quota or LLMTokenQuota policy offers accurate counting across all regions in a given timeframe. 

Use the comparison chart below to help you decide which policy to use for your rate-limiting use case:

| **Quota** | **SpikeArrest** | **LLMTokenQuota** | **PromptTokenLimit**  
---|---|---|---|---  
**Use it to:** |  Limit the number of API proxy calls a developer app or developer can make over a specific period of time. It's best for rate limiting over longer time intervals like days, weeks, or months, especially when accurate counting is a requirement.  |  Limit the number of API calls that can be made against an API proxy across all consumers over a short period of time, such as seconds or minutes.  |  Manage and limit the total token consumption for LLM API calls over a specified period (minute, hour, day, week, or month). This allows you to control LLM expenditures and apply granular quota management based on API products.  |  Protect your API proxy's target backend against token abuse, massive prompts, and potential denial-of-service attempts by limiting the rate of tokens sent in the input by throttling requests based on the number of tokens in the user's prompt message. It is a comparative paradigm to Spike Arrest for API traffic, but for tokens.   
**Don't use it to:** |  Protect your API proxy's target backend against traffic spikes. Use SpikeArrest or PromptTokenLimit for that.  |  Count and limit the number of connections apps can make to your API proxy's target backend over a specific period of time, especially when accurate counting is required.  |  Protect your API proxy's target backend against token abuse. Use PromptTokenLimit for that.  |  Accurately count and limit the total number of tokens consumed for billing or long-term quota management. Use the LLMTokenQuota policy for that.   
**Stores a count?** | Yes | No |  Yes, it maintains counters that track the number of tokens consumed by LLM responses.  |  It counts tokens to enforce a rate limit but does not store a persistent, long-term count like the LLMTokenQuota policy.   
**Best practices for attaching the policy:** |  Attach it to the **ProxyEndpoint Request PreFlow** , generally after the authentication of the user. This enables the policy to check the quota counter at the entry point of your API proxy. |  Attach it to the **ProxyEndpoint Request PreFlow** , generally at the very beginning of the flow. This provides spike protection at the entry point of your API proxy. If you use both SpikeArrest and Quota policies in the same proxy, SpikeArrest should always be attached _before_ the Quota policy in the ProxyEndpoint Request PreFlow. SpikeArrest acts as a first line of defense against sudden traffic bursts, smoothing traffic before requests are evaluated against longer-term Quota limits. This prevents spikes from prematurely exhausting quota. |  Apply the enforcement policy (`EnforceOnly`) in the **request flow** and the counting policy (`CountOnly`) in the **response flow**. For streaming responses, attach the counting policy to an **EventFlow**. |  Attach it to the **ProxyEndpoint Request PreFlow** , at the beginning of the flow, to protect your backend from oversized prompts. If you use both PromptTokenLimit and LLMTokenQuota policies in the same proxy, PromptTokenLimit should always be attached _before_ the LLMTokenQuota policy in the ProxyEndpoint Request PreFlow. PromptTokenLimit acts as a first line of defense against oversized prompts, rejecting them before requests are evaluated against longer-term LLMTokenQuota limits. This prevents oversized prompts from prematurely exhausting token quota.  
**HTTP status code when limit has been reached:** | `429` (Too Many Requests) | `429` (Too Many Requests) | `429` (Too Many Requests) | `429` (Too Many Requests)  
**Good to know:** | 

  * The Quota counter is stored in Cassandra.
  * You can configure the policy to synchronize the counter asynchronously to save resources, but this may allow calls slightly in excess of the limit. 

| 

  * Lets you choose between a _smoothing_ algorithm or an effective count algorithm. The former smooths the number of requests that can occur in a specified period of time, and the latter limits the total number of requests that can occur within a specified time period, no matter how rapidly they are sent in succession. 
  * Smoothing is not coordinated across Message Processors.

| 

  * Can be configured as `CountOnly` to track token usage or `EnforceOnly` to reject requests that exceed the quota. 
  * It works with API Products to allow for granular quota configurations based on the app, developer, model, or a specific LLM operation set. 
  * Uses `<LLMTokenUsageSource>` to extract token count from the LLM response and `<LLMModelSource>` to identify the model used. 

| 

  * The token calculation might differ slightly from the one used by the LLM. 
  * The `<UserPromptSource>` element specifies the location of the user prompt in the request message. 

  
**Get more details:** | [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) | [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) | [LLMTokenQuota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/llm-token-quota-policy) | [PromptTokenLimit policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/prompt-token-limit-policy)  
**Tip:** You can also use the following to protect slow/sluggish backends without impacting the performance of the APIs: 

  * [ Creating reusable shared flows:](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows) Combine policies and resources into a shared flow that you can consume from multiple API proxies, and even from other shared flows. 
  * [ Chaining API proxies together](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/connecting-proxies-other-proxies): Specify that one proxy is the target endpoint of another, effectively connecting the two proxies in a proxy chain. Chaining proxies in this way can help you avoid a network hop, and so improve overall performance. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


