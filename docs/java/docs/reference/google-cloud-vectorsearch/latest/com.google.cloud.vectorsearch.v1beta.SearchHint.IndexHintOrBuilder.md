---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchHint.IndexHintOrBuilder
title: Interface SearchHint.IndexHintOrBuilder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:56.012286+00:00
---

# Interface SearchHint.IndexHintOrBuilder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchHint.IndexHintOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchHint.IndexHintOrBuilder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface SearchHint.IndexHintOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDenseScannParams()
    
    
    public abstract SearchHint.IndexHint.DenseScannParams getDenseScannParams()

Optional. Dense ScaNN parameters.

` .google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.DenseScannParams dense_scann_params = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchHint.IndexHint.DenseScannParams](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.DenseScannParams)` | The denseScannParams.  
  
### getDenseScannParamsOrBuilder()
    
    
    public abstract SearchHint.IndexHint.DenseScannParamsOrBuilder getDenseScannParamsOrBuilder()

Optional. Dense ScaNN parameters.

` .google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.DenseScannParams dense_scann_params = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchHint.IndexHint.DenseScannParamsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.DenseScannParamsOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the index to use for the search. The index must be in the same project, location, and collection. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the index to use for the search. The index must be in the same project, location, and collection. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParamsCase()
    
    
    public abstract SearchHint.IndexHint.ParamsCase getParamsCase()

**Returns**  
---  
**Type** | **Description**  
`[SearchHint.IndexHint.ParamsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.ParamsCase)` |   
  
### hasDenseScannParams()
    
    
    public abstract boolean hasDenseScannParams()

Optional. Dense ScaNN parameters.

` .google.cloud.vectorsearch.v1beta.SearchHint.IndexHint.DenseScannParams dense_scann_params = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the denseScannParams field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
