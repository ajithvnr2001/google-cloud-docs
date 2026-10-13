---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder
title: Interface SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:49.618142+00:00
---

# Interface SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface SearchRequest.BoostSpec.ConditionBoostSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBoost()
    
    
    public abstract float getBoost()

Strength of the condition boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.

Setting to 1.0 gives the document a big promotion. However, it does not necessarily mean that the boosted document will be the top result at all times, nor that other documents will be excluded. Results could still be shown even when none of them matches the condition. And results that are significantly more relevant to the search query can still trump your heavily favored but irrelevant documents.

Setting to -1.0 gives the document a big demotion. However, results that are deeply relevant might still be shown. The document will have an upstream battle to get a fairly high ranking, but it is not blocked out completely.

Setting to 0.0 means no boost applied. The boosting condition is ignored. Only one of the (condition, boost) combination or the boost_control_spec below are set. If both are set then the global boost is ignored and the more fine-grained boost_control_spec is applied.

`float boost = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The boost.  
  
### getBoostControlSpec()
    
    
    public abstract SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec getBoostControlSpec()

Complex specification for custom ranking based on customer defined attribute value.

` .google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec boost_control_spec = 3; `

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec)` | The boostControlSpec.  
  
### getBoostControlSpecOrBuilder()
    
    
    public abstract SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpecOrBuilder getBoostControlSpecOrBuilder()

Complex specification for custom ranking based on customer defined attribute value.

` .google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec boost_control_spec = 3; `

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpecOrBuilder)` |   
  
### getCondition()
    
    
    public abstract String getCondition()

An expression which specifies a boost condition. The syntax and supported fields are the same as a filter expression. See SearchRequest.filter for detail syntax and limitations.

Examples:

  * To boost documents with document ID "doc_1" or "doc_2", and color "Red" or "Blue": `(document_id: ANY("doc_1", "doc_2")) AND (color: ANY("Red", "Blue"))`



`string condition = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The condition.  
  
### getConditionBytes()
    
    
    public abstract ByteString getConditionBytes()

An expression which specifies a boost condition. The syntax and supported fields are the same as a filter expression. See SearchRequest.filter for detail syntax and limitations.

Examples:

  * To boost documents with document ID "doc_1" or "doc_2", and color "Red" or "Blue": `(document_id: ANY("doc_1", "doc_2")) AND (color: ANY("Red", "Blue"))`



`string condition = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for condition.  
  
### hasBoostControlSpec()
    
    
    public abstract boolean hasBoostControlSpec()

Complex specification for custom ranking based on customer defined attribute value.

` .google.cloud.discoveryengine.v1.SearchRequest.BoostSpec.ConditionBoostSpec.BoostControlSpec boost_control_spec = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boostControlSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
