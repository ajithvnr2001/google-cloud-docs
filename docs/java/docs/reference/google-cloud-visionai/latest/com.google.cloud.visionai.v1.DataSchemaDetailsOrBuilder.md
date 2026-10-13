---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetailsOrBuilder
title: Interface DataSchemaDetailsOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:27.688850+00:00
---

# Interface DataSchemaDetailsOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataSchemaDetailsOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DataSchemaDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomizedStructConfig()
    
    
    public abstract DataSchemaDetails.CustomizedStructConfig getCustomizedStructConfig()

Config for CustomizedStruct data type.

` .google.cloud.visionai.v1.DataSchemaDetails.CustomizedStructConfig customized_struct_config = 9; `

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.CustomizedStructConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.CustomizedStructConfig)` | The customizedStructConfig.  
  
### getCustomizedStructConfigOrBuilder()
    
    
    public abstract DataSchemaDetails.CustomizedStructConfigOrBuilder getCustomizedStructConfigOrBuilder()

Config for CustomizedStruct data type.

` .google.cloud.visionai.v1.DataSchemaDetails.CustomizedStructConfig customized_struct_config = 9; `

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.CustomizedStructConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.CustomizedStructConfigOrBuilder)` |   
  
### getGranularity()
    
    
    public abstract DataSchemaDetails.Granularity getGranularity()

The granularity associated with this DataSchema.

`optional .google.cloud.visionai.v1.DataSchemaDetails.Granularity granularity = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.Granularity](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.Granularity)` | The granularity.  
  
### getGranularityValue()
    
    
    public abstract int getGranularityValue()

The granularity associated with this DataSchema.

`optional .google.cloud.visionai.v1.DataSchemaDetails.Granularity granularity = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for granularity.  
  
### getListConfig()
    
    
    public abstract DataSchemaDetails.ListConfig getListConfig()

Config for List data type.

`.google.cloud.visionai.v1.DataSchemaDetails.ListConfig list_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.ListConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.ListConfig)` | The listConfig.  
  
### getListConfigOrBuilder()
    
    
    public abstract DataSchemaDetails.ListConfigOrBuilder getListConfigOrBuilder()

Config for List data type.

`.google.cloud.visionai.v1.DataSchemaDetails.ListConfig list_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.ListConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.ListConfigOrBuilder)` |   
  
### getProtoAnyConfig()
    
    
    public abstract DataSchemaDetails.ProtoAnyConfig getProtoAnyConfig()

Config for protobuf any type.

`.google.cloud.visionai.v1.DataSchemaDetails.ProtoAnyConfig proto_any_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.ProtoAnyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.ProtoAnyConfig)` | The protoAnyConfig.  
  
### getProtoAnyConfigOrBuilder()
    
    
    public abstract DataSchemaDetails.ProtoAnyConfigOrBuilder getProtoAnyConfigOrBuilder()

Config for protobuf any type.

`.google.cloud.visionai.v1.DataSchemaDetails.ProtoAnyConfig proto_any_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.ProtoAnyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.ProtoAnyConfigOrBuilder)` |   
  
### getSearchStrategy()
    
    
    public abstract DataSchemaDetails.SearchStrategy getSearchStrategy()

The search strategy to be applied on the `key` above.

`.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy search_strategy = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.SearchStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy)` | The searchStrategy.  
  
### getSearchStrategyOrBuilder()
    
    
    public abstract DataSchemaDetails.SearchStrategyOrBuilder getSearchStrategyOrBuilder()

The search strategy to be applied on the `key` above.

`.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy search_strategy = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.SearchStrategyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategyOrBuilder)` |   
  
### getType()
    
    
    public abstract DataSchemaDetails.DataType getType()

Type of the annotation.

`optional .google.cloud.visionai.v1.DataSchemaDetails.DataType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DataSchemaDetails.DataType](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.DataType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Type of the annotation.

`optional .google.cloud.visionai.v1.DataSchemaDetails.DataType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasCustomizedStructConfig()
    
    
    public abstract boolean hasCustomizedStructConfig()

Config for CustomizedStruct data type.

` .google.cloud.visionai.v1.DataSchemaDetails.CustomizedStructConfig customized_struct_config = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customizedStructConfig field is set.  
  
### hasGranularity()
    
    
    public abstract boolean hasGranularity()

The granularity associated with this DataSchema.

`optional .google.cloud.visionai.v1.DataSchemaDetails.Granularity granularity = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the granularity field is set.  
  
### hasListConfig()
    
    
    public abstract boolean hasListConfig()

Config for List data type.

`.google.cloud.visionai.v1.DataSchemaDetails.ListConfig list_config = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the listConfig field is set.  
  
### hasProtoAnyConfig()
    
    
    public abstract boolean hasProtoAnyConfig()

Config for protobuf any type.

`.google.cloud.visionai.v1.DataSchemaDetails.ProtoAnyConfig proto_any_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the protoAnyConfig field is set.  
  
### hasSearchStrategy()
    
    
    public abstract boolean hasSearchStrategy()

The search strategy to be applied on the `key` above.

`.google.cloud.visionai.v1.DataSchemaDetails.SearchStrategy search_strategy = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the searchStrategy field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

Type of the annotation.

`optional .google.cloud.visionai.v1.DataSchemaDetails.DataType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
