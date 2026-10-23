---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber/
title: Gemini 3.8 Flash Cyber \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:39.858343+00:00
---

# Gemini 3.8 Flash Cyber  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash-cyber/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 3.8 Flash Cyber Stay organized with collections  Save and categorize content based on your preferences. 

Gemini 3.8 Flash Cyber is a post-training version of the Gemini 3.8 Flash model tailored specifically for cybersecurity use cases. Gemini 3.8 Flash is a Gemini Cyber model subject to Section 31(a) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Gemini 3.8 Flash Cyber is available in GA behind an allowlist. To request access, contact your Google team or apply for access at [Fairwind Program](https://deepmind.google/fairwind-program/).

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/chat?model=gemini-3.8-flash-cyber) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/chat?suggestedPrompt=How%20does%20AI%20work&deploy=true&model=gemini-3.8-flash-cyber) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-3.8-flash-cyber`  
---|---  
Modalities |  description  Text   
Input and output  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only   
Token limits | Context window | 1,048,576  
Maximum output tokens | 65,536  
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Implicit context caching, explicit context caching  
Supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Not supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Not supported
  * [Code execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/code-execution)   
Not supported
  * [Function calling](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tools/function-calling)   
Not supported
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
Not supported
  * [Count Tokens API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)   
Supported
  * [Chat Completions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo with Usage Tiers, Flex PayGo, Priority PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Technical specifications |  **Image** photo | 

  * Maximum images per prompt: 3,000
  * Maximum file size per file for inline data or direct uploads through the console: 7 MB
  * Maximum file size per file from Google Cloud Storage: 30 MB
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`

  
**Text** description | 

  * Maximum number of files per prompt: 3,000
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
  * Supported MIME types: `audio/x-aac`, `audio/flac`, `audio/mp3`, `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`, `audio/pcm`, `audio/wav`, `audio/webm`

  
**Parameter defaults** tune | 

  * Temperature: 1.0
  * topP: 0.95
  * topK: 64
  * Frequency penalty: 0
  * Presence penalty: 0

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`
  * Multi-region: `us`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Multi-region: `us`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * Global: `global`
  * Multi-region: `us`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`

  
Versions | 

  * `gemini-3.8-flash-cyber`
    * Launch stage: GA
    * Release date: September 16, 2026

  
Security controls | **Online prediction** | 

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
