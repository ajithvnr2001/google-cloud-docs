---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-001/
title: Imagen\u00a04 \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:58.709513+00:00
---

# Imagen 4  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate-001/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Imagen 4 Stay organized with collections  Save and categorize content based on your preferences. 

Imagen 4 is our latest line of image generation models. This page documents the capabilities and features of the Imagen 4 models.

**Caution:** The following table describes image generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before June 30, 2026, to avoid service disruption. Discontinued endpoints | Recommended endpoint migration  
---|---  
`imagegeneration@002` | `gemini-2.5-flash-image`  
`imagegeneration@003` | `gemini-2.5-flash-image`  
`imagegeneration@004` | `gemini-2.5-flash-image`  
`imagegeneration@005` | `gemini-2.5-flash-image`  
`imagegeneration@006` | `gemini-2.5-flash-image`  
`imagetext@001` | `gemini-2.5-flash-image`  
`imagen-3.0-capability-001` | `gemini-2.5-flash-image`  
`imagen-3.0-capability-002` | `gemini-2.5-flash-image`  
`imagen-3.0-fast-generate-001` | `gemini-2.5-flash-image`  
`imagen-3.0-generate-001` | `gemini-2.5-flash-image`  
`imagen-3.0-generate-002` | `gemini-2.5-flash-image`  
`imagen-4.0-fast-generate-001` | `gemini-2.5-flash-image`  
`imagen-4.0-generate-001` | `gemini-2.5-flash-image`  
`imagen-4.0-ultra-generate-001` | `gemini-2.5-flash-image`  
  
## 4.0 Generate 001

Model ID | `imagen-4.0-generate-001`  
---|---  
Supported inputs & outputs | 

  * Inputs: Text
  * Outputs: Images

  
Capabilities  | 

  * Supported
    * [Image generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)
    * [Digital watermarking and verification](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#watermark)
    * [User-configurable safety settings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#safety-filters)
    * [Prompt enhancement using prompt rewriter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#prompt-rewriter) preview Preview feature
    * [Person generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
    * [Set output resolution](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/set-output-resolution)
    * [Content Credentials (C2PA)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/content-credentials)
  * Not supported
    * [Image customization using few-shot learning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization#subject-customization)
    * [Subject customization for product, person, and animal companion](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization)
    * [Style customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/style-customization)
    * [Controlled customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-controlled)
    * [Instruct customization or style transfer](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/instruct-customization)
    * [Mask-based image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-inpainting)
    * [Insert objects in images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects)
    * [Remove objects from images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-remove-objects)
    * [Outpainting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting)
    * [Product image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image)
    * [Upscale images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/upscale-image)
    * [Negative prompting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide#negative-prompts)

  
Usage types  | 

  * Supported
    * [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview)
  * Not supported

  
Technical specifications   
**Images** photo | 

  * Maximum image size: 10MB 
  * Maximum number of output images per prompt: 4 
  * Supported aspect ratios: 1:1, 3:4, 4:3, 9:16, and 16:9 
  * Supported resolutions: 1024x1024, 896x1280, 1280x896, 768x1408, 1408x768, 2048x2048, 1792x2560, 2560x1792, 1536x2816, 2816x1536 
  * Supported MIME types: `image/png`, `image/jpeg`

  
Versions | 

  * `imagen-4.0-generate-001`
    * Launch stage: GA
    * Release date: August 14, 2025
    * Discontinuation date: June 30, 2026

  
Prompt languages  | 

  * English 
  * Chinese (simplified)  preview Preview feature
  * Chinese (traditional)  preview Preview feature
  * Hindi  preview Preview feature
  * Japanese  preview Preview feature
  * Korean  preview Preview feature
  * Portuguese  preview Preview feature
  * Spanish  preview Preview feature

  
Quotas  | 

  * Regional online prediction requests per base model per minute per base model: 75

  
  
##  4.0 Fast Generate 001 

Model ID | `imagen-4.0-fast-generate-001`  
---|---  
Supported inputs & outputs | 

  * Inputs: Text
  * Outputs: Images

  
Capabilities  | 

  * Supported
    * [Image generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)
    * [Digital watermarking and verification](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#watermark)
    * [User-configurable safety settings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#safety-filters)
    * [Prompt enhancement using prompt rewriter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#prompt-rewriter) preview Preview feature
    * [Person generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
    * [Set output resolution](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/set-output-resolution)
    * [Content Credentials (C2PA)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/content-credentials)
  * Not supported
    * [Image customization using few-shot learning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization#subject-customization)
    * [Subject customization for product, person, and animal companion](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization)
    * [Style customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/style-customization)
    * [Controlled customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-controlled)
    * [Instruct customization or style transfer](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/instruct-customization)
    * [Mask-based image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-inpainting)
    * [Insert objects in images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects)
    * [Remove objects from images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-remove-objects)
    * [Outpainting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting)
    * [Product image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image)
    * [Upscale images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/upscale-image)
    * [Negative prompting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide#negative-prompts)

  
Usage types  | 

  * Supported
    * [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview)
  * Not supported

  
Technical specifications   
**Images** photo | 

  * Maximum image size: 10MB 
  * Maximum number of output images per prompt: 4 
  * Supported aspect ratios: 1:1, 3:4, 4:3, 9:16, and 16:9 
  * Supported resolutions: 1024x1024, 896x1280, 1280x896, 768x1408, 1408x768 
  * Supported MIME types: `image/png`, `image/jpeg`

  
Versions | 

  * `imagen-4.0-fast-generate-001`
    * Launch stage: GA
    * Release date: August 14, 2025
    * Discontinuation date: June 30, 2026

  
Prompt languages  | 

  * English 
  * Chinese (simplified)  preview Preview feature
  * Chinese (traditional)  preview Preview feature
  * Hindi  preview Preview feature
  * Japanese  preview Preview feature
  * Korean  preview Preview feature
  * Portuguese  preview Preview feature
  * Spanish  preview Preview feature

  
Quotas  | 

  * Regional online prediction requests per base model per minute per base model: 150

  
  
##  4.0 Ultra Generate 001 

Model ID | `imagen-4.0-ultra-generate-001`  
---|---  
Supported inputs & outputs | 

  * Inputs: Text
  * Outputs: Images

  
Capabilities  | 

  * Supported
    * [Image generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)
    * [Digital watermarking and verification](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#watermark)
    * [User-configurable safety settings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#safety-filters)
    * [Prompt enhancement using prompt rewriter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#prompt-rewriter) preview Preview feature
    * [Person generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
    * [Content Credentials (C2PA)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/content-credentials)
  * Not supported
    * [Image customization using few-shot learning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization#subject-customization)
    * [Subject customization for product, person, and animal companion](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization)
    * [Style customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/style-customization)
    * [Controlled customization](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-controlled)
    * [Instruct customization or style transfer](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/instruct-customization)
    * [Mask-based image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-inpainting)
    * [Insert objects in images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects)
    * [Remove objects from images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-remove-objects)
    * [Outpainting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting)
    * [Product image editing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image)
    * [Upscale images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/upscale-image)
    * [Negative prompting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide#negative-prompts)

  
Usage types  | 

  * Supported
    * [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview)
  * Not supported

  
Technical specifications   
**Images** photo | 

  * Maximum image size: 10MB 
  * Maximum number of output images per prompt: 4 
  * Supported aspect ratios: 1:1, 3:4, 4:3, 9:16, and 16:9 
  * Supported resolutions: 1024x1024, 896x1280, 1280x896, 768x1408, 1408x768, 2048x2048, 1792x2560, 2560x1792, 1536x2816, 2816x1536 
  * Supported MIME types: `image/png`, `image/jpeg`

  
Versions | 

  * `imagen-4.0-ultra-generate-001`
    * Launch stage: GA
    * Release date: August 14, 2025
    * Discontinuation date: June 30, 2026

  
Prompt languages  | 

  * English 
  * Chinese (simplified)  preview Preview feature
  * Chinese (traditional)  preview Preview feature
  * Hindi  preview Preview feature
  * Japanese  preview Preview feature
  * Korean  preview Preview feature
  * Portuguese  preview Preview feature
  * Spanish  preview Preview feature

  
Quotas  | 

  * Regional online prediction requests per base model per minute per base model: 30

  
  
For Imagen pricing information, see the [Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing#imagen-models) section of the [Cost of building and deploying AI models in Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing#imagen-models) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
