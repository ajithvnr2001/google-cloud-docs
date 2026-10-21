---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon/
title: Gemini 4 Argon \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:57.932663+00:00
---

# Gemini 4 Argon  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 4 Argon Stay organized with collections  Save and categorize content based on your preferences. 

Gemini 4 Argon is Google's frontier model that excels at deep work in complex, real-world tasks across domains including coding, finance, legal, cybersecurity, and science.

4 Argon differs from earlier Gemini models in the following ways:

  * **Unified input and output token limit and long decodes** : 4 Argon has a unified 1,048,576-token limit that includes both input and output tokens (where output includes thinking, function calls, and the final response) across all supported API surfaces (the [`GenerateContent` API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference), the [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions), and the [OpenAI compatibility Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/openai)). A single synchronous request generates up to 65,536 output tokens (or 32,768 tokens for non-streaming direct HTTP requests). On the [`GenerateContent` API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference) (`v1beta1`), you can extend output up to 1,048,576 tokens (minus your input tokens) using long decodes: the Google Gen AI SDK and Agent Studio handle `continuation_token` automatically across requests, or you can pass `continuation_token` in a custom continuation loop (known issue: long decoding on `GenerateContent` is supported only in the `v1beta1` API, which the Google Gen AI SDK uses by default). For details, see the [developer's guide to Gemini 4 Argon](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon#long-decodes).
  * **Thinking levels** : Supports [thinking levels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking) `LOW`, `MEDIUM` (default), and `HIGH`. Setting `thinking_budget` or `thinking_level="MINIMAL"` returns an HTTP `400` validation error.
  * **Sampling parameters** : Custom values for [sampling parameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/content-generation-parameters) (`temperature`, `top_p`, and `top_k`) are ignored.
  * **Context caching** : 4 Argon supports [implicit caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview) only (4,096-token minimum), with durable caching enabled by default. Explicit context caching isn't supported.



[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/chat?model=gemini-4-argon) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/chat?suggestedPrompt=How%20does%20AI%20work&deploy=true&model=gemini-4-argon) [Developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-4-argon) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-4-argon`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only   
Token limits | Context window | 1,048,576  
Maximum output tokens | 1,048,576  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Implicit context caching  
Supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search, Google Maps, Agent Search, Parallel Web Search, Exa Web Search, Web Grounding for Enterprise  
Supported
  * [Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/code-execution)   
Supported
  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Supported
  * [URL context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/url-context)   
Supported
  * [Computer use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use) previewPreview feature  
Supported

  
APIs | 

  * [GenerateContent API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference)   
Supported
  * [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions) previewPreview feature  
Supported
  * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)   
Not supported
  * [Count Tokens API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)   
Supported
  * [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo, Priority PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Technical specifications |  **Image** photo | 

  * Maximum images per prompt: 3,000 (up to 100 URIs)
  * Maximum file size per file for inline data or direct uploads through the console: 7 MB
  * Maximum file size per file from Google Cloud Storage: 30 MB
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`

  
**Text** description | 

  * Maximum number of files per prompt: 3,000 (up to 100 URIs)
  * Maximum number of pages per file: 3,000
  * Maximum file size per file for the API or Cloud Storage imports: 50 MB(application/pdf) or 7 MB(text/plain)
  * Maximum file size per file for direct uploads through the console: 7 MB
  * Supported MIME types: `application/pdf`, `text/plain`

  
**Video** videocam | 

  * Maximum video length (with audio): Approximately 45 minutes
  * Maximum video length (without audio): Approximately 1 hour
  * Maximum number of videos per prompt: 10
  * Supported MIME types: `video/x-flv`, `video/quicktime`, `video/mpeg`, `video/mpegs`, `video/mpg`, `video/mp4`, `video/webm`, `video/wmv`, `video/3gpp`

  
**Audio** mic | 

  * Maximum audio length per prompt: Approximately 8.4 hours, or up to 1 million tokens
  * Maximum number of audio files per prompt: 1
  * Speech understanding for: Audio summarization, transcription, and translation
  * Supported MIME types: `audio/x-aac`, `audio/flac`, `audio/mp3`, `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`, `audio/pcm`, `audio/wav`, `audio/webm`

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`
  * Europe: `europe-west2`
  * Asia Pacific: `asia-southeast1`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Multi-region: `us`, `eu`
  * Europe: `europe-west2`
  * Asia Pacific: `asia-southeast1`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`
  * Europe: `europe-west2`
  * Asia Pacific: `asia-southeast1`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
**[Priority PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/priority-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
Versions | 

  * `gemini-4-argon`
    * Launch stage: GA
    * Release date: October 13, 2026
    * Retirement date†: October 13, 2027 or later

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
**Batch inference** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
**Context caching** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

## Gemini 4 Argon Cyber Permissive

Gemini 4 Argon Cyber Permissive is a version of Gemini 4 Argon for defensive cybersecurity use cases, such as vulnerability discovery, reverse engineering, exploit verification, and patch generation. Gemini 4 Argon Cyber Permissive is a Google Frontier Cyber Model subject to Section 31 of the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Gemini 4 Argon Cyber Permissive is available behind an allowlist. It is generally available when accessed directly on the Gemini Enterprise Agent Platform, but may also be used with [CodeMender](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender), which is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). To request access, contact your Google team or apply through the [Fairwind Program](https://deepmind.google/fairwind-program/). Access to Gemini 3.8 Flash Cyber doesn't carry over; you must apply separately.

The following table shows how Gemini 4 Argon Cyber Permissive differs from Gemini 4 Argon:

| 4 Argon | 4 Argon Cyber Permissive  
---|---|---  
Model ID | `gemini-4-argon` | `gemini-4-argon-cyber-permissive`  
Access | Publicly available | Allowlist only ([Fairwind Program](https://deepmind.google/fairwind-program/))  
Default thinking level | `MEDIUM` (supports `LOW`, `MEDIUM`, `HIGH`) | `HIGH` (supports `LOW`, `MEDIUM`, `HIGH`)  
Computer use | Supported | Not supported  
Supported regions | `global`, `us`, `eu` | `global`, `us`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
