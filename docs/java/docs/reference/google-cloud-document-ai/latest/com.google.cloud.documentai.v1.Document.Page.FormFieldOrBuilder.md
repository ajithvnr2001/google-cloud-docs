---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.FormFieldOrBuilder
title: Interface Document.Page.FormFieldOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:25.485057+00:00
---

# Interface Document.Page.FormFieldOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.FormFieldOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Document.Page.FormFieldOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static interface Document.Page.FormFieldOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCorrectedKeyText()
    
    
    public abstract String getCorrectedKeyText()

Created for Labeling UI to export key text. If corrections were made to the text identified by the `field_name.text_anchor`, this field will contain the correction.

`string corrected_key_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The correctedKeyText.  
  
### getCorrectedKeyTextBytes()
    
    
    public abstract ByteString getCorrectedKeyTextBytes()

Created for Labeling UI to export key text. If corrections were made to the text identified by the `field_name.text_anchor`, this field will contain the correction.

`string corrected_key_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for correctedKeyText.  
  
### getCorrectedValueText()
    
    
    public abstract String getCorrectedValueText()

Created for Labeling UI to export value text. If corrections were made to the text identified by the `field_value.text_anchor`, this field will contain the correction.

`string corrected_value_text = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The correctedValueText.  
  
### getCorrectedValueTextBytes()
    
    
    public abstract ByteString getCorrectedValueTextBytes()

Created for Labeling UI to export value text. If corrections were made to the text identified by the `field_value.text_anchor`, this field will contain the correction.

`string corrected_value_text = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for correctedValueText.  
  
### getFieldName()
    
    
    public abstract Document.Page.Layout getFieldName()

Layout for the FormField name. For example, `Address`, `Email`, `Grand total`, `Phone number`, etc.

`.google.cloud.documentai.v1.Document.Page.Layout field_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Page.Layout](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Layout)` | The fieldName.  
  
### getFieldNameOrBuilder()
    
    
    public abstract Document.Page.LayoutOrBuilder getFieldNameOrBuilder()

Layout for the FormField name. For example, `Address`, `Email`, `Grand total`, `Phone number`, etc.

`.google.cloud.documentai.v1.Document.Page.Layout field_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Page.LayoutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.LayoutOrBuilder)` |   
  
### getFieldValue()
    
    
    public abstract Document.Page.Layout getFieldValue()

Layout for the FormField value.

`.google.cloud.documentai.v1.Document.Page.Layout field_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Page.Layout](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.Layout)` | The fieldValue.  
  
### getFieldValueOrBuilder()
    
    
    public abstract Document.Page.LayoutOrBuilder getFieldValueOrBuilder()

Layout for the FormField value.

`.google.cloud.documentai.v1.Document.Page.Layout field_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Page.LayoutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.LayoutOrBuilder)` |   
  
### getNameDetectedLanguages(int index)
    
    
    public abstract Document.Page.DetectedLanguage getNameDetectedLanguages(int index)

A list of detected languages for name together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage name_detected_languages = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Document.Page.DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguage)` |   
  
### getNameDetectedLanguagesCount()
    
    
    public abstract int getNameDetectedLanguagesCount()

A list of detected languages for name together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage name_detected_languages = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNameDetectedLanguagesList()
    
    
    public abstract List<Document.Page.DetectedLanguage> getNameDetectedLanguagesList()

A list of detected languages for name together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage name_detected_languages = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguage)>` |   
  
### getNameDetectedLanguagesOrBuilder(int index)
    
    
    public abstract Document.Page.DetectedLanguageOrBuilder getNameDetectedLanguagesOrBuilder(int index)

A list of detected languages for name together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage name_detected_languages = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Document.Page.DetectedLanguageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguageOrBuilder)` |   
  
### getNameDetectedLanguagesOrBuilderList()
    
    
    public abstract List<? extends Document.Page.DetectedLanguageOrBuilder> getNameDetectedLanguagesOrBuilderList()

A list of detected languages for name together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage name_detected_languages = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.documentai.v1.Document.Page.DetectedLanguageOrBuilder>` |   
  
### getProvenance()
    
    
    public abstract Document.Provenance getProvenance()

The history of this annotation.

`.google.cloud.documentai.v1.Document.Provenance provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Document.Provenance](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Provenance)` | The provenance.  
  
### getProvenanceOrBuilder()
    
    
    public abstract Document.ProvenanceOrBuilder getProvenanceOrBuilder()

The history of this annotation.

`.google.cloud.documentai.v1.Document.Provenance provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Document.ProvenanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.ProvenanceOrBuilder)` |   
  
### getValueDetectedLanguages(int index)
    
    
    public abstract Document.Page.DetectedLanguage getValueDetectedLanguages(int index)

A list of detected languages for value together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage value_detected_languages = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Document.Page.DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguage)` |   
  
### getValueDetectedLanguagesCount()
    
    
    public abstract int getValueDetectedLanguagesCount()

A list of detected languages for value together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage value_detected_languages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getValueDetectedLanguagesList()
    
    
    public abstract List<Document.Page.DetectedLanguage> getValueDetectedLanguagesList()

A list of detected languages for value together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage value_detected_languages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DetectedLanguage](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguage)>` |   
  
### getValueDetectedLanguagesOrBuilder(int index)
    
    
    public abstract Document.Page.DetectedLanguageOrBuilder getValueDetectedLanguagesOrBuilder(int index)

A list of detected languages for value together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage value_detected_languages = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Document.Page.DetectedLanguageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.Document.Page.DetectedLanguageOrBuilder)` |   
  
### getValueDetectedLanguagesOrBuilderList()
    
    
    public abstract List<? extends Document.Page.DetectedLanguageOrBuilder> getValueDetectedLanguagesOrBuilderList()

A list of detected languages for value together with confidence.

` repeated .google.cloud.documentai.v1.Document.Page.DetectedLanguage value_detected_languages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.documentai.v1.Document.Page.DetectedLanguageOrBuilder>` |   
  
### getValueType()
    
    
    public abstract String getValueType()

If the value is non-textual, this field represents the type. Current valid values are:

  * blank (this indicates the `field_value` is normal text)
  * `unfilled_checkbox`
  * `filled_checkbox`



`string value_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The valueType.  
  
### getValueTypeBytes()
    
    
    public abstract ByteString getValueTypeBytes()

If the value is non-textual, this field represents the type. Current valid values are:

  * blank (this indicates the `field_value` is normal text)
  * `unfilled_checkbox`
  * `filled_checkbox`



`string value_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for valueType.  
  
### hasFieldName()
    
    
    public abstract boolean hasFieldName()

Layout for the FormField name. For example, `Address`, `Email`, `Grand total`, `Phone number`, etc.

`.google.cloud.documentai.v1.Document.Page.Layout field_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fieldName field is set.  
  
### hasFieldValue()
    
    
    public abstract boolean hasFieldValue()

Layout for the FormField value.

`.google.cloud.documentai.v1.Document.Page.Layout field_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fieldValue field is set.  
  
### hasProvenance()
    
    
    public abstract boolean hasProvenance()

The history of this annotation.

`.google.cloud.documentai.v1.Document.Provenance provenance = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the provenance field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
