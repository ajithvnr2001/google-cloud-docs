---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/vto/virtual-try-on-001/
title: Virtual Try-On \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:47.387177+00:00
---

# Virtual Try-On  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/vto/virtual-try-on-001/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Virtual Try-On Stay organized with collections  Save and categorize content based on your preferences. 

The Virtual Try-On model (`virtual-try-on-001`) lets you generate virtual try-on images from an image of a person and product photos that you provide.

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/generate;tab=image) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `virtual-try-on-001`  
---|---  
Modalities |  text_ad_off  Text   
Not supported  photo  Image   
Input and output  mic_off  Audio   
Not supported  videocam_off  Video   
Not supported   
Capabilities | 

  * [Thinking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/thinking)   
Not supported
  * [System instructions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/system-instruction-introduction)   
Not supported
  * [Structured output](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/control-generated-output)   
Not supported
  * [Context caching](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview)   
Not supported
  * [RAG Engine ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/rag-engine/rag-overview)   
Not supported
  * [Tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tune-models)   
Not supported
  * [Virtual try-on](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/generate-virtual-try-on-images)   
Supported
  * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)   
Supported
  * [Person generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PersonGeneration)   
Supported

  
APIs | 

  * [GenerateContent API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/inference)   
Supported
  * [Interactions API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/interactions) previewPreview feature  
Not supported
  * [Gemini Live API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api)   
Not supported
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

  
Technical specifications |  **Image** photo | 

  * Maximum images per prompt: 2
  * Maximum file size per file for inline data or direct uploads through the console: 7 MB
  * Maximum number of output images per prompt: 4
  * Supported aspect ratios: Same as input image
  * Supported resolutions: Same as input image
  * Supported MIME types: `image/png`, `image/jpeg`

  
**Parameter defaults** tune | 

  * candidateCount: 1-4

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`, `us-east1`, `us-east4`, `us-east5`, `us-south1`, `us-west1`, `us-west4`
  * Canada: `northamerica-northeast1`
  * Europe: `europe-west1`, `europe-west4`, `europe-west8`, `europe-west9`, `europe-southwest1`, `europe-north1`
  * Asia Pacific: `asia-northeast1`, `asia-southeast1`
  * Middle East: `me-central1`

  
**[Standard PayGo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/standard-paygo) ** | 

  * United States: `us-central1`, `us-east1`, `us-east4`, `us-east5`, `us-south1`, `us-west1`, `us-west4`
  * Canada: `northamerica-northeast1`
  * Europe: `europe-west1`, `europe-west4`, `europe-west8`, `europe-west9`, `europe-southwest1`, `europe-north1`
  * Asia Pacific: `asia-northeast1`, `asia-southeast1`
  * Middle East: `me-central1`

  
**[Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) ** | 

  * United States: `us-central1`, `us-east1`, `us-east4`, `us-east5`, `us-south1`, `us-west1`, `us-west4`
  * Canada: `northamerica-northeast1`
  * Europe: `europe-west1`, `europe-west4`, `europe-west8`, `europe-west9`, `europe-southwest1`, `europe-north1`
  * Asia Pacific: `asia-northeast1`, `asia-southeast1`
  * Middle East: `me-central1`

  
Versions | 

  * `virtual-try-on-001`
    * Launch stage: GA
    * Release date: January 20, 2026
    * Deprecation date: September 14, 2026
    * Retirement date†: March 15, 2027

  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
