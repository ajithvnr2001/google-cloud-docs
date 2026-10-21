---
url: https://docs.cloud.google.com/feeds/generative-ai-on-vertex-ai-release-notes.xml
title: Generative AI on Vertex AI - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:02:39.919534+00:00
---

# Generative AI on Vertex AI - Release notes

> Source: https://docs.cloud.google.com/feeds/generative-ai-on-vertex-ai-release-notes.xml

tag:google.com,2016:generative-ai-on-vertex-ai-release-notesGenerative AI on Vertex AI - Release notesGoogle Cloud Platform2026-05-26T00:00:00-07:00May 26, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#May_26_20262026-05-26T00:00:00-07:00Deprecated 

**Vertex AI Extensions deprecation**

Vertex AI Extensions is deprecated and will be shut down after November 26, 2026. We recommend [migrating to Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/migrate) to avoid service disruption.

]]> April 17, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#April_17_20262026-04-17T00:00:00-07:00Feature 

**RAG Cross Corpus Retrieval**

RAG Cross Corpus Retrieval is available in [public preview](https://cloud.google.com/products#product-launch-stages). This feature allows you to retrieve relevant contexts or generate answers from multiple RAG corpora simultaneously using the `AsyncRetrieveContexts` and `AskContexts` APIs.

For more information, see [RAG Cross Corpus Retrieval](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/cross-corpus-retrieval).

]]> April 14, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#April_14_20262026-04-14T00:00:00-07:00Feature 

**Anthropic's Claude Opus 4.7**

[Claude Opus 4.7](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/opus-4-7) is available in Model Garden.

]]> April 06, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#April_06_20262026-04-06T00:00:00-07:00Feature 

**Metadata search for RAG Engine**

Use schema-based metadata search in Vertex AI RAG Engine. You can define a metadata schema for a corpus, attach metadata to files within that corpus, and use this metadata to filter contexts during retrieval. For more information, see [Filter with metadata search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/use-metadata-search).

]]> April 03, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#April_03_20262026-04-03T00:00:00-07:00Feature 

**Gemma 4 26B A4B IT** is available as an experimental launch in Model Garden. This is an open model built by Google DeepMind. Gemma 4 models are multimodal, handling text and image input and generating text output. Gemma 4 26B A4B IT is available as a managed API in Model Garden. To learn more, see [Gemma 4 26B A4B IT](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/google/gemma-4-26b-a4b-it).

### Feature

**Vertex AI RAG Engine Serverless mode**

Vertex AI RAG Engine Serverless mode is now available in [public preview](https://cloud.google.com/products#product-launch-stages). Serverless mode provides a fully managed database for storing RAG resources that abstracts away database provisioning and scaling. You can seamlessly switch between Serverless mode and Spanner mode, which provides dedicated, isolated database instances.

For more information, see the following:

  * [Deployment modes in Vertex AI RAG Engine](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/deployment-modes)
  * [Serverless mode](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/serverless-mode)
  * [Managing Spanner mode](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/spanner-mode)
  * [Switching between modes](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/switching-modes)

]]> April 02, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#April_02_20262026-04-02T00:00:00-07:00Feature 

**Veo 3.1 Lite**

Veo 3.1 Lite is available in [public preview](https://cloud.google.com/products#product-launch-stages). This release is our most cost-efficient Veo on Vertex AI model.

For more information, see [3.1 Lite Generate](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/veo/3-1-generate#3.1-lite-generate-001)

### Announcement

**Gemini 2.5 model retirement dates updated**

The retirement dates for Gemini 2.5 Pro, Gemini 2.5 Flash-Lite, and Gemini 2.5 Flash have been updated to October 16, 2026. For more information, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).

]]> March 25, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#March_25_20262026-03-25T00:00:00-07:00Feature 

**Lyria 3**

Lyria is available in [public preview](https://cloud.google.com/products#product-launch-stages). You can use `lyria-3-pro-preview` to generate 184 seconds of audio, or `lyria-3-clip-preview` to generate 30 seconds of audio.

For more information, see the following:

  * [Lyria 3 Pro Preview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/lyria/lyria-3#lyria-3-pro-preview)

  * [Lyria 3 Clip Preview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/lyria/lyria-3#lyria-3-clip-preview)


]]> March 24, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#March_24_20262026-03-24T00:00:00-07:00Deprecated 

**Imagen generation GA endpoints deprecation**

The following table describes image generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before June 30, 2026, to avoid service disruption.

Discontinued endpoints | Recommended endpoint migration  
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
  
### Deprecated

**Video generation GA endpoints deprecation**

The following table describes video generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before June 30, 2026, to avoid service disruption.

Discontinued endpoints | Recommended endpoint migration  
---|---  
`veo-3.0-generate-001` | `veo-3.1-generate-001`  
`veo-3.0-fast-generate-001` | `veo-3.1-fast-generate-001`  
`veo-2.0-generate-001` | `veo-3.1-generate-001`  
]]> March 12, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#March_12_20262026-03-12T00:00:00-07:00Feature 

**Partner model evaluations**

The Gen AI evaluation service supports evaluating partner models, such as Anthropic and Llama models. For more information, see [Perform evaluation using the console](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-genai-console#evaluate_partner_models).

]]> March 03, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#March_03_20262026-03-03T00:00:00-08:00Deprecated 

**Video generation preview endpoints deprecation**

The following table describes video generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before April 2, 2026, to avoid service disruption.

Discontinued endpoints | Recommended endpoint migration  
---|---  
`veo-3.0-generate-preview` | `veo-3.0-generate-001`  
`veo-3.0-fast-generate-preview` | `veo-3.0-fast-generate-preview`  
`veo-2.0-generate-preview` | `veo-2.0-generate-001`  
`veo-2.0-generate-exp` | `veo-2.0-generate-001`  
`veo-001-preview-0815` | `veo-2.0-generate-001`  
`veo-001-preview` | `veo-2.0-generate-001`  
`veo-3.1-generate-preview` | `veo-3.1-generate-001`  
`veo-3.1-fast-generate-preview` | `veo-3.1-fast-generate-001`  
  
### Feature

**Gemini 3.1 Flash-Lite**

Gemini 3.1 Flash-Lite (`gemini-3.1-flash-lite`) is available in [public preview](https://cloud.google.com/products#product-launch-stages). This release is our most cost-efficient Gemini model and is optimized for low latency use cases for high-volume, cost-sensitive LLM traffic.

For more information, see [Gemini 3.1 Flash-Lite](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-flash-lite).

]]> February 26, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_26_20262026-02-26T00:00:00-08:00Feature 

**Gemini 3.1 Flash Image**

Gemini 3.1 Flash Image (`gemini-3.1-flash-image`) is available in [public preview](https://cloud.google.com/products#product-launch-stages). This release enables high-quality image generation with improved pricing and latency. We recommend using Gemini 3.1 Flash Image when generating images.

For more information, see [Gemini 3.1 Flash Image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-flash-image).

]]> February 23, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_23_20262026-02-23T00:00:00-08:00Deprecated 

**Anthropic's Claude 3 Haiku**

Anthropic's Claude 3 Haiku is deprecated as of February 23, 2026 and will be shut down on August 23, 2026. For more information, see [Partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models#haiku-3).

]]> February 19, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_19_20262026-02-19T00:00:00-08:00Feature 

**Gemini 3.1 Pro Preview**

[Gemini 3.1 Pro](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-pro) is available in preview in Model Garden. Gemini 3.1 Pro is our most advanced reasoning Gemini model, capable of solving complex problems from different information sources, including text, audio, images, video, PDFs, and even entire code repositories with its 1M token context window.

]]> February 17, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_17_20262026-02-17T00:00:00-08:00Feature 

**Anthropic's Claude Sonnet 4.6**

[Claude Sonnet 4.6](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/sonnet-4-6) is available in Model Garden.

### Deprecated

**Image generation preview endpoints deprecation**

The following table describes image generation endpoints that are deprecated and their replacements. We recommend updating your model endpoints before March 19, 2026, to avoid service disruption.

Discontinued endpoints | Recommended endpoint migration  
---|---  
`gemini-2.0-flash-image-generation-preview` | `gemini-2.5-flash-image`  
`gemini-2.5-flash-image-generation-preview` | `imagen-4.0-generate-001` or `gemini-2.5-flash-image`  
`imagen-4.0-generate-preview-05-20` | `imagen-4.0-generate-001` or `gemini-2.5-flash-image`  
`imagen-4.0-generate-preview-06-06` | `imagen-4.0-generate-001` or `gemini-2.5-flash-image`  
`imagen-4.0-ultra-generate-preview-06-06` | `imagen-4.0-generate-001` or `gemini-2.5-flash-image`  
`imagen-4.0-fast-generate-preview-05-20` | `imagen-4.0-generate-001` or `gemini-2.5-flash-image`  
`imagen-product-recontext-preview-06-30` | `gemini-2.5-flash-image`  
`imagen-2.0-edit-preview-0627` | `gemini-2.5-flash-image`  
`virtual-try-on-preview-08-04` | `virtual-try-on-001`  
`imagen-4.0-ingredients-preview` | `gemini-2.5-flash-image`  
]]> February 10, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_10_20262026-02-10T00:00:00-08:00Feature 

**GLM 5** is available as an experimental launch in Model Garden. This model is targeting complex systems engineering and long-horizon agentic tasks. GLM 5 is available as a managed API in Model Garden. To learn more, see [GLM 5](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/zai-org/glm-5).

]]> February 04, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#February_04_20262026-02-04T00:00:00-08:00Feature 

**Anthropic's Claude Opus 4.6**

[Claude Opus 4.6](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude/opus-4-6) is available in Model Garden.

]]> January 23, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_23_20262026-01-23T00:00:00-08:00Feature 

**Virtual Try-On**

Virtual Try-On is now [generally available (GA)](https://cloud.google.com/products/#product-launch-stages). The new endpoint, `virtual-try-on-001`, replaces the previous endpoint, `virtual-try-on-preview-08-04`. We recommend changing to the new endpoint as soon as possible.

For more information, see [Generate Virtual Try-On Images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-virtual-try-on-images).

]]> January 22, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_22_20262026-01-22T00:00:00-08:00Announcement 

Codestral (25.01) and Mistral Large (24.11) are retired as of January 23, 2026.

]]> January 20, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_20_20262026-01-20T00:00:00-08:00Feature 

**GLM 4.7** GA is now available in Model Garden. This model is designed for core or vibe coding, tool use, and complex reasoning. GLM 4.7 is available as a managed API in Model Garden. To learn more, see [GLM 4.7](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/zai-org/glm-47).

]]> January 13, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_13_20262026-01-13T00:00:00-08:00Feature 

**Veo 3.1 reference-to-video update**

Veo 3.1 Preview models now support the following features:

  * 9:16 aspect ratio for reference-to-video.
  * Upsampling for videos generated at 1080p and 4k resolutions.



For more information, see the following:

  * [Generate Veo videos from reference images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/use-reference-images-to-guide-video-generation)
  * [Veo on Vertex AI video generation API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation)

]]> January 06, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_06_20262026-01-06T00:00:00-08:00Feature 

**GLM 4.7** is available as an experimental launch in Model Garden. This model is designed for core or vibe coding, tool use, and complex reasoning. GLM 4.7 is available as a managed API in Model Garden. To learn more, see [GLM 4.7](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/zai-org/glm-47).

]]> January 05, 2026tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#January_05_20262026-01-05T00:00:00-08:00Deprecated 

**Anthropic's Claude 3.5 Haiku**

Anthropic's Claude 3.5 Haiku is deprecated as of January 5, 2026 and will be shut down on July 5, 2026. For more information, see [Partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models#haiku-3-5).

]]> December 18, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_18_20252025-12-18T00:00:00-08:00Feature 

The following models are available through Model Garden:

  * [FunctionGemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/functiongemma)
  * [T5Gemma 2](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/t5gemma)



### Feature

**Save and share prompts in Vertex AI Studio** : The prompt sharing feature no longer needs to be enabled. You can share prompts without asking your administrator to first enable the prompt sharing feature. For more information, see [Save and share prompts](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/prompt-sharing).

]]> December 17, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_17_20252025-12-17T00:00:00-08:00Feature 

[Cloud API Registry](https://docs.cloud.google.com/api-registry/docs/overview) is available in the Google Cloud console in [Preview](https://cloud.google.com/products#product-launch-stages). Use Cloud API Registry in the Google Cloud console to view and manage the MCP servers and tools your agent has access to.

### Feature

**Gemini 3 Flash**

Gemini 3 Flash is now available in public preview. This model is designed to tackle the most challenging agentic problems with strong coding and state-of-the-art reasoning capabilities, and is our best model for complex multimodal understanding.

For more information, see [Gemini 3 Flash](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-flash).

]]> December 16, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_16_20252025-12-16T00:00:00-08:00Change 

Updated pricing for **Vertex AI Agent Engine** :

  * Pricing for Vertex AI Agent Engine Runtime was lowered.

  * On **January 28, 2026** , Sessions, Memory Bank, and Code Execution will begin charging for usage.




For more information, see [Pricing](https://cloud.google.com/vertex-ai/pricing#vertex-ai-agent-engine).

### Announcement

**Vertex AI Agent Engine**

Vertex AI Agent Engine [Sessions](https://docs.cloud.google.com/agent-builder/agent-engine/sessions/overview) and [Memory Bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) are now [Generally Available](https://cloud.google.com/products#product-launch-stages).

### Change

**Vertex AI Agent Engine**

Vertex AI Agent Engine is now available in the following regions:

  * `europe-west6` (Zurich)
  * `europe-west8` (Milan)
  * `asia-east2` (Hong Kong)
  * `asia-northeast3` (Seoul)
  * `asia-southeast2` (Jakarta)
  * `northamerica-northeast2` (Toronto)
  * `southamerica-east1` (São Paulo)



For more information, see [Vertex AI Agent Builder locations](https://docs.cloud.google.com/agent-builder/locations).

### Change

**Virtual Try-On**

Our Virtual Try-On model, `virtual-try-on-preview-08-04`, is improved. Latency is significantly reduced and quality is improved for shoes, body shape preservation, and product fidelity.

]]> December 12, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_12_20252025-12-12T00:00:00-08:00Feature 

**Gemini 2.5 Flash with Gemini Live API Native Audio**

[Gemini 2.5 Flash with Gemini Live API Native Audio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/2-5-flash-live-api) (`gemini-live-2.5-flash-native-audio`) is Generally Available (GA). This model features cutting-edge native audio functionality for [Gemini Live API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api), including enhanced voice quality and adaptability, Proactive Audio, and Affective Dialog.

]]> December 10, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_10_20252025-12-10T00:00:00-08:00Feature 

**DeepSeek-V3.2** is available in Model Garden. DeepSeek-V3.2 is a state-of-the-art large language model from DeepSeek. DeepSeek-V3.2 is available as a managed API in Model Garden. To learn more, see [DeepSeek-V3.2](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/deepseek/deepseek-v32).

]]> December 09, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_09_20252025-12-09T00:00:00-08:00Feature 

The following models are available through Model Garden:

  * [Ministral 3](https://console.cloud.google.com/vertex-ai/publishers/mistralai/model-garden/ministral-3)
  * [Mistral Large 3](https://console.cloud.google.com/vertex-ai/publishers/mistralai/model-garden/mistral-large-3)

]]> December 08, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_08_20252025-12-08T00:00:00-08:00Feature 

**Veo 3.1 video extension**

Veo 3.1 supports video extension in Preview.

For more information, see the following:

  * [Extend Veo videos](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/extend-a-veo-video)
  * [Veo video generation API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/veo-video-generation)

]]> December 02, 2025tag:google.com,2016:generative-ai-on-vertex-ai-release-notes#December_02_20252025-12-02T00:00:00-08:00Feature 

The following models are available through Model Garden:

  * [DeepSeek-V3.2](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-2;publisherModelVersion=deepseek-v3-2)
  * [DeepSeek-V3.2-Speciale](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-2;publisherModelVersion=deepseek-v3-2-speciale)



### Feature

The Vertex AI Model Garden model co-hosting vLLM container is available to use with [this sample notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_model_cohost.ipynb). You can use this container to serve multiple replicas of a model and serve multiple models with dynamic loading and unloading. This allows you to maximize resource utilization and serving efficiency, and flexibly adjust the models to serve.

]]>
