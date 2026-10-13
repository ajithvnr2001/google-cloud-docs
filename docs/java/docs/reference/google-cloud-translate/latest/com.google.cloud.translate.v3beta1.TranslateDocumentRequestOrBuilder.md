---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateDocumentRequestOrBuilder
title: Interface TranslateDocumentRequestOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:24.382116+00:00
---

# Interface TranslateDocumentRequestOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateDocumentRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TranslateDocumentRequestOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.5  2.2.0  2.1.13 
    
    
    public interface TranslateDocumentRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

See <https://cloud.google.com/translate/docs/advanced/labels> for more information.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomizedAttribution()
    
    
    public abstract String getCustomizedAttribution()

Optional. This flag is to support user customized attribution. If not provided, the default is `Machine Translated by Google`. Customized attribution should follow rules in <https://cloud.google.com/translate/attribution#attribution_and_logos>

`string customized_attribution = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customizedAttribution.  
  
### getCustomizedAttributionBytes()
    
    
    public abstract ByteString getCustomizedAttributionBytes()

Optional. This flag is to support user customized attribution. If not provided, the default is `Machine Translated by Google`. Customized attribution should follow rules in <https://cloud.google.com/translate/attribution#attribution_and_logos>

`string customized_attribution = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customizedAttribution.  
  
### getDocumentInputConfig()
    
    
    public abstract DocumentInputConfig getDocumentInputConfig()

Required. Input configurations.

` .google.cloud.translation.v3beta1.DocumentInputConfig document_input_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentInputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DocumentInputConfig)` | The documentInputConfig.  
  
### getDocumentInputConfigOrBuilder()
    
    
    public abstract DocumentInputConfigOrBuilder getDocumentInputConfigOrBuilder()

Required. Input configurations.

` .google.cloud.translation.v3beta1.DocumentInputConfig document_input_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentInputConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DocumentInputConfigOrBuilder)` |   
  
### getDocumentOutputConfig()
    
    
    public abstract DocumentOutputConfig getDocumentOutputConfig()

Optional. Output configurations. Defines if the output file should be stored within Cloud Storage as well as the desired output format. If not provided the translated file will only be returned through a byte-stream and its output mime type will be the same as the input file's mime type.

` .google.cloud.translation.v3beta1.DocumentOutputConfig document_output_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentOutputConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DocumentOutputConfig)` | The documentOutputConfig.  
  
### getDocumentOutputConfigOrBuilder()
    
    
    public abstract DocumentOutputConfigOrBuilder getDocumentOutputConfigOrBuilder()

Optional. Output configurations. Defines if the output file should be stored within Cloud Storage as well as the desired output format. If not provided the translated file will only be returned through a byte-stream and its output mime type will be the same as the input file's mime type.

` .google.cloud.translation.v3beta1.DocumentOutputConfig document_output_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentOutputConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.DocumentOutputConfigOrBuilder)` |   
  
### getEnableRotationCorrection()
    
    
    public abstract boolean getEnableRotationCorrection()

Optional. If true, enable auto rotation correction in DVS.

`bool enable_rotation_correction = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableRotationCorrection.  
  
### getEnableShadowRemovalNativePdf()
    
    
    public abstract boolean getEnableShadowRemovalNativePdf()

Optional. If true, use the text removal server to remove the shadow text on background image for native pdf translation. Shadow removal feature can only be enabled when is_translate_native_pdf_only: false && pdf_native_only: false

`bool enable_shadow_removal_native_pdf = 12 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableShadowRemovalNativePdf.  
  
### getGlossaryConfig()
    
    
    public abstract TranslateTextGlossaryConfig getGlossaryConfig()

Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned.

` .google.cloud.translation.v3beta1.TranslateTextGlossaryConfig glossary_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateTextGlossaryConfig)` | The glossaryConfig.  
  
### getGlossaryConfigOrBuilder()
    
    
    public abstract TranslateTextGlossaryConfigOrBuilder getGlossaryConfigOrBuilder()

Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned.

` .google.cloud.translation.v3beta1.TranslateTextGlossaryConfig glossary_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TranslateTextGlossaryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateTextGlossaryConfigOrBuilder)` |   
  
### getIsTranslateNativePdfOnly()
    
    
    public abstract boolean getIsTranslateNativePdfOnly()

Optional. is_translate_native_pdf_only field for external customers. If true, the page limit of online native pdf translation is 300 and only native pdf pages will be translated.

`bool is_translate_native_pdf_only = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isTranslateNativePdfOnly.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-translate/latest/com.google.cloud.translate.v3beta1.TranslateDocumentRequestOrBuilder#com_google_cloud_translate_v3beta1_TranslateDocumentRequestOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

See <https://cloud.google.com/translate/docs/advanced/labels> for more information.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

See <https://cloud.google.com/translate/docs/advanced/labels> for more information.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

See <https://cloud.google.com/translate/docs/advanced/labels> for more information.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. The labels with user-defined metadata for the request.

Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.

See <https://cloud.google.com/translate/docs/advanced/labels> for more information.

`map<string, string> labels = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getModel()
    
    
    public abstract String getModel()

Optional. The `model` type requested for this translation.

The format depends on model type:

  * AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`

  * General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,




If not provided, the default Google model (NMT) will be used for translation.

`string model = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The model.  
  
### getModelBytes()
    
    
    public abstract ByteString getModelBytes()

Optional. The `model` type requested for this translation.

The format depends on model type:

  * AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`

  * General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,




If not provided, the default Google model (NMT) will be used for translation.

`string model = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for model.  
  
### getParent()
    
    
    public abstract String getParent()

Required. Location to make a regional call.

Format: `projects/{project-number-or-id}/locations/{location-id}`.

For global calls, use `projects/{project-number-or-id}/locations/global`.

Non-global location is required for requests using AutoML models or custom glossaries.

Models and glossaries must be within the same region (have the same location-id), otherwise an INVALID_ARGUMENT (400) error is returned.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Location to make a regional call.

Format: `projects/{project-number-or-id}/locations/{location-id}`.

For global calls, use `projects/{project-number-or-id}/locations/global`.

Non-global location is required for requests using AutoML models or custom glossaries.

Models and glossaries must be within the same region (have the same location-id), otherwise an INVALID_ARGUMENT (400) error is returned.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getSourceLanguageCode()
    
    
    public abstract String getSourceLanguageCode()

Optional. The BCP-47 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in [Language Support](https://cloud.google.com/translate/docs/languages). If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. Source language must be specified if the request contains a glossary or a custom model.

`string source_language_code = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceLanguageCode.  
  
### getSourceLanguageCodeBytes()
    
    
    public abstract ByteString getSourceLanguageCodeBytes()

Optional. The BCP-47 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in [Language Support](https://cloud.google.com/translate/docs/languages). If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. Source language must be specified if the request contains a glossary or a custom model.

`string source_language_code = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceLanguageCode.  
  
### getTargetLanguageCode()
    
    
    public abstract String getTargetLanguageCode()

Required. The BCP-47 language code to use for translation of the input document, set to one of the language codes listed in [Language Support](https://cloud.google.com/translate/docs/languages).

`string target_language_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetLanguageCode.  
  
### getTargetLanguageCodeBytes()
    
    
    public abstract ByteString getTargetLanguageCodeBytes()

Required. The BCP-47 language code to use for translation of the input document, set to one of the language codes listed in [Language Support](https://cloud.google.com/translate/docs/languages).

`string target_language_code = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetLanguageCode.  
  
### hasDocumentInputConfig()
    
    
    public abstract boolean hasDocumentInputConfig()

Required. Input configurations.

` .google.cloud.translation.v3beta1.DocumentInputConfig document_input_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentInputConfig field is set.  
  
### hasDocumentOutputConfig()
    
    
    public abstract boolean hasDocumentOutputConfig()

Optional. Output configurations. Defines if the output file should be stored within Cloud Storage as well as the desired output format. If not provided the translated file will only be returned through a byte-stream and its output mime type will be the same as the input file's mime type.

` .google.cloud.translation.v3beta1.DocumentOutputConfig document_output_config = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentOutputConfig field is set.  
  
### hasGlossaryConfig()
    
    
    public abstract boolean hasGlossaryConfig()

Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned.

` .google.cloud.translation.v3beta1.TranslateTextGlossaryConfig glossary_config = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the glossaryConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
