---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation/
title: ImageSegmentationAnnotation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:55:19.948748+00:00
---

# ImageSegmentationAnnotation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ImageSegmentationAnnotation Stay organized with collections  Save and categorize content based on your preferences. 

Annotation details specific to image segmentation.

Fields  
  
`annotation` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`maskAnnotation` `object (`[MaskAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#MaskAnnotation)`)` Mask based segmentation annotation. Only one mask annotation can exist for one image. | `polygonAnnotation` `object (`[PolygonAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#PolygonAnnotation)`)` Polygon annotation. | `polylineAnnotation` `object (`[PolylineAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#PolylineAnnotation)`)` Polyline annotation. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // annotation
      "maskAnnotation": {
        object ([MaskAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#MaskAnnotation))
      },
      "polygonAnnotation": {
        object ([PolygonAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#PolygonAnnotation))
      },
      "polylineAnnotation": {
        object ([PolylineAnnotation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#PolylineAnnotation))
      }
      // Union type
    }  
  
## MaskAnnotation

The mask based segmentation annotation.

Fields  
  
`maskGcsUri` `string` Google Cloud Storage URI that points to the mask image. The image must be in PNG format. It must have the same size as the DataItem's image. Each pixel in the image mask represents the AnnotationSpec which the pixel in the image DataItem belong to. Each color is mapped to one AnnotationSpec based on annotationSpecColors. | `annotationSpecColors[]` `object (`[AnnotationSpecColor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AnnotationSpecColor)`)` The mapping between color and AnnotationSpec for this Annotation. | JSON representation  
---  
      
    
    {
      "maskGcsUri": string,
      "annotationSpecColors": [
        {
          object ([AnnotationSpecColor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/AnnotationSpecColor))
        }
      ]
    }  
  
## PolygonAnnotation

Represents a polygon in image.

Fields  
  
`vertexes[]` `object (`[Vertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#Vertex)`)` The vertexes are connected one by one and the last vertex is connected to the first one to represent a polygon. | `annotationSpecId` `string` The resource id of the AnnotationSpec that this Annotation pertains to. | `displayName` `string` The display name of the AnnotationSpec that this Annotation pertains to. | JSON representation  
---  
      
    
    {
      "vertexes": [
        {
          object ([Vertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#Vertex))
        }
      ],
      "annotationSpecId": string,
      "displayName": string
    }  
  
## Vertex

Represents a 2D point in the image. Vertex coordinates are normalized to be relative to the original image dimensions and range from 0 to 1. The origin of the coordinate system (0,0) is the top-left corner of the image. x increases to the right, and y increases to the bottom.

Fields  
  
`x` `number` X coordinate of the vertex, normalized to [0.0, 1.0]. | `y` `number` Y coordinate of the vertex, normalized to [0.0, 1.0]. | JSON representation  
---  
      
    
    {
      "x": number,
      "y": number
    }  
  
## PolylineAnnotation

Represents a polyline in image.

Fields  
  
`vertexes[]` `object (`[Vertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#Vertex)`)` The vertexes are connected one by one and the last vertex in not connected to the first one. | `annotationSpecId` `string` The resource id of the AnnotationSpec that this Annotation pertains to. | `displayName` `string` The display name of the AnnotationSpec that this Annotation pertains to. | JSON representation  
---  
      
    
    {
      "vertexes": [
        {
          object ([Vertex](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationAnnotation#Vertex))
        }
      ],
      "annotationSpecId": string,
      "displayName": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
