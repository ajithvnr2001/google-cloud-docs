---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p1beta1.Feature.Type
title: Enum Feature.Type (3.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:49.833090+00:00
---

# Enum Feature.Type (3.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p1beta1.Feature.Type

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum Feature.Type (3.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.97.0 (latest)  3.93.0  3.92.0  3.91.0  3.89.0  3.86.0  3.85.0  3.83.0  3.81.0  3.80.0  3.78.0  3.76.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.68.0  3.66.0  3.65.0  3.62.0  3.61.0  3.60.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.3  2.1.4  2.0.29 
    
    
    public enum Feature.Type extends Enum<Feature.Type> implements ProtocolMessageEnum

Type of image feature.

Protobuf enum `google.cloud.vision.v1p1beta1.Feature.Type`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`CROP_HINTS` |  Run crop hints. `CROP_HINTS = 9;`  
`CROP_HINTS_VALUE` |  Run crop hints. `CROP_HINTS = 9;`  
`DOCUMENT_TEXT_DETECTION` |  Run dense text document OCR. Takes precedence when both DOCUMENT_TEXT_DETECTION and TEXT_DETECTION are present. `DOCUMENT_TEXT_DETECTION = 11;`  
`DOCUMENT_TEXT_DETECTION_VALUE` |  Run dense text document OCR. Takes precedence when both DOCUMENT_TEXT_DETECTION and TEXT_DETECTION are present. `DOCUMENT_TEXT_DETECTION = 11;`  
`FACE_DETECTION` |  Run face detection. `FACE_DETECTION = 1;`  
`FACE_DETECTION_VALUE` |  Run face detection. `FACE_DETECTION = 1;`  
`IMAGE_PROPERTIES` |  Compute a set of image properties, such as the image's dominant colors. `IMAGE_PROPERTIES = 7;`  
`IMAGE_PROPERTIES_VALUE` |  Compute a set of image properties, such as the image's dominant colors. `IMAGE_PROPERTIES = 7;`  
`LABEL_DETECTION` |  Run label detection. `LABEL_DETECTION = 4;`  
`LABEL_DETECTION_VALUE` |  Run label detection. `LABEL_DETECTION = 4;`  
`LANDMARK_DETECTION` |  Run landmark detection. `LANDMARK_DETECTION = 2;`  
`LANDMARK_DETECTION_VALUE` |  Run landmark detection. `LANDMARK_DETECTION = 2;`  
`LOGO_DETECTION` |  Run logo detection. `LOGO_DETECTION = 3;`  
`LOGO_DETECTION_VALUE` |  Run logo detection. `LOGO_DETECTION = 3;`  
`SAFE_SEARCH_DETECTION` |  Run computer vision models to compute image safe-search properties. `SAFE_SEARCH_DETECTION = 6;`  
`SAFE_SEARCH_DETECTION_VALUE` |  Run computer vision models to compute image safe-search properties. `SAFE_SEARCH_DETECTION = 6;`  
`TEXT_DETECTION` |  Run OCR. `TEXT_DETECTION = 5;`  
`TEXT_DETECTION_VALUE` |  Run OCR. `TEXT_DETECTION = 5;`  
`TYPE_UNSPECIFIED` |  Unspecified feature type. `TYPE_UNSPECIFIED = 0;`  
`TYPE_UNSPECIFIED_VALUE` |  Unspecified feature type. `TYPE_UNSPECIFIED = 0;`  
`UNRECOGNIZED` |   
`WEB_DETECTION` |  Run web detection. `WEB_DETECTION = 10;`  
`WEB_DETECTION_VALUE` |  Run web detection. `WEB_DETECTION = 10;`  
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1p1beta1.Feature.Type#com_google_cloud_vision_v1p1beta1_Feature_Type_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
