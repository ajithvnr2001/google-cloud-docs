---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview/
title: Context caching overview \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:12.409896+00:00
---

# Context caching overview  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Context caching overview Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of context caching, run the "Intro to context caching" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/context-caching/intro_context_caching.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fcontext-caching%2Fintro_context_caching.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fcontext-caching%2Fintro_context_caching.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/context-caching/intro_context_caching.ipynb)

Context caching helps reduce the cost and latency of requests to Gemini that contain repeated content. Gemini Enterprise Agent Platform offers two types of caching:

  * **Implicit caching:** Automatic caching enabled by default that provides cost savings when cache hits occur. Implicit caching includes in-memory caching and durable caching.
  * **Explicit caching:** Manual caching enabled using the Gemini Enterprise API, where you explicitly declare the content you want to cache and whether or not your prompts should refer to the cached content.



For both implicit and explicit caching, the [`cachedContentTokenCount`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/GenerateContentResponse) field in your response's metadata indicates the number of tokens in the cached part of your input.

## Caching storage costs

For both implicit and explicit caching, you're billed for the input tokens used to create the cache at the standard input token price. For explicit caching, there are also storage costs based on how long caches are stored. There are no storage costs for implicit caching. For more information, see [Agent Platform pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#context-caching).

## Implicit caching

All Google Cloud projects have implicit caching enabled by default. Implicit caching provides a 90% discount on cached tokens compared to standard input tokens. When enabled, implicit cache hit cost savings are automatically passed on to you.

Implicit caching stores prefixes in two storage tiers:

  * **In-memory caching:** Cached prefixes are kept in memory. Memory capacity is limited, so prefixes are evicted as capacity is reclaimed.
  * **Durable caching:** When a prefix is evicted from in-memory storage, it moves to durable storage instead of being discarded. A later request that reuses the prefix can still get a cache hit, which raises cache hit rates for workloads that reuse the same context over longer intervals.



Both tiers are enabled by default. A cached prefix expires no later than 24 hours after it's created, and most entries are evicted earlier. You can disable durable caching and keep in-memory caching, or you can disable implicit caching entirely. If you have data retention concerns, see [Zero data retention](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention#controlling-data-caching), which describes how cached data is handled and how to disable each tier.

To increase the likelihood of an implicit cache hit, do the following:

  * Place large and common contents at the beginning of your prompt.
  * Send requests with a similar prefix in a short amount of time.



### Supported models

Implicit caching is available on supported Gemini models, and durable caching is available on a subset of those models.

#### In-memory caching

In-memory caching is supported when using the following models:

#### Click to expand supported models

  * [Gemini Nano Banana 2.1](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/nano-banana-2-1)
  * [Gemini 4 Argon Cyber Permissive](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon#cyber)
  * [Gemini 4 Argon](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon)
  * [Gemini 3.8 Flash Cyber](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber)
  * [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)
  * [Gemini 3.7 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash)
  * [Gemini 3.6 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash)
  * [Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)
  * [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash)
  * [Gemini 3.1 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) preview
  * [Gemini 3.1 Flash-Lite Image (Nano Banana 2 Lite)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite-image)
  * [Gemini 3.1 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)
  * [Gemini 3.1 Flash Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-image)
  * [Gemini 3 Pro Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-pro-image)
  * [Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) preview
  * [Gemini 2.5 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-pro)
  * [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)
  * [Gemini 2.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)



#### Durable caching

Durable caching is supported when using the following models:

  * Gemini 4 Argon
  * Gemini 4 Argon Cyber Permissive
  * [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)
  * [Gemini 3.8 Flash Cyber](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber)



Implicit caching also supports open models. For more information, see [Agent Platform open models for MaaS](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/maas/use-open-models#context-caching).

## Explicit caching

Explicit caching offers more control and ensures a discount on input tokens that reference an existing context cache. On Gemini 2.5 or later models, this discount is 90%; on Gemini 2.0 models, this discount is 75%.

Using the Gemini Enterprise API, you can perform the following tasks:

  * [Create context caches](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-create) and control them more effectively.
  * [Use a context cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-use) by referencing its contents in a prompt request with its resource name.
  * [Update a context cache's expiration time (Time to Live, or TTL)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-update) past the default 60 minutes.
  * [Delete a context cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-delete) when no longer needed.



You can also use the Gemini Enterprise API to [retrieve information about a context cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-getinfo).

Explicit caches interact with implicit caching, potentially leading to additional caching beyond the specified contents when [creating a cache](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-create). To prevent cache data retention, disable implicit caching and avoid creating explicit caches. For more information, see [Enable and disable caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention#enabling-disabling-caching).

### Supported models

Explicit caching is supported when using the following models:

#### Click to expand supported models

  * [Gemini 3.8 Flash Cyber](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber)
  * [Gemini 3.8 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)
  * [Gemini 3.7 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-7-flash)
  * [Gemini 3.6 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-6-flash)
  * [Gemini 3.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash-lite)
  * [Gemini 3.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash)
  * [Gemini 3.1 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-pro) preview
  * [Gemini 3.1 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-lite)
  * [Gemini 3 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-flash) preview
  * [Gemini 2.5 Pro](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-pro)
  * [Gemini 2.5 Flash-Lite](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash-lite)
  * [Gemini 2.5 Flash](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/2-5-flash)



## When to use context caching

Context caching is particularly well suited to scenarios where a substantial initial context is referenced repeatedly by subsequent requests.

Cached context items, such as a large amount of text, an audio file, or a video file, can be used in prompt requests to the Gemini API to generate output. Requests that use the same cache in the prompt also include text unique to each prompt. For example, each prompt request that composes a chat conversation might include the same context cache that references a video along with unique text that comprises each turn in the chat.

Consider using context caching for the following use cases:

  * Chatbots with extensive system instructions
  * Repetitive analysis of lengthy video files
  * Recurring queries against large document sets
  * Frequent code repository analysis or bug fixing



Implicit and explicit caching are supported with Provisioned Throughput in [Preview](https://cloud.google.com/products#product-launch-stages). Refer to the [Provisioned Throughput guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/measure-provisioned-throughput#context_caching) for more details. Caches work across traffic types. For example, a cache created while using Provisioned Throughput also works with PayGo.

## Availability

Context caching is available in regions where Generative AI on Agent Platform is available. For more information, see [Generative AI on Agent Platform locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations).

## Limits

Context caching adheres to the limits in the following table:

Context caching limits  
---  
Minimum cache token count for implicit and explicit caching | 

  * **Gemini 3 (with exceptions) and Gemini 4 models:** 4,096 tokens
  * **Gemini 3.0 Flash Preview, 3.1 Pro Preview, 3.7 Flash, and 3.8 Flash (implicit caching only):** 6,144 tokens
  * **Gemini 2 family models:** 2,048 tokens

  
Maximum size of content you can cache using a blob or text | 10 MB  
Minimum time before a cache expires after it's created | 1 minute  
Maximum time before a cache expires after it's created | There isn't a maximum cache duration  
Maximum lifetime of an implicitly cached prefix | Up to 24 hours  
**Important:** When caching objects that are stored in a Cloud Storage bucket, don't make changes to objects until the cached contents are expired or deleted. Updates to Cloud Storage objects can cause the associated cached contents to be unusable.

## Cache data isolation and security for agentic workloads

Google Cloud uses your project number to isolate cached data, and cached content is never shared across projects.

To prevent cross-user data leakage in agentic workloads, scope cached prompt data and outputs to each user session. When you run background agents or multi-tenant proxies, align cache boundaries with end-user permissions so an agent can't reuse cached credentials or data across users.

## VPC Service Controls support

Context caching supports VPC Service Controls, meaning your cache cannot be exfiltrated beyond your service perimeter. If you use Cloud Storage to build your cache, include your bucket in your service perimeter as well to protect your cache content.

For more information, see [VPC Service Controls with Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls) in the Agent Platform documentation.

## What's next

  * Learn about [the Gemini API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models).
  * Learn how to [use multimodal prompts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/design-multimodal-prompts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
