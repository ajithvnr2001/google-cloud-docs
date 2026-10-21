---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/virtual-try-on-001/
title: Virtual Try-On 001 \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:00:43.657502+00:00
---

# Virtual Try-On 001  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/virtual-try-on-001/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Virtual Try-On 001 Stay organized with collections  Save and categorize content based on your preferences. 

Virtual Try-On lets you generate virtual try-on images from an image of a person and product photos that you provide. This page documents the capabilities and features of `virtual-try-on-001`.

Model ID | `virtual-try-on-001`  
---|---  
Supported inputs & outputs | 

  * Inputs: Images
  * Outputs: Images

  
Capabilities  | 

  * Supported
    * [Digital watermarking and verification](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#watermark)
    * [User-configurable safety settings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#safety-filters)
    * [Virtual Try-On](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-virtual-try-on-images)
    * [Person generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
    * [Content Credentials (C2PA)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/content-credentials)
  * Not supported
    * [Image generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)

  
Usage types  | 

  * Supported
    * [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview)
  * Not supported

  
Technical specifications   
**Images** photo | 

  * Maximum image size: 10MB 
  * Maximum number of output images per prompt: 4 
  * Supported aspect ratios: Same as input image 
  * Supported resolutions: Same as input image 
  * Supported MIME types: `image/png`, `image/jpeg`

  
Versions | 

  * `virtual-try-on-001`
    * Launch stage: GA
    * Release date: January 20, 2026
    * Discontinuation date: January 20, 2027

  
Prompt languages  | 

  * English 

  
Quotas  | 

  * Regional online prediction requests per base model per minute per base model: 50

  
  
For Imagen pricing information, see the [Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing#imagen-models) section of the [Cost of building and deploying AI models in Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing#imagen-models) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
