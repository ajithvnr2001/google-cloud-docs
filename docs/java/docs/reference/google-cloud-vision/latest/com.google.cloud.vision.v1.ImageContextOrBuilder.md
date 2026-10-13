---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageContextOrBuilder
title: Interface ImageContextOrBuilder (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:19.928276+00:00
---

# Interface ImageContextOrBuilder (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ImageContextOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImageContextOrBuilder (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.3  2.1.4  2.0.29 
    
    
    public interface ImageContextOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCropHintsParams()
    
    
    public abstract CropHintsParams getCropHintsParams()

Parameters for crop hints annotation request.

`.google.cloud.vision.v1.CropHintsParams crop_hints_params = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CropHintsParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.CropHintsParams)` | The cropHintsParams.  
  
### getCropHintsParamsOrBuilder()
    
    
    public abstract CropHintsParamsOrBuilder getCropHintsParamsOrBuilder()

Parameters for crop hints annotation request.

`.google.cloud.vision.v1.CropHintsParams crop_hints_params = 4;`

**Returns**  
---  
**Type** | **Description**  
`[CropHintsParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.CropHintsParamsOrBuilder)` |   
  
### getLanguageHints(int index)
    
    
    public abstract String getLanguageHints(int index)

List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages).

`repeated string language_hints = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageHints at the given index.  
  
### getLanguageHintsBytes(int index)
    
    
    public abstract ByteString getLanguageHintsBytes(int index)

List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages).

`repeated string language_hints = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the languageHints at the given index.  
  
### getLanguageHintsCount()
    
    
    public abstract int getLanguageHintsCount()

List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages).

`repeated string language_hints = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of languageHints.  
  
### getLanguageHintsList()
    
    
    public abstract List<String> getLanguageHintsList()

List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the [supported languages](https://cloud.google.com/vision/docs/languages).

`repeated string language_hints = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the languageHints.  
  
### getLatLongRect()
    
    
    public abstract LatLongRect getLatLongRect()

Not used.

`.google.cloud.vision.v1.LatLongRect lat_long_rect = 1;`

**Returns**  
---  
**Type** | **Description**  
`[LatLongRect](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LatLongRect)` | The latLongRect.  
  
### getLatLongRectOrBuilder()
    
    
    public abstract LatLongRectOrBuilder getLatLongRectOrBuilder()

Not used.

`.google.cloud.vision.v1.LatLongRect lat_long_rect = 1;`

**Returns**  
---  
**Type** | **Description**  
`[LatLongRectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LatLongRectOrBuilder)` |   
  
### getProductSearchParams()
    
    
    public abstract ProductSearchParams getProductSearchParams()

Parameters for product search.

`.google.cloud.vision.v1.ProductSearchParams product_search_params = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ProductSearchParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchParams)` | The productSearchParams.  
  
### getProductSearchParamsOrBuilder()
    
    
    public abstract ProductSearchParamsOrBuilder getProductSearchParamsOrBuilder()

Parameters for product search.

`.google.cloud.vision.v1.ProductSearchParams product_search_params = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ProductSearchParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchParamsOrBuilder)` |   
  
### getTextDetectionParams()
    
    
    public abstract TextDetectionParams getTextDetectionParams()

Parameters for text detection and document text detection.

`.google.cloud.vision.v1.TextDetectionParams text_detection_params = 12;`

**Returns**  
---  
**Type** | **Description**  
`[TextDetectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.TextDetectionParams)` | The textDetectionParams.  
  
### getTextDetectionParamsOrBuilder()
    
    
    public abstract TextDetectionParamsOrBuilder getTextDetectionParamsOrBuilder()

Parameters for text detection and document text detection.

`.google.cloud.vision.v1.TextDetectionParams text_detection_params = 12;`

**Returns**  
---  
**Type** | **Description**  
`[TextDetectionParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.TextDetectionParamsOrBuilder)` |   
  
### getWebDetectionParams()
    
    
    public abstract WebDetectionParams getWebDetectionParams()

Parameters for web detection.

`.google.cloud.vision.v1.WebDetectionParams web_detection_params = 6;`

**Returns**  
---  
**Type** | **Description**  
`[WebDetectionParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetectionParams)` | The webDetectionParams.  
  
### getWebDetectionParamsOrBuilder()
    
    
    public abstract WebDetectionParamsOrBuilder getWebDetectionParamsOrBuilder()

Parameters for web detection.

`.google.cloud.vision.v1.WebDetectionParams web_detection_params = 6;`

**Returns**  
---  
**Type** | **Description**  
`[WebDetectionParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.WebDetectionParamsOrBuilder)` |   
  
### hasCropHintsParams()
    
    
    public abstract boolean hasCropHintsParams()

Parameters for crop hints annotation request.

`.google.cloud.vision.v1.CropHintsParams crop_hints_params = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cropHintsParams field is set.  
  
### hasLatLongRect()
    
    
    public abstract boolean hasLatLongRect()

Not used.

`.google.cloud.vision.v1.LatLongRect lat_long_rect = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latLongRect field is set.  
  
### hasProductSearchParams()
    
    
    public abstract boolean hasProductSearchParams()

Parameters for product search.

`.google.cloud.vision.v1.ProductSearchParams product_search_params = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the productSearchParams field is set.  
  
### hasTextDetectionParams()
    
    
    public abstract boolean hasTextDetectionParams()

Parameters for text detection and document text detection.

`.google.cloud.vision.v1.TextDetectionParams text_detection_params = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textDetectionParams field is set.  
  
### hasWebDetectionParams()
    
    
    public abstract boolean hasWebDetectionParams()

Parameters for web detection.

`.google.cloud.vision.v1.WebDetectionParams web_detection_params = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the webDetectionParams field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
