---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-0-generate/
title: Veo\u00a03 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:16:41.132919+00:00
---

# Veo 3  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-0-generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Veo 3 Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** The following table describes image generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before June 30, 2026, to avoid service disruption. Discontinued endpoints | Recommended endpoint migration  
---|---  
`veo-3.0-generate-001` | `veo-3.1-generate-001`  
`veo-3.0-fast-generate-001` | `veo-3.1-fast-generate-001`  
  
Veo 3 is our latest line of video generation models. This page documents the capabilities and features of Veo 3.

## 3.0 Generate 001

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/video) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `veo-3.0-generate-001`  
---|---  
Modalities |  description  Text   
Input only  hide_image  Image   
Not supported  mic_off  Audio   
Not supported  videocam  Video   
Output only   
Capabilities | 

  * [Video generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text)   
Text to video, image to video  
Supported
  * [Extend videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/extend-videos)   
Not supported
  * [Use reference images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-references)   
Not supported
  * [Sound generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide#audio)   
Supported
  * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Not supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Supported

  
Technical specifications |  **Video** videocam | 

  * Video lengths: 4, 6, or 8 seconds
  * Maximum number of output videos per prompt: 4
  * Image-to-video maximum input image size: 20 MB
  * Supported aspect ratios: 9:16, 16:9
  * Supported output resolutions: 720p, 1080p
  * Supported framerates: 24 FPS
  * Supported MIME types: `video/mp4`

  
Prompt languages | 

  * English 

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`

  
Quotas | 

  * **Regional online prediction requests per base model per minute per base model** : 10 tokens per minute

  
Versions | 

  * `veo-3.0-generate-001`
    * Launch stage: GA
    * Release date: July 29, 2025
    * Retirement date†: June 30, 2026

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

##  3.0 Fast Generate 001 

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/video) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `veo-3.0-fast-generate-001`  
---|---  
Modalities |  description  Text   
Input only  hide_image  Image   
Not supported  mic_off  Audio   
Not supported  videocam  Video   
Output only   
Capabilities | 

  * [Video generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text)   
Text to video, image to video  
Supported
  * [Extend videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/extend-videos)   
Not supported
  * [Use reference images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-references)   
Not supported
  * [Sound generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide#audio)   
Supported
  * [Content Credentials (C2PA)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/content-credentials)   
Supported

  
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/batch-inference)   
Not supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Not supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Supported

  
Technical specifications |  **Video** videocam | 

  * Video lengths: 4, 6, or 8 seconds
  * Maximum number of output videos per prompt: 4
  * Image-to-video maximum input image size: 20 MB
  * Supported aspect ratios: 9:16, 16:9
  * Supported output resolutions: 720p, 1080p
  * Supported framerates: 24 FPS
  * Supported MIME types: `video/mp4`

  
Prompt languages | 

  * English 

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`

  
Quotas | 

  * **Regional online prediction requests per base model per minute per base model** : 10 tokens per minute

  
Versions | 

  * `veo-3.0-fast-generate-001`
    * Launch stage: GA
    * Release date: July 29, 2025
    * Retirement date†: June 30, 2026

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

For Veo pricing information, see the [Veo](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#veo) section of the [Cost of building and deploying AI models in Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
