---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash/
title: Gemini 3.5 Flash \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:20.966876+00:00
---

# Gemini 3.5 Flash  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-5-flash/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini 3.5 Flash Stay organized with collections  Save and categorize content based on your preferences. 

Gemini 3.5 Flash delivers near-Pro intelligence at Flash-tier cost and speed: Pro-level coding proficiency, parallel agentic execution, all at the same price point as a Flash model.

To get started, view the [introductory notebook for Gemini 3.5 Flash](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash.ipynb).

For more information on using the latest Gemini models, see [Get started with Gemini 3](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/get-started-with-gemini-3).

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/generative/multimodal/create/text?model=gemini-3.5-flash) [Deploy example app](https://console.cloud.google.com/agent-platform/studio/multimodal?suggestedPrompt=How%20does%20AI%20work&deploy=true&model=gemini-3.5-flash) [Developer guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/guides/gemini-3-5-flash) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Note: "Deploy example app" requires a Google Cloud project with billing and Agent Platform API enabled.Model ID | `gemini-3.5-flash`  
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
Supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Supervised fine-tuning, continuous tuning, tuning checkpoints  
Supported
  * [Agentic video understanding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/video-understanding#agentic-video-processing)   
Not supported

  
Tools | 

  * [Grounding](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/overview)   
Google Search, Parallel Web Search, Exa Web Search  
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
Supported
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

  * Temperature: 0.0-2.0 (default 1.0)
  * topP: 0.0-1.0 (default 0.95)
  * topK: 64 (fixed)
  * candidateCount: 1–8 (default 1)

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`
  * Americas: `northamerica-northeast1`
  * Europe: `europe-west2`, `europe-west3`
  * Asia Pacific: `asia-northeast1`, `asia-south1`, `asia-southeast1`, `australia-southeast1`

  
**[ML processing](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/data-residency) ** | 

  * Multi-region: `us`, `eu`
  * Americas: `northamerica-northeast1`
  * Europe: `europe-west2`, `europe-west3`
  * Asia Pacific: `asia-northeast1`, `asia-south1`, `asia-southeast1`, `australia-southeast1`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`
  * Europe: `europe-west2`, `europe-west3`
  * Asia Pacific: `asia-northeast1`, `asia-south1`, `asia-southeast1`, `australia-southeast1`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * Global: `global`
  * Multi-region: `us`, `eu`

  
Versions | 

  * `gemini-3.5-flash`
    * Launch stage: GA
    * Release date: May 19, 2026
    * Retirement date†: May 19, 2027 or later

  
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

  
**Tuning** | 

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

**Note:** In `asia-northeast1`, `asia-south1`, `asia-southeast1`, `australia-southeast1`, and `europe-west2`, only Single Zone Provisioned Throughput is supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
