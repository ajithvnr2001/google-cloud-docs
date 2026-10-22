---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/embedding-2/
title: Gemini Embedding 2 \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:43:07.467487+00:00
---

# Gemini Embedding 2  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/embedding-2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Gemini Embedding 2 Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Embedding 2 is Google's embedding generation model that's ideal for complex retrieval and analytics tasks.

Gemini Embedding 2 accepts multimodal inputs to generate 3072-dimensional vectors. It accepts images, text, documents, audio, and video inputs and semantically maps the generated vectors into a unified semantic space. This lets you perform tasks, such as searching for an image based on a text description.

Gemini Embedding 2 introduces several features to optimize embedding quality and flexibility:

  * **Custom task instructions:** By specifying task instructions (for example, `task:code retrieval` or `task:search result`) optimize the embeddings for the intended relationships and retrieve more accurate results for the specific goal.

  * **Adjustable result size:** The model generates a 3072-dimensional float vector, by default. However, you can retrieve a smaller dimensional output by specifying the `output_dimensionality` parameter.

  * **Document OCR:** Read OCR from document inputs.

  * **Audio track extraction:** Extract audio tracks from video inputs and interleave them with video frames.




For more information on how to use Gemini Embedding 2, see [Get multimodal embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/get-multimodal-embeddings).

[Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)

Model ID | `gemini-embedding-2`  
---|---  
Modalities |  description  Text   
Input only  photo  Image   
Input only  mic  Audio   
Input only  videocam  Video   
Input only  graph_3  Embeddings   
Output only   
Token limits | Maximum input tokens | 8,192  
Maximum output tokens | N/A  
Output dimensions |  Up to 3,072 (with MRL support)   
Maximum sequence length |  8,192 tokens   
Consumption options | 

  * [Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput)   
Not supported
  * [Batch inference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings/batch-prediction-genai-embeddings)   
Supported
  * [Pay-as-you-go](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/consumption-options)   
Standard PayGo  
Supported
  * [Fixed quota](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/quotas)   
Not supported

  
Technical specifications |  **Text** description | 

  * Maximum input tokens: 8,192
  * Maximum number of files per prompt: 1
  * Maximum number of pages per file (for PDF): 6
  * Maximum file size per file: N/A
  * OCR for scanned PDFs: Not used by default
  * Supported MIME types: `text/plain`, `application/pdf`

  
**Image** photo | 

  * Maximum images per prompt: 6
  * Maximum file size per file for inline data or direct uploads through the console: No limit
  * Maximum file size per file from Google Cloud Storage: No limit
  * Maximum number of output images per prompt: N/A
  * Supported MIME types: `image/png`, `image/jpeg`, `image/webp`, `image/bmp`, `image/heic`, `image/heif`, `image/avif`

  
**Video** videocam | 

  * Maximum video length (with audio): 80 seconds
  * Maximum video length (without audio): 120 seconds
  * Maximum number of videos per prompt: 1
  * Supported MIME types: `video/mpeg`, `video/mp4`

  
**Audio** mic | 

  * Maximum audio length per prompt: 180 seconds
  * Maximum number of audio files per prompt: 1
  * Supported MIME types: `audio/mp3`, `audio/wav`

  
Supported regions |  **[Model availability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/locations) ** | 

  * Global: `global`
  * United States multi-region: `us`
  * Europe multi-region: `eu`

  
Knowledge cutoff date |  November 2025   
Versions | 

  * `gemini-embedding-2`
    * Launch stage: GA
    * Release date: April 22, 2026
  * `gemini-embedding-2-preview`
    * Launch stage: Public preview
    * Release date: March 10, 2026

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
