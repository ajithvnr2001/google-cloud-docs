---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-images-overview/
title: Edit images with Imagen on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:09.782451+00:00
---

# Edit images with Imagen on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-images-overview/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Edit images with Imagen on Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

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
  
Imagen on Vertex AI lets you edit Imagen-generated or existing images. You can specify part of the image to modify in addition to a text description of the updates (mask-base editing).

Advanced multi-turn editing is a key strength of Gemini models. For more information, see [Edit images with Gemini](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/gemini-edit-images).

## Types of available editing tools

Imagen supports mask-based editing. Mask-based editing lets you specify a targeted area to apply edits to. This method of editing is good for edits that apply to only parts of an image. Mask-based editing is useful for the following types of image edits:

  * [Insert objects into an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects)
  * [Remove objects from an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-remove-objects)
  * [Expand the content of an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting)
  * [Replace the background of an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image)



## Locations

A location is a [region](https://docs.cloud.google.com/about/locations) you can specify in a request to control where data is stored at rest. For a list of available regions, see [ Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai).

## Safety filtering

Both input data and output content are checked for offensive material when you send an image editing request to Imagen. This means offensive input data from a text prompt or from a base image you provide can be blocked. Similarly, offensive output images might also be blocked, affecting the number of generated images you get in a response.

For more information about safety filtering and blocked content handling, see [Responsible AI and usage guidelines for Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters).

## Model versions

There are multiple image generation models that you can use. Each model may have limits that are specific to that model. For more information, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models).

## What's next

  * [Insert objects into an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects)
  * [Remove objects from an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-remove-objects)
  * [Expand the content of an image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-outpainting)
  * [Edit product images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-product-image)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
