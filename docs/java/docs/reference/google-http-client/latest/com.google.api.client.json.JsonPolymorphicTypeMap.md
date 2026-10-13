---
url: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonPolymorphicTypeMap
title: Annotation Type JsonPolymorphicTypeMap (2.2.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:15.540493+00:00
---

# Annotation Type JsonPolymorphicTypeMap (2.2.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonPolymorphicTypeMap

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Annotation Type JsonPolymorphicTypeMap (2.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.0 (latest)  2.1.1  2.0.3  1.47.1  1.46.3  1.45.3  1.44.2  1.43.2  1.42.3  1.41.8 
    
    
    public interface JsonPolymorphicTypeMap implements Annotation

[Beta](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Beta)   
Declares that the data type enclosing this field is polymorphic, and that the value of this field in a heterogeneous JSON schema will determine what type the data should be parsed into.

A data structure must have no more than one field with this annotation present. The annotated field's type must be considered "primitive" by [Data#isPrimitive(Type)](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Data#com_google_api_client_util_Data_isPrimitive_java_lang_reflect_Type_). The field's value will be compared against the [TypeDef#key()](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonPolymorphicTypeMap.TypeDef#com_google_api_client_json_JsonPolymorphicTypeMap_TypeDef_key_) using [Object#toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--).

## Implements

[Annotation](https://docs.oracle.com/javase/8/docs/api/java/lang/annotation/Annotation.html)

## Methods 

### typeDefinitions()
    
    
    public abstract JsonPolymorphicTypeMap.TypeDef[] typeDefinitions()

The list of mappings from key value to a referenced [Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html).

**Returns**  
---  
**Type** | **Description**  
`[TypeDef](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonPolymorphicTypeMap.TypeDef)[]` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-31 UTC."],[],[]] 
