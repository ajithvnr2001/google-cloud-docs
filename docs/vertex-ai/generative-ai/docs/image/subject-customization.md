---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization/
title: Subject customization \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:12.049006+00:00
---

# Subject customization  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/subject-customization/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Subject customization Stay organized with collections  Save and categorize content based on your preferences. 

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
  
Imagen 3 Customization's subject customization helps you generate new images from a text prompt and a reference image that you provide. The reference image that you provide helps guide new image generation.

The following models support subject customization:

  * [ `imagen-3.0-capability-001`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/imagen/3-0-generate#3.0-capability-001)



## Use cases

Imagen 3 Customization offers free-style prompting, which can give the impression that it can do more than it is trained to do. The following sections describe intended use cases for Imagen 3 Customization, and non-exhaustive examples of unintended use cases.

We recommend using Imagen 3 Customization for the intended use cases, as we've trained the model on those use cases and expect good results for them. Conversely, while you can push the model to do things outside of the intended use cases, we don't expect good results.

### Intended use cases

The following are use cases intended for Imagen 3 Customization subject customization:

  * Stylize a photo of a person
  * Stylize a photo of a person, and preserve the person's facial expressions
  * (Low success) Place a product, such as a couch or a cookie, into different scenes with different product angles.
  * Generate variations of a product that doesn't preserve exact details
  * Stylize a photo of a person, while preserving facial expression



### Examples of unintended use cases

The following are a non-exhaustive list of use cases that Imagen 3 Customization isn't trained to do, and produces poor results for:

  * Place two or more people in different scenes while preserving their identities
  * Place two or more people in different scenes while preserving their identities and specifying the style of the output image using an example image as input for the style.
  * Stylize a photo of two or more people while preserving their identities
  * Place a pet into different scenes while preserving its identity
  * Stylize a photo of a pet and turn it into a drawing
  * Stylize a photo of a pet and turn it into a drawing, while preserving or specifying the style of the image (such as water color)
  * Place a pet and a person into a different scene, preserving the identities of both.
  * Stylize a photo of a pet and one or more people and turn it into a drawing
  * Place a two products into different scenes with different product angles
  * Place a product, such as a cookie or a couch, into different scenes with different product angles, and following a specific image style (such as photorealistic with specific colors, lighting styles, or animation)
  * Place a product into a different scene, while preserving the specific composition of the scene as specified by a control image
  * Place two products into different scenes with different product angles, using a specific image as input (such as photorealistic with specific colors, lighting styles, or animation)
  * Place two products into different scenes, while preserving the specific composition of the scene as specified by a control image



## Subject customization examples

The following sections depict supported cases for Imagen 3 Customization subject customization:

#### Person customization

Sample Input | Sample Output  
---|---  
  
  1. Reference image1:  
![Sample input for product customization](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/woman-long-hair-input.png)
  2. Text prompt:  
_Generate an image about the woman with long hair[1] to match this description: a portrait of a woman with long hair[1] in 3d-cartoon style with blurred background. A cute and lovely character, smile face, looking at the camera, pastel color tone, high quality, 4k, masterpiece, super details, skin texture, texture mapping, soft shadows, soft realistic lighting, vibrant colors. _

|    
![Sample output for product customization](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/woman-long-hair-output.png)  
  
1 Reference input image generated using Imagen 3 image generation from the prompt: _portrait of a woman in paris. she's wearing black pants and a white shirt_.

#### Product customization

Sample Input | Sample Output  
---|---  
  
  1. Reference image2:  
![Sample input for product customization](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/product-cust_input_perfume1_SMALL.png)
  2. Text prompt:  
_Generate an image of the perfume bottle [1] but in cyan _

|    
![Sample output for product customization](https://docs.cloud.google.com/static/vertex-ai/generative-ai/docs/image/images/product-cust_output4_SMALL.png)  
2 Reference input image generated using Imagen 3 image generation from the prompt: _perfume bottle product style image in front of a black background_. 

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




## Subject customization

To see an example of Imagen 3 Customization, run the "Imagen 3 Customized Images" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Vertex AI Workbench](https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fvision%2Fgetting-started%2Fimagen3_customization.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/imagen3_customization.ipynb)

You can provide reference images of subject types when you use Imagen 3 Customization. Specifically, few-shot prompting with Imagen 3 Customization supports the following subjects: product, person, and animal companion. The subject you choose affects how you form your generation request.

The prompt you use with Imagen 3 Customization might affect the quality of your generated images. The following sections describe recommended prompt templates and samples to send customization requests.

### Person customization

The following table describes prompt templates that we recommend as a starting point when writing person customization prompts:

Use case | Reference images | Prompt template | Example  
---|---|---|---  
Person image stylization with face mesh input |  Subject image (1)  


* * *

Facemesh control image (1)  | Generate an image of SUBJECT_DESCRIPTION [1] with the facemesh from the control image [2]. _${PROMPT}_ | Generate an image of the person [1] with the facemesh from the control image [2]. _The person should be looking straight ahead with a neutral expression. The background should be a ..._  
Person image stylization without face mesh input | Subject image (1-4) |  Create an image about SUBJECT_DESCRIPTION [1] to match the description: a portrait of SUBJECT_DESCRIPTION [1] _${PROMPT}_ |  Create an image about a woman with short hair[1] to match the description: a portrait of a woman with short hair[1] _in 3d-cartoon style with blurred background. A cute and lovely character, smile face, looking at the camera, pastel color tone, high quality, 4k, masterpiece, super details, skin texture, texture mapping, soft shadows, soft realistic lighting, vibrant colors_  
Person image stylization without face mesh input | Subject image (1-4) |  Create a STYLE_DESCRIPTION [2] image about SUBJECT_DESCRIPTION [1] to match the description: a portrait of SUBJECT_DESCRIPTION [1] _STYLE_PROMPT_ |  Create a 3d-cartoon style [2] image about a woman with short hair [1] to match the description: a portrait of a woman with short hair [1] _in 3d-cartoon style with blur background. A Cute and lovely character, smile face. see the camera, pastel color tone, high quality, 4k, masterpiece, super details, skin texture, texture mapping, Soft shadows, soft realistic lighting, vibrant colors_  
Person image stylization with face mesh input |  Subject image (1-3)  


* * *

Facemesh control image (1)  |  Create an image about SUBJECT_DESCRIPTION [1] in the pose of the CONTROL_IMAGE [2] to match the description: a portrait of SUBJECT_DESCRIPTION [1] _${PROMPT}_ |  Create an image about a woman with short hair [1] in the pose of the control image [2] to match the description: a portrait of a woman with short hair [1] _in 3d-cartoon style with blur background. A Cute and lovely character, smile face. See the camera, pastel color tone, high quality, 4k, masterpiece, super details, skin texture, texture mapping, Soft shadows, soft realistic lighting, vibrant colors_  
Person image stylization with face mesh input |  Subject image (1-3)  


* * *

Facemesh control image (1)  |  Create a STYLE_DESCRIPTION [3] image about SUBJECT_DESCRIPTION [1] in the pose of the CONTROL_IMAGE [2] to match the description: a portrait of SUBJECT_DESCRIPTION [1] _${PROMPT}_ |  Create a 3d-cartoon style [3] image about a woman with short hair [1] in the pose of the control image [2] to match the description: a portrait of a woman with short hair [1] _in 3d-cartoon style with blur background. A Cute and lovely character, smile face. See the camera, pastel color tone, high quality, 4k, masterpiece, super details, skin texture, texture mapping, Soft shadows, soft realistic lighting, vibrant colors_  
  
We recommend that the face in your reference image has the following properties:

  * Is centered and occupies at least half of the whole image
  * Is rotated in frontal view in all directions (roll, pitch, and yaw)
  * Isn't occluded by objects, such as sunglasses or masks



Use the following samples to send a customization request with person reference images used to guide image generation. You can send this type of request with or without a face mesh control image to further guide image generation.

###  REST 

For more information about the Imagen API, see the following:

  * [Method: `endpoints.predict`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.endpoints/predict)
  * [`VisionGenerativeModelInstance`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelInstance)
  * [`VisionGenerativeModelParams`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelParams)
  * [`VisionGenerativeModelResult`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/Shared.Types/VisionGenerativeModelResult)



This sample shows you how to specify a face mesh control area to guide generation, but you can also omit the control reference object (`"referenceType": "REFERENCE_TYPE_CONTROL"`) and Imagen will automatically detect a face mesh control area.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt guides what images the model generates. To use Imagen 3 Customization, include the `referenceId` of the reference image or images you provide in the format [$referenceId]. For example: 
    * The following text prompt is for a request that has two reference images with `"referenceId": 1`. Both images have an optional description of `"subjectDescription": "man with short hair"`. Additionally, there is a control face mesh image specified with `"referenceId": 2`: _Create an image about a man with short hair [1] in the pose of control image [2] to match the description: A pencil style sketch of a full-body portrait of a man with short hair [1] with hatch-cross drawing, hatch drawing of portrait with 6B and graphite pencils, white background, pencil drawing, high quality, pencil stroke, looking at camera, natural human eyes _
  * `"referenceId"`: The ID of the reference image, or the ID for a series of reference images that correspond to the same subject or style. In this example the two reference images are of the same person, so they share the same `referenceId` (`1`) and the control face mesh image has a distinct `referenceId` (`2`). The generated image will follow the face structure of the face mesh extracted from the reference image and will improve the face appearance following. Only one face mesh control is supported. 
  * BASE64_REFERENCE_IMAGE: A reference image to guide image generation. The image must be specified as a [base64-encoded](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode) byte string. 
  * SUBJECT_DESCRIPTION: Optional. A text description of the reference image you can then use in the `prompt` field. For example: 
        
        "prompt": "_a full-body portrait of a man with short hair [1] with hatch-cross
              drawing_",
              [...],
              "subjectDescription": "man with short hair"
            

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
              "referenceType": "REFERENCE_TYPE_SUBJECT",
              "referenceId": 1,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              },
              "subjectImageConfig": {
                "subjectDescription": "SUBJECT_DESCRIPTION",
                "subjectType": "SUBJECT_TYPE_PERSON"
              }
            },
            {
              "referenceType": "REFERENCE_TYPE_SUBJECT",
              "referenceId": 1,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              },
              "subjectImageConfig": {
                "subjectDescription": "SUBJECT_DESCRIPTION",
                "subjectType": "SUBJECT_TYPE_PERSON"
              }
            },**{
              "referenceType": "REFERENCE_TYPE_CONTROL",
              "referenceId": 2,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              },
              "controlImageConfig": {
                "controlType": "CONTROL_TYPE_FACE_MESH",
                "enableControlImageComputation": true
              }
            }**
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
    

### Product customization

The following table describes prompt templates that we recommend as a starting point when writing product customization prompts:

Reference images | Prompt template | Example  
---|---|---  
Subject image (1-4) |  Create an image about SUBJECT_DESCRIPTION [1] to match the description: _${PROMPT}_ |  Create an image about Luxe Elixir hair oil, golden liquid in glass bottle [1] to match the description: _A close-up, high-key image of a woman's hand holding Luxe Elixir hair oil, golden liquid in glass bottle [1] against a pure white background. The woman's hand is well-lit and the focus is sharp on the bottle, with a shallow depth of field blurring the background and emphasizing the product. The lighting is soft and diffused, creating a subtle glow around the bottle and hand. The overall composition is simple and elegant, highlighting the product's luxurious appeal._  
Subject image (1-4) |  Generate an image of a SUBJECT_DESCRIPTION but _${PROMPT}_ |  Generate an image of a Seiko watch [1] but _in blue_.   
  
Use the following samples to send a customization request with product reference images used to guide image generation.

### Console

  1. In the Google Cloud console, go to the **Vertex AI > Vertex AI Studio ** page.   
[ Go to Vertex AI Studio ](https://console.cloud.google.com/vertex-ai/studio/media/generate;tab=image)
  2. In the **Model** section of the **Parameters** pane, select **Imagen 3** if not already selected. 
  3. Optional. Choose an **Aspect ratio** other than 1:1 (default).
  4. Optional. Change the **Number of results**.
  5. Optional. Provide a **Negative prompt** to guide the model on what to avoid generating.
  6. Optional. Change any **Advanced options**.
  7. In the **text prompt** field (_Write your prompt..._), click **Add reference**. 
     1. In the **Add reference** pane, choose the **Reference type** : **Subject - product**. 
     2. In the **Reference images** section, click **Upload**
     3. Choose a locally-stored image and click **Open**.
     4. Optional. Provide a **Description** for the reference image.
     5. Click **Done**.
     6. Optional. To add more reference images, click **Add an image** and upload another image.
     7. After you add all your reference images, click **Add reference**. 

All the reference images you add in that pane have the same reference number. Use this reference number when you add the text prompt.

  8. In the **text prompt** field (_Write your prompt..._), add a text prompt that includes the reference number or numbers for the reference images. For example: 
     1. _bright white room, the product [1] on a glass table_
     2. _the animal [1] standing on a wide open field with a forest in the distance_
     3. _a black and white portrait of the person [1] on a city street in film noir style [2]_



### REST

For more information about `imagen-3.0-capability-001` model requests, see the [`imagen-3.0-capability-001` model API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api-customization). 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION: Your project's region. For example, `us-central1`, `europe-west2`, or `asia-northeast3`. For a list of available regions, see [Generative AI on Vertex AI locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations-genai). When a regional API endpoint is used, the region from the endpoint's URL determines where the request is processed, and this `LOCATION` in the resource path is ignored if it conflicts. 
  * TEXT_PROMPT: The text prompt guides what images the model generates. To use Imagen 3 Customization, include the `referenceId` of the reference image or images you provide in the format [$referenceId]. For example: 
    * _Create an image about Luxe Elixir hair oil, golden liquid in glass bottle [1] to match the description: A close-up, high-key image of a woman's hand holding Luxe Elixir hair oil, golden liquid in glass bottle [1] against a pure white background. The woman's hand is well-lit and the focus is sharp on the bottle, with a shallow depth of field blurring the background and emphasizing the product. _
  * `"referenceId"`: The ID of the reference image, or the ID for a series of reference images that correspond to the same subject or style. In this example the two reference images are of the same product, so they share the same `referenceId` (`1`). 
  * BASE64_REFERENCE_IMAGE: A reference image to guide image generation. The image must be specified as a [base64-encoded](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/base64-encode) byte string. 
  * SUBJECT_DESCRIPTION: Optional. A text description of the reference image you can then use in the `prompt` field. For example: 
        
        "prompt": "Luxe Elixir hair oil, golden liquid in glass bottle [1]
              _against a pure white background._ ",
              [...],
              "subjectDescription": "Luxe Elixir hair oil, golden liquid in glass bottle"
            

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
              "referenceType": "REFERENCE_TYPE_SUBJECT",
              "referenceId": 1,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              },
              "subjectImageConfig": {**"subjectType": "SUBJECT_TYPE_PRODUCT",**
                "subjectDescription": "SUBJECT_DESCRIPTION"
              }
            },
            {
              "referenceType": "REFERENCE_TYPE_SUBJECT",
              "referenceId": 1,
              "referenceImage": {
                "bytesBase64Encoded": "BASE64_REFERENCE_IMAGE"
              },
              "subjectImageConfig": {**"subjectType": "SUBJECT_TYPE_PRODUCT",**
                "subjectDescription": "SUBJECT_DESCRIPTION"
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
