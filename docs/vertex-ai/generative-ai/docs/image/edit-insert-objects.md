---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects/
title: Insert objects into an image using inpaint \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:09.930718+00:00
---

# Insert objects into an image using inpaint  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/edit-insert-objects/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Insert objects into an image using inpaint Stay organized with collections  Save and categorize content based on your preferences. 

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
  
This page describes how to insert objects into an image, a process also known as _inpainting_. Imagen on Vertex AI lets you specify a mask area to insert objects into an image. You can bring your own mask, or you can let Imagen generate a mask for you.

The following models support inserting objects into an image:

  * [ `imagen-3.0-capability-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-capability-001)



## Content insertion example

To see an example of Imagen 3 Editing, run the "Imagen 3 Image Editing" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_editing.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_editing.ipynb)

With inpainting, you can use a base image, an image mask, and a text prompt to add content to an existing image.

**Inputs**

Base image* to edit | Mask area specified using tools in the Google Cloud console | Text prompt  
---|---|---  
![An example base image. A glass jar contains a red liquid with a
           lemon slice on the side and a straw sticking out. Lemon slices are
           visible in the left foreground](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/inpainting-insert_base-image.jpg) |  ![The base image of a glass jar, now with a mask area specified in
           the Cloud console](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/inpainting-insert_mask-area.png) |  _strawberries_  
  
* _Image credit:[Alex Lvrs](https://unsplash.com/photos/strawberry-juice-with-sliced-oranges-HDjExSGuWUw) on [Unsplash](https://unsplash.com/)._

**Output after specifying a mask area in the Google Cloud console**

![A screenshot from a generated edit of a glass jar containing a
           red liquid. In this screenshot, the lemon slices previously in the
           image foreground are replaced by two strawberries directly in front
           of the jar.](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/inpainting-insert_output1.png) |  ![A screenshot from a generated edit of a glass jar containing a
           red liquid. In this screenshot, the lemon slices previously in the
           image foreground are replaced by three strawberries just to the left
           of the jar.](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/inpainting-insert_output2.png) |  ![A screenshot from a generated edit of a glass jar containing a
           red liquid. In this screenshot, the lemon slices previously in the
           image foreground are replaced by two strawberries, slighly in front
           of and to the left of the jar.](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/inpainting-insert_output3.png)  
---|---|---  
  
[View Imagen for Editing and Customization model card](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/imagen-3.0-capability-001)

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




## Insert with a defined mask area

Use the following samples to send an inpainting request using the Imagen 3 model.

### Console

  1. In the Google Cloud console, go to the **Vertex AI > Vertex AI Studio ** page. 

[ Go to Vertex AI Studio ](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

  2. Click **Generate media**. 

  3. Click **Image**. 

  4. From the **Task** list, select **Inpaint-add**.

  5. From the **Model** list, select the Imagen model to use.

  6. In **Input image** click **Add** and select the image that you are editing to upload.

  7. In the **Prompt** box, enter a prompt that describes how to edit the image.

  8. Do one of the following to specify a mask:

     * Upload your own mask: 
       1. Create a mask on your computer.
       2. Click  upload  **Import mask** and select a mask to upload.
     * Define your mask: in the editing toolbar, use the mask tools (check_box_outline_blank**box** , brush**brush** , or masked_transitions **invert** tool) to specify the area or areas to add content to.
  9. Click **Run**.




### REST

For more information about the Imagen API, see the following: 

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * `REGION`: The region that your project is located in. For more information about supported regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations). 
  * `PROJECT_ID`: Your Google Cloud project ID. 
  * `TEXT_PROMPT`: Optional. A text prompt to guide the images that the model generates. For best results, use a description of the masked area and avoid single-word prompts. For example, use "a cute corgi" instead of "corgi". 
  * `B64_BASE_IMAGE`: A base64-encoded image of the image being edited that is 10MB or less in size. For more information about base64-encoding, see [Base64 encode and decode files](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode). 
  * `B64_MASK_IMAGE`: A base64-encoded black and white mask image that is 10MB or less in size. 
  * `MASK_DILATION`: Optional. A float value between 0 and 1, inclusive, that represents the percentage of the image width to grow the mask by. Using `dilation` helps compensate for imprecise masks. We recommend a value of `0.01`. 
  * `EDIT_STEPS`: Optional. An integer that represents the number of sampling steps. A higher value offers better image quality, a lower value offers better latency. 

We recommend that you try `35` steps to start. If the quality doesn't meet your requirements, then we recomment increasing the value towards an upper limit of `75`. 

  * `SAMPLE_COUNT`: Optional. An integer that describes the number of images to generate. The accepted range of values is `1`-`4`. The default value is `4`. 



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/imagen-3.0-capability-001:predict

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
                "bytesBase64Encoded": "B64_BASE_IMAGE"
              }
            },
            {
              "referenceType": "REFERENCE_TYPE_MASK",
              "referenceImage": {
                "bytesBase64Encoded": "B64_MASK_IMAGE"
              },
              "maskImageConfig": {
                "maskMode": "MASK_MODE_USER_PROVIDED",
                "dilation": MASK_DILATION
              }
            }
          ]
        }
      ],
      "parameters": {
        "editConfig": {
          "baseSteps": EDIT_STEPS
        },**"editMode": "EDIT_MODE_INPAINT_INSERTION",**
        "sampleCount": SAMPLE_COUNT
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
         "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/imagen-3.0-capability-001:predict"

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
        -Uri "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/publishers/google/models/imagen-3.0-capability-001:predict" | Select-Object -Expand Content

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
    

## Insert with automatic mask detection

Use the following samples to specify inpainting to insert content. In these samples you specify a base image and a text prompt. Imagen automatically detects and creates a mask area to modify the base image.

### Console

  1. In the Google Cloud console, go to the **Vertex AI > Vertex AI Studio ** page. 

[ Go to Vertex AI Studio ](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)

  2. Click **Generate media**. 

  3. Click **Image**. 

  4. From the **Task** list, select **Inpaint-add**.

  5. From the **Model** list, select the Imagen model to use.

  6. In **Input image** click **Add** and select the image that you are editing to upload.

  7. In the **Prompt** box, enter a prompt that describes how to edit the image.

  8. In the editing toolbar, click background_replace**Extract mask**.

  9. Select one of the mask extraction options:

     * **Background elements** : detects the background elements and creates a mask around them.

     * wallpaper **Foreground elements** : detects the foreground objects and creates a mask around them.

     * background_replace **People** : detects people and creates a mask around them.

  10. Click **Run**.




### REST

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt guides what images the model generates. When you use a prompt for inpainting insertion, use a description of the masked area for best results. Avoid single-word prompts. For example, use "_a cute corgi_ " instead of "_corgi_ ". 
  * B64_BASE_IMAGE: The base image to edit or upscale. The image must be specified as a [base64-encoded](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode) byte string. Size limit: 10 MB. 
  * MASK_MODE \- A string that sets the type of automatic mask creation the model uses. Available values: 
    * `MASK_MODE_BACKGROUND`: Automatically generates a mask using background segmentation. 
    * `MASK_MODE_FOREGROUND`: Automatically generates a mask using foreground segmentation.
    * `MASK_MODE_SEMANTIC`: Automatically generates a mask using semantic segmentation based on the [segmentation classes](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-customization#segment-ids) you specify in the `maskImageConfig.maskClasses` array. For example: 
          
          "maskImageConfig": {
                      "maskMode": "MASK_MODE_SEMANTIC",**"maskClasses": [175, 176], // bicycle, car**
                      "dilation": 0.01
                    }
                  

  * MASK_DILATION \- float. The percentage of image width to dilate this mask by. A value of `0.01` is recommended to compensate for imperfect input masks. 
  * EDIT_STEPS \- integer. The number of sampling steps for the base model. For inpainting insertion, start at `35` steps. Increase steps to upper limit of `75` if the quality doesn't meet your requirements. Increasing steps also increases request latency. 
  * EDIT_IMAGE_COUNT \- The number of edited images. Accepted integer values: 1-4. Default value: 4. 



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagen-3.0-capability-001:predict

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
                "bytesBase64Encoded": "B64_BASE_IMAGE"
              }
            },
            {
              "referenceType": "REFERENCE_TYPE_MASK",
              "referenceId": 2,
              "maskImageConfig": {**"maskMode": " MASK_MODE",**
                "dilation": MASK_DILATION
              }
            }
          ]
        }
      ],
      "parameters": {
        "editConfig": {
          "baseSteps": EDIT_STEPS
        },**"editMode": "EDIT_MODE_INPAINT_INSERTION",**
        "sampleCount": EDIT_IMAGE_COUNT
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
         "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagen-3.0-capability-001:predict"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/publishers/google/models/imagen-3.0-capability-001:predict" | Select-Object -Expand Content

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
    

## Limitations

The following sections explain limitations of Imagen's remove objects feature.

### Modified pixels

The model generates pixels at its own resolution (for example, 1024x1024), which might differ from the input image's resolution. This means the generated image might have small changes that weren't in the original image.

To perfectly preserve the image, we recommend blending the generated image with the input image using the mask. Typically, if the input image resolution is 2K or higher, blending the generated image and input image is required.

### Insert limitation

While the inserted object usually matches the style of the base image, some keywords might produce cartoon-like results instead of a photorealistic output.

For example, prompting for a "yellow giraffe" might result in a cartoonish image because giraffes are naturally brown and tan. Generating photorealistic images with unnatural colors can be difficult.

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
