---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance/
title: VirtualTryOnModelInstance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:59:52.738774+00:00
---

# VirtualTryOnModelInstance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VirtualTryOnModelInstance Stay organized with collections  Save and categorize content based on your preferences. 

Media generation input format for the Virtual Try On model.

Fields  
  
`prompt` `string` The text prompt describing the desired image. | `productImages[]` `object (`[ProductImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#ProductImage)`)` Required. A single product image to try on the person. | `personImage` `object (`[PersonImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#PersonImage)`)` The image of the person to virtually try-on clothing. | JSON representation  
---  
      
    
    {
      "prompt": string,
      "productImages": [
        {
          object ([ProductImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#ProductImage))
        }
      ],
      "personImage": {
        object ([PersonImage](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#PersonImage))
      }
    }  
  
## ProductImage

A ProductImage is used to provide the product image and its associated configuration options for Virtual Try On.

Fields  
  
`image` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image)`)` Required. An image of a product to virtually try on a person. The following values are supported: - A `bytesBase64` encoded string that encodes the image. - A `gcsUri` string URI to a Google Cloud Storage bucket location. | `maskImage` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image)`)` (Optional) The mask image associated with this product. If provided, the mask image is used to guide the image editing. | `productImageConfig` `object (`[ProductImageConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#ProductImageConfig)`)` The configuration for the product image. | JSON representation  
---  
      
    
    {
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image))
      },
      "maskImage": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image))
      },
      "productImageConfig": {
        object ([ProductImageConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#ProductImageConfig))
      }
    }  
  
## Image

Represents the input image and metadata for virtual try-on.

Fields  
  
`mimeType` `string` The MIME type of the image. The following values are supported: - image/jpeg - image/png | `data` `Union type`  
  
Image content for virtual try-on. The following values are supported: - A `bytesBase64` encoded string that encodes the image. - A `gcsUri` string URI to a Google Cloud Storage bucket location. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bytesBase64Encoded` `string` The base64-encoded bytes of the image. | `gcsUri` `string` The Google Cloud Storage URI of the image. The URI must be in `gs://` format. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // data
      "bytesBase64Encoded": string,
      "gcsUri": string
      // Union type
    }  
  
## ProductImageConfig

Configuration for the product image.

Fields  
  
`maskMode` `enum (`[MaskMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MaskMode)`)` Mode used to control the segmentation logic. | `dilation` `number` (Optional) Factor for dilating the mask. Valid values are in [0.0, 1.0]. If unset, dilation defaults to `0`. | `productDescription` `string` (Optional) A text description of the product. | JSON representation  
---  
      
    
    {
      "maskMode": enum ([MaskMode](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/MaskMode)),
      "dilation": number,
      "productDescription": string
    }  
  
## PersonImage

An image of a person. The model generates a virtual try-on image with the supplied image of the person wearing the garments from `productImages`.

Fields  
  
`image` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image)`)` Required. An image of a person to try-on the clothing product. The following values are supported: - A `bytesBase64` encoded string that encodes the image. - A `gcsUri` string URI to a Google Cloud Storage bucket location. | JSON representation  
---  
      
    
    {
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelInstance#Image))
      }
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
