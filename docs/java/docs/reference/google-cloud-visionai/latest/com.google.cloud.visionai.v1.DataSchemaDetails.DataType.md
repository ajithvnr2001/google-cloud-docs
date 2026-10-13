---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.DataType
title: Enum DataSchemaDetails.DataType (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:04.997626+00:00
---

# Enum DataSchemaDetails.DataType (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.DataType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Enum DataSchemaDetails.DataType (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public enum DataSchemaDetails.DataType extends Enum<DataSchemaDetails.DataType> implements ProtocolMessageEnum

Data type of the annotation.

Protobuf enum `google.cloud.visionai.v1.DataSchemaDetails.DataType`

## Implements

[ProtocolMessageEnum](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolMessageEnum.html)

## Inherited Members

[Enum.<T>valueOf(Class<T>,String)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#valueOf-java.lang.Class-java.lang.String-)

[Enum.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#clone--)

[Enum.compareTo(E)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#compareTo-E-)

[Enum.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#equals-java.lang.Object-)

[Enum.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#finalize--)

[Enum.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#getDeclaringClass--)

[Enum.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#hashCode--)

[Enum.name()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#name--)

[Enum.ordinal()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#ordinal--)

[Enum.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html#toString--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields   
  
---  
**Name** | **Description**  
`BOOLEAN` |  Boolean type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH.

`BOOLEAN = 9;`  
`BOOLEAN_VALUE` |  Boolean type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH.

`BOOLEAN = 9;`  
`CUSTOMIZED_STRUCT` |  Struct type.

  * SearchStrategy:
  * Data Schema that's CUSTOMIZED_STRUCT cannot set search strategy.
  * Leaf-node elements allow setting search strategy based on element's SearchStrategy restriction.
  * Nested layer restrictions:
  * Data Schema that's CUSTOMIZED_STRUCT allows its fields to be of CUSTOMIZED_STRUCT as well, but the overall layers restriction is 10.

`CUSTOMIZED_STRUCT = 6;`  
`CUSTOMIZED_STRUCT_VALUE` |  Struct type.

  * SearchStrategy:
  * Data Schema that's CUSTOMIZED_STRUCT cannot set search strategy.
  * Leaf-node elements allow setting search strategy based on element's SearchStrategy restriction.
  * Nested layer restrictions:
  * Data Schema that's CUSTOMIZED_STRUCT allows its fields to be of CUSTOMIZED_STRUCT as well, but the overall layers restriction is 10.

`CUSTOMIZED_STRUCT = 6;`  
`DATA_TYPE_UNSPECIFIED` |  Unspecified type. `DATA_TYPE_UNSPECIFIED = 0;`  
`DATA_TYPE_UNSPECIFIED_VALUE` |  Unspecified type. `DATA_TYPE_UNSPECIFIED = 0;`  
`DATETIME` |  Supported formats: %Y-%m-%dT%H:%M:%E _S%E_ z (absl::RFC3339_full) %Y-%m-%dT%H:%M:%E _S %Y-%m-%dT%H:%M%E_ z %Y-%m-%dT%H:%M %Y-%m-%dT%H%E _z %Y-%m-%dT%H %Y-%m-%d%E_ z %Y-%m-%d %Y-%m %Y Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by DateTimeRangeArray.

`DATETIME = 5;`  
`DATETIME_VALUE` |  Supported formats: %Y-%m-%dT%H:%M:%E _S%E_ z (absl::RFC3339_full) %Y-%m-%dT%H:%M:%E _S %Y-%m-%dT%H:%M%E_ z %Y-%m-%dT%H:%M %Y-%m-%dT%H%E _z %Y-%m-%dT%H %Y-%m-%d%E_ z %Y-%m-%d %Y-%m %Y Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by DateTimeRangeArray.

`DATETIME = 5;`  
`FLOAT` |  Float type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by FloatRangeArray.

`FLOAT = 2;`  
`FLOAT_VALUE` |  Float type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by FloatRangeArray.

`FLOAT = 2;`  
`GEO_COORDINATE` |  Geo coordinate type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by GeoLocationArray.

`GEO_COORDINATE = 7;`  
`GEO_COORDINATE_VALUE` |  Geo coordinate type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by GeoLocationArray.

`GEO_COORDINATE = 7;`  
`INTEGER` |  Integer type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by IntRangeArray.

`INTEGER = 1;`  
`INTEGER_VALUE` |  Integer type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH. Supports query by IntRangeArray.

`INTEGER = 1;`  
`LIST` |  List type.

  * Each element in the list must be of the exact same data schema; otherwise, they are invalid arguments.
  * List level cannot set search strategy. Leaf node level can do.
  * Elements cannot be another list (no list of list).
  * Elements can be CUSTOMIZED_STRUCT, and max number of layers is 10.

`LIST = 10;`  
`LIST_VALUE` |  List type.

  * Each element in the list must be of the exact same data schema; otherwise, they are invalid arguments.
  * List level cannot set search strategy. Leaf node level can do.
  * Elements cannot be another list (no list of list).
  * Elements can be CUSTOMIZED_STRUCT, and max number of layers is 10.

`LIST = 10;`  
`PROTO_ANY` |  Type to pass any proto as available in annotations.proto. Only use internally. Available proto types and its corresponding search behavior:

  * ImageObjectDetectionPredictionResult, allows SMART_SEARCH on display_names and NO_SEARCH.
  * ClassificationPredictionResult, allows SMART_SEARCH on display_names and NO_SEARCH.
  * ImageSegmentationPredictionResult, allows NO_SEARCH.
  * VideoActionRecognitionPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * VideoObjectTrackingPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * VideoClassificationPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * OccupancyCountingPredictionResult, allows EXACT_SEARCH on stats.full_frame_count.count and NO_SEARCH.
  * ObjectDetectionPredictionResult, allows SMART_SEARCH on identified_boxes.entity.label_string and NO_SEARCH.

`PROTO_ANY = 8;`  
`PROTO_ANY_VALUE` |  Type to pass any proto as available in annotations.proto. Only use internally. Available proto types and its corresponding search behavior:

  * ImageObjectDetectionPredictionResult, allows SMART_SEARCH on display_names and NO_SEARCH.
  * ClassificationPredictionResult, allows SMART_SEARCH on display_names and NO_SEARCH.
  * ImageSegmentationPredictionResult, allows NO_SEARCH.
  * VideoActionRecognitionPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * VideoObjectTrackingPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * VideoClassificationPredictionResult, allows SMART_SEARCH on display_name and NO_SEARCH.
  * OccupancyCountingPredictionResult, allows EXACT_SEARCH on stats.full_frame_count.count and NO_SEARCH.
  * ObjectDetectionPredictionResult, allows SMART_SEARCH on identified_boxes.entity.label_string and NO_SEARCH.

`PROTO_ANY = 8;`  
`STRING` |  String type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH,
  * DataSchema.SearchStrategy.SMART_SEARCH.

`STRING = 3;`  
`STRING_VALUE` |  String type. Allowed search strategies:

  * DataSchema.SearchStrategy.NO_SEARCH,
  * DataSchema.SearchStrategy.EXACT_SEARCH,
  * DataSchema.SearchStrategy.SMART_SEARCH.

`STRING = 3;`  
`UNRECOGNIZED` |   
  
## Static Methods   
  
---  
**Name** | **Description**  
`forNumber(int value)` |   
`getDescriptor()` |   
`internalGetValueMap()` |   
`valueOf(Descriptors.EnumValueDescriptor desc)` |   
`valueOf(int value)` | **Deprecated.** _Use[#forNumber(int)](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.DataSchemaDetails.DataType#com_google_cloud_visionai_v1_DataSchemaDetails_DataType_forNumber_int_) instead._  
`valueOf(String name)` |   
`values()` |   
  
## Methods   
  
---  
**Name** | **Description**  
`getDescriptorForType()` |   
`getNumber()` |   
`getValueDescriptor()` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
