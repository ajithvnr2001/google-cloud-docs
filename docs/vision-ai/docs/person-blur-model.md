---
url: https://docs.cloud.google.com/vision-ai/docs/person-blur-model/
title: Person blur guide \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:16.259762+00:00
---

# Person blur guide  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/person-blur-model/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Person blur guide Stay organized with collections  Save and categorize content based on your preferences. 

![person blur model card in console](https://docs.cloud.google.com/static/vision-ai/docs/images/person-blur-card.png)

The **Person blur** model lets you protect the privacy of people who appear in input videos through distortion such as masking or blurring people's appearance in output videos. The model accepts video streams as input and outputs modified videos with people's face or whole body blurred. The model runs at five FPS. 

You can set up parameters in the console to control the distortion in output videos:

  1. Choose **Full occlusion** or **Blur filter** to control the distortion type:

     * **Full occlusion** : Hide the detected region with an opaque black bounding box.
     * **Blur filter** : Apply pixel-level blurring on the detected region.
  2. Customers can also select or clear **Blur faces only** to control the region of the person's appearance to distort:

     * check_box Select **Blur faces only** : Distort the face region only.
     * check_box_outline_blank Clear **Blur faces only** : Distort the whole person.



You can use these combinations to make the following four output video types:

Distortion type | Face blur only (selected/not selected) | Output video description  
---|---|---  
radio_button_checked**Full occlusion**  
radio_button_unchecked**Blur filter** | check_box**Blur faces only** | Output opaque black boxes on faces only.  
![Full occlusion with blur faces only option output](https://docs.cloud.google.com/static/vision-ai/docs/images/full-occlusion_faces-only.png)  
radio_button_checked**Full occlusion**  
radio_button_unchecked**Blur filter** | check_box_outline_blank**Blur faces only** | Output opaque black boxes over the entirety of detected bodies.  
![Full occlusion option output](https://docs.cloud.google.com/static/vision-ai/docs/images/full-occlusion-only.png)  
radio_button_unchecked**Full occlusion**  
radio_button_checked**Blur filter** | check_box**Blur faces only** | Output a blurred region on faces only.  
![Blur filter with blur faces only option output](https://docs.cloud.google.com/static/vision-ai/docs/images/blur-filter_faces-only.png)  
radio_button_unchecked**Full occlusion**  
radio_button_checked**Blur filter** | check_box_outline_blank**Blur faces only** | Output a blurred region over the entirety of detected bodies.  
![Blur filter option output](https://docs.cloud.google.com/static/vision-ai/docs/images/blur-filter-only.png)  
  
## Best practices and limitations

  * Avoid unusual camera viewpoints (for example, a top-down view) where the people and vehicles look different from their standard or common views. The detection and blurring quality can be largely affected by these unusual views.
  * Make sure that people or faces are fully or mostly visible. The detection and blurring quality can be affected by partial occlusion by other objects.
  * Make sure that the scene has proper lighting. Dark scenes might impact detection and blurring quality.
  * The person and face detector has a minimal-detectable object size. This size is approximately 2% with respect to the size of the camera view. People and faces that are far away from the camera aren't blurred. Avoid crowded scenes and expect every person or face to be blurred. The model operates optimally when people are in the center of the scenes and are sufficiently large.
  * The Person blur model optimizes for protecting user privacy. Consequently, the model might provide an excessively large ("conservative") blur region for the video. To avoid excessive blacked-out regions, switch your blur method from **Full Occlusion** to **Blur Filter**.
  * The Person blur model is a computationally-expensive operation. Consequently, you should consider the following considerations when using this model: 
    * Resolution: There are no constraints on the input video resolution. However, videos with resolution _higher_ than 1280x720 pixels are down-sized to 1280x720 pixels when you use the Person blur model. Smaller faces far from cameras aren't blurred.
    * Output video frame rate: The current output frame rate of the Person blur model is a fixed **five frames per second** regardless of the input video frame rate. This output frame rate is limited by computing resources and is subject to change in future product updates.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
