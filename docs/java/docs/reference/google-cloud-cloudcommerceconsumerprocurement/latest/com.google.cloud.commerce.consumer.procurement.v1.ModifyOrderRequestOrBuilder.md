---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequestOrBuilder
title: Interface ModifyOrderRequestOrBuilder (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:46.998437+00:00
---

# Interface ModifyOrderRequestOrBuilder (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModifyOrderRequestOrBuilder (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public interface ModifyOrderRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. Updated display name of the order, leave as empty if you do not want to update current display name.

`string display_name = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. Updated display name of the order, leave as empty if you do not want to update current display name.

`string display_name = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. The weak etag, which can be optionally populated, of the order that this modify request is based on. Validation checking will only happen if the invoker supplies this field.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. The weak etag, which can be optionally populated, of the order that this modify request is based on. Validation checking will only happen if the invoker supplies this field.

`string etag = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getModifications(int index)
    
    
    public abstract ModifyOrderRequest.Modification getModifications(int index)

Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.

` repeated .google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification modifications = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModifyOrderRequest.Modification](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification)` |   
  
### getModificationsCount()
    
    
    public abstract int getModificationsCount()

Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.

` repeated .google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification modifications = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getModificationsList()
    
    
    public abstract List<ModifyOrderRequest.Modification> getModificationsList()

Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.

` repeated .google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification modifications = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Modification](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification)>` |   
  
### getModificationsOrBuilder(int index)
    
    
    public abstract ModifyOrderRequest.ModificationOrBuilder getModificationsOrBuilder(int index)

Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.

` repeated .google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification modifications = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModifyOrderRequest.ModificationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.ModificationOrBuilder)` |   
  
### getModificationsOrBuilderList()
    
    
    public abstract List<? extends ModifyOrderRequest.ModificationOrBuilder> getModificationsOrBuilderList()

Optional. Modifications for an existing Order created by an Offer. Required when Offer based Order is being modified, except for when going from an offer to a public plan.

` repeated .google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.Modification modifications = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.commerce.consumer.procurement.v1.ModifyOrderRequest.ModificationOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Required. Name of the order to update.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Name of the order to update.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
