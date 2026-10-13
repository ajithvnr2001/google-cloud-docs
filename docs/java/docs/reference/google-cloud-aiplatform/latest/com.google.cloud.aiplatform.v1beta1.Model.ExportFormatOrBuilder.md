---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Model.ExportFormatOrBuilder
title: Interface Model.ExportFormatOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:04.124370+00:00
---

# Interface Model.ExportFormatOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Model.ExportFormatOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Model.ExportFormatOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface Model.ExportFormatOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExportableContents(int index)
    
    
    public abstract Model.ExportFormat.ExportableContent getExportableContents(int index)

Output only. The content of this Model that may be exported.

` repeated .google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent exportable_contents = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Model.ExportFormat.ExportableContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent)` | The exportableContents at the given index.  
  
### getExportableContentsCount()
    
    
    public abstract int getExportableContentsCount()

Output only. The content of this Model that may be exported.

` repeated .google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent exportable_contents = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of exportableContents.  
  
### getExportableContentsList()
    
    
    public abstract List<Model.ExportFormat.ExportableContent> getExportableContentsList()

Output only. The content of this Model that may be exported.

` repeated .google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent exportable_contents = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExportableContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent)>` | A list containing the exportableContents.  
  
### getExportableContentsValue(int index)
    
    
    public abstract int getExportableContentsValue(int index)

Output only. The content of this Model that may be exported.

` repeated .google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent exportable_contents = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of exportableContents at the given index.  
  
### getExportableContentsValueList()
    
    
    public abstract List<Integer> getExportableContentsValueList()

Output only. The content of this Model that may be exported.

` repeated .google.cloud.aiplatform.v1beta1.Model.ExportFormat.ExportableContent exportable_contents = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for exportableContents.  
  
### getId()
    
    
    public abstract String getId()

Output only. The ID of the export format. The possible format IDs are:

  * `tflite` Used for Android mobile devices.

  * `edgetpu-tflite` Used for [Edge TPU](https://cloud.google.com/edge-tpu/) devices.

  * `tf-saved-model` A tensorflow model in SavedModel format.

  * `tf-js` A [TensorFlow.js](https://www.tensorflow.org/js) model that can be used in the browser and in Node.js using JavaScript.

  * `core-ml` Used for iOS mobile devices.

  * `custom-trained` A Model that was uploaded or trained by custom code.




`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Output only. The ID of the export format. The possible format IDs are:

  * `tflite` Used for Android mobile devices.

  * `edgetpu-tflite` Used for [Edge TPU](https://cloud.google.com/edge-tpu/) devices.

  * `tf-saved-model` A tensorflow model in SavedModel format.

  * `tf-js` A [TensorFlow.js](https://www.tensorflow.org/js) model that can be used in the browser and in Node.js using JavaScript.

  * `core-ml` Used for iOS mobile devices.

  * `custom-trained` A Model that was uploaded or trained by custom code.




`string id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
