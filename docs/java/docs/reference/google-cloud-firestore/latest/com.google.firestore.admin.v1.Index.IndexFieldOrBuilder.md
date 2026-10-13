---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexFieldOrBuilder
title: Interface Index.IndexFieldOrBuilder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:39.038629+00:00
---

# Interface Index.IndexFieldOrBuilder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexFieldOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Index.IndexFieldOrBuilder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public static interface Index.IndexFieldOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArrayConfig()
    
    
    public abstract Index.IndexField.ArrayConfig getArrayConfig()

Indicates that this field supports operations on `array_value`s.

`.google.firestore.admin.v1.Index.IndexField.ArrayConfig array_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.ArrayConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.ArrayConfig)` | The arrayConfig.  
  
### getArrayConfigValue()
    
    
    public abstract int getArrayConfigValue()

Indicates that this field supports operations on `array_value`s.

`.google.firestore.admin.v1.Index.IndexField.ArrayConfig array_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for arrayConfig.  
  
### getFieldPath()
    
    
    public abstract String getFieldPath()

Can be **name**. For single field indexes, this must match the name of the field or may be omitted.

`string field_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fieldPath.  
  
### getFieldPathBytes()
    
    
    public abstract ByteString getFieldPathBytes()

Can be **name**. For single field indexes, this must match the name of the field or may be omitted.

`string field_path = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fieldPath.  
  
### getOrder()
    
    
    public abstract Index.IndexField.Order getOrder()

Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.

`.google.firestore.admin.v1.Index.IndexField.Order order = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.Order)` | The order.  
  
### getOrderValue()
    
    
    public abstract int getOrderValue()

Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.

`.google.firestore.admin.v1.Index.IndexField.Order order = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for order.  
  
### getSearchConfig()
    
    
    public abstract Index.IndexField.SearchConfig getSearchConfig()

Indicates that this field supports search operations. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope.

`.google.firestore.admin.v1.Index.IndexField.SearchConfig search_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.SearchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.SearchConfig)` | The searchConfig.  
  
### getSearchConfigOrBuilder()
    
    
    public abstract Index.IndexField.SearchConfigOrBuilder getSearchConfigOrBuilder()

Indicates that this field supports search operations. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope.

`.google.firestore.admin.v1.Index.IndexField.SearchConfig search_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.SearchConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.SearchConfigOrBuilder)` |   
  
### getValueModeCase()
    
    
    public abstract Index.IndexField.ValueModeCase getValueModeCase()

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.ValueModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.ValueModeCase)` |   
  
### getVectorConfig()
    
    
    public abstract Index.IndexField.VectorConfig getVectorConfig()

Indicates that this field supports nearest neighbor and distance operations on vector.

`.google.firestore.admin.v1.Index.IndexField.VectorConfig vector_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.VectorConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.VectorConfig)` | The vectorConfig.  
  
### getVectorConfigOrBuilder()
    
    
    public abstract Index.IndexField.VectorConfigOrBuilder getVectorConfigOrBuilder()

Indicates that this field supports nearest neighbor and distance operations on vector.

`.google.firestore.admin.v1.Index.IndexField.VectorConfig vector_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Index.IndexField.VectorConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.admin.v1.Index.IndexField.VectorConfigOrBuilder)` |   
  
### hasArrayConfig()
    
    
    public abstract boolean hasArrayConfig()

Indicates that this field supports operations on `array_value`s.

`.google.firestore.admin.v1.Index.IndexField.ArrayConfig array_config = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrayConfig field is set.  
  
### hasOrder()
    
    
    public abstract boolean hasOrder()

Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.

`.google.firestore.admin.v1.Index.IndexField.Order order = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the order field is set.  
  
### hasSearchConfig()
    
    
    public abstract boolean hasSearchConfig()

Indicates that this field supports search operations. This field is only currently supported for indexes with MONGODB_COMPATIBLE_API ApiScope.

`.google.firestore.admin.v1.Index.IndexField.SearchConfig search_config = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the searchConfig field is set.  
  
### hasVectorConfig()
    
    
    public abstract boolean hasVectorConfig()

Indicates that this field supports nearest neighbor and distance operations on vector.

`.google.firestore.admin.v1.Index.IndexField.VectorConfig vector_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vectorConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
