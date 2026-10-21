---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/configure-responsible-ai-safety-settings/
title: Configure Responsible AI safety settings \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:10.457210+00:00
---

# Configure Responsible AI safety settings  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/configure-responsible-ai-safety-settings/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Configure Responsible AI safety settings Stay organized with collections  Save and categorize content based on your preferences. 

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
  
[Try image generation (Vertex AI Studio)](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

[Try Imagen in a Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb)

This page describes how to set Responsible AI (RAI) filters in Imagen on Vertex AI.

There are several RAI filtering parameters that you can use with Imagen on Vertex AI models. For example, you can let the model report RAI filter codes for blocked content, disable people or face generation using RAI filters, set the level of content filtering, or return rounded RAI scores of list of safety attributes for input and output.

The available settings depend on the Imagen model version that you use. For more information, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models) and the [API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/image-generation).

For more information about RAI, see [Responsible AI and usage guidelines for Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen).

## Set RAI parameters

Do the following:

### Console

  1. In the Google Cloud console, go to the **Vertex AI > Vertex AI Studio ** page. 

[ Go to Vertex AI Studio ](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

  2. Click **Generate media**. 

  3. Click **Image**. 

  4. From the **Task** list, select an image generation task.

  5. From the **Model** list,choose a model from the available options.

For more information about available models, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models)

  6. In the **Prompt** box, enter your text prompt that describes the images to generate. For example, **small boat on water in the morning watercolor illustration**.

  7. To adjust additional features, click **Parameters** , and then adjust the following options:

     * **Number of results** : Adjust the slider or enter a value between **1** and **4**.
     * Select one of the following **Person generation** settings:

       * **Allow (Adults only)** : Allow generation of adults only, including celebrities.
       * **Allow (All ages)** : Allow generation of people including minors.
       * **Don't allow** : Don't generate people or faces.

The default setting depends on the model. For Imagen 4 generation models, `imagen-3.0-capability-002`, and `imagen-product-recontext`, the default is **Allow (All ages)**. For all other models, the default is **Allow (Adults only)**.

     * Select one of the following **Safety filter threshold** settings:

       * **Block most** : Blocks the most of the harmful content.
       * **Block some** : Blocks some problematic prompts and responses.
       * **Block few** : Blocks very few problematic prompts and responses.
  8. Click **Run**.




### REST

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt that guides what images the model generates. This field is required for both generation and editing. 
  * IMAGE_COUNT: The number of generated images. Accepted integer values: 1-8 (`imagegeneration@002`), 1-4 (all other model versions). Default value: 4.
  * SAFETY_SETTING: string. Optional. A setting that controls safety filter thresholds for generated images. Available values: 
    * `block_low_and_above`: The highest safety threshold, resulting in the largest amount of generated images that are filtered. Previous value: `block_most`. 
    * `block_medium_and_above` (default): A medium safety threshold that balances filtering for potentially harmful and safe content. Previous value: `block_some`. 
    * `block_only_high`: A safety threshold that reduces the number of requests blocked due to safety filters. This setting might increase objectionable content generated by Imagen. Previous value: `block_few`. 
  * PERSON_SETTING: string. Optional. The safety setting that controls the type of people or face generation the model allows. The default value is model-dependent. Available values: 
    * `allow_all`: Allow generation of people, including minors. This is the default for Imagen 4 generation models, imagen-3.0-capability-001, and imagen-product-recontext-preview-06-30. 
    * `allow_adult`: Allow generation of adults only, including celebrities. This is the default for all other models. 
    * `dont_allow`: Disable the inclusion of people or faces in generated images.
  * INCLUDE_RAI_REASON: boolean. Optional. Whether to enable the [Responsible AI filtered reason code](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-categories) in responses with blocked input or output. Default value: `true`. 
  * INCLUDE_SAFETY_ATTRIBUTES: boolean. Optional. Whether to enable rounded Responsible AI scores for a list of safety attributes in responses for unfiltered input and output. Safety attribute categories: `"Death, Harm & Tragedy"`, `"Firearms & Weapons"`, `"Hate"`, `"Health"`, `"Illicit Drugs"`, `"Politics"`, `"Porn"`, `"Religion & Belief"`, `"Toxic"`, `"Violence"`, `"Vulgarity"`, `"War & Conflict"`. Default value: `false`. 



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagegeneration@006:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "prompt": "TEXT_PROMPT"
        }
      ],
      "parameters": {
        "sampleCount": IMAGE_COUNT,**"safetySetting": " SAFETY_SETTING",
        "personGeneration": "PERSON_SETTING",
        "includeRaiReason": INCLUDE_RAI_REASON,
        "includeSafetyAttributes": INCLUDE_SAFETY_ATTRIBUTES**
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagegeneration@006:predict"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagegeneration@006:predict" | Select-Object -Expand Content

The response you get depends on the safety settings you set. For more information, see [Understand and configure Responsible AI (RAI) for Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen). 

## What's next

  * [Responsible AI and usage guidelines for Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
