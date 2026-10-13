---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.PinActionOrBuilder
title: Interface Rule.PinActionOrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:31.278578+00:00
---

# Interface Rule.PinActionOrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.PinActionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Rule.PinActionOrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public static interface Rule.PinActionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsPinMap(long key)
    
    
    public abstract boolean containsPinMap(long key)

Required. A map of positions to product_ids.

Partial matches per action are allowed, if a certain position in the map is already filled that `[position, product_id]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.

Duplicate product_ids are not permitted within a single pin map.

The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).

`map<int64, string> pin_map = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPinMap() (deprecated)
    
    
    public abstract Map<Long,String> getPinMap()

Use [#getPinMapMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.PinActionOrBuilder#com_google_cloud_retail_v2_Rule_PinActionOrBuilder_getPinMapMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<java.lang.Long,[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getPinMapCount()
    
    
    public abstract int getPinMapCount()

Required. A map of positions to product_ids.

Partial matches per action are allowed, if a certain position in the map is already filled that `[position, product_id]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.

Duplicate product_ids are not permitted within a single pin map.

The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).

`map<int64, string> pin_map = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPinMapMap()
    
    
    public abstract Map<Long,String> getPinMapMap()

Required. A map of positions to product_ids.

Partial matches per action are allowed, if a certain position in the map is already filled that `[position, product_id]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.

Duplicate product_ids are not permitted within a single pin map.

The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).

`map<int64, string> pin_map = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<java.lang.Long,[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getPinMapOrDefault(long key, String defaultValue)
    
    
    public abstract String getPinMapOrDefault(long key, String defaultValue)

Required. A map of positions to product_ids.

Partial matches per action are allowed, if a certain position in the map is already filled that `[position, product_id]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.

Duplicate product_ids are not permitted within a single pin map.

The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).

`map<int64, string> pin_map = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getPinMapOrThrow(long key)
    
    
    public abstract String getPinMapOrThrow(long key)

Required. A map of positions to product_ids.

Partial matches per action are allowed, if a certain position in the map is already filled that `[position, product_id]` pair will be ignored but the rest may still be applied. This case will only occur if multiple pin actions are matched to a single request, as the map guarantees that pin positions are unique within the same action.

Duplicate product_ids are not permitted within a single pin map.

The max size of this map is 120, equivalent to the max [request page size](https://cloud.google.com/retail/docs/reference/rest/v2/projects.locations.catalogs.placements/search#request-body).

`map<int64, string> pin_map = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
