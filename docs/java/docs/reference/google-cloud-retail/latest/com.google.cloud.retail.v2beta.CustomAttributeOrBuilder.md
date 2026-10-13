---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CustomAttributeOrBuilder
title: Interface CustomAttributeOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:03.492926+00:00
---

# Interface CustomAttributeOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CustomAttributeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomAttributeOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public interface CustomAttributeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIndexable() (deprecated)
    
    
    public abstract boolean getIndexable()

**Deprecated.** _google.cloud.retail.v2beta.CustomAttribute.indexable is deprecated. See google/cloud/retail/v2beta/common.proto;l=582_

This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in SearchService.Search.

This field is ignored in a UserEvent.

See SearchRequest.filter, SearchRequest.facet_specs and SearchRequest.boost_spec for more details.

`optional bool indexable = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The indexable.  
  
### getNumbers(int index)
    
    
    public abstract double getNumbers(int index)

The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated double numbers = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numbers at the given index.  
  
### getNumbersCount()
    
    
    public abstract int getNumbersCount()

The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated double numbers = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of numbers.  
  
### getNumbersList()
    
    
    public abstract List<Double> getNumbersList()

The numerical values of this custom attribute. For example, `[2.3, 15.4]` when the key is "lengths_cm".

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated double numbers = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Double](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html)>` | A list containing the numbers.  
  
### getSearchable() (deprecated)
    
    
    public abstract boolean getSearchable()

**Deprecated.** _google.cloud.retail.v2beta.CustomAttribute.searchable is deprecated. See google/cloud/retail/v2beta/common.proto;l=561_

This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in SearchService.Search.

This field is ignored in a UserEvent.

Only set if type text is set. Otherwise, a INVALID_ARGUMENT error is returned.

`optional bool searchable = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The searchable.  
  
### getText(int index)
    
    
    public abstract String getText(int index)

The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".

Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated string text = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text at the given index.  
  
### getTextBytes(int index)
    
    
    public abstract ByteString getTextBytes(int index)

The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".

Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated string text = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the text at the given index.  
  
### getTextCount()
    
    
    public abstract int getTextCount()

The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".

Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of text.  
  
### getTextList()
    
    
    public abstract List<String> getTextList()

The textual values of this custom attribute. For example, `["yellow", "green"]` when the key is "color".

Empty string is not allowed. Otherwise, an INVALID_ARGUMENT error is returned.

Exactly one of text or numbers should be set. Otherwise, an INVALID_ARGUMENT error is returned.

`repeated string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the text.  
  
### hasIndexable() (deprecated)
    
    
    public abstract boolean hasIndexable()

**Deprecated.** _google.cloud.retail.v2beta.CustomAttribute.indexable is deprecated. See google/cloud/retail/v2beta/common.proto;l=582_

This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are indexed, so that they can be filtered, faceted or boosted in SearchService.Search.

This field is ignored in a UserEvent.

See SearchRequest.filter, SearchRequest.facet_specs and SearchRequest.boost_spec for more details.

`optional bool indexable = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the indexable field is set.  
  
### hasSearchable() (deprecated)
    
    
    public abstract boolean hasSearchable()

**Deprecated.** _google.cloud.retail.v2beta.CustomAttribute.searchable is deprecated. See google/cloud/retail/v2beta/common.proto;l=561_

This field is normally ignored unless AttributesConfig.attribute_config_level of the Catalog is set to the deprecated 'PRODUCT_LEVEL_ATTRIBUTE_CONFIG' mode. For information about product-level attribute configuration, see [Configuration modes](https://cloud.google.com/retail/docs/attribute-config#config-modes). If true, custom attribute values are searchable by text queries in SearchService.Search.

This field is ignored in a UserEvent.

Only set if type text is set. Otherwise, a INVALID_ARGUMENT error is returned.

`optional bool searchable = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the searchable field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
