---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-live/
title: Gemini 3.8 Live \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:15.539876+00:00
---

# Gemini 3.8 Live  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-live/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 3.8 Live Stay organized with collections  Save and categorize content based on your preferences. 

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/multimodal-live?model=gemini-3.8-live) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `gemini-3.8-live`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input and output  videocam  Video   
Input and output   
Token limits | Maximum input tokens | 128K  
Maximum output tokens | 64K  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Not supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Not supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Not supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Not supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search  
Supported
  * [Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/code-execution)   
Not supported
  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Supported
  * [URL context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/url-context)   
Not supported
  * [Computer use](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/computer-use) previewPreview feature  
Not supported

  
APIs | 

  * [GenerateContent API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference)   
Supported
  * [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions) previewPreview feature  
Not supported
  * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)   
Supported
  * [Count Tokens API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)   
Not supported
  * [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview)   
Not supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Technical specifications |  **Text** description | 

  * Supported MIME types: `text/plain`

  
**Image** photo | 

  * Standard input resolution: 768 x 768
  * Minimum custom avatar reference image resolution: 704 x 1280 (portrait) or 1280 x 704 (landscape)
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`

  
**Audio** mic | 

  * Maximum number of audio files per prompt: 1-stream
  * Required audio input format: Raw 16-bit PCM audio at 16kHz, little-endian
  * Required audio output format: Raw 16-bit PCM audio at 24kHz, little-endian
  * Supported MIME types: `audio/x-aac`, `audio/flac`, `audio/mp3`, `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`, `audio/pcm`, `audio/wav`, `audio/webm`, `audio/mpa`

  
**Video** videocam | 

  * Standard input resolution: 768 x 768 (1 FPS)
  * Minimum Live Avatar output resolution: 704 x 1280 (portrait) or 1280 x 704 (landscape) at 24 FPS
  * Supported MIME types: `video/x-flv`, `video/quicktime`, `video/mpeg`, `video/mpegs`, `video/mpg`, `video/mp4`, `video/webm`, `video/wmv`, `video/3gpp`

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Multi-region: `us`, `eu`
  * United States: `us-central1`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Multi-region: `us`, `eu`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * Multi-region: `us`, `eu`
  * United States: `us-central1`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Multi-region: `us`, `eu`
  * United States: `us-central1`

  
Knowledge cutoff date |  January 2025   
Versions | 

  * `gemini-3.8-live`
    * Launch stage: GA
    * Release date: September 24, 2026
    * Retirement date†: September 25, 2027 or later

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
