---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images/
title: Generate images using text prompts with Imagen on Vertex AI \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:09.354356+00:00
---

# Generate images using text prompts with Imagen on Vertex AI  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Generate images using text prompts with Imagen on Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

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
  
You can use Imagen on Vertex AI to generate new images from a text prompt. Supported interfaces include the Google Cloud console and the Vertex AI API.

The following models support generating images from text prompts:

  * [ `imagen-3.0-generate-002`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-generate-002)
  * [ `imagen-3.0-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-generate-001)
  * [ `imagen-3.0-fast-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-fast-generate-001)
  * [ `imagen-4.0-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-generate-001)
  * [ `imagen-4.0-fast-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-fast-generate-001)
  * [ `imagen-4.0-ultra-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-ultra-generate-001)

For more information about writing text prompts for image generation and editing, see the [prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide). 

[View Imagen for Generation model card](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/imagen-4.0-generate-preview-06-06)

[Try image generation (Vertex AI Studio)](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

[Try Imagen in a Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb)

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  8. Set up authentication for your environment.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




[](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/text-image-gen)

## Generate images with text

You can generate novel images using only descriptive text as an input. The following samples show you basic instructions to generate images.

**Important:** `imagen-4.0-fast-generate-001` may generate undesireable results if the prompt is complex and you use enhanced prompts. To fix this, avoid using **Help me write** in Google Cloud console, or set `enhancePrompt` to `false`.

### Console

1\. In the Google Cloud console, go to the **Vertex AI > Media Studio** page. 
    
    
    <a href="https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image" class="button button-primary"
    target="console" track-name="consoleLink" track-type="task">Go to Media
    Studio</a>
    

  1. Click **Imagen**. The Imagen Media Studio image generation page is displayed.

  2. Optional: In the **Settings** pane, configure the following settings:

     * **Model** : Choose a model from the available options.

For more information about available models, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models)

     * **Aspect ratio** : Choose an aspect ratio from the available options.

     * **Number of results** : Adjust the slider or enter a value between **1** and **4**.

     * **Output resolution** : Choose a resolution from the available options.

  3. Optional: In the **Advanced options** section, select a **Region** to generate your images in.

  4. In the **Write your prompt** box, enter your text prompt that describes the images to generate. For example, **small boat on water in the morning watercolor illustration**.

For more information about writing effective prompts, see [Prompt and image attribute guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide).

  5. Click send **Generate**.




A digital watermark is automatically added to generated images. You can't disable digital watermark for image generation using the Google Cloud console.

You can select an image to view in the **Image detail** window. Watermarked images contain a local_police**Digital watermark** badge.

![A sample watermarked generated image using text](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/image-gen_image-detail_watermarked.png)**Image detail** view of a watermarked image generated with Imagen 2 from the prompt: _small red boat on water in the morning watercolor illustration muted colors_.

### REST

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * REGION: The region that your project is located in. For more information about supported regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations). 
  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * MODEL_VERSION: The Imagen model version to use. For more information about available models, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models). 

  * TEXT_PROMPT: The text prompt that guides what images the model generates. This field is required for both generation and editing. 
  * IMAGE_COUNT: The number of images to generate. The accepted range of values is `1` to `4`. 

**Additional optional parameters**

Use the following optional variables depending on your use case. Add some or all of the following parameters in the `"parameters": {}` object. This list shows common optional parameters and isn't meant to be exhaustive. For more information about optional parameters, see [Imagen API reference: Generate images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api). 
    
    "parameters": {
      "sampleCount": IMAGE_COUNT,**"addWatermark": ADD_WATERMARK,
      "aspectRatio": "ASPECT_RATIO",
      "enhancePrompt": ENABLE_PROMPT_REWRITING,
      "includeRaiReason": INCLUDE_RAI_REASON,
      "includeSafetyAttributes": INCLUDE_SAFETY_ATTRIBUTES,
      "outputOptions": {
        "mimeType": "MIME_TYPE",
        "compressionQuality": COMPRESSION_QUALITY
      },
      "personGeneration": "PERSON_SETTING",
      "safetySetting": "SAFETY_SETTING",
      "seed": SEED_NUMBER,
      "storageUri": "OUTPUT_STORAGE_URI"**
    }
    

    * ADD_WATERMARK: boolean. Optional. Whether to enable a watermark for generated images. Any image generated when the field is set to `true` contains a digital [SynthID](https://deepmind.google/technologies/synthid/) that you can use to verify a watermarked image. If you omit this field, the default value of `true` is used; you must set the value to `false` to disable this feature. You can use the `seed` field to get deterministic output only when this field is set to `false`. 
    * ASPECT_RATIO: string. Optional. A generation mode parameter that controls aspect ratio. Supported ratio values and their intended use: 
      * `1:1` (default, square)
      * `3:4` (Ads, social media)
      * `4:3` (TV, photography)
      * `16:9` (landscape)
      * `9:16` (portrait)
    * ENABLE_PROMPT_REWRITING: boolean. Optional. A parameter to use an LLM-based prompt rewriting feature to deliver higher quality images that better reflect the original prompt's intent. Disabling this feature may impact image quality and prompt adherence. Default value: `true`. 
    * INCLUDE_RAI_REASON: boolean. Optional. Whether to enable the [Responsible AI filtered reason code](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-categories) in responses with blocked input or output. Default value: `true`. 
    * INCLUDE_SAFETY_ATTRIBUTES: boolean. Optional. Whether to enable rounded Responsible AI scores for a list of safety attributes in responses for unfiltered input and output. Safety attribute categories: `"Death, Harm & Tragedy"`, `"Firearms & Weapons"`, `"Hate"`, `"Health"`, `"Illicit Drugs"`, `"Politics"`, `"Porn"`, `"Religion & Belief"`, `"Toxic"`, `"Violence"`, `"Vulgarity"`, `"War & Conflict"`. Default value: `false`. 
    * MIME_TYPE: string. Optional. The MIME type of the content of the image. Available values: 
      * `image/jpeg`
      * `image/gif`
      * `image/png`
      * `image/webp`
      * `image/bmp`
      * `image/tiff`
      * `image/vnd.microsoft.icon`
    * COMPRESSION_QUALITY: integer. Optional. Only applies to JPEG output files. The level of detail the model preserves for images generated in JPEG file format. Values: `0` to `100`, where a higher number means more compression. Default: `75`. 
    * PERSON_SETTING: string. Optional. The safety setting that controls the type of people or face generation the model allows. The default value is model-dependent. Available values: 
      * `allow_all`: Allow generation of people, including minors. This is the default for Imagen 4 generation models, imagen-3.0-capability-001, and imagen-product-recontext-preview-06-30. 
      * `allow_adult`: Allow generation of adults only, including celebrities. This is the default for all other models. 
      * `dont_allow`: Disable the inclusion of people or faces in generated images.
    * SAFETY_SETTING: string. Optional. A setting that controls safety filter thresholds for generated images. Available values: 
      * `block_low_and_above`: The highest safety threshold, resulting in the largest amount of generated images that are filtered. Previous value: `block_most`. 
      * `block_medium_and_above` (default): A medium safety threshold that balances filtering for potentially harmful and safe content. Previous value: `block_some`. 
      * `block_only_high`: A safety threshold that reduces the number of requests blocked due to safety filters. This setting might increase objectionable content generated by Imagen. Previous value: `block_few`. 
    * SEED_NUMBER: integer. Optional. Any non-negative integer you provide to make output images deterministic. Providing the same seed number always results in the same output images. If the model you're using supports digital watermarking, you must set `"addWatermark": false` to use this field. Accepted integer values: `1` \- `2147483647`. 
    * OUTPUT_STORAGE_URI: string. Optional. The Cloud Storage bucket to store the output images. If not provided, base64-encoded image bytes are returned in the response. Sample value: `gs://image-bucket/output/`. 



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/MODEL_VERSION:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "prompt": "TEXT_PROMPT"
        }
      ],
      "parameters": {
        "sampleCount": IMAGE_COUNT
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/MODEL_VERSION:predict"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/MODEL_VERSION:predict" | Select-Object -Expand Content

The following sample response is for a request with `"sampleCount": 2`. The response returns two prediction objects, with the generated image bytes base64-encoded. 
    
    
    {
      "predictions": [
        {
          "bytesBase64Encoded": "BASE64_IMG_BYTES",
          "mimeType": "image/png"
        },
        {
          "mimeType": "image/png",
          "bytesBase64Encoded": "BASE64_IMG_BYTES"
        }
      ]
    }

If you use a model that supports prompt enhancement, the response includes an additional `prompt` field with the enhanced prompt used for generation: 
    
    
    {
      "predictions": [
        {
          "mimeType": "MIME_TYPE",**"prompt": " ENHANCED_PROMPT_1",**
          "bytesBase64Encoded": "BASE64_IMG_BYTES_1"
        },
        {
          "mimeType": "MIME_TYPE",**"prompt": " ENHANCED_PROMPT_2",**
          "bytesBase64Encoded": "BASE64_IMG_BYTES_2"
        }
      ]
    }
    

## What's next

Read articles about Imagen and other Generative AI on Vertex AI products:

  * [A developer's guide to getting started with Imagen 3 on Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/a-developers-guide-to-imagen-3-on-vertex-ai?e=0?utm_source%3Dlinkedin)
  * [New generative media models and tools, built with and for creators](https://blog.google/technology/ai/google-generative-ai-veo-imagen-3/#veo)
  * [New in Gemini: Custom Gems and improved image generation with Imagen 3](https://blog.google/products/gemini/google-gemini-update-august-2024/)
  * [Google DeepMind: Imagen 3 - Our highest quality text-to-image model](https://deepmind.google/technologies/imagen-3/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
