---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1beta.DataSourceReferenceOrBuilder
title: Interface DataSourceReferenceOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:56.660579+00:00
---

# Interface DataSourceReferenceOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1beta.DataSourceReferenceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSourceReferenceOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataSourceReferenceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDataSourceIdCase()
    
    
    public abstract DataSourceReference.DataSourceIdCase getDataSourceIdCase()

**Returns**  
---  
**Type** | **Description**  
`[DataSourceReference.DataSourceIdCase](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-datasources/latest/com.google.shopping.merchant.datasources.v1beta.DataSourceReference.DataSourceIdCase)` |   
  
### getPrimaryDataSourceName()
    
    
    public abstract String getPrimaryDataSourceName()

Optional. The name of the primary data source. Format: `accounts/{account}/dataSources/{datasource}`

`string primary_data_source_name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The primaryDataSourceName.  
  
### getPrimaryDataSourceNameBytes()
    
    
    public abstract ByteString getPrimaryDataSourceNameBytes()

Optional. The name of the primary data source. Format: `accounts/{account}/dataSources/{datasource}`

`string primary_data_source_name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for primaryDataSourceName.  
  
### getSelf()
    
    
    public abstract boolean getSelf()

Self should be used to reference the primary data source itself.

`bool self = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The self.  
  
### getSupplementalDataSourceName()
    
    
    public abstract String getSupplementalDataSourceName()

Optional. The name of the supplemental data source. Format: `accounts/{account}/dataSources/{datasource}`

`string supplemental_data_source_name = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The supplementalDataSourceName.  
  
### getSupplementalDataSourceNameBytes()
    
    
    public abstract ByteString getSupplementalDataSourceNameBytes()

Optional. The name of the supplemental data source. Format: `accounts/{account}/dataSources/{datasource}`

`string supplemental_data_source_name = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for supplementalDataSourceName.  
  
### hasPrimaryDataSourceName()
    
    
    public abstract boolean hasPrimaryDataSourceName()

Optional. The name of the primary data source. Format: `accounts/{account}/dataSources/{datasource}`

`string primary_data_source_name = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the primaryDataSourceName field is set.  
  
### hasSelf()
    
    
    public abstract boolean hasSelf()

Self should be used to reference the primary data source itself.

`bool self = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the self field is set.  
  
### hasSupplementalDataSourceName()
    
    
    public abstract boolean hasSupplementalDataSourceName()

Optional. The name of the supplemental data source. Format: `accounts/{account}/dataSources/{datasource}`

`string supplemental_data_source_name = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the supplementalDataSourceName field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
