---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.FeaturesOrBuilder
title: Interface AnnotateTextRequest.FeaturesOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:06.866318+00:00
---

# Interface AnnotateTextRequest.FeaturesOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.FeaturesOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnnotateTextRequest.FeaturesOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 
    
    
    public static interface AnnotateTextRequest.FeaturesOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClassificationModelOptions()
    
    
    public abstract ClassificationModelOptions getClassificationModelOptions()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationModelOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions)` | The classificationModelOptions.  
  
### getClassificationModelOptionsOrBuilder()
    
    
    public abstract ClassificationModelOptionsOrBuilder getClassificationModelOptionsOrBuilder()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationModelOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptionsOrBuilder)` |   
  
### getClassifyText()
    
    
    public abstract boolean getClassifyText()

Classify the full document into categories. If this is true, the API will use the default model which classifies into a [predefined taxonomy](https://cloud.google.com/natural-language/docs/categories).

`bool classify_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The classifyText.  
  
### getExtractDocumentSentiment()
    
    
    public abstract boolean getExtractDocumentSentiment()

Extract document-level sentiment.

`bool extract_document_sentiment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractDocumentSentiment.  
  
### getExtractEntities()
    
    
    public abstract boolean getExtractEntities()

Extract entities.

`bool extract_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractEntities.  
  
### getExtractEntitySentiment()
    
    
    public abstract boolean getExtractEntitySentiment()

Extract entities and their associated sentiment.

`bool extract_entity_sentiment = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractEntitySentiment.  
  
### getExtractSyntax()
    
    
    public abstract boolean getExtractSyntax()

Extract syntax information.

`bool extract_syntax = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractSyntax.  
  
### getModerateText()
    
    
    public abstract boolean getModerateText()

Moderate the document for harmful and sensitive categories.

`bool moderate_text = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The moderateText.  
  
### hasClassificationModelOptions()
    
    
    public abstract boolean hasClassificationModelOptions()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the classificationModelOptions field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
