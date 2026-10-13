---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdMediaDeliveryConfigOrBuilder
title: Interface AdMediaDeliveryConfigOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:55.813335+00:00
---

# Interface AdMediaDeliveryConfigOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AdMediaDeliveryConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AdMediaDeliveryConfigOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AdMediaDeliveryConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalDeliverySettings(int index)
    
    
    public abstract MediaLocation getAdditionalDeliverySettings(int index)

Optional. List of additional delivery locations. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. In your stream create request, you can set the value of the `dai-dlid` parameter to the name of the MediaLocation you want to use.

` repeated .google.ads.admanager.v1.MediaLocation additional_delivery_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaLocation](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MediaLocation)` |   
  
### getAdditionalDeliverySettingsCount()
    
    
    public abstract int getAdditionalDeliverySettingsCount()

Optional. List of additional delivery locations. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. In your stream create request, you can set the value of the `dai-dlid` parameter to the name of the MediaLocation you want to use.

` repeated .google.ads.admanager.v1.MediaLocation additional_delivery_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdditionalDeliverySettingsList()
    
    
    public abstract List<MediaLocation> getAdditionalDeliverySettingsList()

Optional. List of additional delivery locations. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. In your stream create request, you can set the value of the `dai-dlid` parameter to the name of the MediaLocation you want to use.

` repeated .google.ads.admanager.v1.MediaLocation additional_delivery_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MediaLocation](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MediaLocation)>` |   
  
### getAdditionalDeliverySettingsOrBuilder(int index)
    
    
    public abstract MediaLocationOrBuilder getAdditionalDeliverySettingsOrBuilder(int index)

Optional. List of additional delivery locations. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. In your stream create request, you can set the value of the `dai-dlid` parameter to the name of the MediaLocation you want to use.

` repeated .google.ads.admanager.v1.MediaLocation additional_delivery_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MediaLocationOrBuilder)` |   
  
### getAdditionalDeliverySettingsOrBuilderList()
    
    
    public abstract List<? extends MediaLocationOrBuilder> getAdditionalDeliverySettingsOrBuilderList()

Optional. List of additional delivery locations. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. In your stream create request, you can set the value of the `dai-dlid` parameter to the name of the MediaLocation you want to use.

` repeated .google.ads.admanager.v1.MediaLocation additional_delivery_settings = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.ads.admanager.v1.MediaLocationOrBuilder>` |   
  
### getDeliverySettings()
    
    
    public abstract MediaLocation getDeliverySettings()

Optional. Config for the delivery location that will override the default. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. Null if `overrideDefaultDeliverySettings` is false.

` .google.ads.admanager.v1.MediaLocation delivery_settings = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MediaLocation](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MediaLocation)` | The deliverySettings.  
  
### getDeliverySettingsOrBuilder()
    
    
    public abstract MediaLocationOrBuilder getDeliverySettingsOrBuilder()

Optional. Config for the delivery location that will override the default. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. Null if `overrideDefaultDeliverySettings` is false.

` .google.ads.admanager.v1.MediaLocation delivery_settings = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MediaLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.MediaLocationOrBuilder)` |   
  
### getOverrideDefaultDeliverySettings()
    
    
    public abstract boolean getOverrideDefaultDeliverySettings()

Optional. Whether to override the default delivery CDN. If false, `deliverySettings` must be null.

` optional bool override_default_delivery_settings = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The overrideDefaultDeliverySettings.  
  
### hasDeliverySettings()
    
    
    public abstract boolean hasDeliverySettings()

Optional. Config for the delivery location that will override the default. From MediaLocationDto, the URL prefix field represents the hostname of the external CDN and the security policy will be ignored. Null if `overrideDefaultDeliverySettings` is false.

` .google.ads.admanager.v1.MediaLocation delivery_settings = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deliverySettings field is set.  
  
### hasOverrideDefaultDeliverySettings()
    
    
    public abstract boolean hasOverrideDefaultDeliverySettings()

Optional. Whether to override the default delivery CDN. If false, `deliverySettings` must be null.

` optional bool override_default_delivery_settings = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the overrideDefaultDeliverySettings field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
