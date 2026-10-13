---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysResponseOrBuilder
title: Interface ListCustomTargetingKeysResponseOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:33.405360+00:00
---

# Interface ListCustomTargetingKeysResponseOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ListCustomTargetingKeysResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListCustomTargetingKeysResponseOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ListCustomTargetingKeysResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomTargetingKeys(int index)
    
    
    public abstract CustomTargetingKey getCustomTargetingKeys(int index)

The `CustomTargetingKey` objects from the specified network.

`repeated .google.ads.admanager.v1.CustomTargetingKey custom_targeting_keys = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)` |   
  
### getCustomTargetingKeysCount()
    
    
    public abstract int getCustomTargetingKeysCount()

The `CustomTargetingKey` objects from the specified network.

`repeated .google.ads.admanager.v1.CustomTargetingKey custom_targeting_keys = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCustomTargetingKeysList()
    
    
    public abstract List<CustomTargetingKey> getCustomTargetingKeysList()

The `CustomTargetingKey` objects from the specified network.

`repeated .google.ads.admanager.v1.CustomTargetingKey custom_targeting_keys = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[CustomTargetingKey](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKey)>` |   
  
### getCustomTargetingKeysOrBuilder(int index)
    
    
    public abstract CustomTargetingKeyOrBuilder getCustomTargetingKeysOrBuilder(int index)

The `CustomTargetingKey` objects from the specified network.

`repeated .google.ads.admanager.v1.CustomTargetingKey custom_targeting_keys = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CustomTargetingKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.CustomTargetingKeyOrBuilder)` |   
  
### getCustomTargetingKeysOrBuilderList()
    
    
    public abstract List<? extends CustomTargetingKeyOrBuilder> getCustomTargetingKeysOrBuilderList()

The `CustomTargetingKey` objects from the specified network.

`repeated .google.ads.admanager.v1.CustomTargetingKey custom_targeting_keys = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.CustomTargetingKeyOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getTotalSize()
    
    
    public abstract int getTotalSize()

Total number of `CustomTargetingKey` objects. If a filter was included in the request, this reflects the total number after the filtering is applied.

`total_size` won't be calculated in the response unless it has been included in a response field mask. The response field mask can be provided to the method by using the URL parameter `$fields` or `fields`, or by using the HTTP/gRPC header `X-Goog-FieldMask`.

For more information, see <https://developers.google.com/ad-manager/api/beta/field-masks>

`int32 total_size = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalSize.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
