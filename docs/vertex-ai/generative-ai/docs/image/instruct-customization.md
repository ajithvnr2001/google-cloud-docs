---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/instruct-customization/
title: Instruct Customization \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:12.160893+00:00
---

# Instruct Customization  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/instruct-customization/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Instruct Customization Stay organized with collections  Save and categorize content based on your preferences. 

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
  
You can use Imagen on Vertex AI to instruct the model how to customize and transform the subjects in an image to a style that you specify in a text prompt.

The following models support Instruct Customization:

  * [ `imagen-3.0-capability-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-capability-001)



[View Imagen for Editing and Customization model card](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/imagen-3.0-capability-001)

## Customization prompt writing

The prompt that you use with Imagen 3 Customization might affect the quality of your generated images. Use the following prompt templates as a starting point for writing customization prompts. You might need to send several requests to get your targeted output.

Use case | Reference images | Prompt template | Example  
---|---|---|---  
Instruct customization - Style transfer | Image (1) | Transform the subject in image [1] to have a style of _${STYLE_DESCRIPTION}_. The image depicts _${IMAGE_DESCRIPTION}_.  | Transform the subject in image [1] to have a style of _a watercolor painting of the image with loose watercolor techniques, soft tone, pastel colors, brush strokes, delicate, clean background, spontaneity, analog style drawing, intricate highly detailed painting_. The image depicts _a portrait of a proud woman_.   
  
## Customize using instruct customization for style transfer

To see an example of Imagen 3 Customization, run the "Imagen 3 Customized Images" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_customization.ipynb)

Use the following code samples to specify the style of the output images based on the style described in the text prompt.

### REST

For more information about the Imagen API, see the following: 

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt guides what images the model generates. To use Imagen 3 Customization, include the `referenceId` of the reference image or images you provide in the format [$referenceId]. For example: 
    * _Transform the subject in image[1] to have a Digital Stained Glass style image style. _
    * _Add a red cowboy hat to the cat in the image[1]._
    * _Remove the corgi dog in the image[1]._
    * _Change the red ball in the image[1] to a blue box._
  * `"referenceId"`: The ID of the reference image, or the ID for a series of reference images that correspond to the same subject or style. 
  * BASE64_REFERENCE_IMAGE: A reference image to guide image generation. The image must be specified as a [base64-encoded](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode) byte string. 
  * IMAGE_COUNT: The number of generated images. Accepted integer values: 1-4. Default value: 4. 



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/**imagen-3.0-capability-001** :predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "prompt": "TEXT_PROMPT",
          "referenceImages": [
            {
              "referenceType": "REFERENCE_TYPE_RAW",
              "referenceId": 1,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              }
            }
          ]
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/**imagen-3.0-capability-001** :predict"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/**imagen-3.0-capability-001** :predict" | Select-Object -Expand Content

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
    

## Product usage

To view usage standards and content restrictions associated with Imagen on Vertex AI, see the [usage guidelines](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#imagen-guidelines).

## Model versions

There are multiple image generation models that you can use. For more information, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models).

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
