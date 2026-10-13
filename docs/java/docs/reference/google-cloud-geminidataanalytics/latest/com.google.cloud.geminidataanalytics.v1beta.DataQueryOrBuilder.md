---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.DataQueryOrBuilder
title: Interface DataQueryOrBuilder (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:28.044876+00:00
---

# Interface DataQueryOrBuilder (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.DataQueryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataQueryOrBuilder (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataQueryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDatasources(int index)
    
    
    public abstract Datasource getDatasources(int index)

Optional. The datasources available to answer the question.

` repeated .google.cloud.geminidataanalytics.v1beta.Datasource datasources = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Datasource](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Datasource)` |   
  
### getDatasourcesCount()
    
    
    public abstract int getDatasourcesCount()

Optional. The datasources available to answer the question.

` repeated .google.cloud.geminidataanalytics.v1beta.Datasource datasources = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDatasourcesList()
    
    
    public abstract List<Datasource> getDatasourcesList()

Optional. The datasources available to answer the question.

` repeated .google.cloud.geminidataanalytics.v1beta.Datasource datasources = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Datasource](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.Datasource)>` |   
  
### getDatasourcesOrBuilder(int index)
    
    
    public abstract DatasourceOrBuilder getDatasourcesOrBuilder(int index)

Optional. The datasources available to answer the question.

` repeated .google.cloud.geminidataanalytics.v1beta.Datasource datasources = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DatasourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.DatasourceOrBuilder)` |   
  
### getDatasourcesOrBuilderList()
    
    
    public abstract List<? extends DatasourceOrBuilder> getDatasourcesOrBuilderList()

Optional. The datasources available to answer the question.

` repeated .google.cloud.geminidataanalytics.v1beta.Datasource datasources = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.geminidataanalytics.v1beta.DatasourceOrBuilder>` |   
  
### getLooker()
    
    
    public abstract LookerQuery getLooker()

Optional. A query for retrieving data from a Looker explore.

` .google.cloud.geminidataanalytics.v1beta.LookerQuery looker = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LookerQuery](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.LookerQuery)` | The looker.  
  
### getLookerOrBuilder()
    
    
    public abstract LookerQueryOrBuilder getLookerOrBuilder()

Optional. A query for retrieving data from a Looker explore.

` .google.cloud.geminidataanalytics.v1beta.LookerQuery looker = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LookerQueryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.LookerQueryOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Optional. A snake-case name for the query that reflects its intent. It is used to name the corresponding data result, so that it can be referenced in later steps.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"



`string name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optional. A snake-case name for the query that reflects its intent. It is used to name the corresponding data result, so that it can be referenced in later steps.

  * Example: "total_sales_by_product"
  * Example: "sales_for_product_12345"



`string name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQueryTypeCase()
    
    
    public abstract DataQuery.QueryTypeCase getQueryTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[DataQuery.QueryTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1beta.DataQuery.QueryTypeCase)` |   
  
### getQuestion()
    
    
    public abstract String getQuestion()

Optional. A natural language question to answer.

`string question = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The question.  
  
### getQuestionBytes()
    
    
    public abstract ByteString getQuestionBytes()

Optional. A natural language question to answer.

`string question = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for question.  
  
### hasLooker()
    
    
    public abstract boolean hasLooker()

Optional. A query for retrieving data from a Looker explore.

` .google.cloud.geminidataanalytics.v1beta.LookerQuery looker = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the looker field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
