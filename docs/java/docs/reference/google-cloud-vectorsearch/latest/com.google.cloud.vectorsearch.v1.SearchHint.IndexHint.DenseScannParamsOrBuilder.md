---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchHint.IndexHint.DenseScannParamsOrBuilder
title: Interface SearchHint.IndexHint.DenseScannParamsOrBuilder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:15.255329+00:00
---

# Interface SearchHint.IndexHint.DenseScannParamsOrBuilder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1.SearchHint.IndexHint.DenseScannParamsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchHint.IndexHint.DenseScannParamsOrBuilder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface SearchHint.IndexHint.DenseScannParamsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getTargetRecall()
    
    
    public abstract double getTargetRecall()

Optional. The target recall for the search. Must be a double in the range [0, 1]. While the search aims to achieve this level of recall, it is not guaranteed.

`optional double target_recall = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The targetRecall.  
  
### hasTargetRecall()
    
    
    public abstract boolean hasTargetRecall()

Optional. The target recall for the search. Must be a double in the range [0, 1]. While the search aims to achieve this level of recall, it is not guaranteed.

`optional double target_recall = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the targetRecall field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
