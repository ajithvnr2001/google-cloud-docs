---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview/
title: Generate and edit images on Vertex AI \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:08.375670+00:00
---

# Generate and edit images on Vertex AI  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Generate and edit images on Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

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
  
**API reference overview** : To view an overview of the API options for image generation and editing, see the [ `imagegeneration` model API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api). 

Gemini and Imagen on Vertex AI bring Google's state of the art image generative AI capabilities to application developers. With Gemini and Imagen on Vertex AI on Vertex AI, application developers can build next-generation AI products that transform their user's imagination into high-quality visual assets using AI generation, in seconds.

[Try image generation (Vertex AI Studio)](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

[Try Imagen in a Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb)

With Gemini and Imagen, you can do the following:

  * Generate novel images using only a text prompt (text-to-image AI generation).
  * Edit or expand an uploaded or generated image using a mask area you define.
  * Upscale existing, generated, or edited images.



  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_claymation-scene.png)
  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_balloons-cappadocia.png)
  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_digital-cartoon-robot.png)
  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_clay-bird-sculptor.png)
  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_oil-painting-bouquet.png)
  * ![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/gdm_comic-book-sunset.png)



#### Prompts for preceding images

These images are generated using the general Imagen 3 image generation model (`imagen-3.0-generate-002`) and the following prompts:

  1. _Claymation scene. A medium wide shot of an elderly woman. She is wearing flowing clothing. She is standing in a lush garden watering the plants with an orange watering can_
  2. _Shot in the style of DSLR camera with the polarizing filter. A photo of two hot air balloons over the unique rock formations in Cappadocia, Turkey. The colors and patterns on these balloons contrast beautifully against the earthy tones of the landscape below. This shot captures the sense of adventure that comes with enjoying such an experience._
  3. _A weathered, wooden mech robot covered in flowering vines stands peacefully in a field of tall wildflowers, with a a small blue bird resting on its outstrecteched hand. Digital Cartoon, with warm colors and soft lines. A large cliff with a waterfall looms behind._
  4. _A view of a person's hand as they hold a little clay figurine of a bird in their hand and sculpt it with a modeling tool in their other hand. You can see the sculptor's scarf. Their hands are covered in clay dust. A macro DSLR image highlighting the texture and craftsmanship._
  5. _A large, colorful bouquet of flowers in an old blue glass vase on the table. In front is one beautiful peony flower surrounded by various other blossoms like roses, lilies, daisies, orchids, fruits, berries, green leaves. The background is dark gray. Oil painting in the style of the Dutch Golden Age._
  6. _A single comic book panel of a boy and his father on a grassy hill, staring at the sunset. A speech bubble points from the boy's mouth and says: The sun will rise again. Muted, late 1990s coloring style_



## Quickstart: Generate images from text prompts using Imagen

You can generate novel images using only descriptive text as an input. The following samples show a simplified case for generating images, but you can use [additional parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#use-params) to tailor the generated images to your needs.

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

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  9. Use the following samples to generate an image:

### REST

     1. Set environment variables:
            
            export GOOGLE_CLOUD_PROJECT=GOOGLE_CLOUD_PROJECT # Replace with your Google Cloud project
            export GOOGLE_CLOUD_LOCATION=us-central1 # Replace with the appropriate location for your project
                        

     2. Run the following:
            
            curl -X POST \
            -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            -H "Content-Type: application/json; charset=utf-8" \
            "https://${GOOGLE_CLOUD_LOCATION}-aiplatform.googleapis.com/v1/projects/${GOOGLE_CLOUD_PROJECT}/locations/${GOOGLE_CLOUD_LOCATION}/publishers/google/models/imagen-4.0-generate-preview-05-20:predict" -d \
            $'{
              "instances": [
                {
                  "prompt": "a cat reading a book"
                }
              ],
              "parameters": {
                "sampleCount": 1
              }
            }'
                        

The model returns a base64 image bytes object.

For more information, see the Imagen [Generate images API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api). 




## When to use Gemini or Imagen on Vertex AI

In addition to using Gemini's built-in image generation capabilities, you can also access [Imagen](https://ai.google.dev/gemini-api/docs/imagen), our specialized image generation model.

Attribute | Gemini Image | Imagen 4  
---|---|---  
Strengths | Default recommendation.  
Unparalleled flexibility, contextual understanding, and mask-free editing. Uniquely capable of multi-turn conversational editing. | Best quality/latency  
Availability | Generally available | Generally available  
Latency |  Higher. More computation is required for its advanced capabilities.  | Low. Optimized for near-real-time performance.  
Cost | Token-based pricing. | Cost-effective for specialized tasks.  
Recommended tasks | 

  * Interleaved text and image generation to seamlessly blend text and images. 
  * Combine creative elements from multiple images with a single prompt. 
  * Make highly specific edits to images, modify individual elements with language commands, and iteratively work on an image. 
  * Apply a specific design or texture from one image to another while preserving the original subject's form and details. 

| 

  * Image quality, photorealism, artistic detail, or specific styles (for example, impressionism and anime) are top priorities. 
  * Infusing branding, style, or generating logos and product designs. 
  * Generating advanced spelling or typography.

  
  
We recommend Gemini as a starting point for generating images. Choose Imagen 4 Ultra for advanced use-cases or when you need the best image quality.

## Model versions

There are multiple image generation models that you can use. For more information, see [Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#generally_available_models) or [Imagen models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models).

## Try more examples

To learn more, run the following notebooks in the environment of your choice:

  * "Gemini 3 Pro Image Generation in Vertex AI":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fgetting-started%2Fintro_gemini_3_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fgetting-started%2Fintro_gemini_3_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb)

  * "Gemini 2.5 Flash Image Generation in Vertex AI":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_5_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fgetting-started%2Fintro_gemini_2_5_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fgetting-started%2Fintro_gemini_2_5_image_gen.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_5_image_gen.ipynb)

  * "Imagen 4 Image Generation":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen4_image_generation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen4_image_generation.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen4_image_generation.ipynb)

  * "Imagen 3 Image Editing":

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_editing.ipynb)




For a full list of Jupyter notebook tutorials using Imagen, see the [Generative AI on Vertex AI cookbook](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/cookbook).

## What's next

Use the following links to view the feature documentation.

![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/desert-landscape.png)

Prompt guide 

[ See how to write effective prompts to generate images. ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide)

![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/sneakers-4k.png)

How-to: generate images 

[ Learn how to generate images with Imagen on Vertex AI. ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images)

![](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/magazine-style-drink.png)

Reference: generate images 

[ Learn about optional and required fields when sending an Imagen image generation request. ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api)

Image credit: All images generated using Imagen on Vertex AI.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
