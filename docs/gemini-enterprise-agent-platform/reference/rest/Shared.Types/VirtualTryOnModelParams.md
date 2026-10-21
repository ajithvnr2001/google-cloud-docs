---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelParams/
title: VirtualTryOnModelParams \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:10:53.088436+00:00
---

# VirtualTryOnModelParams  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelParams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VirtualTryOnModelParams Stay organized with collections  Save and categorize content based on your preferences. 

Represents the parameters for a Virtual Try-On prediction request.

Fields  
  
`outputOptions` `object (`[OutputOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/OutputOptions)`)` Options for configuring the output image format. | `sampleCount` `integer` The number of images to generate. Accepted values are in the range [1,4].If not set, defaults to `1`. | `storageUri` `string` The Google Cloud Storage location where the generated images are stored. | `seed` `integer` The random seed for image generation. This avoids randomness in generating the output images.If a `[seed](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelParams#FIELDS.seed)` value is provided, `[addWatermark](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelParams#FIELDS.add_watermark)` must be set to `false`. | `baseSteps` `integer` The number of diffusion steps to run. The higher the number of steps, the higher the quality of the generated image, but the greater the latency.If not set, defaults to `32`. | `safetySetting` `string` Safety filter level for generated images. The filter blocks images that contain objectionable content.The following values are supported:

  * `block-low-and-above`: Strongest filtering level, most strict blocking.
  * `block-medium-and-above`: Block some problematic content prompts and responses.
  * `block-only-high`: Reduces the number of requests blocked due to safety filters. May increase objectionable content in generated images.
  * `block-none`: Block very few problematic prompts and responses. Access to this feature is restricted.

If not set, defaults to `block_medium_and_above`. | `personGeneration` `string` Controls whether or not faces or people are included in generated images.The following values are supported:

  * `dont-allow`: Disallow the inclusion of faces or people in generated images.
  * `allow-adult`: Allow generation of adults only.
  * `allow-all`: Allow generation of people of all ages.

If not set, defaults to `allow-adult`. | `addWatermark` `boolean` Whether to add a watermark to the generated images.If not set, defaults to `true`. | `enhancePrompt` `boolean` Whether to enhance the user-provided prompt internally for models that support it.If not set, defaults to `true`. | JSON representation  
---  
      
    
    {
      "outputOptions": {
        object ([OutputOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/OutputOptions))
      },
      "sampleCount": integer,
      "storageUri": string,
      "seed": integer,
      "baseSteps": integer,
      "safetySetting": string,
      "personGeneration": string,
      "addWatermark": boolean,
      "enhancePrompt": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
