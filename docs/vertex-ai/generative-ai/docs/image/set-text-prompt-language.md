---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/set-text-prompt-language/
title: Set text prompt language \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:11.233417+00:00
---

# Set text prompt language  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/set-text-prompt-language/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Set text prompt language Stay organized with collections  Save and categorize content based on your preferences. 

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
  
**Preview**

This Imagen feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this Imagen feature, you agree to the Generative AI Preview [terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). 

[Try image generation (Vertex AI Studio)](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

[Try Imagen in a Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb)

This page describes how you can set an optional Imagen on Vertex AI parameter to specify the prompt language that you use. If you don't specify a language, then Imagen automatically detects the language.

**Note:** While Imagen models support only English natively, Imagen uses translation to translate several non-English language prompts to English to feed the model.

![a book image generated from a prompt in hindi](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gen-img_param_prompt-lang_hindi.png) Image generated from prompt: ऊपर से देखा गया किताबों का ढेर। सबसे ऊपरी पुस्तक में एक पक्षी का जलरंग चित्रण है। किताब पर VERTEX AI मोटे अक्षरों में लिखा हुआ है 1  
  
1 _A pile of books seen from above. The topmost book contains a watercolor illustration of a bird.**VERTEX AI** is written in bold letters on the book._ |  ![an image of a woman from a prompt in korean](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gen-img_param_prompt-lang_korean.png) Image generated from prompt: 어두운 노란색과 청록색으로 이루어진 밝은 색의 옷을입고 귀걸이를 끼고있는 여자 포스트 모던 패션 사진 2  
  
2 _Woman wearing bright colors, in the style of dark yellow and dark cyan, wearing earrings, postmodern fashion photography._  
---|---  
  
## Set text prompt language

The following input values are supported for the text-prompt lanague:

  * Chinese (simplified) (`zh`/`zh-CN`)
  * Chinese (traditional) (`zh-TW`)
  * English (`en`, default value)
  * French (`fr`)
  * German (`de`)
  * Hindi (`hi`)
  * Japanese (`ja`)
  * Korean (`ko`)
  * Portuguese (`pt`)
  * Spanish (`es`)




###  Console 

If your prompt is in one of the supported languages, Imagen detects and translates your text and returns your generated or edited images.

If your prompt is in an unsupported language, Imagen uses the text verbatim for the request. This might result in unexpected output.

### REST

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)

**Important:** `imagen-3.0-generate-002` doesn't support the text prompt language feature.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * TEXT_PROMPT: The text prompt that guides what images the model generates. This field is required for both generation and editing. 
  * PROMPT_LANGUAGE: string. Optional. The language code that corresponds to your text prompt language. In this example it would be `hi`. Available values: 
    * `auto` \- Automatic detection. If Imagen detects a supported language, the prompt (and optionally, a negative prompt), are translated to English. If the language detected is not supported, Imagen uses the input text verbatim, which might result in unexpected output. No error code is returned. 
    * `en` \- English (default value if omitted)
    * `es` \- Spanish
    * `hi` \- Hindi
    * `ja` \- Japanese
    * `ko` \- Korean
    * `pt` \- Portuguese
    * `zh-TW` \- Chinese (traditional)
    * `zh` or `zh-CN` \- Chinese (simplified)



HTTP method and URL: 
    
    
    POST https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/imagegeneration@005:predict

Request JSON body: 
    
    
    {
      "instances": [
        {
          "prompt": "सूर्यास्त के समय एक समुद्र तट। उड़ते पक्षी, हवा में लहराते नारियल के पेड़। लोग समुद्र तट पर सैर का आनंद ले रहे हैं।"
        }
      ],
      "parameters": {**"language": " PROMPT_LANGUAGE"**
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
         "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/imagegeneration@005:predict"

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
        -Uri "https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/imagegeneration@005:predict" | Select-Object -Expand Content

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
    

## What's next

  * [Use prompt rewriter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/use-prompt-rewriter)
  * [Configure aspect ratio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/configure-aspect-ratio)
  * [Omit content using a negative prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/omit-content-using-a-negative-prompt)
  * [Generate deterministic images](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-deterministic-images)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
