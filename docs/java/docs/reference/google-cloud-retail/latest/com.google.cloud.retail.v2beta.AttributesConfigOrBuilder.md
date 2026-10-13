---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfigOrBuilder
title: Interface AttributesConfigOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:41.683303+00:00
---

# Interface AttributesConfigOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AttributesConfigOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public interface AttributesConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsCatalogAttributes(String key)
    
    
    public abstract boolean containsCatalogAttributes(String key)

Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute.

The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.

The maximum number of catalog attributes allowed in a request is 1000.

`map<string, .google.cloud.retail.v2beta.CatalogAttribute> catalog_attributes = 2; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributeConfigLevel()
    
    
    public abstract AttributeConfigLevel getAttributeConfigLevel()

Output only. The AttributeConfigLevel used for this catalog.

` .google.cloud.retail.v2beta.AttributeConfigLevel attribute_config_level = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AttributeConfigLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributeConfigLevel)` | The attributeConfigLevel.  
  
### getAttributeConfigLevelValue()
    
    
    public abstract int getAttributeConfigLevelValue()

Output only. The AttributeConfigLevel used for this catalog.

` .google.cloud.retail.v2beta.AttributeConfigLevel attribute_config_level = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for attributeConfigLevel.  
  
### getCatalogAttributes() (deprecated)
    
    
    public abstract Map<String,CatalogAttribute> getCatalogAttributes()

Use [#getCatalogAttributesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.AttributesConfigOrBuilder#com_google_cloud_retail_v2beta_AttributesConfigOrBuilder_getCatalogAttributesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[CatalogAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogAttribute)>` |   
  
### getCatalogAttributesCount()
    
    
    public abstract int getCatalogAttributesCount()

Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute.

The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.

The maximum number of catalog attributes allowed in a request is 1000.

`map<string, .google.cloud.retail.v2beta.CatalogAttribute> catalog_attributes = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCatalogAttributesMap()
    
    
    public abstract Map<String,CatalogAttribute> getCatalogAttributesMap()

Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute.

The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.

The maximum number of catalog attributes allowed in a request is 1000.

`map<string, .google.cloud.retail.v2beta.CatalogAttribute> catalog_attributes = 2; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[CatalogAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogAttribute)>` |   
  
### getCatalogAttributesOrDefault(String key, CatalogAttribute defaultValue)
    
    
    public abstract CatalogAttribute getCatalogAttributesOrDefault(String key, CatalogAttribute defaultValue)

Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute.

The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.

The maximum number of catalog attributes allowed in a request is 1000.

`map<string, .google.cloud.retail.v2beta.CatalogAttribute> catalog_attributes = 2; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[CatalogAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogAttribute)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogAttribute)` |   
  
### getCatalogAttributesOrThrow(String key)
    
    
    public abstract CatalogAttribute getCatalogAttributesOrThrow(String key)

Enable attribute(s) config at catalog level. For example, indexable, dynamic_facetable, or searchable for each attribute.

The key is catalog attribute's name. For example: `color`, `brands`, `attributes.custom_attribute`, such as `attributes.xyz`.

The maximum number of catalog attributes allowed in a request is 1000.

`map<string, .google.cloud.retail.v2beta.CatalogAttribute> catalog_attributes = 2; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CatalogAttribute](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2beta.CatalogAttribute)` |   
  
### getName()
    
    
    public abstract String getName()

Required. Immutable. The fully qualified resource name of the attribute config. Format: `projects/*/locations/*/catalogs/*/attributesConfig`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Immutable. The fully qualified resource name of the attribute config. Format: `projects/*/locations/*/catalogs/*/attributesConfig`

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
