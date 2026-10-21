---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/use-prompt-rewriter/
title: Use prompt rewriter \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:10.556862+00:00
---

# Use prompt rewriter  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/use-prompt-rewriter/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Use prompt rewriter Stay organized with collections  Save and categorize content based on your preferences. 

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

[Try Imagen in a Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb) Imagen on Vertex AI offers an LLM-based prompt rewriting tool, also known as a prompt rewriter. The prompt rewriter helps you obtain higher quality output images by adding more detail to your prompt.

If you disable the prompt rewriter, the quality of the images and how well the output resembles the prompt that you supplied may be impacted. This feature is enabled by default for the following model versions:

  * [ `imagen-3.0-generate-002`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-generate-002)
  * [ `imagen-4.0-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-generate-001)
  * [ `imagen-4.0-fast-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-fast-generate-001)
  * [ `imagen-4.0-ultra-generate-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/4-0-generate#4.0-ultra-generate-001)



The rewritten prompt is delivered by API response only if the original prompt is fewer than 30 words long.

**Important:** `imagen-4.0-fast-generate-001` may generate undesireable results if the prompt is complex and you use enhanced prompts. To fix this, avoid using **Help me write** in Google Cloud console, or set `enhancePrompt` to `false`.

## Use the prompt rewriter

To use the prompt rewriter, do the following:

### Console

  1. In the Google Cloud console, go to the **Vertex AI > Media Studio** page.

[Go to Media Studio](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

  2. Click **Imagen**. The Imagen Media Studio image generation page is displayed.

  3. In the **Settings** panel, adjust the following options:

     * **Model** : Choose a model from the available options.

For more information about available models, see [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models)

     * **Number of results** : Adjust the slider or enter a value between **1** and **4**.

     * In the **Negative prompt** box, enter a prompt that describes what you don't want generated in the image.

  4. In the **Write your prompt** box, click **Help me write**.

The **Enhance my prompt** window is displayed.

  5. In the **Current prompt** box, write your prompt, and then click **Enhance**.

The rewritten prompt is displayed in the **Enhanced prompt** box. You can edit the enhanced prompt or use it as displayed.

  6. Click **Insert** to use the displayed prompt.

The prompt is inserted into the **Write your prompt** box.

  7. Click send **Generate**.




### REST

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * MODEL_VERSION: The image generation model version to use. 

For more information about model versions and features, see model versions. 

  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt that guides what images the model generates. Before images are generated, this base prompt is enhanced with more detail and descripitive language using the LLM-based prompt rewriting tool. 
  * IMAGE_COUNT: An integer, describing the number of images to generate. The accepted values are `1`-`4`. The default value is `4`. 
  * PROMPT_SETTING: A boolean value, `true` enables enhanced prompts and `false` disables enhanced prompts. The default value is `true`. 



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_VERSION:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "prompt": "TEXT_PROMPT"
        }
      ],
      "parameters": {
        "sampleCount": IMAGE_COUNT,**"enhancePrompt": PROMPT_SETTING**
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_VERSION:predict"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/MODEL_VERSION:predict" | Select-Object -Expand Content

With prompt enhancement enabled, the response includes an additional `prompt` field that shows the enhanced prompt and its associated generated image: 
    
    
      {
        "predictions": [
          {
            "mimeType": "MIME_TYPE",**        "prompt": "ENHANCED_PROMPT_1",**
            "bytesBase64Encoded": "BASE64_IMG_BYTES_1"
          },
          {
            "mimeType": "MIME_TYPE",**        "prompt": "ENHANCED_PROMPT_2",**
            "bytesBase64Encoded": "BASE64_IMG_BYTES_2"
          }
        ]
      }

For example, the following sample response is for a request with `"sampleCount": 2` and `"prompt": "A raccoon wearing formal clothes, wearing a top hat. Oil painting in the style of Vincent Van Gogh."`. The response returns two prediction objects, each with their enhanced prompt and the generated image bytes base64-encoded. 
    
    
    {
      "predictions": [
        {
          "mimeType": "image/png",**"prompt": " An oil painting in the style of Vincent van Gogh,
            depicting a raccoon adorned in a finely tailored tuxedo, complete with a
            crisp white shirt and a bow tie. The raccoon also sports a classic top
            hat, perched jauntily on its head. The painting uses thick, swirling
            brushstrokes characteristic of van Gogh, with vibrant hues of blue,
            yellow, and green in the background, contrasting with the dark tones of
            the raccoon's attire. The light source is subtly placed, casting a
            dramatic shadow of the raccoon's attire onto the surface it sits upon,
            further enhancing the depth and dimensionality of the composition. The
            overall impression is one of a whimsical and sophisticated character, a
            raccoon elevated to a higher class through its formal attire, rendered
            in van Gogh's iconic style.",**
          "bytesBase64Encoded": "BASE64_IMG_BYTES"
        },
        {
          "mimeType": "image/png",**"prompt": " An oil painting in the style of Vincent van Gogh featuring
            a raccoon in a dapper suit, complete with a black jacket, crisp white
            shirt, and a black bow tie. The raccoon is wearing a black top hat,
            adding a touch of elegance to its ensemble. The painting is rendered
            with characteristic van Gogh brushwork, utilizing thick, impasto strokes
            of color. The background is a swirl of blues, greens, and yellows,
            creating a vibrant yet slightly chaotic atmosphere that contrasts with
            the raccoon's formal attire. The lighting is dramatic, casting sharp
            shadows and highlighting the textures of the fabric and the raccoon's
            fur, enhancing the sense of realism within the fantastical scene. The
            composition focuses on the raccoon's proud posture, highlighting the
            whimsical contrast of a wild animal dressed in formal attire, captured
            in the unique artistic language of van Gogh. ",**
          "bytesBase64Encoded": "BASE64_IMG_BYTES"
        }
      ]
    }
    

## What's next

  * [Set text prompt language](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/set-text-prompt-language)
  * [Configure aspect ratio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/configure-aspect-ratio)
  * [Omit content using a negative prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/omit-content-using-a-negative-prompt)
  * [Generate deterministic images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-deterministic-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
