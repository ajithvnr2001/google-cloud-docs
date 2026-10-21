---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen/
title: Responsible AI and usage guidelines for Imagen \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:01:13.228982+00:00
---

# Responsible AI and usage guidelines for Imagen  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Guides ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Responsible AI and usage guidelines for Imagen Stay organized with collections  Save and categorize content based on your preferences. 

Imagen on Vertex AI brings Google's state of the art generative AI capabilities to application developers. As an early-stage technology, Imagen on Vertex AI's evolving capabilities and uses create potential for misapplication, misuse, and unintended or unforeseen consequences. For example, Imagen on Vertex AI could generate output that you don't expect, such as images that are offensive, insensitive, or contextually incorrect.

Given these risks and complexities, Imagen on Vertex AI is designed with Google's [AI Principles](https://ai.google/principles/) in mind. However, it is important for developers to understand and test their models to deploy them safely and responsibly. To aid developers, Imagen on Vertex AI has built-in safety filters to help customers block potentially harmful outputs within their use case. See the safety filters section for more.

When Imagen on Vertex AI is integrated into a customer's unique use case and context, additional responsible AI considerations and model limitations may need to be considered. We encourage customers to use fairness, interpretability, privacy, and security [recommended practices](https://ai.google/responsibilities/responsible-ai-practices/).

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
  
[View Imagen for Generation model card](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/imagen-4.0-generate-preview-06-06)

[View Imagen for Editing and Customization model card](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/imagen-3.0-capability-001)

## Imagen usage guidelines

Read the following general product attributes and legal considerations before you use Imagen on Vertex AI.

  * **Image and text filters and outputs:** Images (generated or uploaded) through Imagen on Vertex AI are assessed against safety filters. Imagen aims to filter out (generated or uploaded) that violate our acceptable use policy (AUP) or additional Generative AI product restrictions. In addition, our generative imagery models are intended to generate original content and not replicate existing content. We've designed our systems to limit the chances of this occurring, and we will continue to improve how these systems function. Like all cloud service providers, Google maintains an Acceptable Use Policy that prohibits customers from using our services in ways that infringe third-party IP rights.
  * **Configurable safety filter thresholds:** Google blocks model responses that exceed the designated confidence scores for certain safety attributes. To request the ability to modify a safety threshold, contact your Google Cloud account team.
  * **Text addition supported on certain model versions:** Imagen does not support adding text to images (uploaded or generated) using a text prompt when using the `imagegeneration@004` or lower model versions.
  * **Report suspected abuse:** You can report suspected abuse of Imagen on Vertex AI or any generated output that contains inappropriate material or inaccurate information using the [Report suspected abuse on Google Cloud form](https://support.google.com/code/contact/cloud_platform_report). 
  * **Trusted Tester Program opt-out** : If you previously opted in to permit Google to use your data to improve pre-GA AI/ML services as part of the Trusted Tester Program terms, you can opt out using the [Trusted Tester Program - Opt Out Request form](https://docs.google.com/forms/d/e/1FAIpQLSdUwCF62JRg8rVYh5IaN7VWwIrLtWbxtcQDRC97zbzoq54bfg/viewform). 



## Safety filters

Text prompts provided as inputs and images (generated or uploaded) through Imagen on Vertex AI are assessed against a list of safety filters, which include 'harmful categories' (for example, `violence`, `sexual`, `derogatory`, and `toxic`). These safety filters aim to filter out (generated or uploaded) content that violates our [Acceptable Use Policy (AUP)](https://docs.cloud.google.com/terms/aup), [Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy) or our [AI Principles](https://ai.google/principles/).

If the model responds to a request with an error message such as "The prompt couldn't be submitted" or "it might violate our policies", then the input is triggering a safety filter. If fewer images than requested are returned, then some generated output are blocked for not meeting safety requirements.

You can choose how aggressively to filter sensitive content by adjusting the `safetySetting` parameter.

## Safety attributes

Safety attributes and safety filters don't have a one-to-one mapping relationship. Safety attributes are the set of attributes that we return to user when `includeSafetyAttributes` is set. Safety filters are the set of filters we use to filter content. We don't filter on all safety attribute categories. For example, for the safety attribute category "Health", we don't filter content based on the health confidence score. Also, we don't expose the confidence scores for some of our internal sensitive safety filters.

## Configure safety filters

There are several [safety filtering](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#safety-filters) parameters you can use with the image generation models. For example, you can let the model report safety filter codes for blocked content, disable people or face generation, adjust the sensitivity of content filtering, or return rounded safety scores of list of safety attributes for input and output. For more technical information about individual fields, see the [image generation model API reference](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/image-generation).

The response varies depending on which parameters you set; some parameters affect the content produced, while others affect content filtering and how filtering is reported to you. Additionally, the output format depends on if the input data is filtered, or if the generated image output is filtered.

### Parameters that filter content

The following optional parameters affect content filtering or how filtering is reported to you:

  * `safetySetting` \- Lets you set how aggressively to filter for potentially sensitive output content.
  * `includeRaiReason` \- Provides more verbose information on filtered output.
  * `personGeneration` \- A setting that allows you more control over the generation of people, faces, and children.
  * `disablePersonFace` \- Deprecated. A choice to allow person and face generation or not. Users should set `personGeneration` instead.
  * `includeSafetyAttributes` \- Gives you full safety attribute information for input text, input image (for editing), and all generated images. This information includes safety category (for example, `"Firearms & Weapons"`, `"Illicit Drugs"`, or `"Violence"`) and the confidence scores.



#### Filtered input

If your text input or input image (for editing) is filtered, you get a response with a `400` error code. A request with RAI-filtered input returns this output format if you set either `includeRaiReason` or `includeSafetyAttributes`.

Output depends on the model version you use. The following shows output when the input is filtered for different model versions:

### Model
    
    
    {
      "error": {
        "code": 400,
        "message": "Image generation failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google's Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback."
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.DebugInfo",
            "detail": "[ORIGINAL ERROR] generic::invalid_argument: Image generation failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google's Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback. [google.rpc.error_details_ext] { message: \"Image editing failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google's Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback. Support codes: 42876398\" }"
          }
        ]
      }
    }

### Models
    
    
    {
      "error": {
        "code": 400,
        "message": "Image generation failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google's Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback.",
        "status": "INVALID_ARGUMENT",
        "details": [
          {
            "@type": "type.googleapis.com/google.rpc.DebugInfo",
            "detail": "[ORIGINAL ERROR] generic::invalid_argument: Image generation failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google's Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback. [google.rpc.error_details_ext] { message: \"Image generation failed with the following error: The prompt could not be submitted. This prompt contains sensitive words that violate Google\\'s Responsible AI practices. Try rephrasing the prompt. If you think this was an error, send feedback.\" }"
          }
        ]
      }
    }

#### Filtered output

The contents of filtered output vary depending on the RAI parameter you set. The following output examples show the result of using the `includeRaiReason` and `includeSafetyAttributes` parameters.

##### Filtered output using `includeRaiReason`

If you don't add `includeRaiReason` or set `includeRaiReason: false`, your response only includes generated image objects that aren't filtered. Any filtered image objects are omitted from the `"predictions": []` array. For example, the following is a response to a request with `"sampleCount": 4`, but two of the images are filtered and consequently omitted:
    
    
    {
      "predictions": [
        {
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]bdsdgD2PLbZQfW96HEFE/9k=",
          "mimeType": &quot;image/png"
        },
        {
          &quot;mimeType": "image/png",
          "bytesBase64Encoded": &quot;/9j/4AAQSkZJRgABA[...]Ct+F+1SLLH/2+SJ4ZLdOvg//Z"
        }
      ],
      "deployedModelId": "MODEL_ID"
    }

If you set `includeRaiReason: true` and several output images are filtered, your response includes generated image objects and `raiFilteredReason` objects for any filtered output images. For example, the following is a response to a request with `"sampleCount": 4` and `includeRaiReason: true`, but two of the images are filtered. Consequently, two objects include generated image information and the other object includes an error message.

### Model
    
    
    {
      "predictions": [
        {
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]bdsdgD2PLbZQfW96HEFE/9k=",
          "mimeType": &quot;image/png"
        },
        {
          &quot;mimeType": "image/png",
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]Ct+F+1SLLH/2+SJ4ZLdOvg//Z"
        },
        {
          "raiFilteredReason": "Your current safety filter threshold filtered out 2 generated images. You will not be charged for blocked images. Try rephrasing the prompt. If you think this was an error, send feedback."
        },
      ],
      "deployedModelId": "MODEL_ID"
    }

### Models
    
    
    {
      "predictions": [
        {
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]bdsdgD2PLbZQfW96HEFE/9k=",
          "mimeType": &quot;image/png"
        },
        {
          &quot;mimeType": "image/png",
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]Ct+F+1SLLH/2+SJ4ZLdOvg//Z"
        },
        {
          "raiFilteredReason&quot;: &quot;56562880"
        },
        {
          "raiFilteredReason": "56562880"
        }
      ],
      "deployedModelId": "MODEL_ID"
    }

##### Filtered output using `includeSafetyAttributes`

If you set `"includeSafetyAttributes": true`, the response `"predictions": []` array includes the RAI scores (rounded to one decimal place) of text safety attributes of the positive prompt. The image safety attributes are also added to each unfiltered output. If an output image is filtered its safety attributes aren't returned. For example, the following is a response to an unfiltered request, and one image is returned:
    
    
    {
      "predictions": [
        {
          "bytesBase64Encoded": "/9j/4AAQSkZJRgABA[...]bdsdgD2PLbZQfW96HEFE/9k=",
     **** "mimeType": "image/png", 
          "safetyAttributes&quot;: {
            "categories": [
              &quot;Porn";,
              "Violence&qu**ot;**
            ],
            "scores": [
              0.1,
              0.2
            ]
          } 
        }, 
        {
          "con&tentType": "Positive &Prompt",
          "safetyAttributes": {
            "categories": [
              "Death, Harm  Tragedy",
          &    "Firearms  Weapons",
              "Hate",
              "Health&quo&t;,
              "Illicit Drugs",
              &quot;Politics&quot;,
              "Porn",
              "Religion  Belief",
              "Toxic",
              "Violence",
              "Vulgarity&quot;,
              "War  Conflict&quot;
            ],
            "scores": [
              0,
              0,
              0,
              0,
              0,
              0,
              0.2,
              0,
              0.1,
              0,
              0.1,
              0
            ]
          }
        }, 
      ],
      "deployedModelId": "MODEL_ID"
    }
    

### Safety filter code categories

Depending on the safety filters you configure, your output may contain a safety reason code similar to the following:
    
    
        {
          "raiFilteredReason": &quot;ERROR_MESSAGE. Support codes: 56562880""
        }

The code listed corresponds to a specific harmful category. These code to category mappings are as follows:

Error code | Safety category | Description | Content filtered: prompt input or image output  
---|---|---|---  
58061214  
17301594 | Child |  Detects child content where it isn't allowed due to the API request settings or allowlisting.  | input (prompt): 58061214  
output (image): 17301594  
29310472  
15236754 | Celebrity |  Detects a photorealistic representation of a celebrity in the request.  | input (prompt): 29310472  
output (image): 15236754  
62263041 | Dangerous content | Detects content that's potentially dangerous in nature. | input (prompt)  
57734940  
22137204 | Hate | Detects hate-related topics or content. | input (prompt): 57734940  
output (image): 22137204  
74803281  
29578790  
42876398 | Other | Detects other miscellaneous safety issues with the request. | input (prompt): 42876398  
output (image): 29578790, 74803281  
39322892 | People/Face |  Detects a person or face when it isn't allowed due to the request safety settings.  | output (image)  
92201652 | Personal information |  Detects Personally Identifiable Information (PII) in the text, such as the mentioning a credit card number, home addresses, or other such information.  | input (prompt)  
89371032  
49114662  
72817394 | Prohibited content | Detects the request of prohibited content in the request. | input (prompt): 89371032  
output (image): 49114662, 72817394  
90789179  
63429089  
43188360 | Sexual | Detects content that's sexual in nature. | input (prompt): 90789179  
output (image): 63429089, 43188360  
35561574  
35561575 | Third-party content | Guardrails related to third-party content. | input (prompt)  
output (image)  
78610348 | Toxic | Detects toxic topics or content in the text. | input (prompt)  
61493863  
56562880 | Violence | Detects violence-related content from the image or text. | input (prompt): 61493863  
output (image): 56562880  
32635315 | Vulgar | Detects vulgar topics or content from the text. | input (prompt)  
64151117 | Celebrity or child |  Detects photorealistic respresentation of a celebrity or of a child that violates Google's safety policies.  | input (prompt)   
output (image)  
  
## Limitations

The following limits apply to different tasks:

### Image generation and editing limitations

  * **Bias amplification** : While Imagen on Vertex AI can generate high-quality images, there may be potential biases in the generated content. Images generated rely on the product's training data, which can unintentionally include biases that may perpetuate stereotypes or discriminate against certain groups. Careful monitoring and evaluation are necessary to ensure the outputs align with Google's Acceptable Use Policy and your use case.
  * **Transparency and disclosure** : It can be difficult for users to differentiate between AI generated Imagery and non AI generated imagery. When using AI-generated images within your use case, it is important to clearly disclose to users that the images have been generated by an AI system to ensure transparency and maintain trust in the process. We've applied metadata labeling to AI-generated images to help combat the risk of misinformation and as part of our responsible approach to AI.
  * **Insufficient context** : Imagen on Vertex AI may lack the contextual understanding required to generate images that are appropriate for all situations or audiences within your use case. Be sure to check that your generated images align with your chosen context, purpose, and intended audience.
  * **Misrepresentation and authenticity** : Editing images using Imagen on Vertex AI can result in misrepresentation or manipulation of images, potentially leading to the creation of deceptive or misleading content. It is important to ensure that the editing process is used responsibly, without compromising the authenticity and truthfulness of the images edited. We've applied metadata labeling to AI-edited images to help combat the risk of misinformation and as part of our responsible approach to AI.
  * **Misrepresentation and authenticity** : Be cautious when editing images of adults or children, as editing images using Imagen on Vertex AI might result in misrepresentation or manipulation of images. This can potentially lead to the creation of deceptive or misleading content. It's important to ensure that the editing process is used responsibly, without compromising the authenticity and truthfulness of the images edited. We've applied metadata labeling to AI-edited images to help combat the risk of misinformation and as part of our responsible approach to AI.



### Visual captioning limitations

  * **Accuracy and context sensitivity** : Visual captioning may encounter challenges in accurately describing complex or ambiguous images. The generated descriptions may not always capture the complete context or nuances of the visual content. It is important to acknowledge that automated captioning systems have limitations in understanding images with varying levels of complexity, and their descriptions should be used with caution, particularly in critical or sensitive contexts.
  * **Ambiguity and subjective interpretations** : Images can often be open to multiple interpretations, and the generated captions may not always align with human understanding or expectations. Different individuals may perceive and describe images differently based on their subjective experiences and cultural backgrounds. It is crucial to consider the potential for ambiguity and subjectivity in image descriptions and provide additional context or alternative interpretations where necessary.
  * **Accessibility considerations** : While automated image captions can support accessibility by providing descriptions for visually impaired individuals, it is important to recognize that they may not fully replace human-generated alt-text or descriptions tailored to specific accessibility needs. Automated captions may lack the level of detail or contextual understanding necessary for certain accessibility use cases.



### Visual Question Answering (VQA) limitations

  * **Overconfidence and uncertainty** : VQA models may sometimes provide answers with unwarranted confidence, even when the correct answer is uncertain or ambiguous. It is essential to communicate the model's uncertainty and provide appropriate confidence scores or alternative answers when there is ambiguity, rather than conveying a false sense of certainty.



## Recommended practices

To utilize this technology safely and responsibly, it is also important to consider other risks specific to your use case, users, and business context in addition to built-in technical safeguards.

We recommend taking the following steps:

  1. Assess your application's security risks.
  2. Consider adjustments to mitigate safety risks.
  3. Perform safety testing appropriate to your use case.
  4. Solicit user feedback and monitor content.



## Additional Responsible AI resources

  * Learn about [Responsible AI for Large Language Models (LLMs)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai).
  * Learn more about Google's recommendations for [Responsible AI practices](https://ai.google/responsibilities/responsible-ai-practices/?category=general).
  * Read our blog, [A shared agenda for responsible AI progress](https://blog.google/technology/ai/a-shared-agenda-for-responsible-ai-progress/)



## Give feedback on Imagen on Vertex AI

If you receive an output or response that is inaccurate or that you feel is unsafe, you can let us know by [submitting feedback](https://google.qualtrics.com/jfe/form/SV_bltt8DuAzYaDkKG). Your feedback can help improve Imagen on Vertex AI and broader Google efforts in AI.

Because feedback may be human readable, don't submit data that contains personal, confidential, or sensitive information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
