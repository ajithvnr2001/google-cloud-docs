---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfigOrBuilder
title: Interface OcrConfigOrBuilder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:23.368725+00:00
---

# Interface OcrConfigOrBuilder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OcrConfigOrBuilder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public interface OcrConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdvancedOcrOptions(int index)
    
    
    public abstract String getAdvancedOcrOptions(int index)

A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are:

  * `legacy_layout`: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation.



`repeated string advanced_ocr_options = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The advancedOcrOptions at the given index.  
  
### getAdvancedOcrOptionsBytes(int index)
    
    
    public abstract ByteString getAdvancedOcrOptionsBytes(int index)

A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are:

  * `legacy_layout`: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation.



`repeated string advanced_ocr_options = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the advancedOcrOptions at the given index.  
  
### getAdvancedOcrOptionsCount()
    
    
    public abstract int getAdvancedOcrOptionsCount()

A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are:

  * `legacy_layout`: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation.



`repeated string advanced_ocr_options = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of advancedOcrOptions.  
  
### getAdvancedOcrOptionsList()
    
    
    public abstract List<String> getAdvancedOcrOptionsList()

A list of advanced OCR options to further fine-tune OCR behavior. Current valid values are:

  * `legacy_layout`: a heuristics layout detection algorithm, which serves as an alternative to the current ML-based layout detection algorithm. Customers can choose the best suitable layout algorithm based on their situation.



`repeated string advanced_ocr_options = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the advancedOcrOptions.  
  
### getComputeStyleInfo() (deprecated)
    
    
    public abstract boolean getComputeStyleInfo()

**Deprecated.** _google.cloud.documentai.v1.OcrConfig.compute_style_info is deprecated. See google/cloud/documentai/v1/document_io.proto;l=166_

Turn on font identification model and return font style information. Deprecated, use PremiumFeatures.compute_style_info instead.

`bool compute_style_info = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The computeStyleInfo.  
  
### getDisableCharacterBoxesDetection()
    
    
    public abstract boolean getDisableCharacterBoxesDetection()

Turn off character box detector in OCR engine. Character box detection is enabled by default in OCR 2.0 (and later) processors.

`bool disable_character_boxes_detection = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableCharacterBoxesDetection.  
  
### getEnableImageQualityScores()
    
    
    public abstract boolean getEnableImageQualityScores()

Enables intelligent document quality scores after OCR. Can help with diagnosing why OCR responses are of poor quality for a given input. Adds additional latency comparable to regular OCR to the process call.

`bool enable_image_quality_scores = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableImageQualityScores.  
  
### getEnableNativePdfParsing()
    
    
    public abstract boolean getEnableNativePdfParsing()

Enables special handling for PDFs with existing text information. Results in better text extraction quality in such PDF inputs.

`bool enable_native_pdf_parsing = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableNativePdfParsing.  
  
### getEnableSymbol()
    
    
    public abstract boolean getEnableSymbol()

Includes symbol level OCR information if set to true.

`bool enable_symbol = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableSymbol.  
  
### getHints()
    
    
    public abstract OcrConfig.Hints getHints()

Hints for the OCR model.

`.google.cloud.documentai.v1.OcrConfig.Hints hints = 2;`

**Returns**  
---  
**Type** | **Description**  
`[OcrConfig.Hints](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfig.Hints)` | The hints.  
  
### getHintsOrBuilder()
    
    
    public abstract OcrConfig.HintsOrBuilder getHintsOrBuilder()

Hints for the OCR model.

`.google.cloud.documentai.v1.OcrConfig.Hints hints = 2;`

**Returns**  
---  
**Type** | **Description**  
`[OcrConfig.HintsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfig.HintsOrBuilder)` |   
  
### getPremiumFeatures()
    
    
    public abstract OcrConfig.PremiumFeatures getPremiumFeatures()

Configurations for premium OCR features.

`.google.cloud.documentai.v1.OcrConfig.PremiumFeatures premium_features = 11;`

**Returns**  
---  
**Type** | **Description**  
`[OcrConfig.PremiumFeatures](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfig.PremiumFeatures)` | The premiumFeatures.  
  
### getPremiumFeaturesOrBuilder()
    
    
    public abstract OcrConfig.PremiumFeaturesOrBuilder getPremiumFeaturesOrBuilder()

Configurations for premium OCR features.

`.google.cloud.documentai.v1.OcrConfig.PremiumFeatures premium_features = 11;`

**Returns**  
---  
**Type** | **Description**  
`[OcrConfig.PremiumFeaturesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.OcrConfig.PremiumFeaturesOrBuilder)` |   
  
### hasHints()
    
    
    public abstract boolean hasHints()

Hints for the OCR model.

`.google.cloud.documentai.v1.OcrConfig.Hints hints = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hints field is set.  
  
### hasPremiumFeatures()
    
    
    public abstract boolean hasPremiumFeatures()

Configurations for premium OCR features.

`.google.cloud.documentai.v1.OcrConfig.PremiumFeatures premium_features = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the premiumFeatures field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
