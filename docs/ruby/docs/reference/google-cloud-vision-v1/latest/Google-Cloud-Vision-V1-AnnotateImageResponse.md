---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AnnotateImageResponse/
title: Cloud Vision V1 API - Class Google::Cloud::Vision::V1::AnnotateImageResponse (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:23.025475+00:00
---

# Cloud Vision V1 API - Class Google::Cloud::Vision::V1::AnnotateImageResponse (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-AnnotateImageResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1 API - Class Google::Cloud::Vision::V1::AnnotateImageResponse (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Vision V1 API class Google::Cloud::Vision::V1::AnnotateImageResponse.

Response to an image annotation request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #context
    
    
    def context() -> ::Google::Cloud::Vision::V1::ImageAnnotationContext

**Returns**

  * ([::Google::Cloud::Vision::V1::ImageAnnotationContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotationContext)) — If present, contextual information is needed to understand where this image comes from. 



### #context=
    
    
    def context=(value) -> ::Google::Cloud::Vision::V1::ImageAnnotationContext

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::ImageAnnotationContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotationContext)) — If present, contextual information is needed to understand where this image comes from. 



**Returns**

  * ([::Google::Cloud::Vision::V1::ImageAnnotationContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageAnnotationContext)) — If present, contextual information is needed to understand where this image comes from. 



### #crop_hints_annotation
    
    
    def crop_hints_annotation() -> ::Google::Cloud::Vision::V1::CropHintsAnnotation

**Returns**

  * ([::Google::Cloud::Vision::V1::CropHintsAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-CropHintsAnnotation)) — If present, crop hints have completed successfully. 



### #crop_hints_annotation=
    
    
    def crop_hints_annotation=(value) -> ::Google::Cloud::Vision::V1::CropHintsAnnotation

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::CropHintsAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-CropHintsAnnotation)) — If present, crop hints have completed successfully. 



**Returns**

  * ([::Google::Cloud::Vision::V1::CropHintsAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-CropHintsAnnotation)) — If present, crop hints have completed successfully. 



### #error
    
    
    def error() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Rpc-Status)) — If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set. 



### #error=
    
    
    def error=(value) -> ::Google::Rpc::Status

**Parameter**

  * **value** ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Rpc-Status)) — If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set. 



**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Rpc-Status)) — If set, represents the error message for the operation. Note that filled-in image annotations are guaranteed to be correct, even when `error` is set. 



### #face_annotations
    
    
    def face_annotations() -> ::Array<::Google::Cloud::Vision::V1::FaceAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::FaceAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-FaceAnnotation)>) — If present, face detection has completed successfully. 



### #face_annotations=
    
    
    def face_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::FaceAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::FaceAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-FaceAnnotation)>) — If present, face detection has completed successfully. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::FaceAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-FaceAnnotation)>) — If present, face detection has completed successfully. 



### #full_text_annotation
    
    
    def full_text_annotation() -> ::Google::Cloud::Vision::V1::TextAnnotation

**Returns**

  * ([::Google::Cloud::Vision::V1::TextAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation)) — If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text. 



### #full_text_annotation=
    
    
    def full_text_annotation=(value) -> ::Google::Cloud::Vision::V1::TextAnnotation

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::TextAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation)) — If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text. 



**Returns**

  * ([::Google::Cloud::Vision::V1::TextAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation)) — If present, text (OCR) detection or document (OCR) text detection has completed successfully. This annotation provides the structural hierarchy for the OCR detected text. 



### #image_properties_annotation
    
    
    def image_properties_annotation() -> ::Google::Cloud::Vision::V1::ImageProperties

**Returns**

  * ([::Google::Cloud::Vision::V1::ImageProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageProperties)) — If present, image properties were extracted successfully. 



### #image_properties_annotation=
    
    
    def image_properties_annotation=(value) -> ::Google::Cloud::Vision::V1::ImageProperties

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::ImageProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageProperties)) — If present, image properties were extracted successfully. 



**Returns**

  * ([::Google::Cloud::Vision::V1::ImageProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ImageProperties)) — If present, image properties were extracted successfully. 



### #label_annotations
    
    
    def label_annotations() -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, label detection has completed successfully. 



### #label_annotations=
    
    
    def label_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, label detection has completed successfully. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, label detection has completed successfully. 



### #landmark_annotations
    
    
    def landmark_annotations() -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, landmark detection has completed successfully. 



### #landmark_annotations=
    
    
    def landmark_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, landmark detection has completed successfully. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, landmark detection has completed successfully. 



### #localized_object_annotations
    
    
    def localized_object_annotations() -> ::Array<::Google::Cloud::Vision::V1::LocalizedObjectAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::LocalizedObjectAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-LocalizedObjectAnnotation)>) — If present, localized object detection has completed successfully. This will be sorted descending by confidence score. 



### #localized_object_annotations=
    
    
    def localized_object_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::LocalizedObjectAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::LocalizedObjectAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-LocalizedObjectAnnotation)>) — If present, localized object detection has completed successfully. This will be sorted descending by confidence score. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::LocalizedObjectAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-LocalizedObjectAnnotation)>) — If present, localized object detection has completed successfully. This will be sorted descending by confidence score. 



### #logo_annotations
    
    
    def logo_annotations() -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, logo detection has completed successfully. 



### #logo_annotations=
    
    
    def logo_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, logo detection has completed successfully. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, logo detection has completed successfully. 



### #product_search_results
    
    
    def product_search_results() -> ::Google::Cloud::Vision::V1::ProductSearchResults

**Returns**

  * ([::Google::Cloud::Vision::V1::ProductSearchResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ProductSearchResults)) — If present, product search has completed successfully. 



### #product_search_results=
    
    
    def product_search_results=(value) -> ::Google::Cloud::Vision::V1::ProductSearchResults

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::ProductSearchResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ProductSearchResults)) — If present, product search has completed successfully. 



**Returns**

  * ([::Google::Cloud::Vision::V1::ProductSearchResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-ProductSearchResults)) — If present, product search has completed successfully. 



### #safe_search_annotation
    
    
    def safe_search_annotation() -> ::Google::Cloud::Vision::V1::SafeSearchAnnotation

**Returns**

  * ([::Google::Cloud::Vision::V1::SafeSearchAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-SafeSearchAnnotation)) — If present, safe-search annotation has completed successfully. 



### #safe_search_annotation=
    
    
    def safe_search_annotation=(value) -> ::Google::Cloud::Vision::V1::SafeSearchAnnotation

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::SafeSearchAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-SafeSearchAnnotation)) — If present, safe-search annotation has completed successfully. 



**Returns**

  * ([::Google::Cloud::Vision::V1::SafeSearchAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-SafeSearchAnnotation)) — If present, safe-search annotation has completed successfully. 



### #text_annotations
    
    
    def text_annotations() -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, text (OCR) detection has completed successfully. 



### #text_annotations=
    
    
    def text_annotations=(value) -> ::Array<::Google::Cloud::Vision::V1::EntityAnnotation>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, text (OCR) detection has completed successfully. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::EntityAnnotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-EntityAnnotation)>) — If present, text (OCR) detection has completed successfully. 



### #web_detection
    
    
    def web_detection() -> ::Google::Cloud::Vision::V1::WebDetection

**Returns**

  * ([::Google::Cloud::Vision::V1::WebDetection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-WebDetection)) — If present, web detection has completed successfully. 



### #web_detection=
    
    
    def web_detection=(value) -> ::Google::Cloud::Vision::V1::WebDetection

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1::WebDetection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-WebDetection)) — If present, web detection has completed successfully. 



**Returns**

  * ([::Google::Cloud::Vision::V1::WebDetection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-WebDetection)) — If present, web detection has completed successfully. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
