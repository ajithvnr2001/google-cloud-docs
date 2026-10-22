---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate/
title: Veo\u00a03.1 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:02.661042+00:00
---

# Veo 3.1  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Veo 3.1 Stay organized with collections  Save and categorize content based on your preferences. 

Veo 3.1 is our latest line of video generation models. This page documents the capabilities and features of Veo 3.1.

##  3.1 Generate 

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/video) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `veo-3.1-generate-001`  
---|---  
Modalities |  description  Text   
Input only  photo  Image   
Input only  mic_off  Audio   
Not supported  videocam  Video   
Output only   
Capabilities | 

  * [Video generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text)   
Text to video, image to video, from first and last frame  
Supported
  * [Extend videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/extend-videos)   
Supported
  * [Use reference images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-references)   
Asset images  
Supported
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

  * Video lengths: 4, 6, or 8 seconds; reference image to video only supports 8 seconds.
  * Maximum number of output videos per prompt: 4
  * Image-to-video maximum input image size: 20 MB
  * Supported aspect ratios: 9:16, 16:9
  * Supported input resolutions: 720p, 1080p
  * Supported output resolutions: 720p, 1080p, 4K
  * Supported framerates: 24 FPS
  * Supported MIME types: `video/mp4`

  
Prompt languages | 

  * English 

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`

  
Quotas | 

  * **Regional online prediction requests per base model per minute per base model** : 50 tokens per minute

  
Versions | 

  * `veo-3.1-generate-001`
    * Launch stage: GA
    * Release date: November 17, 2025
    * Retirement date†: November 17, 2026 or later

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

##  3.1 Fast Generate 

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/video) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `veo-3.1-fast-generate-001`  
---|---  
Modalities |  description  Text   
Input only  photo  Image   
Input only  mic_off  Audio   
Not supported  videocam  Video   
Output only   
Capabilities | 

  * [Video generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text)   
Text to video, image to video, from first and last frame  
Supported
  * [Extend videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/extend-videos)   
Supported
  * [Use reference images](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-references)   
Asset images  
Supported
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

  * Video lengths: 4, 6, or 8 seconds.
  * Maximum number of output videos per prompt: 4
  * Image-to-video maximum input image size: 20 MB
  * Supported aspect ratios: 9:16, 16:9
  * Supported input resolutions: 720p, 1080p
  * Supported output resolutions: 720p, 1080p
  * Supported framerates: 24 FPS
  * Supported MIME types: `video/mp4`

  
Prompt languages | 

  * English 

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`

  
Quotas | 

  * **Regional online prediction requests per base model per minute per base model** : 50 tokens per minute

  
Versions | 

  * `veo-3.1-fast-generate-001`
    * Launch stage: GA
    * Release date: November 17, 2025
    * Retirement date†: November 17, 2026 or later

  
Security controls | **Online prediction** | 

  * Data residency 
  * CMEK 
  * VPC-SC 
  * AXT 

  
See [Security controls](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/security-controls) for more information.  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

**Preview**

This product or feature is a Generative AI Preview offering, subject to the "Pre-GA Offerings Terms" of the [ Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). For this Generative AI Preview offering, Customers may elect to use it for production or commercial purposes, or disclose Generated Output to third-parties, and may process personal data as outlined in the [ Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. 

##  3.1 Lite Generate 

[Try in Agent Studio](https://console.cloud.google.com/agent-platform/studio/media/video) [Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `veo-3.1-lite-generate-001`  
---|---  
Modalities |  description  Text   
Input only  hide_image  Image   
Not supported  mic_off  Audio   
Not supported  videocam  Video   
Output only   
Capabilities | 

  * [Video generation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-text)   
Text to video, image to video, from first and last frame  
Supported
  * [Extend videos](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/extend-videos)   
Supported
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

  * Video lengths: 4, 6, or 8 seconds.
  * Maximum number of output videos per prompt: 4
  * Image-to-video maximum input image size: 20 MB
  * Supported aspect ratios: 9:16, 16:9
  * Supported input resolutions: 720p, 1080p
  * Supported output resolutions: 720p, 1080p
  * Supported framerates: 24 FPS
  * Supported MIME types: `video/mp4`

  
Prompt languages | 

  * English previewPreview feature

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * United States: `us-central1`

  
Quotas | 

  * **Regional online prediction requests per base model per minute per base model** : 50 tokens per minute

  
Versions | 

  * `veo-3.1-lite-generate-001`
    * Launch stage: Preview
    * Release date: April 2, 2026

  
  
† Listed retirement dates refer to retirement of support in Gemini Enterprise Agent Platform. Models may remain accessible through the Gemini API after these dates have passed. The Gemini API is not a Google Cloud offering and is subject to its own terms of service. For details, see the [Gemini API documentation](https://ai.google.dev/). 

For Veo pricing information, see the [Veo](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing#veo) section of the [Cost of building and deploying AI models in Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
